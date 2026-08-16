# Phase 7 Research: Gap-Driven Pack Builds (GP-01..GP-07)

**Date:** 2026-08-14. Method: local-docs verification against ROADMAP Phase 7,
`6-GAP_ANALYSIS.md` §Phase 7 Routing (P7-PRE-1..5, P7-FUT-1, P7-BACKLOG),
`6-RESEARCH.md` (source URLs + licence evidence — repeated below by reference where
policy allows; this file is a `.planning` research store, same Link Policy as Phase 6),
`.planning/research/capability-gap-report.md` (cluster targets), `docs/PACK-SPEC.md`,
and the proven Phase 3 pipeline (`3-RESEARCH.md` + `3-01-SUMMARY.md`). Live counts
re-verified on the current tree: `packs/` = 56 dirs, `catalog.json` = 54 packs
(+2 signposts uncounted), `SKILLS.md` header "54 packs (+2 signposts)",
README badge `packs-54`, `.cursor-plugin/plugin.json` skills = **55** (all 56 dirs
except `sebok`, which is deliberately absent from the cursor manifest).

---

## 1. Per-pack build sheets

Common values unless overridden (mirrors Phase 3): `license_tier: 1`,
`commercial_use: true`, `share_alike: false`, `attribution_required: false`.
All seven are US-Government works → Tier 1 via 17 U.S.C. § 105. Phase 3 precedent:
any licence string carrying "Public Domain" / "17 U.S.C." classifies Tier 1 in
`vet_source.py` regardless of publisher, so the statute-bearing strings below are
mechanically sufficient even where the publisher text misses a US_GOV keyword.

**Licence strings** (exact strings to pass to vet/build):

- Default statute string: `Public Domain (US Government work, 17 U.S.C. § 105)`
- DIST-A variant (DoD distribution-controlled copies — GP-01, GP-05, GP-07):
  `Public Domain (US Government work, 17 U.S.C. § 105; Distribution Statement A — Approved for public release; distribution is unlimited)`

