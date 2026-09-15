# map-tooling residual harden Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Close the three Phase 21 residual holes on the capability-map tooling flow: WR-01 cluster-name forbidden-character rejection plus renderer pipe escape, WR-02 rules-vs-map `generated_on` fidelity check, WR-03 md freshness gate in generator `--check`.

**Architecture:** Three small edits on surfaces Phase 21 already owns, plus one assert-based probe file in the house style of `tooling/test_link_policy.py`. Validation fires inside `generate_map` before any write, so the clean tree stays byte-stable green. `check_release.py` gets zero edits: its step 5f picks up the checker-side gates and step 5g propagates the new `--check` return code.

**Tech Stack:** Python 3 stdlib only (json, re, sys, pathlib, argparse, datetime, tempfile, io, contextlib). No pytest, no test framework. Local runner is `python` on Windows Git Bash.

**Spec:** `docs/superpowers/specs/2026-09-14-map-tooling-residual-harden.md`

## Global Constraints

- Stdlib only. No new third-party imports anywhere.
- Zero edits to `tooling/check_release.py`. The spec forbids them; steps 5f/5g pick up the new gates through existing invocations.
- Zero edits to `.github/workflows/validate.yml` and no CI changes of any kind.
- No schema changes: `cluster_names` stays `list[str]`; both JSON files keep the single `generated_on` field; `disk_on` stays a check_release local.
- Leading and trailing whitespace in cluster names stay legal (spec Non-goals). No `_deslop` on cluster names; em dashes stay legal in names.
- H-07: sibling checkers never import the generator. The forbidden-character check is duplicated in the two files by design, same as the existing duplicated shape checks.
- Validation must fire before any write: `main()` calls `generate_map` before either file write, so a `ValueError` leaves `docs/capability-pack-map.json` and `docs/capability-pack-map.md` untouched on every mode.
- Byte-stability: on the clean tree every gate must pass with no doc file changing. Verified at HEAD `35c5e3adb34974fa9933232343c064d39f7fdfa9`: 32 cluster names, rules and map `generated_on` both `2026-08-27`, none carry the rejected characters.
- No pytest, no fixtures framework. Probe file is plain asserts with `main() -> int`.
- Commit style: lowercase prefix matching repo history (`tooling: ...`).

## Codebase context

Data flow (context gate, re-verified on live code): `docs/classification-rules.json` plus `docs/capability-pack-map-note-overrides.json` feed `generate_map()`, which writes `docs/capability-pack-map.json` (schema 2) and, with `--sync-md`, rewrites the Summary and cluster tables in `docs/capability-pack-map.md` while preserving the on-disk header verbatim up to `## Summary` (`_split_md_header`).

Surfaces and verified line refs (current tree, HEAD `35c5e3a`):

| File | Lines | Role |
|------|-------|------|
| `tooling/generate_capability_map.py` | L32-36 module constants; L77-83 cluster_names shape check; L84 `cluster_name_set`; L245-276 `render_md` (name injected unescaped at L260 and L265; pipe-escape precedent on pack/chapter/note at L270-272); L279-284 `_split_md_header` (raises `ValueError` on missing `## Summary`); L332-349 `--check` block | WR-01 validation + escape; WR-03 extension |
| `tooling/check_classification_rules.py` | L25-27 constants; L63-67 rules `generated_on` shape; L91-97 cluster_names shape (L96 sets `cluster_names = []` fallback); L242-247 map_version fidelity compare | WR-01 validation; WR-02 fidelity block |
| `tooling/check_release.py` | L295-306 step 5f runs `check_classification_rules.main()` under `[classification-rules]`; L308-343 step 5g reads `disk_on` (L321) and calls `generate_capability_map.main(["--generated-on", disk_on, "--check"])` (L328-329); L368 success line | No edits |

House test style (`tooling/test_link_policy.py`): module docstring with a `Run:` line, `sys.path.insert` then direct module import, `main() -> int`, plain asserts, success print, `raise SystemExit(main())`.

Live data facts the probes rely on: `docs/classification-rules.json` and `docs/capability-pack-map.json` both carry `generated_on: "2026-08-27"`; 32 cluster names; none contain `|`, CR, LF, or tab.

