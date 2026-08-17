---
phase: 11-io-unlocking-packs-decision-analysis-remap
plan: 02
subsystem: knowledge-packs
tags: [tier-1, vva, remap, deferred, thin-register, io-01, io-02, io-05, io-06, io-07]

requires:
  - phase: 11-io-unlocking-packs-decision-analysis-remap
    provides: 11-01 Wave A packs nasa-std-8719-14 + is-gps-200n on main
  - phase: 11-io-unlocking-packs-decision-analysis-remap
    provides: 11-RESEARCH Patterns 3–5 + IO-01 remap table
provides:
  - packs/dod-vva-rpg extended to 13 chapters (IO-02 leftover RPG)
  - IO-01 remap table specified for MAP-19-03 (no map JSON edit)
  - IO-05/06 dated DEFERRED and IO-07 dated ACCEPT (boxes open)
  - thin-register of nasa-std-8719-14 + is-gps-200n (plugin 1.18.0)
affects: [phase-12-capability-map, phase-13-release-surface]

actuals:
  tokens: 14051
  tasks: 3
  commits: 4

tech-stack:
  added: []
  patterns:
    - Pattern 3 extend-in-place (no build_pack on existing slug)
    - Pattern 4 remap table only (MAP-19-03 apply is Phase 12)
    - Pattern 5 dated DEFERRED/ACCEPT; boxes stay `- [ ]`
    - Thin-register exception (no version/tag steal)

key-files:
  created:
    - packs/dod-vva-rpg/chapters/ch11-te-vv-checklist.md
    - packs/dod-vva-rpg/chapters/ch12-developing-the-referent.md
    - packs/dod-vva-rpg/chapters/ch13-conceptual-model-development-and-validation.md
    - .planning/phases/11-io-unlocking-packs-decision-analysis-remap/11-02-SUMMARY.md
  modified:
    - packs/dod-vva-rpg/PACK.yaml
    - packs/dod-vva-rpg/SKILL.md
    - packs/dod-vva-rpg/glossary.md
    - packs/dod-vva-rpg/cheatsheet.md
    - packs/federal-bca/SKILL.md
    - .planning/REQUIREMENTS.md
    - .planning/STATE.md
    - catalog.json
    - SKILLS.md
    - NOTICE
    - .cursor-plugin/plugin.json
    - docs/packs.html
    - README.md

key-decisions:
  - "IO-02 = leftover RPG chapters in existing dod-vva-rpg; no packs/dodm-5000-102"
  - "UCO is HTML-only — skip; Checklist + Developing the Referent + Conceptual Model"
  - "IO-01 is a remap table only; docs/capability-pack-map.json untouched"
  - "IO-05/06 DEFERRED (AAF); IO-07 ACCEPT; boxes stay open"
  - "Thin-register two Wave-A slugs only; plugin version stays 1.18.0"

patterns-established:
  - "P7-PRE-4 per new RPG PDF (DEBoK PD + OSD/USD(R&E) OPR = DIST-equivalent)"
  - "Overlap only ch11/ch12/ch13 full_texts (MJ-01 leftover ch01–ch10 glob)"
  - "MJ-02 bound greps: IO-05|DEFERRED, IO-06|DEFERRED, IO-07|ACCEPT"

requirements-completed: [IO-01, IO-02, IO-05, IO-06, IO-07]

coverage:
  - id: D1
    description: "dod-vva-rpg extended to 13 chapters (Checklist + Referent + Conceptual Model); no dodm-5000-102"
    requirement: IO-02
    verification:
      - kind: other
        ref: "python tooling/validate_pack.py packs/dod-vva-rpg"
        status: pass
      - kind: other
        ref: "python $REF/tools/check_overlap.py --source sources/dod-vva-rpg/chapter_fulltexts/ch11.txt --pack packs/dod-vva-rpg"
        status: pass
      - kind: other
        ref: "python $REF/tools/check_overlap.py --source sources/dod-vva-rpg/chapter_fulltexts/ch12.txt --pack packs/dod-vva-rpg"
        status: pass
      - kind: other
        ref: "python $REF/tools/check_overlap.py --source sources/dod-vva-rpg/chapter_fulltexts/ch13.txt --pack packs/dod-vva-rpg"
        status: pass
    human_judgment: false
  - id: D2
    description: "IO-01 remap table specified (federal-bca ch04+ch06, dod-vva-rpg ch06); map JSON untouched"
    requirement: IO-01
    verification:
      - kind: other
        ref: "grep ch04-uncertainty-and-sensitivity|ch06-reporting-and-decision-use|ch06-accreditation-agent-role .planning/REQUIREMENTS.md"
        status: pass
    human_judgment: false
  - id: D3
    description: "IO-05 and IO-06 dated DEFERRED; IO-07 dated ACCEPT; boxes stay open"
    requirement: IO-05
    verification:
      - kind: other
        ref: "grep IO-05 .planning/REQUIREMENTS.md | grep DEFERRED"
        status: pass
      - kind: other
        ref: "grep IO-06 .planning/REQUIREMENTS.md | grep DEFERRED"
        status: pass
      - kind: other
        ref: "grep IO-07 .planning/REQUIREMENTS.md | grep ACCEPT"
        status: pass
    human_judgment: false
  - id: D4
    description: "Thin-register nasa-std-8719-14 + is-gps-200n; check_release PASS; plugin 1.18.0"
    requirement: IO-03
    verification:
      - kind: other
        ref: "python tooling/check_release.py"
        status: pass
    human_judgment: false

