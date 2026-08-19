---
phase: 9-release-surface-v1-18-0
plan: 01
subsystem: release
tags: [changelog, version-bump, github-release, packs.html, check_release, capability-map, v1.18.0]

requires:
  - phase: 8-agent-enablement-surface
    provides: capability-pack-map v2 (map_version 1.18.0) + CONTRACT + gate
  - phase: 7-gap-driven-pack-builds
    provides: 7 GP packs registered at catalog 61 / dirs 63
provides:
  - v1.18.0 annotated tag + GitHub Release
  - all 11 version surfaces at 1.18.0
  - CHANGELOG 1.18.0 (rename note leads; caveats; wording fix)
  - IN-01/IN-04 closed; OUSD typo fixed
  - v1.19 backlog in STATE
affects: [ship, v1.19]

actuals:
  tokens: 3516
  tasks: 6
  commits: 2

tech-stack:
  added: []
  patterns:
    - "RELEASE-INFO first then gen_packs_page.py (never hand-edit packs.html)"
    - "Single release commit is last content commit; .planning records after tag"
    - "Annotated tag colon-style matching v1.17.0; gh release title em-dash style"

key-files:
  created:
    - .planning/phases/9-release-surface-v1-18-0/9-01-SUMMARY.md
  modified:
    - .claude-plugin/plugin.json
    - .cursor-plugin/plugin.json
    - CHANGELOG.md
    - RELEASE-INFO.txt
    - README.md
    - docs/index.html
    - docs/packs.html
    - docs/products/website/01-jgs-se-knowledge-packs.yaml
    - docs/products/website/catalog.yaml
    - docs/capability-map-CONTRACT.md
    - docs/SOURCE-VETTING.md
    - .planning/STATE.md
    - .planning/MILESTONES.md
    - .planning/ROADMAP.md

key-decisions:
  - "Single release commit holds Tasks 1-3 content (Phase 5 template); per-task intermediate commits soft-reset before tag"
  - "CHANGELOG caveats written plainly without R-number citations (MI-01)"
  - "One-liner style matches 1.17.0 period + Tier parenthetical; no em dashes (MI-02)"
  - "STATE backlog qualifies IN-02 as 7-CODE-REVIEW IN-02 (IN-01 review finding)"

patterns-established:
  - "Release surface phase: bump → CHANGELOG → doc carry-forwards → dual-gate → release commit/tag/push/gh → .planning records"

requirements-completed: [REL-1x-01, REL-1x-02]

coverage:
  - id: D1
    description: "All 11 version surfaces at 1.18.0; packs.html regenerated; IN-04 map_version reconciled"
    requirement: REL-1x-01
    verification:
      - kind: other
        ref: "python tooling/check_release.py → RELEASE CHECK: PASS; grep residual 1.17.0 whitelist-only"
        status: pass
    human_judgment: false
  - id: D2
    description: "Annotated tag v1.18.0 + GitHub Release with CHANGELOG notes leading with doe-o-413-3 rename"
    requirement: REL-1x-02
    verification:
      - kind: other
        ref: "git ls-remote --tags origin v1.18.0; gh release view v1.18.0"
        status: pass
    human_judgment: false
  - id: D3
    description: "check_capability_map.py PASS at map_version 1.18.0 / 628 entries"
    requirement: REL-1x-01
    verification:
      - kind: other
        ref: "python tooling/check_capability_map.py → PASS TOTAL: 628"
        status: pass
    human_judgment: false

duration: 10min
completed: 2026-08-17
status: complete
---

# Phase 9 Plan 01: Release surface v1.18.0 Summary

**v1.18.0 tagged and released: 7 gap-driven Tier-1 packs (61 catalog + 2 signposts), capability map v2, rename-leading CHANGELOG notes**

## Performance

- **Duration:** ~10 min
- **Started:** 2026-08-17T00:59:07Z
- **Completed:** 2026-08-17T01:05:00Z
- **Tasks:** 6/6
- **Files modified:** 11 content (release) + 3 planning (+ this SUMMARY)

## Accomplishments

- Bumped all 11 version surfaces 1.17.0 → 1.18.0; regenerated `docs/packs.html` from RELEASE-INFO (byte-identical re-run)
- CHANGELOG `## [1.18.0]: 2026-08-17` leads with `doe-413-3b` → `doe-o-413-3` rename; live PACK.yaml chapter counts 8/6/6/7/7/8/10; caveats on dod-vva-rpg / faa-std-025 / mil-std-40051; zero em dashes / URLs
- IN-01 CONTRACT cluster-name; SOURCE-VETTING OUSD typo; v1.17.0 index.html registration-wording fix
- Dual gates green at 61 catalog / 63 dirs; map_version 1.18.0 == RELEASE-INFO (IN-04)
- Release commit `d19be1a`, annotated tag `v1.18.0`, GitHub Release published and verified on origin
- STATE/MILESTONES/ROADMAP updated; v1.19 backlog carried; Phase 9 + 9-01-PLAN.md checked

