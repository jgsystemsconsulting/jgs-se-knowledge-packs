# Spec: map-tooling residual harden (2026-09-14)

Package: sanctioned packages ledger P7, size M. Promoted backlog ids b-04, b-05.
Baseline: HEAD `35c5e3adb34974fa9933232343c064d39f7fdfa9` on main. All line refs below were re-verified against this tree on 2026-09-14.
Style note: every `--` in this document is a literal CLI flag (`--check`, `--sync-md`, `--generated-on`) inside a code span or quoted message text; none is dash punctuation.

## Problem

Phase 21's implementation review recorded three residual holes on the capability-map tooling flow. All three exist on the current tree.

**WR-01 (cluster_names).** `generate_map` accepts any non-empty strings (`tooling/generate_capability_map.py` L77-83), and `check_rules` mirrors that shape (`tooling/check_classification_rules.py` L91-97). `render_md` injects `cluster['name']` unescaped into the Summary table row (generator L260) and the cluster heading (L265). A pipe, CR, or LF in a cluster name silently corrupts the md table or heading. Both gates stay green because nothing reads the md back. Pack, chapter, and note fields already reject CR/LF (generator L121-124, L168-173) and already escape pipes in table cells (L270-272); cluster names are the one field left without either guard.

**WR-02 (rules-vs-map date).** check_release step 5g reads the map's own `generated_on` into the local `disk_on` and feeds it back into generator `--check` (`tooling/check_release.py` L321-329). Replay cannot fail on date drift by construction. The fidelity block in `check_rules` compares map_version, ordered cluster names, key sets, and is_support (L238-374), but never compares `rules.generated_on` to the live map's `generated_on`. Both files carry the field; live values agree at `2026-08-27`, so the gap is invisible until real drift happens.

**WR-03 (md freshness).** Generator `--check` compares JSON objects and returns before any md work (generator L332-349). `--sync-md` is optional and write-only. Nothing anywhere compares `docs/capability-pack-map.md` to a fresh render, so the human-readable map can go stale while every gate stays green. check_release has a render-and-compare precedent for `docs/packs.html` (RR-B-30, L206-221) with no equivalent for the map md.

## Goals

- Reject `|`, CR, LF, and tab in `cluster_names` at both enforcement points, before any write.
- Escape pipes in `render_md` as defense in depth for the renderer only. Validation rejects, the escaper never rewrites validated data.
- Fail on rules-vs-map `generated_on` drift from one home.
- Fail when `capability-pack-map.md` differs from a fresh render.
- Keep the clean tree byte-stable green. Confirmed by a read-only probe at spec time: generated JSON equals disk, full md text equals a fresh render, all 32 cluster names carry none of the rejected characters, and rules and map dates agree.

## Non-goals

- No `validate.yml` changes and no CI changes of any kind (P4/P5).
- No version trio, CHANGELOG, tag, or gh release work.
- No CONTRACT rewrite, GAP.md ledger refresh (P8), website YAML, pack content, or new packs.
- No check_release.py edits. The date check lands in `check_rules` and the md check lands in generator `--check`, both already invoked by check_release.
- No schema changes: `cluster_names` stays `list[str]`; both files keep the single `generated_on` field; no `disk_on` field appears on disk (it stays a check_release local).
- Leading and trailing whitespace in cluster names stay legal. Whitespace cannot corrupt md structure or replay stability because names render verbatim on both write and check paths; rejecting it would be a style rule outside this package's corruption scope.
- No `_deslop` on cluster names. `_deslop` rewrites em dashes, and em dashes stay legal in names, so a rewriter for a legal character would violate the reject-don't-rewrite constraint. Pack/chapter/note keep their existing `_deslop` plus escape untouched.

## Codebase context

Data flow (context gate, re-verified on live code): `docs/classification-rules.json` plus `docs/capability-pack-map-note-overrides.json` feed `generate_map()`, which writes `docs/capability-pack-map.json` (schema 2) and, with `--sync-md`, rewrites the Summary and cluster tables in `docs/capability-pack-map.md` while preserving the on-disk header verbatim up to `## Summary` (`_split_md_header`, generator L279-284).

