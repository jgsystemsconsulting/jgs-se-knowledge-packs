---
phase: 2-source-vetting-ruled-out-register
plan: 01
type: execute
wave: 1
depends_on: []
files_modified:
  - docs/SOURCE-VETTING.md
  - .planning/REQUIREMENTS.md
  - .planning/ROADMAP.md
  - .planning/STATE.md
  - .planning/PROJECT.md
  - .planning/MILESTONES.md
autonomous: true
requirements: [RO-01, T2-03]
estimate:
  tokens: 24000
  raw_tokens: 18000
  tasks: 4
  confidence: high

must_haves:
  truths:
    - "docs/SOURCE-VETTING.md Excluded table contains new dated rows for IEEE 15288.2-2014, ECSS standards (incl. ECSS-E-ST-10C Rev.1), INCOSE Guide to Writing Requirements, and the DAU/WARU Feb-2022 duplicate (dedup rationale, not licence)"
    - "The existing ISO/IEC/IEEE row's example list names 15288, 29148, and 21839"
    - "All 8 Tier-1 candidates are recorded as Vetted with licence evidence (US-gov work basis, 17 U.S.C. § 105); NO source URLs are published in docs/SOURCE-VETTING (Link Policy: source-material URLs are never published in a pack or the docs) — SC2's 'source URL' criterion is satisfied by reference via a pointer line to 2-RESEARCH.md as the URL evidence store"
    - "Def Stan 00-051 is recorded as UNVERIFIED/excluded-for-this-milestone pending a registered DSTAN check of in-document terms, with the 00-051 (environmental mgmt) vs 00-056 (system safety) subject-mismatch note"
    - "REQUIREMENTS.md T2-01 and T2-02 are struck as excluded-by-vetting with rationale in Out of Scope; T2-03 recorded as deferred-excluded; REL-01/REL-02 count recomputed to 56 (48 + 8)"
    - "ROADMAP.md Phase 4 reflects 0 Tier-2 packs this milestone (folded/dropped); Phase 5 gate says 56 packs, not 59+"
    - "STATE.md focus/notes match the recomputed counts and the T2-01/T2-02 exclusion outcome"
  artifacts:
    - docs/SOURCE-VETTING.md (updated Excluded table + new URL-free Vetted/UNVERIFIED sections with 2-RESEARCH.md URL-evidence pointer)
    - .planning/REQUIREMENTS.md (T2-01/T2-02 struck, Out of Scope extended, REL counts fixed)
    - .planning/ROADMAP.md (Phase 4/5 corrected)
    - .planning/STATE.md (focus/notes synced)
  key_links:
    - "2-RESEARCH.md findings → SOURCE-VETTING.md rows (every row cites its research evidence, verbatim rationale from the research file's 'How docs/SOURCE-VETTING.md should be extended' section)"
    - "SOURCE-VETTING exclusion outcome → REQUIREMENTS T2-01/T2-02 strike-through + Out of Scope entry"
    - "Exclusion outcome → ROADMAP Phase 4 shrink + Phase 5 count → STATE.md"
---

<objective>
Record definitive tier decisions for all 11 v1.17.0 candidates and propagate the two overturned Tier-2 assumptions (IEEE 15288.2-2014 and ECSS-E-ST-10C Rev.1 are Excluded, not Tier 2) through the planning artifacts so Phase 3+ build against the corrected 56-pack target.

Purpose: The research (2-RESEARCH.md) is authoritative and overturns the milestone's Tier-2 plan. If the docs/planning artifacts are not updated, Phase 4 would attempt licence-breaching packs and Phase 5's gate count (59+) would be wrong.
Output: Updated docs/SOURCE-VETTING.md, .planning/REQUIREMENTS.md, .planning/ROADMAP.md, .planning/STATE.md. No packs built, no code.
</objective>

<execution_context>
@$HOME/.zcode/gsd-core/workflows/execute-plan.md
@$HOME/.zcode/gsd-core/templates/summary.md
</execution_context>

<context>
@.planning/PROJECT.md
@.planning/ROADMAP.md
@.planning/STATE.md
@.planning/phases/2-source-vetting-ruled-out-register/2-RESEARCH.md
@docs/SOURCE-VETTING.md
@docs/PACK-SPEC.md
</context>

<tasks>