duration: 45min
completed: 2026-08-17
status: complete
---

# Phase 11 Plan 02: IO-unlocking Wave B Summary

**Extended `dod-vva-rpg` to 13 leftover RPG chapters, specified the Decision Analysis remap table, recorded AAF deferrals + stakeholder accept, and thin-registered the two Wave-A slugs without a version bump.**

## Performance

- **Duration:** 45 min
- **Started:** 2026-08-17T19:55:00Z
- **Completed:** 2026-08-17T20:40:00Z
- **Tasks:** 3
- **Files modified:** 16 production files + this SUMMARY

## Accomplishments

- Extended `packs/dod-vva-rpg` from 10 → **13** chapters (IO-02). New: T&E/V&V Checklist (`ch11`), Developing the Referent (`ch12`), Conceptual Model Development and Validation (`ch13`). `source_pages` 283 → **368**. P7-PRE-4 per new PDF (DEBoK PD + OSD/USD(R&E) OPR). chars/page 2141.6 / 3151.0 / 2975.1. Overlap exit 0 on **new** `ch11`/`ch12`/`ch13` full_texts only. No `packs/dodm-5000-102`.
- Wrote the IO-01 remap spec (table below) into this SUMMARY and pointed REQUIREMENTS IO-01 at `federal-bca` `ch04-uncertainty-and-sensitivity.md` + `ch06-reporting-and-decision-use.md` and `dod-vva-rpg` `ch06-accreditation-agent-role.md`. Map apply is MAP-19-03 / Phase 12. `docs/capability-pack-map.json` untouched.
- Dated IO-05 **DEFERRED**, IO-06 **DEFERRED**, IO-07 **ACCEPT**. All IO-01..07 boxes remain `- [ ]`. Optional federal-bca Topic Index row `**Decision Analysis** → ch04, ch06` added.
- Thin-registered `nasa-std-8719-14` + `is-gps-200n`: catalog **63**, SKILLS **63 (+2 signposts)**, cursor **64**, dirs **65**, README `packs-63`, plugin version still **1.18.0**. `check_release.py` PASS.

## Task Commits

Each task was committed atomically:

1. **Task 1: Extend packs/dod-vva-rpg (IO-02 leftover RPG chapters)** - `6157641` (feat)
2. **Task 2: IO-01 remap table + IO-05/06 DEFERRED + IO-07 ACCEPT** - `77e9ec5` (docs)
3. **Task 3: Thin-register nasa-std-8719-14 + is-gps-200n** - `b289e62` (chore)

**Plan metadata:** (this SUMMARY commit)

## Files Created/Modified

- `packs/dod-vva-rpg/chapters/ch11-te-vv-checklist.md` — T&E/V&V Integration Checklist
- `packs/dod-vva-rpg/chapters/ch12-developing-the-referent.md` — validation-referent identify/select/specify
- `packs/dod-vva-rpg/chapters/ch13-conceptual-model-development-and-validation.md` — conceptual-model V&V
- `packs/dod-vva-rpg/{SKILL.md,PACK.yaml,glossary.md,cheatsheet.md}` — count 13, P7-PRE-4 provenance, routing
- `packs/federal-bca/SKILL.md` — Decision Analysis Topic Index nudge (not a map edit)
- `.planning/REQUIREMENTS.md` — IO-01 remap pointer; IO-02 chapters-not-a-pack; IO-05/06 DEFERRED; IO-07 ACCEPT
- `.planning/STATE.md` — Phase 11 (2026-08-17) deviations bullet (frontmatter untouched)
- `catalog.json`, `SKILLS.md`, `NOTICE`, `.cursor-plugin/plugin.json`, `docs/packs.html`, `README.md` — thin-register

Gitignored extracts remain under `sources/dod-vva-rpg/` (never staged).

## IO-01 remap table (MAP-19-03 apply)

| Pack | Chapter | From (today) | To | Why |
|---|---|---|---|---|
| `federal-bca` | `ch06-reporting-and-decision-use.md` | Opportunity/Benefit | Decision Analysis & Trade Studies | Decision-use / OMB-facing choice documentation; map note already flags "also decision analysis" |
| `federal-bca` | `ch04-uncertainty-and-sensitivity.md` | Opportunity/Benefit | Decision Analysis & Trade Studies | Uncertainty/sensitivity is the A-94 decision-analysis method spine |
| `dod-vva-rpg` | `ch06-accreditation-agent-role.md` | Assurance & System Assurance | Decision Analysis & Trade Studies | Accreditation is the authority **decision**; 7-RESEARCH targeted cluster 16 for this pack |

