---
phase: 6-source-vetting-unverified-resolution
reviewed: 2026-08-14
depth: deep
scope_commits: c1dfcf0..6a503ae (Task-1 base commit content reviewed via working tree at HEAD)
files_reviewed:
  - docs/SOURCE-VETTING.md
  - .planning/REQUIREMENTS.md
  - .planning/ROADMAP.md
  - .planning/MILESTONES.md
  - .planning/STATE.md
  - .planning/phases/6-source-vetting-unverified-resolution/6-01-SUMMARY.md
  - .planning/phases/6-source-vetting-unverified-resolution/6-01-PLAN.md
  - .planning/phases/6-source-vetting-unverified-resolution/6-RESEARCH.md
  - .planning/research/capability-gap-report.md (evidence cross-reference)
findings:
  blocker: 0
  major: 2
  minor: 2
  info: 2
  total: 6
status: issues_found
---

# Phase 6: Code Review Report — Source Vetting + UNVERIFIED Resolution

**Verdict:** NEEDS_WORK

**Reviewed:** 2026-08-14
**Depth:** deep (cross-file evidence trace: SOURCE-VETTING ↔ 6-RESEARCH ↔ capability-gap-report ↔ REQUIREMENTS/ROADMAP/MILESTONES/STATE)
**Scope:** commits c1dfcf0..6a503ae (5 commits; the Task-1 base commit c1dfcf0 — the "Vetted candidates (v1.18.0)" section — reviewed in the working tree at HEAD)

## Summary

Mechanically, this phase is in excellent shape: `python tooling/check_release.py` **PASS** (exit 0), the Link Policy holds (`grep -c 'http' docs/SOURCE-VETTING.md` = **0**), all 18 date stamps present, GP-01..GP-07 tokens greppable, GP-08 struck with a mirrored Out-of-Scope row, and the 7-pack / 63-total arithmetic (56 dirs + 7 GP; catalog basis 54) is consistent across ROADMAP / MILESTONES / STATE / REQUIREMENTS with no `63-64`, `7-8`, `7–8`, or `GP-01..GP-08` leftovers. Row-by-row verdict fidelity vs 6-RESEARCH.md is faithful for 7 of 8 vetted rows and 2 of 3 excluded rows.

However, two evidence-integrity defects sit in the phase's core deliverable — the vetting register — and both will mislead Phase 7 if not corrected: (1) one of the gap report's five UNVERIFIED items (DAU AAF guidebooks licence spot-check) was silently substituted with AFOTEC and left unresolved, while the new DAG exclusion row recommends the unvetted AAF guidebooks as "the Tier 1 substitute"; (2) the GP-06 federal-bca row carries a "(Verified 2026-08-14.)" stamp for a verification that 6-RESEARCH never performed. Because this register is the repo's declared integrity document and Phase 7 build trust rests on it, these must be fixed before the phase is verified closed.

## Gates Run (all PASS)

| Gate | Result |
|---|---|
| `python tooling/check_release.py` | **PASS** — "repo is release-ready against the mechanical gate" (exit 0) |
| Link Policy: `grep -c 'http' docs/SOURCE-VETTING.md` | **0** (clean) |
| Date stamps: `grep -c 'Verified 2026-08-14' docs/SOURCE-VETTING.md` | **18** (7 pre-phase + 11 new; matches plan arithmetic) |
| GP tokens GP-01..GP-07 greppable in SOURCE-VETTING | PASS |
| Pack counts: `packs/` = 56 dirs; catalog = 54; 56 + 7 = 63 | PASS, consistent on all four surfaces |
| Leftover `63-64` / `7-8` / `7–8` / `GP-01..GP-08` in planning docs | none found (grep exit 1) |
| No `packs/` or `sources/` changes in range (no premature builds) | PASS |
| VET-01/VET-02 checkboxes left open for phase verification | PASS (per plan Deviation 3) |

## Major Findings