<task type="auto">
  <name>Task 1: Extend docs/SOURCE-VETTING.md with vetting outcomes</name>
  <files>docs/SOURCE-VETTING.md</files>
  <action>
    Four edits, all sourced verbatim from 2-RESEARCH.md §"How docs/SOURCE-VETTING.md should be extended" and §"Ruled-out confirmations". Use Edit (scoped replacements), never whole-file Write — docs/SOURCE-VETTING.md carries an SPDX/MIT licence header that a whole-file rewrite risks dropping. Follow the existing two-column `Source | Why excluded` table format; append "(Verified 2026-08-14.)" to each new row per the Phase 2 success criterion (dated rationale).

    1. Add four new rows to the Excluded table:
       - **IEEE 15288.2-2014** — purchase/subscription only; not in the IEEE GET program; IEEE sole copyright holder, GET downloads are personal-use with no redistribution/derivative grant.
       - **ECSS standards (incl. ECSS-E-ST-10C Rev.1)** — free download from ecss.nl but © ESA; "No ECSS document may be reproduced in any form without the explicit consent of ESA" (ECSS-P-00C §5.8); a pack is reproduction + derivative work.
       - **INCOSE Guide to Writing Requirements** — purchase-only, all-rights-reserved (INCOSE); note the FUT-02 revisit trigger if an open-licence edition appears.
       - **DAU/WARU SE Guidebook (Feb 2022) re-pack** — duplicate of existing `packs/dau-se-guidebook/` in the 48-pack baseline; state explicitly this is a dedup exclusion (US-gov public domain), NOT a licence problem, so readers don't infer one.
    2. Amend the existing **ISO / IEC / IEEE standards** row: extend its example list from "(e.g. 15288, 42010, 12207)" to also name 29148 and 21839 (requirements engineering + tailoring; licensed per-user via BSI/Accuris/IHS), and append "(Verified 2026-08-14.)" to this row (research reconfirmed the ruling 2026-08-14) so SC1's "each with rationale and date" holds for pre-existing rows too. Also append "(Verified 2026-08-14.)" to the existing **INCOSE SE Handbook** row (same vetting pass) — SC1 names it and it is currently undated.
    3. Add a **"Vetted candidates (v1.17.0) — statute-basis; confirm in-source at build"** section after the Excluded tier section, recording the 8 Tier-1 confirmations as a compact table (Source | Tier | Licence evidence) — **no URL column**: NIST SP 800-171 Rev.3, NIST SP 800-61 Rev.3, MIL-HDBK-338B, MIL-HDBK-516C, NASA-STD-7009B + NASA-HDBK-7009, DOE O 413.3B Chg 7, CISA CPG 2.0, DOE SEM3. Copy licence-evidence lines from 2-RESEARCH.md §Tier-1 candidates; identify sources by title + publisher + version only. Per the doc's Link Policy (source-material URLs are "not published anywhere in a pack **or the docs**"), do NOT put any source URL in docs/SOURCE-VETTING.md. Instead add one pointer line to the section: "Source URLs for all vetted/excluded/UNVERIFIED candidates are recorded in `.planning/phases/2-source-vetting-ruled-out-register/2-RESEARCH.md` (Link Policy: never published in docs or packs)" — this also completes SC2's URL half for the excluded/UNVERIFIED candidates by reference. Do not copy URLs from research even as evidence: the ECSS URL in 2-RESEARCH.md is abbreviated/truncated and would propagate a dead link. Add a note that in-PDF statements (NIST footers, CISA title page, DOE SEM third-party notices) are confirmed at build time in Phase 3 — the statute-basis rows are pending that in-source confirmation.
    4. Add a **Def Stan 00-051 — UNVERIFIED / excluded from this milestone** subsection recording: Crown copyright; downloads registration-gated via the DSTAN portal so in-document reuse terms could not be inspected; excluded from v1.17.0 pending a registered DSTAN user recording the exact cover/inside-front copyright/reuse statement (OGL v3.0 → Tier 2 attribution; bespoke MOD-consent terms → stays Excluded). Also correct the subject description wherever 00-051 is named: it is *Environmental Management Requirements for Defence Systems*; system safety is Def Stan 00-056 — the original candidate description conflated them.
  </action>
  <verify>
    <automated>grep -c "15288.2-2014\|ECSS-E-ST-10C\|Guide to Writing Requirements\|dau-se-guidebook" docs/SOURCE-VETTING.md | grep -qv '^0$' && grep -c "29148" docs/SOURCE-VETTING.md | grep -qv '^0$' && grep -c "21839" docs/SOURCE-VETTING.md | grep -qv '^0$' && grep -c "statute-basis; confirm in-source at build" docs/SOURCE-VETTING.md | grep -qv '^0$' && grep -c "00-056" docs/SOURCE-VETTING.md | grep -qv '^0$' && [ "$(grep -c "Verified 2026-08-14" docs/SOURCE-VETTING.md)" -ge 8 ] && grep -c "800-171\|800-61\|338B\|516C\|7009\|413.3B\|CPG 2.0\|SEM3" docs/SOURCE-VETTING.md | grep -qv '^0$' && [ "$(grep -c "http" docs/SOURCE-VETTING.md)" -eq 0 ] && echo PASS</automated>
  </verify>
  <done>Excluded table has 4 new dated rows; ISO/IEC/IEEE row names 29148 and 21839 and both pre-existing rows (ISO/IEC/IEEE, INCOSE SE Handbook) are dated 2026-08-14 (≥8 "Verified 2026-08-14" stamps total); Vetted-candidates section lists all 8 Tier-1 sources with licence evidence and NO URLs (doc remains URL-free per Link Policy) plus the 2-RESEARCH.md pointer line; Def Stan 00-051 outcome and 00-051/00-056 subject-mismatch note recorded. Committed independently.</done>
