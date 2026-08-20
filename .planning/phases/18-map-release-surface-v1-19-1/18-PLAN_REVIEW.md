# Phase 18 Plan Review -- 18-01-PLAN.md + 18-02-PLAN.md

**Reviewed:** 2026-08-20
**Depth:** deep (plan vs live tree: ROADMAP Phase 18 SC-1..SC-3, REQUIREMENTS MAP-20-01 / REL-20-01 / REL-20-02, 18-RESEARCH user_constraints + Patterns 1-5, 18-PLAN_CHECK, analog 13-01/13-02 / 13-PLAN_REVIEW; live re-run of claim_verification rows; CPython compile() on every automated python -c payload)
**Plans:** .planning/phases/18-map-release-surface-v1-19-1/18-01-PLAN.md, 18-02-PLAN.md
**Plan check:** 18-PLAN_CHECK.md -- PASS_WITH_FIXES (blockers: 0, 3 warnings)
**Files reviewed:** both plans against locked RESEARCH constraints + live version/catalog/map/release surfaces

**Verdict:** APPROVE_WITH_NOTES

The two waves will bump the 11 analog surfaces plus map_version / CONTRACT example, land an honest [1.19.1] (hygiene + overlap tooling + FUT-05 residual + still-deferred FUT-04/AAF/PACK/IO-05/06; IO-07 accept), dual-gate at frozen 63/65, then publish an annotated tag + GitHub Release and record shipped state -- if the executor follows the actions. No success criterion is missing. No plan would git add -A, create a lightweight tag, unwire the overlap/map gate, rebuild packs, tick MAP/REL boxes, paper over deferrals, or continue after a rejected push.

What keeps this off APPROVE is environment + research-stamp notes, not missing REL/MAP work: active gh identity cannot push (MN-01 / PLAN_CHECK W3); Open Questions unmarked (MN-02 / W2); VALIDATION.md absent under N/A architecture (MN-03 / W1). No redesign, no split, no verdict changes.


---

## Findings

### MN-01 [MINOR] Active gh identity cannot publish (PLAN_CHECK W3)

**File:** 18-02-PLAN.md claim_verification row gh authenticated as publisher; Task 1 precondition gh auth status succeeds
**Issue:** Live 2026-08-20: systems-researcher is the active gh account; jgsystemsconsulting is logged in but inactive. gh api repos/jgsystemsconsulting/jgs-se-knowledge-packs as the active identity returns push: false. gh release view v1.19.0 still works (read). git push / gh release create as the default account will not satisfy REL-20-02.

This is environment drift, not a missing command. The plan analog (git push origin main --follow-tags + phase-dir notes + STOP on reject) is correct. Same class as Phase 13 IN-01.

**Fix:** executor gh auth switch --user jgsystemsconsulting (or equivalent) before 18-02 Task 1. Do not change branch protection.

### MN-02 [MINOR] 18-RESEARCH.md Open Questions unmarked (PLAN_CHECK W2)

**File:** 18-RESEARCH.md Open Questions
**Issue:** No (RESOLVED) suffix and no inline RESOLVED markers. Both items already have Recommendations the plans implemented (CHANGELOG one-liner; em dash in gh title only).

**Fix:** retitle Open Questions (RESOLVED) and prefix each item RESOLVED with the chosen path. Do not reopen.

### MN-03 [MINOR] 18-VALIDATION.md absent (PLAN_CHECK W1)

**File:** phase dir
**Issue:** No 18-VALIDATION.md. RESEARCH Validation Architecture is N/A (existing gates; no new tests). Nyquist 8a-8d still pass (every execute task has automated). 8e existence gate would block if architecture were present.

**Fix:** leave advisory, or add a five-row VALIDATION.md mapping T1-T3 / 18-02 T1-T2 onto check_release / check_capability_map / git cat-file / gh release view. Do not invent tests.

### IN-01 [INFO] PATTERNS.md Pattern 2 / Pattern 5 examples are stale vs locked plan must-NOTs

