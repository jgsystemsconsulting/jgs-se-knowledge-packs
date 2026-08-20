---
phase: 15-source-retries
plan: 01
subsystem: docs-vetting
tags: [source-vetting, fut-04, aaf, rosap, deferred-with-evidence, link-policy]

requires:
  - phase: 10-source-vetting
    provides: FUT-04 DEFERRED + AAF Excluded-pending + GP-06 A-94-only + 10-RESEARCH locators
  - phase: 14-ledger-planning-hygiene
    provides: live VET-20 open boxes + clean v1.19.1 planning surfaces
provides:
  - "v1.19.1 retry Not-cleared section with dated FUT-04 / AAF / ROSAP evidence"
  - "Phase 16 handoff table (2 NO-GO + 1 document-only)"
  - "15-RESEARCH execute-day URL/command store (ASAFM 403, AAF 403/404, ROSAP 403)"
  - "REQUIREMENTS VET-20-01..03 parentheticals (boxes still open)"
  - "STATE Phase 15 deviations bullet"
affects: [16-pack-builds-if-cleared, phase-verify, phase.complete]

actuals:
  tokens: 4592
  tasks: 3
  commits: 3

tech-stack:
  added: []
  patterns:
    - "dated deferred-with-evidence retry (no pack)"
    - "Link Policy: scheme strings only in 15-RESEARCH.md"
    - "Phase N handoff GO/NO-GO table for next pack phase"

key-files:
  created:
    - .planning/phases/15-source-retries/15-01-SUMMARY.md
  modified:
    - docs/SOURCE-VETTING.md
    - .planning/phases/15-source-retries/15-RESEARCH.md
    - .planning/REQUIREMENTS.md
    - .planning/STATE.md

key-decisions:
  - "FUT-04 remains DEFERRED — ASAFM PDF 403 Akamai; no in-source grant; not Tier 1; not new Excluded cell"
  - "AAF Product Support + Software pathway remains NOT yet vetted — do not use; Excluded-pending kept"
  - "ROSAP Rev E optional check is document-only; faa-std-025 Rev F pack untouched"
  - "WarU legacy pdfviewer path returned 404 on execute-day (research-wave had 403); successor aaf.waru.edu/guidebooks/ is Cloudflare 403 challenge — both recorded honestly"

patterns-established:
  - "v1.19.1 retry section between Phase 11 handoff and Def Stan"
  - "GP-0N row suffixes for retry notes without dual-source restore"
  - "VET-20 parentheticals without ticking boxes (verify owns ticks)"

requirements-completed: [VET-20-01, VET-20-02, VET-20-03]

coverage:
  - id: D1
    description: "FUT-04 Army CBA dated 2026-08-20 DEFERRED with ASAFM PDF 403 evidence in 15-RESEARCH + SOURCE-VETTING"
    requirement: VET-20-01
    verification:
      - kind: other
        ref: "python assert heading order + DEFERRED + ASAFM AkamaiGHost 403 in 15-RESEARCH; grep -c http SOURCE-VETTING = 0"
        status: pass
    human_judgment: false
  - id: D2
    description: "AAF unused Excluded-pending + Not-cleared bullet + Phase 16 NO-GO; ROSAP document-only handoff"
    requirement: VET-20-02
    verification:
      - kind: other
        ref: "python assert Phase 16 handoff 2x NO-GO + document-only; AAF row 2026-08-20; sec19 NOT yet vetted"
        status: pass
    human_judgment: false
  - id: D3
    description: "Optional ROSAP Rev E vs faa-std-025 Rev F documented only; GP-02 suffix; no pack rebuild"
    requirement: VET-20-03
    verification:
      - kind: other
        ref: "python assert ROSAP + no rebuild in register; 15-RESEARCH ROSAP 403 + FAA path 404; git diff packs/ empty"
        status: pass
    human_judgment: false
  - id: D4
    description: "VET-20-01..03 parentheticals dated; boxes open; STATE Phase 15 bullet"
    verification:
      - kind: other
        ref: "python assert three VET-20 and three PACK-20 lines start with '- [ ]' and VET lines contain 2026-08-20"
        status: pass
    human_judgment: false

duration: 4min
completed: 2026-08-20
status: complete
---

# Phase 15 Plan 01: Source Retries Summary

**Dated 2026-08-20 retry evidence for Army CBA (FUT-04 DEFERRED 403), AAF (still NOT yet vetted), and optional ROSAP (document-only); zero packs; Link Policy holds.**

## Performance

- **Duration:** ~4 min
- **Started:** 2026-08-20T10:12:01Z
- **Completed:** 2026-08-20T10:15:23Z
- **Tasks:** 3/3
- **Files modified:** 4 (docs + planning only)

## Accomplishments

