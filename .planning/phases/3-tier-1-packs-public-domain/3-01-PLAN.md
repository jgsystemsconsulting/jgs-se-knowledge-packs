---
phase: 3-tier-1-packs-public-domain
plan: 01
type: execute
wave: 1
depends_on: []
files_modified:
  - packs/nist-800-171/**
  - packs/nist-800-61/**
  - packs/cisa-cpg/**
  - packs/doe-sem/**
autonomous: true
requirements: [T1-01, T1-02, T1-07, T1-08]
estimate:
  tokens: 140000
  raw_tokens: 70000
  tasks: 4
  confidence: low

must_haves:
  truths:
    - "packs/nist-800-171 passes tooling/validate_pack.py with complete PACK.yaml provenance (tier 1, licence, pages, chapters, built_on)"
    - "packs/nist-800-61 passes tooling/validate_pack.py with complete PACK.yaml provenance"
    - "packs/cisa-cpg passes tooling/validate_pack.py; vet_source.py verdict is tier 1 (P3-PRE-1 statute-bearing licence string)"
    - "packs/doe-sem passes tooling/validate_pack.py; in-PDF third-party copyright check recorded before generation"
    - "check_overlap.py exits 0 (not 3) for every pack — no verbatim runs"
    - "scan_generated_skill.py findings reviewed and dispositioned per pack"
    - "No source PDF or full_text.txt is committed — downloads stay under gitignored sources/<slug>/"
  artifacts:
    - packs/nist-800-171/SKILL.md, PACK.yaml, LICENSE, chapters/
    - packs/nist-800-61/SKILL.md, PACK.yaml, LICENSE, chapters/
    - packs/cisa-cpg/SKILL.md, PACK.yaml, LICENSE, chapters/
    - packs/doe-sem/SKILL.md, PACK.yaml, LICENSE, chapters/
  key_links:
    - "Every chapters/ link in each SKILL.md Chapter Index resolves to a real file (CI-checked)"
    - "PACK.yaml source_pages matches metadata.json page count from extraction"
---

<objective>
Plan A (Batch A of 3-RESEARCH.md §5): build the 4 born-digital Tier-1 packs —
nist-800-171 (T1-01), nist-800-61 (T1-02), cisa-cpg (T1-07), doe-sem (T1-08) —
via the shared deterministic pipeline in 3-RESEARCH.md §2. This plan also proves
the two Phase 3 preconditions: P3-PRE-1 (cisa statute-bearing licence string,
mandatory) and P3-PRE-2 (accepted gap, record only — no Phase 3 build depends on it).

Purpose: ship the lowest-risk half of the Tier-1 library, proving the pipeline
end-to-end before Batches B/C hit mirror/OCR/multi-doc risks.
Output: 4 validated packs under packs/, one commit per pack. Registration
(catalog.json / SKILLS.md / gen_packs_page.py / NOTICE / check_release.py) is
deliberately NOT done here — it is consolidated once in 3-03-PLAN.md.
</objective>

<execution_context>
@$HOME/.zcode/gsd-core/workflows/execute-plan.md
@$HOME/.zcode/gsd-core/templates/summary.md
</execution_context>

<context>
@.planning/PROJECT.md
@.planning/ROADMAP.md
@.planning/phases/3-tier-1-packs-public-domain/3-RESEARCH.md
@.planning/phases/2-source-vetting-ruled-out-register/2-GAP_ANALYSIS.md
@docs/PACK-SPEC.md
</context>

<claim_verification>
| claim | command | observed | status |
|---|---|---|---|
| sources/ is gitignored (never commit PDFs/full text) | grep -n "Staged SOURCE material" .gitignore | 3-RESEARCH.md:14-17 confirms | VERIFIED (via 3-RESEARCH.md §Key confirmations) |
| cisa absent from vet_source.py US_GOV signals; PD licence strings classify Tier 1 | 2-GAP_ANALYSIS.md:53 + 3-RESEARCH.md §Key confirmations | P3-PRE-1 confirmed against code | VERIFIED |
| nvlpubs DOI-stable NIST PDF URL pattern | 3-RESEARCH.md:219-221 | `https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-171r3.pdf` | VERIFIED |
| doe-sem URL live, application/pdf | 3-RESEARCH.md:52 | confirmed in Phase 2 | VERIFIED |
| pipeline command order (vet → extract → outline → scaffold → generate → validate → scan → overlap) | 3-RESEARCH.md §2 | authoritative | VERIFIED |
</claim_verification>

<tasks>

<task type="auto">
  <name>Task 1: Build packs/nist-800-171 (T1-01) — full pipeline reference run</name>
  <files>packs/nist-800-171/**</files>
  <action>
Execute the 3-RESEARCH.md §2 pipeline for slug `nist-800-171` end-to-end; this run is
the reference — Tasks 2-4 repeat it with their build-sheet parameters.
1. `mkdir -p sources/nist-800-171`; download the PDF from the DOI-stable nvlpubs URL
   (3-RESEARCH.md §6 risk 4: do NOT scrape the csrc pubs page).
2. VET: `python "$REF/tools/vet_source.py" --title "Protecting Controlled Unclassified Information in Nonfederal Systems and Organizations (NIST SP 800-171 Rev. 3)" --publisher "NIST" --license "Public Domain (US Government work, 17 U.S.C. § 105)"`. Expect tier 1, exit 0; a third-party-quote advisory warning is expected for NIST, not a blocker.
3. EXTRACT: `python "$REF/scripts/extract.py" sources/nist-800-171/*.pdf --mode technical --install-missing ask`. Capture the printed %TEMP% book_skill_work path; read pages from metadata.json.
4. OUTLINE: outline.py → sources/nist-800-171/outline.json (stays gitignored).
5. SCAFFOLD: build_pack.py with slug/title/publisher/version "Rev. 3, final 2024-05-14 (DOI 10.6028/NIST.SP.800-171r3)"/default licence string, --out-dir packs.
6. GENERATE per docs/PACK-SPEC.md: 6-8 chapters grouping the 3.1-3.14 control families (build-sheet guidance, 3-RESEARCH.md §1 row T1-01); read full_text.txt only via outline start_char/end_char slices, never whole (>50k-token rule). Each chapter: Core Idea / Frameworks Introduced / Key Concepts / Mental Models / Anti-patterns / Key Takeaways / Connects To. Then glossary.md, patterns.md, cheatsheet.md, SKILL.md (frontmatter + How to Use + Core Frameworks + Chapter Index + Topic Index + Scope & Limits, body < ~4,000 tokens). Fill PACK.yaml TODOs (source_pages from metadata.json, chapters, built_on, notes) and LICENSE with the statute text. Synthesize — no long verbatim passages; no source URLs anywhere in pack files.
7. VALIDATE + SCAN + OVERLAP: `python tooling/validate_pack.py packs/nist-800-171`; `python "$REF/tools/scan_generated_skill.py" packs/nist-800-171` (review findings, record disposition in PACK.yaml notes); `python "$REF/tools/check_overlap.py" --source "$TMP/book_skill_work/full_text.txt" --pack packs/nist-800-171` — exit 3 must be fixed before commit. Bonus: pack_eval.py.
8. Commit packs/nist-800-171 only (`feat(packs): add nist-800-171 (Tier 1)`). Verify `git status` shows nothing from sources/ staged.
REF = C:/Users/gower/OneDrive/Documents/GitHub/jgs-reference-skill. Use `python` (not python3).
  </action>
  <verify>
    <automated>python tooling/validate_pack.py packs/nist-800-171 && git show --stat HEAD | grep -c "packs/nist-800-171" && git show --stat HEAD | grep -v -c "sources/" </automated>
  </verify>
  <done>validate_pack.py passes; check_overlap.py exits 0; PACK.yaml has license_tier 1, licence string, source_pages (actual from metadata.json), chapters count, built_on; scan findings dispositioned; one commit touching only packs/nist-800-171.</done>
</task>

<task type="auto">
  <name>Task 2: Build packs/nist-800-61 (T1-02)</name>
  <files>packs/nist-800-61/**</files>
  <action>
Repeat the Task 1 pipeline with build-sheet row T1-02 (3-RESEARCH.md §1):
title "Incident Response Recommendations and Considerations for Cybersecurity Risk Management (NIST SP 800-61 Rev. 3)", publisher NIST, version "Rev. 3, final 2025-04-03 (DOI 10.6028/NIST.SP.800-61r3)", default licence string, nvlpubs DOI-stable URL (`NIST.SP.800-61r3.pdf` same pattern). 5-7 chapters: IR lifecycle phases, communications, training, coordination, lessons learned. Same gates, same one-commit rule.
  </action>
  <verify>
    <automated>python tooling/validate_pack.py packs/nist-800-61 && python "$REF/tools/check_overlap.py" --source "$TMP800_61/book_skill_work/full_text.txt" --pack packs/nist-800-61</automated>
  </verify>
  <done>Same done-criteria as Task 1 for nist-800-61; ~68 pp confirmed in PACK.yaml source_pages.</done>
</task>

<task type="auto">
  <name>Task 3: Build packs/cisa-cpg (T1-07) — P3-PRE-1 mandatory handling</name>
  <files>packs/cisa-cpg/**</files>
  <action>
Repeat the Task 1 pipeline with build-sheet row T1-07 (3-RESEARCH.md §1):
title "Cross-Sector Cybersecurity Performance Goals 2.0 (CISA CPG 2.0)", publisher CISA, version "CPG 2.0 (2024-25 refresh, aligned to NIST CSF 2.0 incl. GOVERN)".
**P3-PRE-1 (mandatory):** the vet AND build_pack `--license` argument MUST be exactly
`Public Domain (US Government work, 17 U.S.C. § 105)` — publisher "CISA" hits no
US_GOV signal, so only the statute-bearing string classifies Tier 1. Never pass a
bare "CISA performance goals" style licence. Expect tier 1, exit 0.
Download both the main report and the controls-list PDF from the 2-RESEARCH.md §7
cisa.gov publications paths into sources/cisa-cpg/; extract each, sum pages for
PACK.yaml. 4-6 chapters: GOVERN/Identify/Protect/Detect/Respond groupings, IT vs OT
goals, implementation/defining-objectives. Watch for third-party logos/content in the
CISA PDFs — synthesize only CISA-authored content (3-RESEARCH.md §6 risk 5). Same
gates, same one-commit rule.
  </action>
  <verify>
    <automated>python "$REF/tools/vet_source.py" --title "Cross-Sector Cybersecurity Performance Goals 2.0 (CISA CPG 2.0)" --publisher "CISA" --license "Public Domain (US Government work, 17 U.S.C. § 105)" && python tooling/validate_pack.py packs/cisa-cpg</automated>
  </verify>
  <done>vet verdict tier 1 / exit 0 recorded; validate_pack.py passes; check_overlap exits 0; PACK.yaml license carries the statute string; scan findings dispositioned; one commit touching only packs/cisa-cpg.</done>
</task>

<task type="auto">
  <name>Task 4: Build packs/doe-sem (T1-08) + record P3-PRE-2 accepted gap</name>
  <files>packs/doe-sem/**</files>
  <action>
Repeat the Task 1 pipeline with build-sheet row T1-08 (3-RESEARCH.md §1):
title "Systems Engineering Methodology (SEM version 3)", publisher "US Department of
Energy" (matches the `"department of "` US_GOV signal — no P3-PRE-1 concern), version
"SEM3 (SEM3_1231.pdf)", default licence string, URL per 2-RESEARCH.md §8
(energy.gov/sites/prod/files/cioprod/documents/SEM3_1231.pdf — confirmed live).
FIRST build step after extract: read the extracted text for any third-party copyright
notice inside the PDF; if found, halt and surface (3-RESEARCH.md §6 risk 6). Page
count unknown — confirm from metadata.json and record actual. 6-8 chapters: SEM
lifecycle phases, core methodology elements, technical reviews, artifacts. Same gates,
same one-commit rule.
**P3-PRE-2 (record only, accepted gap):** in this plan's SUMMARY, record verbatim:
"Accepted gap: vet_source.py lacks ecss/esa/def-stan/dstan EXCLUDED signals; the
human rubric governs, the tool under-blocks, and none of the affected sources appear
in Phase 3 build lists. External-repo fix scheduled as follow-up." (Disposition per
2-GAP_ANALYSIS.md:90 and 3-RESEARCH.md §7.)
  </action>
  <verify>
    <automated>python tooling/validate_pack.py packs/doe-sem && python "$REF/tools/check_overlap.py" --source "$TMPSEM/book_skill_work/full_text.txt" --pack packs/doe-sem</automated>
  </verify>
  <done>validate_pack.py passes; PACK.yaml source_pages = actual metadata.json count; in-PDF third-party-copyright check result recorded; check_overlap exits 0; P3-PRE-2 accepted-gap text present in plan SUMMARY; one commit touching only packs/doe-sem.</done>
</task>

</tasks>

<threat_model>
## Trust Boundaries

| Boundary | Description |
|----------|-------------|
| internet → sources/ | downloaded PDFs are untrusted build inputs, never committed |
| source text → pack content | licence-safety boundary: verbatim runs must not cross (check_overlap gate) |

## STRIDE Threat Register

| Threat ID | Category | Component | Severity | Disposition | Mitigation Plan |
|-----------|----------|-----------|----------|-------------|-----------------|
| T-3A-01 | Repudiation | PACK.yaml provenance | medium | mitigate | source_pages/chapters/built_on filled from metadata.json, not estimated |
| T-3A-02 | Elevation of privilege (licence tier) | cisa-cpg vet gate | high | mitigate | P3-PRE-1 statute-bearing licence string; vet must exit 0 tier 1 before scaffold |
| T-3A-03 | Information disclosure | sources/, full_text.txt | high | mitigate | gitignored paths; per-task `git show --stat` check for stray staged source files |
| T-3A-04 | IP theft (verbatim copying) | chapters/ | high | mitigate | check_overlap.py exit-3 gate must not be bypassed; synthesize per PACK-SPEC |
</threat_model>

<verification>
After Task 4: `for p in nist-800-171 nist-800-61 cisa-cpg doe-sem; do python tooling/validate_pack.py packs/$p || exit 1; done` passes; `git log --oneline -4` shows one commit per pack; `git status` clean of sources/ paths.
</verification>

<success_criteria>
4 packs built, all validators pass, PACK.yaml provenance complete per ROADMAP Phase 3 SC1-SC3; P3-PRE-1 proven; P3-PRE-2 recorded; no source material committed.
</success_criteria>

<output>
Create `.planning/phases/3-tier-1-packs-public-domain/3-01-SUMMARY.md` when done
</output>