## Research

research: skipped (in-repo stdlib tooling hardening only; no external APIs, libraries, platforms, or version-sensitive choices)

## File Structure

- Modify: `tooling/generate_capability_map.py` (WR-01 constant + reject loop + two escape lines; WR-03 `--check` extension + one docstring line)
- Modify: `tooling/check_classification_rules.py` (WR-01 constant + reject loop; WR-02 fidelity compare)
- Create: `tooling/test_generate_capability_map.py` (probes (a)-(e), grown across Tasks 1-3)

---

### Task 1: WR-01 cluster_names reject set and renderer pipe escape

**Files:**
- Modify: `tooling/generate_capability_map.py` (constant after L36; loop after L83; escape lines at L257-260 and L264-265)
- Modify: `tooling/check_classification_rules.py` (constant after L27; loop after L97)
- Create: `tooling/test_generate_capability_map.py` (probes (a) and (b))

**Interfaces:**
- Consumes: existing `generate_map(rules: dict, overrides: dict, generated_on: str) -> dict`, `render_md(map_obj: dict, header_prefix: str) -> str`, `check_rules(data: dict, packs_root: Path | None = None, live_map: dict | None = None) -> list[str]`.
- Produces: module constant `_CLUSTER_NAME_FORBIDDEN = ("|", "\r", "\n", "\t")` in both tooling files; later tasks and probes read `generate_capability_map.MAP_PATH`, `MD_PATH`, `RULES_PATH`, `OVERRIDES_PATH`, `_load_json`, `_split_md_header`, `dumps_map`.

**Model:** flash

- [ ] **Step 1: Create the probe file with probes (a) and (b)**

Create `tooling/test_generate_capability_map.py` with exactly this content:

```python
#!/usr/bin/env python3
# Copyright (c) 2026 JG Systems Consulting Ltd. — MIT License (see LICENSE).
# SPDX-License-Identifier: MIT
"""Assert-based probes for capability-map tooling hardening (no framework).

Run:  python tooling/test_generate_capability_map.py
Exits 0 when cluster-name validation, renderer escaping, the --check md
freshness gate, the rules-vs-map generated_on fidelity check, and clean-tree
byte stability all hold. Any failed assert raises and exits nonzero.

Probe (c) points the generator module's MAP_PATH/MD_PATH at files inside a
TemporaryDirectory and restores the real paths in finally; docs/ is never
written by this file.
"""
from __future__ import annotations

import contextlib
import io
import json
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_classification_rules  # noqa: E402
import generate_capability_map  # noqa: E402

FORBIDDEN = ("|", "\r", "\n", "\t")


def rules_fixture(cluster_names, on="2026-01-01"):
    return {
        "schema_version": 1,
        "map_version": "1.0.0",
        "generated_on": on,
        "support_policy": "Support files ship with every pack.",
        "rules_of_construction": ["Construction rule one."],
        "support_filenames": ["glossary.md", "patterns.md", "cheatsheet.md"],
        "signpost_packs": ["omg-signpost", "se-standards-signpost"],
        "cluster_names": list(cluster_names),
        "assignments": [],
    }


def map_fixture(cluster_names, on="2026-01-01"):
    return {
        "schema_version": 2,
        "map_version": "1.0.0",
        "generated_on": on,
        "clusters": [{"name": n, "chapters": []} for n in cluster_names],
    }


def main() -> int:
    # (a) every rejected character fails closed in both entry points
    for ch in FORBIDDEN:
        name = "A" + ch + "B"
        raised = False
        try:
            generate_capability_map.generate_map(
                rules_fixture([name]), {}, "2026-01-01"
            )
        except ValueError as exc:
            raised = True
            assert (
                "rules cluster_names[0] contains a forbidden character"
                in str(exc)
            ), f"wrong generator rejection message for {name!r}: {exc}"
        assert raised, f"generate_map accepted forbidden character in {name!r}"
        errs = check_classification_rules.check_rules(
            rules_fixture([name]), live_map=map_fixture([name])
        )
        assert any(
            "envelope: cluster_names[0] contains a forbidden character" in m
            for m in errs
        ), f"check_rules missed forbidden character in {name!r}: {errs}"

    # (b) renderer escapes pipes; clean names pass through byte-identical
    piped = generate_capability_map.render_md(map_fixture(["A|B"]), "Header line\n")
    lines = piped.splitlines()
    row = next(ln for ln in lines if ln.startswith("| 1. "))
    head = next(ln for ln in lines if ln.startswith("## 1. "))
    assert row == "| 1. A\\|B | 0 |", f"summary row not escaped: {row!r}"
    assert head == "## 1. A\\|B", f"heading not escaped: {head!r}"
    clean = generate_capability_map.render_md(map_fixture(["Clean"]), "Header line\n")
    assert "| 1. Clean | 0 |" in clean, clean
    assert "## 1. Clean" in clean, clean

    print("generate-capability-map tests: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

Notes for the implementer: probe (a) passes `packs_root=None` (default), so `check_rules` scans the real `packs/` tree and its error list carries coverage noise alongside the target message; the assertion is containment by design. The in-memory `live_map` fixture keeps the fidelity block off disk.

- [ ] **Step 2: Run the probe file to verify it fails**

Run: `python tooling/test_generate_capability_map.py`
Expected: nonzero exit, `AssertionError: wrong generator rejection message for 'A|B': overrides schema_version must be int 1, got None` (pre-change `generate_map` sails past cluster_names and dies on the overrides shape checks at L90-92, where an empty overrides dict fails schema_version before notes, so the message assert fires).

- [ ] **Step 3: Add the generator constant and reject loop**

In `tooling/generate_capability_map.py`, edit 1 of 3. Old:

```python
ASSIGNMENT_KEYS = {"pack", "chapter", "cluster", "is_support"}
NOTE_KEYS = {"pack", "chapter", "note"}
```

New:

```python
ASSIGNMENT_KEYS = {"pack", "chapter", "cluster", "is_support"}
NOTE_KEYS = {"pack", "chapter", "note"}
_CLUSTER_NAME_FORBIDDEN = ("|", "\r", "\n", "\t")
```

Edit 2 of 3 (the loop sits between the shape check and `cluster_name_set`, so it fires before assignments and overrides are even read). Old:

```python
        raise ValueError("rules cluster_names must be a non-empty list of strings")
    cluster_name_set = set(cluster_names)