Leave federal-bca ch01–ch03, ch05 (+ support files) in Opportunity so cluster 15 does not collapse. Leave dod-vva-rpg ch08 in Validation. Leave ch10 in Risk. Result after Phase 12 apply: Decision Analysis 2 → 5 entries, 2 → 4 packs. That is the Phase 12 SC-1 contract — **not** verified against live JSON this phase.

## Decisions Made

- Lean leftover set = Checklist (must) + Developing the Referent + Conceptual Model Development and Validation (live-index validation-adjacent special topics). Do not add all ~17 special topics or legacy role guides.
- UCO (`vva-rpg-uco`) is HTML-only on the live cto.mil index — skip; does not block IO-02.
- IO-02 SC-2 reading: Validation depth via chapters-not-a-pack; DoDM 5000.102 stays deferred; no invented slug.
- Thin-register only the two new slugs. Do not bump plugin version, CHANGELOG, or tag REL-19-02. Catalog `dod-vva-rpg.chapters` left at 10 (Phase 13).

## Deviations from Plan

### Auto-fixed Issues

None.

## Deviations

- What changed: UCO skipped (HTML-only); two live-index special topics added with the Checklist (total new = 3 = Checklist + ≤2).
- Why: Plan authorizes UCO skip if HTML-only; leftover titles must come from the live index, not be pre-invented.
- Which IO-02 acceptance is affected: none — chapter count 13 > 10; no DoDM pack.

- What changed: glossary/cheatsheet lightly updated for ch11–ch13 routing.
- Why: keep pack-side Topic/term routing consistent with new chapters.
- Which acceptance is affected: none.

If counting only unplanned scope: UCO skip is a pre-authorized deviation.

## MJ-01 / MJ-02 resolutions

- **MJ-01:** Overlap gated on `ch11.txt` / `ch12.txt` / `ch13.txt` only — leftover `ch01`–`ch10` extracts were **not** treated as new. Chapter count **13 > 10**. PACK.yaml notes contain per-new-chapter P7-PRE-4 provenance (title + retrieved 2026-08-17 + Checklist / TEVV / Referent / Conceptual Model). `git show HEAD` on the pack commit has no `sources/` or `capability-pack-map.json`.
- **MJ-02:** Bound greps all hold:
  - `grep IO-05 .planning/REQUIREMENTS.md | grep DEFERRED` — hit
  - `grep IO-06 .planning/REQUIREMENTS.md | grep DEFERRED` — hit
  - `grep IO-07 .planning/REQUIREMENTS.md | grep ACCEPT` — hit
- **MN-01:** each scoped commit `git show --name-only HEAD` has no `capability-pack-map.json`.

## Issues Encountered

- Shared `%TEMP%/book_skill_work` overwritten by sequential extracts. Copied ch12 then ch13 under `sources/dod-vva-rpg/extracts/chNN/book_skill_work/` immediately; ch11 Phase 7 leftover extract left intact.
- Windows quoting broke an inline `root.replace('\\','/')` copy helper; used `cp` from `%LOCALAPPDATA%/Temp/book_skill_work` instead.

## User Setup Required

None - no external service configuration required.

## Next Phase Readiness

- Ready for Phase 12 MAP-19-01 regen + MAP-19-03 apply of the table above. Do **not** edit the map JSON until then.
- Phase 13 owns version bump / CHANGELOG IO narrative / GitHub Release / `v1.19.0` tag. Basis: dirs **65** / catalog **63** / SKILLS **63 (+2 signposts)** / cursor **64** / README packs-63 / plugin **1.18.0**.
- Do not tick IO-01..07 boxes here (verify does that).

## Self-Check: PASSED

- Key files exist (`packs/dod-vva-rpg/chapters/ch11–ch13`, REQUIREMENTS IO parentheticals, this SUMMARY).
- Task commits present: `6157641`, `77e9ec5`, `b289e62`.
- `validate_pack.py` PASS on dod-vva-rpg / nasa-std-8719-14 / is-gps-200n.
- `check_release.py` PASS.
- Chapter count 13; no `packs/dodm-5000-102`; no AAF / army-cba / stakeholder / SP-7084.
- IO-05/06 DEFERRED and IO-07 ACCEPT bound greps hold; boxes still `- [ ]`.
- `docs/capability-pack-map.json` untouched; `grep -c http docs/SOURCE-VETTING.md` = 0.
- Plugin version 1.18.0; no 1.19.0 tag.
- IO-01 remap table heading + three-row table present in this file.

---
*Phase: 11-io-unlocking-packs-decision-analysis-remap*
*Completed: 2026-08-17*
