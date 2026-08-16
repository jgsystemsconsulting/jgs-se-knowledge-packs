---
phase: 7-gap-driven-pack-builds
plan: 03
subsystem: knowledge-packs
tags: [tier-1, dod, vva, m&s, registration, gap-driven, chapter-wise, dist-a]

requires:
  - phase: 7-gap-driven-pack-builds
    provides: 7-RESEARCH build sheets; Wave A/B packs (faa-std-025, dote-te-guidebook, dafman-63-119, federal-bca, mil-std-881f, mil-std-40051); jina/DEBoK fetch patterns
provides:
  - packs/dod-vva-rpg chapter-wise Tier-1 pack (GP-01)
  - consolidated registration of all 7 GP packs at exact counts
  - cluster-target baseline table for Phase 8
affects: [phase-8-capability-map, phase-9-release]

actuals:
  tokens: 31503
  tasks: 2
  commits: 3

tech-stack:
  added: []
  patterns:
    - Chapter-wise multi-PDF pack build (no consolidated source)
    - DEBoK OTMM guest session for cto.mil-linked RPG chapter PDFs
    - P7-PRE-4 per-chapter DEBoK Public Domain + OSD/OUSD authorship evidence
    - Single registration sweep (Phase 3 3-03 precedent)

key-files:
  created:
    - packs/dod-vva-rpg/**
  modified:
    - catalog.json
    - SKILLS.md
    - README.md
    - NOTICE
    - docs/packs.html
    - .cursor-plugin/plugin.json

key-decisions:
  - "dod-vva-rpg: 10 new-development role + special-topic chapters; T&E/V&V Checklist selected out (not licence drop)"
  - "P7-PRE-4 DIST-A: DEBoK Copyright=Public Domain + OSD/OUSD OPR when cover lacks printed DIST block (881F metadata pattern)"
  - "federal-bca catalog source_version honest A-94-only note"
  - "Registration only — no version bumps (Phase 9 owns)"

patterns-established:
  - "DEBoK OTMM guest credentials embedded in SPA (double-atob) for public PDF renditions"
  - "work_dir_chN.txt + chapter_fulltexts/chNN.txt convention for multi-source packs"
  - "One registration commit for all GP packs after last pack build"

requirements-completed: [GP-01]

coverage:
  - id: D1
    description: "packs/dod-vva-rpg built chapter-wise, validated, overlap-clean, committed"
    requirement: GP-01
    verification:
      - kind: other
        ref: "python tooling/validate_pack.py packs/dod-vva-rpg"
        status: pass
      - kind: other
        ref: "check_overlap.py per sources/dod-vva-rpg/chapter_fulltexts/*.txt"
        status: pass
      - kind: other
        ref: "scan_generated_skill.py packs/dod-vva-rpg"
        status: pass
    human_judgment: false
  - id: D2
    description: "All 7 GP packs registered; check_release PASS at 61/62/63"
    requirement: GP-01
    verification:
      - kind: other
        ref: "python tooling/check_release.py"
        status: pass
      - kind: other
        ref: "catalog 61 / cursor 62 / packs 63 / SKILLS 61(+2) / packs-61"
        status: pass
    human_judgment: false

duration: 22min
completed: 2026-08-16
status: complete
---

# Phase 7 Plan 03: Wave C VV&A + Registration Summary

**Chapter-wise dod-vva-rpg (10 ch, 283 pp, DEBoK PD/DIST evidence) plus consolidated registration of all 7 GP packs to catalog 61 / cursor 62 / packs 63 with check_release PASS.**

## Performance

- **Duration:** ~22 min wall (fetch/extract dominated earlier wall clock in session)
- **Tasks:** 2/2
- **Commits:** 2 task + 1 docs summary (this file)

## Commits

| Task | SHA | Message |
|------|-----|---------|
| 1 | `3b5b2f7` | feat(packs): add dod-vva-rpg (Tier 1) |
| 2 | `e00ac7d` | docs(registration): register 7 GP packs (catalog 61, cursor 62) |

## Task 1 — dod-vva-rpg (GP-01)

### Fetch route
- Index: cto.mil VV&A RPG HTML (per-chapter DEBoK search links).
- PDFs: DEBoK OTMM guest session → `search/text` by filename → `/otmmapi/v5/renditions/<id>`.
- Selected set (10): key-pr, user-new, dev-new, pm-new, vv-new, aa-new, fidelity, Validation, DataVV-new, Risk.
- Dropped (selection): TEVVchecklist-pr.PDF (keep 8–10 chapter band); also DEBoK PD.

### P7-PRE-4
| Ch | File | Pages | chars/page | DEBoK Copyright | Author/OPR | Gate |
|----|------|------:|-----------:|-----------------|------------|------|
| 01 | key-pr.pdf | 34 | 2791.6 | Public Domain | OUSD R&E / OSD | PASS |
| 02 | user-new-pr.pdf | 31 | 2639.0 | Public Domain | OSD R&E / OSD | PASS |
| 03 | dev-new-pr.pdf | 31 | 2913.8 | Public Domain | OSD R&E / OSD | PASS |
| 04 | pm-new-pr.pdf | 40 | 2873.3 | Public Domain | OSD R&E / OSD | PASS |
| 05 | vv-new-pr.pdf | 46 | 3034.0 | Public Domain | OUSD R&E / OSD | PASS |
| 06 | aa-new-pr.pdf | 26 | 2664.8 | Public Domain | OSD R&E / OSD | PASS |
| 07 | fidelity-pr.PDF | 10 | 3015.5 | Public Domain | OSD R&E / OSD | PASS |
| 08 | Validation-pr.PDF | 36 | 2764.7 | Public Domain | OSD R&E / OSD | PASS |
| 09 | DataVV-new-pr.PDF | 12 | 2588.8 | Public Domain | OSD R&E / OSD | PASS |
| 10 | Risk-pr.PDF | 17 | 2668.1 | Public Domain | OSD R&E / OSD | PASS |

- **source_pages = 283** (sum metadata.json).
- Cover text layers lack printed DIST-A prose; DIST equivalent = DEBoK PD + OSD/OUSD authorship (881F Dist-Stmt metadata pattern). Provenance headers recorded in build full_texts; PACK.yaml notes carry per-chapter titles + retrieved 2026-08-16 (no URLs).

### Gates
| Gate | Result |
|------|--------|
| validate_pack.py | PASS |
| check_overlap ×10 chapter full_texts | all exit 0 |
| scan_generated_skill.py | PASS |
| When to use / Prerequisites | 1 / 1 |
| no TODO in PACK.yaml; retrieved present | OK |
| work_dir_ch*.txt chars/page ≥300 | all PASS |
| git show leak (sources/\|full_text) | clean |

## Task 2 — Registration sweep

### Counts (evidence)
| Surface | Value |
|---------|------:|
| catalog.json packs | **61** |
| .cursor-plugin/plugin.json skills | **62** |
| packs/ directories | **63** |
| SKILLS.md header | **61 packs (+2 signposts)** |
| README badge | **packs-61** |
| NOTICE `[pack: <slug>]` ×7 | all present |
| catalog `updated` | **2026-08-16** |
| check_release.py | **PASS** |

### federal-bca source_version (catalog)
`Circular A-94 (2023-11-09) only; Army CBA excluded at build (source unreachable)`

### Slug-set assert
`{'dod-vva-rpg','faa-std-025','dote-te-guidebook','dafman-63-119','mil-std-881f','federal-bca','mil-std-40051'} ⊆ catalog` — ok

### docs/packs.html
Regenerated via `python tooling/gen_packs_page.py` (63 packs listed).

### Version surfaces
Not touched (Phase 9): CHANGELOG, plugin 1.17.0→1.18.0, RELEASE-INFO.

## Cluster-target baseline (Phase 8 asserts)

Copied from 7-RESEARCH.md §5:

| Pack | Baseline clusters targeted (entries / distinct packs before) | Post-build expectation (Phase 8 asserts) |
|---|---|---|
| GP-01 `dod-vva-rpg` | 8 (3/2 THIN), 7 (9/2), 16 (2/2 THIN), 9 (11/1) | 8 becomes count-adequate; 16 fattened; 9 diversity fixed (2nd+ pack); 7 diversity improved |
| GP-02 `faa-std-025` | 5 (2/2 THIN), 3 (2/2 THIN), 12 (14/5) | 5 and 3 fattened (THIN-count exit requires ≥8 entries — partial; record actuals) |
| GP-03 `dote-te-guidebook` | 9 (11/1 single-source), 7, 8, 23 (11/1) | 9 and 23 single-source risk broken; 7/8 strengthened |
| GP-04 `dafman-63-119` | 9, 6 (3/3 THIN), 27 (7/6 THIN) | 6 and 27 fattened; 9 diversity |
| GP-05 `mil-std-881f` | 17 (6/5 THIN), 26 (66/11) | 17 fattened toward ≥8 |
| GP-06 `federal-bca` | 15 (1/1 worst), 16, 17 | 15 no longer worst/1-pack; 16/17 fattened |
| GP-07 `mil-std-40051` | 25 (0/0 **EMPTY**), 24 (6/4 THIN) | **25 non-empty** (ROADMAP Phase 8 SC-2 hard requirement); 24 fattened |

## Deviations from Plan

| # | Deviation | Plan reference | Proposed classification | Rationale |
|---|-----------|----------------|--------------------------|-----------|
| 1 | DIST-A via DEBoK PD metadata + OSD/OUSD OPR (not in-PDF DIST-A sentence) | Task 1 P7-PRE-4 | in-scope fix | Cover text layer has no DIST-A block; DEBoK Copyright=Public Domain on every chapter + DoD RPG body authorship; same metadata-evidence pattern as mil-std-881f |
| 2 | DEBoK OTMM guest session for PDF binaries (not raw de-bok.org/search HTML) | Task 1 fetch | in-scope fix | SPA search URLs are not direct PDFs; guest OTMM rendition API is the live download path behind cto.mil links |
| 3 | Dropped T&E/V&V Checklist from chapter set (selection) | Task 1 8–10 set | in-scope fix | Kept 10 chapters in band; checklist PD confirmed; recorded as selection drop not licence drop |
| 4 | Included vv-new-pr (V&V Agent) after index mis-linked environment-pr for that role | Task 1 chapter set | in-scope fix | Filename vv-new-pr.pdf resolves correctly via DEBoK search |

### Auto-fixed Issues

**1. [Rule 2 - Critical] P7-PRE-4 metadata DIST evidence path**
- **Found during:** Task 1 licence gate
- **Issue:** No chapter PDF text layer contained “DISTRIBUTION STATEMENT A”
- **Fix:** Per-chapter DEBoK Copyright=Public Domain + OPR/Author OSD/OUSD R&E; provenance header + PACK.yaml notes
- **Files modified:** packs/dod-vva-rpg/PACK.yaml (notes), sources build full_texts (gitignored)
- **Commit:** `3b5b2f7`

## Full-phase verification (7 packs)

```
PASS dod-vva-rpg, faa-std-025, dote-te-guidebook, dafman-63-119,
     mil-std-881f, federal-bca, mil-std-40051
RELEASE CHECK: PASS — repo is release-ready against the mechanical gate.
```

## check_release output (final)

```
RELEASE CHECK: PASS — repo is release-ready against the mechanical gate.
```

## Count evidence (final)

```
catalog 61
cursor 62
packs 63
SKILLS.md: 61 packs (+2 signposts) in this release...
README badge: packs-61
NOTICE: [pack: faa-std-025|dote-te-guidebook|dafman-63-119|federal-bca|mil-std-881f|mil-std-40051|dod-vva-rpg] all present
slug-set ok
catalog.updated: 2026-08-16
```

## Self-Check: PASSED

- FOUND: packs/dod-vva-rpg/{SKILL.md,PACK.yaml,LICENSE,chapters/×10,glossary,patterns,cheatsheet}
- FOUND: commits `3b5b2f7`, `e00ac7d`
- FOUND: catalog 61, cursor 62, packs 63, check_release PASS