Three surfaces own this work:

| File | Role here |
|------|-----------|
| `tooling/generate_capability_map.py` | WR-01 validation (L77-83) and escape (L245-276); WR-03 `--check` extension (L332-349) |
| `tooling/check_classification_rules.py` | WR-01 validation (L91-97); WR-02 fidelity compare (near L242-247) |
| `tooling/check_release.py` | No edits. Step 5f runs check_rules (L295-306); step 5g runs generator `--check` (L308-343) and propagates the return code |

Constraints carried from the package and repo:

- Stdlib only. No new third-party imports.
- H-07: sibling checkers never import the generator; checkers load JSON independently. The forbidden-character check is therefore duplicated in the two files, same discipline as the already-duplicated shape checks, `MAP_VERSION_RE`, and `SUPPORT_SUFFIX`.
- Fail-closed idioms stay: the generator raises `ValueError` from `generate_map` and prints `FAIL:` / `PASS:` from `main()`; `check_rules` collects errors with `fail()` and exits nonzero when the list is non-empty; check_release wraps each step in a `[tag]` (`[classification-rules]`, `[map-replay]`).
- Validation must fire before any write. `main()` calls `generate_map` before either file write, and the `--sync-md` path already computes md text before writing JSON (generator L351-368).

## Design

### WR-01: cluster_names validation and md escaping

**Rejected character set: `|`, `\r`, `\n`, `\t`.** Shared constant in both files:

```python
_CLUSTER_NAME_FORBIDDEN = ("|", "\r", "\n", "\t")
```

Rationale per character: pipe breaks md table cells and is the one character the renderer's escaper would rewrite, so it must be rejected up front rather than silently converted; CR and LF turn one heading or row into two and corrupt the md line structure; tab is in the same control-character family as CR/LF, has no legitimate use in a cluster name, and renders as alignment noise inside cells and headings. Leading and trailing whitespace are deliberately not rejected (see Non-goals).

**Generator enforcement** (`generate_map`, after the existing shape check at L77-83; the shape check and its message stay as-is):

```python
for i, name in enumerate(cluster_names):
    if any(c in name for c in _CLUSTER_NAME_FORBIDDEN):
        raise ValueError(
            f"rules cluster_names[{i}] contains a forbidden character "
            f"(|, CR, LF, tab): {name!r}"
        )
```

The message names the index and the offending value, mirroring the existing assignments/notes messages (`assignments[{i}]: pack contains CR or LF: {pack!r}`). Because `generate_map` raises during build, `main()` prints `FAIL: ...` and returns 1 before `MAP_PATH` or `MD_PATH` is touched, so the write-before-validate hole stays closed on every mode (`--generated-on` write, `--sync-md`, `--check`).

**Checker enforcement** (`check_rules`, after the existing shape check at L91-97; the shape check keeps its `cluster_names = []` fallback, which makes the loop a no-op on shape failure):

```python
for i, name in enumerate(cluster_names):
    if any(c in name for c in _CLUSTER_NAME_FORBIDDEN):
        fail(
            errs,
            f"envelope: cluster_names[{i}] contains a forbidden character "
            f"(|, CR, LF, tab): {name!r}",
        )
```

Prefixes follow the files' existing conventions: `rules cluster_names[...]` in the generator, `envelope: cluster_names[...]` in the checker.

**Renderer escape.** In `render_md`, escape the pipe on both name injection sites. This is defense in depth for future callers of `render_md`; on live paths the name has already passed validation, so the escape never fires and md bytes are unchanged on a clean tree.

```python
for i, cluster in enumerate(clusters, start=1):
    n = len(cluster["chapters"])
    total += n
    name = cluster["name"].replace("|", "\\|")
    lines.append(f"| {i}. {name} | {n} |")
# ...
for i, cluster in enumerate(clusters, start=1):
    name = cluster["name"].replace("|", "\\|")
    lines.append(f"## {i}. {name}")
```

