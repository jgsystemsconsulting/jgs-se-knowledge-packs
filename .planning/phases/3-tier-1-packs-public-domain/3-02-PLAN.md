---
phase: 3-tier-1-packs-public-domain
plan: 02
type: execute
wave: 1
depends_on: []
files_modified:
  - packs/mil-hdbk-338/**
  - packs/mil-hdbk-516/**
autonomous: true
requirements: [T1-03, T1-04]
estimate:
  tokens: 120000
  raw_tokens: 60000
  tasks: 2
  confidence: low

must_haves:
  truths:
    - "packs/mil-hdbk-338 passes tooling/validate_pack.py; 8-10 SELECTED chapters from Part 2 design guidance; annex tables skipped"
    - "packs/mil-hdbk-516 passes tooling/validate_pack.py with complete PACK.yaml provenance"
    - "Both packs' vet/build licence strings carry the Distribution Statement A variant (per 3-RESEARCH.md §1)"
    - "check_overlap.py exits 0 for both packs"
    - "If either PDF is image-only, the OCR fallback ran and is recorded in PACK.yaml notes + plan SUMMARY (never hand-typed content)"
    - "No source PDF or full_text.txt committed"
  artifacts:
    - packs/mil-hdbk-338/SKILL.md, PACK.yaml, LICENSE, chapters/
    - packs/mil-hdbk-516/SKILL.md, PACK.yaml, LICENSE, chapters/
  key_links:
    - "Every Chapter Index link resolves (CI-checked)"
    - "Chapter slices read via outline.json offsets only — the 716pp full_text.txt is never loaded whole (>50k-token rule)"
---

<objective>
Plan B (Batch B of 3-RESEARCH.md §5): build the two DoD handbook packs —
mil-hdbk-338 (T1-03, Electronic Reliability Design Handbook, ~716 pp) and
mil-hdbk-516 (T1-04, Airworthiness Certification Criteria, ~320 pp) — via the
same pipeline as Plan A (3-RESEARCH.md §2), with two batch-specific
contingencies: mirror-fallback downloads (DLA token-gated) and scanned-PDF/OCR
fallback. Isolates the download/OCR risk from the easy packs.

Purpose: ship the two hardest-to-source Tier-1 packs with failure contained.
Output: 2 validated packs, one commit per pack. Registration consolidated in
3-03-PLAN.md (not here).
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
@.planning/phases/2-source-vetting-ruled-out-register/2-RESEARCH.md
@docs/PACK-SPEC.md
</context>

<claim_verification>
| claim | command | observed | status |
|---|---|---|---|
| pipeline order identical to Plan A | 3-RESEARCH.md §2 | authoritative | VERIFIED |
| 338B mirror at nde-ed.org; DLA quicksearch ident 54022 | 3-RESEARCH.md §1 row T1-03 + §6 risk 3 | recorded in Phase 2 | VERIFIED |
| 516C DLA-hosted PDF text begins "DISTRIBUTION STATEMENT A" | 3-RESEARCH.md §1 row T1-04 | quoted from DLA-hosted copy | VERIFIED |
| DoD licence string variant (Distribution Statement A) | 3-RESEARCH.md §1 licence strings | exact string available | VERIFIED |
| extract.py aborts on scanned/image PDFs; OCR fallback = ocrmypdf then --mode text | 3-RESEARCH.md §6 risk 2 | mitigation specified | VERIFIED |
</claim_verification>

<tasks>

<task type="auto">
  <name>Task 1: Build packs/mil-hdbk-338 (T1-03) — chapter selection over 716 pp</name>
  <files>packs/mil-hdbk-338/**</files>
  <action>
Pipeline per 3-RESEARCH.md §2 with build-sheet row T1-03. Download: try DLA
quicksearch (ident 54022) from a fresh browser session first; if token-gated, use the
verified nde-ed.org mirror, then verify the Distribution Statement A page appears in
the downloaded copy before proceeding (3-RESEARCH.md §6 risk 3). EXTRACT FIRST,
before any generation work — if extraction aborts as image-only, run the OCR
fallback (`ocrmypdf` then re-extract with `--mode text`) and record the OCR step in
PACK.yaml notes and the plan SUMMARY; do not hand-type content.
VET + SCAFFOLD with:
- title "DoD Electronic Reliability Design Handbook (MIL-HDBK-338B)"
- publisher "US Department of Defense"
- version "MIL-HDBK-338B, 1 Oct 1998 (Notice 2, 2007)"
- licence `Public Domain (US Government work, 17 U.S.C. § 105; Distribution Statement A — Approved for public release; distribution is unlimited)`
CHAPTER SELECTION (716 pp — the core risk): SELECT 8-10 chapters from Part 2 design
guidance: reliability prediction, derating, MTBF/MTTR, FMECA/FTA, reliability growth
testing, testability, physics of failure. Skip the ~400 pp of annex tables. Slice via
outline.json start_char/end_char offsets only; never load full_text.txt whole
(>50k-token rule). GENERATE per docs/PACK-SPEC.md (same structure as Plan A Task 1),
fill PACK.yaml (source_pages ~716 confirmed from metadata.json), LICENSE carrying the
Distribution Statement A text. VALIDATE → SCAN → OVERLAP. One commit
(`feat(packs): add mil-hdbk-338 (Tier 1)`), touching only packs/mil-hdbk-338.
REF = C:/Users/gower/OneDrive/Documents/GitHub/jgs-reference-skill; `python`, not python3.
  </action>
  <verify>
    <automated>python tooling/validate_pack.py packs/mil-hdbk-338 && ls packs/mil-hdbk-338/chapters | wc -l</automated>
  </verify>
  <done>validate_pack.py passes; chapters/ contains 8-10 files drawn from the selected topics (no annex-table chapters); PACK.yaml source_pages = actual; check_overlap exits 0; scan findings dispositioned; if OCR ran, recorded; one commit touching only packs/mil-hdbk-338.</done>
</task>

<task type="auto">
  <name>Task 2: Build packs/mil-hdbk-516 (T1-04)</name>
  <files>packs/mil-hdbk-516/**</files>
  <action>
Same pipeline and contingencies as Task 1, build-sheet row T1-04:
title "DoD Airworthiness Certification Criteria (MIL-HDBK-516C)", publisher "US
Department of Defense", version "516C, 12 Dec 2014 (Change 1, 2016)", same
Distribution Statement A licence-string variant. Download: DLA quicksearch from a
fresh browser session (3-RESEARCH.md §6 risk 3 fallbacks apply — verify a
Distribution Statement A page in the copy before use). If the DLA PDF is a scanned
image, same OCR fallback + PACK.yaml/SUMMARY record. 6-8 chapters: airworthiness
process, tailoring, one chapter per functional-area cluster (systems engineering,
structures, flight, propulsion, avionics/EW, system software, crew systems).
~320 pp. Same gates (validate → scan disposition → overlap exit 0), one commit
touching only packs/mil-hdbk-516.
  </action>
  <verify>
    <automated>python tooling/validate_pack.py packs/mil-hdbk-516 && python "$REF/tools/check_overlap.py" --source "$TMP516/book_skill_work/full_text.txt" --pack packs/mil-hdbk-516</automated>
  </verify>
  <done>Same done-criteria as Task 1 for mil-hdbk-516; PACK.yaml carries Distribution Statement A licence, tier 1, actual source_pages; one commit touching only packs/mil-hdbk-516.</done>
</task>

</tasks>

<threat_model>
## Trust Boundaries

| Boundary | Description |
|----------|-------------|
| mirror sites → sources/ | third-party mirrors of DoD PDFs: untrusted provenance until Distribution Statement page verified in-copy |
| source text → pack content | verbatim-run boundary (check_overlap) |

## STRIDE Threat Register

| Threat ID | Category | Component | Severity | Disposition | Mitigation Plan |
|-----------|----------|-----------|----------|-------------|-----------------|
| T-3B-01 | Tampering (source substitution) | mirrored PDFs | high | mitigate | verify Distribution Statement A page inside the downloaded copy before vet/extract; record mirror used in PACK.yaml notes |
| T-3B-02 | Information disclosure | sources/, full_text.txt | high | mitigate | gitignored; per-task commit-stat check |
| T-3B-03 | DoS (extraction abort) | scanned image PDFs | medium | mitigate | OCR fallback (ocrmypdf + --mode text), recorded; never hand-type |
| T-3B-04 | IP theft (verbatim copying) | chapters/ | high | mitigate | check_overlap exit-3 gate; synthesis only |
</threat_model>

<verification>
`python tooling/validate_pack.py packs/mil-hdbk-338 && python tooling/validate_pack.py packs/mil-hdbk-516` pass; `git log --oneline -2` shows two per-pack commits; no sources/ paths in either commit.
</verification>

<success_criteria>
Both DoD packs built and validated per ROADMAP Phase 3 SC1-SC3; mirror + OCR contingencies either avoided or executed-and-recorded; PACK.yaml provenance complete; no source material committed.
</success_criteria>

<output>
Create `.planning/phases/3-tier-1-packs-public-domain/3-02-SUMMARY.md` when done
</output>