- Inserted exactly one `### Not cleared this session (v1.19.1 retry)` after Phase 11 handoff and before Def Stan, with 15-RESEARCH pointer and dated FUT-04 / AAF / ROSAP bullets.
- Recorded execute-day fetches in 15-RESEARCH.md: ASAFM PDF 403 AkamaiGHost 489-byte HTML deny; WarU PSM pdfviewer 404; aaf.dau.edu 301 → aaf.waru.edu/guidebooks/ Cloudflare 403 challenge; ROSAP 42955 403; guessed FAA Rev F path 404.
- Phase 16 handoff table: Army CBA NO-GO, AAF NO-GO, ROSAP document-only — no forced rebuild of `faa-std-025`.
- Annotated live VET-20-01..03 with 2026-08-20 parentheticals; left VET-20 and PACK-20 boxes unchecked.
- `grep -c http docs/SOURCE-VETTING.md` = 0; `git diff --name-only -- packs/` empty across plan.

## Task Commits

1. **Task 1 (tracer): End-to-end FUT-04 dated retry** - `925206c` (docs)
2. **Task 2: AAF unused + ROSAP optional note** - `393d834` (docs)
3. **Task 3: Annotate VET-20 parentheticals + STATE** - `fdc7b10` (docs)

**Plan metadata:** (pending final docs commit)

## Files Created/Modified

- `docs/SOURCE-VETTING.md` — v1.19.1 Not-cleared section, GP-06/GP-02/AAF/DAG suffixes, Phase 16 handoff
- `.planning/phases/15-source-retries/15-RESEARCH.md` — execute-day VET-20-01/02/03 command store
- `.planning/REQUIREMENTS.md` — VET-20-01..03 italic parentheticals (boxes open)
- `.planning/STATE.md` — Phase 15 (2026-08-20) deviations bullet only (YAML frontmatter untouched by task)

## Decisions Made

