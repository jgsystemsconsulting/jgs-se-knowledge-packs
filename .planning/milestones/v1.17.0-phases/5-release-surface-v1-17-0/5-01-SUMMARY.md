---
phase: 5-release-surface-v1-17-0
plan: 01
subsystem: release
tags: [changelog, version-bump, github-release, packs.html, check_release]

requires:
  - phase: 3-tier-1-packs-public-domain
    provides: 8 Tier-1 packs registered in catalog/SKILLS/NOTICE at 54/56 basis
provides:
  - v1.17.0 annotated tag on origin
  - GitHub Release v1.17.0 with CHANGELOG-derived notes
  - All 11 version surfaces at 1.17.0
  - PACK-SPEC When-to-use/Prerequisites body-order addendum
  - README pack table + doe-413-3b series framing
affects: [ship, v1.18-planning]

actuals:
  tokens: 3200
  tasks: 7
  commits: 2

tech-stack:
  added: []
  patterns:
    - "Release commit is last content commit; .planning records commit after annotated tag"
    - "Explicit-path git add only (never git add docs/ or -A) when untracked user files live under docs/"
    - "packs.html regenerated from RELEASE-INFO.txt via gen_packs_page.py; never hand-edited"
    - "Annotated tag colon style matching v1.16.3; GitHub Release title may use em dash"

key-files:
  created:
    - .planning/phases/5-release-surface-v1-17-0/5-01-SUMMARY.md
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
    - docs/PACK-SPEC.md
    - .planning/STATE.md
    - .planning/MILESTONES.md
    - .planning/ROADMAP.md
    - .planning/REQUIREMENTS.md

key-decisions:
  - "doe-413-3b rename to doe-o-413-3 deferred to v1.18+; series framing only in README"
  - "CHANGELOG chapter counts from PACK.yaml live values 8/6/5/7/9/8/7/6 (MA-01)"
  - "README pack table gained 8 missing rows so badge packs-54 matches table (MI-02 / REL-01)"
  - "Annotated tag message uses colon style (v1.16.3 convention), not research em-dash draft"

patterns-established:
  - "Task content edits batch into single release(vX.Y.Z) commit; planning docs follow after tag"
  - "gh release create --notes-file from CHANGELOG entry body with short intro prose"

requirements-completed: [REL-01, REL-02]

coverage:
  - id: D1
    description: All 11 version surfaces at 1.17.0; packs.html regenerated and gate-identical
    requirement: REL-01
    verification:
      - kind: other
        ref: "grep -rn 1.16.3 (only CHANGELOG history) + python tooling/check_release.py"
        status: pass
    human_judgment: false
  - id: D2
    description: check_release PASS with independent catalog 54 / packs dirs 56
    requirement: REL-01
    verification:
      - kind: other
        ref: "python tooling/check_release.py; python -c catalog len; ls packs | wc -l"
        status: pass
    human_judgment: false
  - id: D3
    description: Annotated tag v1.17.0 on origin + GitHub Release published
    requirement: REL-02
    verification:
      - kind: other
        ref: "git ls-remote --tags origin v1.17.0; gh release view v1.17.0"
        status: pass
    human_judgment: false
  - id: D4
    description: CHANGELOG 1.17.0 entry with correct PACK.yaml chapter counts, em-dash/URL free
    requirement: REL-01
    verification:
      - kind: other
        ref: "grep chapter one-liners vs packs/*/PACK.yaml chapters field"
        status: pass
    human_judgment: false

duration: 5min
completed: 2026-08-15
status: complete
---

# Phase 5 Plan 01: Release surface + v1.17.0 Summary

**v1.17.0 shipped: 8 Tier-1 packs on all release surfaces, gate PASS at 54/56, annotated tag + GitHub Release**

## Performance

- **Duration:** ~5 min
- **Started:** 2026-08-15T05:45:53Z
- **Completed:** 2026-08-15T05:50:30Z
- **Tasks:** 7/7
- **Files modified:** 10 content (release commit) + 4 planning (follow-up)

## Accomplishments

- Bumped all 11 version surfaces 1.16.3 → 1.17.0; regenerated `docs/packs.html` from RELEASE-INFO
- CHANGELOG `## [1.17.0]: 2026-08-15` with PACK.yaml chapter counts 8/6/5/7/9/8/7/6 (MA-01)
- PACK-SPEC body-order list now leads with `## When to use` + `**Prerequisites:**` (RR-S-13)
- README: 8 new pack table rows (MI-02 badge/table agreement) + `doe-413-3b` series-framing line
- `python tooling/check_release.py` → `RELEASE CHECK: PASS`; catalog 54; packs dirs 56
- Release commit `bcd32af`, annotated tag `v1.17.0`, GitHub Release published and verified on origin

