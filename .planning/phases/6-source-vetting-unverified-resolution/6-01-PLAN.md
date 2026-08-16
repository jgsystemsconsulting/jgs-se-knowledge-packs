---
phase: 6-source-vetting-unverified-resolution
plan: 01
type: execute
wave: 1
depends_on: []
files_modified:
  - docs/SOURCE-VETTING.md
  - .planning/REQUIREMENTS.md
  - .planning/ROADMAP.md
  - .planning/MILESTONES.md
  - .planning/STATE.md
autonomous: true
requirements: [VET-01, VET-02]
estimate:
  tokens: 45000
  raw_tokens: 22000
  tasks: 5
  confidence: med

must_haves:
  truths:
    - All 5 UNVERIFIED items have a definitive tier decision recorded in docs/SOURCE-VETTING.md with licence evidence and date stamps
    - AFOTEC Test Design Guide, DoD DAG, and CMU SEI appear in the Excluded table with dated rationale
    - GP-08 (NASA-HDBK-2203) is struck from v1.18 scope in REQUIREMENTS.md with the NPR 7150.2 + NASA-STD-8739.8 rescope note
    - ROADMAP Phase 7 criteria reference 7 packs (GP-08 out or explicitly conditional), and STATE.md notes reflect 63-pack target
    - docs/SOURCE-VETTING.md contains zero http/https URLs (Link Policy)
  artifacts:
    - docs/SOURCE-VETTING.md with a "Vetted candidates (v1.18.0)" section and three new Excluded rows
    - .planning/REQUIREMENTS.md v1.18 section updated (GP-08 descoped, GP-01/GP-03 build-model notes)
    - .planning/ROADMAP.md Phase 7 entry adjusted to 7 packs
    - .planning/STATE.md Deviations/Notes updated
  key_links:
    - SOURCE-VETTING vetted rows must point to .planning/phases/6-source-vetting-unverified-resolution/6-RESEARCH.md as the URL store (never inline URLs)
    - REQUIREMENTS GP rows must match the verdicts in 6-RESEARCH.md §5 summary table
---

<objective>
Record the Phase 6 vetting verdicts (6-RESEARCH.md is AUTHORITATIVE) into the persistent integrity surfaces: docs/SOURCE-VETTING.md (vetted + excluded), .planning/REQUIREMENTS.md (GP-08 descope, build-model notes), .planning/ROADMAP.md (Phase 7 = 7 packs), .planning/STATE.md (notes).

Purpose: Every v1.18 candidate must have a definitive tier decision before pack builds start (Phase 7 gate); dead/gated sources must be permanently excluded so they are never re-proposed.
Output: Updated docs/planning files only — no pack builds in this phase.
</objective>

<execution_context>
@$HOME/.zcode/gsd-core/workflows/execute-plan.md
@$HOME/.zcode/gsd-core/templates/summary.md
</execution_context>

<context>
@.planning/PROJECT.md
@.planning/ROADMAP.md
@.planning/STATE.md
@.planning/REQUIREMENTS.md
@docs/SOURCE-VETTING.md
@.planning/phases/6-source-vetting-unverified-resolution/6-RESEARCH.md
</context>

<claim_verification>
| claim | command | observed | status |
|---|---|---|---|
| 6-RESEARCH.md gives Tier-1-confirmed verdicts for 40051-2C, SP-7084, VV&A RPG, 881F + exclusions for AFOTEC/DAG/SEI + GP-08 descope | grep -n "Verdict\|DEFER" .planning/phases/6-source-vetting-unverified-resolution/6-RESEARCH.md | Verdicts at §1a-1e, §3a-3b, §4; §5 summary table lists all 11 rows | VERIFIED |
| docs/SOURCE-VETTING.md currently has a "Vetted candidates (v1.17.0)" section and an Excluded table with dated rows | grep -n "Vetted candidates (v1.17.0)\|Verified 2026-08-14" docs/SOURCE-VETTING.md | Section present; Excluded rows carry "(Verified 2026-08-14.)" date stamps (v1.17 Vetted rows are undated; dating Vetted rows is new in v1.18, required by must_haves) | VERIFIED |
| Link Policy: no source URLs in docs/ | grep -c "http" docs/SOURCE-VETTING.md | 0 http occurrences (17 U.S.C. § 105 is plain text, not a URL) | VERIFIED |
| REQUIREMENTS.md GP-08 row exists as stretch (line 87) | grep -n "GP-08" .planning/REQUIREMENTS.md | `- [ ] **GP-08** (stretch): nasa-sw-handbook — NASA-HDBK-2203 select chapters [13, 19, 32]` | VERIFIED |
| ROADMAP Phase 7 requirements list includes GP-08 and success criteria say "7–8 packs" | grep -n "GP-08\|7–8" .planning/ROADMAP.md | Line 94 Goal "7–8 public-domain packs"; line 96 Requirements include GP-08 | VERIFIED |
| STATE.md pack target says 63-64 and needs 63 (GP-08 out) | grep -n "63-64\|Packs shipped" .planning/STATE.md | "Packs shipped: 56 (target after v1.18.0: 63-64)" | VERIFIED |
| VV&A RPG verdict is chapter-wise build, not consolidated PDF | sed -n '/1c/,/1d/p' .planning/phases/6-source-vetting-unverified-resolution/6-RESEARCH.md | "Tier 1 CONFIRMED, but 'consolidated PDF' premise is DEAD (rescope)" | VERIFIED |
</claim_verification>

