---
phase: 7-gap-driven-pack-builds
plan: 03
type: execute
wave: 3
depends_on: ["7-01", "7-02"]
files_modified:
  - packs/dod-vva-rpg/**
  - catalog.json
  - SKILLS.md
  - README.md
  - NOTICE
  - docs/packs.html
  - .cursor-plugin/plugin.json
autonomous: true
requirements: [GP-01]
estimate:
  tokens: 120000
  raw_tokens: 60000
  tasks: 2
  confidence: low

must_haves:
  truths:
    - "packs/dod-vva-rpg passes tooling/validate_pack.py; built chapter-wise from per-chapter PDFs off the cto.mil index with per-chapter DIST-A/authorship confirmed in EACH chapter PDF used (P7-PRE-4) and per-chapter provenance recorded in PACK.yaml notes (titles + retrieval date, no URLs)"
    - "check_overlap.py exits 0 for dod-vva-rpg (against chapter full_texts); SKILL.md has `## When to use` + `**Prerequisites:**`; no TODO stubs"
    - "After registration: catalog.json = 61 packs, SKILLS.md header = 61 packs (+2 signposts), README badge = packs-61 + 7 new table rows, .cursor-plugin/plugin.json = 62 skills (sebok still excluded), NOTICE has 7 new [pack: <slug>] blocks, docs/packs.html regenerated via gen_packs_page.py"
    - "python tooling/check_release.py PASSES on the 61-catalog / 63-directory basis"
    - "All 8 commits clean of sources/ and full_text.txt paths"
  artifacts:
    - packs/dod-vva-rpg/{SKILL.md,PACK.yaml,LICENSE,chapters/}
    - updated catalog.json, SKILLS.md, README.md, NOTICE, docs/packs.html, .cursor-plugin/plugin.json
  key_links:
    - "PACK.yaml source_pages = SUM of per-chapter metadata.json counts"
    - "Every one of the 7 new catalog entries resolves to an existing packs/<slug>/ dir passing validate_pack.py"
---

<objective>
Wave C (7-RESEARCH.md §3): build the chapter-wise pack dod-vva-rpg (GP-01, the
bespoke build model — no consolidated PDF exists), then run the consolidated
registration sweep for all 7 GP packs (Section 4 deltas) + check_release.py PASS.

Purpose: the remaining pack plus the single registration sweep that closes the
build phase (Phase 3 3-03 precedent — registration is one sweep, never per-pack
edits).
Output: packs/dod-vva-rpg (one commit) + all registration surfaces at their
exact expected counts (one commit).
</objective>

<execution_context>
@$HOME/.zcode/gsd-core/workflows/execute-plan.md
@$HOME/.zcode/gsd-core/templates/summary.md
</execution_context>

<context>
@.planning/PROJECT.md
@.planning/ROADMAP.md
@.planning/phases/7-gap-driven-pack-builds/7-RESEARCH.md
@.planning/phases/7-gap-driven-pack-builds/7-01-SUMMARY.md
@.planning/phases/7-gap-driven-pack-builds/7-02-SUMMARY.md
@docs/PACK-SPEC.md
@.planning/phases/3-tier-1-packs-public-domain/3-01-PLAN.md
</context>

<claim_verification>
| claim | command | observed | status |
|---|---|---|---|
| registration basis, pre-Phase-7 basis: 56 dirs / catalog 54 / SKILLS.md "54 packs (+2 signposts)" / README packs-54 / cursor 55; at 7-03 start (post-7-01+7-02): 62 dirs / catalog 54 / cursor 55 | `ls packs \| wc -l`; python len(catalog packs); grep SKILLS.md:9; grep -o packs-54 README.md; python len(plugin skills) | 56 / 54 / 54 packs (+2 signposts) / packs-54 / 55 | VERIFIED (pre-Phase-7; expect 62/54/55 at 7-03 start — 7-01/7-02 add pack dirs only, no registration) |
| target basis after: 63 dirs / 61 catalog / SKILLS.md 61(+2) / packs-61 / cursor 62 | 7-RESEARCH.md §4 table | 54+7 / 55+7 (sebok still excluded) | VERIFIED |
| gen_packs_page.py exists; packs.html is generated (never hand-edit) | tooling listing + gen_packs_page.py:74 disclaimer | present | VERIFIED |
| no gen_skills_index.py exists (SKILLS.md hand-edited, keep disclaimer) | 7-RESEARCH.md §4 | authoritative | VERIFIED |
| cto.mil chapter index + UCO URL; no consolidated RPG PDF | 7-RESEARCH.md §1 GP-01 row + §2 delta 1 | authoritative | VERIFIED |
</claim_verification>

<tasks>

<task type="auto">
  <name>Task 1: Build packs/dod-vva-rpg (GP-01) chapter-wise — P7-PRE-4 per-chapter gate</name>
  <files>packs/dod-vva-rpg/**</files>
  <action>
Chapter-wise build per 7-RESEARCH.md §2 delta 1 (fix the chapter set up front
from 6-RESEARCH §1c; treat each chapter as a mini-extract). REF =
`C:/Users/gower/OneDrive/Documents/GitHub/jgs-reference-skill`; `python`.
1. `mkdir -p sources/dod-vva-rpg`; from the cto.mil index
   `https://www.cto.mil/sea/vva_rpg/` download the selected per-chapter PDFs
   (de-bok.org-hosted links): Key Concepts; core role guides (user / developer
   / M&S PM / V&V agent / accreditation agent — cluster or select); fidelity;
   validation; data V&V; risk; T&E/V&V Checklist — 8-10 chapter set (UCO at
   .../vva-rpg-uco/ optional if it fits the set).
2. VET once on the guide title: `python "$REF/tools/vet_source.py" --title "M&S Verification, Validation & Accreditation Recommended Practice Guide" --publisher "US Department of Defense (OUSW(R&E) CTO / M&S Office)" --license "Public Domain (US Government work, 17 U.S.C. § 105; Distribution Statement A — Approved for public release; distribution is unlimited)"`. Expect tier 1, exit 0.
3. **P7-PRE-4 (hard gate, per chapter):** EACH chapter PDF used gets an
   individual extract + in-PDF DIST-A/authorship check before it enters the
   chapter set; a chapter failing the check is dropped from the set (recorded),
   never included on statute basis alone. Chars/page floor >= 300 per chapter
   extraction (small PDFs; a near-empty one indicates a failed download or
   placeholder page — re-fetch or drop).
4. OUTLINE: per-chapter outline.py is meaningless — derive the chapter
   structure directly from the chapter set (one pack chapter per source
   chapter, or grouped per build sheet). Synthesis slices are the per-chapter
   full_texts; work-roots recorded per chapter in sources/dod-vva-rpg/ as
   `work_dir_ch1.txt`, `work_dir_ch2.txt`, ... (exact naming — the verify
   block globs this pattern); `mkdir -p sources/dod-vva-rpg/chapter_fulltexts`
   and copy each chapter's full_text.txt to
   `sources/dod-vva-rpg/chapter_fulltexts/chNN.txt` (one per chapter, in
   chapter order) — these are the per-chapter overlap sources and the concat
   inputs; keep book_skill_work copies under sources/dod-vva-rpg/ so %TEMP%
   is not clobbered.
5. SCAFFOLD: build_pack.py --slug dod-vva-rpg --title per above --publisher
   per above --version "RPG web edition (no dated rev; retrieved 2026-08-XX)"
   --license DIST-A variant --out-dir packs.
6. GENERATE 8-10 pack chapters per the build-sheet chapter list. Target-cluster
   vocabulary: Validation, Verification, Decision Analysis, Test & Evaluation.
   SKILL.md contract: `## When to use` + `**Prerequisites:**`; body < ~4,000
   tokens; no source URLs.
7. PACK.yaml: source_pages = SUM of per-chapter metadata.json counts; notes
   records the chapter set WITH PER-CHAPTER PROVENANCE (titles + edition/
   retrieval date — no URLs, Link Policy); no TODO stubs.
8. VALIDATE + SCAN + OVERLAP against every chapter full_text in
   sources/dod-vva-rpg/chapter_fulltexts/ (all exit 0; if the tool needs a
   single --source, concatenate chNN.txt in chapter order into one overlap
   source file under sources/). One scoped commit
   (`feat(packs): add dod-vva-rpg (Tier 1)`).
  </action>
  <verify>
    <automated>REF="C:/Users/gower/OneDrive/Documents/GitHub/jgs-reference-skill"; python tooling/validate_pack.py packs/dod-vva-rpg && for f in sources/dod-vva-rpg/chapter_fulltexts/*.txt; do python "$REF/tools/check_overlap.py" --source "$f" --pack packs/dod-vva-rpg || exit 1; done && python "$REF/tools/scan_generated_skill.py" packs/dod-vva-rpg && grep -c "^## When to use" packs/dod-vva-rpg/SKILL.md && grep -c "^\*\*Prerequisites:\*\*" packs/dod-vva-rpg/SKILL.md && ! grep -qi "TODO" packs/dod-vva-rpg/PACK.yaml && grep -Eqi "retrieved" packs/dod-vva-rpg/PACK.yaml && python -c "import json,sys,pathlib,glob
found=False
for f in sorted(glob.glob('sources/dod-vva-rpg/work_dir_ch*.txt')):
    found=True
    w=pathlib.Path(open(f).read().strip().replace(chr(92),'/'))/'book_skill_work'
    ft=(w/'full_text.txt').read_text(errors='ignore')
    m=json.load(open(w/'metadata.json')); pg=m.get('pages') or m.get('num_pages')
    c=len(ft)/pg; print(f, 'chars/page:', round(c,1))
    if c<300: sys.exit(1)
sys.exit(0 if found else 1)" && [ -z "$(git show --name-only --pretty=format: HEAD | grep -E 'sources/|full_text.txt')" ]</automated>
  </verify>
  <done>validate_pack.py passes; check_overlap exits 0 against every chapter full_text; P7-PRE-4 per-chapter DIST-A/authorship checks recorded (dropped chapters, if any, noted); PACK.yaml carries summed source_pages + per-chapter provenance (titles + retrieval date, no URLs); SKILL.md has When-to-use + Prerequisites; one scoped commit.</done>
</task>

<task type="auto">
  <name>Task 2: Consolidated registration sweep for all 7 GP packs + check_release.py</name>
  <files>catalog.json, SKILLS.md, README.md, NOTICE, docs/packs.html, .cursor-plugin/plugin.json</files>
  <action>
One sweep registering all 7 packs (7-RESEARCH.md §4 exact counts; mechanics per
3-RESEARCH §4). The 7 slugs: dod-vva-rpg, faa-std-025, dote-te-guidebook,
dafman-63-119, mil-std-881f, federal-bca, mil-std-40051.
1. catalog.json: hand-add 7 pack objects (license_tier: 1, commercial_use:
   true, status "live", actual chapter counts from the built packs). Copy the
   exact key shape from a live Tier-1 catalog object — read the faa-rma or
   nasa-se-handbook entry first and mirror its key set (slug / title /
   publisher / source_version / license / license_tier / commercial_use /
   chapters / status; PACK.yaml carries share_alike / attribution_required,
   the catalog does not). Also bump the catalog top-level `updated` field to
   the registration date (3-RESEARCH §4 mechanics). Expect 61 packs after.
2. SKILLS.md: hand-edit (no gen_skills_index.py exists) — add 7 rows, keep the
   generated-file disclaimer, update header line to "61 packs (+2 signposts)".
3. README.md: update badge to `packs-61`; add 7 table rows in the pack table.
4. NOTICE: add 7 `[pack: <slug>]` Public Domain attribution blocks mirroring
   the existing Public Domain entries.
5. .cursor-plugin/plugin.json: add 7 skill entries (all 7 are Tier 1, so all
   ship in the cursor manifest — unlike sebok, which stays excluded). Expect 62
   skills after.
6. docs/packs.html: regenerate via `python tooling/gen_packs_page.py` — never
   hand-edit (RR-B-00/RR-B-30).
7. Gate: `python tooling/check_release.py` must PASS on the 61-catalog /
   63-directory basis. If it fails on a count mismatch, fix the registration
   (not the gate) and rerun.
8. Copy the 7-RESEARCH.md §5 cluster-target table into the plan SUMMARY as the
   baseline record Phase 8 asserts against.
9. One commit for the registration sweep
   (`docs(registration): register 7 GP packs (catalog 61, cursor 62)`).
NOTE: version-surface bump (CHANGELOG, plugin 1.17.0→1.18.0, RELEASE-INFO) is
Phase 9 scope — do NOT touch it here.
  </action>
  <verify>
    <automated>python tooling/check_release.py && [ "$(python -c "import json;print(len(json.load(open('catalog.json'))['packs']))")" = "61" ] && [ "$(python -c "import json;print(len(json.load(open('.cursor-plugin/plugin.json'))['skills']))")" = "62" ] && [ "$(find packs -mindepth 1 -maxdepth 1 -type d | wc -l)" = "63" ] && grep -q "61 packs (+2 signposts)" SKILLS.md && grep -q "packs-61" README.md && for s in faa-std-025 dote-te-guidebook dafman-63-119 federal-bca mil-std-881f mil-std-40051 dod-vva-rpg; do grep -q "\[pack: $s\]" NOTICE || { echo "MISSING $s"; exit 1; }; done && python -c "import json;c=json.load(open('catalog.json'));new={'dod-vva-rpg','faa-std-025','dote-te-guidebook','dafman-63-119','mil-std-881f','federal-bca','mil-std-40051'};slugs={p['slug'] for p in c['packs']};assert new<=slugs, new-slugs;print('slug-set ok')" && grep -q "dote-te-guidebook" docs/packs.html && [ -z "$(git show --name-only --pretty=format: HEAD | grep -E 'sources/|full_text.txt')" ]</automated>
  </verify>
  <done>check_release.py PASS; catalog = 61 packs; cursor manifest = 62 skills (sebok still absent); packs/ = 63 dirs; SKILLS.md header "61 packs (+2 signposts)"; README badge packs-61 + 7 new rows; 7 NOTICE blocks; packs.html regenerated; cluster-target baseline table copied to SUMMARY; one registration commit.</done>
</task>

</tasks>

<threat_model>
## Trust Boundaries

| Boundary | Description |
|----------|-------------|
| per-chapter web downloads → sources/ | each chapter PDF is an independent untrusted input (per-chapter tamper exposure, P7-PRE-4) |
| registration surfaces → consumers | catalog/manifest counts must match reality or downstream consumers (cursor plugin, packs.html) break |

## STRIDE Threat Register

| Threat ID | Category | Component | Severity | Disposition | Mitigation Plan |
|-----------|----------|-----------|----------|-------------|-----------------|
| T-7C-01 | Tampering (evidence integrity) | per-chapter RPG PDFs | high | mitigate | P7-PRE-4: per-chapter in-PDF DIST-A/authorship check; failing chapters dropped and recorded (T-6-03 enforcement) |
| T-7C-02 | Repudiation | per-chapter provenance | medium | mitigate | PACK.yaml notes: chapter titles + retrieval date per chapter, no URLs (Link Policy) |
| T-7C-03 | Tampering | registration counts | high | mitigate | exact-count verify gates (61/62/63) + check_release.py PASS; distinctive-literal greps per slug |
| T-7C-04 | Information disclosure | sources/, full_text.txt | high | mitigate | gitignored; per-task git-show leak check |
| T-7C-05 | IP theft (verbatim copying) | chapters/ | high | mitigate | check_overlap exit 0 against every chapter full_text |
</threat_model>

<verification>
Full-phase check: `for p in dod-vva-rpg faa-std-025 dote-te-guidebook dafman-63-119 mil-std-881f federal-bca mil-std-40051; do python tooling/validate_pack.py packs/$p || exit 1; done && python tooling/check_release.py`; `git log --oneline -9` shows 7 pack commits + 1 registration commit (+2 Wave-A/B summaries if committed separately); no sources/ in any.
</verification>

<success_criteria>
All 7 GP packs built, validated, and registered at the exact expected counts (61 catalog / 62 cursor / 63 dirs / packs-61); check_release.py PASS; P7-PRE-4 per-chapter gate enforced; cluster-target baseline recorded for Phase 8; no source material committed anywhere in the phase.
</success_criteria>

<output>
Create `.planning/phases/7-gap-driven-pack-builds/7-03-SUMMARY.md` when done
</output>
