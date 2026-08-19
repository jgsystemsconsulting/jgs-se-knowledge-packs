---
phase: 3-tier-1-packs-public-domain
plan: 03
subsystem: knowledge-packs
tags: [tier-1, nasa, doe, registration, public-domain, multi-document]

requires:
  - phase: 3-tier-1-packs-public-domain
    provides: 3-01 Batch A packs + 3-02 Batch B packs + pipeline exemplars
  - phase: 2-source-vetting-ruled-out-register
    provides: vetted Tier-1 source list and URLs
provides:
  - packs/nasa-ms-7009 validated Tier-1 pack (T1-05, two-PDF)
  - packs/doe-413-3b validated Tier-1 pack (T1-06, consolidated Order)
  - catalog/SKILLS/NOTICE/packs.html/README/index registration for all 8 Tier-1 packs
  - check_release PASS (54 catalog / 56 directory basis)
affects:
  - phase 5 release gate (catalog basis established)

actuals:
  tokens: 18500
  tasks: 3
  commits: 4

tech-stack:
  added: []
  patterns:
    - two-PDF pack with dual work_dir_std/hdbk + dual check_overlap
    - successor-document build when library supersedes named Chg PDF (413.3C)
    - single closing registration commit for all 8 Tier-1 packs incl. MJ-01 surfaces

