# CI Local-Gate Coverage Gap Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Close the highest-value CI-blind release-gate gaps with four inline-stdlib GitHub Actions steps twinned to `tooling/check_release.py`, move the overlap whitelist to a shared fail-closed data file, document the local-only remainder, and stamp the local gate's PASS receipt with version and sha.

**Architecture:** Four new steps appended to `.github/workflows/validate.yml`, each a `python3 - <<'PY'` heredoc that reads repo files as data and never executes checked-out code. Drift against the local gate is controlled by a kept assert-based probe (`tooling/test_ci_gate.py`) that extracts the shipped heredocs by pinned step name and asserts regex literal parity. The overlap whitelist becomes one shared data file read fail-closed by both gates. No mechanical pre-tag control is trustworthy under the no-checkout-execution posture, so the pre-tag control is procedural: a sha-stamped PASS banner plus a documented release rule.

**Tech Stack:** GitHub Actions (ubuntu-latest, inline bash + python3 stdlib heredocs), Python stdlib only (`json`, `re`, `sys`, `os`, `pathlib`, `subprocess`, `textwrap`, `tempfile`). No PyYAML, no third-party actions, no new `uses:`.

**Spec:** `docs/superpowers/specs/2026-09-14-ci-local-gate-coverage-gap.md` (the plan argues from the spec; executors read both)

## Research

research: skipped (in-repo CI/gate alignment only; no external APIs, libraries, platforms, or version-sensitive choices; GitHub Actions inline python3 stdlib is already the established pattern in this repo)

## Codebase context

Context gate output (reused): `docs/superpowers/context/2026-09-14-ci-local-gate-coverage-gap-context.md` (log sibling in the same directory). Facts below are verified against today's tree; line numbers refer to the files as they exist now.

- Local gate `tooling/check_release.py` runs eleven numbered checks plus extras 5b (RR-S-13), 5c (RR-B-30 packs.html), 6b (cursor manifest). Report prints `RELEASE CHECK: FAIL (N issue(s))` or `RELEASE CHECK: PASS — repo is release-ready against the mechanical gate.` (line 368; the only PASS site).
- CI `.github/workflows/validate.yml` has exactly four steps: leak sentinels, link policy (with the P4 `TRUSTED_HOSTS` inline pin plus parity assert against `tooling/link-policy-hosts.txt` inside that same step), frontmatter lint, catalog JSON. Header comment is lines 1-11; last line of the file is 134. `permissions: read-all` at line 19. Do not weaken or reorder anything existing.
- P4 data-file precedent to mirror: `tooling/check_release.py:65-88` (`load_banned_hosts`: token regex `^[A-Za-z0-9.-]+$`, blank/`#` lines skipped, malformed line raises, zero tokens raises, sorted dedup output) and `tooling/test_link_policy.py` (assert-based probe, no framework).
- Live version is 1.20.0 in `.claude-plugin/plugin.json`, `RELEASE-INFO.txt`, both `docs/products/website/*.yaml`, and the top `## [1.20.0]` heading in `CHANGELOG.md` (`## [Unreleased]` sits above it; the changelog regex still matches 1.20.0 first).
- Signpost packs: `packs/omg-signpost`, `packs/se-standards-signpost` (SKILL.md contains a `kind: signpost` frontmatter line). 63 content packs; SKILLS.md table links use `` [`slug`](packs/slug/SKILL.md) ``.
- `tooling/check_capability_map.py:29-31` pins `SUPPORT_SUFFIX = " (support file)"`, `MAP_VERSION_RE = re.compile(r"^\d+\.\d+\.\d+$")`, `GENERATED_ON_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")`; same two regexes at `tooling/check_classification_rules.py:26-27`. The map twin derives on-disk packs by `chapters/` directory existence and accepts ALL files under `chapters/` (`iterdir()` + `is_file()`, lines 176-203). The rules twin's reverse coverage scans `packs_root.glob("*/chapters/*.md")` (lines 216-224); signpost packs have no `chapters/` dir, so the glob is inherently signpost-free.
- `tooling/check_overlap.py` currently carries `WHITELIST = {"ch01-introduction.md"}` as an in-code constant (lines 31-34) and imports only `sys` and `pathlib`.
- Local Windows runs use `python`; CI runs `python3` on ubuntu-latest. Verification commands below use `python`.
- `.planning/codebase/TESTING.md` is stale: line references are old and its gaps section still says the SKILLS.md count is only caught locally.
- `CHANGELOG.md` has an open `## [Unreleased]` section with `### Added` (two bullets) and `### Changed` (one bullet) from the P4 work.

## Global Constraints

- Trust posture is unchanged and non-negotiable: the workflow never executes checked-out repository code; inline bash + python3 stdlib heredocs only; no new `uses:`; `permissions: read-all` unchanged; no `pull_request_target`. The P4 link-policy step (including its parity assert) is untouched.
- The four new step names are pinned exactly and are the probe's extraction markers: `Version single-source`, `SKILLS index count`, `Chapter basename overlap`, `Map and classification data invariants`.
- Every policy regex copied into the workflow must be byte-identical to its local twin. `tooling/test_ci_gate.py` enforces literal parity; a regex edit means editing both sides plus the probe's literals.
- New CI failures print `::error::` (or `::error file=<path>::`) lines carrying the local gate tags `[version]`, `[index]`, `[overlap]`, `[map-data]`, `[rules-data]`, then exit 1.
- The CI subset of checks 9/10 must stay a strict subset of the local twins' guarantees; it derives the disk side exactly as each twin derives it so the two gates cannot disagree.
- Local runs use `python` (Windows Git Bash); CI uses `python3` (ubuntu-latest). All code is stdlib-only on both sides.
- Zero em dashes in any newly authored prose or comment (existing copyright header lines keep their repo-standard form).

---

### Task 1: Overlap whitelist becomes a shared fail-closed data file

**Files:**
- Create: `tooling/overlap-whitelist.txt`
- Modify: `tooling/check_overlap.py` (docstring lines 17-20, imports lines 26-27, constant lines 31-34, `main()` lines 41-52)

**Interfaces:**
- Consumes: nothing new; `check_overlap.main()` keeps its existing `int` return contract (0 pass, 1 fail) consumed by `check_release.py` check 8.
- Produces: `tooling/overlap-whitelist.txt` (one `[A-Za-z0-9.-]+` token per line, `#` comments, blank lines allowed), `OverlapDataError`, and `load_whitelist() -> set[str]` in `tooling/check_overlap.py`. Task 3's CI step and Task 2's probe depend on the data file path `tooling/overlap-whitelist.txt`; Task 2's probe depends on the fail-closed behavior.

**Model:** flash

- [ ] **Step 1: Write the failing check first (fail-closed demo on the old constant)**

Run:

```bash
python tooling/check_overlap.py
```

Expected: `OVERLAP: PASS`. Then prove the current code has no data-file failure mode (this is the gap being closed):

```bash
grep -n "WHITELIST" tooling/check_overlap.py
```

Expected: lines 31-34 show `WHITELIST: set[str] = {...}` as an in-code constant; no `load_whitelist` exists yet (`grep -c "def load_whitelist" tooling/check_overlap.py` prints `0`).

- [ ] **Step 2: Create the data file**

Create `tooling/overlap-whitelist.txt` with exactly this content:

```
# Intentional cross-pack chapter-basename overlaps (TOOL-20).
# One token per line: a chapter basename allowed to appear under more than one
# pack. Both gates load this file at runtime and fail closed on an unreadable,
# malformed, or empty file: tooling/check_overlap.py locally, and the
# "Chapter basename overlap" step in .github/workflows/validate.yml in CI.
# Keep sorted. '#' comments and blank lines are ignored; every other line must
# match [A-Za-z0-9.-]+.
ch01-introduction.md
```

(The rationale comment lives in the data file: three source packs, dau-se-guidebook, nasa-npr-7123, and nasa-system-safety, legitimately share the canonical intro chapter name; different sources, same chapter name.)

- [ ] **Step 3: Rewrite `tooling/check_overlap.py` to load the data file fail-closed**