</task>

<task type="auto">
  <name>Task 2: Strike T2-01/T2-02, resolve T2-03, recompute REL counts in REQUIREMENTS.md</name>
  <files>.planning/REQUIREMENTS.md</files>
  <precondition>Task 1 committed (SOURCE-VETTING.md now records the exclusion evidence the rationale links to).</precondition>
  <action>
    Use Edit (scoped replacements), never whole-file Write.
    1. **T2-01** (IEEE 15288.2-2014): mark `~~struck~~` / rewrite as **excluded-by-vetting** with one-line rationale: "Excluded 2026-08-14 — purchase-only, not in IEEE GET program, IEEE sole copyright, no redistribution/derivative grant (see docs/SOURCE-VETTING.md)." Move to the Out of Scope table under the existing umbrella row "Paywalled standards full texts".
    2. **T2-02** (ECSS-E-ST-10C Rev.1): same treatment — rationale: "Excluded 2026-08-14 — © ESA; ECSS-P-00C §5.8 forbids reproduction without explicit ESA consent; a pack is reproduction + derivative." For the Out of Scope mirror do NOT use the "Paywalled" label — ECSS downloads are free (© ESA, no redistribution grant). Use reason text "Non-redistributable free downloads (see docs/SOURCE-VETTING.md)", or add a second umbrella row "Free-download, no-redistribution-grant standards (ECSS/ESA)" alongside the paywalled row.
    3. **T2-03** (Def Stan 00-051): recorded outcome: **deferred-excluded pending registered DSTAN in-document licence check** — keep the T2-03 checkbox UNCHECKED (the in-document terms were never inspected; this is a conservative milestone deferral, not a completed vet — do not use the word "resolved"). Annotate "in-document terms UNVERIFIED; no DSTAN retrieval performed this milestone"; note the subject-mismatch correction (00-051 = environmental management; safety is 00-056) and that any future revival must re-point the requirement and re-read the licence. Record this outcome in the "v2 Requirements (Deferred)" Future Candidates section so it isn't lost.
    4. **REL-01 / REL-02**: write the literal string **56 (48 baseline + 8 Tier-1)** into the v1.17.0 milestone expectation (no pack count exists in REQUIREMENTS today), and adjust REL wording that implies Tier-2 packs (T2-01/T2-02 excluded; T2-03 deferred means 0 Tier-2 packs in v1.17.0).
    5. Leave the existing Out of Scope row "Paywalled standards full texts" as the umbrella rationale; the two new entries cite it.
  </action>
  <verify>
    <automated>grep -c "excluded-by-vetting" .planning/REQUIREMENTS.md | grep -qv '^0$' && grep -c "56 (48 baseline + 8 Tier-1)" .planning/REQUIREMENTS.md | grep -qv '^0$' && grep -c "deferred-excluded pending registered DSTAN" .planning/REQUIREMENTS.md | grep -qv '^0$' && echo PASS</automated>
  </verify>
  <done>T2-01 and T2-02 struck with dated rationale and mirrored in Out of Scope (ECSS under non-redistributable free downloads, not paywalled); T2-03 recorded as deferred-excluded pending registered DSTAN in-document licence check with checkbox UNCHECKED, subject-mismatch note, and a Future Candidates entry; REL-01/REL-02 carry the literal "56 (48 baseline + 8 Tier-1)" count. Committed independently.</done>