## Task Commits

Tasks 1–5 content were landed in the single release commit (plan Task 6 owns the content commit); Task 7 is the post-tag planning commit.

1. **Task 1: Version bump — all 11 surfaces** - `bcd32af` (release)
2. **Task 2: CHANGELOG v1.17.0 entry** - `bcd32af` (release)
3. **Task 3: PACK-SPEC When to use + Prerequisites** - `bcd32af` (release)
4. **Task 4: README doe-413 framing + 8 pack rows** - `bcd32af` (release)
5. **Task 5: Final validation** - no commit (verify-only; gate PASS)
6. **Task 6: Release commit, tag, push, GitHub Release** - `bcd32af` + tag `v1.17.0`
7. **Task 7: Post-release records** - (this SUMMARY + STATE/MILESTONES/ROADMAP/REQUIREMENTS commit)

**Release commit:** `bcd32af` — `release(v1.17.0): 8 Tier-1 public-domain packs (54 +2 signposts)`

## Verify outputs (evidence)

### Task 1 — version surfaces
- `grep -rn "1\.16\.3"` outside `.planning`/packs/sources after bump: only `CHANGELOG.md` history heading `## [1.16.3]: 2026-06-26`
- All gate + non-gate surfaces at 1.17.0: plugin.json ×2, RELEASE-INFO Version/Tag/Staged, README badge+prose×2, index.html REV×2, packs.html REV, website YAMLs×2
- `python tooling/gen_packs_page.py` idempotent on working tree (byte-identical re-run)

### Task 2 — CHANGELOG chapter counts (MA-01)
| Pack | PACK.yaml chapters | CHANGELOG one-liner |
|------|-------------------:|---------------------|
| nist-800-171 | 8 | (8 ch) |
| nist-800-61 | 6 | (6 ch) |
| cisa-cpg | 5 | (5 ch) |
| doe-sem | 7 | (7 ch) |
| mil-hdbk-338 | 9 | (9 ch) |
| mil-hdbk-516 | 8 | (8 ch) |
| nasa-ms-7009 | 7 | (7 ch) |
| doe-413-3b | 6 | (6 ch) |
- Em-dash count in 1.17.0 entry: 0; no `http` URLs in entry

### Task 3 — PACK-SPEC
- `grep -n "When to use" docs/PACK-SPEC.md` → line 33 inside body-order list (first item before How to Use)

### Task 4 — README
- Framing line at README ~166; 8 new table rows 156–163; `grep -c '"doe-413-3b"' catalog.json` = 1

### Task 5 — gate battery
```
python tooling/check_release.py
→ RELEASE CHECK: PASS — repo is release-ready against the mechanical gate. (exit 0)

python -c "import json;print(len(json.load(open('catalog.json'))['packs']))"
→ 54

ls packs | wc -l
→ 56

python tooling/validate_pack.py packs/nist-800-171 → PASS
python tooling/validate_pack.py packs/doe-413-3b → PASS

Final pre-commit re-run: RELEASE CHECK: PASS (exit 0)
```

### Task 6 — tag + release
```
git tag -l -n3 v1.17.0
→ v1.17.0         v1.17.0: 8 Tier-1 public-domain packs (54 +2 signposts)

git ls-remote --tags origin | grep v1.17.0
→ 2a8b0cb… refs/tags/v1.17.0
→ bcd32af… refs/tags/v1.17.0^{}

gh release view v1.17.0 --json name,tagName,url
→ {"name":"v1.17.0 — 8 Tier-1 public-domain packs","tagName":"v1.17.0",
   "url":"https://github.com/jgsystemsconsulting/jgs-se-knowledge-packs/releases/tag/v1.17.0"}

git log --oneline -1 origin/main
→ bcd32af release(v1.17.0): 8 Tier-1 public-domain packs (54 +2 signposts)
```
- Staged paths explicit only; untracked `docs/ROLE-AGENTS-REQUIREMENTS-V2.md`, `docs/capability-pack-map.{md,json}` never staged

### Task 7 — planning records
- STATE.md: v1.17.0 shipped + deferrals/residuals
- MILESTONES.md: shipped record with commit/tag/URL
- ROADMAP.md: Phase 4 + Phase 5 checked; 5-01 plan checked
- REQUIREMENTS.md: REL-01, REL-02 checked

