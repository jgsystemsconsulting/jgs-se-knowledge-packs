# Phase 2 Plan Review

**Phase:** 2-source-vetting-ruled-out-register
**Plan reviewed:** `2-01-PLAN.md` (post-plan_check; W1–W6 from `2-PLAN_CHECK.md` not yet folded)
**Reviewed:** 2026-08-14
**Method:** Adversarial plan review against ROADMAP Phase 2 SC1–SC3, REQUIREMENTS (RO-01, T2-01–T2-03, REL-01/02), `docs/SOURCE-VETTING.md` (tiers, checklist, Link Policy), and `2-RESEARCH.md`. Every factual premise re-verified against the working tree.

**Verdict:** NEEDS_WORK

The plan's propagation logic (SOURCE-VETTING → REQUIREMENTS → ROADMAP → STATE, 56-pack recompute, 0 Tier-2) is correct and well-sequenced, and the count math (48 + 8 = 56) checks out. But one instruction set is self-contradictory and breaches the repo's own published Link Policy if executed as written (BL-01), the plan claims ROADMAP SC1–SC3 will be "all satisfied" when SC1/SC2 remain only partially satisfiable as tasked (MA-01, MA-05), and three of the automated verifies are passable without the intended edit (MA-02). All fixes are small, in-scope plan edits — no re-planning, no split, no new files required.

---

## Findings

### BL-01. [BLOCKER] [licence_contract] Task 1.3 publishes source URLs in docs/SOURCE-VETTING.md against that doc's own Link Policy, justified by a false premise

**Plan:** 2-01-PLAN.md:75 (Task 1 item 3); amplified by must_haves truth at :24 and threat T-2-03 at :158
**Issue:** Task 1.3 instructs "Copy URLs and licence evidence lines from 2-RESEARCH.md" into a `Source | Tier | URL | Licence evidence` table in docs/SOURCE-VETTING.md, and justifies this with "the doc's Link Policy note: these URLs are vetting evidence recorded in the integrity doc (which is where vetting URLs already live per the checklist)". That premise is factually false and the instruction contradicts the policy:

- Link Policy (docs/SOURCE-VETTING.md:122–125): source-material URLs "are **not** published anywhere in a pack **or the docs**". docs/SOURCE-VETTING.md is in `docs/`.
- Checklist item 1 (:108–109): "the source URL is used for vetting only, **never published**".
- Checklist item 8 (:116–117): "**no source-material URL published** (see LICENSING.md)".
- Empirically verified: `grep -n "http" docs/SOURCE-VETTING.md` returns nothing — zero URLs live in that doc today, including in the row added 2026-08-14 (INCOSE Competency Framework, commit e5f01bc).

The executor is told both "copy the URLs in" and "respect the doc's Link Policy note" — the trailing clause "do NOT publish them in any pack" silently drops the policy's "or the docs" scope, so both branches cannot be obeyed. Threat T-2-03's "accept" disposition rests on the same false premise. This is the repo's licence-integrity trust anchor; executing as written makes it violate its own published policy.
**Fix:** Pick one branch and make the plan say it:
- (b) (recommended — also resolves MA-05): drop the URL column; identify sources by title + publisher + version; add one pointer line to the section: "Source URLs for all vetted/excluded candidates are recorded in `.planning/phases/2-source-vetting-ruled-out-register/2-RESEARCH.md` (Link Policy: never published in docs or packs)." Update the must_haves truth (:24) to remove "with source URL" and re-scope threat T-2-03, or
- (a): make Task 1 explicitly amend the Link Policy paragraph to add a scoped integrity-doc exception as part of the same edit — but then the policy text and the new table must land in the same commit, and LICENSING.md §4 (cross-referenced at :125) needs the same exception.

### MA-01. [MAJOR] [requirement_coverage] SC1's "each with rationale and date" is left unsatisfiable for the two pre-existing rows while the plan claims SC1–SC3 all satisfied

**Plan:** 2-01-PLAN.md:67 ("append '(Verified 2026-08-14.)' to **each new row**"), :74 (amends ISO row without dating it), :169 (claims "Phase 2 success criteria 1-3 (ROADMAP) all satisfied")
**Issue:** ROADMAP Phase 2 SC1 requires INCOSE Handbook, INCOSE GWR, ISO/IEC/IEEE 15288/29148/21839, and the DAU/WARU duplicate "each with rationale **and date**". The Handbook row (docs/SOURCE-VETTING.md:72) and the ISO/IEC/IEEE row (:71) are pre-existing and undated; the plan dates only the new rows. After execution, SC1's date requirement is unmet for two of its four named sources, yet the plan's success_criteria asserts full satisfaction — a false gate claim that Phase 2 verify would surface. (Checker W1, unfolded.)
**Fix:** In Task 1, append "(Verified 2026-08-14.)" to the existing INCOSE SE Handbook and ISO/IEC/IEEE rows when the example list is extended (research confirmed both rulings 2026-08-14, so the date is honest), and add `grep -c "Verified 2026-08-14" docs/SOURCE-VETTING.md` ≥ 8 (4 new + 2 amended + GWR + DAU) plus a `21839` assertion to the Task 1 verify.