| Req | Slug | Title | Publisher | Version / doc ID | Licence string | Source URL (evidence in 6-RESEARCH) | Pages (est.; confirm from extract metadata.json) | Expected chapters | Target clusters |
|---|---|---|---|---|---|---|---|---|---|
| GP-01 | `dod-vva-rpg` | M&S Verification, Validation & Accreditation Recommended Practice Guide | US Department of Defense (OUSW(R&E) CTO / M&S Office) | RPG web edition (no dated rev; record retrieval date) | DIST-A variant | 6-RESEARCH §1c: cto.mil index `https://www.cto.mil/sea/vva_rpg/` → per-chapter PDFs (de-bok.org-hosted links); UCO at `https://www.cto.mil/sea/vva-rpg-uco/` | ~200 selected (many small PDFs; sum metadata.json per chapter set) | 8–10: Key Concepts; core role guides (user / developer / M&S PM / V&V agent / accreditation agent — cluster or select); fidelity; validation; data V&V; risk; T&E/V&V Checklist | 8 Validation, 7 Verification, 16 Decision Analysis, 9 T&E |
| GP-02 | `faa-std-025` | Preparation of Interface Documentation (FAA-STD-025) | Federal Aviation Administration | **rev E (2002-08-09, ROSAP canonical) or rev F (everyspec mirror) — record which in PACK.yaml (P7-PRE-3)** | Default statute | 6-RESEARCH §2a: ROSAP `https://rosap.ntl.bts.gov/view/dot/42955` → `dot_42955_DS1.pdf` (~1.06 MB, rev E); mirror rev F `https://everyspec.com/FAA/FAA-STD/download.php?spec=FAA-STD-025F.003031.pdf` | ~50 | 5–7: purpose/IR-ICD-IRD family definitions; IRD content; ICD content; IR content; change control/CM interface; application examples | 5 Interface Mgmt, 3 Requirements Traceability, 12 CM |
| GP-03 | `dote-te-guidebook` | Test & Evaluation Enterprise Guidebook | US Department of Defense (Director, Operational Test & Evaluation) | **Aug 2022 edition (8.02) preferred; afacpo v3-June (2022-06) fallback — record which in PACK.yaml (P7-PRE-3)** | Default statute | 6-RESEARCH §2b: canonical `https://www.dote.osd.mil/Guidance/` (lists Aug 2022 8.02); DMI mirror `https://www.dmi-ida.org/knowledge-base-detail/test-and-evaluation-enterprise-guidebook` → `.../download-pdf/pdf/TE%20Enterprise%20Guidebook%208.02.pdf`; afacpo fallback (single-encoded URL in 6-RESEARCH §2b — the gap-report double-encoded `%2526E` form 404s) | ~120 | 7–9: T&E enterprise overview/roles; DT&E; OT&E; LFT&E; cybersecurity T&E; MOSA/automated T&E; suitability/reliability growth; planning documents (TEMP/STE) | 9 T&E, 7 Verification, 8 Validation, 23 Logistics |
| GP-04 | `dafman-63-119` | Mission-Oriented Test Readiness Certification (DAFMAN 63-119) | US Department of the Air Force | 15 APR 2021 | Default statute | 6-RESEARCH §2c: `https://static.e-publishing.af.mil/production/1/saf_aq/publication/dafman63-119/dafman63-119.pdf` (403s plain curl — bot protection; rendered/browser fetch works) | ~103 (6-RESEARCH: ~103 pp) | 6–8: MOTRC framework; readiness certification process; DT&E/contractor testing; integration; certification gates/roles; documentation | 9 T&E, 6 Integration, 27 Supplier |
| GP-05 | `mil-std-881f` | Work Breakdown Structures for Defense Materiel Items (MIL-STD-881F) | US Department of Defense | 881F (13 May 2022 per AF/DoD citations; **resolve exact rev date from QuickSearch detail at build** — 6-RESEARCH §1d) | DIST-A variant | 6-RESEARCH §1d: QuickSearch `https://quicksearch.dla.mil/qsdocdetails.aspx?ident_number=36026` (free account/session); GovTribe attachment `https://govtribe.com/file/government-file/b08-attachment-4-mil-std-881f-dot-pdf` (HTML wrapper); everyspec has **only 881E** (fallback, must be labelled with its revision) | ~100–140 | 6–8: WBS principles/definitions; WBS roles/responsibilities; tailoring; element definitions (air systems; ground; sea; space; C3I; services; R&D) — cluster the appendices; WBS numbering/reporting | 17 Technical Planning & WBS, 26 PM/Measurement |
| GP-06 | `federal-bca` | Guidelines and Discount Rates for Benefit-Cost Analysis of Federal Programs (OMB Circular A-94) + US Army Cost Benefit Analysis Guide | US Office of Management and Budget; US Army (ASAFM) | A-94 current + Army CBA Guide current (record both editions in PACK.yaml) | Default statute (per document, at scaffold; single pack licence = statute string) | gap report §2 cluster-15 rows: `https://www.whitehouse.gov/omb/information-for-agencies/circulars/` (A-94); `https://www.asafm.army.mil/Portals/72/Documents/Offices/CE/US%20Army%20Cost%20Benefit%20Analysis.pdf` | ~60 + ~80 (~140 combined; dual-document pack — sum extractions) | 6–8: BCA principles/discounting (A-94); treatment of uncertainty; opportunity cost; Army CBA process steps; cost element structures; sensitivity/risk analysis; reporting | 15 Opportunity/Benefit (worst cluster), 16 Decision Analysis, 17 |
| GP-07 | `mil-std-40051` | Preparation of Digital Technical Information for Page-Based Technical Manuals (MIL-STD-40051-2C) | US Department of Defense (DLA) | MIL-STD-40051-2C, 15 DEC 2015 (record "-2C slice of split family" in PACK.yaml) | DIST-A variant | 6-RESEARCH §1a: everyspec `https://everyspec.com/MIL-STD/MIL-STD-10000-and-Up/MIL-STD-40051-2C_53570/` → `.../download.php?spec=MIL-STD-40051-2C.053570.pdf` (37.7 MB, 1168 page objects — select, don't ingest whole) | ~150 main body selected (file total 1168 pp — most is per-TM format plates) | 5–7: TDP/TM structure; page-based TM format conventions; front matter/back matter requirements; style/format rules; change packages/revision marking; select plate exemplars | 25 Training & Documentation (EMPTY cluster), 24 Ops & Maintenance |

Chapter counts are guidance, not gates (validate_pack.py checks link integrity).
Norm for Tier-1 US-gov packs is 6–8 chapters. Selection pressure: GP-07 (1168 pp
scanned-ish) and GP-05 (appendix-heavy element definitions).

### Per-pack caveats mapped to P7-PRE obligations

| Pack | P7-PRE obligations in force |
|---|---|
| GP-01 `dod-vva-rpg` | **P7-PRE-4**: chapter-wise build; confirm DIST-A / authorship inside **each chapter PDF used**; per-chapter provenance in PACK.yaml. **P7-PRE-5** generic statute-basis confirmation. No consolidated PDF exists (6-RESEARCH §1c) — third-party whole-RPG ZIPs are fallback-only, never canonical. |
| GP-02 `faa-std-025` | **P7-PRE-3** edition recording (rev E canonical vs rev F mirror). **P7-PRE-5**: confirm in-PDF rights statement at build (ROSAP record carries none beyond repository disclaimer). |
| GP-03 `dote-te-guidebook` | **P7-PRE-3** edition recording (8.02 vs v3-June afacpo). **P7-PRE-5**. |
| GP-04 `dafman-63-119` | **P7-PRE-5** — already strong in-source evidence ("no releasability restrictions", quoted 6-RESEARCH §2c); re-confirm in the copy actually downloaded (bot-protected fetch may serve a variant). |
| GP-05 `mil-std-881f` | **P7-PRE-1**: DIST-A **visual** cover confirmation (mirror/attachment fetch). Resolve exact revision date from QuickSearch. If only 881E obtainable, label revision in PACK.yaml. **P7-PRE-5**. |
| GP-06 `federal-bca` | **P7-PRE-2**: dual-document **in-source licence confirmation REQUIRED for BOTH A-94 and Army CBA BEFORE content generation** (lightest evidence trail of the eight — statute basis only, per SOURCE-VETTING.md:135). If either fails the in-source check, drop that document and rescope/descope the pack before generating chapters. |
| GP-07 `mil-std-40051` | **P7-PRE-1**: DIST-A **visual** cover confirmation — the mirror copy's Distribution Statement is a **scanned image**, text layer has only boilerplate. Additionally enforce a **chars/page floor** (~≥200 chars/page avg) before trusting extraction: 37.7 MB / 1168 pp suggests scanned plates; if the body extracts near-empty, OCR fallback per Phase 3 Risk 2 (recorded in PACK.yaml notes). |

Security pass note (P7-PRE-5): the Phase 7 security audit must verify T-6-03
(tampering/evidence-integrity) enforcement across these build-time confirmations
(6-SECURITY_AUDIT N3 names this explicitly).

Slug-collision watch: GP-03 `dote-te-guidebook` is distinct from the existing
`dod-te-guidebook` pack (different source: DOT&E OSD vs DoD-wide). Keep the slugs
distinct and state the relationship in both SKILL.md Scope & Limits sections;
`check_overlap` will also cross-compare. Also note `nasa-npr-7150` already exists —
if GP-08 is ever revived as NPR 7150.2 + NASA-STD-8739.8, NPR 7150.2 is already
covered and must not be rebuilt.

---

## 2. Pipeline command sequence (per pack)

Copy of the proven Phase 3 sequence (`3-RESEARCH.md` §2), reused verbatim except the
deltas noted after. CWD = jgs-se-knowledge-packs; `$REF` =
`C:/Users/gower/OneDrive/Documents/GitHub/jgs-reference-skill`; Windows/Git Bash:
use `python`.

```bash
REF="C:/Users/gower/OneDrive/Documents/GitHub/jgs-reference-skill"
SLUG=<slug>                             # per build sheet §1
mkdir -p sources/$SLUG                  # gitignored — build inputs only

# 1. Download source PDF(s) into sources/$SLUG/   (URL per §1 build sheet)
# 2. VET FIRST (exit 2 = Excluded — must not happen):
python "$REF/tools/vet_source.py" \
    --title "<title>" --publisher "<publisher>" --license "<licence string §1>"
# Expect: tier 1, exit 0. DoD/Army publishers may emit the advisory
# third-party-quote warning — expected, not a blocker.
# 3. EXTRACT:
python "$REF/scripts/extract.py" sources/$SLUG/*.pdf --mode technical --install-missing no
#    (no: non-interactive; docling absent → pdftotext fallback, Phase 3 deviation #1)
# 4. OUTLINE:
python "$REF/tools/outline.py" \
    --source "$TMP/book_skill_work/full_text.txt" --out sources/$SLUG/outline.json
# 5. SCAFFOLD:
python "$REF/tools/build_pack.py" \
    --slug $SLUG --title "<title>" --publisher "<publisher>" \
    --version "<version>" --license "<licence string §1>" --out-dir packs
# 6. GENERATE chapters/glossary/patterns/cheatsheet/SKILL.md from outline slices;
#    fill PACK.yaml TODOs (source_pages, chapters, built_on, notes); complete LICENSE
# 7. VALIDATE:   python tooling/validate_pack.py packs/$SLUG
# 8. SCAN:       python "$REF/tools/scan_generated_skill.py" packs/$SLUG
# 9. OVERLAP:    python "$REF/tools/check_overlap.py" \
#       --source "$TMP/book_skill_work/full_text.txt" --pack packs/$SLUG
# (bonus)        python "$REF/tools/pack_eval.py" --pack packs/$SLUG
```

Per-pack work_dir handling (Phase 3 pattern): copy `book_skill_work` under
`sources/<slug>/` between packs so %TEMP% is not clobbered; record paths in
`work_dir.txt` (write `printf '%s'`, read `tr -d '\r\n'`); dual-doc packs use
`work_dir_main.txt` / `work_dir_ctrl.txt` (cisa-cpg precedent). Per-pack commit:
one scoped commit per pack; `git show --name-only <sha>` to prove zero `sources/`
or `full_text.txt` leakage (MN-01 pattern). Pages for PACK.yaml come from
`metadata.json` (sum across extractions for GP-01/GP-06), not PDF page-object counts.

**Phase 7 deltas on the Phase 3 sequence:**

1. **GP-01 (dod-vva-rpg) — chapter-wise web source.** No single PDF. Download the
   selected chapter PDFs individually from the cto.mil index (core role guides,
   fidelity, validation, data V&V, risk special topics, T&E/V&V checklist — the
   6-RESEARCH §1c list). VET runs once on the guide title; each chapter PDF gets an
   extract + in-PDF DIST-A/authorship check (P7-PRE-4); `source_pages` = sum of the
   per-chapter metadata.json page counts; PACK.yaml `notes` records the chapter set
   with per-chapter provenance (titles + edition/retrieval date — no URLs, Link
   Policy). outline.py is per-chapter meaningless — derive the outline from the
   chapter set directly; synthesis slices are per-chapter full_texts.
2. **GP-07 (mil-std-40051) — 37.7 MB scanned-ish PDF.** Before trusting extraction:
   visual DIST-A cover check (P7-PRE-1, image statement) + compute avg chars/page
   from metadata.json (pages vs words); floor ~200 chars/page. If the main body is
   image-only → OCR fallback (`ocrmypdf` then re-extract `--mode text`), recorded in
   PACK.yaml notes and the deviation log (Phase 3 Risk 2 pattern). Do not attempt
   the 1168-page ingest whole: extract, then select ~150 pp of main body via
   outline/manual offsets; skip the per-TM format plates.
3. **GP-05 (mil-std-881F) — gated/mirror fetch.** Try QuickSearch detail page
   `ident_number=36026` first (resolve the exact revision date while there);
   direct PDF needs free account/session — if blocked, use the GovTribe attachment
   (HTML download wrapper) or, last resort, everyspec 881E labelled with its
   revision. Whichever copy: visual DIST-A in-copy check (P7-PRE-1).
4. **GP-06 (federal-bca) — dual-source.** Two vet runs (one per document) and two
   extracts (`work_dir_main.txt`/`work_dir_ctrl.txt`, cisa-cpg precedent);
   **both in-source licence checks must pass BEFORE any chapter generation**
   (P7-PRE-2 hard gate). Overlap check against both full_texts; `source_pages` = sum.
5. **GP-04 (dafman-63-119) — bot-protected host.** Plain curl gets 403; use a
   rendered/browser fetch (or browser-UA + cookie jar) to retrieve the PDF, then
   proceed offline. Re-confirm the releasability line in the downloaded copy.
6. **GP-03 (dote-te-guidebook) — dote.osd.mil may be page-not-file.** If no direct
   PDF link is obtainable from the Guidance page in-session, use the DMI/IDA mirror
   download or the afacpo single-encoded URL (6-RESEARCH §2b). Record the edition
   actually built (P7-PRE-3).

---

## 3. Risk-batched wave recommendation

Three waves, risk-homogeneous (mirrors Phase 3 batching; one plan per wave, one
scoped commit per pack; a consolidated registration sweep closes the phase).

- **Wave A — born-digital direct PDFs (lowest risk; build first, proves P7-PRE-2/3
  handling on friendly sources):** `faa-std-025` (GP-02), `dote-te-guidebook` (GP-03),
  `dafman-63-119` (GP-04), `federal-bca` (GP-06). All small-to-medium born-digital
  PDFs with confirmed-live URLs. GP-06 carries the P7-PRE-2 dual in-source licence
  gate; GP-02/GP-03 carry P7-PRE-3 edition recording. GP-04 needs the rendered-fetch
  workaround only.
- **Wave B — DoD mirror/spec fetches (download + scanned-copy risk):** `mil-std-881f`
  (GP-05), `mil-std-40051` (GP-07). Both carry P7-PRE-1 visual DIST-A obligations;
  40051 adds the chars/page floor and possible OCR fallback; 881F adds gated-download
  contingency (QuickSearch → GovTribe → 881E-labelled fallback).
- **Wave C — chapter-wise web source + registration sweep:** `dod-vva-rpg` (GP-01;
  P7-PRE-4 per-chapter DIST-A/authorship + per-chapter provenance), then the
  consolidated registration sweep (Section 4) + `check_release.py` PASS + SUMMARY.

Rationale: identical pipeline ~90% across packs; wave A failures cannot block wave B;
GP-01's bespoke build model is isolated last; registration is one sweep (Phase 3 3-03
precedent) rather than per-pack edits.

