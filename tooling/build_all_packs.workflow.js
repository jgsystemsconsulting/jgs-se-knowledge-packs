/*
 * Copyright (c) 2026 JG Systems Consulting Ltd. — MIT License (see ../LICENSE).
 * SPDX-License-Identifier: MIT
 *
 * build_all_packs.workflow.js — the "one go" orchestrator for docs/BUILD-PLAN.md.
 * Builds every backlog pack whose source is staged under sources/<slug>/, through a
 * gated pipeline (vet -> extract -> outline -> scaffold -> chapters -> verify), then
 * registers the passers once. Fail-closed: a pack that fails vet/overlap/validate is
 * NOT registered. Does NOT git commit or push — packs land in the working tree for review.
 *
 * Launch:
 *   Workflow({ scriptPath: ".../tooling/build_all_packs.workflow.js",
 *              args: { slugs: ["nasa-systems-modeling"] } })   // omit slugs => all staged
 */
export const meta = {
  name: 'build-all-packs',
  description: 'Build every staged backlog pack end-to-end (vet→extract→outline→scaffold→chapters→verify) and register the passers.',
  phases: [
    { title: 'Build', detail: 'per-pack: prepare → fan-out chapter synthesis → verify (fail-closed)' },
    { title: 'Register', detail: 'update SKILLS/catalog/NOTICE/README/CHANGELOG for passed packs; run release gates' },
  ],
}

const PACKS = (args && args.packsDir) || '/c/Users/gower/OneDrive/Documents/GitHub/jgs-se-knowledge-packs'
const REF = (args && args.refSkillDir) || '/c/Users/gower/OneDrive/Documents/GitHub/jgs-reference-skill'
const PD = 'Public Domain (US Government work)'

