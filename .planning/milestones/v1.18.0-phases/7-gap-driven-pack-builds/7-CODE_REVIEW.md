---
phase: 7-gap-driven-pack-builds
review: code
scope: "7 GP packs (faa-std-025, dote-te-guidebook, dafman-63-119, federal-bca, mil-std-881f, mil-std-40051, dod-vva-rpg) + registration e00ac7d; commit range f7d7d81..e00ac7d"
reviewed: 2026-08-14
depth: deep
files_reviewed: 85
files_reviewed_list:
  - packs/faa-std-025/** (SKILL.md, PACK.yaml, LICENSE, chapters/ch01-06, glossary.md, patterns.md, cheatsheet.md)
  - packs/dote-te-guidebook/** (SKILL.md, PACK.yaml, LICENSE, chapters/ch01-08, glossary.md, patterns.md, cheatsheet.md)
  - packs/dafman-63-119/** (SKILL.md, PACK.yaml, LICENSE, chapters/ch01-07, glossary.md, patterns.md, cheatsheet.md)
  - packs/federal-bca/** (SKILL.md, PACK.yaml, LICENSE, chapters/ch01-06, glossary.md, patterns.md, cheatsheet.md)
  - packs/mil-std-881f/** (SKILL.md, PACK.yaml, LICENSE, chapters/ch01-07, glossary.md, patterns.md, cheatsheet.md)
  - packs/mil-std-40051/** (SKILL.md, PACK.yaml, LICENSE, chapters/ch01-08, glossary.md, patterns.md, cheatsheet.md)
  - packs/dod-vva-rpg/** (SKILL.md, PACK.yaml, LICENSE, chapters/ch01-10, glossary.md, patterns.md, cheatsheet.md)
  - catalog.json
  - .cursor-plugin/plugin.json
  - SKILLS.md
  - README.md
  - NOTICE
  - docs/packs.html
findings:
  blocker: 0
  major: 1
  minor: 3
  info: 3
  total: 7
status: issues_found
---

# Phase 7: Code Review — Gap-Driven Pack Builds

**Verdict:** PASS_WITH_NOTES

**Reviewed:** 2026-08-14 (depth: deep — per-file plus cross-file verification against gitignored `sources/` build evidence)
**Scope:** 7 new GP packs + registration commit `e00ac7d` (build range `bab559d..e00ac7d`)
**Files Reviewed:** 85 pack/registration files; claims cross-checked against `sources/*/book_skill_work/` extractions

## Summary

All mechanical gates pass fresh: `validate_pack.py` 7/7 PASS, `check_release.py` PASS. Registration counts are exact and semantically clean: catalog.json 61 packs / cursor 62 / packs/ 63 dirs / SKILLS.md "61 packs (+2 signposts)" / README badge packs-61 / NOTICE `[pack:]` blocks x7 / `catalog.updated` 2026-08-16; data-level diff of `e00ac7d` catalog.json shows exactly 7 entries added, 0 existing entries modified or removed (the ~1305-line textual churn is re-serialization only). No source-material URLs in any shipped pack file; `sources/` gitignored; every pack commit scoped to pack paths only.

Adversarial fact-checks against the local build evidence **confirm** the load-bearing claims rather than refuting them:

- 881F appendix mapping (A Aircraft / B Electronics / C Missile-Ordnance / D Strategic / E Sea / F Space / G Ground / H Unmanned Maritime / I Launch / J IS-DBS / K Common / L Sustainment / M Gov ST&E) matches the source TOC exactly, including the 881F-specific deltas the pack teaches (L upgraded from information-only; K applicability A-J only).
- DAFMAN "31 templates (Attachments 2-32)" is exact (Attachment 1 is the glossary); releasability line, 15-calendar-day memo rule, and MBCRA/MRAP-C/LDTO/AFSIT/JITC terminology all verbatim-present in the extracted 2021 text; the 1995 wrong-edition mirror was correctly rejected (HALT.txt documents the halt).
- federal-bca honesty holds: `sources/federal-bca/US_Army_Cost_Benefit_Analysis.pdf` is a 489-byte "Access Denied" HTML stub — the Army fetch genuinely failed and the A-94-only rescope (P7-PRE-2) was executed before generation; the `2e7bc2e` authority paraphrase removed the verbatim statute run.
- DIST-A evidence: dote in-PDF DIST-A line verbatim (x2); 40051 DIST-A present in selected body text plus rendered-cover visual; 881F honestly records DIST-A-from-ASSIST-QuickSearch-column (cover has no printed block — provenance header in build full_text says so); VV&A carries per-chapter DEBoK "Copyright Details: Public Domain" + OSD/OUSD R&E OPR headers for all 10 chapters.
- Editions recorded per SOURCE-VETTING v1.18 build caveats: FAA Rev F 2007-11-30, DOT&E 8.02 Aug 2022, DAFMAN 2021-04-15, A-94 2023-11-09, 881F 2022-05-13, 40051-2C 2015-12-15, VV&A web edition + retrieval date. RR-S-13 (When to use + Prerequisites) present in all 7. chars/page figures in PACK.yaml match extraction metadata arithmetic. dote's "same August 2022 guidebook family" claim matches dod-te-guidebook's own source_version.

Findings below are records-accuracy and index-hygiene defects; none are licence-safety or correctness blockers.

## Findings

### MA-01: GP-06 marked complete in REQUIREMENTS.md while dual-source requirement is half-met

**Class:** MAJOR
**File:** `.planning/REQUIREMENTS.md:85` (record); `packs/federal-bca/PACK.yaml` (shipped reality)
**Issue:** REQUIREMENTS.md checks `[x] GP-06: federal-bca — OMB Circular A-94 + Army CBA Guide (dual-source)`, but the pack shipped A-94-only (plan-sanctioned P7-PRE-2 halt-and-rescope, honestly documented in PACK.yaml and catalog). The unmet Army CBA half (cost element structures, Army CEAC process) is not tracked as an open gap anywhere at milestone level — only inside the pack's "re-expand if available" note — so a future release can silently ship without ever closing it.
**Fix:** Annotate the GP-06 line (e.g. `[x] (A-94 only; Army CBA half open — retry alternate mirror/session)`) or add a gap-register/backlog entry so the residual is tracked outside the pack folder.

### MI-01: "OUSW(R&E)" malformed office abbreviation in shipped attribution surfaces

**Class:** MINOR
**File:** `packs/dod-vva-rpg/PACK.yaml:3,18`; `packs/dod-vva-rpg/LICENSE:7,20`; `catalog.json:607`; `NOTICE:637`
**Issue:** The publisher string reads "OUSW(R&E) CTO / M&S Office". The DoD office is OUSD(R&E) (Office of the Under Secretary of Defense for Research and Engineering); the build evidence itself records "Author (DEBoK): OUSD R&E". "OUSW" is a research-note typo (originating in 7-RESEARCH.md and docs/SOURCE-VETTING.md:130) propagated into four shipped surfaces. Under the no-source-link policy the publisher field IS the attribution record, so it should name the office correctly.
**Fix:** Replace `OUSW(R&E)` with `OUSD(R&E)` in dod-vva-rpg PACK.yaml, LICENSE, catalog.json publisher, and the NOTICE Author line (and correct the SOURCE-VETTING v1.18 GP-01 row for consistency).

### MI-02: dod-vva-rpg source_version hides ~2011 chapter currency

**Class:** MINOR
**File:** `packs/dod-vva-rpg/PACK.yaml` (source_version / notes)
**Issue:** `source_version: "RPG web edition (no dated rev; retrieved 2026-08-16)"` is true for the guide as a whole, but the chapter PDFs carry internal dates circa 2011 (e.g. ch01 header "1/31/2011"). A consumer assessing currency cannot tell from PACK.yaml that the packaged content is roughly 15 years old — a provenance-completeness gap, not an untruth.
**Fix:** Add one line to notes, e.g. "Chapter PDFs carry internal dates circa 2011 (e.g. Introduction 2011-01-31); web edition container undated."

### MI-03: mil-std-40051 page-object discrepancy (1168 vs 584) flagged but unresolved

**Class:** MINOR
**File:** `packs/mil-std-40051/PACK.yaml` (notes)
**Issue:** Research counted ~1168 page objects; pdftotext metadata says 584. PACK.yaml notes flag the discrepancy but resolve nothing. Internal selection ratios (151 of 584; cpp 2939.9 from selected_stats "443929 151") are consistent and no gate was bypassed, but the provenance trail leaves an open question about the fetched file's identity.
**Fix:** One sentence in notes settling it (e.g. "1168 counts image plate xobjects twice on some tools; pdftotext 584 is authoritative for this file") after a one-time re-verify, or record it as an accepted ambiguity.

### IN-01: Topic-index hygiene nits (ordering, circular routing, invented label)

**Class:** INFO
**File:** `packs/mil-std-881f/SKILL.md:89`; `packs/mil-std-40051/SKILL.md:77`; `packs/federal-bca/SKILL.md:73`; `packs/dafman-63-119/SKILL.md:65`
**Issue:** (a) 881F index entry "PM / measurement / EVMS mapping" sits last, out of the alphabetical order PACK-SPEC specifies (would sort between "Missile/ordnance" and "Program Element"); dafman lists "AFOTEC" after "Agile". (b) 40051 routes "Training & Documentation → ch01, ch07, ch08, Topic Index" — routing a topic to the Topic Index itself is circular. (c) federal-bca's "Opportunity/Benefit Analysis" label matches no term used in the chapters (source concepts are opportunity cost and benefit-cost analysis).
**Fix:** Re-sort the two entries; drop the "Topic Index" routing target; rename the federal-bca entry to "Opportunity cost / benefit identification".

### IN-02: check_overlap.py / scan_generated_skill.py not committed — licence-safety gate not CI-reproducible

**Class:** INFO
**File:** `tooling/` (absent); attested in all 7 `PACK.yaml` notes
**Issue:** PACK-SPEC's licence-safety rule ("never copy long verbatim passages") is enforced by check_overlap/scan scripts that live outside the committed repo (build-time agent tooling under gitignored `sources/`). CI (validate.yml) cannot re-run them, so the anti-verbatim control rests entirely on build-session attestations. Pre-existing Phase-3 model, not a Phase 7 regression.
**Fix:** Consider committing a minimal overlap checker to `tooling/` in a future phase so the no-long-verbatim rule is mechanically enforceable post-hoc.

### IN-03: Pack built_on/retrieval dates (2026-08-16) vs reviewer clock (2026-08-14)

**Class:** INFO
**File:** all 7 `PACK.yaml` (`build.built_on`)
**Issue:** Build dates are internally self-consistent with git author dates (Aug 16-17) but postdate the review clock's "today" (2026-08-14); almost certainly a clock-context artifact rather than a data error. Recorded so the P7-PRE-3 repudiation control gets one explicit confirmation.
**Fix:** Confirm once that 2026-08-16 was the actual build day; no change expected.

## Verified clean (no action)

- `python tooling/validate_pack.py` on all 7 packs: PASS (7/7, exit 0). `python tooling/check_release.py`: PASS.
- Required layout, frontmatter name==slug, chapter-link resolution, mandatory PACK.yaml fields, tier 1 — all packs.
- Chapter structure uniform across all 52 chapters (Core Idea / Frameworks Introduced / Key Concepts / Mental Models / Anti-patterns / Key Takeaways / Connects To).
- No http(s) URLs anywhere in the 7 packs (link policy); `sources/` gitignored; pack commits contain only pack paths (no PDFs, no full_text).
- docs/packs.html regenerates byte-identical from SKILLS.md (RR-B-00/RR-B-30 hold).
- Cursor manifest 62 == 63 dirs minus 1 NC pack (sebok); catalog "planned" section correctly untouched by registration.

---

_Reviewed: 2026-08-14_
_Reviewer: gsd-code-reviewer (adversarial pass; claims verified against local build evidence in sources/)_
_Depth: deep_