<tasks>

<task type="auto">
  <name>Task 1: Add "Vetted candidates (v1.18.0)" section to docs/SOURCE-VETTING.md</name>
  <files>docs/SOURCE-VETTING.md</files>
  <action>Edit-only (file carries an SPDX header — never rewrite the file wholesale; use scoped Edits). Insert a new "### Vetted candidates (v1.18.0)" section immediately after the existing "Vetted candidates (v1.17.0)" section, following the v1.17 section format: same table format (| Source | Tier | Licence evidence |) and prose conventions. Open with the same Link Policy pointer paragraph but pointing at .planning/phases/6-source-vetting-unverified-resolution/6-RESEARCH.md as the URL store. Add 8 rows — each row's Source cell includes its GP token so per-pack confirmation is greppable — per 6-RESEARCH.md §1, §2, and §5: (1) GP-07 / MIL-STD-40051-2C — Tier 1, 17 U.S.C. § 105, build caveat: Distribution Statement is a scanned image on the mirror copy, DIST-A must be visually confirmed on the cover at build time; (2) NASA SP-7084 — Tier 1 (VET-01 item, not a GP pack), NTRS metadata "Work of the US Gov. Public Use Permitted", prefer 1998 rev if mirror has text layer else NTRS 1990 canonical; (3) GP-01 / DoD VV&A RPG — Tier 1, chapter-wise build model (no consolidated PDF exists), per-chapter provenance in PACK.yaml, confirm DIST-A inside each chapter PDF used; (4) GP-05 / MIL-STD-881F — Tier 1, fetch via DLA ASSIST-QuickSearch (free account) or GovTribe attachment (everyspec has only 881E), DIST-A visual confirm at build, resolve exact revision date on the QuickSearch detail page; (5) GP-02 / FAA-STD-025 — Tier 1, rev E canonical (ROSAP full-text PDF) + rev F mirror, record chosen revision in PACK.yaml; (6) GP-03 / DOT&E T&E Enterprise Guidebook — Tier 1, target the Aug 2022 edition (8.02) from dote.osd.mil if a direct PDF is obtainable; fall back to the afacpo fixed-URL single-encoded mirror PDF (v3 June 2022) if direct download is unavailable; PACK.yaml records the edition actually built (8.02 or mirror v3-June) (URLs live only in 6-RESEARCH.md §2b); (7) GP-04 / DAFMAN 63-119 — Tier 1, in-document "RELEASABILITY: There are no releasability restrictions on this publication", title corrected to Mission-Oriented Test Readiness Certification; (8) GP-06 / federal-bca (dual-source: OMB Circular A-94 + US Army CBA Guide) — Tier 1, both are U.S. Government works, public domain per 17 U.S.C. § 105 (licence basis per 6-RESEARCH.md §2 spot-check scope and capability-gap-report shortlist item 5); record per-source provenance for both documents in PACK.yaml. Rows carry "(Verified 2026-08-14.)" date stamps — dated Vetted rows are a deliberate new v1.18 convention required by must_haves (the v1.17 Vetted rows are undated; only the Excluded table carried stamps). Include a short closing note recording the GP-08 deferral: NASA-HDBK-2203 standards-page PDF is a placeholder; content is swehb.nasa.gov wiki HTML only — deferred out of v1.18, see Task 3. Do NOT include any http/https URLs anywhere in the added text.</action>
  <verify>
    <automated>! grep -n "http" docs/SOURCE-VETTING.md && test "$(grep -c 'Verified 2026-08-14' docs/SOURCE-VETTING.md)" -ge 14 && grep -n "Vetted candidates (v1.18.0)" docs/SOURCE-VETTING.md && grep -n "6-RESEARCH.md" docs/SOURCE-VETTING.md</automated>
  </verify>
  <done>Vetted candidates (v1.18.0) section exists with 8 dated rows (GP-01..GP-07 tokens each present, incl. GP-06 federal-bca dual-source row) + GP-08 deferral note; zero http strings in the file; pointers to 6-RESEARCH.md, no inline URLs.</done>
