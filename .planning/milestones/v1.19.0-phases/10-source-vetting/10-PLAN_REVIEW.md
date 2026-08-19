# Phase 10 Plan Review — 10-01-PLAN.md + 10-02-PLAN.md

**Reviewed:** 2026-08-17
**Depth:** deep (plan vs live tree: ROADMAP, REQUIREMENTS, STATE, SOURCE-VETTING, 10-RESEARCH decision table + recommended plan shape, 10-PLAN_CHECK, 10-VALIDATION, MILESTONES; live re-run of every claim_verification row and every `<automated>` verify)
**Plans:** `.planning/phases/10-source-vetting/10-01-PLAN.md`, `10-02-PLAN.md`
**Plan check:** 10-PLAN_CHECK.md — PASS_WITH_FIXES (0 blockers, 5 warnings)
**Files reviewed:** both plans against 8 live surfaces

**Verdict:** PASS_WITH_FIXES

The two waves will record a dated tier / deferral for every v1.19 candidate and leave AAF unused if the executor follows the actions. 10-01 owns `docs/SOURCE-VETTING.md`; 10-02 annotates planning surfaces so Phase 11 does not re-guess. Honest deferral is the ROADMAP-legal outcome, not a silent v1 cut. Unlike Phase 6, no automated gate is invalid bash, no success criterion is missing, and no plan writes URLs, treats unreachable as Tier 1, uses AAF, creates `packs/`, or checks VET-19 boxes. What keeps this off APPROVE is the same class as Phase 6 MJ-03: three automated blocks can green-light incomplete work that the acceptance lines already require. Fixes are one-line verify rewrites — no redesign, no split, no verdict changes.

---

## Findings

### MJ-01 [MAJOR] 10-01 Task 1 verify misses insert-point and the v1.18 SP-7084 reconfirm suffix

**File:** 10-01-PLAN.md, Task 1 `<verify><automated>`
**Issue:** must_haves truth 1 and Task 1 acceptance require `### Vetted candidates (v1.19.0)` immediately after the v1.18 section / before `### Def Stan 00-051`, plus `Reconfirmed 2026-08-17` on the existing v1.18 SP-7084 cell. The automated block greps the new heading, 8719.14C, IS-GPS-200N, `Tier 1 RECONFIRMED`, the 10-RESEARCH pointer, IS-300 / IS-GPS-300 tokens, `! grep http`, and heading uniqueness — it never compares heading line order and never greps the v1.18 suffix. A faithful executor is fine; a sloppy one can drop the section at EOF (or skip the v1.18 suffix) and still go green. Live pre-phase: no v1.19 heading, SP-7084 line 129 ends `(Verified 2026-08-14.)` only.
**Fix:** add a line-order check (`v1.18` line < `v1.19` line < Def Stan) and `grep -n "Reconfirmed 2026-08-17" docs/SOURCE-VETTING.md`. Same as 10-PLAN_CHECK W1.

### MJ-02 [MAJOR] 10-01 Task 2 verify never asserts the six GO / NO-GO cells

**File:** 10-01-PLAN.md, Task 2 `<verify><automated>`
**Issue:** Acceptance and must_haves require a Phase 11 handoff table with greppable `GO —` / `NO-GO —` for all six candidates. The automated block greps the three new headings, `FUT-04`, `NOT yet vetted — do not use`, `Product Support Manager Guidebook`, `shipped A-94-only`, `http=0`, `Verified 2026-08-17 >= 5`, and empty `packs/` diff — it never greps `GO —` or `NO-GO —`. A heading-only stub (or a table missing cells) passes. Live file has none of those headings; the `>= 5` floor is grounded (prescribed T1+T2 text yields six `Verified 2026-08-17` hits: 8719, 200N, FUT-04, AAF unused bullet, GP-06 rewrite, AAF Excluded-pending; SP-7084 uses Reconfirmed and DoDM uses Recorded).
**Fix:** conjunct `test "$(grep -c 'GO —' docs/SOURCE-VETTING.md)" -eq 3` and `test "$(grep -c 'NO-GO —' docs/SOURCE-VETTING.md)" -eq 3` plus the six candidate names. Same as 10-PLAN_CHECK W2.

### MJ-03 [MAJOR] 10-02 Task 1 `Phase 10 handoff` grep is a single-hit gate