---

## 4. Registration deltas (exact expected counts)

Current live basis (re-verified): 56 pack dirs (54 catalog + 2 signposts), catalog 54,
SKILLS.md "54 packs (+2 signposts)", README badge `packs-54`,
`.cursor-plugin/plugin.json` 55 skill entries (56 dirs minus `sebok`, which is
intentionally absent from the cursor manifest).

After Wave C registration of all 7 GP packs (all Tier 1, so unlike `sebok` every one
ships in the cursor manifest):

| Surface | Before | After | Delta |
|---|---|---|---|
| `packs/` directories | 56 | **63** | +7 |
| `catalog.json` packs (gate catalog basis) | 54 | **61** | +7 (54+7) |
| Signposts | 2 | **2** (unchanged) | 0 |
| `SKILLS.md` header count | 54 (+2 signposts) | **61 packs (+2 signposts)** | +7 rows, header +7 |
| `README.md` badge / pack count | 54 | **61** (`packs-61`) | +7; also 7 new table rows |
| `.cursor-plugin/plugin.json` skills | 55 | **62** (55+7) | +7 entries (sebok still excluded) |
| `docs/packs.html` | regenerated | regenerated | via `python tooling/gen_packs_page.py` (never hand-edit; RR-B-30 freshness) |
| `NOTICE` | n/a | +7 `[pack: <slug>]` Public Domain attribution blocks | — |