Edit 1, docstring: replace lines 17-20 (old block):

```
WHITELIST currently contains:
  - ch01-introduction.md — three distinct source packs (dau-se-guidebook,
    nasa-npr-7123, nasa-system-safety) legitimately share that canonical
    intro topic; different sources, same chapter name.
```

with (new block):

```
Whitelist: loaded from the shared data file tooling/overlap-whitelist.txt
(the same file the CI overlap step reads), fail-closed: an unreadable,
malformed, or empty data file fails the gate. The rationale for each entry
lives as a comment in the data file.
```

Edit 2, imports: replace (old block, lines 26-27):

```python
import sys
from pathlib import Path
```

with (new block):

```python
import re
import sys
from pathlib import Path
```

Edit 3, constant becomes loader: replace (old block, lines 31-34):

```python
# Intentional cross-pack canonical chapter basenames (not collisions to block).
WHITELIST: set[str] = {
    "ch01-introduction.md",
}
```

with (new block):

```python
# Intentional cross-pack canonical chapter basenames (not collisions to block)
# live in this data file, shared with the CI overlap step. Kept as data, not a
# literal here, so the two gates cannot drift; loaded fail-closed.
OVERLAP_DATA = "tooling/overlap-whitelist.txt"
_TOKEN = re.compile(r"^[A-Za-z0-9.-]+$")


class OverlapDataError(Exception):
    """The whitelist data file is missing, empty, or malformed (fail closed)."""


def load_whitelist() -> set[str]:
    """Load whitelisted chapter basenames from OVERLAP_DATA, de-duplicated.

    Skips blank lines and '#' comments. Any other malformed line, an unreadable
    file, or zero tokens raises OverlapDataError so the gate fails closed
    instead of silently unblocking collisions. Mirrors
    check_release.load_banned_hosts (the link-policy-hosts.txt reader).
    """
    try:
        lines = (ROOT / OVERLAP_DATA).read_text(encoding="utf-8").splitlines()
    except OSError as e:
        raise OverlapDataError(f"cannot read {OVERLAP_DATA}: {e}") from e
    tokens: set[str] = set()
    for lineno, raw in enumerate(lines, 1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if not _TOKEN.fullmatch(line):
            raise OverlapDataError(
                f"malformed line in {OVERLAP_DATA} (line {lineno}): {raw!r}"
            )
        tokens.add(line)
    if not tokens:
        raise OverlapDataError(f"whitelist empty ({OVERLAP_DATA} has no tokens)")
    return tokens
```

Edit 4, `main()`: replace (old block, lines 47-52):

```python
    packs_root = ROOT / "packs"
    if packs_root.is_dir():
        for p in sorted(packs_root.glob("*/chapters/*.md")):
            slug = p.parent.parent.name
            chaps.setdefault(p.name, []).append(slug)

    collisions = {name: packs for name, packs in chaps.items() if len(packs) > 1}
    bad = {name: packs for name, packs in collisions.items() if name not in WHITELIST}
```

with (new block):

```python
    packs_root = ROOT / "packs"
    if packs_root.is_dir():
        for p in sorted(packs_root.glob("*/chapters/*.md")):
            slug = p.parent.parent.name
            chaps.setdefault(p.name, []).append(slug)

    try:
        whitelist = load_whitelist()
    except OverlapDataError as e:
        print("OVERLAP: FAIL (whitelist data file)")
        print(f"  {e}")
        return 1

    collisions = {name: packs for name, packs in chaps.items() if len(packs) > 1}
    bad = {name: packs for name, packs in collisions.items() if name not in whitelist}
```

`check_release.py` needs no change here; it calls `check_overlap.main()` and reports `[overlap] check_overlap.py failed (see output above)` on a nonzero return.

- [ ] **Step 4: Run the checks and the fail-closed demos**

```bash
python tooling/check_overlap.py
```

Expected: `OVERLAP: PASS`, exit 0.

Fail-closed demo A (unreadable file):

```bash
mv tooling/overlap-whitelist.txt tooling/overlap-whitelist.txt.bak
python tooling/check_overlap.py; echo "exit=$?"
mv tooling/overlap-whitelist.txt.bak tooling/overlap-whitelist.txt
```

Expected: `OVERLAP: FAIL (whitelist data file)`, a `cannot read tooling/overlap-whitelist.txt:` line, `exit=1`.

Fail-closed demo B (zero tokens):

```bash
printf '# only a comment\n' > tooling/overlap-whitelist.txt
python tooling/check_overlap.py; echo "exit=$?"
git checkout -- tooling/overlap-whitelist.txt 2>/dev/null || true
```

Since the file is new and untracked at this point, restore it by re-creating it if the checkout fails: rewrite the exact content from Step 2. Expected demo output: `OVERLAP: FAIL (whitelist data file)`, a `whitelist empty (tooling/overlap-whitelist.txt has no tokens)` line, `exit=1`.

Fail-closed demo C (malformed token):

```bash
printf 'ch01-introduction.md\nbad token!\n' > tooling/overlap-whitelist.txt
python tooling/check_overlap.py; echo "exit=$?"
```

Expected: `OVERLAP: FAIL (whitelist data file)`, a `malformed line in tooling/overlap-whitelist.txt (line 2): 'bad token!'` line, `exit=1`. Then restore the exact Step 2 content.

After restore:

```bash
python tooling/check_overlap.py && python tooling/check_release.py
```

Expected: `OVERLAP: PASS`, then the gate ends `RELEASE CHECK: PASS — repo is release-ready against the mechanical gate.` (old banner text; Task 4 changes it), exit 0. The PASS also proves the whitelist still unlocks the live `ch01-introduction.md` three-pack overlap.

- [ ] **Step 5: Commit**

```bash
git add tooling/overlap-whitelist.txt tooling/check_overlap.py
git commit -m "feat(overlap): load whitelist from shared fail-closed data file"
```

---

### Task 2: Write the CI-gate probe (red: zero heredocs to extract yet)

**Files:**
- Create: `tooling/test_ci_gate.py`

**Interfaces:**
- Consumes: the data file from Task 1 (positive overlap demo and real-tree runs); the workflow heredocs and pinned step names that Task 3 lands.
- Produces: `tooling/test_ci_gate.py` with `extract_heredoc(workflow_text: str, step_name: str) -> str | None`, `run_gate(body: str, cwd: Path) -> tuple[int, str]`, `PINNED_STEPS: list[str]`, and `main() -> int` (exit 0 = all probe sections OK). Task 3 runs this probe as its test cycle.

**Model:** flash

This is the TDD "write the failing test" task. The probe tests the shipped workflow text itself (not a mirror of it): it extracts each heredoc by pinned step name and executes it. Mirror-functions fallback criterion, stated plainly: the P4 pattern would re-implement the gates as local functions if heredoc extraction matched zero steps, but zero extraction already fails this probe loudly, so the fallback is effectively unreachable and no mirror lives in the file.

Do not commit in this task; Task 3 commits the probe and the workflow steps together once green.

- [ ] **Step 1: Create `tooling/test_ci_gate.py` with exactly this content**

