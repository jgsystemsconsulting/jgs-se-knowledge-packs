---
phase: 3-tier-1-packs-public-domain
plan: 01
subsystem: knowledge-packs
tags: [tier-1, nist, cisa, doe, public-domain, pack-build]

requires:
  - phase: 2-source-vetting-ruled-out-register
    provides: vetted Tier-1 source list and URLs (2-RESEARCH)
  - phase: 3-tier-1-packs-public-domain
    provides: 3-RESEARCH pipeline and build sheets
provides:
  - packs/nist-800-171 validated Tier-1 pack
  - packs/nist-800-61 validated Tier-1 pack
  - packs/cisa-cpg validated Tier-1 pack (P3-PRE-1 proven)
  - packs/doe-sem validated Tier-1 pack
  - P3-PRE-2 accepted-gap record for SUMMARY consumers
affects:
  - 3-02 (remaining Tier-1 packs)
  - 3-03 (registration: catalog.json, SKILLS.md, gen_packs_page, NOTICE, check_release)

actuals:
  tokens: 44325
  tasks: 4
  commits: 5

tech-stack:
  added: []
  patterns:
    - jgs-reference-skill extract→outline→scaffold→synthesize→validate→scan→overlap
    - work_dir.txt via printf; preserve book_skill_work under sources/<slug>/
    - statute-bearing PD licence string for all Tier-1 packs