```

New:

```python
        raise ValueError("rules cluster_names must be a non-empty list of strings")
    for i, name in enumerate(cluster_names):
        if any(c in name for c in _CLUSTER_NAME_FORBIDDEN):
            raise ValueError(
                f"rules cluster_names[{i}] contains a forbidden character "
                f"(|, CR, LF, tab): {name!r}"
            )
    cluster_name_set = set(cluster_names)
```

Edit 3 of 3 (renderer escape, defense in depth; on validated names it never fires, so md bytes are unchanged on a clean tree). Old:

```python
    for i, cluster in enumerate(clusters, start=1):
        n = len(cluster["chapters"])
        total += n
        lines.append(f"| {i}. {cluster['name']} | {n} |")
```

New:

```python
    for i, cluster in enumerate(clusters, start=1):
        n = len(cluster["chapters"])
        total += n
        name = cluster["name"].replace("|", "\\|")
        lines.append(f"| {i}. {name} | {n} |")
```

And immediately below, the heading site. Old:

```python
    for i, cluster in enumerate(clusters, start=1):
        lines.append(f"## {i}. {cluster['name']}")
```

New:

```python
    for i, cluster in enumerate(clusters, start=1):
        name = cluster["name"].replace("|", "\\|")
        lines.append(f"## {i}. {name}")
```

- [ ] **Step 4: Add the checker constant and reject loop**

In `tooling/check_classification_rules.py`, edit 1 of 2. Old:

```python
SUPPORT_SUFFIX = " (support file)"
MAP_VERSION_RE = re.compile(r"^\d+\.\d+\.\d+$")
GENERATED_ON_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
```

New:

```python
SUPPORT_SUFFIX = " (support file)"
MAP_VERSION_RE = re.compile(r"^\d+\.\d+\.\d+$")
GENERATED_ON_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
_CLUSTER_NAME_FORBIDDEN = ("|", "\r", "\n", "\t")
```

Edit 2 of 2 (the loop sits after the shape check's `cluster_names = []` fallback, so it is a no-op when the shape check already failed). Old:

```python
        fail(errs, "envelope: cluster_names must be a list of non-empty strings")
        cluster_names = []
    cluster_name_set = set(cluster_names)