// slug -> source identity + the one critical build caveat (full row is in docs/PACK-BACKLOG.md)
const META = {
  'nasa-systems-modeling': { title: 'NASA Systems Modeling Handbook (NASA-HDBK-1009A Rev A)', pub: 'NASA', lic: PD, tier: '1', caveat: 'Tool-agnostic SysML tied to NPR 7123.1; current Rev A (2025).' },
  'faa-sem': { title: 'FAA Systems Engineering Manual v1.0.1', pub: 'FAA', lic: PD, tier: '1', caveat: 'Civil-agency SE process companion to NASA/DAU.' },
  'gao-cost': { title: 'GAO Cost Estimating and Assessment Guide (GAO-20-195G)', pub: 'GAO', lic: PD, tier: '1', caveat: 'Redraw embedded third-party figures; do not reproduce them.' },
  'nasa-ceh': { title: 'NASA Cost Estimating Handbook v4.0', pub: 'NASA', lic: PD, tier: '1', caveat: 'Pairs with nasa-risk.' },
  'gao-schedule': { title: 'GAO Schedule Assessment Guide (GAO-16-89G)', pub: 'GAO', lic: PD, tier: '1', caveat: 'Redraw embedded third-party figures.' },
  'nasa-schedule': { title: 'NASA Schedule Management Handbook (2024 ed)', pub: 'NASA', lic: PD, tier: '1', caveat: 'Use the 2024 edition, not the 2010 SP-2010-3403.' },
  'dod-te-guidebook': { title: 'DoD Test & Evaluation Enterprise Guidebook (Aug 2022)', pub: 'OUSD R&E', lic: PD + '; Distribution A', tier: '1', caveat: 'Headline open T&E source.' },
  'faa-ams-vv': { title: 'FAA AMS Lifecycle V&V Guidelines v3.0', pub: 'FAA', lic: PD, tier: '1', caveat: 'Paraphrase the quoted CMMI v1.2 (SEI) blocks — never verbatim.' },
  'nasa-de-acquisition': { title: 'NASA Digital Engineering Acquisition Framework Handbook (NASA-HDBK-1004)', pub: 'NASA', lic: PD, tier: '1', caveat: 'Pairs with NASA-HDBK-1009A.' },
  'dod-digital-engineering': { title: 'DoD Digital Engineering Strategy (2018)', pub: 'OUSD R&E', lic: PD + '; Distribution A', tier: '1', caveat: 'Build around the 2018 Strategy; exclude CAC-gated DEBoK.' },
  'nasa-se-expanded': { title: 'Expanded Guidance for NASA Systems Engineering (NASA/SP-2016-6105-SUPPL Vols 1-2)', pub: 'NASA', lic: PD, tier: '1', caveat: 'Build as added DEPTH vs nasa-se-handbook; run a redundancy check.' },
  'nasa-rm-standard': { title: 'NASA Reliability and Maintainability Standard (NASA-STD-8729.1A)', pub: 'NASA', lic: PD, tier: '1', caveat: 'Objectives-driven R&M framework.' },
  'faa-rma': { title: 'FAA Reliability, Maintainability, and Availability Handbook (FAA-HDBK-006D)', pub: 'FAA', lic: PD, tier: '1', caveat: 'Use 006D (2020), not 006B.' },
  'nasa-pra': { title: 'Probabilistic Risk Assessment Procedures Guide 2nd ed (NASA/SP-2011-3421)', pub: 'NASA', lic: PD, tier: '1', caveat: 'Deepens nasa-risk with quantitative methods.' },
  'dod-rio': { title: 'DoD Risk, Issue, and Opportunity Management Guide (Sep 2023 +Ch2.2)', pub: 'OUSD R&E', lic: PD + '; Distribution A', tier: '1', caveat: 'DoD-side complement to nasa-risk/dau-se-guidebook.' },
  'nasa-swehb': { title: 'NASA Software Engineering and Assurance Handbook (NASA-HDBK-2203 Ver D)', pub: 'NASA', lic: PD, tier: '1', caveat: 'EXCLUDE IEEE/ISO-reprinted blocks verbatim (precedent: nist-sse).' },
  'gao-agile': { title: 'GAO Agile Assessment Guide (GAO-24-105506)', pub: 'GAO', lic: PD, tier: '1', caveat: 'Exclude embedded copyrighted images.' },
  'dod-mosa': { title: 'MOSA Implementation Guidebook (Feb 2025)', pub: 'OUSD R&E', lic: PD + '; Distribution A', tier: '1', caveat: 'Current authority replacing the 2013 OSA guidebook.' },
  'nist-cps': { title: 'NIST Framework for Cyber-Physical Systems Vols 1-3 (SP 1500-201/202/203)', pub: 'NIST', lic: PD, tier: '1', caveat: 'Bundle as one pack; drop the 2 permission-licensed 3rd-party figures (Beecham/ETSI).' },
  'mil-hdbk-61': { title: 'MIL-HDBK-61B Configuration Management (Change 1, 2025)', pub: 'DoD', lic: PD + '; Distribution A', tier: '1', caveat: 'Use current 61B, not 2001 61A(SE).' },
  'mrl-deskbook': { title: 'Manufacturing Readiness Level (MRL) Deskbook (v2025)', pub: 'OSD ManTech', lic: PD + '; Distribution A', tier: '1', caveat: 'Deepens gao-tra (MRL 1-10).' },
  'nasa-fault-management': { title: 'NASA Fault Management Handbook (NASA-HDBK-1002 Draft 2)', pub: 'NASA', lic: PD, tier: '1', caveat: 'DRAFT — flag draft status prominently in SKILL.md + PACK.yaml notes.' },
  'dod-mq-bok': { title: 'DoD Manufacturing and Quality Body of Knowledge (Jul 2025)', pub: 'OUSD R&E', lic: PD + '; Distribution A', tier: '1', caveat: 'Large (~1,658 pp) — chunk by lifecycle phase.' },
  'faa-hf-std': { title: 'FAA Human Factors Design Standard (HF-STD-001B)', pub: 'FAA', lic: PD, tier: '1', caveat: 'HSI beyond NASA; complements nasa-hsi.' },
  'faa-req-handbook': { title: 'Requirements Engineering Management Handbook (DOT/FAA/AR-08/32)', pub: 'DOT/FAA', lic: PD, tier: '1', caveat: 'Embedded/real-time slant; complements requirements-writing.' },
  'nist-stat-handbook': { title: 'NIST/SEMATECH e-Handbook of Statistical Methods (NIST HB 151)', pub: 'NIST', lic: PD, tier: '1', caveat: 'HTML/web-native per-chapter — different ingestion; watch per-block 3rd-party figures.' },
  'sd-22-dmsms': { title: 'SD-22 DMSMS Guidebook (Apr 2024)', pub: 'DSPO', lic: PD + '; Distribution A', tier: '1', caveat: 'Sustainment/obsolescence.' },
  'grcse': { title: 'Graduate Reference Curriculum for Systems Engineering (GRCSE v1.1)', pub: 'BKCASE / Trustees of the Stevens Institute of Technology', lic: 'CC BY-NC-SA 3.0', tier: '2', caveat: 'Stevens prose ONLY (3rd-party tables are CC BY-NC-ND, exclude); mirror packs/sebok/LICENSE.' },
  'dau-glossary': { title: 'DAU Glossary of Defense Acquisition Acronyms and Terms', pub: 'Defense Acquisition University', lic: PD, tier: '1', caveat: 'Lookup companion to dau-se-guidebook.' },
  'digital-systems-engineering': { title: 'Towards Digital Engineering: The Advent of Digital Systems Engineering (arXiv:2002.11672)', pub: 'arXiv (Old Dominion University)', lic: 'CC BY 4.0', tier: '2', caveat: 'arXiv PDF ONLY (not the paywalled journal version); ~28 pp — thin.' },
  'nist-800-37': { title: 'NIST SP 800-37 Rev 2 (Risk Management Framework)', pub: 'NIST', lic: PD, tier: '1', caveat: 'RMF/security-engineering edge of SE.' },
  'faa-system-safety': { title: 'FAA System Safety Handbook', pub: 'FAA', lic: PD, tier: '1', caveat: 'Use the FAA original; reprint commentary is not PD.' },
}