key-files:
  created:
    - packs/nasa-ms-7009/**
    - packs/doe-413-3b/**
  modified:
    - catalog.json
    - SKILLS.md
    - docs/packs.html
    - NOTICE
    - README.md
    - docs/index.html

key-decisions:
  - "nasa-ms-7009 source_pages=263 (STD 88 + HDBK 175 metadata sum); 7 chapters STD spine + HDBK depth"
  - "doe-413-3b built from DOE O 413.3C (2026-08-05) which cancels O 413.3B Chg 7; slug retained for T1-06"
  - "Registration includes MJ-01 README badge + docs/index.html publisher group counts"

patterns-established:
  - "MN-05: work_dir_std.txt + work_dir_hdbk.txt for multi-PDF packs"
  - "MJ-01: registration must bump README packs badge and docs/index.html catalogue counts"

requirements-completed: [T1-05, T1-06]

coverage:
  - id: D1
    description: "nasa-ms-7009 pack built from STD-7009B + HDBK-7009B, dual overlap clean, committed"
    requirement: T1-05
    verification:
      - kind: other
        ref: "python tooling/validate_pack.py packs/nasa-ms-7009"
        status: pass
      - kind: other
        ref: "check_overlap STD + HDBK exit 0"
        status: pass
    human_judgment: false
  - id: D2
    description: "doe-413-3b pack built from consolidated capital-asset Order PDF; copyright clear; committed"
    requirement: T1-06
    verification:
      - kind: other
        ref: "python tooling/validate_pack.py packs/doe-413-3b"
        status: pass
      - kind: other
        ref: "in-PDF copyright scan; check_overlap exit 0"
        status: pass
    human_judgment: false
  - id: D3
    description: "Registration sweep for all 8 Tier-1 packs; check_release PASS"
    verification:
      - kind: other
        ref: "python tooling/check_release.py"
        status: pass
    human_judgment: false

duration: 90min
completed: 2026-08-15
status: complete
---

# Phase 3 Plan 03: Batch C Multi-Doc Packs + Registration Summary

**nasa-ms-7009 (two-PDF M&S standard+handbook) and doe-413-3b (capital-asset Order) shipped with full gates, then one registration commit synchronized all 8 Tier-1 packs through catalog/SKILLS/NOTICE/packs.html/README/index with check_release PASS.**

## Performance

- **Duration:** ~90 min
- **Tasks:** 3/3
- **Commits:** 2 pack commits + 1 registration commit + 1 docs SUMMARY commit

## Per-task results

| Task | Deliverable | Commit | Key gates |
|------|-------------|--------|-----------|
| 1 | packs/nasa-ms-7009 | `7767a7b` | validate PASS; overlap STD+HDBK exit 0; scan PASS; MN-01 PASS |
| 2 | packs/doe-413-3b | `570adf3` | validate PASS; overlap exit 0; scan PASS; copyright clear; MN-01 PASS |
| 3 | Registration ×8 | `863bfeb` | check_release PASS; catalog 54/tier1 50; SKILLS 8 rows; MJ-01 badge+index |

### Task 1 — nasa-ms-7009 (T1-05)

- Downloaded NASA-STD-7009B (88 pp extract) + NASA-HDBK-7009B (175 pp extract) from standards.nasa.gov.
- `work_dir_std.txt` / `work_dir_hdbk.txt` recorded (MN-05).
- Licence: `Public Domain (US Government work, 17 U.S.C. § 105)`.
- **source_pages=263** (88+175); PACK.yaml notes two-source build naming STD-7009B + HDBK-7009B (MN-02).
- 7 chapters: programmatics/criticality; development evidence/capability; V&V; uncertainty/sensitivity; use/results; risk/reporting; HDBK life-cycle depth.
- SKILL.md: `## When to use` + `**Prerequisites:**` present.
- Dual `check_overlap` exit 0; `scan_generated_skill` PASS; `validate_pack` PASS.
- Commit scoped to `packs/nasa-ms-7009/**` only; MN-01 leak check PASS.

### Task 2 — doe-413-3b (T1-06)

- Directives library current capital-asset Order is **DOE O 413.3C** (approved 2026-08-05), media `energy.gov/media/364627`, which **cancels DOE O 413.3B Chg 7** (2023-06-21). Chg 7 PDF is no longer the library current entry; consolidated successor used.
- Pack slug remains `doe-413-3b` for T1-06 continuity; provenance recorded in PACK.yaml notes + LICENSE + SKILL Scope.
- Extract metadata **source_pages=132**; `work_dir.txt` recorded.
- **In-PDF third-party copyright check:** zero `copyright` / `©` / `all rights reserved` hits; ANSI only as invoked-standards citations. Proceeded.
- 6 chapters: purpose/applicability; CD-0–CD-4; acquisition/IPT; PB/cost/schedule/EVMS; risk/safety/exceptions; reviews/responsibilities/CRD.
- validate / overlap / scan all PASS; When-to-use + Prerequisites present; MN-01 PASS.

### Task 3 — Registration sweep (all 8)

| Surface | Update |
|---------|--------|
| catalog.json | +8 live tier-1 entries; `updated=2026-08-15`; **54 packs / 50 tier-1** |
| SKILLS.md | header **54 packs (+2 signposts)**; 8 backtick-slug rows |
| docs/packs.html | `python tooling/gen_packs_page.py` (56 packs incl. signposts) |
| NOTICE | 8 `[pack: …]` Public Domain blocks |
| README.md | badge **packs-54** (MJ-01) |
| docs/index.html | **54 packs · 2 signposts**; NASA 15; DoD 13; NIST 9; DOE 2; CISA/DHS 1 (MJ-01) |

**check_release.py:** `RELEASE CHECK: PASS — repo is release-ready against the mechanical gate.`

Chapter counts registered: nist-800-171=8, nist-800-61=6, cisa-cpg=5, doe-sem=7, mil-hdbk-338=9, mil-hdbk-516=8, nasa-ms-7009=7, doe-413-3b=6.

## MUST-ADDRESS resolutions

| ID | Resolution |
|----|------------|
| MJ-01 | Registration updated README packs badge (46→54) and docs/index.html heading + publisher group counts (NASA+1, DoD+2, NIST+2, DOE+2 group, CISA/DHS+1 group). |
| MN-01 | `git show --name-only` on `7767a7b`, `570adf3`, `863bfeb` — zero `sources/` or `full_text` paths. |
| MN-02 | Both PACK.yaml `build:` blocks have real source_pages/chapters/built_on; no TODO. |
| MN-05 | nasa: work_dir_std.txt + work_dir_hdbk.txt; doe: work_dir.txt via path bytes without CRLF junk. |
| MN-07 | SKILLS.md contains all 8 new backtick-slug rows (count==8); header 54. |
| doe copyright | Halt-and-surface check run first post-extract: **no third-party copyright notices** — proceeded. |
| nasa dual | Two extractions, summed pages, dual overlap, STD requirements spine + HDBK depth chapters. |

## Deviations from Plan

| # | Deviation | Plan reference | Proposed classification | Rationale |
|---|-----------|----------------|--------------------------|-----------|
| 1 | extract `--install-missing no` | pipeline | in-scope fix | Non-interactive agent; pdftotext fallback supported |
| 2 | build_pack `--force` | scaffold | in-scope fix | Third-party-quote advisory for US-gov publishers |
| 3 | doe source = O 413.3C not Chg 7 PDF body | Task 2 download | in-scope fix | Library current consolidated Order cancels Chg 7; same subject; provenance documented |
| 4 | STD pages 88 / HDBK 175 vs ~30+100 est. | Task 1 | in-scope fix | metadata.json authoritative; sum 263 used |
| 5 | MJ-01 README + index.html beyond plan files_modified list | Task 3 / folded finding | in-scope fix | User MUST-ADDRESS MJ-01; no gate otherwise |
| 6 | doe chapters 6 (plan 5–7) | Task 2 | in-scope fix | Within guidance band |

### Auto-fixed Issues

None beyond expected scaffold `--force` and non-interactive extract flags.

## Accomplishments

- Completed Phase 3 Batch C multi-document + order packs
- Closed registration for all 8 Tier-1 packs from 3-01/3-02/3-03
- Established Phase 5 gate basis: **54 catalog / 56 directory**, check_release PASS
- Zero sources/ leakage on pack and registration commits

## Self-Check: PASSED

- FOUND: packs/nasa-ms-7009/SKILL.md, PACK.yaml, LICENSE, chapters/ (7)
- FOUND: packs/doe-413-3b/SKILL.md, PACK.yaml, LICENSE, chapters/ (6)
- FOUND commits: 7767a7b, 570adf3, 863bfeb
- validate_pack PASS ×2; dual+single overlap exit 0; scan PASS ×2
- check_release PASS (fresh run after registration)
- MN-01 PASS ×3; MJ-01 surfaces updated