Only `|` becomes `\|`; nothing else is substituted. The heading is not a table cell, so a pipe there is cosmetic, but escaping both sites with one line each keeps a single rule: no unescaped pipe can enter the rendered md. GFM renders `\|` as `|`, so even the defense-in-depth output reads correctly. The byte-stability constraint holds because the only character the escaper changes is the one character validation rejects: a name the escaper would rewrite can never reach a write.

### WR-02: rules-vs-map generated_on cross-check

**Home: the fidelity block of `check_rules`** (option A), immediately after the map_version compare (L242-247), mirroring its exact shape:

```python
live_on = live.get("generated_on")
if live_on != generated_on:
    fail(
        errs,
        f"fidelity: rules generated_on {generated_on!r} != live map {live_on!r}",
    )
```

`generated_on` is the local already extracted from the rules envelope at L63. No `None` guard: the map_version compare above has none either, a missing envelope date already fails its own shape check at L63-67, and one extra fidelity line of consistent noise matches the house style.

**Why fidelity and not the replay feed (option B).** Feeding the rules date into 5g would make `--check` detect the same drift through its envelope diff, but it changes what replay proves (from "the on-disk map reproduces from rules plus its own recorded date" to a mixed content-plus-date assertion) and the failure surfaces as a generic envelope diff inside the generator instead of a named rules-vs-map statement. It also edits check_release, a Phase 21 folded path, for a comparison the fidelity block can carry with six lines in a file already dedicated to rules-vs-map agreement. Detection is equivalent; A is smaller and says the failure out loud.

**Why not both (option C).** Two homes for one invariant means two places to update when date semantics change. One home, the one that already owns every other rules-vs-map comparison.

**check_release stays untouched.** Step 5f runs before 5g, so date drift fails the release gate through the existing `[classification-rules]` wrapper. 5g keeps reading `disk_on` from the map; its job remains proving the on-disk file reproduces.

### WR-03: md freshness gate in --check

**Owner: generator `--check`** (option A), extending the existing block at L332-349. The JSON compare stays first with its early return; md is downstream of JSON because JSON is the md's source of truth.

```python
if args.check:
    try:
        disk = _load_json(MAP_PATH, "map")
    except ValueError as exc:
        print(f"FAIL: {exc}")
        return 1
    if built != disk:
        # ... existing envelope diff prints unchanged ...
        return 1
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

Decisions inside this block:

- **Full-text compare (header plus rendered body), not body alone.** `--sync-md` preserves the on-disk header verbatim, so after any legitimate sync the full text equals `render_md(built, _split_md_header(existing))` exactly. The loop is self-consistent: a human header edit fails `--check`, and rerunning `--sync-md` keeps the edited header and regenerates the body, after which `--check` passes. A body-only compare would miss header edits that break `_split_md_header` on a later run.
- **Missing md and missing `## Summary` fail closed.** The explicit `is_file` guard gives a clean message; `_split_md_header` keeps its existing `ValueError` for a missing marker, caught and printed with the `FAIL: md check:` prefix.
- **The stale message embeds the actual date.** At that point `args.generated_on` equals the matched disk envelope date, so the printed rerun command is copy-paste runnable, matching the RR-B-30 precedent of an actionable stale message.
- **check_release needs no change.** 5g calls `main(["--generated-on", disk_on, "--check"])` and propagates the return code (L328-336), so the freshness gate rides the existing `[map-replay]` step.

Operator-visible behavior change: `--check` now also asserts md freshness and fails without `--sync-md` when the md is stale or missing. The generator's module docstring gets one line noting this during implementation. `--sync-md` write behavior is unchanged, including its render-before-write order.

### Failure UX summary