</task>

<task type="auto">
  <name>Task 3: Shrink Phase 4 and fix Phase 5 count in ROADMAP.md</name>
  <files>.planning/ROADMAP.md</files>
  <precondition>Task 2 committed (ROADMAP must match the corrected REQUIREMENTS, not fight it).</precondition>
  <action>
    Use Edit (scoped replacements), never whole-file Write.
    1. **Phase 4 (Tier 2 packs)**: 0 Tier-2 packs remain for this milestone — T2-01/T2-02 excluded by vetting, T2-03 deferred-excluded. Rewrite **both** Phase-4 surfaces in ROADMAP.md so no live Tier-2 build instruction survives anywhere: (a) the Phases bullet (currently "Phase 4: Tier 2 packs (conditional licences) - Build the 3 Tier-2 packs with attribution preserved") → "Phase 4: Tier 2 packs — closed by vetting: 0 packs (T2-01/T2-02 Excluded, T2-03 deferred; see docs/SOURCE-VETTING.md)"; and (b) the Phase Details block: Goal → "closed by vetting: 0 Tier-2 packs", Requirements → point at the SOURCE-VETTING outcome instead of listing T2-01/T2-02/T2-03 as active, Success Criteria → "no execution; outcome recorded in docs/SOURCE-VETTING.md". Keep-the-slot (no renumbering; downstream `Depends on` references stay stable); do NOT drop the phase.
    2. **Phase 5 (Release surface)**: change the success criterion from "59+ packs" to **56 packs** (48 + 8). Update the Overview line "11 researched candidate packs (8 Tier-1, 3 Tier-2)" to reflect 8 Tier-1 builds + 3 vetted-out.
    3. **Phase 2 success criterion 3** ("Def Stan 00-051 redistribution terms resolved"): annotate that the recorded outcome for this milestone is *deferred-excluded pending registered DSTAN in-document licence check* (decision recorded, build deferred — never worded as "resolved") so the criterion reads as satisfied by the recorded decision rather than by an unblock.
  </action>
  <verify>
    <automated>grep -c "59+" .planning/ROADMAP.md | grep -q '^0$' && grep -c "56 packs" .planning/ROADMAP.md | grep -qv '^0$' && grep -c "Build the 3 Tier-2 packs" .planning/ROADMAP.md | grep -q '^0$' && grep -c "closed by vetting" .planning/ROADMAP.md | grep -qv '^0$' && echo PASS</automated>
  </verify>
  <done>No "59+" remains; no "Build the 3 Tier-2 packs" bullet remains; Phase 4 bullet AND Details block (Goal, Requirements, Success Criteria) record the closed-by-vetting outcome (0 packs); Phase 5 gate says 56 packs; Overview reflects 8 Tier-1 + 3 vetted-out. Committed independently.</done>
</task>

<task type="auto">
  <name>Task 4: Sync STATE.md focus and notes</name>
  <files>.planning/STATE.md, .planning/PROJECT.md, .planning/MILESTONES.md</files>
  <precondition>Tasks 1-3 committed.</precondition>
  <action>
    Use Edit (scoped replacements), never whole-file Write.
    1. STATE.md: update to match the corrected milestone: Performance Metrics "Packs shipped: 48 (target after v1.17.0: 56)"; Deviations/Notes — replace the T2-03 line with the recorded outcome ("T2-01/T2-02 excluded by vetting (IEEE GET terms / ECSS-P-00C §5.8); Def Stan 00-051 deferred-excluded pending registered DSTAN in-document licence check + 00-051/00-056 subject-mismatch noted; 0 Tier-2 packs in v1.17.0"); Current focus unchanged in substance (Phase 2 vetting) unless Phase 2 is thereby complete, in which case note "Phase 2 outcome recorded; next: Phase 3".
    2. PROJECT.md: update the "11 researched candidate packs (8 Tier-1, 3 Tier-2)" line to reflect 8 Tier-1 builds + 3 vetted-out (0 Tier-2 in v1.17.0).
    3. MILESTONES.md: update the "3 Tier-2 conditional licence" mention to the vetted-out/deferred outcome (0 Tier-2 packs in v1.17.0).
  </action>
  <verify>
    <automated>grep -c "target after v1.17.0: 56" .planning/STATE.md | grep -qv '^0$' && grep -c "59+" .planning/STATE.md | grep -q '^0$' && grep -c "3 Tier-2" .planning/PROJECT.md | grep -q '^0$' && grep -c "3 Tier-2" .planning/MILESTONES.md | grep -q '^0$' && echo PASS</automated>
  </verify>
  <done>STATE.md packs target reads 56; deviations record the two exclusions and the 00-051 deferral (never "resolved"); no stale 59+ reference; PROJECT.md and MILESTONES.md no longer imply 3 Tier-2 packs in v1.17.0. Committed.</done>
