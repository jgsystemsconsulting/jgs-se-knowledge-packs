---
phase: 12-map-regen-hygiene-gate-wiring
plan: 02
subsystem: release-gate
tags: [check-release, capability-map, hygiene, gitattributes, vet-source]

requires:
  - phase: 12-map-regen-hygiene-gate-wiring
    provides: GREEN standalone check_capability_map.py (644 / DA 5/4)
provides:
  - MAP-19-04 in-process check_capability_map.main() wire in check_release.py
  - HYG-01 CHANGELOG BOM/LF + .gitattributes pin
  - HYG-02 four SKILL.md topic-index nits
  - HYG-04 federal-bca (c) enumeration-marker wording
  - HYG-03 sibling EXCLUDED keys + external PR
affects: [phase-13-release-surface]

actuals:
  tokens: 1822
  tasks: 3
  commits: 3

tech-stack:
  added: []
  patterns:
    - In-process import of check_capability_map.main() (no subprocess)
    - Local/trusted map gate; CI still does not exec repo Python
    - Sibling HYG-03 Path A (commit + PR) without vendoring vet_source.py

key-files:
  created:
    - .gitattributes
    - .planning/phases/12-map-regen-hygiene-gate-wiring/12-02-SUMMARY.md
  modified:
    - tooling/check_release.py
    - tooling/check_capability_map.py
    - docs/capability-map-CONTRACT.md
    - CHANGELOG.md
    - packs/mil-std-881f/SKILL.md
    - packs/dafman-63-119/SKILL.md
    - packs/mil-std-40051/SKILL.md
    - packs/federal-bca/SKILL.md
    - packs/federal-bca/PACK.yaml

key-decisions:
  - "Wire after cursor-manifest (~5d) and before authored-file headers"
  - "HYG-03 Path A: sibling commit 1c8b781 + PR #2; no vendor copy"
  - "SEI keys use cmu / carnegie mellon / software engineering institute (not bare sei)"
  - "Version trio stays 1.18.0; no [1.19.0]; no tag"

patterns-established:
  - "Map gate is a first-class check_release issue via import + fail on non-zero"
  - "HYG-03 lives in jgs-reference-skill; this repo records the sibling SHA + PR"

requirements-completed: [MAP-19-04, HYG-01, HYG-02, HYG-03, HYG-04]

coverage:
  - id: D1
    description: "MAP-19-04: check_release imports check_capability_map.main() in-process and PASSes"
    requirement: MAP-19-04
    verification:
      - kind: other
        ref: "python tooling/check_capability_map.py"
        status: pass
      - kind: other
        ref: "python tooling/check_release.py"
        status: pass
    human_judgment: false
  - id: D2
    description: "HYG-01: CHANGELOG BOM stripped + LF; .gitattributes pins *.md text eol=lf"
    requirement: HYG-01
    verification:
      - kind: other
        ref: "python CHANGELOG first-bytes / CRLF / [1.18.0] assert"
        status: pass
    human_judgment: false
  - id: D3
    description: "HYG-02: four SKILL.md topic-index nits fixed and revalidated"
    requirement: HYG-02
    verification:
      - kind: other
        ref: "python tooling/validate_pack.py ×4 slugs"
        status: pass
    human_judgment: false
  - id: D4
    description: "HYG-04: federal-bca PACK.yaml records A-94 (c) as enumeration markers"
    requirement: HYG-04
    verification:
      - kind: other
        ref: "python assert enumeration markers present; old (c) claim absent"
        status: pass
    human_judgment: false
  - id: D5
    description: "HYG-03 Path A: sibling EXCLUDED keys + external PR (merge not required)"
    requirement: HYG-03
    verification:
      - kind: other
        ref: "https://github.com/jgsystemsconsulting/jgs-reference-skill/pull/2"
        status: pass
    human_judgment: false

duration: 11min
completed: 2026-08-17
status: complete
---

# Phase 12 Plan 02: Gate wire + hygiene Summary

**Wired the GREEN capability-map gate into `check_release.py` in-process, stripped CHANGELOG BOM/CRLF with a `*.md` LF pin, fixed four topic-index nits plus federal-bca `(c)` wording, and landed sibling EXCLUDED keys as PR #2.**

