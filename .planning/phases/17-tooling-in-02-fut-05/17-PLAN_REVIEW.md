# Phase 17 Plan Review

**Reviewed:** 2026-08-20
**Reviewer:** gsd-code-reviewer (plan review mode)
**Plan:** `.planning/phases/17-tooling-in-02-fut-05/17-01-PLAN.md`
**Plan check:** `17-PLAN_CHECK.md` (PASS_WITH_FIXES, 0 blockers, 2 warnings)
**Research:** `17-RESEARCH.md` (HIGH; overlap + honest FUT-05 residual)
**Patterns:** `17-PATTERNS.md` (basename whitelist; in-process gate wire; FUT-05 honesty)
**Requirements:** TOOL-20-01, TOOL-20-02, TOOL-20-03

**Verdict:** APPROVE_WITH_NOTES

---

## Summary

Single plan `17-01` ships IN-02 (stdlib overlap checker on the local release path) and an honest FUT-05 residual (mechanical slice already in `check_capability_map.py` + CONTRACT language for agent classification). Three tasks: tracer checker + in-process `check_release` wire, CONTRACT overlap docs + runnable WHITELIST assert, FUT-05 residual + SUMMARY.

Plan does **not** invent a full FUT-05 map generator, skip the release wire, or add non-stdlib deps. Honest residual is ROADMAP-legal TOOL-20-03 else-branch. Phase 18 still owns `map_version` / v1.19.1.

What keeps this off plain APPROVE: Task 3 CI-fence assert uses a contiguous header phrase that is line-wrapped in live `validate.yml`, and the plan forbids editing that file. Fold MAJOR into executor brief; no redesign.

---

## Blocker gate (hard fails)

| Gate | Result | Evidence |
|------|--------|----------|
| Invents full FUT-05 regen without proof? | PASS — forbidden | files_modified has no generate_capability_map.py; Task 3 must-NOT write a generator; CONTRACT residual must refuse byte-stable regen; RESEARCH says cluster assignment/note need judgment |
| Skips release wire? | PASS — required | Task 1 inserts in-process import check_overlap / check_overlap.main() before the existing map block; fail() on non-zero; no subprocess |
| Non-stdlib deps? | PASS — forbidden | stdlib only; no pip/npm/cargo; no pytest suite; PATTERNS optional tests/test_overlap.py omitted |
| Ticks live TOOL-20 boxes? | PASS — forbidden | Task 3 forbids; verify asserts three open TOOL-20-01..03 lines |
| Bumps version / tag / CI repo-Python? | PASS — forbidden | version trio stays 1.19.0; no v1.19.1 tag; validate.yml unnamed and unedited |
| Invents packs? | PASS — forbidden | files_modified tooling + CONTRACT + SUMMARY only |

**BLOCKER count: 0**

---

## Coverage vs TOOL-20