**File:** 18-PATTERNS.md Pattern 2 (CHANGELOG heading with em dash); Pattern 5 (commit REQUIREMENTS.md and tick REL-20)
**Issue:** Plans correctly refuse both: new CHANGELOG entry is em-dash-free; MAP/REL boxes stay unchecked for phase.complete. Pattern 3 analog still lists catalog.json on the release commit; 18-02 correctly omits it.

**Fix:** none for execute. Optional later PATTERNS tidy.

### IN-02 [INFO] 18-02 T1 notes-body token is overlap lowercase vs CHANGELOG Overlap heading

**File:** 18-02-PLAN.md Task 1 automated; 18-01 Task 2 draft
**Issue:** 18-02 greps token overlap (lowercase). 18-01 T2 draft heading is Overlap checker. Python in is case-sensitive. The draft also contains check_overlap.py so the substring overlap still matches. Not a false-fail on the planned draft. If an executor rewrites the Added bullet and drops the module path, 18-02 T1 could fail after a successful gh create.

**Fix:** none required if the draft lands as written. Executor: keep check_overlap.py or the word overlap in the new entry body.


---

## Verify-command re-run (this session)

All five automated blocks extracted verbatim. CPython compile() of each python -c payload:

| Task | compile() | Distinguishes live tree? |
|---|---|---|
| 18-01 T1 | COMPILE_OK | Yes. Live plugin/RELEASE-INFO/README still 1.19.0; ## [1.19.1] absent (T2 owns heading) |
| 18-01 T2 | COMPILE_OK | Yes. Fail-closed at missing ## [1.19.1]. http/em-dash bans apply to new-entry slice only |
| 18-01 T3 | COMPILE_OK | Yes. Live map_version still 1.19.0; live files still contain 1.19.0 (expected until T1) |
| 18-02 T1 | COMPILE_OK | Yes. No local v1.19.1 tag; git rev-parse would fail closed |
| 18-02 T2 | COMPILE_OK | Yes. MILESTONES heading still in execution; MAP/REL boxes unchecked; ROADMAP Phase 18 [ ] |

No 2>/dev/null || echo 0. No || true feeding a comparison. No caret-anchored package-manager grep. Loop-body assert indents are valid Python (for-loop suite), not the Phase 13 leftover-indent class.

---

## claim_verification live re-run (cwd repo root, 2026-08-20)

No missing/empty claim_verification. No invented replacements. Current-state rows match except the publisher-account active flag (MN-01):

| Plan | Claim | Live | Status |
|---|---|---|---|
| 18-01 / 18-02 | Branch is main; v1.19.0 exists; v1.19.1 does not | main; git tag -l v1.19* = v1.19.0 | Accurate |
| 18-01 | Both gates PASS at 1.19.0 basis | map PASS TOTAL 644 exit 0; RELEASE CHECK: PASS exit 0 (overlap then map) | Accurate |
| 18-01 | Version trio still 1.19.0; no [1.19.1] | plugin 1.19.0; cursor 1.19.0; ## [1.19.0]: 2026-08-17; Version 1.19.0 Tag v1.19.0 Staged 2026-08-17T22:56:12Z | Accurate |
| 18-01 | map envelope 1.19.0 / 644 | schema 2, map_version 1.19.0, generated_on 2026-08-17, 32 clusters, 644 | Accurate |
| 18-01 | CONTRACT example envelope 1.19.0 | L15 map_version 1.19.0; L35 e.g. 1.19.0; L54 historical 1.17.0; section 8 FUT-05 residual present | Accurate |
| 18-01 | catalog / dirs frozen | n_catalog 63; dirs 65 | Accurate |
| 18-01 | No leftover registration | RPG already 13; nasa-std-8719-14 / is-gps-200n already live | Accurate (do not re-edit catalog.json) |
| 18-01 | CI never execs repo Python | validate.yml header never executes checked-out repository code | Accurate |
| 18-01 | Link policy SOURCE-VETTING | http count 0 | Accurate |
| 18-01 / 18-02 | gh authenticated as publisher | systems-researcher active (repo); jgsystemsconsulting inactive; gh api push:false as active | Publisher exists; active identity is systems-researcher (MN-01) |
| 18-02 | Live tag style | v1.18.0 / v1.19.0 colon; cat-file -t v1.19.0 == tag | Accurate |
| 18-02 | Live GitHub Release title style | v1.19.0 em dash Agent IO Depth ... | Accurate |
| 18-02 | Surprise untracked | ?? phase master_flow_state.json | Accurate |
| 18-02 | Admin-bypass; MILESTONES in-execution; REL/MAP boxes open | STATE Deviations; ## v1.19.1 (in execution); REQUIREMENTS unchecked | Accurate |