**File:** 10-02-PLAN.md, Task 1 `<verify><automated>`
**Issue:** Acceptance requires IO-01..06 each carry `Phase 10 handoff`. `grep -n "Phase 10 handoff"` exits 0 on one match. Distinctive VET-19 strings are conjunct and do distinguish the pre-phase tree (live `Phase 10 handoff` count = 0; `Excluded-pending` already appears in the VET-19-03 stem — weak conjunct only). Checkbox tests (`grep -c '^- \[x\] **VET-19' = 0` and open-box = 4) work as written on this tree (live GNU grep 3.0 and the ugrep wrapper both count 4 open / 0 checked). The gap is IO coverage, not the checkbox regex.
**Fix:** `test "$(grep -c 'Phase 10 handoff' .planning/REQUIREMENTS.md)" = "6"` (IO-07 uses `Phase 10:` and must stay out of that count). Same as 10-PLAN_CHECK W3.

### MN-01 [MINOR] 10-VALIDATION.md Per-Task map still describes four 10-01-* tasks

**File:** 10-VALIDATION.md lines 43–47
**Issue:** Plans actually split 2+2 across 10-01 / 10-02. Row 10-01-01 claims REQUIREMENTS/STATE contain the FUT-04 sentence; those files are 10-02. Nyquist 8a–8d still pass (every task has automated verify). Advisory only.
**Fix:** remap to 10-01-T1 / 10-01-T2 / 10-02-T1 / 10-02-T2. Same as 10-PLAN_CHECK W4.

### MN-02 [MINOR] 10-RESEARCH.md Open Questions not marked RESOLVED

**File:** 10-RESEARCH.md Open Questions
**Issue:** No `(RESOLVED)` suffix and no inline RESOLVED markers. All four items already have Recommendations the plans implemented (do not block on browser fetch; Excluded-pending for AAF; do not assume Tier 1 from the copyright footer; annotate VET-19-01 instead of ticking).
**Fix:** retitle Open Questions (RESOLVED) and prefix each item RESOLVED with the chosen path. Do not reopen the decisions. Same as 10-PLAN_CHECK W5.

### MN-03 [MINOR] Task 2 action numbers “insert two blocks” then lists Block 1 / 2 / 3

**File:** 10-01-PLAN.md, Task 2 action A
**Issue:** Prose says “insert two blocks if missing” then specifies Block 1 (Not cleared), Block 2 (DoDM UNVERIFIED), and Block 3 (Phase 11 handoff). Executable — all three blocks are fully specified — but a literal reader may stop after two.
**Fix:** “insert three blocks if missing”.

---

## Verify-command re-run (this session)

All four `<automated>` blocks extracted verbatim and run under Git Bash 5.3 / GNU grep 3.0:

| Task | `bash -n` | Pre-phase execute | Distinguishes live tree? |
|---|---|---|---|
| 10-01 T1 | SYNTAX_OK | rc=1 (no v1.19 heading) | Yes on heading / 8719 / 200N / RECONFIRMED / pointer / IS-300 tokens / heading count |
| 10-01 T2 | SYNTAX_OK | rc=1 (no Not-cleared heading) | Yes on all named headings / FUT-04 / do not use / PSM / A-94-only; `Verified 2026-08-17` live = 0 |
| 10-02 T1 | SYNTAX_OK | rc=1 (no “retry failed” string) | Yes on distinctive annotation strings; checkbox counts match live 0 checked / 4 open |
| 10-02 T2 | SYNTAX_OK | rc=1 (no Phase 10 dated STATE bullet) | Yes; live `**Plans**: TBD` = 4, gate = 3 after Phase 10 rewrite is correct |

No unquoted parenthetical (Phase 6 BL-01 class). No `2>/dev/null \|\| echo 0`. `! grep -n "http"` survives `set -e` on the current URL-free file. `test "$(git diff --name-only -- packs/ | wc -l)" = "0"` is `<0>` here (no wc padding). Em-dash in the DoDM UNVERIFIED heading is U+2014 in both the action and the verify string.

---

## Plan-check incorporation

All five 10-PLAN_CHECK warnings are in-scope as small edits (three verify lines + two advisory stamps). No check finding requires a scope change, a new file outside `files_modified`, or renegotiating any verdict.