### MA-02. [MAJOR] [verification_derivation] Task 2 and Task 4 `grep -c "56"` verifies are passable via the incidental "00-056" string; REQUIREMENTS.md currently contains no "56"/"59" at all

**Plan:** 2-01-PLAN.md:96 (Task 2 verify), :125 (Task 4 verify), :91–92 (Task 2 writes the "00-051/00-056" subject note), :122 (Task 4 writes "00-051/00-056" into STATE.md)
**Issue:** Verified: `.planning/REQUIREMENTS.md` contains zero occurrences of "56" or "59" today. Task 2 step 4 says "replace any 59+ assumption" — there is none in REQUIREMENTS (REL-01/REL-02 at :49–50 carry no pack count; the 59+ strings live only in ROADMAP:60 and STATE:33, handled by Tasks 3–4). So the only "56" Task 2 is guaranteed to produce is the "00-056" inside the subject-mismatch note — `grep -c "56"` passes with the REL/milestone count never updated. Task 4 has the identical hole ("00-051/00-056 subject-mismatch noted" satisfies `grep -c "56" .planning/STATE.md`). Task 1's verify (:79) additionally omits 21839, the date stamps, the 8 Tier-1 names, and any URL/licence-evidence column check. (Checker W5, unfolded and sharpened.)
**Fix:** Assert distinctive strings: Task 2 — `grep -c "56 (48 baseline + 8 Tier-1)" .planning/REQUIREMENTS.md` (and have Task 2 actually write that string into the v1.17.0 section header, since no count exists there today); Task 4 — `grep -c "target after v1.17.0: 56" .planning/STATE.md`; Task 1 — add greps for `21839`, `Verified 2026-08-14`, and one short name per Tier-1 source (e.g. `800-171`, `800-61`, `338B`, `516C`, `7009`, `413.3B`, `CPG 2.0`, `SEM3`).

### MA-03. [MAJOR] [key_links_planned] Phase 4 "rewrite the phase entry" is ambiguous — the Goal/Success Criteria and the top-level "Build the 3 Tier-2 packs" bullet can survive as live build instructions

**Plan:** 2-01-PLAN.md:107 (Task 3.1)
**Issue:** ROADMAP has two Phase-4 surfaces: the Phases bullet at ROADMAP.md:12 ("**Phase 4: Tier 2 packs (conditional licences)** - Build the 3 Tier-2 packs with attribution preserved") and the Phase Details block at :46–53 (Goal "3 conditional-licence packs built…", Requirements [T2-01, T2-02, T2-03], Success Criteria "Each pack's LICENSE reproduces source terms; attribution banners present"). Task 3.1 says "Rewrite the phase entry … and update its Requirements list accordingly" — it does not explicitly require rewriting the Goal and Success Criteria, and does not name the bullet at :12 at all. If either survives, ROADMAP still instructs a future executor to build licence-breaching packs (IEEE/ECSS are Excluded; 00-051 UNVERIFIED) — precisely the harm W6 describes. Task 3's verify (no "59+", "56 packs" present) cannot catch this. (Checker W6, unfolded.)
**Fix:** Enumerate in Task 3.1: rewrite **both** ROADMAP:12 and the :46–53 block — Goal → "closed by vetting: 0 Tier-2 packs", Requirements → point at the SOURCE-VETTING outcome instead of listing T2-01/T2-02/T2-03 as active, Success Criteria → "no execution; outcome recorded in docs/SOURCE-VETTING.md". Keep-the-slot (no renumbering) is the right churn trade. Add a verify grep asserting `grep -c "Build the 3 Tier-2 packs" .planning/ROADMAP.md | grep -q '^0$'`.

### MA-04. [MAJOR] [scope_reduction] "Mark T2-03 resolved as deferred-excluded" + frontmatter `requirements: [RO-01, T2-03]` risks ticking T2-03 [x] when the licence read never happened