```python
#!/usr/bin/env python3
# Copyright (c) 2026 JG Systems Consulting Ltd. — MIT License (see LICENSE).
# SPDX-License-Identifier: MIT
"""Assert-based probe for the four inline CI gates in .github/workflows/validate.yml.

Run:  python tooling/test_ci_gate.py
Exits 0 when regex literal parity, heredoc extraction, negative demos, and
positive clean-tree runs all hold. Any failed assert raises and exits nonzero.

The probe extracts each heredoc from the workflow by its pinned step name and
executes the shipped workflow text (not a copy of it), so workflow breakage
fails here too. Mirror-functions fallback: the P4 pattern would re-implement
the gates as local functions if extraction matched zero heredocs, but zero
extraction already fails this probe loudly, so the fallback is effectively
unreachable and no mirror lives in this file.

Regex parity pins (P4 pin-plus-parity, extended to the four new steps):
  - three version regexes, the SKILLS link regex, and the signpost regex must
    appear verbatim in both tooling/check_release.py and validate.yml
  - MAP_VERSION_RE / GENERATED_ON_RE must appear verbatim in validate.yml and
    both local twins (check_capability_map.py, check_classification_rules.py)
"""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORKFLOW = ROOT / ".github" / "workflows" / "validate.yml"
RELEASE_TWIN = ROOT / "tooling" / "check_release.py"
MAP_TWIN = ROOT / "tooling" / "check_capability_map.py"
RULES_TWIN = ROOT / "tooling" / "check_classification_rules.py"

# Extraction markers; byte-for-byte the `- name:` values in validate.yml.
PINNED_STEPS = [
    "Version single-source",
    "SKILLS index count",
    "Chapter basename overlap",
    "Map and classification data invariants",
]

# Literals that must appear verbatim in check_release.py AND validate.yml.
RELEASE_PAIR = [
    ("changelog version", r"^##\s*\[(\d+\.\d+\.\d+)\]"),
    ("RELEASE-INFO version", r"Version:\s*([0-9]+\.[0-9]+\.[0-9]+)"),
    ("website YAML version", r'version:\s*"([0-9]+\.[0-9]+\.[0-9]+)"'),
    ("SKILLS link", r"\[`([^`]+)`\]\(packs/"),
    ("signpost kind", r"^kind:\s*signpost\s*$"),
]

# Literals pinned per local twin (map/classification envelope).
MAP_VERSION_LITERAL = r're.compile(r"^\d+\.\d+\.\d+$")'
GENERATED_ON_LITERAL = r're.compile(r"^\d{4}-\d{2}-\d{2}$")'


def extract_heredoc(workflow_text: str, step_name: str) -> str | None:
    """Return the dedented python3 heredoc body under `- name: <step_name>`.

    Returns None when the pinned step line, its `python3 - <<'PY'` invocation,
    the `PY` terminator, or a non-empty body is missing.
    """
    lines = workflow_text.splitlines()
    for start, line in enumerate(lines):
        if line.strip() == f"- name: {step_name}":
            break
    else:
        return None
    for begin in range(start, len(lines)):
        if "python3 - <<'PY'" in lines[begin]:
            begin += 1
            break
    else:
        return None
    body: list[str] = []
    for line in lines[begin:]:
        if line.strip() == "PY":
            break
        body.append(line)
    else:
        return None  # unterminated heredoc
    if not any(l.strip() for l in body):
        return None
    return textwrap.dedent("\n".join(body)) + "\n"


def run_gate(body: str, cwd: Path) -> tuple[int, str]:
    """Run an extracted heredoc body with cwd set; return (returncode, output)."""
    proc = subprocess.run(
        [sys.executable, "-c", body],
        cwd=str(cwd),
        capture_output=True,
        text=True,
    )
    return proc.returncode, proc.stdout + proc.stderr


def write_tree(root: Path, files: dict[str, str]) -> None:
    for rel, content in files.items():
        p = root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content, encoding="utf-8")


VERSION_BASE = {
    ".claude-plugin/plugin.json": '{"version": "1.2.3"}\n',
    "CHANGELOG.md": "# Changelog\n\n## [Unreleased]\n\n## [1.2.3]: 2026-01-01\n",
    "RELEASE-INFO.txt": "Version:    1.2.4\n",
    "docs/products/website/01-jgs-se-knowledge-packs.yaml": 'version: "1.2.3"\n',
    "docs/products/website/catalog.yaml": 'version: "1.2.3"\n',
}

SKILLS_FILTERED = (
    "# Skills\n\n"
    "- [`alpha`](packs/alpha/SKILL.md)\n"
    "- [`beta`](packs/beta/SKILL.md)\n"
    "- [`omg-signpost`](packs/omg-signpost/SKILL.md)\n"
)
SKILLS_ONE_LINK = (
    "# Skills\n\n"
    "- [`alpha`](packs/alpha/SKILL.md)\n"
    "- [`omg-signpost`](packs/omg-signpost/SKILL.md)\n"
)
SIGNPOST_MARKED = "---\nname: omg-signpost\nkind: signpost\n---\nbody\n"
SIGNPOST_UNMARKED = "---\nname: omg-signpost\n---\nbody\n"


def index_tree(skills: str, signpost_skill: str) -> dict[str, str]:
    return {
        "SKILLS.md": skills,
        "packs/alpha/SKILL.md": "---\nname: alpha\n---\nbody\n",
        "packs/beta/SKILL.md": "---\nname: beta\n---\nbody\n",
        "packs/omg-signpost/SKILL.md": signpost_skill,
    }


def overlap_tree(with_whitelist_file: bool) -> dict[str, str]:
    files = {
        "packs/alpha/chapters/ch01-introduction.md": "intro\n",
        "packs/beta/chapters/ch01-introduction.md": "intro\n",
        "packs/alpha/chapters/ch09-shared.md": "shared\n",
        "packs/beta/chapters/ch09-shared.md": "shared\n",
    }
    if with_whitelist_file:
        files["tooling/overlap-whitelist.txt"] = "# intentional\nch01-introduction.md\n"
    return files


VALID_MAP = {
    "schema_version": 2,
    "map_version": "1.0.0",
    "generated_on": "2026-01-01",
    "clusters": [
        {"name": "C", "chapters": [{"pack": "alpha", "chapter": "ch01.md", "note": ""}]},
    ],
}
VALID_RULES = {
    "schema_version": 1,
    "map_version": "1.0.0",
    "generated_on": "2026-01-01",
    "cluster_names": ["C"],
    "signpost_packs": [],
    "support_policy": "p",
    "rules_of_construction": ["r"],
    "support_filenames": ["glossary.md", "patterns.md", "cheatsheet.md"],
    "assignments": [
        {"pack": "alpha", "chapter": "ch01.md", "cluster": "C", "is_support": False},
    ],
}


def map_rules_tree(
    map_obj: dict | None = None,
    rules_obj: dict | None = None,
    extra_disk: list[str] | None = None,
) -> dict[str, str]:
    files: dict[str, str] = {"packs/alpha/chapters/ch01.md": "a\n"}
    for rel in extra_disk or []:
        files[rel] = "x\n"
    files["docs/capability-pack-map.json"] = json.dumps(map_obj or VALID_MAP)
    files["docs/classification-rules.json"] = json.dumps(rules_obj or VALID_RULES)
    return files


