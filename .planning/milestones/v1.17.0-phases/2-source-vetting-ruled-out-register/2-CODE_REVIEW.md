---
phase: 2-source-vetting-ruled-out-register
reviewed: 2026-08-14T23:30:00Z
depth: deep
files_reviewed: 11
files_reviewed_list:
  - docs/SOURCE-VETTING.md
  - .planning/REQUIREMENTS.md
  - .planning/ROADMAP.md
  - .planning/STATE.md
  - .planning/PROJECT.md
  - .planning/MILESTONES.md
  - .planning/phases/2-source-vetting-ruled-out-register/2-RESEARCH.md
  - .planning/phases/2-source-vetting-ruled-out-register/2-01-PLAN.md
  - .planning/phases/2-source-vetting-ruled-out-register/2-01-SUMMARY.md
  - .planning/phases/2-source-vetting-ruled-out-register/2-PLAN_CHECK.md
  - .planning/phases/2-source-vetting-ruled-out-register/2-PLAN_REVIEW.md
findings:
  critical: 0
  blocker: 0
  warning: 1
  major: 1
  info: 6
  minor: 6
  total: 7
status: issues_found
verdict: PASS_WITH_NOTES
---

# Phase 2: Code Review Report

**Reviewed:** 2026-08-14 (commits 1699507..311621c, with full-phase context b1c7c8f..311621c)
**Depth:** deep (cross-artifact: SOURCE-VETTING ↔ REQUIREMENTS ↔ ROADMAP ↔ STATE ↔ PROJECT ↔ MILESTONES ↔ 2-RESEARCH ↔ 2-01-PLAN/SUMMARY ↔ PACK-SPEC ↔ LICENSING Link Policy ↔ tooling/check_release.py)
**Files Reviewed:** 11
**Status:** issues_found

**Verdict:** PASS_WITH_NOTES

## Summary

Phase 2 is substantively correct. Every independently re-executed check passes:

- **Link Policy (zero source URLs):** `grep -c "http" docs/SOURCE-VETTING.md` = **0**. The Vetted table is `Source | Tier | Licence evidence` (no URL column); the 2-RESEARCH.md pointer line (SOURCE-VETTING.md:92-94) satisfies SC2's URL half by reference, exactly per BL-01 option (b).
- **Folded MAJORs N1–N4 all confirmed resolved in the tree, not just claimed:**
  - N1: `grep -c "Verified 2026-08-14" docs/SOURCE-VETTING.md` = **7** (gate honestly lowered from the plan's false `-ge 8`; no dummy stamps minted).
  - N2: each of the 8 Tier-1 short names (`800-171`, `800-61`, `338B`, `516C`, `7009`, `413.3B`, `CPG 2.0`, `SEM3`) appears exactly **once** — verified individually, not via one OR-grep.
  - N3: ECSS is mirrored under a dedicated Out-of-Scope umbrella "Free-download, no-redistribution-grant standards (ECSS/ESA)" (REQUIREMENTS.md:65), not under "Paywalled"; SOURCE-VETTING.md:81 correctly says "Free download … but © ESA".
  - N4: REQUIREMENTS.md:41 T2-03 is `- [ ]` with "deferred-excluded pending registered DSTAN in-document licence check"; **zero** occurrences of "resolved" in REQUIREMENTS/ROADMAP/STATE; FUT-03 preserves the revival path. The `requirements.mark-complete` regression was reverted in 311621c.
- **ROADMAP Phase 2 SC1–SC3:** SC1's four named sources all present, dated, with rationale (ISO row extended to 29148/21839); SC2's 11 candidates all have recorded outcomes (8 Vetted + IEEE/ECSS Excluded + Def Stan 00-051 UNVERIFIED subsection); SC3 records deferred-excluded without claiming an unblock. RO-01 is `[x]` and earned.
- **56-pack consistency:** no `59+` survives anywhere; "56 (48 baseline + 8 Tier-1)" / "target after v1.17.0: 56" / "56 packs" agree across REQUIREMENTS.md:49-50, ROADMAP.md:59, STATE.md:41, PROJECT.md:44, MILESTONES.md:9. Phase 4 is closed by vetting in both ROADMAP surfaces (bullet + Details block); no live Tier-2 build instruction survives.
- **PACK-SPEC conformance:** Phase 2 builds no packs; the vetting outcomes impose no Excluded-tier source on any future `PACK.yaml`, and the statute-basis/confirm-in-source-at-build framing of the Vetted section does not overclaim the checklist's in-source licence read (MI-05 resolved via the qualified heading).

One traceability defect survives the remediation pass (MA-01 below), plus documentation-hygiene minors. No blocker: the governing artifacts (SOURCE-VETTING, REQUIREMENTS, ROADMAP) are mutually consistent and licence-conservative.

## Structural Findings (fallow)

None provided by the workflow for this phase.

## Narrative Findings (AI reviewer)

### MAJOR

#### MA-01: 2-01-SUMMARY.md frontmatter still records T2-03 as a completed requirement

**File:** `.planning/phases/2-source-vetting-ruled-out-register/2-01-SUMMARY.md:52`
**Issue:** `requirements-completed: [RO-01, T2-03]` claims T2-03 is complete. This directly contradicts (a) REQUIREMENTS.md:41, where T2-03 is deliberately `- [ ]` per N4 ("deferred-excluded, never resolved"), (b) the SUMMARY's own N4 resolution row (line 144) and Auto-fixed Issue #1 (lines 204-209), and (c) commit 311621c's stated purpose ("keep T2-03 unchecked"). The related coverage entry D2 (`requirement: T2-03`, `status: pass`, line 63-70) is defensible — it verifies the *recording* of the deferral — but the frontmatter's "completed" claim is the exact drift class N4 was written to prevent: a future phase-verify or milestone audit reading SUMMARY frontmatter will mark T2-03 satisfied and skip the registered-DSTAN licence read that gates any 00-051 revival. The fix commit updated the N4 narrative rows but missed the frontmatter line three lines above them.
**Fix:** In 2-01-SUMMARY.md frontmatter, change to `requirements-completed: [RO-01]` and add `requirements-deferred: [T2-03]` (or annotate `"T2-03 (vetting half only; build half deferred-excluded)"`). One-line edit; can ride the next docs commit.

### MINOR

#### MI-01: STATE.md `milestone_name` contains Phase 5's goal text, not the milestone name

**File:** `.planning/STATE.md:4`
**Issue:** `milestone_name: "**Goal**: Catalog, docs, installers, and release artifacts include the new packs"` is ROADMAP Phase 5's goal (ROADMAP.md:55), not the v1.17.0 milestone name ("Source Expansion" per MILESTONES.md:9). SDK copy-from-wrong-slot error propagated by the 07ef874 sync.
**Fix:** `milestone_name: Source Expansion (v1.17.0)`.

#### MI-02: STATE.md Decisions section has three unfilled `[Phase ?]` placeholders

**File:** `.planning/STATE.md:56-58`
**Issue:** All three decision log entries are tagged `[Phase ?]` — the phase number was never substituted, so the decision log is not filterable by phase and reads as template residue.
**Fix:** Replace `[Phase ?]` with `[Phase 2]` on all three lines.

#### MI-03: STATE.md is internally contradictory about plan/phase status and drifted a frontmatter type

**File:** `.planning/STATE.md:2,7,32`
**Issue:** (a) Frontmatter says `status: planning` and the body says "Plan: 01 executing / completing" (line 32) while the same frontmatter records `completed_plans: 1` of `total_plans: 1` and the body says "Status: Phase 2 outcome recorded; next: Phase 3" (line 33) — three different tenses for the same fact. (b) `gsd_state_version: 1.0` was changed from the quoted string `'1.0'` to an unquoted float (diff 1699507..311621c), a silent YAML schema-type change for any consumer doing strict string comparison.
**Fix:** Set `status: executing` (or the SDK's terminal value) consistently, change line 32 to "Plan: 01 of 01 complete", and restore `gsd_state_version: '1.0'`.

#### MI-04: ROADMAP Phase 2 "Plans: TBD" is stale now that 2-01 exists and is complete

**File:** `.planning/ROADMAP.md:34`
**Issue:** Phase 1 sets the convention ("Plans: 0 (retroactive; no execution required)") and Phase 4 records "Plans: none", but Phase 2 still says `**Plans**: TBD` even though 2-01-PLAN.md was created, executed, and summarized. A planner scoping Phase 3 against "TBD" gets an inaccurate picture of what Phase 2 consumed.
**Fix:** `**Plans**: 1 (2-01 — executed 2026-08-14; see 2-01-SUMMARY.md)`. (If the convention is to fill this at phase close, apply it at the verify gate — but then Phase 4's "none" was premature by the same rule.)

#### MI-05: The 56-pack Phase 5 gate count is defined on a different basis than the release gate counts

**File:** `.planning/ROADMAP.md:59` (authored in 29c8ba0); cross-ref `tooling/check_release.py:86-92,118-161`, `catalog.json`
**Issue:** "48 baseline" counts pack **directories** (48, including the two `kind: signpost` packs `omg-signpost` and `se-standards-signpost`). `check_release.py` explicitly *excludes* signpost packs from its shipped-pack checks, and catalog.json lists **46** entries today. After Phase 3 adds 8 Tier-1 packs: 56 directories, but **54** catalog-listed / gate-counted packs. ROADMAP Phase 5 SC1 ("check_release / CI content-integrity gate passes with 56 packs") never states which basis — a Phase 5 verifier counting catalog or SKILLS.md entries will see 54 and either false-fail the gate or assume drift. This is a pre-existing vocabulary ambiguity (48 vs 46) that Phase 2's new numeric criterion inherited and made load-bearing.
**Fix:** Amend SC1 to "56 pack directories (54 catalog-listed + 2 signposts)" or "54 catalog-listed packs (56 incl. signposts)" — pick one basis and use it in REL-01/REL-02 too. Zero code impact today; prevents a Phase 5 verify dispute.

#### MI-06: Workflow state file lags the phase's actual progress and records a stale plan_review verdict

**File:** `.planning/phases/2-source-vetting-ruled-out-register/master_flow_state.json` (working tree, uncommitted)
**Issue:** The phase state records `current_gate: plan_check`, `blocked_by: plan_review`, `verdicts.plan_review: "needs_work:bl_01_link_policy_breach;_5_major"`, and `execute: {plans_total: 0, plans_complete: 0}` — but plan_review was re-checked PASS_WITH_FIXES at aaaba0b (2-PLAN_CHECK.md "Re-check" section) and 2-01 was subsequently executed and summarized (c98a9d2, 311621c). If the session resumes from this file, the flow would re-run plan gates and has no record that execution happened. Caveat: this file is orchestrator-owned and currently modified mid-gate, so it may be advanced when the code_review gate closes — flagged so it is not forgotten.
**Fix:** After this gate, ensure the state file advances through `plan_review → execute → code_review` with `plans_total: 1, plans_complete: 1` and the re-check verdict (or a `regate` note superseding `needs_work`), then commit it with the next docs commit.

## Info

#### IN-01: Bare domain "ecss.nl" in the SOURCE-VETTING Excluded row brushes the Link Policy's intent

**File:** `docs/SOURCE-VETTING.md:81`
**Issue:** "Free download from ecss.nl but © ESA" names the download host. It is not a URL (the http-count verify correctly stays 0) and the wording was prescribed by the remediated plan (2-01-PLAN.md Task 1.2), so this is compliant as verified — but it is source-location information in prose form, one edit away from a policy breach by a future row-copy. Worth a parenthetical in the Link Policy note if it recurs.
**Fix (optional):** Replace with "free download from the ECSS portal" and keep only the 2-RESEARCH.md pointer as the location record.

## Contract compliance matrix

| Contract / criterion | Result |
|---|---|
| docs/PACK-SPEC.md (no source_url, tier ∈ {1,2,3}, licence provenance) | N/A this phase (no packs built); vetting outcomes impose no Excluded-tier source on Phase 3 |
| docs/SOURCE-VETTING.md Link Policy (zero source URLs in docs) | PASS — http count = 0; URL evidence correctly centralized in 2-RESEARCH.md with pointer line |
| ROADMAP Phase 2 SC1 (4 named sources, rationale + date) | PASS — all four dated "(Verified 2026-08-14.)", ISO row names 29148/21839 |
| ROADMAP Phase 2 SC2 (11 candidates, tier decision + URL + licence evidence) | PASS — 8 Vetted + 2 Excluded + 1 UNVERIFIED; URL half by reference to 2-RESEARCH.md (agreed BL-01(b) reading) |
| ROADMAP Phase 2 SC3 (00-051 build-or-exclude decision recorded) | PASS — deferred-excluded, explicitly not worded as "resolved" |
| REQUIREMENTS.md T2-03 unchecked; 56-pack count | PASS — `- [ ]` retained; "56 (48 baseline + 8 Tier-1)" in REL-01/REL-02; excluded-by-vetting ×5 |
| Folded MAJORs N1–N4 (per 2-01-SUMMARY.md) | PASS — all four independently re-verified in the tree (see Summary) |
| Cross-file: PROJECT / MILESTONES / STATE / ROADMAP / REQUIREMENTS agree | PASS on substance (56, 0 Tier-2, 3 vetted-out) — PASS_WITH_NOTES for the STATE.md metadata defects MI-01..MI-03 |

---

_Reviewed: 2026-08-14T23:30:00Z_
_Reviewer: ZCode (gsd code reviewer)_
_Depth: deep_
_Verdict: PASS_WITH_NOTES (0 BLOCKER, 1 MAJOR, 6 MINOR, 1 INFO)_
