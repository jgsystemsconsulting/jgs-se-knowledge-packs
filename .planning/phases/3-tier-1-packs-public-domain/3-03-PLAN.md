---
phase: 3-tier-1-packs-public-domain
plan: 03
type: execute
wave: 2
depends_on: [3-01, 3-02]
files_modified:
  - packs/nasa-ms-7009/**
  - packs/doe-413-3b/**
  - packs/catalog.json
  - SKILLS.md
  - docs/packs.html
  - NOTICE
autonomous: true
requirements: [T1-05, T1-06]
estimate:
  tokens: 120000
  raw_tokens: 60000
  tasks: 3
  confidence: low

must_haves:
  truths:
    - "packs/nasa-ms-7009 built from BOTH PDFs (STD-7009B + HDBK-7009B): two extractions, one pack; source_pages = sum"
    - "packs/doe-413-3b built from the consolidated Chg 7 PDF (old deep link 404s); in-PDF third-party copyright check recorded"
    - "Both packs pass tooling/validate_pack.py with complete PACK.yaml provenance; check_overlap exits 0"
    - "catalog.json contains all 8 new Tier-1 pack entries (license_tier 1, status live); `updated` bumped"
    - "SKILLS.md has 8 new table rows with Public Domain (US Gov) column; header count bumped"
    - "docs/packs.html regenerated via tooling/gen_packs_page.py (never hand-edited)"
    - "NOTICE has one [pack: <slug>] block per new pack"
    - "python tooling/check_release.py exits PASS"
  artifacts:
    - packs/nasa-ms-7009/SKILL.md, PACK.yaml, LICENSE, chapters/
    - packs/doe-413-3b/SKILL.md, PACK.yaml, LICENSE, chapters/
    - updated packs/catalog.json, SKILLS.md, docs/packs.html, NOTICE
  key_links:
    - "Chapter Index links resolve in both new packs"
    - "catalog.json pack count consistent with packs/ directories (check_release.py verifies, incl. packs.html freshness)"
---

<objective>
Plan C (Batch C of 3-RESEARCH.md §5): build the two multi-document packs —
nasa-ms-7009 (T1-05, STD-7009B + HDBK-7009B two PDFs → one pack) and doe-413-3b
(T1-06, consolidated O 413.3B Chg 7 PDF) — then run the consolidated registration
sweep for ALL 8 Tier-1 packs (catalog.json, SKILLS.md, gen_packs_page.py, NOTICE,
check_release.py).

Registration consolidation decision (laziest safe option): registration runs ONCE
here, at the end of Plan C, covering all 8 packs. Rationale: gen_packs_page.py,
check_release.py, and the catalog/SKILLS.md/NOTICE edits are repo-global — running
them in every plan would triple repeated edits and merge conflicts on the same four
files for zero benefit. Plans A/B commit only their packs/ directories; this plan
depends_on them so the single sweep sees all 8. Contribution flow ("one pack per
PR") stays satisfiable — commits remain per-pack; registration is one closing commit.
</objective>

<execution_context>
@$HOME/.zcode/gsd-core/workflows/execute-plan.md
@$HOME/.zcode/gsd-core/templates/summary.md
</execution_context>

<context>
@.planning/PROJECT.md
@.planning/ROADMAP.md
@.planning/phases/3-tier-1-packs-public-domain/3-RESEARCH.md
@.planning/phases/3-tier-1-packs-public-domain/3-01-PLAN.md
@.planning/phases/3-tier-1-packs-public-domain/3-02-PLAN.md
@.planning/phases/2-source-vetting-ruled-out-register/2-RESEARCH.md
@docs/PACK-SPEC.md
</context>

<claim_verification>
| claim | command | observed | status |
|---|---|---|---|
| nasa-ms-7009 = STD (~30pp) + HDBK (100+pp), both PDFs exist on standards.nasa.gov | 3-RESEARCH.md §1 row T1-05 | STD-7009B approved 2024-03-05 + HDBK-7009B 2026-02-03 | VERIFIED |
| standards.nasa.gov PDFs behind tmp-prefixed paths — download promptly | 3-RESEARCH.md §6 risk 7 | stated | VERIFIED |
| doe-413-3b old deep link 404s; use consolidated Chg 7 PDF from directives library entry | 3-RESEARCH.md §1 row T1-06 | confirmed in Phase 2 | VERIFIED |
| registration steps (catalog hand-edit, SKILLS.md hand-edit, gen_packs_page.py regen, NOTICE blocks, check_release PASS) | 3-RESEARCH.md §4 | authoritative; gen_skills_index.py absent, hand-edit SKILLS.md keeping disclaimer | VERIFIED |
| Phase 5 gate basis: 54 catalog / 56 directory packs after +8 | 3-RESEARCH.md §4 step 5 | matches ROADMAP Phase 5 SC1 | VERIFIED |
</claim_verification>

<tasks>

<task type="auto">
  <name>Task 1: Build packs/nasa-ms-7009 (T1-05) — two PDFs, one pack</name>
  <files>packs/nasa-ms-7009/**</files>
  <action>
Pipeline per 3-RESEARCH.md §2, build-sheet row T1-05, with the multi-document
variation (§6 risk 7):
1. Download BOTH PDFs from standards.nasa.gov promptly (tmp-prefixed `system/files/tmp/`
   paths may be re-generated on publish): NASA-STD-7009B and NASA-HDBK-7009B into
   sources/nasa-ms-7009/.
2. VET: title "NASA Standard for Models and Simulations (NASA-STD-7009B with
   NASA-HDBK-7009B)", publisher NASA, default licence string
   `Public Domain (US Government work, 17 U.S.C. § 105)` — "nasa" is a US_GOV signal,
   so no P3-PRE-1 concern.
3. EXTRACT EACH PDF separately (two runs, two book_skill_work dirs; capture both
   %TEMP% paths). metadata.json absent for multi-PDF sums → source_pages = STD +
   HDBK page counts summed; record both.
4. OUTLINE each; build ONE pack. Primary chapter spine = the STD's 43 mandatory
   requirements grouped into credibility facets (verification/validation/uncertainty);
   HDBK slices become depth chapters. Target 6-8 chapters per build sheet.
5. SCAFFOLD version "STD-7009B approved 2024-03-05 + HDBK-7009B (2026-02-03)".
6. GENERATE per docs/PACK-SPEC.md (same structure as Plan A Task 1; slice reads via
   each outline's offsets). PACK.yaml notes state two-source build and summed pages.
   LICENSE carries the statute text.
7. VALIDATE → SCAN (disposition findings) → OVERLAP against BOTH full_text.txt files
   (run check_overlap twice, once per source; both must exit 0).
8. One commit touching only packs/nasa-ms-7009.
REF = C:/Users/gower/OneDrive/Documents/GitHub/jgs-reference-skill; `python`, not python3.
  </action>
  <verify>
    <automated>python tooling/validate_pack.py packs/nasa-ms-7009 && grep -c "43" packs/nasa-ms-7009/SKILL.md</automated>
  </verify>
  <done>validate_pack.py passes; PACK.yaml source_pages = summed STD+HDBK actuals with note; check_overlap exits 0 against both sources; one commit touching only packs/nasa-ms-7009.</done>
</task>

<task type="auto">
  <name>Task 2: Build packs/doe-413-3b (T1-06) — consolidated order PDF</name>
  <files>packs/doe-413-3b/**</files>
  <action>
Pipeline per 3-RESEARCH.md §2, build-sheet row T1-06:
title "Program and Project Management for the Acquisition of Capital Assets (DOE O
413.3B, Chg 7)", publisher "US Department of Energy" (matches `"department of "`
signal — no P3-PRE-1 concern), version "O 413.3B Chg 7 (LtdChg), 2023-06-21",
default licence string. Download the CONSOLIDATED Chg 7 PDF via the energy.gov
directives-library entry (2-RESEARCH.md §6) — the old deep link 404s. FIRST step
after extract: read the extracted text for third-party copyright notices inside the
PDF (same in-PDF confirmation as doe-sem); halt and surface if found. ~100+ pp,
confirm actual from metadata.json. 5-7 chapters: CD-0..CD-5 milestone chapters,
acquisition planning, budget/cost, risk, emergency procurement exceptions. Same
gates (validate → scan disposition → overlap exit 0), PACK.yaml provenance complete,
one commit touching only packs/doe-413-3b.
  </action>
  <verify>
    <automated>python tooling/validate_pack.py packs/doe-413-3b && python "$REF/tools/check_overlap.py" --source "$TMP413/book_skill_work/full_text.txt" --pack packs/doe-413-3b</automated>
  </verify>
  <done>validate_pack.py passes; PACK.yaml source_pages = actual; in-PDF third-party-copyright check result recorded; check_overlap exits 0; one commit touching only packs/doe-413-3b.</done>
</task>

<task type="auto">
  <name>Task 3: Registration sweep for all 8 Tier-1 packs + check_release</name>
  <files>packs/catalog.json, SKILLS.md, docs/packs.html, NOTICE</files>
  <action>
Execute 3-RESEARCH.md §4 once, covering all 8 packs from Plans A/B/C:
1. catalog.json: add 8 pack objects to `packs[]` mirroring the existing shape (slug,
   title, publisher, source_version, license, license_tier: 1, commercial_use: true,
   chapters, status "live"); bump `updated`. Hand-edit is the documented route.
2. SKILLS.md: add 8 table rows `| [slug](packs/<slug>/SKILL.md) | Public Domain (US
   Gov) | <description incl. scope limits> |`; bump the header count. Hand-edit
   (gen_skills_index.py does not exist in tooling/); keep the generated-file
   disclaimer intact.
3. docs/packs.html: DO NOT hand-edit — run `python tooling/gen_packs_page.py`.
4. NOTICE: add one `[pack: <slug>]` attribution block per pack (Source / Author /
   Licence / Changes / Terms), mirroring existing Public Domain (US Government work)
   entries.
5. Final sweep: `python tooling/check_release.py` → PASS. Expected catalog basis
   after +8: 54 packs (48 + 8 new − 2 signposts) / 56 directory basis — this is the
   Phase 5 gate basis; if the counts disagree, fix catalog/directory inconsistency
   before committing.
6. No source URLs anywhere in catalog/packs (no-source-link policy). One closing
   commit (`chore(registration): register 8 Tier-1 packs (catalog, SKILLS.md, packs.html, NOTICE)`).
  </action>
  <verify>
    <automated>python tooling/check_release.py && python -c "import json;c=json.load(open('packs/catalog.json'));print(len([p for p in c['packs'] if p.get('license_tier')==1]))"</automated>
  </verify>
  <done>check_release.py exits PASS; catalog.json contains all 8 new tier-1 entries; SKILLS.md has 8 new rows with bumped count; packs.html regenerated; NOTICE has 8 new blocks; one registration commit.</done>
</task>

</tasks>

<threat_model>
## Trust Boundaries

| Boundary | Description |
|----------|-------------|
| standards.nasa.gov tmp paths → sources/ | tmp-prefixed PDF paths may vanish; download promptly |
| source text → pack content | verbatim-run boundary (check_overlap, both sources for nasa) |
| catalog ↔ filesystem | registration consistency boundary (check_release.py) |

## STRIDE Threat Register

| Threat ID | Category | Component | Severity | Disposition | Mitigation Plan |
|-----------|----------|-----------|----------|-------------|-----------------|
| T-3C-01 | Tampering (provenance) | nasa-ms-7009 dual-source pack | medium | mitigate | PACK.yaml notes record two-source build; source_pages = summed actuals |
| T-3C-02 | Repudiation | registration sweep | medium | mitigate | check_release.py PASS gate (catalog/packs.html consistency, RR-B-30) |
| T-3C-03 | Information disclosure | sources/, full_text.txt | high | mitigate | gitignored; commit-stat checks per task |
| T-3C-04 | IP theft (verbatim copying) | chapters/ | high | mitigate | check_overlap exit-3 gate against every source (twice for nasa-ms-7009) |
</threat_model>

<verification>
All 8 packs: `python tooling/validate_pack.py packs/<slug>` passes. Registration: check_release.py PASS with 54/56 pack basis. `git log` shows per-pack commits plus one registration commit; no sources/ paths in any commit.
</verification>

<success_criteria>
All 8 Tier-1 packs built, validated, provenance-complete per ROADMAP Phase 3 SC1-SC3; registration surface synchronized; check_release.py PASS — Phase 3 complete, Phase 5 gate basis established.
</success_criteria>

<output>
Create `.planning/phases/3-tier-1-packs-public-domain/3-03-SUMMARY.md` when done
</output>