```

New:

```python
        fail(errs, "envelope: cluster_names must be a list of non-empty strings")
        cluster_names = []
    for i, name in enumerate(cluster_names):
        if any(c in name for c in _CLUSTER_NAME_FORBIDDEN):
            fail(
                errs,
                f"envelope: cluster_names[{i}] contains a forbidden character "
                f"(|, CR, LF, tab): {name!r}",
            )
    cluster_name_set = set(cluster_names)
```

- [ ] **Step 5: Run the probe file to verify it passes**

Run: `python tooling/test_generate_capability_map.py`
Expected: exit 0, output exactly `generate-capability-map tests: OK`.

- [ ] **Step 6: Confirm the live tree stays green**

Run: `python tooling/check_classification_rules.py`
Expected: exit 0, output `PASS: classification rules OK`.

Run: `python tooling/generate_capability_map.py --generated-on 2026-08-27 --check`
Expected: exit 0, output `PASS: generated map matches on-disk capability-pack-map.json` (the md PASS line does not exist until Task 3).

Run: `git status --porcelain docs/`
Expected: empty output (no doc file written by any gate).

- [ ] **Step 7: Commit**

```bash
git add tooling/generate_capability_map.py tooling/check_classification_rules.py tooling/test_generate_capability_map.py
git commit -m "tooling: reject | CR LF tab in cluster_names and escape pipes in render_md"
```

---

### Task 2: WR-02 rules-vs-map generated_on fidelity check

**Files:**
- Modify: `tooling/check_classification_rules.py` (fidelity block, after the map_version compare at L242-247)
- Modify: `tooling/test_generate_capability_map.py` (add probe (d))

**Interfaces:**
- Consumes: `check_rules` local `generated_on` (extracted from the rules envelope at L63) and the `live` map dict; `fail(errs, msg)` helper; probe helpers `rules_fixture(cluster_names, on=...)` and `map_fixture(cluster_names, on=...)` from Task 1.
- Produces: fidelity error message `fidelity: rules generated_on {rules!r} != live map {map!r}`; nothing else consumes it.

**Model:** flash

- [ ] **Step 1: Add probe (d) to the probe file**

In `tooling/test_generate_capability_map.py`, insert this block immediately before the line `print("generate-capability-map tests: OK")`:

```python
    # (d) rules-vs-map generated_on drift fails; equal dates yield no date error
    errs = check_classification_rules.check_rules(
        rules_fixture(["C1"], on="2026-01-01"),
        live_map=map_fixture(["C1"], on="2026-02-02"),
    )
    assert (
        "fidelity: rules generated_on '2026-01-01' != live map '2026-02-02'"
        in errs
    ), f"date drift not reported: {errs}"
    errs = check_classification_rules.check_rules(
        rules_fixture(["C1"]), live_map=map_fixture(["C1"])
    )
    assert not any(
        m.startswith("fidelity: rules generated_on") for m in errs
    ), f"false date error on equal dates: {errs}"
```

- [ ] **Step 2: Run the probe file to verify it fails**

Run: `python tooling/test_generate_capability_map.py`
Expected: nonzero exit, `AssertionError: date drift not reported: [...]` (the fidelity block compares map_version, names, keys, and is_support but not dates, so both fixture lists come back without the fidelity-date message).

- [ ] **Step 3: Add the fidelity date compare**

In `tooling/check_classification_rules.py`, insert immediately after the map_version compare. Old:

```python
    live_mv = live.get("map_version")
    if live_mv != map_version:
        fail(
            errs,
            f"fidelity: rules map_version {map_version!r} != live map {live_mv!r}",
        )
```

New:

```python
    live_mv = live.get("map_version")
    if live_mv != map_version:
        fail(
            errs,
            f"fidelity: rules map_version {map_version!r} != live map {live_mv!r}",
        )

    live_on = live.get("generated_on")
    if live_on != generated_on:
        fail(
            errs,
            f"fidelity: rules generated_on {generated_on!r} != live map {live_on!r}",
        )
