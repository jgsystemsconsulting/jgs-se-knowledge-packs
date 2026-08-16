---
phase: 7-gap-driven-pack-builds
plan: 01
subsystem: knowledge-packs
tags: [tier-1, faa, dote, omb, pack-build, gap-driven]

requires:
  - phase: 7-gap-driven-pack-builds
    provides: 7-RESEARCH build sheets and Phase 3 pipeline deltas
  - phase: 3-tier-1-packs-public-domain
    provides: proven extract→scaffold→synthesize→validate→overlap pipeline
provides:
  - packs/faa-std-025 validated Tier-1 pack (GP-02)
  - packs/dote-te-guidebook validated Tier-1 pack (GP-03)
  - packs/federal-bca validated Tier-1 pack rescoped to OMB A-94 only (GP-06 partial)
  - P7-PRE-2/3/5 evidence records; dafman-63-119 halt surface (GP-04 blocked)
affects:
  - 7-02 (Wave B packs)
  - 7-03 (registration sweep — must include only built packs + decide dafman/federal-bca rescope)
  - Phase 8 cluster map (cluster 15 fattens via A-94; cluster 9 via dote; 5/3 via faa)

actuals:
  tokens: 26150
  tasks: 3
  commits: 4

tech-stack:
  added: []
  patterns:
    - Phase 3 pipeline with work_dir.txt printf + tr -d convention
    - P7-PRE-2 halt-and-rescope when dual-doc second source unfetchable
    - P7-PRE-3 edition strings in source_version
    - slug-distinction Scope & Limits crosswalk (dote vs dod-te-guidebook)

