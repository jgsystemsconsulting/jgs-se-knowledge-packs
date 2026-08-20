---
phase: 17-tooling-in-02-fut-05
plan: 01
subsystem: tooling
tags: [check_overlap, check_release, capability-map, FUT-05, TOOL-20, stdlib]

requires:
  - phase: 12
    provides: "check_release dual-gate pattern and in-process check_capability_map.main()"
  - phase: 16
    provides: "capability map TOTAL 644 / map_version 1.19.0 baseline"
provides:
  - "tooling/check_overlap.py multi-pack chapter-basename collision gate with WHITELIST"
  - "in-process check_overlap.main() wire on check_release release path"
  - "CONTRACT §7 overlap thresholds/whitelist and §8 FUT-05 residual (no full generator)"
affects:
  - "18-v1-19-1-release-surface"
  - "local release readiness (check_release)"

actuals:
  tokens: 4200
  tasks: 3
  commits: 4

tech-stack:
  added: []
  patterns:
    - "stdlib in-process gate via check_*.main() before map check"
    - "WHITELIST module constant for intentional shared chapter basenames"
    - "honest FUT residual: mechanical checker slice vs agent classification"

key-files:
  created:
    - tooling/check_overlap.py
    - .planning/phases/17-tooling-in-02-fut-05/17-01-SUMMARY.md
  modified:
    - tooling/check_release.py
    - docs/capability-map-CONTRACT.md

key-decisions:
  - "Scan only packs/*/chapters/*.md so pack-root support files never false-fail"
  - "WHITELIST = {ch01-introduction.md} only live multi-pack collision (3 packs)"
  - "FUT-05 residual refuses byte-stable full-map generator; Phase 18 owns map_version"
  - "CI fence stays: validate.yml never executes checked-out repository code; check_overlap absent"

patterns-established:
  - "Overlap gate mirrors map gate: import check_X; rc = check_X.main(); fail on non-zero"
  - "CONTRACT documents local/trusted gates without scheme strings or CI repo-Python claims"

requirements-completed: [TOOL-20-01, TOOL-20-02, TOOL-20-03]

coverage:
  - id: D1
    description: "stdlib check_overlap.py detects un-whitelisted multi-pack chapter basename collisions; WHITELIST covers ch01-introduction.md"
    requirement: TOOL-20-01
    verification:
      - kind: other
        ref: "python tooling/check_overlap.py → OVERLAP: PASS"
        status: pass
      - kind: other
        ref: "python -c WHITELIST/dups assert → OVERLAP_ASSERT_OK"
        status: pass
    human_judgment: false
  - id: D2
    description: "check_release imports check_overlap and calls check_overlap.main() in-process; thresholds/whitelist documented in CONTRACT §7"
    requirement: TOOL-20-02
    verification:
      - kind: other
        ref: "python tooling/check_release.py → RELEASE CHECK: PASS (prints OVERLAP: PASS)"
        status: pass
      - kind: other
        ref: "CONTRACT contains check_overlap + ch01-introduction.md + WHITELIST"
        status: pass
    human_judgment: false
  - id: D3
    description: "CONTRACT §8 FUT-05 residual names mechanical check_capability_map slice and agent judgment; no full-map generator claimed"
    requirement: TOOL-20-03
    verification:
      - kind: other
        ref: "CONTRACT FUT-05 section + byte-stable full-map generator refusal"
        status: pass
      - kind: other
        ref: "python tooling/check_capability_map.py → PASS TOTAL 644 map_version 1.19.0"
        status: pass
    human_judgment: false

duration: 25min
completed: 2026-08-20
status: complete
---

# Phase 17 Plan 01: Tooling IN-02 + FUT-05 Residual Summary

**Stdlib multi-pack chapter-basename overlap gate on the release path, with honest FUT-05 residual (mechanical map checker slice; agent classification not a generator)**

## Performance

- **Duration:** ~25 min (resume after partial prior agent)
- **Started:** 2026-08-20T11:54:21Z
- **Completed:** 2026-08-20T12:00:00Z
- **Tasks:** 3/3
- **Files modified:** 4 (check_overlap.py, check_release.py, capability-map-CONTRACT.md, 17-01-SUMMARY.md)

## Accomplishments

- Shipped `tooling/check_overlap.py`: stdlib scan of `packs/*/chapters/*.md`, `WHITELIST = {"ch01-introduction.md"}`, prints `OVERLAP: PASS` / `OVERLAP: FAIL`.
- Wired in-process into `tooling/check_release.py` at block `# 5d. overlap (TOOL-20)` immediately before map block `# 5e`; docstring items 8–9 list both local/trusted gates.
- Documented CONTRACT **§7 Chapter basename overlap gate** (scan scope, zero un-whitelisted threshold, whitelist rationale) and **§8 FUT-05 residual** (mechanical slice vs agent judgment; no byte-stable full-map generator).
- Both local gates green; version trio and `map_version` stay `1.19.0`; TOOL-20 boxes left open; CI fence intact (MJ-01).

## Task Commits

1. **Task 1 (tracer): End-to-end overlap check** - `84a0f35` (fix)
2. **Task 2: Document overlap thresholds and whitelist** - `cf1d361` (docs)
3. **Task 3: FUT-05 residual in CONTRACT** - (this session; docs commit for CONTRACT)
4. **Task 3: SUMMARY** - (this session; docs commit for SUMMARY)

_Note: Prior agent completed Tasks 1–2 and drafted §8 residual uncommitted; resume agent verified gates, finished residual commit + SUMMARY._

## Files Created/Modified