```

Notes: no `None` guard, matching the map_version compare directly above; a missing rules date already fails its own shape check at L63-67. `tooling/check_release.py` stays untouched: step 5f runs before 5g, so date drift fails the release gate through the existing `[classification-rules]` wrapper.

- [ ] **Step 4: Run the probe file to verify it passes**

Run: `python tooling/test_generate_capability_map.py`
Expected: exit 0, output exactly `generate-capability-map tests: OK`.

- [ ] **Step 5: Confirm the live tree stays green**

Run: `python tooling/check_classification_rules.py`
Expected: exit 0, output `PASS: classification rules OK` (rules and map dates agree at `2026-08-27`, so the new compare stays silent).

- [ ] **Step 6: Commit**

```bash
git add tooling/check_classification_rules.py tooling/test_generate_capability_map.py
git commit -m "tooling: fail check_rules on rules-vs-map generated_on drift"
```

---

### Task 3: WR-03 md freshness gate in --check

**Files:**
- Modify: `tooling/generate_capability_map.py` (module docstring one-liner; `--check` tail at L348-349)
- Modify: `tooling/test_generate_capability_map.py` (add probes (c) and (e))

**Interfaces:**
- Consumes: `render_md`, `_split_md_header` (raises `ValueError("capability-pack-map.md missing ## Summary heading")` on a missing marker), module globals `MAP_PATH`/`MD_PATH` (probe (c) swaps and restores them), `dumps_map`, `args.generated_on` inside `main()`.
- Produces: `--check` exit semantics: 0 only when the JSON matches AND the md equals a fresh full-text render; new prints `FAIL: md check: capability-pack-map.md missing`, `FAIL: md check: {exc}`, `FAIL: capability-pack-map.md is stale; rerun tooling/generate_capability_map.py --generated-on <date> --sync-md`, `PASS: capability-pack-map.md is fresh`.

**Model:** flash

- [ ] **Step 1: Add probes (c) and (e) to the probe file**

In `tooling/test_generate_capability_map.py`, insert this block immediately before the line `print("generate-capability-map tests: OK")`:

```python
    # (c) --check md freshness: stale, missing, missing marker, fresh
    tmp = tempfile.TemporaryDirectory()
    real_map_path = generate_capability_map.MAP_PATH
    real_md_path = generate_capability_map.MD_PATH
    try:
        generate_capability_map.MAP_PATH = Path(tmp.name) / "map.json"
        generate_capability_map.MD_PATH = Path(tmp.name) / "map.md"
        rules = generate_capability_map._load_json(
            generate_capability_map.RULES_PATH, "rules"
        )
        overrides = generate_capability_map._load_json(
            generate_capability_map.OVERRIDES_PATH, "overrides"
        )
        built = generate_capability_map.generate_map(rules, overrides, "2026-01-01")
        generate_capability_map.MAP_PATH.write_text(
            generate_capability_map.dumps_map(built), encoding="utf-8"
        )
        good_md = generate_capability_map.render_md(built, "Probe header\n")

        def run_check():
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                rc = generate_capability_map.main(
                    ["--generated-on", "2026-01-01", "--check"]
                )
            return rc, buf.getvalue()

        generate_capability_map.MD_PATH.write_text(
            good_md.replace("## Summary", "## Summary\n<!-- tampered -->", 1),
            encoding="utf-8",
        )
        rc, out = run_check()
        assert rc == 1, f"stale md did not fail: rc={rc}"
        assert "capability-pack-map.md is stale" in out, out

        generate_capability_map.MD_PATH.unlink()
        rc, out = run_check()
        assert rc == 1, f"missing md did not fail: rc={rc}"
        assert "md check: capability-pack-map.md missing" in out, out

        generate_capability_map.MD_PATH.write_text("no marker here\n", encoding="utf-8")
        rc, out = run_check()
        assert rc == 1, f"missing ## Summary did not fail: rc={rc}"
        assert "md check:" in out and "## Summary" in out, out

        generate_capability_map.MD_PATH.write_text(good_md, encoding="utf-8")
        rc, out = run_check()
        assert rc == 0, f"fresh md failed: rc={rc} out={out}"
        assert "PASS: capability-pack-map.md is fresh" in out, out
    finally:
        generate_capability_map.MAP_PATH = real_map_path
        generate_capability_map.MD_PATH = real_md_path
        tmp.cleanup()

    # (e) clean tree stays byte-stable green
    disk_map = json.loads(
        generate_capability_map.MAP_PATH.read_text(encoding="utf-8")
    )
    disk_on = disk_map["generated_on"]
    disk_rules = generate_capability_map._load_json(
        generate_capability_map.RULES_PATH, "rules"
    )
    assert disk_rules["generated_on"] == disk_on, "rules vs map date drift"
    names = disk_rules["cluster_names"]
    assert len(names) == 32, f"expected 32 cluster names, got {len(names)}"
    assert not any(
        c in n for n in names for c in FORBIDDEN
    ), "live cluster name carries a forbidden character"
    built = generate_capability_map.generate_map(
        disk_rules,
        generate_capability_map._load_json(
            generate_capability_map.OVERRIDES_PATH, "overrides"
        ),
        disk_on,
    )
    disk_md = generate_capability_map.MD_PATH.read_text(encoding="utf-8")
    assert generate_capability_map.render_md(
        built, generate_capability_map._split_md_header(disk_md)
    ) == disk_md, "fresh render differs from on-disk capability-pack-map.md"
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = generate_capability_map.main(["--generated-on", disk_on, "--check"])
    out = buf.getvalue()
    assert rc == 0, f"--check failed on clean tree: rc={rc} out={out}"
    assert "PASS: generated map matches on-disk capability-pack-map.json" in out, out
    assert "PASS: capability-pack-map.md is fresh" in out, out