| Check finding | In-scope? | Covered by |
|---|---|---|
| W1 T1 verify misses insert-point + Reconfirmed | Yes — rewrite one command | MJ-01 |
| W2 T2 verify misses GO/NO-GO | Yes — rewrite one command | MJ-02 |
| W3 T1 handoff single-hit | Yes — rewrite one command | MJ-03 |
| W4 VALIDATION.md task map stale | Yes — advisory remap | MN-01 |
| W5 Open Questions unmarked | Yes — stamp only | MN-02 |

---

## Confirmed correct (checked, not raised)

- Verdict fidelity: 10-RESEARCH decision table maps 1:1 onto the tasked rows (VET-19-01 DEFERRED 403/503; 02a UNVERIFIED; 02b 8719.14C Tier 1 leaning; 02c IS-GPS-200N Tier 1 leaning, no IS-300; 02d SP-7084 RECONFIRMED; 03 NOT yet vetted — do not use; 04 AAF Excluded-pending only).
- ROADMAP SC-1..SC-4 and REQUIREMENTS VET-19-01..04 are all tasked. DoDM as Def Stan-pattern UNVERIFIED / deferred-excluded is RESEARCH + Claude's Discretion, not a missing SC-2 verdict. VET-19-01 “build-or-exclude” is satisfied by ROADMAP SC-1’s deferral-with-fresh-evidence path; boxes stay open for verify.
- Link Policy: live `grep -c http docs/SOURCE-VETTING.md` = 0; both plans forbid `http`/`https` in the published register; pointer names `10-source-vetting/10-RESEARCH.md`; `17 U.S.C. § 105` and `Internet Public` are explicitly allowed.
- Insertion point matches the live file (after the GP-08 deferral paragraph that closes v1.18 / before Def Stan at line 141).
- GP-06 rewrite is required: live row 135 still claims dual-source + “build-time check outstanding”; shipped `packs/federal-bca/PACK.yaml` already dropped Army CBA (403/503). Plan forbids adding Army CBA / DoDM as hard-Excluded Source cells.
- AAF path is unused: DAG sentence kept and strengthened; new Excluded-pending row; IO-05/IO-06 NO-GO; no `packs/aaf-*`.
- No pack creep: `files_modified` excludes `packs/`; both plans assert `git diff --name-only -- packs/` empty; no extract.py / catalog / vet_source.py.
- VET-19 / IO / Phase 10 ROADMAP checkboxes left unchecked. STATE frontmatter (`current_phase`, `progress.*`, `completed_plans`) forbidden. 10-02 `depends_on: ["10-01"]` is acyclic; single writer on SOURCE-VETTING.
- claim_verification on both plans is present, non-empty, and live-accurate (v1.19 heading count 0; stamp baseline 17; AAF unused sentence at line 85 without “do not use” yet; no 8719 / IS-GPS / 5000.102 rows; branch `main`; no CLAUDE.md / AGENTS.md; ROADMAP Plans TBD count 4; STATE `current_phase: 10`, `status: planning`, `completed_plans: 14`).
- MILESTONES.md v1.19 blurb does not hard-code a pack count this phase would invalidate — no analog of Phase 6 MJ-02.
- Unclassified `.edge-coverage.json` probes left unresolved by explicit must_haves — no invented `check_kind` / `check_target`.
- Recommended-plan-shape split (register vs planning-surface) is a valid deviation from “one docs plan”; it avoids two writers on SOURCE-VETTING.

---

## Recommendation

Tighten the three automated verify blocks (MJ-01..03) before execute so a partial register or a single IO annotation cannot go green. Stamp Open Questions / VALIDATION.md if convenient (MN-01/02) — not execute-blocking. No verdict changes, no scope changes, no re-plan. A quick re-check of the edited verify lines is sufficient after revision; a full re-review is not.

---

**Verdict:** PASS_WITH_FIXES

Two-wave docs-only plan covers every Phase 10 success criterion and every VET-19 ID. Actions are copy-exact and match 10-RESEARCH. All four verify scripts are valid bash and fail closed on the current tree. Advance after rewriting the three weak gates (insert-point + Reconfirmed; GO/NO-GO = 3/3; Phase 10 handoff count = 6).