</task>

<task type="auto">
  <name>Task 2: Add AFOTEC, DoD DAG, CMU SEI Excluded rows to docs/SOURCE-VETTING.md</name>
  <files>docs/SOURCE-VETTING.md</files>
  <action>Edit-only, scoped Edit appending three rows to the existing Excluded markdown table (after the DAU/WARU row), following the "| **Source** | Why excluded |" format with "(Verified 2026-08-14.)" date stamps, per 6-RESEARCH.md §1e, §3a, §3b: (1) **AFOTEC Test Design Guide** — DTIC serving maintenance shells on citation and PDF endpoints so no in-copy licence check possible; only DTIC hit is the 1989 edition (AD-A205 489), ~37 years stale vs live DAFMAN 63-119 (2021) and DOT&E Enterprise Guidebook (2022); revisit only if AFOTEC publishes a modern public edition. (2) **DoD DAG (Defense Acquisition Guidebook)** — retired per DAU AAF guidebooks page ("has been retired and replaced"); AFCAPO retirement notice 2022-08-15; dead canonical URLs, Wayback-only text, provenance/versioning risk; AAF guidebooks remain the Tier 1 substitute. (3) **CMU SEI technical reports** — © Carnegie Mellon University; IP page grants government-purpose reproduction only with notice retention; non-government reuse routed through permission@sei.cmu.edu; DIST-A on some SEI reports governs DoD distribution, not CMU copyright, and creates no Tier 1/2 grant; excluded absent written CMU/SEI permission. No http/https URLs anywhere in the added rows; the bare email address permission@sei.cmu.edu (no mailto: prefix) is permitted and retained as the routing path for reuse requests.</action>
  <verify>
    <automated>grep -n "AFOTEC Test Design Guide" docs/SOURCE-VETTING.md && grep -n "Defense Acquisition Guidebook" docs/SOURCE-VETTING.md && grep -n "CMU SEI" docs/SOURCE-VETTING.md && ! grep -n "http" docs/SOURCE-VETTING.md && test "$(grep -c 'Verified 2026-08-14' docs/SOURCE-VETTING.md)" -ge 17</automated>
  </verify>
  <done>Three new dated Excluded rows present; file still URL-free.</done>
</task>

<task type="auto">
  <name>Task 3: Update REQUIREMENTS.md — GP-08 descope + GP-01/GP-03 build notes</name>
  <files>.planning/REQUIREMENTS.md</files>
  <action>Edit-only. Three scoped changes in the v1.18.0 section: (1) GP-08 — change the checkbox line to struck-through (`- [ ] ~~**GP-08** (stretch): ...~~ — DESCOPED 2026-08-14: NASA-HDBK-2203 has no consolidated PDF (standards-page PDF is a placeholder; content is swehb.nasa.gov wiki HTML); see 6-RESEARCH.md §4`) and add a row to the v1.18 "Out of Scope" table: `nasa-sw-handbook (GP-08)` | No consolidated PDF edition exists; per-SWE wiki-harvest build is out of v1.18 scope. Alternative: rescope to NPR 7150.2 + NASA-STD-8739.8 (both downloadable PDFs; 8739.8 cover states APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED) as v1.19 candidates or a Phase 7 stretch decision. (2) GP-01 — append note: "(build model: VV&A RPG has NO consolidated PDF — chapter-wise build with per-chapter provenance in PACK.yaml; per 6-RESEARCH.md §1c)". (3) GP-03 — append note: "(target the Aug 2022 edition 8.02 from dote.osd.mil; fall back to the afacpo fixed single-encoded mirror PDF if direct download unavailable; PACK.yaml records the edition actually built; the gap-report mirror URL was double-encoded and is fixed in 6-RESEARCH.md §2b)". (4) GP-04 — update the row description to "DAF Mission-Oriented Test Readiness Certification manual (DAFMAN 63-119)" and append note: "(title correction: MOTRC compliance manual, 15 Apr 2021 — per 6-RESEARCH.md §2c)". Also append to VET-01/VET-02 lines nothing — those stay open until Phase 6 verification; do not check them here.</action>
  <verify>
    <automated>grep -n "GP-08" .planning/REQUIREMENTS.md && grep -n "NPR 7150.2" .planning/REQUIREMENTS.md && grep -n "chapter-wise" .planning/REQUIREMENTS.md && grep -n "8.02" .planning/REQUIREMENTS.md && grep -n "Mission-Oriented Test Readiness Certification" .planning/REQUIREMENTS.md</automated>
  </verify>
  <done>GP-08 struck + Out-of-Scope row with NPR 7150.2 / NASA-STD-8739.8 alternatives; GP-01 chapter-wise note; GP-03 8.02-conditional note; GP-04 description corrected to DAF Mission-Oriented Test Readiness Certification manual (DAFMAN 63-119); VET rows untouched.</done>
