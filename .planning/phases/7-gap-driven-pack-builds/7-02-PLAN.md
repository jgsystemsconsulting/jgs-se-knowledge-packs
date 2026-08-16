---
phase: 7-gap-driven-pack-builds
plan: 02
type: execute
wave: 2
depends_on: ["7-01"]
files_modified:
  - packs/mil-std-881f/**
  - packs/mil-std-40051/**
autonomous: true
requirements: [GP-05, GP-07]
estimate:
  tokens: 110000
  raw_tokens: 55000
  tasks: 2
  confidence: low

must_haves:
  truths:
    - "packs/mil-std-881f passes tooling/validate_pack.py; DIST-A visually confirmed on the actual fetched copy (P7-PRE-1); exact revision resolved and recorded in PACK.yaml, or 881E fallback clearly labelled"
    - "packs/mil-std-40051 passes tooling/validate_pack.py; DIST-A visually confirmed on the scanned cover page (P7-PRE-1); chars/page floor >= 300 on the selected main-body extraction; OCR contingency exercised and recorded if triggered"
    - "mil-std-40051 chapter set (6-10 chapters from ~1168 pp) targets cluster 25 (Training & Documentation, currently EMPTY — hard ROADMAP requirement) plus cluster 24 (Ops & Maintenance)"
    - "check_overlap.py exits 0 for both packs; every SKILL.md has `## When to use` + `**Prerequisites:**`; no TODO stubs"
    - "No source PDFs or full_text.txt committed; one scoped commit per pack"
  artifacts:
    - packs/mil-std-881f/{SKILL.md,PACK.yaml,LICENSE,chapters/}
    - packs/mil-std-40051/{SKILL.md,PACK.yaml,LICENSE,chapters/}
  key_links:
    - "PACK.yaml source_pages reflects the SELECTED content (metadata.json-based), not the 1168-page file total"
    - "PACK.yaml notes record the DIST-A visual confirmation method and (for 40051) the OCR/no-OCR decision"
---

<objective>
Wave B (7-RESEARCH.md §3): build the two DoD mirror/spec fetches — mil-std-881f
(GP-05) and mil-std-40051 (GP-07) — carrying the P7-PRE-1 visual DIST-A
obligations, the 881F gated-download fallback chain, and the 40051
scanned-copy quality gates (chars/page floor, OCR contingency, hard chapter
selection from 1168 pp).

Purpose: the two highest single-pack risk builds, isolated from Waves A/C so
their fetch/scan failures cannot block the friendly sources.
Output: 2 validated packs under packs/, one scoped commit per pack.
Registration consolidated in 7-03-PLAN.md.
</objective>

<execution_context>
@$HOME/.zcode/gsd-core/workflows/execute-plan.md
@$HOME/.zcode/gsd-core/templates/summary.md
</execution_context>

<context>
@.planning/PROJECT.md
@.planning/ROADMAP.md
@.planning/phases/7-gap-driven-pack-builds/7-RESEARCH.md
@.planning/phases/6-source-vetting-unverified-resolution/6-GAP_ANALYSIS.md
@docs/PACK-SPEC.md
@.planning/phases/3-tier-1-packs-public-domain/3-01-PLAN.md
</context>

<claim_verification>
| claim | command | observed | status |
|---|---|---|
| everyspec has only 881E (fallback must be revision-labelled) | 7-RESEARCH.md §1 GP-05 row + risk 2 | authoritative | VERIFIED |
| 40051 mirror PDF is 37.7 MB / 1168 page objects; Distribution Statement is a scanned image | 7-RESEARCH.md §1 GP-07 row + §2 delta 2 | authoritative | VERIFIED |
| QuickSearch detail ident_number=36026; GovTribe attachment URL | 7-RESEARCH.md §1 GP-05 row | authoritative | VERIFIED |
| DIST-A licence string variant exact text | 7-RESEARCH.md §2 licence strings | `Public Domain (US Government work, 17 U.S.C. § 105; Distribution Statement A — Approved for public release; distribution is unlimited)` | VERIFIED |
| validate_pack.py / overlap / scan toolchain paths | 7-RESEARCH.md §2; tooling/ listing | all present | VERIFIED |
</claim_verification>

<tasks>

<task type="auto">
  <name>Task 1: Build packs/mil-std-881f (GP-05) — fetch fallback chain + P7-PRE-1 visual DIST-A</name>
  <files>packs/mil-std-881f/**</files>
  <action>
Execute the 7-RESEARCH.md §2 pipeline for slug `mil-std-881f` with §2 delta 3.
REF = `C:/Users/gower/OneDrive/Documents/GitHub/jgs-reference-skill`; `python`.
1. `mkdir -p sources/mil-std-881f`; FETCH via the fallback chain, in order:
   a. QuickSearch detail `https://quicksearch.dla.mil/qsdocdetails.aspx?ident_number=36026`
      (free account/session) — while there, RESOLVE THE EXACT REVISION DATE
      (expected 881F, 13 May 2022 per AF/DoD citations; record what the detail
      page actually says); direct PDF download needs the free session.
   b. If blocked: GovTribe attachment
      `https://govtribe.com/file/government-file/b08-attachment-4-mil-std-881f-dot-pdf`
      (HTML download wrapper — use a rendered/browser fetch).
   c. Last resort: everyspec 881E — permitted ONLY with the revision clearly
      labelled in PACK.yaml version ("MIL-STD-881E (everyspec mirror; 881F
      unobtainable — fallback per 7-RESEARCH §2 delta 3)").
2. **P7-PRE-1 (hard gate, P7-PRE mirror-fetch):** VISUALLY inspect the fetched
   PDF's cover/notice page and confirm the Distribution Statement A text
   (rendered view or extracted image — not just a text grep, mirror copies
   differ). Record the confirmation method and finding in PACK.yaml notes
   BEFORE generation. If DIST-A cannot be visually confirmed, halt and surface.
3. VET: `python "$REF/tools/vet_source.py" --title "Work Breakdown Structures for Defense Materiel Items (MIL-STD-881F)" --publisher "US Department of Defense" --license "Public Domain (US Government work, 17 U.S.C. § 105; Distribution Statement A — Approved for public release; distribution is unlimited)"`. Expect tier 1, exit 0.
4. EXTRACT (`--mode technical --install-missing no`); chars/page floor >= 300
   (avg chars/page from metadata.json pages vs full_text length); work-root to
   sources/mil-std-881f/work_dir.txt.
5. OUTLINE → outline.json; SCAFFOLD (version per the resolved revision).
6. GENERATE 6-8 chapters per build sheet: WBS principles/definitions; WBS
   roles/responsibilities; tailoring; element definitions (cluster the
   appendices: air systems; ground; sea; space; C3I; services; R&D); WBS
   numbering/reporting. Target-cluster vocabulary: Technical Planning & WBS,
   PM/Measurement. SKILL.md contract: `## When to use` + `**Prerequisites:**`;
   no source URLs; PACK.yaml TODOs filled (source_pages from metadata.json,
   chapters, built_on, notes incl. fetch-path taken and DIST-A confirmation).
7. VALIDATE + SCAN + OVERLAP (exit 0 mandatory). One scoped commit
   (`feat(packs): add mil-std-881f (Tier 1)` — slug stays 881f even on an 881E
   fallback build; the version field carries the truth).
  </action>
  <verify>
    <automated>REF="C:/Users/gower/OneDrive/Documents/GitHub/jgs-reference-skill"; WRK=$(cat sources/mil-std-881f/work_dir.txt | tr -d '\r\n') && python tooling/validate_pack.py packs/mil-std-881f && python "$REF/tools/check_overlap.py" --source "$WRK/book_skill_work/full_text.txt" --pack packs/mil-std-881f && python "$REF/tools/scan_generated_skill.py" packs/mil-std-881f && grep -c "^## When to use" packs/mil-std-881f/SKILL.md && grep -c "^\*\*Prerequisites:\*\*" packs/mil-std-881f/SKILL.md && ! grep -qi "TODO" packs/mil-std-881f/PACK.yaml && grep -Eq "^source_version:.*881[EF]" packs/mil-std-881f/PACK.yaml && grep -Eqi "distribution statement" "$WRK/book_skill_work/full_text.txt" && python -c "import json,sys,pathlib;w=pathlib.Path('$WRK'.replace(chr(92),'/'))/'book_skill_work';ft=(w/'full_text.txt').read_text(errors='ignore');m=json.load(open(w/'metadata.json'));pg=m.get('pages') or m.get('num_pages');c=len(ft)/pg;print('mil-std-881f chars/page:',round(c,1));sys.exit(0 if c>=300 else 1)" && [ -z "$(git show --name-only --pretty=format: HEAD | grep -E 'sources/|full_text.txt')" ]</automated>
  </verify>
  <done>validate_pack.py passes; check_overlap exit 0; scan dispositioned; PACK.yaml carries the resolved revision (or the labelled 881E fallback), the fetch path taken, and the P7-PRE-1 visual DIST-A confirmation in notes; SKILL.md has When-to-use + Prerequisites; chars/page >= 300; one scoped commit with zero sources/ leakage.</done>
</task>

<task type="auto">
  <name>Task 2: Build packs/mil-std-40051 (GP-07) — scanned-copy gates + cluster-25 empties (hard ROADMAP requirement)</name>
  <files>packs/mil-std-40051/**</files>
  <action>
Execute the pipeline with 7-RESEARCH.md §2 delta 2 (highest single-pack risk —
gates run BEFORE content generation).
1. `mkdir -p sources/mil-std-40051`; download the 37.7 MB PDF from the
   everyspec MIL-STD-40051-2C page (7-RESEARCH §1 GP-07 URL). Version:
   "MIL-STD-40051-2C, 15 DEC 2015 (-2C slice of split family — record in
   PACK.yaml)".
2. **P7-PRE-1 (hard gate):** the mirror copy's Distribution Statement is a
   SCANNED IMAGE on the cover — text-layer greps hit only boilerplate. VISUALLY
   inspect the scanned cover page (rendered view) and confirm DIST-A; record
   method + finding in PACK.yaml notes BEFORE generation. Halt and surface if
   it cannot be confirmed.
3. EXTRACT (`--mode technical --install-missing no`). Record the whole-file
   avg chars/page (len(full_text.txt)/metadata.json pages) in PACK.yaml notes
   as INFORMATIONAL ONLY — the gate does not run on this number (1168 pp of
   mostly image plates would drag it below the floor even on a healthy body).
4. **Chapter selection (hard — runs BEFORE the floor gate):** the file is 1168
   page objects, mostly per-TM format plates — do NOT ingest whole. Select
   ~150 pp of main body via outline + manual offsets; skip the per-TM format
   plates. PACK.yaml source_pages reflects the SELECTED content basis from
   metadata.json, and notes state the selection (main body ~150 pp of 1168
   total; plates skipped).
5. **Quality gate on the SELECTED body (order is fixed: select first, floor
   second):** compute chars/page = chars(selected_body) / selected_pages;
   floor >= 300; record the computed value in PACK.yaml notes. The whole-file
   number from step 3 is informational only. OCR contingency triggers ONLY on
   the selected-body floor failing: if the selected body extracts near-empty
   (image-only), run `ocrmypdf` on the PDF, re-extract `--mode text`,
   re-select, and recompute; record the OCR decision (taken or not needed) and
   the final selected-body chars/page in PACK.yaml notes and the plan SUMMARY
   deviation log (Phase 3 Risk 2 pattern).
6. VET with the DIST-A licence-string variant, title "Preparation of Digital
   Technical Information for Page-Based Technical Manuals (MIL-STD-40051-2C)",
   publisher "US Department of Defense (DLA)". Expect tier 1, exit 0.
7. OUTLINE from the selected main body; SCAFFOLD; GENERATE 6-10 chapters per
   build sheet: TDP/TM structure; page-based TM format conventions;
   front-matter/back-matter requirements; style/format rules; change
   packages/revision marking; selected plate exemplars.
   **Cluster-25 requirement (ROADMAP Phase 7/8): cluster 25 Training &
   Documentation is EMPTY and this pack is its only incoming entry — the
   SKILL.md Topic Index MUST use Training & Documentation / technical-manual /
   documentation vocabulary prominently so the Phase 8 map harvest populates
   cluster 25 (non-empty is a hard Phase 8 success criterion). Also target
   cluster 24 Ops & Maintenance.**
8. Work-root to sources/mil-std-40051/work_dir.txt; SKILL.md contract
   (When-to-use + Prerequisites); PACK.yaml TODOs filled.
9. VALIDATE + SCAN + OVERLAP (exit 0 mandatory). One scoped commit.
  </action>
  <verify>
    <automated>REF="C:/Users/gower/OneDrive/Documents/GitHub/jgs-reference-skill"; WRK=$(cat sources/mil-std-40051/work_dir.txt | tr -d '\r\n') && python tooling/validate_pack.py packs/mil-std-40051 && python "$REF/tools/check_overlap.py" --source "$WRK/book_skill_work/full_text.txt" --pack packs/mil-std-40051 && python "$REF/tools/scan_generated_skill.py" packs/mil-std-40051 && grep -c "^## When to use" packs/mil-std-40051/SKILL.md && grep -c "^\*\*Prerequisites:\*\*" packs/mil-std-40051/SKILL.md && ! grep -qi "TODO" packs/mil-std-40051/PACK.yaml && grep -Eqi "40051-2C" packs/mil-std-40051/PACK.yaml && grep -Eqi "distribution statement|DIST-A" packs/mil-std-40051/PACK.yaml && grep -q "Training & Documentation" packs/mil-std-40051/SKILL.md && grep -Eqi "chars/page" packs/mil-std-40051/PACK.yaml && python -c "import json,sys,pathlib;w=pathlib.Path('$WRK'.replace(chr(92),'/'))/'book_skill_work';ft=(w/'full_text.txt').read_text(errors='ignore');m=json.load(open(w/'metadata.json'));pg=m.get('pages') or m.get('num_pages');c=len(ft)/pg;print('mil-std-40051 whole-file chars/page (informational; OCR trigger <200):',round(c,1));sys.exit(0 if c>=200 else 1)" && [ -z "$(git show --name-only --pretty=format: HEAD | grep -E 'sources/|full_text.txt')" ]</automated>
  </verify>
  <done>validate_pack.py passes; check_overlap exit 0; P7-PRE-1 visual DIST-A confirmed on the scanned cover and recorded; chars/page floor >= 300 on the selected body (or OCR contingency exercised and recorded); 6-10 chapters selected from ~1168 pp with plates skipped and source_pages reflecting the selection; Topic Index carries cluster-25 Training & Documentation vocabulary; SKILL.md has When-to-use + Prerequisites; one scoped commit.</done>
</task>

</tasks>

<threat_model>
## Trust Boundaries

| Boundary | Description |
|----------|-------------|
| internet mirror sites → sources/ | untrusted mirror copies (GovTribe/everyspec wrappers); variant-detection gates required |
| scanned image layer → evidence | DIST-A statements live in images on mirror copies — text greps are insufficient (T-6-03) |
| source text → pack content | verbatim-run licence boundary (check_overlap) |

## STRIDE Threat Register

| Threat ID | Category | Component | Severity | Disposition | Mitigation Plan |
|-----------|----------|-----------|----------|-------------|-----------------|
| T-7B-01 | Tampering (evidence integrity) | DIST-A cover statements (both packs) | high | mitigate | P7-PRE-1 visual confirmation on the fetched copy before generation; method recorded in PACK.yaml notes (T-6-03 enforcement) |
| T-7B-02 | Tampering | 881E/881F substitution | medium | mitigate | revision resolved from QuickSearch detail or labelled explicitly on fallback; slug/version separation of concerns |
| T-7B-03 | Spoofing (quality) | 40051 scanned-body extraction | high | mitigate | chars/page floor >= 300 + OCR contingency + hard page selection; deviation-logged |
| T-7B-04 | Repudiation | PACK.yaml provenance | medium | mitigate | source_pages from metadata.json selection basis; fetch path recorded |
| T-7B-05 | Information disclosure | sources/, full_text.txt | high | mitigate | gitignored; per-task git-show leak check |
</threat_model>

<verification>
After Task 2: `for p in mil-std-881f mil-std-40051; do python tooling/validate_pack.py packs/$p || exit 1; done` passes; `git log --oneline -2` shows one commit per pack; packs/ dir count now 62 (60+2); catalog still 54 (registration is 7-03).
</verification>

<success_criteria>
Both Wave-B packs built and validated; P7-PRE-1 visual DIST-A confirmations recorded for both; 881F revision resolved or 881E fallback labelled; 40051 extraction quality gated (floor >= 300, OCR if needed, plates skipped, 6-10 chapters); cluster-25 vocabulary present in mil-std-40051 SKILL.md; no source material committed.
</success_criteria>

<output>
Create `.planning/phases/7-gap-driven-pack-builds/7-02-SUMMARY.md` when done
</output>