**Plan:** 2-01-PLAN.md:91 (Task 2 step 3: "mark **resolved** as deferred-excluded"), :13 (frontmatter), :109 (Task 3.3 SC3 annotation)
**Issue:** 2-RESEARCH.md:189–195 is explicit: the tier decision is "UNVERIFIED — pending manual retrieval" by a registered DSTAN user; the in-document copyright/reuse statement was never inspected. T2-03 as written (REQUIREMENTS.md:41) is a vet-then-decide requirement; deferral is a conservative milestone decision, not a completed vet. The plan's verb "mark resolved" invites the executor to tick the T2-03 checkbox, permanently recording an unverified licence read as a satisfied requirement — and the revival path then depends solely on the Future Candidates note. The Task 3.3 SC3 annotation itself is defensible (SC3's own parenthetical already reads "build-or-exclude decision recorded"), but only if the recorded decision is labelled UNVERIFIED-deferral, not resolution. (Checker W3, unfolded.)
**Fix:** Reword Task 2 step 3 to "record T2-03 as deferred-excluded for v1.17.0 — keep the checkbox **unchecked**; annotate 'in-document terms UNVERIFIED; no DSTAN retrieval performed this milestone'". Keep the one-line open note ("licence read remains open if 00-051 is revived") in both the Future Candidates entry and the SC3 annotation, and change `mark resolved` → `record outcome` throughout (:91, must_hives :25).

### MA-05. [MAJOR] [requirement_coverage] SC2's "source URL and licence evidence" is unmet for 3 of 11 candidates and the plan leaves the disposition implicit

**Plan:** 2-01-PLAN.md:70–76 (Task 1 items 1–4)
**Issue:** ROADMAP SC2 requires each of the 11 candidates to have "a recorded tier decision with source URL and licence evidence". The Vetted table covers 8. IEEE 15288.2-2014 and ECSS land in the two-column Excluded table (no URL field; the prescribed rationale carries licence evidence only), and Def Stan 00-051 is UNVERIFIED with no inspected in-document evidence. The plan nowhere states where SC2's URL half for these three lives — it is currently discoverable only by reading 2-RESEARCH.md. Note this finding and BL-01 are two faces of one decision: adding URLs to the doc breaches the Link Policy (BL-01); the pointer-line resolution satisfies both. (Checker W2, unfolded.)
**Fix:** Resolve jointly with BL-01 option (b): the explicit pointer line ("SC2 URL evidence for excluded/UNVERIFIED candidates is recorded in 2-RESEARCH.md §Tier-2 candidates") makes the SC2 record complete by reference; alternatively include each research URL inside the exclusion rationale text — but only under BL-01 option (a)'s policy exception.

### MI-01. [MINOR] [doc_consistency] ECSS mirrored under the "Paywalled standards full texts" Out-of-Scope umbrella, but ECSS is free-to-download

**Plan:** 2-01-PLAN.md:89 (Task 2 step 1)
**Issue:** Task 2 cites the umbrella row "Paywalled standards full texts" (REQUIREMENTS.md:63) as the mirror rationale for both T2-01 and T2-02. The label fits IEEE 15288.2 (purchase/subscription only) but contradicts the plan's own ECSS rationale (:71 — "free download from ecss.nl but © ESA"). The umbrella row's *reason* column ("Not licence-redistributable") fits both; the *label* does not.
**Fix:** Use reason text "Not licence-redistributable (see docs/SOURCE-VETTING.md)" for the T2-02 mirror, or add a second umbrella row "Free-download, no-redistribution-grant standards (ECSS/ESA)" alongside the paywalled row.

### MI-02. [MINOR] [cross_artifact_drift] Plan's verification claim "no artifact … implies Tier-2 packs in v1.17.0" is over-broad: PROJECT.md and MILESTONES.md are outside files_modified and still say "3 Tier-2"

**Plan:** 2-01-PLAN.md:164 (verification bullet); files_modified at :7–11
**Issue:** Verified: PROJECT.md:44 ("11 researched candidate packs (8 Tier-1, 3 Tier-2)") and MILESTONES.md:9 ("3 Tier-2 conditional licence") both still imply Tier-2 packs in v1.17.0 and are not in scope. The verification bullet as written will be false after execution. (Checker I3.)
**Fix:** Either add a two-line fifth edit (or a rider on Task 3) touching those two strings, or narrow the claim to "no artifact in files_modified still says 59+ or implies Tier-2 packs".

### MI-03. [MINOR] [robustness] "Use Edit (scoped replacements), never whole-file Write" is mandated only for Task 3

**Plan:** 2-01-PLAN.md:106 (Task 3 only)
**Issue:** Tasks 1, 2, and 4 edit docs of equal or greater fragility — docs/SOURCE-VETTING.md carries the SPDX/MIT licence header at :1–4 and is the repo's integrity document; a whole-file rewrite risks dropping the header or reflowing the policy text. The Edit-only constraint should be plan-wide.
**Fix:** Hoist the constraint to the plan preamble or repeat it in Tasks 1, 2, and 4.

### MI-04. [MINOR] [data_quality] Verbatim-copy rule would propagate the truncated ECSS URL from 2-RESEARCH.md