// Batch to build this run. Set to a slug list, or Object.keys(META) for "all staged".
// (args.slugs is honoured when the runner passes it; pinned here for reliable batching.)
const SLUGS = (args && Array.isArray(args.slugs) && args.slugs.length) ? args.slugs : ['faa-req-handbook', 'sd-22-dmsms']

const PREP_SCHEMA = {
  type: 'object',
  properties: {
    slug: { type: 'string' },
    ok: { type: 'boolean' },
    reason: { type: 'string' },
    source_pages: { type: 'number' },
    full_text_path: { type: 'string' },
    chapters: { type: 'array', items: { type: 'object', properties: {
      file: { type: 'string' }, title: { type: 'string' },
      start_line: { type: 'number' }, end_line: { type: 'number' } },
      required: ['file', 'title', 'start_line', 'end_line'] } },
  },
  required: ['slug', 'ok'],
}
const CH_SCHEMA = { type: 'object', properties: { file: { type: 'string' }, ok: { type: 'boolean' }, note: { type: 'string' } }, required: ['file', 'ok'] }
const GEN_SCHEMA = {
  type: 'object',
  properties: {
    slug: { type: 'string' },
    status: { type: 'string', enum: ['passed', 'needs-fix', 'skipped'] },
    overlap_clean: { type: 'boolean' }, validate_pass: { type: 'boolean' }, eval_pass: { type: 'boolean' },
    chapters: { type: 'number' }, notes: { type: 'string' },
  },
  required: ['slug', 'status'],
}

const prepPrompt = (slug) => {
  const m = META[slug]
  return `Build knowledge pack "${slug}" for the repo at ${PACKS}, PREPARE stage. Use the Bash tool (git-bash, python3) and Read/Write.
Source: "${m.title}" by ${m.pub}; licence "${m.lic}" (tier ${m.tier}). Caveat: ${m.caveat}
Also read the pack's row in ${PACKS}/docs/PACK-BACKLOG.md and the rubric in ${PACKS}/docs/PACK-SPEC.md.

Steps:
1. ls ${PACKS}/sources/${slug}/ — if it has NO source file, STOP and return {slug, ok:false, reason:"no source staged"}.
2. Vet: python3 ${REF}/tools/vet_source.py --title '${m.title}' --publisher '${m.pub}' --license '${m.lic}' --json. If excluded (exit 2), return {ok:false, reason:"excluded by vet"}.
3. Extract the staged SOURCE file(s) — the PDF/HTML directly in sources/${slug}/, NOT the .build/ subdir:
   BOOK_SKILL_WORKDIR=${PACKS}/sources/${slug}/.build python3 ${REF}/scripts/extract.py <the source file(s)> --mode text --install-missing no. Read .build/metadata.json for pages/words. (docling is not installed; text mode uses pdfminer/pdftotext.)
4. Outline: python3 ${REF}/tools/outline.py --source ${PACKS}/sources/${slug}/.build/full_text.txt --out ${PACKS}/sources/${slug}/.build/outline.json. NOTE: outline.json is a HINT only — its heading scan is noisy on irregular docs. Determine the REAL structure by also scanning full_text.txt (grep -n -iE 'chapter|section|^[0-9]+(\\.[0-9]+)? ' and reading the table of contents near the top).
5. Scaffold: python3 ${PACKS}/tooling/build_pack.py --slug ${slug} --title '${m.title}' --publisher '${m.pub}' --version '<from source>' --license '${m.lic}' --tier ${m.tier} (run --help first if unsure of flags). This creates ${PACKS}/packs/${slug}/.
6. Plan 5-9 coherent reference-depth chapters with CORRECT line ranges (merge tiny sections, split huge ones; do not emit a chapter for front-matter/affiliations/references). Use real headings, not the noisy outline titles.
Return {slug, ok:true, source_pages, full_text_path:"${PACKS}/sources/${slug}/.build/full_text.txt", chapters:[{file:"chNN-${slug}-topic.md", title, start_line, end_line}]}. On any tool failure return {ok:false, reason}.`
}

