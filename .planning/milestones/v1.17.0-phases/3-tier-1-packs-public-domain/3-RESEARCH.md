# Phase 3 Research: Tier-1 Packs (Public Domain)

Date: 2026-08-14. Method: local-docs verification (ROADMAP Phase 3, 2-RESEARCH.md,
2-GAP_ANALYSIS.md P3-PRE-1/P3-PRE-2, docs/PACK-SPEC.md, CONTRIBUTING.md,
tooling/build_pack.py --help, jgs-reference-skill README + SKILL.md + tools/ CLI
helps, existing packs, catalog.json, SKILLS.md, NOTICE). No WebFetch needed — every
command/flag was resolved from local docs.

**Key confirmations**

- All 8 Tier-1 candidates verified in 2-RESEARCH.md; source URLs by reference there
  (Link Policy: this file repeats none).
- `sources/` **is gitignored** (`.gitignore`: "Staged SOURCE material ... never
  redistribute/commit them") — downloads go to `sources/<slug>/`. Precedent:
  `sources/` already holds per-source subfolders from backlog builds (sebok,
  mil-hdbk-61, nasa-pra, ...). Also gitignored: `**/.build/` and `*.full_text.txt`
  (raw extracted text never committed).
- **P3-PRE-1 confirmed against code.** `vet_source.py` US_GOV signals = (nasa,
  nist, department of defense, dod, ousd, faa, gao, "u.s. ", us government,
  "u.s. government", federal aviation, "department of ", army, navy, air force,
  defense acquisition). No `cisa` (nor `energy`/`doe` — but "Department of Energy"
  matches the generic `"department of "` signal). PD_LICENSE includes `"public
  domain"`, `"17 u.s.c"`, `"us government work"`, `"distribution statement a"` — so
  **any licence string carrying "Public Domain" or "17 U.S.C." classifies Tier 1
  regardless of publisher**. Fix: give every pack the statute-bearing licence string
  (below), which satisfies P3-PRE-1 mechanically for cisa-cpg.
- Note: vet_source.py tier-1 branch appends a third-party-quote warning for
  nist/dod/ousd publishers — expected, advisory only, exit 0.

---

## 1. Per-pack build sheets

Common values unless overridden: `license_tier: 1`, `commercial_use: true`,
`share_alike: false`, `attribution_required: false` (PD; attribution is courtesy).

**Licence strings** (exact strings to pass to vet/build):

- Default: `Public Domain (US Government work, 17 U.S.C. § 105)`
- DoD handbooks (T1-03, T1-04): `Public Domain (US Government work, 17 U.S.C. § 105; Distribution Statement A — Approved for public release; distribution is unlimited)`
- **cisa-cpg (P3-PRE-1, mandatory)**: `Public Domain (US Government work, 17 U.S.C. § 105)` — publisher "CISA" hits no US_GOV signal, so the statute-bearing string is what classifies it Tier 1. Do NOT pass a bare "CISA performance goals" style licence.

| Req | Slug | Title | Publisher | Version / doc ID | Licence string | Source URL (in 2-RESEARCH.md) | Pages (est., confirm from PDF) | Expected chapters |
|---|---|---|---|---|---|---|---|---|
| T1-01 | `nist-800-171` | Protecting Controlled Unclassified Information in Nonfederal Systems and Organizations (NIST SP 800-171 Rev. 3) | NIST | Rev. 3, final 2024-05-14 (DOI 10.6028/NIST.SP.800-171r3) | default | 2-RESEARCH §1 (csrc.nist.gov/pubs/sp/800/171/r3/final → nvlpubs PDF) | ~111 | 6–8 (3.1–3.14 control families → group into ~8: AC/IA/AT/PR family chapters + assessment + glossary slices) |
| T1-02 | `nist-800-61` | Incident Response Recommendations and Considerations for Cybersecurity Risk Management (NIST SP 800-61 Rev. 3) | NIST | Rev. 3, final 2025-04-03 (DOI 10.6028/NIST.SP.800-61r3) | default | 2-RESEARCH §2 (csrc 800/61/r3/final → nvlpubs) | ~68 | 5–7 (IR lifecycle phases, comms, training, coordination, lessons learned) |
| T1-03 | `mil-hdbk-338` | DoD Electronic Reliability Design Handbook (MIL-HDBK-338B) | US Department of Defense | MIL-HDBK-338B, 1 Oct 1998 (Notice 2, 2007) | Distribution Statement A variant | 2-RESEARCH §3 (DLA quicksearch ident 54022; PDF mirror at nde-ed.org) | ~716 | 8–10 (SELECT — reliability prediction, derating, MTBF/MTTR, FMECA/FTA overlap, growth testing, testability, physics of failure; skip the 400 pp of annex tables) |
| T1-04 | `mil-hdbk-516` | DoD Airworthiness Certification Criteria (MIL-HDBK-516C) | US Department of Defense | 516C, 12 Dec 2014 (Change 1, 2016) | Distribution Statement A variant | 2-RESEARCH §4 (DLA quicksearch; DLA-hosted PDF, text begins "DISTRIBUTION STATEMENT A") | ~320 | 6–8 (airworthiness process, tailoring, one chapter per functional area cluster: systems engineering, structures, flight, propulsion, avionics/EW, system software, crew sys) |
| T1-05 | `nasa-ms-7009` | NASA Standard for Models and Simulations (NASA-STD-7009B with NASA-HDBK-7009B) | NASA | STD-7009B approved 2024-03-05 + HDBK-7009B (2026-02-03) | default | 2-RESEARCH §5 (standards.nasa.gov/standard/NASA/NASA-STD-7009 and /NASA-HDBK-7009) | STD ~30 + HDBK 100+ (extract both, build one pack) | 6–8 (M&S credibility facets, verification/validation/uncertainty, the 43 mandatory requirements grouped, HDBK implementation guidance) |
| T1-06 | `doe-413-3b` | Program and Project Management for the Acquisition of Capital Assets (DOE O 413.3B, Chg 7) | US Department of Energy | O 413.3B Chg 7 (LtdChg), 2023-06-21 | default | 2-RESEARCH §6 (energy.gov/management/directives-library entry — old deep link 404s; use consolidated Chg 7 PDF) | ~100+ | 5–7 (CD-0..CD-5 milestone chapters, acquisition planning, budget/cost, risk, emergency procurement exceptions) |
| T1-07 | `cisa-cpg` | Cross-Sector Cybersecurity Performance Goals 2.0 (CISA CPG 2.0) | CISA | CPG 2.0 (2024–25 refresh, aligned to NIST CSF 2.0 incl. GOVERN) | **statute-bearing string (P3-PRE-1)** | 2-RESEARCH §7 (cisa.gov CPG 2.0 landing + /sites/default/files/publications/ controls PDF) | ~40 (main report) + controls list | 4–6 (GOVERN/Identify/Protect/Detect/Respond groupings, IT vs OT goals, implementation/defining-objectives) |
| T1-08 | `doe-sem` | Systems Engineering Methodology (SEM version 3) | US Department of Energy | SEM3 (SEM3_1231.pdf) | default | 2-RESEARCH §8 (energy.gov/sites/prod/files/cioprod/documents/SEM3_1231.pdf — live, confirmed application/pdf) | unknown ("substantial" — confirm at build) | 6–8 (SEM lifecycle phases, core methodology elements, technical reviews, artifacts) |

Chapter counts are guidance, not gates — validate_pack.py checks link integrity,
not counts. Existing pack precedent: 6–8 chapters is the norm for Tier-1 US-gov
packs (faa-rma: 8, nasa-pra: 8, nasa-se-expanded: 6). Only mil-hdbk-338 needs
aggressive selection (716 pp).

---

## 2. Pipeline command sequence (per pack)

All commands run with CWD = jgs-se-knowledge-packs unless noted. Reference-skill
repo path: `C:/Users/gower/OneDrive/Documents/GitHub/jgs-reference-skill` (referred
to below as `$REF`). On Windows/Git Bash use `python` not `python3`.

```bash
REF="C:/Users/gower/OneDrive/Documents/GitHub/jgs-reference-skill"
SLUG=nist-800-171                      # per build sheet
mkdir -p sources/$SLUG                 # gitignored — build inputs only

# 1. Download source PDF(s) into sources/$SLUG/
#    (curl/powershell Invoke-WebRequest; URL per 2-RESEARCH.md build sheet)

# 2. VET FIRST (gate; exit 2 = Excluded, must not happen for these 8).
#    Pass the licence string from the build sheet — for cisa-cpg it MUST carry
#    the statute text (P3-PRE-1), else the tool mis-classifies Tier 3.
python "$REF/tools/vet_source.py" \
    --title "<title from build sheet>" \
    --publisher "<publisher>" \
    --license "<licence string from build sheet>"
# Expect: tier 1, exit 0. NIST/DoD publishers also emit an advisory
# third-party-quote warning — expected, not a blocker.

# 3. EXTRACT (structure-aware for standards/handbooks)
python "$REF/scripts/extract.py" sources/$SLUG/*.pdf --mode technical --install-missing ask
# Output: <tempdir>/book_skill_work/{full_text.txt, metadata.json}
# (On Windows the tempdir is under %TEMP% — check tool output for the exact path.)
# NOTE: if extraction aborts as a scanned/image PDF, see Risks (OCR fallback).

# 4. OUTLINE (deterministic offsets)
python "$REF/tools/outline.py" \
    --source "$TMP/book_skill_work/full_text.txt" --out sources/$SLUG/outline.json
# (outline.json inside gitignored sources/ is fine — build input, never committed)

# 5. SCAFFOLD with provenance (re-runs the vet gate internally)
python "$REF/tools/build_pack.py" \
    --slug $SLUG --title "<title>" --publisher "<publisher>" \
    --version "<version>" --license "<licence string>" \
    --out-dir packs
# Equivalently, the repo-local wrapper works too:
#   python tooling/build_pack.py --slug ... --license ... --tier 1 --commercial-use true
# (repo-local build_pack.py has no --out-dir; it targets ./packs — same place.)

# 6. GENERATE (agent-driven, per docs/PACK-SPEC.md + reference-skill SKILL.md Steps 6-9):
#    For each outline.json section selected in the build sheet: read the
#    start_char/end_char slice of full_text.txt, write chapters/chNN-<slug>.md with
#    the reference-depth structure (Core Idea / Frameworks Introduced / Key Concepts
#    / Mental Models / Anti-patterns / Key Takeaways / Connects To). Then
#    glossary.md, patterns.md, cheatsheet.md, and SKILL.md (frontmatter + How to Use
#    + Core Frameworks + Chapter Index + Topic Index + Scope & Limits). Fill PACK.yaml
#    TODOs (source_pages, chapters, built_on, notes) and complete LICENSE with the
#    source's terms (statute / Distribution Statement A text).

# 7. VALIDATE (structural gate — repo tooling)
python tooling/validate_pack.py packs/$SLUG

# 8. SCAN (advisory, Phase 3 SC2)
python "$REF/tools/scan_generated_skill.py" packs/$SLUG
# Review any findings; document disposition per pack.

# 9. OVERLAP (licence-safety gate; exit 3 = verbatim runs found, must be fixed)
python "$REF/tools/check_overlap.py" \
    --source "$TMP/book_skill_work/full_text.txt" --pack packs/$SLUG

# (Reference-skill also has pack_eval.py — topic-index grounding; run it as a bonus:)
python "$REF/tools/pack_eval.py" --pack packs/$SLUG
```

Order note: vet before scaffold (build_pack re-runs the gate anyway, but running it
standalone first gives a clean verdict record); overlap after generation; validate
can run repeatedly during generation.

---

## 3. Source downloads and page counts

- **Location:** `sources/<slug>/` — gitignored (confirmed in `.gitignore`: "Staged
  SOURCE material ... never redistribute/commit"). Raw extracted text is
  additionally excluded by `**/.build/` and `*.full_text.txt`. Never move PDFs or
  full_text.txt into `packs/` or tracked paths.
- **Page count for PACK.yaml `source_pages`:** extract.py writes
  `book_skill_work/metadata.json` with pages/words/tokens (per reference-skill
  SKILL.md Step 2). Use `metadata.json`'s page count; if absent for a multi-PDF pack
  (nasa-ms-7009: STD + HDBK), sum the two extractions. Cross-check against the
  build-sheet estimate and record the actual number.

---

## 4. Registration steps (per pack, after gates pass)

1. **catalog.json**: add a pack object to `packs[]` mirroring the existing shape
   (slug, title, publisher, source_version, license, license_tier: 1,
   commercial_use: true, chapters, status: "live"); bump `updated`. Hand-edit is
   the documented route (CONTRIBUTING: "Add a catalog row and rebuild catalog.json").
2. **SKILLS.md**: add a table row (`| [slug](packs/<slug>/SKILL.md) | Public Domain
   (US Gov) | <description incl. scope limits> |`) and bump the header count.
   Header says "Regenerate with tooling/gen_skills_index.py" but that script does
   not exist in this repo's tooling/ — hand-edit, keeping the generated-file
   disclaimer intact.
3. **docs/packs.html**: generated — DO NOT hand-edit. Re-run
   `python tooling/gen_packs_page.py` (check_release.py RR-B-30 verifies it is
   fresh; it parses SKILLS.md).
4. **NOTICE**: add one `[pack: <slug>]` attribution block per shipped pack (Source /
   Author / Licence / Changes / Terms) — Tier-1 blocks mirror the existing
   "Public Domain (US Government work)" entries.
5. Final sweep: `python tooling/check_release.py` → PASS (includes catalog/packs.html
   consistency); this is the Phase 5 gate basis: 54 packs on the catalog basis
   (48 + 8 new − 2 signposts) / 56 directory basis.

---

## 5. Recommended task batching

**Recommendation: 3 batches of grouped plans, one plan per batch — not one plan
per pack, and not one plan for all 8.**

- **Batch A (4 plans-worth of NIST/CISA PDFs, smallest risk):** nist-800-171,
  nist-800-61, cisa-cpg, doe-sem — all small-to-medium born-digital PDFs from
  stable agency sites. One plan, one execution subagent per pack or sequential.
  Include the P3-PRE-1 licence-string rule and P3-PRE-2 disposition in this plan
  (they're one-time preconditions, proven on the first build).
- **Batch B (DoD handbooks):** mil-hdbk-338, mil-hdbk-516 — Distribution Statement A
  licence handling, DLA/mirror download risk, large-PDF chapter selection. Same
  pipeline; isolates the download/mirror risk to one plan.
- **Batch C (multi-document + order):** nasa-ms-7009 (two PDFs, one pack), doe-413-3b
  (consolidated Chg 7 PDF from directives library). One plan.

Rationale: the 8 builds share one deterministic pipeline (~90% identical commands);
per-pack plans would repeat identical scaffolding 8 times. But a single monolithic
plan risks a 716-page MIL-HDBK-338 extraction problem blocking the seven easy packs.
Three risk-homogeneous batches is the laziest safe split: one template plan body,
reused; failures contained per batch; a final registration sweep (Section 4 +
check_release.py) as a small closing task in Batch C or a standalone Phase 5-prep
commit. CONTRIBUTING's "one pack per PR" stays satisfiable: batch = plan, commits
still per-pack.

---

## 6. Risks and mitigations

1. **Large PDF — MIL-HDBK-338B (~716 pp, task said ~1000; DLA record says ~716).**
   Extraction is slow but fine; the real risk is chapter sprawl. Mitigation:
   build-sheet selection (8–10 chapters from Part 2 design guidance; skip annex
   tables), slice via outline.json offsets, never load full_text.txt whole
   (>50k-token rule from reference-skill SKILL.md Step 3).
2. **Scanned/image PDFs → extraction abort.** Older DoD scans may be image-only.
   Mitigation: extract first (Batch B early); if it aborts, OCR fallback (e.g.
   `ocrmypdf` then re-extract in `--mode text`), and record the OCR step in
   PACK.yaml `notes` + the deviation log. Do not hand-type content.
3. **DLA ASSIST/QuickSearch token-gated downloads** (MIL-HDBK-516C's direct PDF
   needs a session token). Mitigations in order: (a) the DLA record page and its
   "View Document" from a fresh browser session sometimes works; (b) use the
   verified mirrors already recorded in 2-RESEARCH.md (338B at nde-ed.org;
   516C text/Distribution Statement already quoted from the DLA-hosted copy);
   (c) other public .mil / university mirrors — verify the Distribution Statement A
   page in the mirrored copy before use.
4. **NIST PDF URL patterns.** Do not scrape the csrc.nist.gov pubs page; the final
   PDFs live at nvlpubs.nist.gov with the DOI-stable form
   `https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-171r3.pdf`
   (same pattern for SP 800-61r3). Use the DOI-stable nvlpubs URL directly.
5. **cisa-cpg mis-tiering (P3-PRE-1).** Mitigated by the statute-bearing licence
   string (§1); verified against vet_source.py source. Also watch for third-party
   logos/content in CISA PDFs — synthesize only CISA-authored content.
6. **doe-sem page count unknown + DOE PDF could not be machine-read by Phase 2
   tooling.** Mitigation: first build step is extract + metadata.json; confirm no
   third-party copyright notice inside the PDF before generation (2-RESEARCH
   requirement). Same in-PDF confirmation applies to DOE O 413.3B.
7. **nasa-ms-7009 two-document pack.** Two extractions, one outline each; pick one
   primary chapter spine (STD's 43 requirements) with HDBK slices as depth
   chapters; `source_pages` = sum. standards.nasa.gov PDFs sit behind
   `system/files/tmp/` style paths — download promptly (tmp-prefixed paths may be
   re-generated on publish).
8. **Windows quirks.** Use `python` (not `python3`); extract.py already forces
   UTF-8 streams; the book_skill_work tempdir is under %TEMP% — capture the exact
   printed path before running outline/overlap.
9. **No source URLs anywhere in packs/catalog** (PACK-SPEC no-source-link policy;
   CI link-policy step). Source identity is title+publisher+version only; URL
   evidence lives in 2-RESEARCH.md (.planning, now CI-exempt per G-1 fix).

---

## 7. Precondition dispositions to encode in the Phase 3 plan

- **P3-PRE-1 (must):** cisa-cpg vet/build invocations use
  `--license "Public Domain (US Government work, 17 U.S.C. § 105)"`. Verified
  sufficient: PD_LICENSE contains "public domain" and "17 u.s.c".
- **P3-PRE-2 (should):** either add `ecss`/`esa` (and consider `def stan`/`dstan`)
  to vet_source.py EXCLUDED signals in the external jgs-reference-skill repo + sync
  its companion rubric, or record the accepted gap in the Phase 3 plan ("human
  rubric governs; tool under-blocks; none of the affected sources appear in Phase 3
  build lists"). Recommend: record the accepted gap now (no Phase 3 build depends on
  it); schedule the external-repo change as follow-up.

---

_Researcher: ZCode (Phase 3 research). All commands verified against local CLI helps;
licence-string sufficiency verified against vet_source.py source._