## Task Commits

Tasks 1–5 content landed in the single release commit (Phase 5 template; intermediate task commits soft-reset before tag). Task 6 is the post-tag planning commit.

| Task | Name | Commit | Files |
|------|------|--------|-------|
| 1 | Version bump — all 11 surfaces | `d19be1a` (release) | plugin.json ×2, RELEASE-INFO, README, index.html, packs.html, website YAMLs ×2 |
| 2 | CHANGELOG v1.18.0 entry | `d19be1a` (release) | CHANGELOG.md |
| 3 | CONTRACT cluster-name + OUSD typo | `d19be1a` (release) | capability-map-CONTRACT.md, SOURCE-VETTING.md |
| 4 | Final validation (verify-only) | — | no commit |
| 5 | Release commit, tag, push, GitHub Release | `d19be1a` + tag `v1.18.0` | 11 content files |
| 6 | Post-release records | `7081649` (docs) | STATE.md, MILESTONES.md, ROADMAP.md, REQUIREMENTS.md, 9-01-SUMMARY.md |

**Release commit:** `d19be1a` — `release(v1.18.0): 7 gap-driven Tier-1 packs (61 +2 signposts), capability map v2`

**Tag:** `v1.18.0` — `v1.18.0: 7 gap-driven Tier-1 packs (61 +2 signposts), capability map v2`

**GitHub Release:** https://github.com/jgsystemsconsulting/jgs-se-knowledge-packs/releases/tag/v1.18.0

## Verify outputs (evidence)

### Task 1 — version surfaces

- Residual `1.17.0` outside `.planning`/`.git`/`sources` after bump: CHANGELOG history + exactly 5 whitelisted historical doc lines (capability-map-CONTRACT.md:54, capability-pack-map.md:16, SOURCE-VETTING.md:93/144/149)
- All 11 surfaces at 1.18.0: plugin.json ×2, RELEASE-INFO Version/Tag/Staged, README badge+prose×2, index.html REV×2, packs.html REV, website YAMLs×2
- `python tooling/gen_packs_page.py` byte-identical on re-run (`cmp` match)
- `map_version` 1.18.0 == RELEASE-INFO Version 1.18.0 (IN-04)

### Task 2 — CHANGELOG chapter counts

| Pack | PACK.yaml chapters | CHANGELOG one-liner |
|------|-------------------:|---------------------|
| dote-te-guidebook | 8 | (8 ch) |
| faa-std-025 | 6 | (6 ch) |
| federal-bca | 6 | (6 ch) |
| dafman-63-119 | 7 | (7 ch) |
| mil-std-881f | 7 | (7 ch) |
| mil-std-40051 | 8 | (8 ch) |
| dod-vva-rpg | 10 | (10 ch) |

- Em-dash count in 1.18.0 entry: 0; `http` count: 0
- Rename paragraph precedes first `###` heading
- Caveats present: vva ~2011 internal dates; faa Rev F vs ROSAP Rev E; 40051 counters 1168 vs metadata 584
- `python tooling/check_release.py` → `RELEASE CHECK: PASS`

### Task 3 — doc carry-forwards

- `grep "cluster 30" docs/capability-map-CONTRACT.md` → zero
- `grep "Standards, Tailoring" docs/capability-map-CONTRACT.md` → hit at §4
- `grep "OUSW" docs/SOURCE-VETTING.md` → zero
- Both gates still PASS

### Task 4 — dual-gate + basis + residual sweep

```
python tooling/check_release.py     → RELEASE CHECK: PASS (exit 0)
python tooling/check_capability_map.py → PASS: capability map OK; TOTAL: 628 (exit 0)
catalog.json packs                  → 61
ls packs | wc -l                    → 63
validate_pack.py dod-vva-rpg        → PASS
validate_pack.py mil-std-40051      → PASS
gen_packs_page.py re-run            → empty working-tree delta vs committed packs.html
residual 1.17.0                     → CHANGELOG history + 5 whitelist doc lines only
final pre-commit check_release      → PASS
```

### Task 5 — tag + release provenance