**Plan:** 2-01-PLAN.md:35 (key_links "verbatim rationale"), :156 (threat T-2-01 "do not paraphrase")
**Issue:** 2-RESEARCH.md:157 records the ECSS URL as `https://ecss.nl/standard/ecss-e-st-10c-rev-1-...-15-february-2017/` — containing a literal ellipsis. Any outcome record copying research strings verbatim (and any future URL recording under BL-01 option (a)) inherits a dead link.
**Fix:** Note in Task 1 that the ECSS URL in research is abbreviated; if a URL is ever recorded, resolve it against ecss.nl first. Rationale *text* can stay verbatim; URLs cannot.

### MI-05. [MINOR] [licence_contract] "Vetted candidates" section label slightly overclaims vs checklist item 2 for the statute-based Tier-1 rows

**Plan:** 2-01-PLAN.md:75 (Task 1 item 3)
**Issue:** The vetting checklist (docs/SOURCE-VETTING.md:110–111) requires the licence statement "in the source itself, not a third-party claim". For NIST (footer), CISA (title page), DOE O 413.3B and DOE SEM3, 2-RESEARCH.md marks the in-PDF statements unconfirmed until build time (tier rests on 17 U.S.C. § 105 + repo precedent). The planned build-time-confirmation note mitigates this, but a bare "Vetted" heading in the integrity doc reads as checklist-complete.
**Fix:** Title the section "Vetted candidates (v1.17.0) — Tier 1; in-document statements confirmed at build (Phase 3)" or add the pending-confirmation qualifier to each affected row (NIST ×2, CPG 2.0, 413.3B, SEM3).

---

## W1–W6 incorporability

| Checker finding | Folded into plan? | Incorporable within current scope? | This review |
|---|---|---|---|
| W1 SC1 dates on Handbook/ISO rows | No | Yes — same file, same task, two appends + verify line | MA-01 |
| W2 SC2 URLs for 3 non-Tier-1 | No | Yes — one pointer sentence (joint with W4) | MA-05 |
| W3 T2-03 not fully resolved | Partially (deferred-excluded recorded; "mark resolved" verb and frontmatter remain) | Yes — wording only | MA-04 |
| W4 Link Policy vs Vetted URLs | No (contradiction restated at :75) | Yes — drop URL column or add explicit policy exception; touches must_hives + threat register, still plan-scope | BL-01 |
| W5 grep false-pass | No | Yes — distinctive-string asserts | MA-02 |
| W6 Phase 4 vacuous criteria | Partially (preferred option stated; Goal/SC/bullet not enumerated) | Yes — enumerate surfaces in Task 3.1 | MA-03 |

All six fold into the existing four tasks without new files, new tasks, re-sequencing, or estimate change (well under the 100k budget). W2 and W4 must be resolved as a single decision (URL column in-doc vs pointer to research) because they pull in opposite directions; the pointer option satisfies both plus the Link Policy.

## Claims re-verified against the tree

- No `http` URLs anywhere in docs/SOURCE-VETTING.md (BL-01 premise check).
- `packs/dau-se-guidebook/` exists (count = 1).
- Excluded table header at docs/SOURCE-VETTING.md:69; ISO row examples "15288, 42010, 12207" at :71; undated Handbook row at :72.
- REQUIREMENTS.md: T2-01/T2-02/T2-03 at :39–41; REL-01/REL-02 at :49–50 (no pack-count strings anywhere in the file); Out of Scope table at :59–66; Future Candidates at :52–57 (both targets of Task 2 exist).
- ROADMAP.md: Overview "3 Tier-2" at :5; Phase-4 bullet "Build the 3 Tier-2 packs" at :12; Phase 4 details at :46–53; Phase 5 "59+ packs" at :60; Phase 2 SC3 at :33.
- STATE.md "target after v1.17.0: 59+" at :33; Task 4's "00-051/00-056" note would satisfy its own `grep -c "56"` verify.
- 2-RESEARCH.md sections cited by the plan's claim_verification all present at the cited lines (spot-checked :136–165, :173–179, :213–229).
- Count math: 48 + 8 = 56; original 59+ = 48 + 11. Consistent across Tasks 2–4.

## Recommendation

Fix BL-01 before execution (one decision, then three coordinated line edits: Task 1.3 action, must_hives truth :24, threat T-2-03 :158 — plus the MA-05 pointer sentence if option (b)). Fold MA-01 through MA-05 in the same pass; all are wording/verify-level. With those edits the plan is APPROVE-grade: scope, sequencing, preconditions, and the exclusion propagation itself are sound. MI-01 through MI-05 can ride along or be deferred to execution judgement.

---

_Reviewed: 2026-08-14_
_Reviewer: ZCode (gsd plan reviewer)_
_Depth: deep (cross-artifact: plan ↔ ROADMAP ↔ REQUIREMENTS ↔ SOURCE-VETTING ↔ LICENSING/Link Policy ↔ 2-RESEARCH ↔ tree state)_