- Generator `ValueError`: `rules cluster_names[{i}] contains a forbidden character (|, CR, LF, tab): {name!r}`, printed by `main()` as `FAIL: ...`, exit 1, nothing written.
- `check_rules`: `envelope: cluster_names[{i}] contains a forbidden character (|, CR, LF, tab): {name!r}`, collected, exit 1 under the `FAIL: n issue(s)` report.
- `check_rules` fidelity: `fidelity: rules generated_on {rules!r} != live map {map!r}`.
- Generator `--check`: `FAIL: md check: capability-pack-map.md missing`, or `FAIL: md check: capability-pack-map.md missing ## Summary heading`, or `FAIL: capability-pack-map.md is stale; rerun tooling/generate_capability_map.py --generated-on <date> --sync-md`, each exit 1 after the JSON PASS line.

## Verification

One new file, `tooling/test_generate_capability_map.py`, in the house assert style modeled on `tooling/test_link_policy.py`: module docstring with a run line, `main() -> int`, plain asserts, stdlib only, `print("generate-capability-map tests: OK")`, exit 0 on success. No pytest, no fixtures framework.

Probes:

- **(a) Fail-closed on every rejected character in both entry points.** For each of `|`, `\r`, `\n`, `\t`: a rules fixture with one name carrying that character makes `generate_map` raise `ValueError` naming the index, and `check_rules` (with an in-memory `live_map` fixture and default `packs_root`) returns an error list containing the `envelope: cluster_names[...]` message. Uses the existing `live_map` parameter, so no disk writes.
- **(b) Renderer escape at fixture level.** A hand-built map object with a pipe-bearing name renders `\|` in both the Summary row and the heading, and no unescaped pipe appears in either line. A clean name passes through byte-identical, proving the clean-tree render is unchanged.
- **(c) Stale, missing, and fresh md under `--check`.** Point the module's `MAP_PATH`/`MD_PATH` attributes at files in a `tempfile.TemporaryDirectory` (restore in `finally`): with matching JSON and one altered md byte, `main(["--generated-on", D, "--check"])` returns 1 and prints the stale message; with the md file absent, returns 1; with a fresh render, returns 0.
- **(d) Date drift fails.** `check_rules` with rules `generated_on = "2026-01-01"` and a `live_map` at `"2026-02-02"` yields the `fidelity: rules generated_on` error; equal dates yield none.
- **(e) Clean tree stays byte-stable green.** `main(["--generated-on", <live map generated_on>, "--check"])` returns 0 and writes nothing, `render_md(built, _split_md_header(disk_md)) == disk_md` by full text, and rules and map `generated_on` are equal. This held at spec time on the unmodified tree (32 cluster names, dates `2026-08-27`), so the post-change gate must also pass without touching any doc.

Gate coverage with zero check_release edits: 5f picks up (a, checker side) and (d); 5g picks up (a, generator side) and (c). Run lines: `python tooling/test_generate_capability_map.py`, then `python tooling/check_release.py`. The test file stays free of banned hosts and leak sentinels because check_release scans `tooling/*.py`.

## Research

research: skipped (in-repo stdlib tooling hardening only; no external APIs, libraries, platforms, or version-sensitive choices)

## Approach

Three small edits on surfaces Phase 21 already owns, plus one assert-based probe file. WR-01: a four-character reject set (`|`, CR, LF, tab) enforced in `generate_map` and `check_rules` ahead of any write, with a pipe-only escape as renderer defense in depth. WR-02: a single date comparison in the `check_rules` fidelity block, matching the map_version pattern, leaving check_release 5g untouched. WR-03: `--check` extends its JSON compare with a full-text md freshness compare, covered by the release gate through the existing 5g return code. Estimated size: roughly 15 lines in the generator, 10 in the checker, and a test file near 130 lines. The clean tree is verified byte-stable green at HEAD, so no shipped file changes.

## Open questions

None. The four decisions are locked: reject set and its whitespace carve-out, fidelity as the date-check home, `--check` as the md freshness owner, and assert-style probes in the house test format.