- No in-source redistribution grant obtained for Army CBA or AAF → both stay unused for pack builds.
- Execute-day WarU legacy path is **404** (not planner's research-wave 403); successor guidebooks path is Cloudflare **403 challenge** — both codes recorded; verdict unchanged (NOT yet vetted).
- ROSAP unreachable does not force faa-std-025 rebuild; shipped Rev F stands.
- Live VET-20/PACK-20 boxes deliberately left open for verify / phase.complete.

## Deviations from Plan

### Auto-fixed / execute-day code deltas

**1. [Rule 1 - Bug / evidence honesty] WarU PSM path status code differs from planner HEAD**
- **Found during:** Task 2 (live curl)
- **Issue:** Plan claim_verification and research-wave Fresh Evidence recorded WarU pdfviewer PSM path as 403 Cloudflare. Execute-day HEAD returned **404 Not Found** (Cloudflare server). Successor `aaf.waru.edu/guidebooks/` is the 403 Cloudflare challenge (`Cf-Mitigated: challenge`).
- **Fix:** Recorded actual codes in 15-RESEARCH.md §VET-20-02. Published register wording uses "successor-host challenge 403" (accurate for the guidebooks path) and does not invent a grant from the 404 or landing 200.
- **Files modified:** `15-RESEARCH.md`, `docs/SOURCE-VETTING.md`
- **Commit:** `393d834`

### plan_review MJ resolutions

**MJ-01 — Task 1 automated python TAB IndentationError**
- **Resolution:** Detabbed verify blocks to spaces-only before running. Task 1 (and Tasks 2–3) python asserts executed successfully and printed `VET20_01_TRACER_OK` / `VET20_02_03_OK` / `VET20_ANNOTATIONS_OK`.
- **Evidence:** executor ran space-indented python -c; no IndentationError.

**MJ-02 — Naive `assert '403' in rs` if WarU already has 403**
- **Resolution:** Did not rely on bare `403 in rs` alone for pass criteria. Task 1 verify required execute-day block markers: `Execute-day evidence (2026-08-20)`, `VET-20-01`, `ASAFM`, `403 Forbidden`, `AkamaiGHost`, and `Cost Benefit Analysis`. Task 2 required `### VET-20-02` / `### VET-20-03`, `aaf.waru.edu/guidebooks/`, ROSAP locator, and FAA Rev F `404 Not Found`. GP-06 suffix assertion used the exact dated string `v1.19.1 retry 2026-08-20: official ASAFM PDF still 403`.
- **Evidence:** python asserts in executor session (stronger than plan's minimal 403 check).

**MJ-03 — Greps for "unused" may hit pre-existing v1.19.0 rows; NO-GO==2 hard-require**
- **Resolution:** Scoped AAF/ROSAP content checks to the split section after `### Not cleared this session (v1.19.1 retry)` (and Phase 16 handoff subsection). Did not hard-require global unique "unused" greps. Phase 16 table has exactly two `| NO-GO —` rows and one `document-only` (expected NO-GO path; no GO because no opened-PDF grant). AAF Excluded-table row count remains 1 (no second row).
- **Evidence:** `sec19` scoped asserts; `sec16.count('| NO-GO —') == 2`; `aaf_excluded_rows 1`.

### Other deviations

None beyond execute-day status-code honesty and MJ-hardening of verifies.

## Auth Gates

None.

## Known Stubs

None. No placeholder grants, no empty pack scaffolds, no TODO licence claims.

## Claim verification

Live commands this executor session (2026-08-20), cwd repo root.

| claim | command / check | observed | status |
|---|---|---|---|
| Branch main | `git branch --show-current` | `main` | PASS |
| ASAFM PDF | `curl -sI` ASAFM Cost Benefit Analysis PDF | `HTTP/1.1 403 Forbidden` AkamaiGHost `text/html` 489 | PASS |
| armypubs host | `curl -sI` armypubs.army.mil | `200 OK` HTML (not a grant) | PASS |
| WarU PSM pdfviewer | `curl -sI` waru.edu pdfviewer PSM path | `404 Not Found` Cloudflare | PASS (code delta vs research-wave 403) |
| aaf.dau.edu guidebooks | `curl -sI` | `301` → `https://aaf.waru.edu/guidebooks/` | PASS |
| aaf.waru.edu/guidebooks/ | `curl -sI` | `403` Cloudflare `Cf-Mitigated: challenge` | PASS |
| aaf.waru.edu root | `curl -sI` | `200 OK` HTML landing (not a grant) | PASS |
| ROSAP 42955 | `curl -sI` rosap.ntl.bts.gov/view/dot/42955 | `403 Forbidden` Akamai HTML 397 | PASS |
| FAA host | `curl -sI` faa.gov | `200 OK` | PASS |
| Guessed FAA Rev F path | `curl -sI` documentLibrary … FAA_Standard_025_Rev_F.pdf | `404 Not Found` | PASS |
| Link Policy | python `'http' not in sv.lower()` / conceptual `grep -c http` | 0 | PASS |
| v1.19.1 heading once, ordered | python i11 < i19 < i_ds; count==1 | PASS | PASS |
| Phase 16 handoff | heading + 2 NO-GO + document-only | PASS | PASS |
| VET-20 boxes open | three `- [ ] **VET-20-0N**` with 2026-08-20 | PASS | PASS |
| PACK-20 boxes open | three `- [ ] **PACK-20-0N**` | PASS | PASS |
| packs/ clean | `git diff --name-only -- packs/` | empty | PASS |
| faa-std-025 untouched | PACK.yaml source_version still Rev F everyspec | unchanged | PASS |
| Task1 verify | python VET20_01_TRACER_OK (spaces, MJ-02 hardened) | printed OK | PASS |
| Task2 verify | python VET20_02_03_OK (MJ-02/03 scoped) | printed OK | PASS |
| Task3 verify | python VET20_ANNOTATIONS_OK | printed OK | PASS |

## must_haves evidence

| truth | result |
|---|---|
| v1.19.1 Not-cleared heading after Phase 11, before Def Stan | PASS (ordered indices; count==1) |
| FUT-04 dated 2026-08-20 DEFERRED with ASAFM 403; not Vetted Tier 1; not new Excluded cell | PASS |
| AAF + Software pathway NOT yet vetted — do not use; Excluded-pending present | PASS (sec19 + one Excluded row) |
| ROSAP optional document-only 2026-08-20; no forced rebuild | PASS |
| 15-RESEARCH.md pointer in SOURCE-VETTING | PASS |
| `grep -c http` SOURCE-VETTING = 0 | PASS |
| VET-20-01..03 unchecked + 2026-08-20 parentheticals | PASS |
| STATE Phase 15 (2026-08-20) bullet; YAML progress not task-edited | PASS |
| No packs/ edits | PASS |
| Idempotency: single v1.19.1 heading | PASS |
| Concurrency: single-writer sequential tasks | PASS |

## Threat Flags

None new. Mitigations T-15-01..07 applied: scheme-string count 0; no Tier 1 invent; packs/ empty; boxes open; pathspec commits; dated notes.

## Self-Check: PASSED

| check | result |
|---|---|
| `docs/SOURCE-VETTING.md` exists with v1.19.1 Not-cleared + Phase 16 handoff | FOUND |
| `15-RESEARCH.md` execute-day VET-20-01/02/03 blocks | FOUND |
| `15-01-SUMMARY.md` | FOUND |
| commit `925206c` FUT-04 | FOUND |
| commit `393d834` AAF/ROSAP | FOUND |
| commit `fdc7b10` annotations | FOUND |
| Link Policy http count 0 | PASS |
| packs/ diff empty | PASS |
| VET-20/PACK-20 boxes unchecked | PASS |
