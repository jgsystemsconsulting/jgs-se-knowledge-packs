---
phase: 17-tooling-in-02-fut-05
reviewed: 2026-08-20T13:45:00Z
depth: deep
files_reviewed: 9
files_reviewed_list:
  - tooling/check_overlap.py
  - tooling/check_release.py
  - docs/capability-map-CONTRACT.md
  - .planning/phases/17-tooling-in-02-fut-05/17-01-PLAN.md
  - .planning/phases/17-tooling-in-02-fut-05/17-01-SUMMARY.md
  - .planning/phases/17-tooling-in-02-fut-05/17-RESEARCH.md
  - .planning/phases/17-tooling-in-02-fut-05/17-PATTERNS.md
  - .planning/phases/17-tooling-in-02-fut-05/17-PLAN_CHECK.md
  - .planning/phases/17-tooling-in-02-fut-05/17-PLAN_REVIEW.md
findings:
  critical: 0
  warning: 2
  info: 4
  total: 6
status: issues_found
verdict: PASS_WITH_NOTES
---

# Phase 17: Code Review Report

**Reviewed:** 2026-08-20T13:45:00Z  
**Depth:** deep (source + planning artifacts + live gates + cross-module wire)  
**Files Reviewed:** 9  
**Status:** issues_found  
**Verdict:** PASS_WITH_NOTES

## Summary

Phase 17 ships TOOL-20-01..03 as planned: stdlib `tooling/check_overlap.py` with `WHITELIST = {"ch01-introduction.md"}`, in-process wire in `check_release.py` `# 5d` before map `# 5e`, CONTRACT §7 thresholds/whitelist and §8 FUT-05 residual that **refuses** a byte-stable full-map generator. Live re-run this review:

```
OVERLAP: PASS                              (rc=0)
PASS: capability map OK  TOTAL: 644       (rc=0)
RELEASE CHECK: PASS                        (rc=0; prints OVERLAP then map)
OVERLAP_ASSERT_OK                          dups == {ch01-introduction.md: 3 packs}
OVERLAP_WIRE_OK                            single import + main()
FUT05_RESIDUAL_OK                          map_version 1.19.0 schema 2; residual sentence present
CI_FENCE_OK                                split: never + executes checked-out…; check_overlap absent
BOXES_OPEN                                 TOOL-20-01..03 still - [ ]
FAIL_PATH_OK                               empty WHITELIST → OVERLAP FAIL rc=1; restore → 0
catalog 63 / packs dirs 65
SOURCE-VETTING http=0; CONTRACT http=0
git tag v1.19* → v1.19.0 only
no tooling/generate_capability_map.py
```

No BLOCKER. Two WARNINGs (dead `errs` accumulator; silent PASS if `packs/` missing). TOOL-20 coverage complete; FUT-05 residual honest (no false full-regen claim). MJ-01 (contiguous CI phrase) already folded in SUMMARY split assert — not re-opened. Scope fences hold (no version/map bump, no packs/, no validate.yml edit, no CI repo-Python).

Prior sibling gates this phase: impl_review PASS_WITH_NOTES, integration PASS, security SECURED — this full-scope code_review agrees on ship readiness with notes only.

## TOOL-20 coverage

| ID | Intent | Evidence | Status |
|----|--------|----------|--------|
| TOOL-20-01 | Stdlib overlap checker under tooling/ | `tooling/check_overlap.py`; glob `packs/*/chapters/*.md`; WHITELIST; exit 0/1 | **COVERED** |
| TOOL-20-02 | Wire into release path; thresholds; no support-file false-fail | `check_release.py:216-223` in-process `check_overlap.main()`; CONTRACT §7; support files excluded by chapters/ scope | **COVERED** |
| TOOL-20-03 | Mechanical slice + residual agent procedure; no false full-closed | CONTRACT §8 names `check_capability_map` mechanical slice; agent cluster/note; "does **not** claim a byte-stable full-map generator" | **COVERED** (honest residual) |

Live REQUIREMENTS boxes remain unchecked (correct — verify / phase.complete owns ticks).

## Critical Issues

None.

## Warnings

### WR-01: `errs` / `fail` in `check_overlap.main` are write-only

**File:** `tooling/check_overlap.py:37-60`  
**Severity:** WARNING  
**Issue:** `fail(errs, msg)` appends to `errs`, but the FAIL path never reads `errs`. Reporting is pure `print` + `return 1`. Sibling `check_capability_map.py` aggregates `errs` and prints them in a final block. Dead accumulator is pattern drift and invites a future edit that fills `errs` without printing. Exit codes and release wire are still correct today (`check_release` keys off `rc != 0`).  
**Fix:** Prefer the map-checker shape:

```python
def main() -> int:
    errs: list[str] = []
    chaps: dict[str, list[str]] = {}
    packs_root = ROOT / "packs"
    if packs_root.is_dir():
        for p in sorted(packs_root.glob("*/chapters/*.md")):
            chaps.setdefault(p.name, []).append(p.parent.parent.name)

    collisions = {name: packs for name, packs in chaps.items() if len(packs) > 1}
    bad = {name: packs for name, packs in collisions.items() if name not in WHITELIST}

    for name in sorted(bad):
        fail(errs, f"{name}: {', '.join(sorted(bad[name]))}")

    if errs:
        print(f"OVERLAP: FAIL ({len(errs)} issue(s))")
        for msg in errs:
            print(f"  {msg}")
        return 1
    print("OVERLAP: PASS")
    return 0
```

Or drop `errs`/`fail` entirely and print only. Either is fine; pick one style and stick to it.

### WR-02: Missing `packs/` directory yields silent OVERLAP PASS