- `tooling/check_overlap.py` — multi-pack chapter-basename collision gate; export `WHITELIST`
- `tooling/check_release.py` — `import check_overlap`; `rc = check_overlap.main()` before map; docstring gate list
- `docs/capability-map-CONTRACT.md` — §7 overlap gate; §8 FUT-05 residual
- `.planning/phases/17-tooling-in-02-fut-05/17-01-SUMMARY.md` — this file

## must_haves evidence

| Truth | Evidence |
|---|---|
| `check_overlap.py` exits 0; only live collision `ch01-introduction.md` in WHITELIST | `OVERLAP: PASS`; runnable assert `OVERLAP_ASSERT_OK` |
| `check_release` imports/calls `check_overlap.main()` in-process; still PASS | `OVERLAP_WIRE_OK`; stdout includes `OVERLAP: PASS` then map TOTAL 644 then `RELEASE CHECK: PASS` |
| Thresholds + whitelist documented (docstring + CONTRACT) | Module docstring; CONTRACT §7 |
| FUT-05 residual honest; no full generator claimed | CONTRACT §8: "This milestone does **not** claim a byte-stable full-map generator." |
| Map gate PASS; schema 2; map_version 1.19.0; catalog 63 / dirs 65 | `PASS: capability map OK`; `TOTAL: 644`; `VERSIONS_OK` |
| Version trio 1.19.0; no v1.19.1 tag; validate.yml not given repo-Python step | `VERSIONS_OK`; `git tag -l 'v1.19*'` → `v1.19.0` only; `CI_FENCE_OK` |
| TOOL-20-01..03 boxes unchecked | `BOXES_OPEN` |
| No new deps; stdlib only; no packs/ edits | no package installs; pathspecs tooling/ + docs/ + SUMMARY only |
| Idempotent single wire/sections | single import block; single §7 and §8 |

### Gate stdout (resume verification)

```
OVERLAP: PASS
...
TOTAL: 644
PASS: capability map OK
...
OVERLAP: PASS
...
TOTAL: 644
PASS: capability map OK
RELEASE CHECK: PASS — repo is release-ready against the mechanical gate.
OVERLAP_ASSERT_OK
OVERLAP_WIRE_OK
CONTRACT_OK
CI_FENCE_OK
VERSIONS_OK 1.19.0 schema 2
BOXES_OPEN
```

### OVERLAP_ASSERT_OK command

```bash
python -c "import sys; from pathlib import Path; sys.path.insert(0, str(Path('tooling').resolve())); import check_overlap; assert 'ch01-introduction.md' in check_overlap.WHITELIST; chaps={}; root=Path('.').resolve();
[chaps.setdefault(p.name, []).append(p.parent.parent.name) for p in (root/'packs').glob('*/chapters/*.md')]; dups={k:v for k,v in chaps.items() if len(v)>1}; assert set(dups)=={'ch01-introduction.md'}, dups; assert not {k:v for k,v in dups.items() if k not in check_overlap.WHITELIST}; print('OVERLAP_ASSERT_OK')"
```

Observed: `OVERLAP_ASSERT_OK`

### Insertion point (`check_release.py`)

```python
# 5d. overlap (TOOL-20): multi-pack chapter-basename collisions (same process)
try:
    import check_overlap  # type: ignore
    rc = check_overlap.main()
    if rc != 0:
        fail(errs, "[overlap] check_overlap.py failed (see output above)")
except Exception as e:
    fail(errs, f"[overlap] check_overlap failed to run: {e}")

# 5e. MAP-19-04: capability-pack map freshness (same process; prints its own counts)
```

### CONTRACT residual sentence (FUT-05 generator refusal)

> This milestone does **not** claim a byte-stable full-map generator. The refresh path in section 4 remains the agent classification pass plus the map checker.

### MJ-01 CI fence

Split assert (do not edit `validate.yml`):

```python
t = Path('.github/workflows/validate.yml').read_text(encoding='utf-8')
assert 'never' in t
assert 'executes checked-out repository code' in t
assert 'check_overlap' not in t
```

Result: `CI_FENCE_OK`. `check_overlap` absent from workflow.

## Decisions Made

- Followed plan: in-process overlap before map; no subprocess; no CI repo-Python; no version bumps; TOOL-20 boxes stay open until phase.complete/verify.
- FUT-05 residual documents mechanical slice already in `check_capability_map.py` and keeps cluster/note as agent procedure.

## Deviations from Plan

None.

_Resume note (not a deviation): prior executor crashed after Tasks 1–2 commits with §8 FUT-05 residual already written but uncommitted in `docs/capability-map-CONTRACT.md`. Resume verified both gates, committed residual + SUMMARY. Did not recreate `check_overlap.py`._

## Issues Encountered

- Prior agent partial crash left dirty CONTRACT with complete §8 text — finished by committing residual rather than rewriting.

## User Setup Required

None - no external service configuration required.

## Next Phase Readiness

- IN-02 overlap gate live on local release path; FUT-05 residual documented honestly.
- Phase 18 owns public v1.19.1 surface (`map_version`, plugin.json, CHANGELOG, RELEASE-INFO, tag).
- TOOL-20-01..03 remain unchecked for verify / phase.complete.
- Leftovers not stolen: no packs rebuild, no full map generator, no CI validate.yml edit.

## Phase 18 leftovers (explicit non-scope)

- Do not bump `map_version` / version trio / CHANGELOG top / RELEASE-INFO
- Do not create `v1.19.1` tag
- Do not tick TOOL-20 requirement boxes here

---
*Phase: 17-tooling-in-02-fut-05*
*Completed: 2026-08-20*
