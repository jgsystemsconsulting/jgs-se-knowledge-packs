---
phase: 3-tier-1-packs-public-domain
plan: 02
subsystem: knowledge-packs
tags: [tier-1, dod, mil-hdbk, public-domain, pack-build, distribution-statement-a]

requires:
  - phase: 2-source-vetting-ruled-out-register
    provides: vetted Tier-1 source list and mirror URLs (2-RESEARCH)
  - phase: 3-tier-1-packs-public-domain
    provides: 3-RESEARCH pipeline and Batch B build sheets; 3-01 pipeline exemplars
provides:
  - packs/mil-hdbk-338 validated Tier-1 pack (T1-03)
  - packs/mil-hdbk-516 validated Tier-1 pack (T1-04)
affects:
  - 3-03 (registration: catalog.json, SKILLS.md, gen_packs_page, NOTICE, check_release)

actuals:
  tokens: 16458
  tasks: 2
  commits: 3

tech-stack:
  added: []
  patterns:
    - extract-first before vet/scaffold (Batch B reorder)
    - mirror URL + DIST-A in-copy verification recorded in PACK.yaml notes
    - chars/page floor (>=300) before synthesis
    - work_dir.txt via printf; book_skill_work preserved under sources/<slug>/

key-files:
  created:
    - packs/mil-hdbk-338/**
    - packs/mil-hdbk-516/**
  modified: []

key-decisions:
  - "338B: nde-ed.org mirror used (DLA token-gated); metadata pages=1046 vs DLA ~716 — accepted after cpp floor + full body section presence"
  - "516C: everyspec.com mirror used (DLA token-gated); metadata pages=527 vs build-sheet ~320 — accepted after cpp floor + DIST-A + full section spine"
  - "338: 9 chapters selected from Part 2 design guidance; annex tables skipped"
  - "516: 8 chapters (scope/tailoring, SE, structures, flight, propulsion, avionics/E3/diagnostics, software, crew systems)"
  - "OCR not required for either PDF (pdftotext text layer sufficient)"
  - "build_pack --force for DoD third-party-quote advisory"

patterns-established:
  - "MJ-02: record mirror actually used + DIST-A verification in PACK.yaml notes"
  - "MJ-03: chars/page floor after extract before any generation"
  - "Extract-before-vet reorder for risky DoD PDFs (MN-06)"

requirements-completed: [T1-03, T1-04]

coverage:
  - id: D1
    description: "mil-hdbk-338 pack built, validated, overlap-clean, committed"
    requirement: T1-03
    verification:
      - kind: other
        ref: "python tooling/validate_pack.py packs/mil-hdbk-338"
        status: pass
      - kind: other
        ref: "python REF/tools/check_overlap.py --pack packs/mil-hdbk-338"
        status: pass
    human_judgment: false
  - id: D2
    description: "mil-hdbk-516 pack built, validated, overlap-clean, committed"
    requirement: T1-04
    verification:
      - kind: other
        ref: "python tooling/validate_pack.py packs/mil-hdbk-516"
        status: pass
      - kind: other
        ref: "python REF/tools/check_overlap.py --pack packs/mil-hdbk-516"
        status: pass
    human_judgment: false

duration: 90min
completed: 2026-08-15
status: complete
---

# Phase 3 Plan 02: Batch B DoD Tier-1 Packs Summary

**Two DoD handbook packs (mil-hdbk-338, mil-hdbk-516) built via extract-first pipeline with mirror + DIST-A verification, chars/page floor, 8–9 synthesized chapters each, one scoped commit per pack, and no sources/ leakage.**

## Performance

- **Duration:** ~90 min
- **Tasks:** 2/2
- **Commits:** 2 pack commits + 1 docs SUMMARY commit

## Per-pack results

| Pack | Commit | Mirror | Pages (extract) | chars/page | DIST-A | Chapters | validate_pack | check_overlap | scan | OCR |
|------|--------|--------|-----------------|------------|--------|----------|---------------|---------------|------|-----|
| mil-hdbk-338 | `4dfba84` | nde-ed.org | 1046 | 2407.1 | PASS (cover) | 9 | PASS | exit 0 | PASS | not needed |
| mil-hdbk-516 | `7ac09ad` | everyspec.com | 527 | 2954.2 | PASS (cover) | 8 | PASS | exit 0 | PASS | not needed |

### mil-hdbk-338 (T1-03)

- **Download:** DLA QuickSearch ident 54022 remains authoritative record; PDF fetched from verified **nde-ed.org** mirror (`MILHDBK338B.pdf`).
- **DIST-A:** Cover page text includes `DISTRIBUTION STATEMENT A. Approved for public release; distribution is unlimited.`
- **Extract:** pdftotext fallback (`--install-missing no`); metadata **1046 pages**, 2,517,789 chars → **2407.1 chars/page** (MJ-03 floor ~300 **PASS**).
- **Page-count vs record:** DLA/build-sheet ~716; PDF page objects 1046 (blanks/front matter). Not treated as truncated mirror: cpp floor passed and body sections §5–§12 present end-to-end.
- **Chapter selection (9):** R/M/A theory; spec/allocation/prediction; parts+derating; circuit+fault tolerance; environment+human; FMEA/FTA/SCA; reviews/testability/safety; data/FRACAS/demo/growth; systems R&M. Annex tables skipped. Slices via offsets only (never whole full_text in agent context for generation).
- **Licence:** `Public Domain (US Government work, 17 U.S.C. § 105; Distribution Statement A — Approved for public release; distribution is unlimited)` in PACK.yaml + LICENSE.
- **work_dir.txt:** `printf` path to `sources/mil-hdbk-338` (MN-05).

### mil-hdbk-516 (T1-04)

- **Download:** DLA PDF token-gated; used **everyspec.com** mirror `MIL-HDBK-516C.052120.pdf`.
- **DIST-A:** Cover includes `DISTRIBUTION STATEMENT A: Approved for public release; distribution is unlimited.`
- **Extract:** pdftotext; metadata **527 pages**, 1,556,876 chars → **2954.2 chars/page** (MJ-03 **PASS**).
- **Page-count vs estimate:** build-sheet ~320; extract 527 page objects. Full section spine present (scope through crew systems/software/etc.); not treated as truncation.
- **Chapters (8):** scope/applicability/tailoring; systems engineering; structures; flight technology; propulsion+installation; diagnostics/avionics/electrical/E3; computers/software; crew systems (incl. UAS control-station applicability).
- **Licence:** same DIST-A variant string in PACK.yaml + LICENSE.
- **OCR:** not required.

## MUST-ADDRESS resolutions

| ID | Resolution |
|----|------------|
| MJ-02 | Mirror actually used recorded in each PACK.yaml `notes` (nde-ed.org / everyspec.com); DIST-A verified in-copy; page-count cross-check documented above (divergence explained; no halt — not truncated). |
| MJ-03 | chars/page floor enforced post-extract: 338=2407.1, 516=2954.2 (both >>300). OCR contingency **not** triggered. |
| MN-01 | `git show --name-only` on `4dfba84` and `7ac09ad` — zero `sources/` or `full_text` paths. |
| MN-02 | PACK.yaml `build:` real values (source_pages, chapters, built_on); no TODO stubs. |
| MN-05 | `work_dir.txt` written with `printf '%s'`; read with `tr -d '\r\n'`. |
| MN-06 | **Extract-before-vet reorder followed** (claim row: pipeline extract first for Batch B risk containment). Claim verification updated here in SUMMARY, not by editing the plan. |

## Claim verification updates (SUMMARY, not plan)

| claim | observed | status |
|---|---|---|
| extract before generation/vet work for Batch B | both PDFs extracted + cpp floor before scaffold/generate | VERIFIED (MN-06) |
| OCR fallback if image-only | not needed; text layer OK | N/A (contingency unused) |

## Registration notes for 3-03 executor

Do **not** assume catalog/SKILLS/NOTICE/packs.html were updated here.

When registering these two packs, 3-03 must:

1. **catalog.json** — add mil-hdbk-338 (9 ch) and mil-hdbk-516 (8 ch); bump `updated`.
2. **SKILLS.md** — two rows; bump header pack count (+2).
3. **README badge / pack count** — bump displayed total.
4. **docs/packs.html** — `python tooling/gen_packs_page.py`.
5. **NOTICE** — two `[pack: …]` Public Domain + DIST-A attribution blocks.
6. **check_release.py** — final PASS after registration.

## Deviations from Plan

| # | Deviation | Plan reference | Proposed classification | Rationale |
|---|-----------|----------------|--------------------------|-----------|
| 1 | extract `--install-missing no` (not `ask`) | Task pipeline | in-scope fix | Non-interactive agent; pdftotext fallback supported |
| 2 | build_pack `--force` for DoD advisory | scaffold | in-scope fix | Third-party-quote advisory blocks without --force |
| 3 | 338 pages 1046 vs ~716 estimate | Task 1 done / MJ-02 | in-scope fix | metadata.json authoritative; cpp + body completeness OK |
| 4 | 516 pages 527 vs ~320 estimate | Task 2 / MJ-02 | in-scope fix | same; everyspec full 516C body present |
| 5 | 516 mirror = everyspec (not live DLA token URL) | Task 2 download | in-scope fix | DLA token-gated; DIST-A verified in-copy per risk 3 |
| 6 | Initial Key Concepts used near-verbatim source bullets; rewritten before commit | overlap gate | in-scope fix | check_overlap exit 3 → synthetic concepts; exit 0 |
| 7 | Plan text said 6–8 chapters for 516; shipped 8 | Task 2 action | in-scope fix | Within expected structure; no chapter-count gate |

### Auto-fixed Issues

**1. [Rule 1 - Bug] Overlap hits from source-bullet Key Concepts**
- **Found during:** Task 1/2 verify (check_overlap exit 3)
- **Issue:** generator planted near-verbatim handbook phrases in Key Concepts
- **Fix:** replaced all Key Concepts with fully synthetic short bullets; re-ran overlap exit 0 on both packs before commit
- **Files modified:** all `packs/mil-hdbk-338/chapters/*`, `packs/mil-hdbk-516/chapters/*`
- **Commit:** included in `4dfba84` / `7ac09ad` (pre-commit fix)

## Accomplishments

- Shipped 2 validated Tier-1 DoD packs (29 files under packs/)
- Contained download/mirror risk for Batch B without OCR
- DIST-A licence variant on both packs
- Zero source PDF / full_text commits (MN-01)
- Both SKILL.md files satisfy When-to-use + Prerequisites

## Self-Check: PASSED

- FOUND: packs/mil-hdbk-338/SKILL.md, PACK.yaml, LICENSE, chapters/ (9)
- FOUND: packs/mil-hdbk-516/SKILL.md, PACK.yaml, LICENSE, chapters/ (8)
- FOUND commits: 4dfba84, 7ac09ad
- validate_pack PASS ×2; check_overlap exit 0 ×2; scan PASS ×2
- MN-01 leak check PASS ×2