## Performance

- **Duration:** 11 min
- **Started:** 2026-08-17T20:36:30Z
- **Completed:** 2026-08-17T20:47:25Z
- **Tasks:** 3
- **Files modified:** 10 production (this repo) + sibling `tools/vet_source.py` + this SUMMARY

## Accomplishments

- MAP-19-04: `check_release.py` imports `check_capability_map.main()` after the cursor-manifest block and `fail()`s on non-zero. Both gates PASS; map cluster-count block now prints inside `check_release`.
- HYG-01: CHANGELOG first bytes `3c212d2d0a` (no BOM); 0 CRLF; still `## [1.18.0]`; `.gitattributes` is exactly `*.md text eol=lf`.
- HYG-02: four SKILL.md nits; `validate_pack.py` PASS on all four slugs.
- HYG-04: federal-bca notes record A-94 literal `(c)` hits as enumeration markers.
- HYG-03 Path A: sibling keys + PR (merge not required for Phase 12 close).

## Wire insertion point

In `tooling/check_release.py`, new `# 5d. MAP-19-04` block immediately after the cursor-manifest try/except and before `# 7. authored-file headers`. Reuses the existing `sys.path.insert(0, str(ROOT / "tooling"))` from §5. No subprocess. Module docstring gained check 8. `check_capability_map.py` docstring no longer says standalone / Phase 9 maybe-wire. CONTRACT §4 now says the refresh path still runs the map script **and** `check_release.py` invokes `main()` in-process. MAP-19-05 paragraph untouched.

## Both-gate stdout (Task 3 re-run)

`python tooling/check_capability_map.py` → exit **0**, `PASS: capability map OK`, TOTAL **644**.

`python tooling/check_release.py` → printed the same cluster-count block (duplicate stdout from `main()`) then `RELEASE CHECK: PASS — repo is release-ready against the mechanical gate.` Exit **0**.

## HYG-01 bytes

- CHANGELOG first 8: `3c 21 2d 2d 0a 43 6f 70` (`<!--` + LF + `Cop`); BOM False; CRLF 0.
- Header `## [1.18.0]: 2026-08-17` retained; `## [1.19.0]` absent.
- JGSC copyright + SPDX remain in the first 600 chars.
- `.gitattributes` created with exactly `*.md text eol=lf\n`. No `* text=auto`.

## HYG-02 before/after

| File | Before | After |
|---|---|---|
| `packs/mil-std-881f/SKILL.md` | `PM / measurement / EVMS mapping` last (after Unmanned maritime) | same label between `Missile / ordnance (C) / strategic (D)` and `Program Element / defense materiel item` |
| `packs/dafman-63-119/SKILL.md` | Agile then AFOTEC | AFOTEC then Agile |
| `packs/mil-std-40051/SKILL.md` | `Training & Documentation` → `ch01, ch07, ch08, Topic Index` | `ch01, ch07, ch08` (circular Topic Index dropped) |
| `packs/federal-bca/SKILL.md` | `Opportunity/Benefit Analysis` → ch01, ch02, ch06 | `Opportunity cost / benefit identification` → ch01, ch02, ch06 |

`python tooling/validate_pack.py` PASS: mil-std-881f, dafman-63-119, mil-std-40051, federal-bca.

## HYG-04 wording

`packs/federal-bca/PACK.yaml` notes now: `no third-party copyright / all-rights-reserved notices (literal "(c)" hits in A-94 are enumeration markers, not copyright claims)`. P7-PRE-2 Army-CBA fetch-fail substance unchanged. No URL added.

## HYG-03 outcome (Path A — in-tree sibling)

Sibling file: `C:/Users/gower/OneDrive/Documents/GitHub/jgs-reference-skill/tools/vet_source.py`.

Keys added (existing EXCLUDED keys not weakened):

- `afotec` — AFOTEC OT&E / CERT products are not a redistribution grant for this library
- `defense acquisition guidebook` / `dod dag` — DAG is not packageable here
- `cmu` / `carnegie mellon` / `software engineering institute` — SEI technical reports are not a blanket redistribution grant

Did **not** add bare `sei` (substring trap). `defense acquisition` US_GOV publisher signal left as-is.