---

## Plan-check incorporation

All three 18-PLAN_CHECK warnings are in-scope as notes (gh switch at 18-02 T1; advisory VALIDATION/Open-Questions stamps). No blockers to re-open.

| Check finding | In-scope? | Covered by |
|---|---|---|
| W1 VALIDATION.md absent | Yes -- advisory | MN-03 |
| W2 Open Questions unmarked | Yes -- stamp only | MN-02 |
| W3 active gh cannot push | Yes -- executor switch | MN-01 |

---

## Confirmed correct (checked, not raised)

- ROADMAP SC-1 / SC-2 / SC-3 and REQUIREMENTS MAP-20-01 / REL-20-01 / REL-20-02 are all tasked. Frontmatter IDs: both plans list [MAP-20-01, REL-20-01, REL-20-02]. 18-01 owns map bump + honesty + both gates; 18-02 owns annotated tag + push + gh release create + records.
- Analog order locked: RELEASE-INFO first then gen_packs_page.py then remaining surfaces; CHANGELOG heading is Task 2 (trio intentionally split after T1).
- map_version bump is string-only. Membership asserted 644. No cluster rewrite. CONTRACT L54 historical 1.17.0 left alone. generated_on stays 2026-08-17.
- Two-plan split is Claude's Discretion / Phase 13 analog. 18-02 soft-resets to PRE_RELEASE_HEAD and restages explicit paths into one release(v1.19.1) content commit. Not a locked-decision contradiction. Do not merge the plans.
- Must-NOT holds: no pack rebuild; no map reclassify; no unwire; no CI repo-Python; no git add -A / git add docs/ / git add .; no /tmp notes; no lightweight tag; no AAF/CBA/DoDM/stakeholder packs; no SKILLS/NOTICE/cursor skill-list rewrite; no MAP/REL box ticks; records commit is .planning-only after the tag; catalog.json not added.
- T2 http/em-dash bans apply to the new-entry slice, not the Keep-a-Changelog header.
- 18-02 T1 verify requires git cat-file -t == tag, origin ls-remote, and gh release view body tokens FUT-04/AAF/PACK-20/overlap/FUT-05/IO-05/06/07 + DEFERRED. Title em dash is public-only.
- 18-02 T2 ticks Phase 18 + both plan filenames; MAP/REL stay open; MILESTONES must leave in execution on the v1.19.1 heading; STATE carries se-agents / IO-07 / DoDM / FUT-04 / AAF.
- Push-reject STOP is explicit. No PR workaround.
- 18-01 40000 and 18-02 35000 are under the 100k smart-zone.
- Stay on main. No branches / worktrees.
- Untracked master_flow_state.json remains untracked by instruction.

---

## Recommendation

Switch gh to jgsystemsconsulting before 18-02 Task 1. Stamp Open Questions / VALIDATION.md if convenient -- not execute-blocking. No verdict changes, no scope changes, no re-plan, no phase split.

Execute may proceed.

---

**Verdict:** APPROVE_WITH_NOTES

blockers: 0
**majors:** 0
**minors:** 3

Path: .planning/phases/18-map-release-surface-v1-19-1/18-PLAN_REVIEW.md

Two-wave plan covers every Phase 18 success criterion and MAP-20 / REL-20 IDs. Actions match 18-RESEARCH and the Phase 13 analog (including push + STOP on reject). Advance after switching the gh publisher account at 18-02 T1.