def main() -> int:
    workflow_text = WORKFLOW.read_text(encoding="utf-8")
    release_text = RELEASE_TWIN.read_text(encoding="utf-8")

    # 1. literal parity: the drift control comes first, it is the cheapest check
    for name, literal in RELEASE_PAIR:
        assert literal in release_text, (
            "regex drifted between check_release.py and validate.yml; sync them: "
            f"{name} missing from check_release.py"
        )
        assert literal in workflow_text, (
            "regex drifted between check_release.py and validate.yml; sync them: "
            f"{name} missing from validate.yml"
        )
    for name, literal in (
        ("MAP_VERSION_RE", MAP_VERSION_LITERAL),
        ("GENERATED_ON_RE", GENERATED_ON_LITERAL),
    ):
        assert literal in MAP_TWIN.read_text(encoding="utf-8"), (
            "regex drifted between validate.yml and check_capability_map.py; "
            f"sync them: {name} missing from check_capability_map.py"
        )
        assert literal in RULES_TWIN.read_text(encoding="utf-8"), (
            "regex drifted between validate.yml and check_classification_rules.py; "
            f"sync them: {name} missing from check_classification_rules.py"
        )
        assert literal in workflow_text, (
            "regex drifted between validate.yml and "
            "check_capability_map.py / check_classification_rules.py; sync them: "
            f"{name} missing from validate.yml"
        )

    # 2. extraction of the shipped heredocs by pinned step name
    bodies: dict[str, str] = {}
    for step in PINNED_STEPS:
        body = extract_heredoc(workflow_text, step)
        assert body is not None, (
            f"extraction failed: pinned step '{step}' has no python3 heredoc in "
            ".github/workflows/validate.yml; the probe runs the shipped workflow "
            "text, so fix the step name or the heredoc markers"
        )
        bodies[step] = body
    assert len(bodies) == len(PINNED_STEPS), "expected exactly four pinned heredocs"

    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)

        def demo(files: dict[str, str], step: str, expect: str, label: str) -> None:
            d = tmp / label
            write_tree(d, files)
            rc, out = run_gate(bodies[step], d)
            assert rc != 0, f"{label}: expected failure, got exit 0\n{out}"
            assert expect in out, f"{label}: expected {expect!r} in output\n{out}"

        def demo_ok(files: dict[str, str], step: str, label: str) -> None:
            d = tmp / label
            write_tree(d, files)
            rc, out = run_gate(bodies[step], d)
            assert rc == 0, f"{label}: expected exit 0\n{out}"

        # version: plugin.json vs RELEASE-INFO disagreement
        demo(VERSION_BASE, "Version single-source",
             "[version] disagreement / missing", "version-disagreement")
        # version: missing website YAML version line
        v2 = dict(VERSION_BASE)
        v2["RELEASE-INFO.txt"] = "Version:    1.2.3\n"
        v2["docs/products/website/01-jgs-se-knowledge-packs.yaml"] = "title: x\n"
        demo(v2, "Version single-source",
             "website YAML version '' != RELEASE-INFO '1.2.3'",
             "version-website-missing")

        # index: with the signpost marker, the signpost link is NOT counted,
        # so one content link vs two shipped packs fails
        demo(index_tree(SKILLS_ONE_LINK, SIGNPOST_MARKED), "SKILLS index count",
             "[index] SKILLS.md lists 1 packs but 2 are shipped", "index-mismatch")
        # index positive: the signpost link is filtered and the count matches
        demo_ok(index_tree(SKILLS_FILTERED, SIGNPOST_MARKED),
                "SKILLS index count", "index-filter-ok")

        # overlap: an un-whitelisted shared basename fails with both packs
        demo(overlap_tree(True), "Chapter basename overlap",
             "[overlap] ch09-shared.md: alpha, beta", "overlap-collision")
        # overlap: a missing whitelist data file fails closed
        demo(overlap_tree(False), "Chapter basename overlap",
             "[overlap] whitelist data file", "overlap-missing-file")
        # overlap positive: the whitelisted ch01-introduction.md collision passes
        demo_ok({
            "tooling/overlap-whitelist.txt": "ch01-introduction.md\n",
            "packs/alpha/chapters/ch01-introduction.md": "i\n",
            "packs/beta/chapters/ch01-introduction.md": "i\n",
        }, "Chapter basename overlap", "overlap-whitelisted-ok")

        # map: an on-disk chapter missing from the map fails on the disk side
        demo(map_rules_tree(extra_disk=["packs/alpha/chapters/ch02.md"]),
             "Map and classification data invariants",
             "[map-data] chapter-set: on disk not in map: alpha/ch02.md",
             "map-missing-chapter")
        # rules: an assignment row pointing at a nonexistent file
        r1 = json.loads(json.dumps(VALID_RULES))
        r1["assignments"].append(
            {"pack": "alpha", "chapter": "ch09-missing.md", "cluster": "C",
             "is_support": False}
        )
        demo(map_rules_tree(rules_obj=r1), "Map and classification data invariants",
             "coverage: assignment has no on-disk chapter: "
             "packs/alpha/chapters/ch09-missing.md", "rules-phantom-assignment")
        # rules: wrong schema_version
        r2 = json.loads(json.dumps(VALID_RULES))
        r2["schema_version"] = 2
        demo(map_rules_tree(rules_obj=r2), "Map and classification data invariants",
             "schema_version must be int 1, got 2", "rules-schema")
        # rules/map: generated_on mismatch between the two files
        r3 = json.loads(json.dumps(VALID_RULES))
        r3["generated_on"] = "2026-01-02"
        demo(map_rules_tree(rules_obj=r3), "Map and classification data invariants",
             "generated_on mismatch: map '2026-01-01' != rules '2026-01-02'",
             "rules-date-mismatch")

    # 3. positive runs against the real repo tree: what CI sees on a clean tree
    for step in PINNED_STEPS:
        rc, out = run_gate(bodies[step], ROOT)
        assert rc == 0, (
            f"positive run against the real tree failed for '{step}':\n{out}"
        )

    print("ci-gate probe: OK (parity, extraction, negative demos, positive runs)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 2: Run the probe to verify it fails loudly on zero extractions**

Run:

```bash
python tooling/test_ci_gate.py; echo "exit=$?"
```

Expected: `exit=1` with an `AssertionError` raised by the parity section — the version/map regex literals do not exist in `validate.yml` until Task 3 lands them, so parity drift fires first (e.g. the changelog-version literal missing from `validate.yml`); extraction is never reached. This is the required red state.

- [ ] **Step 3: No commit in this task**

Leave `tooling/test_ci_gate.py` uncommitted; Task 3 commits it together with the workflow steps so the history stays green.

---

### Task 3: Four CI steps plus coverage-map header in validate.yml

**Files:**
- Modify: `.github/workflows/validate.yml` (header comment lines 1-11; append four steps after line 134, the end of the "Catalog JSON valid" step)
- Test: `tooling/test_ci_gate.py` (from Task 2)

**Interfaces:**
- Consumes: `tooling/overlap-whitelist.txt` (Task 1) read fail-closed by the overlap step; the probe from Task 2.
- Produces: the four pinned steps `Version single-source`, `SKILLS index count`, `Chapter basename overlap`, `Map and classification data invariants`, each ending `sys.exit(1)` on failure with `::error` annotations. Later tasks and the probe rely on these exact names.

**Model:** flash

- [ ] **Step 1: Replace the header comment**

Replace (old block, lines 1-11; keep line 1's copyright text exactly as it is):

```
# Copyright (c) 2026 JG Systems Consulting Ltd. — MIT License (see ../../LICENSE).
# SPDX-License-Identifier: MIT
#
# RR-S-12 CI quality gate. Self-contained (inline bash + python3 stdlib only); never
# executes checked-out repository code. Runs on push to main and on every PR.
# Leak sentinels, link policy with signpost exemption, frontmatter lint, catalog
# validity. Link policy enforces from a trusted inline host set and asserts
# set-parity against tooling/link-policy-hosts.txt (the data file the local gate
# tooling/check_release.py loads) before scanning; any divergence fails the build.
# Both leak and link gates skip .planning identically (internal GSD workflow state;
# never ships).
```

with (new block):

```
# Copyright (c) 2026 JG Systems Consulting Ltd. — MIT License (see ../../LICENSE).
# SPDX-License-Identifier: MIT
#
# RR-S-12 CI quality gate. Self-contained (inline bash + python3 stdlib only); never
# executes checked-out repository code. Runs on push to main and on every PR.
# Leak sentinels, link policy with signpost exemption, frontmatter lint, catalog
# validity, version single-source, SKILLS index count, chapter basename overlap,
# and map/classification data invariants. Link policy enforces from a trusted
# inline host set and asserts set-parity against tooling/link-policy-hosts.txt
# (the data file the local gate tooling/check_release.py loads) before scanning;
# any divergence fails the build. Both leak and link gates skip .planning
# identically (internal GSD workflow state; never ships).
#
# Coverage map vs the local gate (run `python tooling/check_release.py` before
# tagging; CI green is not release-ready):
#   Version single-source                      twins check_release 4 + 4a (complete port)
#   SKILLS index count                         twins check_release 6 (complete port)
#   Chapter basename overlap                   twins check_release 8, shared tooling/overlap-whitelist.txt
#   Map and classification data invariants     pure-data subset of check_release 9 + 10
#
# CI does not cover, and why: full validate_pack (non-trivial parser; a fork
# invites permanent drift), RR-B-30 packs.html regeneration equality (needs the
# generator), full map threshold and note logic, full classification semantics
# beyond set coverage, and generate_capability_map --check replay (definitionally
# generator execution).
#
# Honest residual on the overlap whitelist: tooling/overlap-whitelist.txt is
# PR-editable, so a PR can relax that gate in both places at once. That is the
# same posture as the old in-code constant (also PR-editable); review is the
# control, and the data file removes accidental divergence between the gates.
```

- [ ] **Step 2: Append the four steps after the "Catalog JSON valid" step**

After current line 134 (`        run: python3 -c "import json; json.load(open('catalog.json')); print('catalog.json OK')"`), append exactly:

```yaml

      - name: Version single-source
        run: |
          python3 - <<'PY'
          # Twins tooling/check_release.py checks 4 + 4a. The three version
          # regex literals below are byte-identical to the local gate's;
          # tooling/test_ci_gate.py asserts that parity and fails on drift.
          import json, os, re, sys
          versions = {}
          try:
              with open(".claude-plugin/plugin.json", encoding="utf-8") as fh:
                  versions["plugin.json"] = json.load(fh).get("version", "")
          except Exception as e:
              print(f"::error::[version] cannot read plugin.json: {e}")
              versions["plugin.json"] = ""
          cl = open("CHANGELOG.md", encoding="utf-8").read() if os.path.isfile("CHANGELOG.md") else ""
          m = re.search(r"^##\s*\[(\d+\.\d+\.\d+)\]", cl, re.M)
          versions["CHANGELOG.md"] = m.group(1) if m else ""
          ri = open("RELEASE-INFO.txt", encoding="utf-8").read() if os.path.isfile("RELEASE-INFO.txt") else ""
          m = re.search(r"Version:\s*([0-9]+\.[0-9]+\.[0-9]+)", ri)
          versions["RELEASE-INFO.txt"] = m.group(1) if m else ""
          fails = 0
          # 4a. both website product YAMLs must carry the release version.
          expected = versions["RELEASE-INFO.txt"]
          for rel in ("docs/products/website/01-jgs-se-knowledge-packs.yaml",
                      "docs/products/website/catalog.yaml"):
              body = open(rel, encoding="utf-8", errors="ignore").read() if os.path.isfile(rel) else ""
              m = re.search(r'version:\s*"([0-9]+\.[0-9]+\.[0-9]+)"', body)
              got = m.group(1) if m else ""
              if got != expected:
                  print(f"::error file={rel}::[version] website YAML version '{got}' != RELEASE-INFO '{expected}'")
                  fails += 1
          distinct = {v for v in versions.values() if v}
          if len(distinct) > 1 or "" in versions.values():
              print(f"::error::[version] disagreement / missing: {versions}")
              fails += 1
          sys.exit(1 if fails else 0)
          PY

      - name: SKILLS index count
        run: |
          python3 - <<'PY'
          # Twins tooling/check_release.py check 6 (SKILLS.md entries vs shipped
          # packs, signpost-aware). The link regex and the signpost regex are
          # byte-identical to the local gate's; tooling/test_ci_gate.py asserts it.
          import re, sys, pathlib
          root = pathlib.Path(".")
          signpost_dirs = {
              p.parent for p in root.glob("packs/*/SKILL.md")
              if re.search(r"^kind:\s*signpost\s*$", p.read_text(encoding="utf-8", errors="ignore"), re.M)
          }
          packs = sorted(p for p in root.glob("packs/*") if p.is_dir() and p not in signpost_dirs)
          skills = (root / "SKILLS.md").read_text(encoding="utf-8") if (root / "SKILLS.md").is_file() else ""
          signpost_names = {d.name for d in signpost_dirs}
          entry_slugs = re.findall(r"\[`([^`]+)`\]\(packs/", skills)
          entry_count = len([s for s in entry_slugs if s not in signpost_names])
          if packs and entry_count != len(packs):
              print(f"::error::[index] SKILLS.md lists {entry_count} packs but {len(packs)} are shipped")
              sys.exit(1)
          print(f"[index] SKILLS.md entries match shipped packs ({entry_count})")
          PY

      - name: Chapter basename overlap
        run: |
          python3 - <<'PY'
          # Twins tooling/check_overlap.py. The whitelist lives in the shared
          # data file tooling/overlap-whitelist.txt, read fail-closed by both
          # gates (parity by construction). Honest residual: the data file is
          # PR-editable, so a PR can relax this gate in both places at once,
          # the same posture as the old in-code constant; review is the control.
          import re, sys, pathlib
          DATA_PATH = "tooling/overlap-whitelist.txt"
          TOKEN = re.compile(r"^[A-Za-z0-9.-]+$")

          def load_whitelist():
              # Mirrors the link-policy-hosts.txt reader: [A-Za-z0-9.-]+ tokens,
              # '#' comments and blank lines ignored; unreadable or malformed
              # file and zero tokens all fail closed.
              try:
                  lines = pathlib.Path(DATA_PATH).read_text(encoding="utf-8").splitlines()
              except OSError as e:
                  return None, f"cannot read {DATA_PATH}: {e}"
              tokens = set()
              for lineno, raw in enumerate(lines, 1):
                  line = raw.strip()
                  if not line or line.startswith("#"):
                      continue
                  if not TOKEN.fullmatch(line):
                      return None, f"malformed line in {DATA_PATH} (line {lineno}): {raw!r}"
                  tokens.add(line)
              if not tokens:
                  return None, f"whitelist empty ({DATA_PATH} has no tokens)"
              return tokens, None

          whitelist, err = load_whitelist()
          if whitelist is None:
              print(f"::error::[overlap] whitelist data file: {err}")
              sys.exit(1)
          chaps = {}
          for p in sorted(pathlib.Path(".").glob("packs/*/chapters/*.md")):
              slug = p.parent.parent.name
              chaps.setdefault(p.name, []).append(slug)
          bad = {name: packs for name, packs in chaps.items()
                 if len(packs) > 1 and name not in whitelist}
          if bad:
              for name in sorted(bad):
                  print(f"::error::[overlap] {name}: {', '.join(sorted(bad[name]))}")
              sys.exit(1)
          print("[overlap] no un-whitelisted chapter basename collisions")
          PY

      - name: Map and classification data invariants
        run: |
          python3 - <<'PY'
          # Pure-data subset of tooling/check_capability_map.py (check 9) and
          # tooling/check_classification_rules.py (check 10). Envelope pins and
          # disk-set derivation mirror the local twins exactly so the two gates
          # cannot disagree; thresholds, note/override consistency, support
          # policy, and generator replay stay local-only.
          import json, os, re, sys, pathlib
          SUPPORT_SUFFIX = " (support file)"
          MAP_VERSION_RE = re.compile(r"^\d+\.\d+\.\d+$")
          GENERATED_ON_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
          fails = 0

          def report(tag, path, msgs):
              global fails
              for msg in msgs:
                  print(f"::error file={path}::{tag} {msg}")
                  fails += 1

          def envelope(path, tag, want_schema):
              if not os.path.isfile(path):
                  report(tag, path, [f"file missing: {path}"])
                  return None, "", ""
              try:
                  with open(path, encoding="utf-8") as fh:
                      data = json.load(fh)
              except (json.JSONDecodeError, UnicodeDecodeError) as e:
                  report(tag, path, [f"JSON decode error: {e}"])
                  return None, "", ""
              if not isinstance(data, dict):
                  report(tag, path, ["top-level JSON must be an object"])
                  return None, "", ""
              errs = []
              schema = data.get("schema_version")
              if not isinstance(schema, int) or isinstance(schema, bool) or schema != want_schema:
                  errs.append(f"schema_version must be int {want_schema}, got {schema!r}")
              mv = data.get("map_version")
              if not mv:
                  errs.append("missing or empty map_version")
              elif not isinstance(mv, str) or not MAP_VERSION_RE.fullmatch(mv):
                  errs.append(f"map_version must match N.N.N, got {mv!r}")
              go = data.get("generated_on")
              if not go:
                  errs.append("missing or empty generated_on")
              elif not isinstance(go, str) or not GENERATED_ON_RE.fullmatch(go):
                  errs.append(f"generated_on must match YYYY-MM-DD, got {go!r}")
              report(tag, path, errs)
              return data, mv, go

          map_data, map_mv, map_go = envelope("docs/capability-pack-map.json", "[map-data]", 2)
          rules_data, rules_mv, rules_go = envelope("docs/classification-rules.json", "[rules-data]", 1)

          if map_mv and rules_mv and map_mv != rules_mv:
              print(f"::error::[map-data] map_version mismatch: map {map_mv!r} != rules {rules_mv!r}")
              fails += 1
          if map_go and rules_go and map_go != rules_go:
              print(f"::error::[rules-data] generated_on mismatch: map {map_go!r} != rules {rules_go!r}")
              fails += 1

          packs_root = pathlib.Path("packs")

          # map chapters vs disk; same derivation as check_capability_map.py
          # (packs by chapters/ dir existence, all files on disk, support-file
          # rows excluded from the map side)
          if isinstance(map_data, dict):
              clusters = map_data.get("clusters")
              if not isinstance(clusters, list):
                  report("[map-data]", "docs/capability-pack-map.json", ["missing or non-list clusters"])
                  clusters = []
              map_chapters = set()
              for cluster in clusters:
                  if not isinstance(cluster, dict):
                      continue
                  chapters = cluster.get("chapters")
                  if not isinstance(chapters, list):
                      continue
                  for entry in chapters:
                      if not isinstance(entry, dict):
                          continue
                      pack, chapter = entry.get("pack"), entry.get("chapter")
                      if not isinstance(pack, str) or not isinstance(chapter, str) or not pack:
                          continue
                      if chapter.endswith(SUPPORT_SUFFIX):
                          continue
                      map_chapters.add((pack, chapter))
              on_disk_packs = (
                  {p.name for p in packs_root.iterdir() if p.is_dir() and (p / "chapters").is_dir()}
                  if packs_root.is_dir() else set()
              )
              disk_chapters = set()
              for pack_name in sorted(on_disk_packs):
                  for path in (packs_root / pack_name / "chapters").iterdir():
                      if path.is_file():
                          disk_chapters.add((pack_name, path.name))
              only_disk = sorted(disk_chapters - map_chapters)
              only_map = sorted(map_chapters - disk_chapters)
              msgs = [f"chapter-set: on disk not in map: {p}/{c}" for p, c in only_disk[:20]]
              if len(only_disk) > 20:
                  msgs.append(f"chapter-set: ... and {len(only_disk) - 20} more on-disk-only")
              msgs += [f"chapter-set: in map not on disk: {p}/{c}" for p, c in only_map[:20]]
              if len(only_map) > 20:
                  msgs.append(f"chapter-set: ... and {len(only_map) - 20} more map-only")
              report("[map-data]", "docs/capability-pack-map.json", msgs)

          # rules coverage vs disk; same derivation as
          # check_classification_rules.py (packs/*/chapters/*.md; signpost packs
          # have no chapters/ dir so the glob is inherently signpost-free;
          # signpost_packs is read as a set for exclusion only, and its exact
          # value fidelity stays a local-only guarantee)
          if isinstance(rules_data, dict):
              assignments = rules_data.get("assignments")
              if not isinstance(assignments, list):
                  report("[rules-data]", "docs/classification-rules.json", ["missing or non-list assignments"])
                  assignments = []
              sp = rules_data.get("signpost_packs")
              signpost_set = {s for s in sp if isinstance(s, str)} if isinstance(sp, list) else set()
              non_support = set()
              msgs = []
              for entry in assignments:
                  if not isinstance(entry, dict):
                      continue
                  pack, chapter, is_support = entry.get("pack"), entry.get("chapter"), entry.get("is_support")
                  if is_support is not False:
                      continue  # support rows skipped; support policy stays local
                  if not isinstance(pack, str) or not pack or not isinstance(chapter, str) or not chapter:
                      continue
                  non_support.add((pack, chapter))
                  if pack in signpost_set:
                      msgs.append(f"signpost: assignment for signpost pack {pack!r} ({chapter})")
                  if not (packs_root / pack / "chapters" / chapter).is_file():
                      msgs.append(f"coverage: assignment has no on-disk chapter: packs/{pack}/chapters/{chapter}")
              for path in packs_root.glob("*/chapters/*.md"):
                  if (path.parent.parent.name, path.name) not in non_support:
                      msgs.append(f"coverage: on-disk chapter has no assignment: {path.parent.parent.name}/{path.name}")
              report("[rules-data]", "docs/classification-rules.json", msgs)

          if not fails:
              print("[map-data]/[rules-data] data invariants OK")
          sys.exit(1 if fails else 0)
          PY
```

Indentation is load-bearing: `- name:` and `run:` at 6 spaces, heredoc body at 10 spaces, `PY` terminator at 10 spaces, matching the existing steps.

- [ ] **Step 3: Trust-posture sanity greps**

```bash
grep -n "uses:" .github/workflows/validate.yml
grep -c "permissions: read-all" .github/workflows/validate.yml
grep -n "TRUSTED_HOSTS" .github/workflows/validate.yml | head -1
```

Expected: the only `uses:` line is `actions/checkout@v4`; the read-all count is `1`; the P4 `TRUSTED_HOSTS` pin is still present in the link step (untouched).

- [ ] **Step 4: Run the probe to verify green**

```bash
python tooling/test_ci_gate.py; echo "exit=$?"
```

Expected: `ci-gate probe: OK (parity, extraction, negative demos, positive runs)`, `exit=0`. This exercises: five plus two regex literal-parity asserts, extraction of all four heredocs by pinned name, nine negative demos (two version, one index, two overlap, four map/rules; the map-missing-chapter demo also produces a `[rules-data]` line, which the probe tolerates since it asserts only the named `[map-data]` substring), two fixture positives, and the four real-tree positive runs. If a negative demo message drifts from the expectation printed by the probe, fix the workflow heredoc message, never the expectation.

- [ ] **Step 5: Simulate each step's real-tree behavior once more, directly**

```bash
python - <<'PY'
import sys, pathlib
sys.path.insert(0, "tooling")
from test_ci_gate import PINNED_STEPS, extract_heredoc, run_gate, ROOT
text = pathlib.Path(".github/workflows/validate.yml").read_text(encoding="utf-8")
for step in PINNED_STEPS:
    rc, out = run_gate(extract_heredoc(text, step), ROOT)
    print(step, "->", rc)
    assert rc == 0, out
PY
```

Expected: four lines, each `<pinned name> -> 0`.

- [ ] **Step 6: Commit**

```bash
git add .github/workflows/validate.yml tooling/test_ci_gate.py
git commit -m "feat(ci): add version, index, overlap, and map/rules data gates with probe"
```

---

### Task 4: check_release docstring split and sha-stamped PASS banner

**Files:**
- Modify: `tooling/check_release.py` (docstring lines 27-31, imports lines 34-37, report block lines 362-369)

**Interfaces:**
- Consumes: `versions["RELEASE-INFO.txt"]` parsed inside `main()` (check 4); `git` on PATH.
- Produces: PASS line of the exact form `RELEASE CHECK: PASS (v<version> @ <short-sha>)`, or `RELEASE CHECK: PASS (v<version> @ no-git)` when git is unavailable. Task 5 documents this form in TESTING.md and the CHANGELOG.

**Model:** flash

- [ ] **Step 1: Confirm the current banner (baseline)**

```bash
python tooling/check_release.py | tail -1
```

Expected: `RELEASE CHECK: PASS — repo is release-ready against the mechanical gate.`

- [ ] **Step 2: Extend the docstring with the CI-covered vs local-only split and the pre-tag rule**

Replace (old block, lines 27-31):

```
stdlib only. This is a LOCAL/trusted gate and may run repo code; the CI workflow
(.github/workflows/validate.yml) inlines its own checks and never executes repo code.

Usage:  python tooling/check_release.py
"""
```

with (new block):

```
stdlib only. This is a LOCAL/trusted gate and may run repo code; the CI workflow
(.github/workflows/validate.yml) inlines its own checks and never executes repo code.
CI-covered: version, index, overlap, map/rules data invariants. Local-only required
before tag: pack validation, packs.html freshness, full map/rules checks, replay.

Pre-tag rule: run this gate at the exact commit being tagged and require a PASS
line whose sha matches that commit (a `@ no-git` receipt never satisfies it).

Usage:  python tooling/check_release.py
"""
```

- [ ] **Step 3: Add the subprocess import**

Replace (old block, lines 34-37):

```python
import json
import re
import sys
from pathlib import Path
```

with (new block):

```python
import json
import re
import subprocess
import sys
from pathlib import Path
```

- [ ] **Step 4: Replace the PASS banner with the sha-stamped receipt**

Replace (old block, lines 362-369):

```python
    # report
    if errs:
        print(f"RELEASE CHECK: FAIL ({len(errs)} issue(s))")
        for e in errs:
            print(f"  - {e}")
        return 1
    print("RELEASE CHECK: PASS — repo is release-ready against the mechanical gate.")
    return 0
```

with (new block):

```python
    # report
    if errs:
        print(f"RELEASE CHECK: FAIL ({len(errs)} issue(s))")
        for e in errs:
            print(f"  - {e}")
        return 1
    # PASS receipt: version + short sha of the exact commit the gate ran at, so
    # a pasted transcript is verifiable. Pre-tag rule (docstring): require the
    # sha to match the commit being tagged. `@ no-git` is distinct and can
    # never satisfy that match.
    version = versions["RELEASE-INFO.txt"]
    try:
        short_sha = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            capture_output=True, text=True, cwd=ROOT, check=True,
        ).stdout.strip()
        receipt = f"v{version} @ {short_sha}"
    except Exception:
        receipt = f"v{version} @ no-git"
    print(f"RELEASE CHECK: PASS ({receipt})")
    return 0
```

On the PASS path the gate has already proven RELEASE-INFO parsed and agreed (check 4), so `version` is non-empty there.

- [ ] **Step 5: Verify the normal and no-git receipts**

```bash
python tooling/check_release.py | tail -1
git rev-parse --short HEAD
```

Expected: the first command prints `RELEASE CHECK: PASS (v1.20.0 @ <short-sha>)` where `<short-sha>` equals the second command's output, exit 0.

No-git fallback demo (point git at a nonexistent repo via the inherited env):

```bash
GIT_DIR=$PWD/.git-nonexistent python tooling/check_release.py | tail -1; echo "exit=$?"
```

Expected: `RELEASE CHECK: PASS (v1.20.0 @ no-git)`, `exit=0`. The `@ no-git` form is distinct so it can never satisfy the pre-tag sha match.

Also confirm nothing else in the repo greps the old banner string:

```bash
grep -rn "repo is release-ready" --include="*.py" --include="*.js" --include="*.yml" . | grep -v ".git/"
```

Expected: no hits outside `docs/superpowers/` (historical plan/context prose only; no live code or CI depends on the old text).

- [ ] **Step 6: Re-run the kept probes**

```bash
python tooling/check_release.py >/dev/null && echo gate-ok
python tooling/test_ci_gate.py
python tooling/test_link_policy.py
```

Expected: `gate-ok`, then `ci-gate probe: OK (...)`, then `link-policy tests: OK`. The gate PASS here also re-proves the probe's real-tree positive runs still see a clean tree.

- [ ] **Step 7: Commit**

```bash
git add tooling/check_release.py
git commit -m "feat(release): stamp PASS receipt with version and short sha, document CI split"
```

---

### Task 5: TESTING.md refresh and CHANGELOG entry

**Files:**
- Modify: `.planning/codebase/TESTING.md` (gates table line 15 and 17, run commands lines 19-25, gaps lines 78-80)
- Modify: `CHANGELOG.md` (`## [Unreleased]` section)

**Interfaces:**
- Consumes: the landed banner form `RELEASE CHECK: PASS (v<version> @ <short-sha>)` from Task 4 and the probe from Task 2.
- Produces: documentation only; no code surfaces.

**Model:** flash

- [ ] **Step 1: Refresh the gates table in `.planning/codebase/TESTING.md`**

Replace (old block, line 15):

```
| CI content-integrity | `.github/workflows/validate.yml` (GitHub Actions, `content-integrity` job) | leak sentinels, link policy, frontmatter lint, `catalog.json` JSON validity |
```

with (new block):

```
| CI content-integrity | `.github/workflows/validate.yml` (GitHub Actions, `content-integrity` job) | leak sentinels, link policy (P4 host parity vs `tooling/link-policy-hosts.txt`), frontmatter lint, `catalog.json` JSON validity, version single-source incl. both website YAMLs, SKILLS.md index count, chapter basename overlap (shared `tooling/overlap-whitelist.txt`), map/classification data invariants (envelope pins, disk set equality, rules coverage subset) |
| CI gate probe | `python tooling/test_ci_gate.py` | extracts the four inline CI heredocs by pinned step name, runs negative demos and positive clean-tree runs, asserts regex literal parity with the local twins |
```

Replace (old block, line 17):

```
| Release gate | `python tooling/check_release.py` | required governance files, leak sentinels, link policy, version single-source (`plugin.json` == CHANGELOG top == `RELEASE-INFO.txt`), all packs validate, `SKILLS.md` entry count, JGSC/SPDX headers on authored files |
```

with (new block):

```
| Release gate | `python tooling/check_release.py` | required governance files, leak sentinels, link policy (`tooling/link-policy-hosts.txt` data file), version single-source (`plugin.json` == CHANGELOG top == `RELEASE-INFO.txt` == both website YAMLs), all packs validate, RR-S-13 markers, packs.html freshness, `SKILLS.md` entry count, cursor manifest, chapter-basename overlap (`tooling/overlap-whitelist.txt`), capability-map freshness, classification-rules completeness, generator replay, JGSC/SPDX headers on authored files |
```

- [ ] **Step 2: Add the probe to run commands and state the pre-tag rule**

Replace (old block, lines 19-25):

```
**Run Commands:**
```bash
python tooling/validate_pack.py --all     # Validate every pack under packs/
python tooling/validate_pack.py packs/dau-se-guidebook   # Validate one pack
python tooling/check_release.py           # Full local release-readiness gate
```
CI runs automatically on push to `main` and every PR (`.github/workflows/validate.yml`).
```

with (new block):

```
**Run Commands:**
```bash
python tooling/validate_pack.py --all     # Validate every pack under packs/
python tooling/validate_pack.py packs/dau-se-guidebook   # Validate one pack
python tooling/check_release.py           # Full local release-readiness gate
python tooling/test_ci_gate.py            # Probe the four inline CI gates + regex parity (kept, no framework)
python tooling/test_link_policy.py        # Link-policy loader + parity checks (kept, no framework)
```
CI runs automatically on push to `main` and every PR (`.github/workflows/validate.yml`).

**Pre-tag rule:** no mechanical control can verify a local gate ran (CI never
executes repo code, so any in-repo stamp would be self-issued). Before tagging,
run `python tooling/check_release.py` at the exact commit being tagged and
require a PASS line whose sha matches that commit, e.g.
`RELEASE CHECK: PASS (v1.20.0 @ a1b2c3d)`. A `@ no-git` receipt never
satisfies the match. The release procedure (P8, gsd-ship) requires the pasted
PASS transcript.
```

- [ ] **Step 3: Refresh the gaps section**

Replace (old block, lines 78-80):

```
- Restoring `tooling/eval/` (eval.py + pytest tests) from git history or rewriting it is a prerequisite for any eval/scoring work
- Pure-Python helpers (`parse_simple_yaml`, `deslop`, host regexes) are duplicated between `tooling/check_release.py` and inline CI python — changes must be made in both places
- Generated artifacts drift risk: `docs/packs.html`, `catalog.json`, `SKILLS.md` counts are only caught by `check_release.py`, not by CI
```

with (new block):

```
- Restoring `tooling/eval/` (eval.py + pytest tests) from git history or rewriting it is a prerequisite for any eval/scoring work
- Pure-Python helpers (`parse_simple_yaml`, `deslop`, host regexes, version regexes, signpost regex) are duplicated between `tooling/check_release.py` and inline CI python; changes must be made in both places, and `python tooling/test_ci_gate.py` catches drift on the pinned regex literals
- Generated artifacts drift risk: `docs/packs.html` and `catalog.json` freshness are only caught by `check_release.py`, not by CI (version agreement, the SKILLS.md pack count, overlap, and the map/rules data invariants moved to CI in the 2026-09-14 gate package; the local gate remains the full eleven-check surface plus extras)
- CI's map/rules steps are deliberately weaker than the local checkers: cluster minimum thresholds, note and override consistency, rules-of-construction edge semantics, support-file policy, and generator replay stay local-only, and the CI subset must remain a strict subset of the local guarantees
```

- [ ] **Step 4: Add the CHANGELOG entries under `## [Unreleased]`**

In `CHANGELOG.md`, replace (old block):

```
## [Unreleased]

### Added

- `tooling/link-policy-hosts.txt`: single data file with the 18 banned
```

with (new block):

```
## [Unreleased]

### Added

- `.github/workflows/validate.yml`: four inline-stdlib CI steps twinned to the
  local release gate: `Version single-source` (checks 4 + 4a, both website
  YAMLs included), `SKILLS index count` (check 6), `Chapter basename overlap`
  (check 8), and `Map and classification data invariants` (pure-data subset of
  checks 9 and 10).
- `tooling/overlap-whitelist.txt`: shared data file for intentional
  cross-pack chapter-basename overlaps, loaded fail-closed by both
  `tooling/check_overlap.py` and the CI overlap step.
- `tooling/test_ci_gate.py`: assert-based probe that extracts the four new
  heredocs from the workflow by pinned step name, runs negative demos and
  positive clean-tree runs, and asserts regex literal parity with the local
  twins (`check_release.py`, `check_capability_map.py`,
  `check_classification_rules.py`).
- `tooling/link-policy-hosts.txt`: single data file with the 18 banned
```

Then replace (old block):

```
### Changed

- CI link policy enforces from a trusted inline host set and fails on
```

with (new block):

```
### Changed

- `tooling/check_overlap.py` loads its whitelist from
  `tooling/overlap-whitelist.txt` (fail-closed) instead of an in-code constant.
- `tooling/check_release.py` PASS banner now carries the version and short
  commit sha (`RELEASE CHECK: PASS (v<version> @ <short-sha>)`; `@ no-git`
  when git is unavailable), and its docstring records the CI-covered vs
  local-only split plus the pre-tag sha-match rule.
- CI link policy enforces from a trusted inline host set and fails on
```

- [ ] **Step 5: Verify the docs and the gate still pass**

```bash
grep -c "tooling/overlap-whitelist.txt" .planning/codebase/TESTING.md CHANGELOG.md
python tooling/check_release.py | tail -1
```

Expected: nonzero counts in both files (the whitelist name is documented), and the gate ends `RELEASE CHECK: PASS (v1.20.0 @ <short-sha>)`, exit 0. The PASS re-proves the CHANGELOG edits did not trip the leak/link scans or the version gate (`## [Unreleased]` above `## [1.20.0]` remains harmless to the changelog regex).

- [ ] **Step 6: Commit**

```bash
git add .planning/codebase/TESTING.md CHANGELOG.md
git commit -m "docs: refresh TESTING.md CI-gap note and CHANGELOG for the CI gate package"
```

---

### Task 6: Whole-package verification

**Files:**
- None created or modified (verification only; fix-ups belong to the task that introduced the defect)

**Interfaces:**
- Consumes: every deliverable from Tasks 1-5.
- Produces: the evidence list the PR description should carry.

**Model:** flash

- [ ] **Step 1: Run every gate and probe in sequence**

```bash
python tooling/check_release.py; echo "release=$?"
python tooling/check_overlap.py; echo "overlap=$?"
python tooling/test_ci_gate.py; echo "probe=$?"
python tooling/test_link_policy.py; echo "linkpolicy=$?"
```

Expected: `RELEASE CHECK: PASS (v1.20.0 @ <short-sha>)` then `release=0`; `OVERLAP: PASS` then `overlap=0`; `ci-gate probe: OK (parity, extraction, negative demos, positive runs)` then `probe=0`; `link-policy tests: OK` then `linkpolicy=0`.

- [ ] **Step 2: Verify the failure paths one last time from the shipped files**

```bash
python - <<'PY'
import sys
sys.path.insert(0, "tooling")
from test_ci_gate import PINNED_STEPS, extract_heredoc, run_gate, ROOT, write_tree, VERSION_BASE, overlap_tree
import tempfile, pathlib
text = pathlib.Path(".github/workflows/validate.yml").read_text(encoding="utf-8")
bodies = {s: extract_heredoc(text, s) for s in PINNED_STEPS}
assert all(bodies.values())
with tempfile.TemporaryDirectory() as td:
    d = pathlib.Path(td) / "neg"
    write_tree(d, overlap_tree(False))
    rc, out = run_gate(bodies["Chapter basename overlap"], d)
    print("missing whitelist ->", rc)
    assert rc == 1 and "[overlap] whitelist data file" in out
print("failure paths OK")
PY
```

Expected: `missing whitelist -> 1` and `failure paths OK`. (The full negative matrix already lives in the kept probe; this spot-check re-derives one failure from the shipped workflow text.)

- [ ] **Step 3: Trust-posture and byte-stability audit**

```bash
grep -n "uses:" .github/workflows/validate.yml
git diff --stat HEAD~4 2>/dev/null | tail -1
grep -rn "python3 tooling/\|python tooling/" .github/workflows/validate.yml
```

Expected: only `actions/checkout@v4` in `uses:`; the only `python tooling/` occurrences in the workflow are in comment lines (the header coverage map) — no executable line invokes any `tooling/*.py` (the workflow reads data files as text, never executes them); the diff footprint is limited to `.github/workflows/validate.yml`, `tooling/overlap-whitelist.txt`, `tooling/check_overlap.py`, `tooling/check_release.py`, `tooling/test_ci_gate.py`, `.planning/codebase/TESTING.md`, `CHANGELOG.md`. The P4 link-policy step text is byte-identical to before this package (`git diff HEAD~4 -- .github/workflows/validate.yml | grep -c "TRUSTED_HOSTS"` shows context lines only, no removed pin lines).

- [ ] **Step 4: Push and confirm CI**

```bash
git push origin main  # or the PR branch
gh run watch $(gh run list --workflow validate --limit 1 --json databaseId -q '.[0].databaseId')
```

Expected: the run is green with the four new steps `Version single-source`, `SKILLS index count`, `Chapter basename overlap`, and `Map and classification data invariants` executing after `Catalog JSON valid`. If a step fails on CI only, reproduce locally with the probe (Task 3 Step 4) before touching the heredoc; the probe runs the same shipped text.

---

## Self-review record

Spec coverage checklist run against `docs/superpowers/specs/2026-09-14-ci-local-gate-coverage-gap.md`: four pinned CI steps (Task 3), header coverage map plus local-only remainder list (Task 3 Step 1), whitelist extraction with fail-closed loader mirroring the link-policy reader including token regex, zero-token fail, and dedup (Task 1), docstring two-liner (Task 4 Step 2), sha-stamped PASS banner with distinct `@ no-git` form (Task 4 Step 4), TESTING.md refresh and CHANGELOG entry (Task 5), probe with heredoc extraction by the four pinned names, loud failure on zero extractions, negative demo per step, positive clean-tree runs, and literal-parity asserts with per-twin-pair drift messages (Task 2). Residual advisories folded in: rules reverse disk coverage scans `packs/*/chapters/*.md` matching `check_classification_rules.py` (Task 3 Step 2, rules section comment and code), and the mirror-fallback brittleness criterion is stated in the probe docstring (Task 2: the fallback is effectively unreachable because zero extraction already fails the probe). Pre-tag procedural control documented in docstring, TESTING.md, and CHANGELOG; P8 wiring explicitly out of scope per the spec. Trust constraints carried in Global Constraints and audited in Task 6 Step 3. Placeholders: none; every code step contains full content. Type and name consistency: `OverlapDataError` / `load_whitelist` match between Tasks 1 and 2; `PINNED_STEPS`, `extract_heredoc`, `run_gate` match between Tasks 2, 3, and 6; tags `[version]`, `[index]`, `[overlap]`, `[map-data]`, `[rules-data]` match across workflow, probe expectations, and docs.