- Sibling commit: `1c8b781` on branch `hyg-03-excluded-afotec-dag-sei` (not merged to sibling main; not required)
- External PR: https://github.com/jgsystemsconsulting/jgs-reference-skill/pull/2
- `tooling/vet_source.py` does **not** exist in this repo

## Phase 13 leftovers not stolen

- plugin / CHANGELOG top / RELEASE-INFO still **1.18.0**; no `## [1.19.0]`; `git tag -l 'v1.19*'` empty
- `map_version` still 1.18.0 (untouched this plan)
- catalog `dod-vva-rpg.chapters` still **10**
- no README new-slug rows; no catalog.json edit; no `.github/workflows/validate.yml` change
- `grep -c http docs/SOURCE-VETTING.md` = **0**
- no generator; no AAF/CBA/DoDM/stakeholder packs; no Cyber/DE bindings

## Task Commits

1. **Task 1: Wire check_capability_map.main() into check_release (MAP-19-04)** - `ca27199` (fix)
2. **Task 2: HYG-01 BOM+LF+.gitattributes + HYG-02 four SKILL nits + HYG-04 (c) wording** - `bb39a3a` (chore)
3. **Task 3: HYG-03 sibling EXCLUDED + SUMMARY** — sibling `1c8b781` (out of tree); this-repo SUMMARY commit follows

**Plan metadata:** (this SUMMARY commit)

## Files Created/Modified

- `tooling/check_release.py` — MAP-19-04 in-process import + docstring check 8
- `tooling/check_capability_map.py` — docstring: invoked by check_release (local/trusted)
- `docs/capability-map-CONTRACT.md` — §4 wired sentence
- `CHANGELOG.md` — BOM stripped, LF only
- `.gitattributes` — `*.md text eol=lf`
- `packs/mil-std-881f/SKILL.md` — PM/EVMS alpha
- `packs/dafman-63-119/SKILL.md` — AFOTEC before Agile
- `packs/mil-std-40051/SKILL.md` — drop circular Topic Index
- `packs/federal-bca/SKILL.md` — Opportunity cost / benefit identification
- `packs/federal-bca/PACK.yaml` — enumeration-markers wording
- sibling `tools/vet_source.py` — EXCLUDED keys (not in this repo)

## Decisions Made

- Insertion after cursor-manifest (plan-recommended) so a map failure is a first-class release issue.
- HYG-03 Path A because `$REF` was writable; opened PR rather than merging sibling main.
- Prefer longer SEI keys over bare `sei`.

## Deviations

None.

## Deviations from Plan

None - plan executed exactly as written.

## Issues Encountered

None.

## User Setup Required

None - no external service configuration required.

## Next Phase Readiness

- Phase 12 execute complete. Ready for **verify-work** then **Phase 13** (catalog chapter integer, README new-slug rows, version trio 1.19.0, tag + GitHub Release).
- Do not tick MAP-19 / HYG boxes here (verify does that).
- Sibling PR #2 need not merge before Phase 12 close.

## Self-Check: PASSED

- Key files exist (`tooling/check_release.py`, `tooling/check_capability_map.py`, `docs/capability-map-CONTRACT.md`, `CHANGELOG.md`, `.gitattributes`, four SKILL.md, `packs/federal-bca/PACK.yaml`, this SUMMARY).
- Production commits present: `ca27199`, `bb39a3a`.
- `python tooling/check_capability_map.py` exit 0; `python tooling/check_release.py` exit 0 with map counts.
- CHANGELOG no BOM, LF only, still [1.18.0]; `.gitattributes` pins `*.md text eol=lf`.
- Four SKILL nits + validate_pack ×4 PASS; federal-bca enumeration markers.
- HYG-03 Path A recorded (`afotec`, `dod-dag` / `defense acquisition guidebook`, `cmu-sei`) + PR URL.
- plugin 1.18.0; catalog dod-vva-rpg.chapters == 10; SOURCE-VETTING http == 0; no v1.19 tag; no `tooling/vet_source.py`.
- ## Deviations ledger present.

---
*Phase: 12-map-regen-hygiene-gate-wiring*
*Completed: 2026-08-17*