key-files:
  created:
    - packs/faa-std-025/**
    - packs/dote-te-guidebook/**
    - packs/federal-bca/**
  modified: []

key-decisions:
  - "faa-std-025: ROSAP rev E 403 → built Rev F everyspec (2007-11-30); recorded per P7-PRE-3"
  - "dote-te-guidebook: DMI 8.02 Aug 2022; complementary to dod-te-guidebook (same guidebook family)"
  - "federal-bca: P7-PRE-2 rescope to A-94 only after Army CBA 403/Wayback 503"
  - "dafman-63-119: HALTED — cannot obtain 2021 PDF for P7-PRE-5 in-copy releasability reconfirm"

patterns-established:
  - "Bot-protected AF e-publishing may block even Playwright Chrome; do not substitute wrong-edition mirrors"
  - "Dual-doc packs must drop missing half before generation (P7-PRE-2)"

requirements-completed: [GP-02, GP-03, GP-06]
# GP-04 not completed (halt)

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
    description: "dafman-63-119 pack — NOT built (fetch/P7-PRE-5 halt)"
    requirement: GP-04
    verification:
      - kind: other
        ref: "canonical PDF 403; Wayback 498/503; IU=1995 wrong edition"
        status: fail
    human_judgment: true
    rationale: "Need human/network path to 2021 DAFMAN PDF to reconfirm releasability line"
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

duration: 34min
completed: 2026-08-16
status: complete
---

# Phase 7 Plan 01: Wave A Gap-Driven Pack Builds Summary

**Three Tier-1 packs shipped (faa-std-025, dote-te-guidebook, federal-bca/A-94-only); dafman-63-119 halted on bot-protected fetch so P7-PRE-5 could not reconfirm the 2021 releasability line.**

## Performance

- **Duration:** ~34 min
- **Tasks:** 3/4 complete (Task 3 halted)
- **Commits:** 4 (3 pack + 1 overlap fix)

## Per-pack results

| Pack | Commit | Mirror/source | Edition recorded | Pages | chars/page | Chapters | validate | overlap | scan | P7-PRE |
|------|--------|---------------|------------------|-------|------------|----------|----------|---------|------|--------|
| faa-std-025 | `bab559d` | everyspec Rev F (ROSAP 403) | Rev F 2007-11-30 | 64 | 2420.5 | 6 | PASS | exit 0 | PASS | PRE-3 Rev F; PRE-5 no © in PDF |
| dote-te-guidebook | `e400335` | DMI 8.02 PDF | 8.02 Aug 2022 | 165 | 2729.2 | 8 | PASS | exit 0 | PASS | PRE-3 8.02; PRE-5 DIST-A in PDF |
| dafman-63-119 | — | **HALTED** | — | — | — | — | — | — | — | PRE-5 blocked (no 2021 copy) |
| federal-bca | `8892ac7` + fix `2e7bc2e` | whitehouse.gov A-94 PDF | A-94 rev 2023-11-09; Army dropped | 28 | 2832.3 | 6 | PASS | exit 0 | PASS | PRE-2 A-94 PASS / Army FAIL→rescope |

## P7-PRE resolutions

### P7-PRE-3 (edition recording)
- **faa-std-025:** `source_version: "Rev F (2007-11-30, everyspec mirror; ROSAP rev E blocked at build)"`
- **dote-te-guidebook:** `source_version: "8.02 (Aug 2022, DMI mirror)"` (afacpo v3-June available but unused)

### P7-PRE-5 (in-copy rights)
- **faa-std-025:** No third-party copyright/releasability lines; FAA/DoT standard cover; statute basis retained
- **dote-te-guidebook:** Verbatim DIST-A: "DISTRIBUTION STATEMENT A . Approved for public release . Distribution is unlimited."
- **dafman-63-119:** **Could not reconfirm** "no releasability restrictions" — 2021 PDF not obtained

### P7-PRE-2 (federal-bca dual in-source)
| Document | Fetch | In-source licence | Disposition |
|----------|-------|-------------------|-------------|
| OMB Circular A-94 (2023-11-09) | OK (whitehouse.gov) | No © / third-party copyright hits; OMB circular | **Keep — generate** |
| US Army CBA Guide | FAIL (ASAFM 403; Wayback 503) | N/A — no file | **Drop — rescope pack to A-94 only before generation** |

## Task 3 halt-and-surface (dafman-63-119)

**Blocked by:** Cannot download DAFMAN 63-119 (15 APR 2021) to reconfirm P7-PRE-5 releasability line in the actually-downloaded copy.

Attempts:
1. Plain curl / browser-UA / Referer cookie jar → HTTP 403 Akamai HTML
2. Playwright Chromium + Chrome channel after visiting e-publishing home → still 403 Access Denied
3. Wayback CDX shows historical 200 PDF snapshots; retrieval from this environment → 498/503
4. Indiana University mirror → **wrong edition** (AFMAN 63-119, 22 Feb 1995, dedicated OT&E certification templates) — must not be labelled as 2021 MOTRC

**Required human/orchestrator action:** Provide a reachable 2021 DAFMAN 63-119 PDF (or open network path), then re-run Task 3 only.

## Deviations from Plan

| # | Deviation | Plan reference | Proposed classification | Rationale |
|---|-----------|----------------|--------------------------|-----------|
| 1 | ROSAP blocked; used everyspec Rev F | Task 1 step 1 fallback | in-scope fix | Plan explicitly allows rev F mirror with P7-PRE-3 labelling |
| 2 | dote pack complementary to existing dod-te-guidebook (same Aug 2022 guidebook) | Task 2 slug-distinction | in-scope fix | Plan requires cross-reference; source is the public Enterprise Guidebook 8.02 |
| 3 | federal-bca rescoped to A-94 only | Task 4 P7-PRE-2 | in-scope fix | Hard gate: drop failing document before generation |
| 4 | dafman-63-119 not built | Task 3 | in-scope fix (halt) | P7-PRE-5 cannot be satisfied without 2021 copy |
| 5 | Extra fix commit for federal-bca overlap paraphrase | Task 4 verify | in-scope fix | check_overlap flagged 12-word authority string |

### Auto-fixed Issues

**1. [Rule 1 - Bug] federal-bca check_overlap hit on authority clause**
- **Found during:** Task 4 verify (after initial commit)
- **Issue:** Verbatim run "31 u s c 1111 and the budget and accounting act of 1921 as amended"
- **Fix:** Paraphrased authority bullet in ch01
- **Files modified:** packs/federal-bca/chapters/ch01-purpose-scope-and-principles.md
- **Commit:** `2e7bc2e`

## Registration note

Catalog still 54; packs/ dirs now **59** (56 baseline + faa + dote + federal-bca). Registration intentionally deferred to **7-03**. Do not register dafman-63-119 until built.

## Self-Check: PASSED

- FOUND: packs/faa-std-025/SKILL.md, PACK.yaml, LICENSE, chapters/
- FOUND: packs/dote-te-guidebook/SKILL.md, PACK.yaml, LICENSE, chapters/
- FOUND: packs/federal-bca/SKILL.md, PACK.yaml, LICENSE, chapters/
- MISSING (expected): packs/dafman-63-119 (halted)
- FOUND commits: bab559d, e400335, 8892ac7, 2e7bc2e