Gate expectation: `python tooling/check_release.py` PASS on the 61-catalog /
63-directory basis. Registration mechanics per 3-RESEARCH §4: catalog objects hand-added
(license_tier: 1, commercial_use: true, status "live", actual chapter counts); SKILLS.md
hand-edited (no gen_skills_index.py exists) keeping the generated-file disclaimer;
NOTICE blocks mirror the existing Public Domain entries. Note: full version-surface
bump (CHANGELOG, plugin versions 1.17.0→1.18.0, RELEASE-INFO, etc.) is Phase 9's
release-surface scope, not Wave C's — Wave C registers packs only.

---

## 5. Cluster-fattening verification plan (captured for Phase 8)

Phase 8 regenerates `docs/capability-pack-map.json` and re-scores; Phase 7 only needs
to (a) build against these target clusters and (b) capture the baseline for later
assertion. Baseline (gap report §1, authoritative): 570 entries / 32 clusters;
1 EMPTY (25) / 15 THIN / 16 ADEQUATE.

| Pack | Baseline clusters targeted (entries / distinct packs before) | Post-build expectation (Phase 8 asserts) |
|---|---|---|
| GP-01 `dod-vva-rpg` | 8 (3/2 THIN), 7 (9/2), 16 (2/2 THIN), 9 (11/1) | 8 becomes count-adequate; 16 fattened; 9 diversity fixed (2nd+ pack); 7 diversity improved |
| GP-02 `faa-std-025` | 5 (2/2 THIN), 3 (2/2 THIN), 12 (14/5) | 5 and 3 fattened (THIN-count exit requires ≥8 entries — partial; record actuals) |
| GP-03 `dote-te-guidebook` | 9 (11/1 single-source), 7, 8, 23 (11/1) | 9 and 23 single-source risk broken; 7/8 strengthened |
| GP-04 `dafman-63-119` | 9, 6 (3/3 THIN), 27 (7/6 THIN) | 6 and 27 fattened; 9 diversity |
| GP-05 `mil-std-881f` | 17 (6/5 THIN), 26 (66/11) | 17 fattened toward ≥8 |
| GP-06 `federal-bca` | 15 (1/1 worst), 16, 17 | 15 no longer worst/1-pack; 16/17 fattened |
| GP-07 `mil-std-40051` | 25 (0/0 **EMPTY**), 24 (6/4 THIN) | **25 non-empty** (ROADMAP Phase 8 SC-2 hard requirement); 24 fattened |

