---
phase: 7-gap-driven-pack-builds
plan: 01
subsystem: knowledge-packs
tags: [tier-1, faa, dote, omb, dafman, pack-build, gap-driven]

requires:
  - phase: 7-gap-driven-pack-builds
    provides: 7-RESEARCH build sheets and Phase 3 pipeline deltas
  - phase: 3-tier-1-packs-public-domain
    provides: proven extract→scaffold→synthesize→validate→overlap pipeline
provides:
  - packs/faa-std-025 validated Tier-1 pack (GP-02)
  - packs/dote-te-guidebook validated Tier-1 pack (GP-03)
  - packs/dafman-63-119 validated Tier-1 pack (GP-04)
  - packs/federal-bca validated Tier-1 pack rescoped to OMB A-94 only (GP-06 partial)
  - P7-PRE-2/3/5 evidence records including dafman P7-PRE-5 reconfirm
affects:
  - 7-02 (Wave B packs)
  - 7-03 (registration sweep — include dafman-63-119; federal-bca A-94-only rescope)
  - Phase 8 cluster map (cluster 15 fattens via A-94; cluster 9 via dote/dafman; 5/3 via faa)

actuals:
  tokens: 42000
  tasks: 4
  commits: 6

tech-stack:
  added: []
  patterns:
    - Phase 3 pipeline with work_dir.txt printf + tr -d convention
    - P7-PRE-2 halt-and-rescope when dual-doc second source unfetchable
    - P7-PRE-3 edition strings in source_version
    - slug-distinction Scope & Limits crosswalk (dote vs dod-te-guidebook)
    - jina reader-proxy full-text fetch when Akamai blocks direct PDF (dafman GP-04)