key-files:
  created:
    - packs/nist-800-171/**
    - packs/nist-800-61/**
    - packs/cisa-cpg/**
    - packs/doe-sem/**
  modified: []

key-decisions:
  - "cisa-cpg: no separate CPG 2.0 controls-list PDF at build; used main report (36pp) + slick sheet (2pp); goals sliced from main report only"
  - "doe-sem source_pages=318 from extract metadata.json (not PDF page-object count 135)"
  - "nist-800-61 source_pages=48 from metadata (build-sheet est. ~68)"
  - "extract.py --install-missing no (docling absent; pdftotext fallback)"

patterns-established:
  - "Per-pack sources/<slug>/book_skill_work copy so TEMP is not clobbered across packs"
  - "SKILL.md always includes ## When to use + **Prerequisites:** (rr-s-13)"
  - "build_pack.py --force for NIST third-party-quote advisory"

requirements-completed: [T1-01, T1-02, T1-07, T1-08]

coverage:
  - id: D1
    description: "nist-800-171 pack built, validated, overlap-clean, committed"
    requirement: T1-01
    verification:
      - kind: other
        ref: "python tooling/validate_pack.py packs/nist-800-171"
        status: pass
      - kind: other
        ref: "python REF/tools/check_overlap.py --pack packs/nist-800-171"
        status: pass
    human_judgment: false
  - id: D2
    description: "nist-800-61 pack built, validated, overlap-clean, committed"
    requirement: T1-02
    verification:
      - kind: other
        ref: "python tooling/validate_pack.py packs/nist-800-61"
        status: pass
      - kind: other
        ref: "python REF/tools/check_overlap.py --pack packs/nist-800-61"
        status: pass
    human_judgment: false
  - id: D3
    description: "cisa-cpg pack built with P3-PRE-1 licence string; dual overlap; committed"
    requirement: T1-07
    verification:
      - kind: other
        ref: "vet_source.py CISA + statute licence → tier 1"
        status: pass
      - kind: other
        ref: "check_overlap main + slick; validate_pack cisa-cpg"
        status: pass
    human_judgment: false
  - id: D4
    description: "doe-sem pack built after in-PDF copyright check; validated; committed"
    requirement: T1-08
    verification:
      - kind: other
        ref: "python tooling/validate_pack.py packs/doe-sem"
        status: pass
      - kind: other
        ref: "in-PDF copyright scan (no © notices)"
        status: pass
    human_judgment: false

duration: 90min
completed: 2026-08-14
status: complete
---

# Phase 3 Plan 01: Batch A Tier-1 Packs Summary

**Four born-digital Tier-1 packs (nist-800-171, nist-800-61, cisa-cpg, doe-sem) built via the shared extract→scaffold→synthesize→validate→overlap pipeline, each with one scoped commit and no sources/ leakage.**

## Performance

- **Duration:** ~90 min
- **Tasks:** 4/4
- **Commits:** 4 pack commits + 1 docs SUMMARY commit

## Per-pack results

| Pack | Commit | Pages | Chapters | validate_pack | check_overlap | scan_generated_skill | When-to-use / Prerequisites | MN-01 leak |
|------|--------|-------|----------|---------------|---------------|----------------------|-----------------------------|------------|
| nist-800-171 | `c6820a7` | 120 | 8 | PASS | exit 0 (after glossary paraphrase) | PASS (no findings) | 1 / 1 | PASS |
| nist-800-61 | `5e4663d` | 48 | 6 | PASS | exit 0 | PASS | 1 / 1 | PASS |
| cisa-cpg | `62bd340` | 38 (36+2) | 5 | PASS | exit 0 ×2 (main+slick) | PASS | 1 / 1 | PASS |
| doe-sem | `301a47d` | 318 | 7 | PASS | exit 0 | PASS | 1 / 1 | PASS |

### nist-800-171 (T1-01)
- DOI-stable nvlpubs PDF; vet tier 1 (NIST third-party advisory expected).
- Families 3.1–3.17 grouped into 8 chapters + glossary/patterns/cheatsheet.
- Overlap: one glossary definition hit ≥12 words; paraphrased before final commit amend (`c6820a7`).
- PACK.yaml build: source_pages 120, chapters 8, built_on 2026-08-14 (MN-02 verified).

### nist-800-61 (T1-02)
- nvlpubs SP 800-61r3; metadata **48 pages** (build-sheet estimate was ~68 — actual used).
- 6 chapters: scope shift, CSF life cycle, roles/playbooks, Table 2 prep profile, Table 3 DE/RS/RC, coordination/training.
- outline.py weak on this PDF; structure taken from body offsets manually.
- PACK.yaml build complete (MN-02).

### cisa-cpg (T1-07) — P3-PRE-1
- Licence string **exactly** `Public Domain (US Government work, 17 U.S.C. § 105)` at vet and scaffold → tier 1 exit 0.
- Main: `CPG_Report_2.0_508c.pdf` (36 pp, Dec 2025). Secondary: `CPG_Slicksheet_508c.pdf` (2 pp).
- **MN-04:** No separate CPG 2.0 “controls-list” PDF was published on cisa.gov at build time (probed resource pages and filename patterns). Full goal inventory (outcome + recommended action) lives in the main report and was **sliced into chapters**. Slick sheet was **extracted and overlap-checked only** (overview/NSM-5/CSF alignment); not chapter-sliced.
- work_dir_main.txt / work_dir_ctrl.txt recorded; dual overlap exit 0.

### doe-sem (T1-08)
- energy.gov SEM3_1231.pdf; publisher "US Department of Energy" hits US_GOV signal.
- **In-PDF third-party copyright check:** no `copyright` / `©` / `all rights reserved` notices. IEEE/SEI appearances are bibliographic citations only. Proceeded.
- source_pages **318** from metadata.json (file(1) reported 135 page objects — pack uses extract metadata).
- 7 chapters covering intro, lifecycle+quality gates, planning, requirements/functional design, system design/construction, test/acceptance, maintenance.
- P3-PRE-2 accepted gap recorded below.

## P3-PRE-2 (accepted gap — record only)

Accepted gap: vet_source.py lacks ecss/esa/def-stan/dstan EXCLUDED signals; the human rubric governs, the tool under-blocks, and none of the affected sources appear in Phase 3 build lists. External-repo fix scheduled as follow-up.

## MUST-ADDRESS resolutions

| ID | Resolution |
|----|------------|
| MJ-01 | **Skipped this plan** (registration is 3-03). See registration notes below for 3-03 executor. |
| MN-01 | After each pack commit: `git show --name-only <sha>` — zero `sources/` or `full_text.txt` paths on all four commits. |
| MN-02 | Manual PACK.yaml `build:` check per pack: real source_pages/chapters/built_on; no TODO stubs. |
| MN-04 | cisa-cpg: controls-list PDF absent; main report sliced; slick referenced/extracted only (see above). |
| MN-05 | work_dir files written with `printf '%s'`; read with `tr -d '\r\n'`. |
| MN-06 | n/a |

## Registration notes for 3-03 executor (MJ-01)

Do **not** assume README badge or docs/packs.html counts were updated in 3-01 — they were intentionally not touched.

When registering these four packs, 3-03 must:

1. **catalog.json** — add four pack objects (slug, title, publisher, source_version, license, license_tier: 1, commercial_use: true, chapters, status: live); bump `updated`.
2. **SKILLS.md** — add four table rows; **bump header pack count** (+4).
3. **README badge / pack count** — bump any displayed total (48→52 after this batch alone; full Phase 3 target 56 after all eight Tier-1 packs).
4. **docs/packs.html** — regenerate via `python tooling/gen_packs_page.py` (do not hand-edit); verify freshness for check_release RR-B-30.
5. **NOTICE** — four `[pack: <slug>]` Public Domain attribution blocks.
6. **check_release.py** — final PASS after registration (Phase 5 gate basis).

Chapter counts to register: nist-800-171=8, nist-800-61=6, cisa-cpg=5, doe-sem=7.

## Deviations from Plan

| # | Deviation | Plan reference | Proposed classification | Rationale |
|---|-----------|----------------|--------------------------|-----------|
| 1 | extract `--install-missing no` (not `ask`) | Task 1 step 3 | in-scope fix | Non-interactive agent; docling missing; pdftotext fallback is supported |
| 2 | build_pack `--force` for NIST packs | Task 1/2 scaffold | in-scope fix | NIST third-party-quote advisory blocks scaffold without --force; advisory dispositioned in notes |
| 3 | nist-800-61 pages 48 vs ~68 estimate | Task 2 done criteria | in-scope fix | metadata.json is authoritative per RESEARCH |
| 4 | cisa secondary = slick sheet, not controls-list PDF | Task 3 | in-scope fix | Controls-list PDF not published for 2.0; MN-04 documents disposition |
| 5 | doe-sem pages 318 vs unknown | Task 4 | in-scope fix | metadata.json actual |
| 6 | nist-800-171 first commit amended after overlap fix | Task 1 verify | in-scope fix | Kept one commit per pack; HEAD was ours unpushed |
| 7 | outline.py low quality on 800-61/CISA; manual section offsets | Tasks 2–3 | in-scope fix | Synthesis still slice-grounded from full_text |

### Auto-fixed Issues

**1. [Rule 1 - Bug] Overlap hit in nist-800-171 glossary**
- **Found during:** Task 1 verify
- **Issue:** verbatim ≥12-word run on nonfederal system definition
- **Fix:** paraphrased glossary entry; re-ran overlap exit 0; amended pack commit
- **Files modified:** packs/nist-800-171/glossary.md
- **Commit:** c6820a7

## Accomplishments

- Shipped 4 validated Tier-1 packs (50 files under packs/)
- Proved P3-PRE-1 (CISA statute-bearing licence → tier 1)
- Recorded P3-PRE-2 accepted gap
- Zero source PDF / full_text commits (MN-01)
- All SKILL.md files satisfy rr-s-13 When-to-use + Prerequisites

## Self-Check: PASSED

- FOUND: packs/nist-800-171/SKILL.md, PACK.yaml, LICENSE, chapters/
- FOUND: packs/nist-800-61/SKILL.md, PACK.yaml, LICENSE, chapters/
- FOUND: packs/cisa-cpg/SKILL.md, PACK.yaml, LICENSE, chapters/
- FOUND: packs/doe-sem/SKILL.md, PACK.yaml, LICENSE, chapters/
- FOUND commits: c6820a7, 5e4663d, 62bd340, 301a47d
- validate_pack PASS ×4 on final sweep