```

Implementation notes: the stale case tampers the rendered body (a comment line inserted after the `## Summary` marker) while keeping the marker intact; `_split_md_header` preserves the on-disk header verbatim, so the gate detects body drift — a header-only edit round-trips and passes by construction, which is accepted (header prose is human-owned, body is generated). The missing-marker case covers the `_split_md_header` `ValueError` path. `main()` reads `MAP_PATH`/`MD_PATH` as module globals at call time, so the swap works without any production-code hook.

- [ ] **Step 2: Run the probe file to verify it fails**

Run: `python tooling/test_generate_capability_map.py`
Expected: nonzero exit, `AssertionError: stale md did not fail: rc=0` (pre-change `--check` returns 0 right after the JSON compare and never reads the md).

- [ ] **Step 3: Add the docstring line and the --check extension**

In `tooling/generate_capability_map.py`, edit 1 of 2 (module docstring, operator-visible behavior note). Old:

```python
Usage:
  python tooling/generate_capability_map.py --generated-on YYYY-MM-DD [--sync-md]
  python tooling/generate_capability_map.py --generated-on YYYY-MM-DD --check
"""
```

New:

```python
Usage:
  python tooling/generate_capability_map.py --generated-on YYYY-MM-DD [--sync-md]
  python tooling/generate_capability_map.py --generated-on YYYY-MM-DD --check

`--check` also asserts docs/capability-pack-map.md freshness and writes nothing when it is stale or missing.
"""
```

Edit 2 of 2 (the `--check` tail; the JSON compare and its envelope-diff prints above stay byte-for-byte unchanged, so JSON remains first and md is downstream). Old:

```python
        print("PASS: generated map matches on-disk capability-pack-map.json")
        return 0
```

New:

```python
        print("PASS: generated map matches on-disk capability-pack-map.json")
        if not MD_PATH.is_file():
            print("FAIL: md check: capability-pack-map.md missing")
            return 1
        try:
            existing = MD_PATH.read_text(encoding="utf-8")
            fresh = render_md(built, _split_md_header(existing))
        except (OSError, ValueError) as exc:
            print(f"FAIL: md check: {exc}")
            return 1
        if fresh != existing:
            print(
                "FAIL: capability-pack-map.md is stale; rerun "
                "tooling/generate_capability_map.py --generated-on "
                f"{args.generated_on} --sync-md"
            )
            return 1
        print("PASS: capability-pack-map.md is fresh")
        return 0
```