key-files:
  created:
    - packs/faa-std-025/**
    - packs/dote-te-guidebook/**
    - packs/dafman-63-119/**
    - packs/federal-bca/**
  modified: []

key-decisions:
  - "faa-std-025: ROSAP rev E 403 → built Rev F everyspec (2007-11-30); recorded per P7-PRE-3"
  - "dote-te-guidebook: DMI 8.02 Aug 2022; complementary to dod-te-guidebook (same guidebook family)"
  - "federal-bca: P7-PRE-2 rescope to A-94 only after Army CBA 403/Wayback 503"
  - "dafman-63-119: 2021 full text via r.jina.ai reader of canonical e-publishing URL; P7-PRE-5 reconfirmed; 1995 IU mirror rejected"

patterns-established:
  - "Bot-protected AF e-publishing may block even Playwright Chrome; do not substitute wrong-edition mirrors"
  - "Dual-doc packs must drop missing half before generation (P7-PRE-2)"
  - "When PDF binary is Akamai-blocked, reader-proxy extracted text of the canonical URL is acceptable if title page + page count + releasability line verify (record route in PACK.yaml notes)"

requirements-completed: [GP-02, GP-03, GP-04, GP-06]

coverage:
  - id: D1
    description: "faa-std-025 pack built, validated, overlap-clean, committed"
    requirement: GP-02
    verification:
      - kind: other
        ref: "python tooling/validate_pack.py packs/faa-std-025"
        status: pass
      - kind: other
        ref: "check_overlap exit 0; chars/page 2420.5"
        status: pass
    human_judgment: false
  - id: D2
    description: "dote-te-guidebook pack built with edition 8.02 and dod-te crosswalk"
    requirement: GP-03
    verification:
      - kind: other
        ref: "python tooling/validate_pack.py packs/dote-te-guidebook"
        status: pass
      - kind: other
        ref: "source_version 8.02; grepped dod-te-guidebook in SKILL.md"
        status: pass
    human_judgment: false
  - id: D3
    description: "dafman-63-119 pack built with P7-PRE-5 releasability reconfirm"
    requirement: GP-04
    verification:
      - kind: other
        ref: "python tooling/validate_pack.py packs/dafman-63-119"
        status: pass
      - kind: other
        ref: "check_overlap exit 0; scan pass; chars/page 2018.1; commit 4bc093c"
        status: pass
      - kind: other
        ref: "P7-PRE-5 verbatim releasability line in obtained 2021 text"
        status: pass
    human_judgment: false
  - id: D4
    description: "federal-bca pack built A-94-only after P7-PRE-2 Army drop"
    requirement: GP-06
    verification:
      - kind: other
        ref: "validate_pack + check_overlap exit 0 after authority paraphrase"
        status: pass
      - kind: other
        ref: "P7-PRE-2 notes record Army fetch fail + A-94 in-source clean"
        status: pass
    human_judgment: false

duration: 55min
completed: 2026-08-16
status: complete
---

# Phase 7 Plan 01: Wave A Gap-Driven Pack Builds Summary

**Four Tier-1 packs shipped (faa-std-025, dote-te-guidebook, dafman-63-119, federal-bca/A-94-only). GP-04 completed after reader-proxy fetch of the 2021 DAFMAN with P7-PRE-5 releasability reconfirm.**

## Performance

- **Duration:** ~55 min (incl. GP-04 resume)
- **Tasks:** 4/4 complete (Task 3 resumed and closed)
- **Commits:** 6 (4 pack + 1 overlap fix + docs; pack sha for dafman `4bc093c`)

## Per-pack results

| Pack | Commit | Mirror/source | Edition recorded | Pages | chars/page | Chapters | validate | overlap | scan | P7-PRE |
|------|--------|---------------|------------------|-------|------------|----------|----------|---------|------|--------|
| faa-std-025 | `bab559d` | everyspec Rev F (ROSAP 403) | Rev F 2007-11-30 | 64 | 2420.5 | 6 | PASS | exit 0 | PASS | PRE-3 Rev F; PRE-5 no © in PDF |
| dote-te-guidebook | `e400335` | DMI 8.02 PDF | 8.02 Aug 2022 | 165 | 2729.2 | 8 | PASS | exit 0 | PASS | PRE-3 8.02; PRE-5 DIST-A in PDF |
| dafman-63-119 | `4bc093c` | r.jina.ai reader of canonical e-publishing PDF | DAFMAN 63-119, 15 Apr 2021 | 103 | 2018.1 | 7 | PASS | exit 0 | PASS | PRE-5 releasability reconfirmed |
| federal-bca | `8892ac7` + fix `2e7bc2e` | whitehouse.gov A-94 PDF | A-94 rev 2023-11-09; Army dropped | 28 | 2832.3 | 6 | PASS | exit 0 | PASS | PRE-2 A-94 PASS / Army FAIL→rescope |

## P7-PRE resolutions

### P7-PRE-3 (edition recording)
- **faa-std-025:** `source_version: "Rev F (2007-11-30, everyspec mirror; ROSAP rev E blocked at build)"`
- **dote-te-guidebook:** `source_version: "8.02 (Aug 2022, DMI mirror)"` (afacpo v3-June available but unused)

### P7-PRE-5 (in-copy rights)
- **faa-std-025:** No third-party copyright/releasability lines; FAA/DoT standard cover; statute basis retained
- **dote-te-guidebook:** Verbatim DIST-A: "DISTRIBUTION STATEMENT A . Approved for public release . Distribution is unlimited."
- **dafman-63-119:** Reconfirmed on obtained 2021 text: "RELEASABILITY: There are no releasability restrictions on this publication." Title page MOTRC + 15 APRIL 2021 + Pages: 103 verified.

### P7-PRE-2 (federal-bca dual in-source)
| Document | Fetch | In-source licence | Disposition |
|----------|-------|-------------------|-------------|
| OMB Circular A-94 (2023-11-09) | OK (whitehouse.gov) | No © / third-party copyright hits; OMB circular | **Keep — generate** |
| US Army CBA Guide | FAIL (ASAFM 403; Wayback 503) | N/A — no file | **Drop — rescope pack to A-94 only before generation** |

## GP-04 completion (dafman-63-119) — resumed Task 3

**Status:** COMPLETE — pack committed `4bc093c`.

### Fetch route
- Canonical URL: `https://static.e-publishing.af.mil/production/1/saf_aq/publication/dafman63-119/dafman63-119.pdf`
- Direct/browser/Playwright still Akamai 403 in prior halt; resume used scout-verified reader proxy:
  `https://r.jina.ai/https://static.e-publishing.af.mil/production/1/saf_aq/publication/dafman63-119/dafman63-119.pdf`
- HTTP 200, ~211KB extracted text; header `Number of Pages: 103`; title page = DAFMAN 63-119, 15 APRIL 2021, MISSION-ORIENTED TEST READINESS CERTIFICATION
- Extraction skip: reader text **is** the extraction (no extract.py / pdftotext); stored under gitignored `sources/dafman-63-119/book_skill_work/`
- 1995 IU/AFMAN mirror PDF present in sources was **not** used (wrong edition)

### Gates (all pass)
| Gate | Result |
|------|--------|
| P7-PRE-5 releasability line in obtained text | PASS — verbatim "no releasability restrictions" |
| MOTRC title page | PASS |
| chars/page = len(text)/103 | **2018.1** ≥ 300 |
| licence string | `Public Domain (US Government work, 17 U.S.C. § 105)` |
| SKILL.md `## When to use` + `**Prerequisites:**` | 1 + 1 |
| PACK.yaml `source_version` | `DAFMAN 63-119, 15 Apr 2021` |
| chapters | 7 (in 6–8 band) |
| `validate_pack.py` | PASS exit 0 |
| `check_overlap.py` vs full_text | PASS exit 0 |
| `scan_generated_skill.py` | PASS exit 0 |
| TODO in PACK.yaml | none |
| git-show leak (`sources/` / `full_text.txt`) | none — pack paths only |
| commit | `4bc093c` `feat(packs): add dafman-63-119 (Tier 1)` |

### PACK.yaml notes (route record)
Records reader-proxy provenance, P7-PRE-5 verbatim finding, chars/page, and rejection of the 1995 wrong edition.

## Deviations from Plan

| # | Deviation | Plan reference | Proposed classification | Rationale |
|---|-----------|----------------|--------------------------|-----------|
| 1 | ROSAP blocked; used everyspec Rev F | Task 1 step 1 fallback | in-scope fix | Plan explicitly allows rev F mirror with P7-PRE-3 labelling |
| 2 | dote pack complementary to existing dod-te-guidebook (same Aug 2022 guidebook) | Task 2 slug-distinction | in-scope fix | Plan requires cross-reference; source is the public Enterprise Guidebook 8.02 |
| 3 | federal-bca rescoped to A-94 only | Task 4 P7-PRE-2 | in-scope fix | Hard gate: drop failing document before generation |
| 4 | dafman full text via jina reader proxy (not PDF binary / extract.py) | Task 3 fetch | in-scope fix | Akamai blocks non-browser PDF; scout-verified reader returns full 103pp text of canonical URL; title+releasability verified before generation |
| 5 | Extra fix commit for federal-bca overlap paraphrase | Task 4 verify | in-scope fix | check_overlap flagged 12-word authority string |
| 6 | Initial Task 3 halt then resume | Task 3 | in-scope fix | Prior session could not obtain 2021 text; resume closed GP-04 |

### Auto-fixed Issues

**1. [Rule 1 - Bug] federal-bca check_overlap hit on authority clause**
- **Found during:** Task 4 verify (after initial commit)
- **Issue:** Verbatim run "31 u s c 1111 and the budget and accounting act of 1921 as amended"
- **Fix:** Paraphrased authority bullet in ch01
- **Files modified:** packs/federal-bca/chapters/ch01-purpose-scope-and-principles.md
- **Commit:** `2e7bc2e`

## Registration note

Catalog still 54; packs/ dirs now **60** (56 baseline + faa + dote + federal-bca + dafman). Registration intentionally deferred to **7-03**. Include `dafman-63-119` in the 7-03 registration sweep.

## Self-Check: PASSED

- FOUND: packs/faa-std-025/SKILL.md, PACK.yaml, LICENSE, chapters/
- FOUND: packs/dote-te-guidebook/SKILL.md, PACK.yaml, LICENSE, chapters/
- FOUND: packs/federal-bca/SKILL.md, PACK.yaml, LICENSE, chapters/
- FOUND: packs/dafman-63-119/SKILL.md, PACK.yaml, LICENSE, chapters/ (7 ch)
- FOUND commits: bab559d, e400335, 8892ac7, 2e7bc2e, 4bc093c