Phase 8 success criteria already encoded in ROADMAP: cluster 25 non-empty; clusters
3/5/15 above critical thresholds; map carries schema+version+generated-on and
regenerates idempotently. Phase 7 plan should copy the table above into the plan's
verify section as the per-pack cluster-target record, and each pack's SKILL.md topic
index should be written with these cluster vocabularies in mind (that is what the map
harvests).

---

## 6. Top risks

1. **GP-07 extraction quality** — 37.7 MB / 1168 pp, scanned cover, suspected partial
   image content. Mitigation: chars/page floor, visual DIST-A check, OCR fallback,
   hard page-selection (~150 pp main body). Highest single-pack failure risk.
2. **GP-05 access path** — QuickSearch session-gated; GovTribe wrapper; everyspec has
   only 881E. Mitigation: fallback chain with revision labelling; 881E is still Tier 1
   if labelled.
3. **GP-06 P7-PRE-2 hard gate** — lightest licence evidence; if either in-source check
   fails, the pack must be rescoped (single doc) or descoped before generation, not
   built on statute basis alone.
4. **GP-01 build-model novelty** — per-chapter downloads, per-chapter licence checks,
   per-chapter provenance; no outline spine. Mitigation: fix the chapter set from
   6-RESEARCH §1c up front; treat each chapter as a mini-extract.
5. **Slug adjacency** — `dote-te-guidebook` vs existing `dod-te-guidebook`; keep both
   distinct, cross-reference in Scope & Limits, rely on check_overlap.
6. **Windows/TEMP quirks** — book_skill_work tempdir path capture, work_dir.txt
   convention (Phase 3 MN-05 pattern) — already proven; reuse.

---

_Researcher: ZCode (Phase 7 research). Counts verified live against catalog.json,
packs/, SKILLS.md, README.md, .cursor-plugin/plugin.json; obligations from
6-GAP_ANALYSIS.md §Phase 7 Routing; URLs and licence evidence from 6-RESEARCH.md._