const chapterPrompt = (slug, ftPath, ch) => {
  const m = META[slug]
  return `Write ONE reference-depth chapter for pack "${slug}" (repo ${PACKS}).
Read lines ${ch.start_line}-${ch.end_line} of ${ftPath} (sed -n '${ch.start_line},${ch.end_line}p' or Read offset/limit). Synthesize chapter "${ch.title}".
Structure: # Chapter — title; ## Core Idea; ## Frameworks Introduced (exact source names, when/how); ## Key Concepts; ## Mental Models; ## Anti-patterns (only if the source names them); ## Key Takeaways; ## Connects To.
RULES: ground every claim in this slice; NEVER copy a verbatim run of >8 words from the source — paraphrase; honour the caveat: ${m.caveat}
Write the file to ${PACKS}/packs/${slug}/chapters/${ch.file}. Return {file:"${ch.file}", ok:true}.`
}

const finalizePrompt = (slug, prep) => {
  const m = META[slug]
  return `FINALIZE pack "${slug}" in ${PACKS}/packs/${slug}/ (chapters already written). Use Bash/Read/Write.
1. Write glossary.md, patterns.md, cheatsheet.md (per ${PACKS}/docs/PACK-SPEC.md).
2. Write SKILL.md: frontmatter name:${slug} + a description stating coverage AND scope limits; body order = How to Use; Core Frameworks & Mental Models (~2000 tok); Chapter Index (table linking EVERY chapters/chNN-*.md); Topic Index (alphabetical term→chapter); Supporting Files; Scope & Limits (what the source is thin on; ${m.caveat.includes('DRAFT') ? 'STATE the draft status' : 'source version'}).
3. Complete PACK.yaml TODOs (source_pages=${prep.source_pages || 0}, chapters=<count>, built_on, notes carrying the licence conditions + caveat) and write the source's terms into LICENSE.
4. VERIFY (fail-closed):
   a. python3 ${REF}/tools/check_overlap.py --source ${prep.full_text_path} --pack ${PACKS}/packs/${slug} — if it finds verbatim runs, paraphrase the offending chapters and re-run until clean.
   b. python3 ${PACKS}/tooling/validate_pack.py ${PACKS}/packs/${slug}
   c. python3 ${REF}/tools/pack_eval.py --pack ${PACKS}/packs/${slug}
Return {slug:"${slug}", status: (all three pass ? "passed" : "needs-fix"), overlap_clean, validate_pass, eval_pass, chapters:<count>, notes}.`
}

phase('Build')
const results = await pipeline(
  SLUGS,
  (slug) => agent(prepPrompt(slug), { label: `prep:${slug}`, phase: 'Build', schema: PREP_SCHEMA }),
  async (prep, slug) => {
    if (!prep || !prep.ok) return { slug, status: 'skipped', notes: prep ? prep.reason : 'prep failed' }
    const chs = prep.chapters || []
    await parallel(chs.map(ch => () =>
      agent(chapterPrompt(slug, prep.full_text_path, ch), { label: `ch:${slug}:${ch.file}`, phase: 'Build', schema: CH_SCHEMA })
    ))
    return agent(finalizePrompt(slug, prep), { label: `final:${slug}`, phase: 'Build', schema: GEN_SCHEMA })
  }
)

const built = results.filter(Boolean)
const passed = built.filter(r => r.status === 'passed').map(r => r.slug)
log(`Built+verified ${passed.length}/${SLUGS.length}: ${passed.join(', ') || '(none)'}`)

phase('Register')
let register = null
const skipRegister = !!(args && args.skipRegister)
if (passed.length && !skipRegister) {
  const REG_SCHEMA = { type: 'object', properties: {
    registered: { type: 'array', items: { type: 'string' } },
    release_check: { type: 'string' }, validate_all: { type: 'string' }, version: { type: 'string' }, notes: { type: 'string' } },
    required: ['registered', 'release_check'] }
  register = await agent(
    `Register freshly-built, verified packs into the repo at ${PACKS}. Newly built this run: ${passed.join(', ')}.
FIRST reconcile: list ${PACKS}/packs/, and register EVERY pack directory that is not yet present in catalog.json/SKILLS.md — this includes the new ones above AND any pack from a prior trial (e.g. digital-systems-engineering). Skip kind:signpost packs' special handling per existing convention.
Update, consistently and matching the EXISTING file formats: SKILLS.md (table + count), catalog.json, NOTICE, README.md (pack list + count + version refs), CHANGELOG.md (new dated semver entry listing the added packs — use a MINOR version bump), and bump the version in .claude-plugin/plugin.json + RELEASE-INFO.txt to match. Then run python3 ${PACKS}/tooling/check_release.py and python3 ${PACKS}/tooling/validate_pack.py --all and report both (fix any failures they surface). DO NOT git commit or push — leave everything in the working tree for human review.
Return {registered:[...], release_check:"<summary>", validate_all:"<summary>", version, notes}.`,
    { phase: 'Register', schema: REG_SCHEMA }
  )
}

return { requested: SLUGS.length, passed_count: passed.length, passed, results: built, register }