Notes: the compare is full text (header plus rendered body), not body alone, because `--sync-md` preserves the on-disk header verbatim, so after any legitimate sync the full text equals `render_md(built, _split_md_header(existing))` exactly. At the stale print, `args.generated_on` equals the matched disk envelope date, so the rerun command is copy-paste runnable. `tooling/check_release.py` needs no change: 5g calls `main(["--generated-on", disk_on, "--check"])` and propagates the return code under `[map-replay]`.

- [ ] **Step 4: Run the probe file to verify it passes**

Run: `python tooling/test_generate_capability_map.py`
Expected: exit 0, output exactly `generate-capability-map tests: OK`.

- [ ] **Step 5: Confirm the live tree stays green and byte-stable**

Run: `python tooling/generate_capability_map.py --generated-on 2026-08-27 --check`
Expected: exit 0, output exactly:

```text
PASS: generated map matches on-disk capability-pack-map.json
PASS: capability-pack-map.md is fresh
```

Run: `git status --porcelain docs/`
Expected: empty output.

- [ ] **Step 6: Commit**

```bash
git add tooling/generate_capability_map.py tooling/test_generate_capability_map.py
git commit -m "tooling: assert capability-pack-map.md freshness in --check"
```

---

### Task 4: Full release-gate verification (no code changes)

**Files:**
- None modified. Read-only verification that the three gates ride the existing check_release steps.

**Interfaces:**
- Consumes: everything shipped in Tasks 1-3.
- Produces: evidence that check_release passes end to end with zero edits to it.

**Model:** flash

- [ ] **Step 1: Run the probe suite**

Run: `python tooling/test_generate_capability_map.py`
Expected: exit 0, `generate-capability-map tests: OK`.

- [ ] **Step 2: Run the checker**

Run: `python tooling/check_classification_rules.py`
Expected: exit 0, `PASS: classification rules OK`.

- [ ] **Step 3: Run the generator replay**

Run: `python tooling/generate_capability_map.py --generated-on 2026-08-27 --check`
Expected: exit 0, both PASS lines (`... capability-pack-map.json` and `PASS: capability-pack-map.md is fresh`).

- [ ] **Step 4: Run the full release gate**

Run: `python tooling/check_release.py`
Expected: exit 0, final line `RELEASE CHECK: PASS — repo is release-ready against the mechanical gate.` and no `FAIL:` lines anywhere in the output. Step 5f exercises the WR-01 checker gate and the WR-02 date gate; step 5g exercises the WR-01 generator gate and the WR-03 freshness gate through the propagated return code.

- [ ] **Step 5: Confirm zero unintended edits**

Run: `git status --porcelain` and `git diff --stat tooling/check_release.py`
Expected: `git status` shows no modifications under `docs/` or `tooling/` beyond what Tasks 1-3 committed (any `docs/superpowers/` untracked planning artifacts are expected); `git diff --stat tooling/check_release.py` is empty.

No commit: this task changes nothing.

---

## Self-review

- **Spec coverage:** WR-01 reject set in both entry points (Task 1, exact spec messages and prefixes), WR-01 `render_md` pipe escape at both injection sites (Task 1), WR-02 fidelity date compare with the exact spec block (Task 2), WR-03 full-text freshness compare with the exact spec block, docstring line, and fail-closed missing-md/missing-marker handling (Task 3), probes (a)-(e) all present with the spec's assertions (Tasks 1-3), clean-tree byte stability (probes (e) + Task 4 step 5). Non-goals respected: no CI, no check_release, no schema, no `_deslop` on names, whitespace carve-out kept.
- **Placeholder scan:** every code step carries complete old/new content or a complete file; every run step carries the command and expected output; no placeholder patterns of any kind.
- **Type and name consistency:** `_CLUSTER_NAME_FORBIDDEN` identical in both tooling files; probe helpers `rules_fixture(cluster_names, on=...)` / `map_fixture(cluster_names, on=...)` defined in Task 1 and reused verbatim in Tasks 2-3; `FORBIDDEN` probe constant matches the tooling tuple element for element; `main(["--generated-on", D, "--check"])` signature matches the generator's `main(argv: list[str] | None = None) -> int`.