</task>

</tasks>

<claim_verification>
| claim | command | observed | status |
|---|---|---|---|
| Research rules IEEE 15288.2-2014 Excluded (purchase-only, not GET) | grep -n "EXCLUDED-leaning" 2-RESEARCH.md | :136 heading + GET terms at :143-146 | VERIFIED |
| Research rules ECSS Excluded per ECSS-P-00C §5.8 | grep -n "5.8" 2-RESEARCH.md | :159, :162-165 licence quotes | VERIFIED |
| Research flags 00-051 subject mismatch vs 00-056 | grep -n "00-056" 2-RESEARCH.md | :176-179 conflation warning | VERIFIED |
| Research prescribes exact SOURCE-VETTING.md extension rows | grep -n "How docs/SOURCE-VETTING.md should be extended" 2-RESEARCH.md | :213 section with 4-row list incl. DAU dedup rationale | VERIFIED |
| Excluded table exists in two-column format | grep -n "^| Source | Why excluded |" docs/SOURCE-VETTING.md | :69 | VERIFIED |
| ISO/IEC/IEEE row currently cites 15288, 42010, 12207 only | grep -n "e.g. 15288" docs/SOURCE-VETTING.md | :71 | VERIFIED |
| dau-se-guidebook pack exists in 48-pack baseline | ls packs/ \| grep -c "dau-se-guidebook" | 1 | VERIFIED |
| REQUIREMENTS T2-01/T2-02/REL-01/REL-02 wording as quoted | grep -n "T2-01\|REL-01" .planning/REQUIREMENTS.md | :39-41, :49-50 | VERIFIED |
| ROADMAP Phase 5 says "59+ packs" | grep -n "59+" .planning/ROADMAP.md | :60 | VERIFIED |
| STATE.md says "target after v1.17.0: 59+" | grep -n "59+" .planning/STATE.md | :33 | VERIFIED |
</claim_verification>

<threat_model>
## Trust Boundaries

Docs/planning-only phase; no runtime trust boundaries. Content boundary: licence statements quoted from vendor/agency pages are legal evidence — misquotation creates licence risk.

## STRIDE Threat Register

| Threat ID | Category | Component | Severity | Disposition | Mitigation Plan |
|-----------|----------|-----------|----------|-------------|-----------------|
| T-2-01 | Tampering | Licence-evidence quotes in SOURCE-VETTING.md | high | mitigate | Copy rationale verbatim from 2-RESEARCH.md (verified 2026-08-14); do not paraphrase legal terms; date each row |
| T-2-02 | Repudiation | Exclusion decisions (T2-01/T2-02) | medium | mitigate | Each strike/Out-of-Scope entry cites SOURCE-VETTING.md and the research date |
| T-2-03 | Information Disclosure | Source URLs for vetted/excluded candidates | low | mitigate | No URLs published in docs/SOURCE-VETTING.md (Link Policy: not in a pack or the docs); a pointer line names 2-RESEARCH.md as the sole URL evidence store; verify asserts `grep -c "http" docs/SOURCE-VETTING.md` = 0 |
</threat_model>

<verification>
- All four tasks' automated greps pass.
- Every one of the 11 candidates has a recorded outcome in SOURCE-VETTING.md: 8 Vetted (Tier 1), 3 ruled-out/deferred (IEEE 15288.2, ECSS, INCOSE-GWR + ISO-row extension, DAU dedup, Def Stan 00-051 UNVERIFIED note).
- Cross-artifact consistency: 56 appears in REQUIREMENTS, ROADMAP, STATE; no artifact still says 59+ or implies Tier-2 packs in v1.17.0.
- git log shows 4 independent commits, one per task.
</verification>

<success_criteria>
- Phase 2 success criteria 1-3 (ROADMAP) all satisfied by the recorded decisions, including the 00-051 build-or-exclude decision being *recorded* as deferred-excluded pending DSTAN registration.
- Phases 3-5 plans can be written against a stable, corrected 56-pack target with no Tier-2 build work.
</success_criteria>

<output>
Create `.planning/phases/2-source-vetting-ruled-out-register/2-01-SUMMARY.md` when done
</output>