| ID | Live SoT intent | Plan delivery | Status |
|----|-----------------|---------------|--------|
| TOOL-20-01 | Minimal stdlib overlap checker under tooling/ | Task 1 tracer: check_overlap.py, WHITELIST ch01-introduction.md, glob packs/*/chapters/*.md | COVERED |
| TOOL-20-02 | Wire into check_release (or documented mandatory step); thresholds; no support-file false-fail | Task 1 in-process main() + Task 2 CONTRACT + runnable assert | COVERED |
| TOOL-20-03 | Generator for mechanical fields, or largest deterministic slice + residual agent procedure; no full-closed claim without proof | Task 3 CONTRACT residual; existing check_capability_map is the mechanical slice | COVERED (honest residual) |

---

## Spot-check (plan claims vs disk)

| Claim | Observed (this review) | Match |
|-------|------------------------|-------|
| Branch is main | main | Yes |
| check_overlap.py absent | no such file | Yes |
| Version trio 1.19.0 | plugin / CHANGELOG / RELEASE-INFO | Yes |
| map_version 1.19.0 schema 2 entries 644 | 1.19.0 / 2 / 644 | Yes |
| Catalog 63 / packs dirs 65 | 63 / 65 | Yes |
| TOOL-20-01..03 unchecked | three open boxes | Yes |
| Tags v1.19.0 only | v1.19.0 | Yes |
| glob chapters collisions | 536 files / 534 unique / ch01-introduction.md in dau-se-guidebook, nasa-npr-7123, nasa-system-safety | Yes |
| Support files at pack root | glossary/patterns/cheatsheet 63 each | Yes |
| SOURCE-VETTING http | 0 | Yes |
| CONTRACT no FUT-05 / no check_overlap | 112 lines; neither string present | Yes (plan said 113; off by 1, non-blocking) |
| check_release map import ~217; sys.path.insert present; no overlap import | True | Yes |
| validate.yml never-executes contiguous phrase | False — header wraps after never; executes checked-out repository code present; check_overlap absent | Fail phrase — MJ-01 |
| All automated python -c payloads compile | 6/6 COMPILE OK; tabs=0 | Yes |
| estimate 32000 vs 100000 | over_budget false; confidence low; sample_count 0 | Yes |

RESEARCH vs plan (plan wins, correctly): PATTERNS/RESEARCH skeleton uses rglob("chapters/*.md"); plan uses glob("*/chapters/*.md"). Live dups identical. Plan is the tighter documented scan.

---

## Findings

### BLOCKER

None.

Plan will not invent a full FUT-05 generator, will not skip the check_release in-process wire, and will not add non-stdlib dependencies.

### MAJOR (fold into executor brief)

1. **MAJOR — MJ-01: Task 3 CI-fence assert cannot pass on live validate.yml**
   **File:** `17-01-PLAN.md` Task 3 automated verify (CI python -c)
   **Issue:** Asserts contiguous `never executes checked-out repository code` in t. Live `.github/workflows/validate.yml` header wraps after `never` onto `# executes checked-out repository code`. Contiguous substring is absent. Action forbids editing validate.yml. Closing verify false-fails even when overlap/map/release gates and FUT-05 residual are correct. Same as 17-PLAN_CHECK W1.
   **Fix (executor brief):** Split the assert: `never` in t and `executes checked-out repository code` in t; keep `check_overlap` absent. Do **not** unwrap the YAML comment. Do **not** add a repo-Python CI step.
   **Fold:** Pre-execute one-line plan edit **or** executor detune-in-place then run Task 3 verify.

### MINOR

1. **MINOR — MN-01: claim_verification quotes the same contiguous CI phrase**
   **File:** 17-01-PLAN.md claim_verification CI row
   **Issue:** Intent (CI does not exec repo Python; overlap/map unnamed) is live-true. Quoted contiguous string is not. Same as W2.
   **Fix:** Optional reword. Do not add a CI repo-Python step.

2. **MINOR — MN-02: CONTRACT line count 113 vs live 112**
   **File:** claim_verification CONTRACT row
   **Issue:** Residual/FUT-05-absent claim is accurate; line count off by 1.
   **Fix:** None required for execute.

3. **MINOR — MN-03: Task 3 agent-in-CONTRACT already true on live CONTRACT**
   **File:** Task 3 automated verify
   **Issue:** CONTRACT already says agent consumption / se-agents. Distinguishing conjunct is FUT-05 (absent live). Residual only.
   **Fix:** Optional; executor must still write the residual section that refuses a full generator.

4. **MINOR — MN-04: PATTERNS rglob vs plan glob**
   **File:** 17-PATTERNS.md / 17-RESEARCH.md skeleton
   **Issue:** Plan correctly documents glob("*/chapters/*.md"). Live measurement matches rglob dups. No execute defect.
   **Fix:** None required. Do not edit RESEARCH/PATTERNS this plan.

5. **MINOR — MN-05: Task 3 does not assert CONTRACT http=0**
   **File:** Task 3 verify greps SOURCE-VETTING http, not CONTRACT
   **Issue:** Action forbids scheme strings in CONTRACT. Live CONTRACT http count is 0. Residual only.
   **Fix:** Executor keep CONTRACT locator-free; optional grep in SUMMARY.

---

## plan_check PASS_WITH_FIXES justification

| Dimension | Assessment |
|-----------|------------|
| Requirement coverage | All three TOOL-20 IDs in frontmatter + tasks; TOOL-20-03 honest residual is ROADMAP-legal |
| Task completeness | files / action / verify / done; insert point before 5d map block; WHITELIST named |
| Scope / prohibitions | No generator; no pip/pytest; no version bump; no CI repo-Python; no TOOL-20 ticks; pathspec commits; main only |
| Claim verification | Present, command-backed; file/git rows re-spot-checked true except wrapped CI phrase |
| Research conflict | Explicit plan-wins on glob vs rglob; live dups identical |
| Patterns | Overlap whitelist / in-process wire / FUT-05 honesty / stdlib; correctly skips optional pytest file |
| Verification derivation | WARN justified — W1 CI phrase = MJ-01 below, not a blocker |

Checker 0 blockers / 2 warnings map onto MJ-01 + MN-01. No hidden revision loop. No phase split.

---

## Executor-brief fold list (APPROVE_WITH_NOTES)

Copy into execute brief:

1. **Detune Task 3 CI assert** so it matches the wrapped validate.yml header (`never` + `executes checked-out repository code` as separate substrings). Keep `check_overlap` absent. Do not edit validate.yml.
2. **T1 overlap checker:** stdlib; WHITELIST exactly `ch01-introduction.md`; scan `packs/*/chapters/*.md` only; in-process `check_overlap.main()` immediately before the existing map block; reuse existing sys.path.insert; no subprocess; no REQUIRED_FILES / authored-header add.
3. **T2/T3 CONTRACT:** edit-only (keep HTML copyright comment); overlap section then FUT-05 residual that refuses a byte-stable full generator; no scheme strings; do not bump example map_version.
4. **Never:** generate_capability_map.py; pip/pytest; packs/; version trio / map_version / v1.19.1 tag; tick TOOL-20 boxes; git add -A; CI repo-Python step.
5. **SUMMARY:** overlap path + WHITELIST, insertion point, both-gate stdout, OVERLAP_ASSERT_OK, residual sentence quote, `## Deviations` (None. valid).

Optional (non-blocking): reword claim_verification CI cell; assert CONTRACT http=0.

---

## Execute readiness

- Branch: **main** (required)
- Tasks: 3 (tracer overlap+wire then CONTRACT whitelist then FUT-05 residual + SUMMARY)
- Expected commits (explicit pathspecs): check_overlap.py + check_release.py; CONTRACT (+ overlap.py if docstring changed); CONTRACT + 17-01-SUMMARY.md
- Live TOOL-20 boxes stay open until phase.complete / verify
- Version trio and map_version stay 1.19.0
- OneDrive: git commit --no-verify may timeout; check `git log --oneline -1` before retry

---

## Counts

| Severity | Count |
|----------|------:|
| BLOCKER | 0 |
| MAJOR | 1 |
| MINOR | 5 |
| **Total** | **6** |

---

**Verdict:** APPROVE_WITH_NOTES

_Reviewed: 2026-08-20_
_Reviewer: gsd-code-reviewer (plan review mode)_
_Blockers: 0 · Majors: 1_