### MA-01: SC-1 coverage gap — gap-report UNVERIFIED item #5 (DAU AAF guidebooks) never resolved; silently substituted with AFOTEC

**File:** `docs/SOURCE-VETTING.md:84-86`; `.planning/REQUIREMENTS.md:75` (VET-01); `.planning/STATE.md:55`; `.planning/phases/6-source-vetting-unverified-resolution/6-RESEARCH.md:4-6`
**Issue:** The capability-gap-report §4 "UNVERIFIED items (needs resolution during v1.18 vetting)" list is: (1) MIL-STD-40051, (2) NASA SP-7084, (3) VV&A RPG PDF build, (4) MIL-STD-881F canonical PDF, (5) **DAU AAF guidebooks pagination/licence page** ("per-guidebook copyright notices (third-party embedded content) should be spot-checked during vetting"). Phase 6 resolved 40051, SP-7084, VV&A, 881F — and **AFOTEC**, which is a §4 *excluded-table* row marked UNVERIFIED inline, not the fifth list item. The DAU AAF guidebooks spot-check was never performed and no tier decision (vetted, excluded, or deferred) exists for it anywhere in SOURCE-VETTING or 6-RESEARCH. This is compounded by the new DAG exclusion row (`docs/SOURCE-VETTING.md:85`) actively recommending the unvetted AAF guidebooks as "the Tier 1 substitute" — pointing builders at the one source whose licence caveat was the dropped obligation. ROADMAP Phase 6 SC-1 ("All 5 UNVERIFIED items resolved to Tier 1/2/Excluded with evidence") is therefore not literally satisfied, yet STATE.md:55, the Decisions block, and 6-01-SUMMARY all assert "5 UNVERIFIED items resolved". Lineage: the substitution originates in VET-01's wording (scoping commit 6a54366, pre-phase) and was inherited by 6-RESEARCH without re-checking the gap report — the plan/execute/review gates did not catch it.
**Fix:** Two small, either-or edits. (a) Add an AAF-guidebooks row to SOURCE-VETTING (Tier 1 statute-basis with the per-guidebook third-party-notice build caveat the gap report asked to spot-check), or record an explicit deferral note; **and** correct the "5 UNVERIFIED items resolved" claims in STATE.md:55 and 6-01-SUMMARY to name the substitution (4 of the gap report's 5 + AFOTEC from the excluded table). (b) If AAF is deliberately out of v1.18 candidate scope, amend VET-01 and the STATE/summary wording to state that explicitly with rationale, and soften the DAG row's "AAF guidebooks remain the Tier 1 substitute" to note their licence spot-check is still pending.

### MA-02: GP-06 federal-bca row stamped "(Verified 2026-08-14.)" for a verification that was never performed

**File:** `docs/SOURCE-VETTING.md:135`
**Issue:** The GP-06 / federal-bca row's licence evidence reads "(licence basis per 6-RESEARCH.md §2 spot-check scope and capability-gap-report shortlist item 5) … (Verified 2026-08-14.)". 6-RESEARCH §2 contains exactly three spot-checks — §2a FAA-STD-025, §2b DOT&E, §2c DAFMAN 63-119 (header: "spot-check 3 ranked candidates"). OMB Circular A-94 and the Army CBA Guide were never fetched, inspected, or licence-checked in Phase 6; "§2 spot-check scope" is a non-citation (at best an oblique admission that federal-bca fell outside the spot-check scope). The "(Verified 2026-08-14.)" stamp therefore overstates the evidence in the repo's integrity register, and the row is the **only** v1.18 Vetted row lacking a build-time in-source confirmation caveat — despite being the only candidate with zero in-source inspection (every sibling row says "confirm DIST-A / in-PDF statement at build", as do all v1.17 statute-basis rows). The plan (Task 1, item 8) specified this wording, so the executor followed the plan — the defect is in the plan's wording, now propagated to the published doc.
**Fix:** Restamp the row to match the v1.17 convention: "Both are U.S. Government works, public domain per 17 U.S.C. § 105 (statute basis per capability-gap-report shortlist item 5; not re-checked in 6-RESEARCH §2). Confirm in-PDF statements/copyright notices for **both** sources at build; record per-source provenance in PACK.yaml." Drop the "(Verified 2026-08-14.)" stamp or replace with "(Tier recorded 2026-08-14; in-source check at build.)".

## Minor Findings

### MI-01: AFOTEC Excluded row hardens an inference into dated fact ("the 1989 edition")

**File:** `docs/SOURCE-VETTING.md:84`
**Issue:** The row states "only DTIC hit is the 1989 edition (AD-A205 489)" as fact. 6-RESEARCH §1e could not load the DTIC citation — both endpoints served "Under Maintenance" HTML shells — and inferred the date: "AD-A numbers of that range are late-1980s" and "the **1989** AFOTEC Test Design Guide era". The published register converts an accession-number-range inference into a verified edition date. The exclusion outcome is unaffected (unverifiable + stale either way), so Minor.
**Fix:** Reword to "only DTIC hit is the 1989-era edition (AD-A205 489; date inferred from the accession-number range — the citation page was unfetchable, DTIC under maintenance)".

### MI-02: "Vetted candidates (v1.18.0)" table lists 8 candidates under the v1.18.0 heading while v1.18 scope is 7 packs

**File:** `docs/SOURCE-VETTING.md:115-137` (SP-7084 row at :129)
**Issue:** The section heading scopes the table to v1.18.0, but only GP-01..GP-07 are v1.18 builds; NASA SP-7084 is a VET-01 resolution item with no GP slot and no Phase 7 build plan. The plan carried the disambiguation ("VET-01 item, not a GP pack") but it was dropped from the published row, so a reader of the integrity doc can reasonably expect 8 v1.18 packs / 64 total against the recorded 63-pack target (56 + 7).
**Fix:** Append to the SP-7084 row: "(VET-01 resolution only — not a v1.18 pack build; cluster-25 candidate bench)".

## Info

### IN-01: MILESTONES header stale relative to phase state
**File:** `.planning/MILESTONES.md:16` — header still reads "v1.18.0 (in planning — scoped 2026-08-16)" on a file edited this phase while STATE reports Phase 6 executed/awaiting verification. Suggest "(in progress)".

### IN-02: AE-03 references an untracked file
**File:** `.planning/REQUIREMENTS.md:93` — references `docs/ROLE-AGENTS-REQUIREMENTS-V2.md`, which is untracked in the working tree (outside this diff; a milestone requirement pointing at an uncommitted file). Commit or mark it as planned-artifact.

## Verified Faithful (spot-check detail)

- GP-07/40051-2C, SP-7084, GP-01/VV&A, GP-05/881F, GP-02/FAA, GP-03/DOT&E, GP-04/DAFMAN rows each trace faithfully to 6-RESEARCH §1a-1d, §2a-2c (build caveats, editions, title correction, URL-encoding fix all preserved).
- DAG and CMU SEI Excluded rows faithful to §3a/§3b (retirement quote, AFCAPO 2022-08-15 date, permission@sei.cmu.edu routing, DIST-A-vs-copyright distinction).
- GP-08 descope mirrored correctly across REQUIREMENTS strike-through + Out-of-Scope table (NPR 7150.2 / NASA-STD-8739.8 alternative), ROADMAP Phase 7 goal/requirements/overview bullet, MILESTONES, and STATE.
- 6-01-SUMMARY's "http" count of 8 is the grep-command quotations, not URLs — Link Policy intact in the summary artifact as well.

---

**Required before phase close-out:** MA-01 and MA-02 (both are scoped edits to SOURCE-VETTING + STATE wording; no pack or tooling changes).

_Reviewer: code-review subagent (adversarial pass)_
_Depth: deep_