```
git ls-remote --tags origin | grep v1.18.0
  cae0145fee77c68cee90af381ec14eb7f7aa1458  refs/tags/v1.18.0
  d19be1a74635aa858ee0563029c7645892cf3bab  refs/tags/v1.18.0^{}

gh release view v1.18.0 --json name,tagName,url
  name: "v1.18.0 — 7 gap-driven Tier-1 packs + capability map v2"
  tagName: "v1.18.0"
  url: https://github.com/jgsystemsconsulting/jgs-se-knowledge-packs/releases/tag/v1.18.0

Notes body leads with:
  The `doe-413-3b` pack was renamed to `doe-o-413-3` ...
```

- `git show --stat d19be1a` → 11 content files only; no deletions; no untracked strays
- Release commit is last content commit on main before the tag

### Task 6 — planning records

- STATE.md: shipped record + IN-01/IN-04 closed + v1.19 backlog (FUT-04, FUT-05, 7-CODE-REVIEW IN-02, clusters 3/5/15)
- MILESTONES.md: v1.18.0 converted to shipped format with commit/tag/URL
- ROADMAP.md: Phase 9 checkbox line 79 `[x]`; Plans list line 132 `9-01-PLAN.md` `[x]` (MI-03)

## Decisions Made

- Followed Phase 5 release-commit template: one content commit for the public tree, then tag, then .planning-only follow-up
- Applied plan-review MI-01/02/03 and IN-01 as execution constraints without editing the plan file
- Temporary notes file for `gh release create` written under the phase dir and deleted (never committed)

## Deviations from Plan

| # | Deviation | Plan reference | Proposed classification | Rationale |
|---|-----------|----------------|--------------------------|-----------|
| 1 | Soft-reset intermediate Task 1–3 commits into single release commit | Task commit protocol vs Task 5 "last content commit" | in-scope fix | Phase 5 template and REL-1x-02 require one public release commit as last content; intermediate atomic commits would leave non-release SHAs on main ahead of the tag |
| 2 | First `gh release create` failed on `/tmp` path (Windows); retried with phase-dir notes file | Task 5 notes-file path | in-scope fix | Windows Git Bash `/tmp` path not visible to gh; same notes content, second attempt succeeded |
| 3 | Applied MI-01/02/03 + IN-01 review findings without amending PLAN.md | 9-PLAN_REVIEW folded findings | in-scope fix | User prompt required folded findings; public notes and ROADMAP tick match review intent |

### Auto-fixed Issues

**1. [Rule 3 - Blocking] Consolidated intermediate commits before tag**
- **Found during:** Task 5
- **Issue:** GSD per-task commits would make release commit not the sole content delta from pre-release HEAD in the Phase 5 sense
- **Fix:** `git reset --soft` to pre-task HEAD, explicit-path restage of 11 files, single `release(v1.18.0)` commit
- **Files modified:** same 11 content paths
- **Commit:** `d19be1a`

**2. [Rule 3 - Blocking] gh notes path on Windows**
- **Found during:** Task 5
- **Issue:** `open C:/Users/.../Temp/v1.18.0-notes.md: The system cannot find the file specified` after writing via `/tmp`
- **Fix:** Wrote notes to `.planning/phases/9-release-surface-v1-18-0/_v1.18.0-notes.tmp.md`, created release, deleted temp file
- **Verification:** `gh release view v1.18.0` notes lead with rename paragraph

---

**Total deviations:** 3 (all in-scope; no scope creep)
**Impact on plan:** Public tree and tag match plan success criteria; intermediate commit SHAs intentionally not preserved on main

## Issues Encountered

- Windows temp-path mismatch for `gh release create --notes-file` (resolved)
- `init.execute-phase` returned `phase_found: false` for phase key form; execution proceeded from explicit plan path in the prompt

## User Setup Required

None - no external service configuration required.

## Next Phase Readiness

- v1.18.0 milestone complete and published
- v1.19 backlog explicit in STATE.md (FUT-04/05, 7-CODE-REVIEW IN-02, thin clusters 3/5/15, ROSAP/optional notes)
- No open blockers

## Self-Check: PASSED

- [x] RELEASE-INFO / plugins / README / index / packs.html / website YAMLs at 1.18.0
- [x] CHANGELOG `## [1.18.0]` present above 1.17.0
- [x] Tag `v1.18.0` on origin; GitHub Release exists
- [x] Release commit `d19be1a` present
- [x] STATE / MILESTONES / ROADMAP updated
- [x] SUMMARY path: `.planning/phases/9-release-surface-v1-18-0/9-01-SUMMARY.md`

---
*Phase: 9-release-surface-v1-18-0*
*Completed: 2026-08-17*
