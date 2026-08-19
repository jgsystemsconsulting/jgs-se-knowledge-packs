# Phase 2 Verification: Source vetting + ruled-out register

Date: 2026-08-14. Method: goal-backward verification against actual repo state (docs read directly; `python tooling/check_release.py` executed).

**Verdict:** passed

---

## Criterion 1 — Excluded table contains the four rejected sources with rationale and date

**PASS.** All four rows present in docs/SOURCE-VETTING.md Excluded table, each with rationale and a "(Verified 2026-08-14.)" date:

- ISO/IEC/IEEE (names all three of 15288/29148/21839): "**ISO / IEC / IEEE standards** (e.g. 15288, 42010, 12207, 29148, 21839) | Paywalled, all-rights-reserved. Licensed per-user, often via BSI/Accuris/IHS. Requirements engineering (29148) and tailoring (21839) are the same per-user licence model. (Verified 2026-08-14.)"
- INCOSE SE Handbook: "**INCOSE SE Handbook** | Copyrighted (Wiley). Not redistributable. (Verified 2026-08-14.)"
- INCOSE Guide to Writing Requirements: "**INCOSE Guide to Writing Requirements** | Purchase-only, all-rights-reserved (INCOSE). Revisit only if an open-licence edition appears (FUT-02). (Verified 2026-08-14.)"
- DAU/WARU 2022 duplicate: "**DAU/WARU SE Guidebook (Feb 2022) re-pack** | Duplicate of existing `packs/dau-se-guidebook/` in the 48-pack baseline (US-gov public domain; excluded for duplication, not licence). (Verified 2026-08-14.)"

Also confirmed: RO-01 checked in .planning/REQUIREMENTS.md — `- [x] **RO-01**: Add researched-and-rejected sources to docs/SOURCE-VETTING.md Excluded table...`.

## Criterion 2 — All 11 candidates have a recorded tier decision; source URLs live in 2-RESEARCH.md per Link Policy

**PASS.** 2-RESEARCH.md records a definitive decision for all 11:

- 8 x Tier 1 (VERIFIED), each with resolving source URL and licence evidence: NIST SP 800-171 Rev.3, NIST SP 800-61 Rev.3, MIL-HDBK-338B, MIL-HDBK-516C, NASA-STD-7009B + NASA-HDBK-7009, DOE O 413.3B Chg 7, CISA CPG 2.0, DOE SEM3 (URLs e.g. "https://csrc.nist.gov/pubs/sp/800/171/r3/final (confirmed)", "https://www.energy.gov/sites/prod/files/cioprod/documents/SEM3_1231.pdf").
- #9 IEEE 15288.2-2014: "Tier decision: **Excluded** (paywalled / all-rights-reserved...)" with URL https://standards.ieee.org/ieee/15288.2/5705/ and GET-program licence evidence.
- #10 ECSS-E-ST-10C Rev.1: "Tier decision: **Excluded** absent written ESA/ECSS consent" with ecss.nl URL and ECSS-P-00C §5.8 licence quote.
- #11 Def Stan 00-051: "Tier decision: **UNVERIFIED — pending manual retrieval**" — definitive for this milestone as deferred-excluded (see Criterion 3).

SOURCE-VETTING.md mirrors the 8 Tier-1 rows with licence evidence and states the Link Policy explicitly: "Source URLs for all vetted/excluded/UNVERIFIED candidates are recorded in `.planning/phases/2-source-vetting-ruled-out-register/2-RESEARCH.md` (Link Policy: never published in docs or packs)."

## Criterion 3 — Def Stan 00-051 redistribution terms resolved as a recorded deferral decision

**PASS.** SOURCE-VETTING.md has a dedicated section "Def Stan 00-051 — UNVERIFIED / excluded from this milestone" ending: "**Recorded outcome (2026-08-14):** deferred-excluded for this milestone; no pack build until the in-document terms are recorded by a registered DSTAN user." REQUIREMENTS.md T2-03 is unchecked with matching deferral: "- [ ] **T2-03**: ... **deferred-excluded pending registered DSTAN in-document licence check**." Decision path (OGL v3.0 → Tier 2; bespoke terms → Excluded) is recorded in both files.

## Mechanical gate + phase artifacts

- `python tooling/check_release.py` → "RELEASE CHECK: PASS — repo is release-ready against the mechanical gate." exit code 0.
- All required artifacts exist in .planning/phases/2-source-vetting-ruled-out-register/: 2-RESEARCH.md, 2-01-PLAN.md, 2-01-SUMMARY.md, 2-PLAN_CHECK.md, 2-PLAN_REVIEW.md, 2-IMPL_REVIEW.md, 2-CODE_REVIEW.md, 2-INTEGRATION_CHECK.md, 2-SECURITY_AUDIT.md, 2-GAP_ANALYSIS.md.

## Notes

- Two of three expected Tier-2 candidates (IEEE 15288.2, ECSS) were excluded by evidence rather than packaged; Phase 4 is correspondingly closed at 0 Tier-2 packs, which ROADMAP.md and REQUIREMENTS.md (REL-01: 56 packs) already reflect. This is a correct goal-backward outcome, not a gap.
- Phase goal "Every candidate source has a definitive tier decision with evidence" holds for 00-051 in the deferral sense: the decision is definitive for v1.17.0 (deferred-excluded) with a recorded revival path.