**File:** `tooling/check_overlap.py:45-63`  
**Severity:** WARNING  
**Issue:** If `ROOT / "packs"` is not a directory, the scan loop is skipped and the function prints `OVERLAP: PASS` / returns 0. Standalone misuse (wrong checkout, broken install) green-lights an empty tree. On the normal `check_release` path other steps still fail without packs, so release readiness is not fully bypassed — but the overlap gate itself is not fail-closed.  
**Fix:**

```python
packs_root = ROOT / "packs"
if not packs_root.is_dir():
    print("OVERLAP: FAIL (1 issue(s))")
    print("  packs/ directory missing")
    return 1
for p in sorted(packs_root.glob("*/chapters/*.md")):
    ...
```

## Info

### IN-01: SUMMARY `requirements-completed` vs open REQUIREMENTS boxes

**File:** `17-01-SUMMARY.md` frontmatter `requirements-completed: [TOOL-20-01, TOOL-20-02, TOOL-20-03]`  
**Issue:** Frontmatter marks IDs complete while live `.planning/REQUIREMENTS.md` still has three `- [ ] **TOOL-20-0x` lines (intentional per plan). Downstream must not treat SUMMARY frontmatter as box-tick.  
**Fix:** None for this phase. verify / phase.complete owns ticks. Optional clarifying note already present in SUMMARY body.

### IN-02: `check_overlap.py` omitted from authored-header list (intentional)

**File:** `tooling/check_release.py:234-241`  
**Issue:** New checker is not on the JGSC/SPDX authored-file list. Same treatment as `check_capability_map.py`; plan explicitly forbids adding it. File itself carries correct headers.  
**Fix:** None. Keep parity with map checker unless a later phase expands the authored list for all `tooling/check_*.py`.

### IN-03: `check_release` section labels `5d`/`5e` sit after `6b`

**File:** `tooling/check_release.py:216-232`  
**Issue:** Comment numbers are historical (`5d` overlap / `5e` map after `6` / `6b`). Docstring items 8–9 correctly describe order. Confusing for readers grepping step numbers; not a behavioral bug.  
**Fix:** Optional later renumber of body comments to match docstring (out of Phase 17 must-have scope).

### IN-04: WHITELIST is basename-only (pack set not enforced)

**File:** `tooling/check_overlap.py:32-34`; CONTRACT §7  
**Issue:** CONTRACT rationale names three packs for `ch01-introduction.md`. Gate does not assert pack membership — a fourth pack adding the same basename still PASSes. Matches plan (basename whitelist). Documented intentional shared name stays open-ended by design.  
**Fix:** Only if product later wants pack-set pinning: `WHITELIST = {"ch01-introduction.md": frozenset({...})}` and fail on unexpected pack membership. YAGNI for current TOOL-20.

## FUT-05 residual honesty

| Claim check | Result |
|-------------|--------|
| CONTRACT claims full-map generator? | **No** — §8: "This milestone does **not** claim a byte-stable full-map generator." |
| Mechanical slice named? | **Yes** — `check_capability_map.py` envelope/staleness/existence/uniqueness/thresholds |
| Agent judgment residual named? | **Yes** — cluster assignment + `chapters[].note` |
| Generator file added? | **No** |
| Phase 18 owns `map_version`? | **Yes** (still `1.19.0`; no `v1.19.1` tag) |

Honest residual. No false full-regen claim.

## Cross-module wire (deep)

| Link | Expected | Observed |
|------|----------|----------|
| `check_release` → `check_overlap.main()` | in-process, fail on non-zero | `import check_overlap`; `rc = check_overlap.main()`; `fail(errs, …)` lines 216–223 |
| Order vs map | overlap before map | `# 5d` then `# 5e`; no early `return` between |
| `sys.path.insert` | single | count=1 at line 121 |
| subprocess | none | absent in both modules |
| CONTRACT → WHITELIST | documents `ch01-introduction.md` + three packs | §7 matches live dups |
| CI fence | no repo-Python / no check_overlap in validate.yml | split phrase present; `check_overlap` absent |

## Scope fences

| Fence | Status |
|-------|--------|
| Version trio 1.19.0 | PASS |
| `map_version` 1.19.0 / schema 2 / TOTAL 644 | PASS |
| No `v1.19.1` tag | PASS |
| No packs/ edits in execute commits | PASS |
| No validate.yml edit / no CI repo-Python step | PASS (MJ-01 handled via split assert) |
| TOOL-20 boxes open | PASS |
| Stdlib only / no new deps | PASS |
| Deviations ledger in SUMMARY | PASS (`None.` + resume note) |

## Counts

| Severity | Count |
|----------|------:|
| Critical / BLOCKER | 0 |
| Warning | 2 |
| Info | 4 |
| **Total** | **6** |

## Verdict rationale

Must-haves live-true. IN-02 gate works on PASS and FAIL paths. Release wire order and in-process shape match Phase 12 map pattern. FUT-05 residual is honest. MJ-01 closed without touching CI. WARNINGs are robustness/maintainability (dead `errs`, fail-open missing `packs/`) — not incorrect current-repo behavior. Ship Phase 17 tooling; optional cleanup of WR-01/WR-02 can ride a later tiny fix or Phase 18 if desired. TOOL-20 boxes stay for verify / phase.complete.

**Verdict: PASS_WITH_NOTES**

---

_Reviewed: 2026-08-20T13:45:00Z_  
_Reviewer: Claude (gsd-code-reviewer, code_review full-scope)_  
_Depth: deep_  
_Live gates: OVERLAP PASS · map PASS TOTAL 644 · RELEASE CHECK PASS · FAIL_PATH_OK · CI_FENCE_OK · BOXES_OPEN_