</task>

<task type="auto">
  <name>Task 4: Update ROADMAP.md Phase 7 + STATE.md notes</name>
  <files>.planning/ROADMAP.md, .planning/MILESTONES.md, .planning/STATE.md</files>
  <action>Edit-only, scoped Edits. ROADMAP.md Phase 7 section: change Goal from "7–8 public-domain packs" to "7 public-domain packs (GP-01..GP-07; GP-08 descoped — see REQUIREMENTS Out of Scope; conditional rescope to NPR 7150.2 + NASA-STD-8739.8 only as a Phase 7 stretch decision)"; change Requirements line from [GP-01..GP-08] to [GP-01, GP-02, GP-03, GP-04, GP-05, GP-06, GP-07] with a parenthetical "(GP-08 descoped 2026-08-14, no consolidated NASA-HDBK-2203 PDF)"; also update the ROADMAP v1.18 phase-list overview bullet (line 77, "Build GP-01..GP-08 packs via jgs-reference-skill pipeline") to "Build GP-01..GP-07 packs (GP-08 descoped) via jgs-reference-skill pipeline" so the overview matches the details; leave Success Criteria items otherwise intact but adjust criterion 1 wording only if it references 8 packs (it does not — it references pack conformance, so no change needed there). MILESTONES.md line 18: change "7-8 Tier-1 packs" to "7 Tier-1 packs" so the milestone surface matches the descope. STATE.md: update "Packs shipped: 56 (target after v1.18.0: 63-64)" to "56 (target after v1.18.0: 63 — 7 GP packs, GP-08 descoped)"; append a Deviations/Notes line: "Phase 6 (2026-08-14): 5 UNVERIFIED items resolved (4 Tier 1 confirmed, AFOTEC excluded); DoD DAG + CMU SEI exclusions confirmed; VV&A RPG rescoped to chapter-wise build; DOT&E URL fixed to single-encoded; GP-08 descoped — verdicts in 6-RESEARCH.md". Do not touch STATE.md frontmatter progress fields (execute workflow handles them).</action>
  <verify>
    <automated>grep -n "GP-08 descoped" .planning/ROADMAP.md .planning/STATE.md && grep -n "63 — 7 GP packs" .planning/STATE.md && grep -n "7 Tier-1 packs" .planning/MILESTONES.md && test "$(grep -c 'GP-01..GP-08' .planning/ROADMAP.md)" = "0"</automated>
  </verify>
  <done>Phase 7 goal/requirements reference 7 packs with GP-08 descope rationale; ROADMAP overview bullet reads GP-01..GP-07; MILESTONES.md reads 7 Tier-1 packs; STATE pack target reads 63; deviation note records all Phase 6 verdicts.</done>
</task>

