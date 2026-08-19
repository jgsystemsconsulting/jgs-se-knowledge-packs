---
phase: 11-io-unlocking-packs-decision-analysis-remap
plan: 01
subsystem: knowledge-packs
tags: [tier-1, nasa, gps, icd, orbital-debris, io-03, io-04, dist-a]

requires:
  - phase: 10-source-vetting
    provides: Phase 11 handoff GO on NASA-STD-8719.14C and IS-GPS-200N; Tier-1 leaning not skip-confirm
  - phase: 11-io-unlocking-packs-decision-analysis-remap
    provides: 11-RESEARCH Pattern 1 pipeline + IO-03/IO-04 chapter tables
provides:
  - packs/nasa-std-8719-14 validated Tier-1 pack (IO-03)
  - packs/is-gps-200n validated Tier-1 ICD exemplar (IO-04)
  - P11-PRE-1 and P11-PRE-2 quotes on the extracted copies
affects: [phase-11-02-thin-register, phase-12-capability-map]

actuals:
  tokens: 20958
  tasks: 2
  commits: 3

tech-stack:
  added: []
  patterns:
    - Phase 7 Pattern 1 extract → outline → scaffold → generate → validate → scan → overlap
    - MN-07 work_dir.txt as forward-slash sources/<slug> path
    - ICD exemplar-not-dump (body + appendix map; no App II–IV transcription)

