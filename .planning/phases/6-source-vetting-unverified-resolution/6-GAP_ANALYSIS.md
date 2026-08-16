# Phase 6: Gap Analysis — Source vetting + UNVERIFIED resolution

**Date:** 2026-08-16
**Inputs:** 6-IMPL_REVIEW, 6-CODE_REVIEW, 6-INTEGRATION_CHECK, 6-SECURITY_AUDIT (all four present, none skipped) + 6-RESEARCH / 6-01-PLAN / 6-01-SUMMARY (incl. deviation #4) / 6-PLAN_CHECK / 6-PLAN_REVIEW / 6-REVIEW-FIX / ROADMAP Phase 6 / REQUIREMENTS VET section / docs/SOURCE-VETTING.md current state
**Method:** Adjudication of all post-execute findings against ROADMAP Phase 6 success criteria, with independent live re-verification of the post-fix tree (fix commits `3381958` / `05eb9ad` read back directly: SOURCE-VETTING rows at :84-86/:129/:135/:137, STATE.md:55, REQUIREMENTS VET-01; gates re-run — `grep -c http docs/SOURCE-VETTING.md` = 0, dated verdict stamps = 18 (17 × `Verified 2026-08-14` + 1 × `Confirmed-by-statute 2026-08-16`), `python tooling/check_release.py` PASS exit 0).

**Verdict:** CLOSED

## Review Inventory

| Review | Verdict | Blocker | Major | Minor | Info/Warn | Post-review state |
|---|---|---|---|---|---|---|
| 6-IMPL_REVIEW | PASS_WITH_NOTES | 0 | 0 | 3 (MN-01/02/03) | — | No action required (reviewer's own fix guidance: none / process note / cosmetic) |
| 6-CODE_REVIEW | NEEDS_WORK | 0 | 2 (MA-01/02) | 2 (MI-01/02) | 2 (IN-01/02) | **6/6 fixed** at `3381958` + `05eb9ad` per 6-REVIEW-FIX; verified on current tree (see §Thread 1) |
| 6-INTEGRATION_CHECK | PASS_WITH_NOTES | 0 | 0 | — | 2 warnings | WARNING-2 (untracked AE-03 doc) closed by `05eb9ad`; WARNING-1 (external tool drift) adjudicated §Thread 3 |
| 6-SECURITY_AUDIT | SECURED_WITH_NOTES | 0 | 0 | 0 | 3 notes (N1-N3) | 3/3 declared threats CLOSED at declared boundaries; N3 is an explicit Phase 7 forward obligation (routed §Phase 7) |

The only NEEDS_WORK verdict was driven solely by MA-01/MA-02; both are evidence-integrity edits to SOURCE-VETTING/STATE/REQUIREMENTS/SUMMARY wording and are confirmed landed. No blocking defect remains open in any prior review.

## Success-Criteria Cross-Check (ROADMAP Phase 6)

| Criterion | Requirement | Status | Evidence (reproduced at gap-analysis time) |
|---|---|---|---|
| SC-1: All 5 UNVERIFIED items resolved to Tier 1/2/Excluded with evidence (URL + licence statement) | VET-01 | **VERIFIED under recorded re-scope** — see §Thread 1 | The 5 items VET-01 names are all resolved with evidence: 40051-2C → Tier 1 (§1a), SP-7084 → Tier 1 (§1b), VV&A RPG → Tier 1 chapter-wise (§1c), 881F → Tier 1 (§1d), AFOTEC → Excluded (§1e). Gap-report list item #5 (DAU AAF guidebooks licence spot-check) is explicitly deferred as not-a-v1.18-candidate — annotated in REQUIREMENTS VET-01, STATE.md:55, SOURCE-VETTING.md:85, SUMMARY deviation #4. |
| SC-2: DoD DAG, CMU SEI, and any failing candidates in the Excluded table with dated rationale | VET-02 | VERIFIED | SOURCE-VETTING.md:84-86 — AFOTEC, DoD DAG, CMU SEI rows all present, dated, rationale-faithful to 6-RESEARCH §1e/§3a/§3b (security audit §2b re-verified). Failing UNVERIFIED candidate = AFOTEC → excluded. |
| SC-3: Each GP pack candidate confirmed or dropped; stretch items (GP-08) decided | VET-01 (scope) | VERIFIED | GP-01..GP-07 all Tier 1-confirmed with build caveats; GP-08 decided (descoped 2026-08-14, mirrored in REQUIREMENTS Out of Scope + ROADMAP + MILESTONES + STATE); SP-7084 disambiguated as VET-01-evidence-only, not a pack (SOURCE-VETTING.md:129/:137). |
| Phase goal: "Every v1.18 candidate has a definitive tier decision" | VET-01/02 | VERIFIED | All 8 v1.18 Vetted-section rows carry a tier + dated evidence basis (7 × `Verified 2026-08-14`, 1 × `Confirmed-by-statute 2026-08-16` with build-check caveat); 3 new Excluded rows; GP-08 descoped. No v1.18 candidate is left UNVERIFIED. |

## Thread Adjudication

### Thread 1 — MA-01/02 + MI/IN fixes at `3381958`/`05eb9ad`: closable; SC-1 satisfied under recorded re-scope

**Fixes verified on the current tree (not taken on the REVIEW-FIX's word):**

- MA-01: SOURCE-VETTING.md:85 DAG row now reads "AAF guidebooks are the intended substitute but are **NOT yet vetted** — licence spot-check deferred (not a v1.18 build item); vet before any future use"; STATE.md:55 and SUMMARY deviation #4 corrected to "4 of 5 UNVERIFIED resolved; 5th (DAU AAF guidebooks licence spot-check) deferred"; VET-01 requirement text amended. This is exactly fix option (b) the code reviewer prescribed as acceptable.
- MA-02: SOURCE-VETTING.md:135 GP-06 row restamped "Statute-basis confirmation only … NO in-source licence inspection yet — build-time in-source confirmation REQUIRED for both A-94 and Army CBA … (Confirmed-by-statute 2026-08-16; build-time check outstanding.)" — the overstated verification claim is gone.
- MI-01 (":84 "late-1980s edition … circa 1989"), MI-02 (":129 SP-7084 "(VET-01 item, not a GP pack)" + :137 8→7 note), IN-01 (MILESTONES header), IN-02 (AE-03 doc tracked at `05eb9ad`) — all confirmed landed. `3381958` touched exactly the 5 files the reviewer scoped; no out-of-scope edits.

**SC-1 formal adjudication.** SC-1's letter ("All 5 UNVERIFIED items resolved to Tier 1/2/Excluded with evidence") is satisfied for the five items VET-01 itself names — including AFOTEC, which was an inline-UNVERIFIED row in the gap report's §4 excluded table and is now resolved to Excluded. Against the gap report's list lineage it is 4 resolved + 1 (DAU AAF guidebooks) formally deferred as not-a-v1.18-candidate. Adjudicated **not a gap**, on four grounds:

1. The phase goal is literally true: no v1.18 candidate is left without a definitive tier decision; the AAF guidebooks appear in no v1.18 build list (no GP slot, not SP-7084, only referenced as a future DAG substitute).
2. Gap-report item #5 is worded as a conditional spot-check obligation ("should be spot-checked during vetting"), not a pack candidate awaiting a tier decision — forcing it to Tier 1/2/Excluded now would be a research task serving only a hypothetical future revival, which nothing in v1.18 depends on.
3. The deferral is honest and quadruple-recorded (VET-01 text, STATE, SOURCE-VETTING DAG row, SUMMARY deviation #4) — the substitution is no longer silent, which was the actual defect in MA-01.
4. The reviewer's own prescribed acceptable remedy (option b: amend VET-01 + STATE/SUMMARY wording, soften the DAG row) is what was applied; option (a) (vet AAF now) was explicitly either-or.

**Residual (verify-time, non-blocking):** ROADMAP SC-1 lacks the parenthetical annotation VET-01 now carries, so the two texts read asymmetrically. When verify closes the Phase 6 checkbox (ROADMAP v1.18 phase list), it should append the same one-line annotation to SC-1 ("4/5 gap-report items + AFOTEC resolved; AAF guidebooks spot-check deferred — not a v1.18 candidate"). One-line paperwork in the edit verify already performs; not execute re-entry.

### Thread 2 — Phase 7 preconditions (routing; see §Phase 7 Routing)

All build-time obligations Phase 6 recorded are already encoded in the vetted rows and REQUIREMENTS GP notes; they route forward as Phase 7 plan preconditions, with the security audit's N3 making T-6-03 enforcement a Phase 7 security-pass obligation. No Phase 6 gap — recording was this phase's declared obligation and it is complete (T-6-03 CLOSED at the declared boundary).

### Thread 3 — External vet_source.py EXCLUDED-dict sync (AFOTEC/DAG/SEI): ACCEPT as recorded gap, backlog

Integration WARNING-1: `jgs-reference-skill/tools/vet_source.py` returns Tier 1 for AFOTEC and DoD DAG, Tier 3 + warning for CMU SEI; none are encoded in its EXCLUDED dict. Adjudicated **accept** (route to backlog), same class as Phase 2 P3-PRE-2 and the Phase 3 recorded accepted gap ("human rubric governs; the tool under-blocks"):

- The fix lives in an external repo (jgs-reference-skill) — outside this repo's execute surface entirely.
- The governing integrity document is SOURCE-VETTING.md (human rubric); `tooling/validate_pack.py` independently enforces `license_tier ∈ {1,2,3}` at pack level, so an Excluded source can never ship regardless of the external classifier.
- None of the three sources appears in any Phase 7 build list — no E2E flow breaks (integration §2/§4).
- The AFOTEC/DAG exclusions are provenance-based (stale edition, retirement), not licence-keyword-expressible; a keyword classifier cannot encode them as-is without a design change that belongs to the external repo's backlog, not this phase.

**Route:** extend the existing external-repo sync backlog item to cover `afotec` / `dod dag` / `cmu sei` alongside the already-tracked `ecss`/`esa`/`def-stan` entries.

### Thread 4 — VET-01/VET-02 checkbox closure at verify: YES, both, with the annotation

- **VET-02: close.** Fully satisfied with no caveats — DAG, CMU SEI, and the failing UNVERIFIED candidate (AFOTEC) are all in the Excluded table with dated rationale (SC-2 verified).
- **VET-01: close.** Its requirement text as now written defines completion as "4/5 resolved; AAF guidebooks check deferred — not blocking Phase 7", and that state is what exists; every item the requirement names has a definitive tier decision with evidence. Closing it is honest — the deferral is part of the recorded requirement, not a hidden shortfall. The Phase 6 overview checkbox (ROADMAP v1.18 phase list) closes with it.
- Verify should also perform the SC-1 annotation (Thread 1 residual) in the same ROADMAP edit.

## Phase 7 Routing (preconditions to carry into the Phase 7 plan / 3 build waves)

| ID | Obligation | Source of record | Consequence if skipped |
|---|---|---|---|
| P7-PRE-1 | DIST-A **visual** cover confirmation at build for GP-07 / MIL-STD-40051-2C (statement is a scanned image on the mirror copy) and GP-05 / MIL-STD-881F (mirror-fetch) | SOURCE-VETTING.md:128, :131 | T-6-03 (tampering) re-opens in Phase 7 security pass |
| P7-PRE-2 | GP-06 dual-document **in-source licence confirmation REQUIRED for both** OMB Circular A-94 and US Army CBA Guide **before Phase 7 content generation** (lightest evidence trail of the eight — statute basis only) | SOURCE-VETTING.md:135; security audit N2 | T-6-03 re-opens; row's own REQUIRED condition unmet |
| P7-PRE-3 | Edition/revision recording in PACK.yaml: GP-03 DOT&E (8.02 or afacpo mirror v3-June, whichever actually built); GP-02 FAA-STD-025 (rev E canonical or rev F mirror) | SOURCE-VETTING.md:132-133; REQUIREMENTS GP-02/GP-03 | Provenance gap vs SC-2 of Phase 7 (PACK.yaml provenance complete) |
| P7-PRE-4 | GP-01 VV&A RPG chapter-wise build: confirm DIST-A / authorship inside **each chapter PDF used**; per-chapter provenance in PACK.yaml (no consolidated PDF exists) | SOURCE-VETTING.md:130; REQUIREMENTS GP-01 | Same as P7-PRE-3 plus per-chapter tamper exposure |
| P7-PRE-5 | Generic: the v1.18 section preamble's in-PDF statements (DIST-A, releasability lines, NTRS metadata) are confirmed at build for all statute-basis rows; Phase 7's security pass must verify T-6-03 enforcement (security audit N3 names this explicitly) | SOURCE-VETTING.md:121-124; 6-SECURITY_AUDIT N3 | T-6-03 re-opens |
| P7-FUT-1 (not Phase 7) | AAF guidebooks per-guidebook licence spot-check before any future DAG-substitute use | SOURCE-VETTING.md:85 | Future-scope only; not a v1.18 build item |
| P7-BACKLOG (external) | vet_source.py EXCLUDED-dict sync: add afotec / dod-dag / cmu-sei alongside ecss/esa/def-stan | 6-INTEGRATION_CHECK WARNING-1; Thread 3 | Under-blocking only; human rubric governs |

## Residual Notes That Ship (no action required)

- **ROADMAP SC-1 annotation asymmetry** — recommended one-liner at verify (Thread 1); the honest record already exists in four other surfaces.
- **SUMMARY D1 gate wording drift** — the coverage ref "grep -c 'Verified 2026-08-14' >= 18" now yields 17, because the MA-02 fix intentionally restamped one row to `Confirmed-by-statute 2026-08-16`; total dated verdict stamps remain 18 (≥ 18 plan must-have still passes). Verify should interpret the gate on the mixed-stamp basis; do not re-edit the stamp (that would recreate MA-02).
- **MN-03 date convention** — rows stamped with research date 2026-08-14 vs commit dates 2026-08-16; plan-mandated, documented in SUMMARY deviation #2. Cosmetic.
- **MN-01 / MN-02 process notes** — SDK side-effect atomicity and Task-5 gate advisory-under-per-task-commits; final tree verified correct; the commit-union pattern is recorded in SUMMARY as established practice.
- **6-RESEARCH.md:165** still says "AAF guidebooks remain the Tier 1 substitute" without the not-yet-vetted qualifier — the research store is the historical evidence record; the governing published register (:85) carries the qualifier. Acceptable as-is.
- **Working-tree dirt** — `.planning/master_flow_state.json` ×2 modified (flow bookkeeping, out of phase scope per all reviews).

## Rejected as Non-Gaps

- **"SC-1 fails because the AAF item is neither built nor excluded"** — rejected: recorded scope decision with rationale, reviewer-prescribed remedy applied, phase goal (every v1.18 candidate decided) literally true (Thread 1).
- **"vet_source.py misclassification blocks Phase 7"** — rejected: external-repo surface, precedent-accepted, no build-list overlap, pack-level enforcement independent (Thread 3).
- **"GP-06 row lacks build caveat"** — rejected: that was MA-02, fixed; the row now carries the strongest caveat of the eight.
- **"8 rows under a v1.18.0 heading vs 7-pack scope"** — rejected: MI-02 fixed (row annotation + section note at :137).
- **Phase-artifact quotes of pre-fix state** ("5 UNVERIFIED resolved" inside pre-fix plan/check text) — rejected: phase artifacts are historical records; the corrected claim is in STATE/SUMMARY-deviation-4/VET-01, and impl review explicitly scoped them out by design.

## Verify-Time Actions (checklist for the closing step)

1. Close VET-01 and VET-02 in REQUIREMENTS (honest per Thread 4) and the Phase 6 checkbox in ROADMAP's v1.18 phase list.
2. Append the SC-1 deferral annotation to ROADMAP Phase 6 SC-1 (one line, mirroring VET-01's wording).
3. Re-run the phase gates on the mixed-stamp basis: `http` = 0; dated stamps = 18; `python tooling/check_release.py` PASS.
4. Hand §Phase 7 Routing (P7-PRE-1..5, P7-FUT-1, P7-BACKLOG) into Phase 7 planning as explicit plan preconditions.

**Next commands:** none — no `plan-phase --gaps` / `execute --gaps-only` re-entry is required for Phase 6. Proceed to Phase 7 planning with the routing table above.

---

_Gap analysis: ZCode (gap-analysis subagent) — all four reviews read in full; fixes re-verified live on `main` at `05eb9ad`._
