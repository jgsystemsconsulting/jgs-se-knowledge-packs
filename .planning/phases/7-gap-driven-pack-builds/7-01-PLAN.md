---
phase: 7-gap-driven-pack-builds
plan: 01
type: execute
wave: 1
depends_on: []
files_modified:
  - packs/faa-std-025/**
  - packs/dote-te-guidebook/**
  - packs/dafman-63-119/**
  - packs/federal-bca/**
autonomous: true
requirements: [GP-02, GP-03, GP-04, GP-06]
estimate:
  tokens: 150000
  raw_tokens: 75000
  tasks: 4
  confidence: low

must_haves:
  truths:
    - "packs/faa-std-025 passes tooling/validate_pack.py; PACK.yaml records which revision was built (rev E ROSAP canonical or rev F everyspec mirror) per P7-PRE-3"
    - "packs/dote-te-guidebook passes tooling/validate_pack.py; PACK.yaml records the edition actually built (Aug 2022 8.02 or afacpo v3-June) per P7-PRE-3; SKILL.md Scope & Limits states the relationship to the existing dod-te-guidebook pack"
    - "packs/dafman-63-119 passes tooling/validate_pack.py; the releasability line ('no releasability restrictions') is re-confirmed in the actually-downloaded copy per P7-PRE-5"
    - "packs/federal-bca passes tooling/validate_pack.py; in-source licence evidence for BOTH OMB A-94 and US Army CBA Guide confirmed BEFORE any chapter generation per P7-PRE-2"
    - "check_overlap.py exits 0 for every pack (both full_texts for federal-bca)"
    - "Every SKILL.md contains `## When to use` + a `**Prerequisites:**` line; no TODO stubs in any PACK.yaml"
    - "Every extraction meets the chars/page floor >= 300 (avg chars/page from metadata.json pages vs full_text length)"
    - "No source PDF or full_text.txt committed — one scoped commit per pack, zero sources/ paths in each"
  artifacts:
    - packs/faa-std-025/{SKILL.md,PACK.yaml,LICENSE,chapters/}
    - packs/dote-te-guidebook/{SKILL.md,PACK.yaml,LICENSE,chapters/}
    - packs/dafman-63-119/{SKILL.md,PACK.yaml,LICENSE,chapters/}
    - packs/federal-bca/{SKILL.md,PACK.yaml,LICENSE,chapters/}
  key_links:
    - "Every chapters/ link in each SKILL.md Chapter Index resolves to a real file"
    - "PACK.yaml source_pages matches metadata.json (summed across both extractions for federal-bca)"
---

<objective>
Wave A (7-RESEARCH.md §3): build the 4 born-digital packs — faa-std-025 (GP-02),
dote-te-guidebook (GP-03), dafman-63-119 (GP-04), federal-bca (GP-06) — via the
proven Phase 3 pipeline (7-RESEARCH.md §2, deltas 4/5/6). This plan proves
P7-PRE-2 (dual in-source licence gate), P7-PRE-3 (edition recording) and P7-PRE-5
(in-source confirmation on friendly sources) before Wave B/C hit fetch/scan risk.

Purpose: ship the lowest-risk half of the 7 GP packs and prove the Phase 7
obligation handling end-to-end.
Output: 4 validated packs under packs/, one scoped commit per pack. Registration
is deliberately NOT done here — consolidated in 7-03-PLAN.md.
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
|---|---|---|---|
| 56 pack dirs / catalog 54 today (registration untouched this plan) | `ls packs \| wc -l`; `python -c "import json;print(len(json.load(open('catalog.json'))['packs']))"` | 56 / 54 | VERIFIED |
| `dod-te-guidebook` already exists (slug-collision watch, 7-RESEARCH §1) | `ls packs \| grep te-guidebook` | dod-te-guidebook/ | VERIFIED |
| default + DIST-A licence strings and per-pack source URLs from 6-RESEARCH | 7-RESEARCH.md §1 table + §2 licence strings | authoritative | VERIFIED |
| dafman63-119.pdf 403s plain curl (bot protection) | 7-RESEARCH.md §1 GP-04 row + delta 5 | rendered/browser fetch required | VERIFIED (via 7-RESEARCH) |
| validate_pack.py / gen_packs_page.py / check_release.py exist in tooling/ | `ls tooling/*.py` | all present | VERIFIED |
| Phase 3 pipeline command order + work_dir.txt convention | 3-01-PLAN.md Task 1 + 7-RESEARCH.md §2 | authoritative | VERIFIED |
</claim_verification>

<tasks>

<task type="auto">
  <name>Task 1: Build packs/faa-std-025 (GP-02) — P7-PRE-3 edition recording</name>
  <files>packs/faa-std-025/**</files>
  <action>
Execute the 7-RESEARCH.md §2 pipeline for slug `faa-std-025`. REF =
`C:/Users/gower/OneDrive/Documents/GitHub/jgs-reference-skill`; use `python`.
1. `mkdir -p sources/faa-std-025`; download the ROSAP canonical PDF
   `https://rosap.ntl.bts.gov/view/dot/42955` → `dot_42955_DS1.pdf` (rev E,
   ~1.06 MB). If ROSAP fails, fall back to the everyspec rev F mirror
   (7-RESEARCH §1 GP-02 URL).
2. VET: `python "$REF/tools/vet_source.py" --title "Preparation of Interface Documentation (FAA-STD-025)" --publisher "Federal Aviation Administration" --license "Public Domain (US Government work, 17 U.S.C. § 105)"`. Expect tier 1, exit 0; third-party-quote advisory is expected, not a blocker.
3. **P7-PRE-3 (hard gate):** open the downloaded PDF and record exactly which
   revision it is (cover page "FAA-STD-025, Change/Edition" line). PACK.yaml
   `version` MUST carry the actual revision and source, e.g. "Rev E (2002-08-09,
   ROSAP dot-42955)" or "Rev F (everyspec mirror)" — never an unattributed
   "current". Also do the P7-PRE-5 in-PDF rights-statement check: grep the
   extracted text for a rights/releasability statement; record the finding in
   PACK.yaml notes (ROSAP record itself carries none beyond the repository
   disclaimer, so the in-PDF check is the evidence).
4. EXTRACT (`--mode technical --install-missing no`); chars/page floor: compute
   `len(full_text.txt)/metadata.json pages` — must be >= 300; if below, the copy
   is suspect (wrong/scan PDF) → halt and re-fetch before proceeding.
5. OUTLINE → sources/faa-std-025/outline.json; SCAFFOLD via build_pack.py
   (slug/title/publisher/version-per-P7-PRE-3/licence string, --out-dir packs).
6. GENERATE 5-7 chapters per the build sheet: IR/ICD/IRD family definitions; IRD
   content; ICD content; IR content; change control/CM interface; application
   examples. Target-cluster vocabulary (Interface Management, Requirements
   Traceability, Configuration Management) in the SKILL.md Topic Index. SKILL.md
   contract: `## When to use` section immediately followed by a
   `**Prerequisites:**` line; body < ~4,000 tokens; no source URLs in pack
   files. Fill PACK.yaml TODOs (source_pages from metadata.json, chapters,
   built_on, notes incl. the P7-PRE-3/P7-PRE-5 findings); complete LICENSE.
7. Work-root to `sources/faa-std-025/work_dir.txt` (printf '%s', read tr -d '\r\n').
8. VALIDATE + SCAN + OVERLAP (validate_pack.py; scan_generated_skill.py with
   disposition recorded in PACK.yaml notes; check_overlap.py exit 0 mandatory).
9. Commit only packs/faa-std-025 (`feat(packs): add faa-std-025 (Tier 1)`).
  </action>
  <verify>
    <automated>REF="C:/Users/gower/OneDrive/Documents/GitHub/jgs-reference-skill"; WRK=$(cat sources/faa-std-025/work_dir.txt | tr -d '\r\n') && python tooling/validate_pack.py packs/faa-std-025 && python "$REF/tools/check_overlap.py" --source "$WRK/book_skill_work/full_text.txt" --pack packs/faa-std-025 && python "$REF/tools/scan_generated_skill.py" packs/faa-std-025 && grep -c "^## When to use" packs/faa-std-025/SKILL.md && grep -c "^\*\*Prerequisites:\*\*" packs/faa-std-025/SKILL.md && ! grep -qi "TODO" packs/faa-std-025/PACK.yaml && grep -Eq "rev[. ]*[EF]\b|Rev [EF]" packs/faa-std-025/PACK.yaml && python -c "import json,sys,pathlib;w=pathlib.Path('$WRK'.replace(chr(92),'/'))/'book_skill_work';ft=(w/'full_text.txt').read_text(errors='ignore');m=json.load(open(w/'metadata.json'));pg=m.get('pages') or m.get('num_pages');c=len(ft)/pg;print('faa-std-025 chars/page:',round(c,1));sys.exit(0 if c>=300 else 1)" && [ -z "$(git show --name-only --pretty=format: HEAD | grep -E 'sources/|full_text.txt')" ]</automated>
  </verify>
  <done>validate_pack.py passes; check_overlap exit 0; scan dispositioned; SKILL.md has When-to-use + Prerequisites; PACK.yaml carries the actual revision (E or F) with source attribution per P7-PRE-3, the P7-PRE-5 rights-statement finding in notes, no TODO stubs; chars/page >= 300 recorded; one commit scoped to packs/faa-std-025 with zero sources/ leakage.</done>
</task>

<task type="auto">
  <name>Task 2: Build packs/dote-te-guidebook (GP-03) — P7-PRE-3 + slug-distinction</name>
  <files>packs/dote-te-guidebook/**</files>
  <action>
Repeat the Task 1 pipeline (same gates: chars/page floor >= 300, SKILL.md
When-to-use + Prerequisites contract, work_dir.txt, one scoped commit) with
build-sheet row GP-03 (7-RESEARCH §1): title "Test & Evaluation Enterprise
Guidebook", publisher "US Department of Defense (Director, Operational Test &
Evaluation)", default statute licence string.
Source chain: prefer the Aug 2022 edition (8.02) — try
`https://www.dote.osd.mil/Guidance/` for a direct PDF in-session; if
page-not-file, use the DMI mirror download (`.../TE%20Enterprise%20Guidebook%208.02.pdf`,
7-RESEARCH §1 GP-03); last resort the afacpo v3-June (2022-06) fallback using
the SINGLE-encoded URL from 6-RESEARCH §2b (the gap-report double-encoded %2526E
form 404s — do not use it).
**P7-PRE-3 (hard gate):** PACK.yaml `version` records the edition actually built
and its source, e.g. "8.02 (Aug 2022, DMI mirror)" or "v3-June 2022-06 (afacpo)".
P7-PRE-5: check in-PDF rights/releasability statement, record in notes.
Generate 7-9 chapters per build sheet (T&E enterprise overview/roles; DT&E;
OT&E; LFT&E; cybersecurity T&E; MOSA/automated T&E; suitability/reliability
growth; TEMP/STE planning documents).
**Slug-distinction requirement:** SKILL.md Scope & Limits MUST state the
relationship to the existing `dod-te-guidebook` pack (different source: DOT&E
OSD vs DoD-wide) so users can route correctly; check_overlap will cross-compare
the two — if overlap flags, tighten synthesis and rerun. Target-cluster
vocabulary: Test & Evaluation, Verification, Validation, Logistics.
  </action>
  <verify>
    <automated>REF="C:/Users/gower/OneDrive/Documents/GitHub/jgs-reference-skill"; WRK=$(cat sources/dote-te-guidebook/work_dir.txt | tr -d '\r\n') && python tooling/validate_pack.py packs/dote-te-guidebook && python "$REF/tools/check_overlap.py" --source "$WRK/book_skill_work/full_text.txt" --pack packs/dote-te-guidebook && python "$REF/tools/scan_generated_skill.py" packs/dote-te-guidebook && grep -c "^## When to use" packs/dote-te-guidebook/SKILL.md && grep -c "^\*\*Prerequisites:\*\*" packs/dote-te-guidebook/SKILL.md && grep -ci "dod-te-guidebook" packs/dote-te-guidebook/SKILL.md && ! grep -qi "TODO" packs/dote-te-guidebook/PACK.yaml && grep -Eq "^source_version:.*(8\.02|v3-June)" packs/dote-te-guidebook/PACK.yaml && python -c "import json,sys,pathlib;w=pathlib.Path('$WRK'.replace(chr(92),'/'))/'book_skill_work';ft=(w/'full_text.txt').read_text(errors='ignore');m=json.load(open(w/'metadata.json'));pg=m.get('pages') or m.get('num_pages');c=len(ft)/pg;print('dote-te-guidebook chars/page:',round(c,1));sys.exit(0 if c>=300 else 1)" && [ -z "$(git show --name-only --pretty=format: HEAD | grep -E 'sources/|full_text.txt')" ]</automated>
  </verify>
  <done>All Task 1 done-criteria for dote-te-guidebook; PACK.yaml records the built edition per P7-PRE-3; SKILL.md cross-references the distinct dod-te-guidebook pack; chars/page >= 300; one scoped commit.</done>
</task>

<task type="auto">
  <name>Task 3: Build packs/dafman-63-119 (GP-04) — rendered fetch + P7-PRE-5 re-confirm</name>
  <files>packs/dafman-63-119/**</files>
  <action>
Repeat the Task 1 pipeline (same gates) with build-sheet row GP-04 (7-RESEARCH
§1): title "Mission-Oriented Test Readiness Certification (DAFMAN 63-119)",
publisher "US Department of the Air Force", version "15 APR 2021", default
statute licence string.
Fetch (7-RESEARCH §2 delta 5): `https://static.e-publishing.af.mil/production/1/saf_aq/publication/dafman63-119/dafman63-119.pdf`
403s plain curl (bot protection) — use a rendered/browser fetch (or browser-UA +
cookie jar) to retrieve the PDF, then proceed fully offline.
**P7-PRE-5 (hard gate):** the downloaded copy may differ from the one vetted in
Phase 6 — re-confirm the "no releasability restrictions" line in the extracted
text of the ACTUALLY downloaded copy before generation; record the verbatim
finding in PACK.yaml notes. If the line is absent, halt and surface to the
orchestrator rather than proceeding on statute basis alone.
Chars/page floor >= 300. Generate 6-8 chapters per build sheet (MOTRC framework;
readiness certification process; DT&E/contractor testing; integration;
certification gates/roles; documentation). Target-cluster vocabulary: Test &
Evaluation, Integration, Supplier/Industry.
Work-root to sources/dafman-63-119/work_dir.txt; one scoped commit.
  </action>
  <verify>
    <automated>REF="C:/Users/gower/OneDrive/Documents/GitHub/jgs-reference-skill"; WRK=$(cat sources/dafman-63-119/work_dir.txt | tr -d '\r\n') && python tooling/validate_pack.py packs/dafman-63-119 && python "$REF/tools/check_overlap.py" --source "$WRK/book_skill_work/full_text.txt" --pack packs/dafman-63-119 && python "$REF/tools/scan_generated_skill.py" packs/dafman-63-119 && grep -c "^## When to use" packs/dafman-63-119/SKILL.md && grep -c "^\*\*Prerequisites:\*\*" packs/dafman-63-119/SKILL.md && ! grep -qi "TODO" packs/dafman-63-119/PACK.yaml && grep -Eqi "15 APR 2021|2021-04-15" packs/dafman-63-119/PACK.yaml && grep -qi "no releasability restrictions" "$WRK/book_skill_work/full_text.txt" && python -c "import json,sys,pathlib;w=pathlib.Path('$WRK'.replace(chr(92),'/'))/'book_skill_work';ft=(w/'full_text.txt').read_text(errors='ignore');m=json.load(open(w/'metadata.json'));pg=m.get('pages') or m.get('num_pages');c=len(ft)/pg;print('dafman-63-119 chars/page:',round(c,1));sys.exit(0 if c>=300 else 1)" && [ -z "$(git show --name-only --pretty=format: HEAD | grep -E 'sources/|full_text.txt')" ]</automated>
  </verify>
  <done>All Task 1 done-criteria for dafman-63-119; releasability line re-confirmed in the downloaded copy and recorded per P7-PRE-5; PACK.yaml version 15 APR 2021; one scoped commit.</done>
</task>

<task type="auto">
  <name>Task 4: Build packs/federal-bca (GP-06) — P7-PRE-2 dual in-source licence hard gate</name>
  <files>packs/federal-bca/**</files>
  <action>
Dual-document pack (7-RESEARCH §2 delta 4, cisa-cpg precedent). Build-sheet row
GP-06: title "Guidelines and Discount Rates for Benefit-Cost Analysis of Federal
Programs (OMB Circular A-94) + US Army Cost Benefit Analysis Guide", publishers
"US Office of Management and Budget; US Army (ASAFM)", default statute licence
string at scaffold.
1. `mkdir -p sources/federal-bca`; download BOTH PDFs (7-RESEARCH §1 GP-06):
   OMB Circular A-94 from the whitehouse.gov circulars page, and the US Army
   CBA Guide from the asafm.army.mil URL.
2. VET each document separately (two vet_source.py runs, same licence string,
   title/publisher per document). Both must exit 0 tier 1.
3. **P7-PRE-2 (HARD GATE — BEFORE ANY CHAPTER GENERATION):** for EACH document,
   confirm in-source licence evidence (in-PDF rights/releasability statement or
   equivalent US-government-work statement in the extracted text). This source
   pair has the lightest evidence trail of the eight (statute basis only,
   SOURCE-VETTING.md:135). If EITHER fails the in-source check: STOP — do not
   generate chapters; drop the failing document and rescope the pack to the
   surviving document (updating title/version) or descope entirely, and surface
   to the orchestrator. Record both findings verbatim in PACK.yaml notes.
4. EXTRACT both (`--mode technical --install-missing no`); chars/page floor >=
   300 on EACH extraction; work-roots to `sources/federal-bca/work_dir_main.txt`
   (A-94) and `work_dir_ctrl.txt` (Army CBA). Copy book_skill_work under
   sources/federal-bca/ between runs so %TEMP% is not clobbered.
5. OUTLINE from the A-94 full_text (primary spine); SCAFFOLD with combined
   title; PACK.yaml `version` records BOTH editions ("A-94 current (retrieved
   2026-08-XX); Army CBA Guide current (retrieved 2026-08-XX)").
6. GENERATE 6-8 chapters per build sheet: BCA principles/discounting (A-94);
   treatment of uncertainty; opportunity cost; Army CBA process steps; cost
   element structures; sensitivity/risk analysis; reporting — drawn from BOTH
   full_texts via outline slices. Target-cluster vocabulary: Opportunity/Benefit
   Analysis (worst cluster 15), Decision Analysis, Technical Planning.
7. VALIDATE + SCAN + OVERLAP against BOTH full_texts (both must exit 0).
   PACK.yaml source_pages = SUM of both metadata.json counts. SKILL.md contract
   (When-to-use + Prerequisites). One scoped commit.
  </action>
  <verify>
    <automated>REF="C:/Users/gower/OneDrive/Documents/GitHub/jgs-reference-skill"; W1=$(cat sources/federal-bca/work_dir_main.txt | tr -d '\r\n'); W2=$(cat sources/federal-bca/work_dir_ctrl.txt | tr -d '\r\n') && python tooling/validate_pack.py packs/federal-bca && python "$REF/tools/check_overlap.py" --source "$W1/book_skill_work/full_text.txt" --pack packs/federal-bca && python "$REF/tools/check_overlap.py" --source "$W2/book_skill_work/full_text.txt" --pack packs/federal-bca && python "$REF/tools/scan_generated_skill.py" packs/federal-bca && grep -c "^## When to use" packs/federal-bca/SKILL.md && grep -c "^\*\*Prerequisites:\*\*" packs/federal-bca/SKILL.md && ! grep -qi "TODO" packs/federal-bca/PACK.yaml && grep -Eqi "circular a-?94" "$W1/book_skill_work/full_text.txt" && grep -Eqi "cost benefit" "$W2/book_skill_work/full_text.txt" && python -c "import json,sys,pathlib
for tag,p in (('A-94','$W1'),('Army-CBA','$W2')):
    w=pathlib.Path(p.replace(chr(92),'/'))/'book_skill_work';ft=(w/'full_text.txt').read_text(errors='ignore');m=json.load(open(w/'metadata.json'));pg=m.get('pages') or m.get('num_pages');c=len(ft)/pg;print('federal-bca',tag,'chars/page:',round(c,1))
    if c<300: sys.exit(1)" && [ -z "$(git show --name-only --pretty=format: HEAD | grep -E 'sources/|full_text.txt')" ]</automated>
  </verify>
  <done>validate_pack.py passes; check_overlap exits 0 against BOTH full_texts; P7-PRE-2 in-source evidence recorded verbatim for BOTH documents (or the halt-and-rescope path taken and surfaced); PACK.yaml records both editions, summed source_pages, no TODO stubs; SKILL.md has When-to-use + Prerequisites; chars/page >= 300 on each extraction; one scoped commit.</done>
</task>

</tasks>

<threat_model>
## Trust Boundaries

| Boundary | Description |
|----------|-------------|
| internet → sources/ | downloaded PDFs are untrusted build inputs, never committed |
| source text → pack content | licence-safety boundary: verbatim runs must not cross (check_overlap gate) |
| fetched copy → vetted copy | bot-protected/mirror fetches may serve a different variant than Phase 6 vetted |

## STRIDE Threat Register

| Threat ID | Category | Component | Severity | Disposition | Mitigation Plan |
|-----------|----------|-----------|----------|-------------|-----------------|
| T-7A-01 | Tampering (evidence integrity) | federal-bca licence evidence | high | mitigate | P7-PRE-2: in-source check for BOTH docs before generation; halt-and-surface on failure (T-6-03 enforcement) |
| T-7A-02 | Tampering | dafman/dote fetched variants | medium | mitigate | P7-PRE-5/P7-PRE-3: re-confirm rights statement + edition in the actually-downloaded copy |
| T-7A-03 | Repudiation | PACK.yaml provenance | medium | mitigate | edition + retrieval date recorded per P7-PRE-3; source_pages from metadata.json only |
| T-7A-04 | Information disclosure | sources/, full_text.txt | high | mitigate | gitignored; per-task git-show leak check |
| T-7A-05 | IP theft (verbatim copying) | chapters/ | high | mitigate | check_overlap exit-3 gate; synthesize per PACK-SPEC |
</threat_model>

<verification>
After Task 4: `for p in faa-std-025 dote-te-guidebook dafman-63-119 federal-bca; do python tooling/validate_pack.py packs/$p || exit 1; done` passes; `git log --oneline -4` shows one commit per pack; `git status` clean of sources/ paths; packs/ dir count now 60 (56+4), catalog still 54 (registration is 7-03).
</verification>

<success_criteria>
4 Wave-A packs built, all validators pass, PACK.yaml provenance complete per ROADMAP Phase 7 SC-1/SC-2; P7-PRE-2 gate enforced with recorded evidence; P7-PRE-3 editions recorded; P7-PRE-5 re-confirmations recorded; chars/page floor >= 300 on every extraction; no source material committed.
</success_criteria>

<output>
Create `.planning/phases/7-gap-driven-pack-builds/7-01-SUMMARY.md` when done
</output>