key-files:
  created:
    - packs/nasa-std-8719-14/**
    - packs/is-gps-200n/**
    - .planning/phases/11-io-unlocking-packs-decision-analysis-remap/11-01-SUMMARY.md
  modified: []

key-decisions:
  - "P11-PRE-1: extracted 8719.14C has 0 Copyright/All-rights hits; Internet Public + title-page quoted in PACK.yaml"
  - "P11-PRE-2: extracted 200N has DIST-A verbatim; SAIC ICC line recorded as watch-item only"
  - "is-gps-200n is exemplar not dump; faa-std-025 named in Scope & Limits"
  - "When-to-use body paragraph kept (analog nasa-ms-7009 / faa-std-025); Prerequisites follows that paragraph"

patterns-established:
  - "work_dir.txt = sources/<slug> (forward slashes) so python Path interpolation cannot SyntaxError"
  - "Scoped git add -- packs/<slug> + --no-verify; leak check includes capability-pack-map.json on HEAD"

requirements-completed: [IO-03, IO-04]

coverage:
  - id: D1
    description: "packs/nasa-std-8719-14 exists, P11-PRE-1 recorded, validate/overlap/scan pass, 7 chapters"
    requirement: IO-03
    verification:
      - kind: other
        ref: "python tooling/validate_pack.py packs/nasa-std-8719-14"
        status: pass
      - kind: other
        ref: "python $REF/tools/check_overlap.py --source sources/nasa-std-8719-14/book_skill_work/full_text.txt --pack packs/nasa-std-8719-14"
        status: pass
      - kind: other
        ref: "python $REF/tools/scan_generated_skill.py packs/nasa-std-8719-14"
        status: pass
    human_judgment: false
  - id: D2
    description: "packs/is-gps-200n exists, P11-PRE-2 DIST-A on this copy, faa-std-025 cross-link, 6 chapters, no appendix dump"
    requirement: IO-04
    verification:
      - kind: other
        ref: "python tooling/validate_pack.py packs/is-gps-200n"
        status: pass
      - kind: other
        ref: "python $REF/tools/check_overlap.py --source sources/is-gps-200n/book_skill_work/full_text.txt --pack packs/is-gps-200n"
        status: pass
      - kind: other
        ref: "python $REF/tools/scan_generated_skill.py packs/is-gps-200n"
        status: pass
    human_judgment: false

duration: 13min
completed: 2026-08-17
status: complete
---

# Phase 11 Plan 01: IO-unlocking packs (8719.14C + IS-GPS-200N) Summary

**Two licence-clean GO packs on main: nasa-std-8719-14 (7 chapters, orbital-debris process) and is-gps-200n (6-chapter ICD exemplar, no App II–IV dump).**

## Performance

- **Duration:** 13 min
- **Started:** 2026-08-17T17:57:42Z
- **Completed:** 2026-08-17T18:10:55Z
- **Tasks:** 2
- **Files modified:** 26 pack files created (13 + 12 + this SUMMARY)

## Accomplishments

- Built `packs/nasa-std-8719-14` from official NASA-STD-8719.14C (905,584 bytes, `%PDF-1.7`, 77 pp). P11-PRE-1 third-party scan: 0 Copyright / All rights / © hits; title page NASA-STD-8719.14C Approved 2021-11-05 superseding 8719.14B. Internet Public quoted in PACK.yaml. chars/page = 2567.5.
- Built `packs/is-gps-200n` from official IS-GPS-200N (3,338,120 bytes, `%PDF-1.6`, 248 pp). P11-PRE-2: DIST-A sentence present on this extract. SAIC ICC line recorded as watch-item only. Exemplar chapters only; Apps II–IV not transcribed. chars/page = 2462.2.
- Both packs: `validate_pack.py` exit 0; `check_overlap.py` exit 0; `scan_generated_skill.py` clean; no `http`/`https` in pack trees; no `sources/` or `full_text.txt` in scoped commits; map JSON untouched; IO-03/IO-04 boxes still `- [ ]`.

## Task Commits

Each task was committed atomically:

1. **Task 1: Build packs/nasa-std-8719-14 (IO-03)** - `1b3e4f4` (feat)
2. **Task 2: Build packs/is-gps-200n (IO-04)** - `ee762d0` (feat)

**Plan metadata:** (this SUMMARY commit)

## Files Created/Modified

- `packs/nasa-std-8719-14/{SKILL.md,PACK.yaml,LICENSE,chapters/ch01–ch07,glossary.md,patterns.md,cheatsheet.md}` — IO-03 orbital-debris process pack
- `packs/is-gps-200n/{SKILL.md,PACK.yaml,LICENSE,chapters/ch01–ch06,glossary.md,patterns.md,cheatsheet.md}` — IO-04 ICD exemplar

Gitignored extracts remain under `sources/nasa-std-8719-14/` and `sources/is-gps-200n/` (never staged).

## Decisions Made

- Follow analog When-to-use layout (short reach-for paragraph, then `**Prerequisites:**`) rather than putting Prerequisites on the immediately next line. Matches `nasa-ms-7009` / `faa-std-025` and `check_release.py` RR-S-13.
- GPS pack stays one exemplar (200N only). No 705J / 800J / ICD-GPS-153 / IS-300.
- `work_dir.txt` written as `sources/<slug>` with forward slashes (MN-07).

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 2 - Missing Critical] Overlap paraphrase in nasa-std-8719-14 ch04**
- **Found during:** Task 1 validate/overlap
- **Issue:** `check_overlap.py` flagged one ≥12-word run: “heat pipes battery cells and passive nutation dampers need not be depressurized”
- **Fix:** Rewrote as “Sealed heat pipes, individual battery cells, and passive nutation dampers are called out as not requiring EOM depressurization.”
- **Files modified:** `packs/nasa-std-8719-14/chapters/ch04-explosions-breakups-collisions.md`
- **Verification:** overlap re-run exit 0
- **Committed in:** `1b3e4f4` (Task 1)

**2. [Rule 1 - Bug] When-to-use / Prerequisites adjacency vs analog layout**
- **Found during:** Task 1 MN-02-style check
- **Issue:** Plan action said “immediately followed”; live analogs insert a reach-for paragraph between `## When to use` and `**Prerequisites:**`. Strict next-line would diverge from shipped packs.
- **Fix:** Kept analog layout (heading → reach-for paragraph → Prerequisites). Both markers present; RR-S-13 still satisfied.
- **Files modified:** both SKILL.md files
- **Verification:** `grep -c '^## When to use'` and `grep -c '^\*\*Prerequisites:\*\*'` each ≥ 1
- **Committed in:** pack commits

## Deviations ledger

- What changed: When-to-use is not literally adjacent to Prerequisites (one body paragraph between).
- Why: Match shipped analog packs and check_release RR-S-13; MN-02 noted analogs already do this.
- Which IO-03 / IO-04 acceptance is affected: wording of “immediately followed” only; both headings exist; no other acceptance missed.

- What changed: one ch04 sentence paraphrased after first overlap fail.
- Why: licence-safety gate (`check_overlap` exit 0 mandatory).
- Which acceptance is affected: none after fix.

If counting only unplanned scope: the adjacency choice is the sole intentional plan wording miss. Overlap paraphrase is required-gate repair.

## MN-05 / MN-07 resolutions

- **MN-05:** nasa-std-8719-14 chapter file count = **7** (band 6–7). is-gps-200n chapter file count = **6** (band 5–6).
- **MN-07:** `sources/nasa-std-8719-14/work_dir.txt` and `sources/is-gps-200n/work_dir.txt` contain `sources/nasa-std-8719-14` and `sources/is-gps-200n` (forward slashes), not `%TEMP%` backslash paths.

## Issues Encountered

- Shared `%TEMP%/book_skill_work` is overwritten by the second extract. Copied each extract under `sources/<slug>/book_skill_work/` immediately (NASA copy confirmed intact after GPS extract).
- First NASA overlap fail on a 12-word shall-like list — paraphrased; re-run clean.

## User Setup Required

None - no external service configuration required.

## Next Phase Readiness

- Ready for 11-02 (thin-register the two new slugs; IO-02 extend-or-defer; IO-01 remap table; IO-05/06 DEFERRED; IO-07 ACCEPT).
- Do not edit `docs/capability-pack-map.json` until Phase 12. Do not tick IO-03/IO-04 boxes here (verify does that).
- Catalog still 61; pack dirs now 65. `check_release.py` will fail index/cursor counts until 11-02 thin-register.

## Self-Check: PASSED

- Key files exist on disk (`packs/nasa-std-8719-14/{SKILL.md,PACK.yaml,LICENSE,chapters}`, `packs/is-gps-200n/{SKILL.md,PACK.yaml,LICENSE,chapters}`).
- `git log --oneline --all --grep="11-01"` / pack feat commits present: `1b3e4f4`, `ee762d0`.
- Task acceptance re-run: both `validate_pack.py` exit 0; both overlap exit 0; both scan clean; no http in either tree; HEAD leak checks clean; map JSON untouched; IO boxes still open; chapter counts in band.
- Plan-level verification: `python tooling/validate_pack.py packs/nasa-std-8719-14 && python tooling/validate_pack.py packs/is-gps-200n` PASS; `git log --oneline -2` shows one commit per pack; pack dir count 65; catalog 61; `grep -c http docs/SOURCE-VETTING.md` = 0.

---
*Phase: 11-io-unlocking-packs-decision-analysis-remap*
*Completed: 2026-08-17*