<task type="auto">
  <name>Task 5: Consistency verification sweep</name>
  <files>docs/SOURCE-VETTING.md, .planning/REQUIREMENTS.md, .planning/ROADMAP.md, .planning/STATE.md</files>
  <action>Read-only sweep of all five edited files. Check: (1) no http/https in docs/SOURCE-VETTING.md (grep -c, expect 0); (2) date-stamp count equals pre-phase count (7) + 11 new (8 vetted rows incl. GP-06 + 3 excluded rows, all "Verified 2026-08-14" = 18 total); (3) pack-count arithmetic consistent everywhere: 56 shipped + 7 GP = 63, no surface still says 64, "7-8"/"7–8", or "GP-01..GP-08" (ROADMAP overview bullet and MILESTONES.md updated by Task 4); (4) every verdict in the new SOURCE-VETTING rows traces to a 6-RESEARCH.md § (cite section numbers in row text where natural, as done for the v1.17 section's T2 references); (5) REQUIREMENTS GP-01..GP-07 rows still unchecked and unmodified except the three notes (GP-01, GP-03, GP-04); (6) ROADMAP Phase 6 SC wording "Each GP pack candidate confirmed or dropped; stretch items (GP-08) decided" is satisfied by artifacts: GP-01..GP-07 each confirmed in SOURCE-VETTING (including GP-06 federal-bca row from Task 1), GP-08 dropped in REQUIREMENTS — verify each GP token individually (see automated gate). Fix any drift found with scoped Edits.</action>
  <verify>
    <automated>test "$(grep -c 'http' docs/SOURCE-VETTING.md)" = "0" && test "$(grep -c 'Verified 2026-08-14' docs/SOURCE-VETTING.md)" -ge 18 && for gp in GP-01 GP-02 GP-03 GP-04 GP-05 GP-06 GP-07; do grep -q "$gp" docs/SOURCE-VETTING.md || exit 1; done && test "$(grep -c '63-64' .planning/STATE.md)" = "0" && test "$(grep -c '7-8' .planning/MILESTONES.md)" = "0" && test "$(grep -c '7–8' .planning/ROADMAP.md)" = "0" && test "$(grep -c 'GP-01..GP-08' .planning/ROADMAP.md)" = "0" && test "$(git diff --name-only | sort)" = "$(printf '.planning/MILESTONES.md\n.planning/REQUIREMENTS.md\n.planning/ROADMAP.md\n.planning/STATE.md\ndocs/SOURCE-VETTING.md')"</automated>
  </verify>
  <done>Zero URLs in SOURCE-VETTING; 11 new dated rows (total 18); GP-01..GP-07 tokens each present in SOURCE-VETTING; 63-pack count consistent, no "7-8"/"7–8"/"GP-01..GP-08"/"63-64" leftovers; git diff --name-only shows exactly the 5 expected files; every verdict traceable to 6-RESEARCH.md.</done>
</task>

</tasks>

<threat_model>
## Trust Boundaries

| Boundary | Description |
|----------|-------------|
| research-store → docs | Verdict evidence (URLs, licence quotes) crosses from .planning (private) into docs/ (published) |
| mirror-hosted sources | Third-party mirrors (everyspec, GovTribe, afacpo) host copies whose provenance/DIST-A status must be confirmed in-copy at build |

## STRIDE Threat Register

| Threat ID | Category | Component | Severity | Disposition | Mitigation Plan |
|-----------|----------|-----------|----------|-------------|-----------------|
| T-6-01 | Information Disclosure | docs/SOURCE-VETTING.md | medium | mitigate | Link Policy grep gate (Task 5): zero http strings; URLs live only in 6-RESEARCH.md |
| T-6-02 | Repudiation | SOURCE-VETTING verdicts | low | mitigate | Every row carries a "(Verified 2026-08-14.)" date stamp and traces to a 6-RESEARCH.md § |
| T-6-03 | Tampering | mirror-fetched PDFs (Phase 7 builds) | high | mitigate | Recorded build caveats: DIST-A visual confirm at build (40051-2C, 881F), per-chapter in-PDF statement check (VV&A) — enforcement lands in Phase 7 pack validation |
</threat_model>

<verification>
- All 5 UNVERIFIED items have definitive decisions: 4 Tier 1 confirmed + 1 Excluded (AFOTEC), recorded in docs/SOURCE-VETTING.md with evidence and date stamps (VET-01)
- DoD DAG, CMU SEI, AFOTEC all in the Excluded table with dated rationale (VET-02)
- GP-08 decided: descoped with documented alternatives (NPR 7150.2 + NASA-STD-8739.8)
- ROADMAP Phase 7 and STATE.md consistent at 7 packs / 63 total
- Link Policy holds: no source URLs in docs/
</verification>

<success_criteria>
- docs/SOURCE-VETTING.md contains "Vetted candidates (v1.18.0)" (8 rows, GP-01..GP-07 all confirmed incl. GP-06 federal-bca) and 3 new Excluded rows, all dated, URL-free
- REQUIREMENTS.md: GP-08 struck + Out-of-Scope row; GP-01 chapter-wise note; GP-03 8.02-conditional note; GP-04 MOTRC title correction
- ROADMAP.md Phase 7 + overview bullet: 7 packs (GP-01..GP-07), GP-08 descope rationale; MILESTONES.md: 7 Tier-1 packs; STATE.md: 63 target + deviation note
- git diff --name-only shows exactly the 5 expected files; no pack builds started
</success_criteria>

<output>
Create .planning/phases/6-source-vetting-unverified-resolution/6-01-SUMMARY.md when done
</output>