## Files Created/Modified

- `.claude-plugin/plugin.json` / `.cursor-plugin/plugin.json` — version 1.17.0
- `RELEASE-INFO.txt` — Version/Tag/Staged 2026-08-15T05:46:56Z
- `CHANGELOG.md` — 1.17.0 entry
- `README.md` — version strings, 8 pack rows, doe-413 framing
- `docs/index.html`, `docs/packs.html` — REV 1.17.0
- `docs/products/website/*.yaml` — version 1.17.0
- `docs/PACK-SPEC.md` — When to use + Prerequisites body-order item
- `.planning/STATE.md`, `MILESTONES.md`, `ROADMAP.md`, `REQUIREMENTS.md` — shipped records

## Decisions Made

- Tag message colon style per live `v1.16.3` (`v1.17.0: …`), not research §4 em-dash draft (plan Task 6 overrides research)
- README pack table completed with 8 rows (user MUST-ADDRESS MI-02) so packs-54 badge agrees with table
- doe-413 rename deferred to v1.18+; only framing prose in README
- Accepted residuals recorded: catalogue licence-string sweep skip; user-owned docs/ untracked; scan_generated_skill.py not re-run in Phase 5

## Deviations from Plan

| # | Deviation | Plan reference | Proposed classification | Rationale |
|---|-----------|----------------|--------------------------|-----------|
| 1 | Batched Tasks 1–5 into single release commit rather than per-task commits | task_commit_protocol vs Task 6 "LAST content commit" | in-scope fix | Public release surface must be one atomic release commit matching prior convention (6ede444); intermediate version-bump commits would leave main briefly inconsistent |
| 2 | Added 8 missing README pack table rows (not only framing line) | Task 4 + user MI-02 MUST-ADDRESS | in-scope fix | Badge said packs-54 while table stopped at faa-rma; REL-01 surface agreement required |
| 3 | PACK-SPEC Prerequisites wording used ASCII hyphen not research em dash | Task 3 / research §3.1 | in-scope fix | PACK-SPEC had zero em dashes; avoided introducing first em dash while preserving RR-S-13 meaning |
| 4 | gh release notes path: first attempt wrote `/tmp/...` (missing on Windows); retried with repo-local notes file | Task 6 | in-scope fix | Windows Git Bash has no `/tmp` for gh; used `.planning/.../_v1.17.0-notes.md` then deleted untracked |

### Auto-fixed Issues

**1. [Rule 2 - Missing Critical] README pack table missing 8 new packs**
- **Found during:** Task 4
- **Issue:** Badge packs-54 vs table ending at faa-rma (MI-02)
- **Fix:** Added 8 rows matching existing row format before mit-ocw-se planned row
- **Files modified:** README.md
- **Commit:** bcd32af

**2. [Rule 3 - Blocking] GitHub Release notes path on Windows**
- **Found during:** Task 6
- **Issue:** `gh release create --notes-file /tmp/...` failed (path not found)
- **Fix:** Wrote notes under `.planning/phases/5-release-surface-v1-17-0/_v1.17.0-notes.md`, created release, deleted temp file
- **Verification:** `gh release view v1.17.0` succeeds with CHANGELOG body
- **Committed in:** N/A (no code change; release metadata only)

---

**Total deviations:** 4 (all in-scope; no scope creep beyond MI-02 MUST-ADDRESS)
**Impact on plan:** Release correctness improved; no architectural change

## Issues Encountered

- OneDrive/Windows: `/tmp` notes path failed for `gh release create`; fixed with local path
- Push to main reported branch-protection bypass notice but succeeded (`main -> main`, tag pushed)

## User Setup Required

None - no external service configuration required.

## Next Phase Readiness

- v1.17.0 milestone complete (REL-01, REL-02)
- v1.18+ backlog seed: `doe-413-3b` → `doe-o-413-3` rename with catalog alias
- User should refresh or discard stale untracked `docs/capability-pack-map.*` (still claim pre-v1.17 completeness)

## Self-Check: PASSED

- FOUND: release commit `bcd32af` on origin/main
- FOUND: annotated tag `v1.17.0` on origin (`git ls-remote`)
- FOUND: GitHub Release `v1.17.0` (`gh release view`)
- FOUND: CHANGELOG `## [1.17.0]: 2026-08-15`
- FOUND: check_release PASS + catalog 54 + packs 56
- FOUND: untracked user docs/ files still untracked (not in release commit)

---
*Phase: 5-release-surface-v1-17-0*
*Completed: 2026-08-15*
