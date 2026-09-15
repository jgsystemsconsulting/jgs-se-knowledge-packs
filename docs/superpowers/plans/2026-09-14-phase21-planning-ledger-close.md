# Phase 21 Planning Ledger Close and v1.20.0 Ship Handoff Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Close the v1.20.0 planning ledger honestly (phase 21 gap/verify executed with artifacts, all shared surfaces moved to "closed, ship pending", then "shipped"), and publish the v1.20.0 GitHub Release behind an explicit user gate.

**Architecture:** Two-wave ledger move with assert gates between waves. Wave 1 records the milestone as closed with the release pending; a user-gated publish pushes 29 existing commits plus the annotated tag `v1.20.0` and creates the GitHub Release from a CHANGELOG `[1.20.0]`-only notes file; wave 2 backfills the release URL into every surface. Every assertion is an inline command block; no permanent test files.

**Tech Stack:** Git + GitHub CLI (`gh`) on Windows Git Bash; local `python` (stdlib) for JSON asserts and the repo's own gate scripts (`tooling/check_release.py`, `tooling/generate_capability_map.py`).

**Spec:** `docs/superpowers/specs/2026-09-14-phase21-planning-ledger-close.md`

## Global Constraints

- **Zero commits.** `.planning/` is gitignored (commit `55ef575` policy) and `docs/superpowers/` is untracked. No task has a commit step; never run `git add`, `git commit`, `git stash`, or any force-push. The only network writes in this package are the three publish commands in Task 5.
- **No product changes.** No edits to `docs/products/`, `tooling/`, packs, CI workflows, `CHANGELOG.md`, version trio surfaces, or the tag. Do not re-tick REQUIREMENTS items P3 closed. Do not rewrite `21-IMPL_REVIEW.md`.
- **Tag frozen.** Annotated tag `v1.20.0` stays on `ffe385a` (`git rev-parse --short "v1.20.0^{commit}"` must print `ffe385a` at every assert). Quote `v1.20.0^{commit}` in every rev-parse (Git Bash brace/glob safety).
- **No network in Tasks 1-4.** Remote reads (`git ls-remote`, `gh release view`, `gh auth status`) happen only inside Task 5, immediately before the user gate. Publish commands run only after the user answers the gate.
- **Historical verdicts.** `verdicts.verify: "passed_with_notes:gh_release_pending_user_go"` in the phase master_flow is a historical record of the wave-1 gate run (saboteur advisory: do not "fix" it later). Wave 2 refreshes only `notes` (and `updated_at`) fields; verdicts and verdict strings never change after Task 1.
- **CHANGELOG discipline.** `CHANGELOG.md` is never edited. Release notes come from the `[1.20.0]` section only; `[Unreleased]` stays as the next release's staging area. No `--generate-notes`, no `gh pr create` (stock `/gsd-ship` is deliberately not used).
- **Execution-time variables** used throughout: `<EXEC_TS>` = current UTC timestamp in ISO-8601 with `Z` (expected date 2026-09-14); `<RELEASE_URL>` = URL captured in Task 5 from `gh release view v1.20.0 --json url -q .url`; `<N>` = ahead count recorded in Task 4 (29 on 2026-09-14). Calendar dates pinned by the spec (2026-09-14) stay literal.
- **Gates scripts are local:** run all repo commands from the repo root `C:/Users/gower/OneDrive/Documents/GitHub/jgs-se-knowledge-packs`.

## Research

research: skipped (in-repo GSD ledger close plus a documented release-command handoff; no external APIs, libraries, or version-sensitive choices beyond the repo's own release procedure)

## Codebase context

Context gate output (reuse): `docs/superpowers/context/2026-09-14-phase21-planning-ledger-close-context.md` plus log sibling `docs/superpowers/context/2026-09-14-phase21-planning-ledger-close-context-log.md`. Key facts re-verified live on 2026-09-14: branch `main` @ `5b2183c`; origin/main `55ef575`, 29 ahead / 0 behind; annotated tag `v1.20.0` peel `ffe385a`, message `chore: annotate v1.20.0 generator refresh path`; tag and release absent on origin; working tree clean except untracked `docs/superpowers/`. Phase 19/20 precedent: gap_analysis + verify executed to `passed`, artifacts authored, `current_gate` parked at `doc_check` with `doc_check`, `milestone_audit`, `complete`, `retrospective` in `skipped`. Version surfaces verified live: `.claude-plugin/plugin.json` version `1.20.0`, `RELEASE-INFO.txt` at repo root, map envelope `"map_version": "1.20.0"`, `catalog.json` `packs` array length 63, `packs/` has 65 entries. P3 already closed (do-not-redo): impl_review regate, master_flow review wave through `security_audit`, REQUIREMENTS ticks, ROADMAP plan boxes / progress 2/2 / coverage, REL-21-02 `Complete (gh release: P8)` tail (cleared only after a real release exists).

## File Structure

Created:

- `.planning/phases/21-contract-rewrite-release-surfaces/21-GAP_ANALYSIS.md` (Task 1)
- `.planning/phases/21-contract-rewrite-release-surfaces/21-VERIFICATION.md` (Task 1)
- `docs/superpowers/release-notes/v1.20.0.md` (Task 4; untracked directory, never staged)
- `.planning/SHIP-HANDOFF.md` (Task 5, only on the no-go or self-run-without-release branch)

Modified:

- `.planning/phases/21-contract-rewrite-release-surfaces/master_flow_state.json` (Tasks 1, 6)
- `.planning/master_flow_state.json` root pointer (Tasks 1, 6)
- `.planning/STATE.md` (Tasks 2, 6), `.planning/PROJECT.md` (Tasks 2, 6), `.planning/ROADMAP.md` (Tasks 2, 6), `.planning/GAP.md` (Task 2)
- `.planning/MILESTONES.md`, `.planning/REQUIREMENTS.md` (Task 6 only)

Never touched: `CHANGELOG.md`, anything under `docs/products/`, `tooling/`, `.github/`, packs, git tags.

---

### Task 1: Execute phase 21 gap_analysis and verify gates with real artifacts

**Files:**
- Create: `.planning/phases/21-contract-rewrite-release-surfaces/21-GAP_ANALYSIS.md`
- Create: `.planning/phases/21-contract-rewrite-release-surfaces/21-VERIFICATION.md`
- Modify: `.planning/phases/21-contract-rewrite-release-surfaces/master_flow_state.json`
- Modify: `.planning/master_flow_state.json`

**Interfaces:**
- Consumes: the four existing review artifacts `21-IMPL_REVIEW.md`, `21-CODE_REVIEW.md`, `21-INTEGRATION_CHECK.md`, `21-SECURITY_AUDIT.md` in the phase dir; recorded verdicts in the phase `master_flow_state.json`.
- Produces: `verdicts.gap_analysis = "passed"`, `verdicts.verify = "passed_with_notes:gh_release_pending_user_go"`, `artifacts.gap_analysis` / `artifacts.verify` paths, `current_gate = "doc_check"`, root pointer `active_phase/active_phase_dir/active_state/lock = null`. Task 3 and Task 5's no-go re-run depend on this end state.

**Model:** standard

- [ ] **Step 1: Read the four review artifacts and the two summaries**

Read in full: `.planning/phases/21-contract-rewrite-release-surfaces/21-IMPL_REVIEW.md`, `21-CODE_REVIEW.md`, `21-INTEGRATION_CHECK.md`, `21-SECURITY_AUDIT.md`, plus `21-01-SUMMARY.md` and `21-02-SUMMARY.md`. While reading, count Critical / Warning / Info findings per review artifact (master_flow already pins the verdicts: impl `passed_with_notes`, code `passed_with_notes`, integration `passed_with_notes`, security `passed:secured`; all four have zero critical findings). Do not edit any of these files.

- [ ] **Step 2: Re-run the behavioral checks and record outputs**

```bash
python tooling/check_release.py
# Expected: gate banners ending in "RELEASE CHECK: PASS", exit 0
python tooling/generate_capability_map.py --generated-on 2026-08-27 --check
# Expected: exit 0 (byte-stable replay on the live catalogue)
git cat-file -t v1.20.0
# Expected: tag
git rev-parse --short "v1.20.0^{commit}"
# Expected: ffe385a
python -c "import json; print(json.load(open('.claude-plugin/plugin.json'))['version'])"
# Expected: 1.20.0
grep -o '"map_version": "[^"]*"' docs/capability-pack-map.json
# Expected: "map_version": "1.20.0"
python -c "import json; print(len(json.load(open('catalog.json'))['packs']))"
# Expected: 63
ls -1 packs | wc -l
# Expected: 65
```

If any check fails, stop: the package has a product regression that P3 closed, and no ledger edit may proceed.

- [ ] **Step 3: Author 21-GAP_ANALYSIS.md**

Write `.planning/phases/21-contract-rewrite-release-surfaces/21-GAP_ANALYSIS.md` with exactly this content, filling the Review Inventory count columns with the integers observed in Step 1 (all Critical columns are 0):

```markdown
---
phase: 21-contract-rewrite-release-surfaces
analyzed: 2026-09-14
requirement_scope: MAP-21-05, REL-21-01, REL-21-02
reviews_present: [21-IMPL_REVIEW.md, 21-CODE_REVIEW.md, 21-INTEGRATION_CHECK.md, 21-SECURITY_AUDIT.md]
review_verdicts:
  impl: PASS_WITH_NOTES
  code: PASS_WITH_NOTES
  integration: PASS_WITH_NOTES
  security: SECURED
critical_findings: 0
---

# Phase 21 Gap Analysis: CONTRACT rewrite + release surfaces

**Verdict:** CLOSED

All four required reviews exist and were read in full. Zero critical findings across them; impl_review was re-gated 2026-09-14 by the P3 package with CR-01/WR-01/WR-02/WR-03 closed. Every warning and note item is either a verified ship-able residual or the recorded ship handoff. No execute re-entry is required.

## Review Inventory

| Review | Verdict | Critical | Warning | Info |
|---|---|---|---|---|
| 21-IMPL_REVIEW.md | PASS_WITH_NOTES (re-gated 2026-09-14, regate attempt 2) | 0 | <count> | <count> |
| 21-CODE_REVIEW.md | PASS_WITH_NOTES | 0 | <count> | <count> |
| 21-INTEGRATION_CHECK.md | PASS_WITH_NOTES | 0 | <count> | <count> |
| 21-SECURITY_AUDIT.md | SECURED | 0 | <count> | <count> |

No review was skipped. Product gates were re-run live for this analysis (see 21-VERIFICATION.md for command outputs).

## Requirement Cross-Check Against ROADMAP Success Criteria

| Criterion | Status | Evidence |
|---|---|---|
| 1. `docs/capability-map-CONTRACT.md` section 4 names the generator as the refresh path | MET | Section 4 names `tooling/generate_capability_map.py`; live check `grep -n "generate_capability_map" docs/capability-map-CONTRACT.md` matches. Recorded PASS in 21-IMPL_REVIEW (re-gated) and 21-INTEGRATION_CHECK. |
| 2. CONTRACT section 8 residual is closed or reduced to documented note overrides only | MET | The section 8 residual is the mandatory `docs/capability-pack-map-note-overrides.json` input only; the generator fails closed without it. Confirmed by 21-CODE_REVIEW and the CHANGELOG [1.20.0] entry. |
| 3. `python tooling/check_release.py` PASS at frozen 63 catalog / 65 dirs; `map_version` is 1.20.0; no new packs | MET | Re-run this session: exit 0, `RELEASE CHECK: PASS`; catalog 63 / dirs 65; map envelope `map_version 1.20.0`, schema 2, 644 entries, 32 clusters. |
| 4. Version surfaces + CHANGELOG [1.20.0] record the generator honestly; annotated tag + GitHub Release when the product surface is ready | MET | Version trio 1.20.0 (`.claude-plugin/plugin.json`, `RELEASE-INFO.txt`, CHANGELOG top section); annotated tag `v1.20.0` on `ffe385a`. The GitHub Release is scoped by REL-21-02 to this package's ship step and runs under the user-gated handoff (Decision 4 of the P8 spec); SC4's "when the product surface is ready" condition governs, so the pending release is a recorded handoff, not a criterion failure. |

## Residuals (ship-able, no action required this phase)

None new. The only open item in phase scope is the GitHub Release, which is not a phase gap (below).

## Rejected as Non-Gaps

| Item | Reason for rejection |
|---|---|
| The GitHub Release does not exist yet | Ship-handoff item owned by the user-gated publish (Decision 4 of the P8 spec). REL-21-02 already scopes the release to this package's ship step; the annotated tag exists on `ffe385a`; nothing inside phase scope is missing. |
| Post-tag CI and tooling commits recorded in CHANGELOG [Unreleased] | Landed after the tag tip `ffe385a`; out of phase scope and not part of the tagged release. They stage the next release, not this one. |

## Verdict Rationale

CLOSED, not OPEN_GAPS: all four reviews passed with zero critical findings; MAP-21-05 and REL-21-01 are met with live evidence re-run this session; REL-21-02's tag half is done and its release half is the recorded user-gated handoff, which the requirement text itself scopes to the ship step.

CLOSED, not NEEDS_WORK: no blocking defect is open in any prior review. IMPL, CODE, and INTEGRATION all returned PASS_WITH_NOTES; security returned SECURED.

Next command for the orchestrator: record verdicts in master_flow, close the shared ledger (wave 1), then present the user-gated publish.
```

- [ ] **Step 4: Author 21-VERIFICATION.md**

Write `.planning/phases/21-contract-rewrite-release-surfaces/21-VERIFICATION.md` with exactly this content, replacing the `<observed>` markers with the actual outputs captured in Step 2:

```markdown
---
phase: 21-contract-rewrite-release-surfaces
verified: <EXEC_TS>
status: passed
score: 6/6 must-haves verified
behavior_unverified: 0
overrides_applied: 0
---

# Phase 21: CONTRACT rewrite + release surfaces Verification Report

**Phase Goal:** Contract and release surfaces tell the truth that the generator is the refresh path; v1.20.0 ships at frozen catalogue with honest CHANGELOG
**Verified:** <EXEC_TS>
**Status:** passed
**Verdict:** passed
**Re-verification:** Yes; live-gate re-run on 2026-09-14 after the P3 regate

## Goal Achievement

Every claim below was re-checked against the live tree this session. SUMMARY and P3 probe claims were not trusted; gates, git facts, and counts were re-run from scratch.

### Observable Truths

| # | Truth | Status | Evidence |
|---|-------|--------|----------|
| 1 | `python tooling/check_release.py` exits 0 at HEAD | VERIFIED (behavioral) | <observed: final banner and exit code> |
| 2 | Generator replay is byte-stable on the live catalogue | VERIFIED (behavioral) | `python tooling/generate_capability_map.py --generated-on 2026-08-27 --check` exit 0 |
| 3 | Annotated tag `v1.20.0` peels to `ffe385a`, type `tag` | VERIFIED | `git cat-file -t v1.20.0` printed `tag`; `git rev-parse --short "v1.20.0^{commit}"` printed `ffe385a` |
| 4 | Version trio and `map_version` 1.20.0 agree | VERIFIED | `.claude-plugin/plugin.json` version `1.20.0`; `RELEASE-INFO.txt` says 1.20.0; CHANGELOG top section `## [1.20.0]: 2026-08-27`; map envelope `"map_version": "1.20.0"`. `check_release` enforces the trio (truth 1) |
| 5 | Catalog frozen at 63 packs / 65 dirs | VERIFIED | `python -c "import json; print(len(json.load(open('catalog.json'))['packs']))"` printed 63; `ls -1 packs | wc -l` printed 65 |
| 6 | ROADMAP success criteria 1-4 each map to live evidence | VERIFIED | SC1 CONTRACT section 4 names the generator (grep match); SC2 section 8 residual is the mandatory note-overrides input only; SC3 truths 1 and 4; SC4 trio + tag + CHANGELOG [1.20.0]; the GitHub Release is scoped to the user-gated ship step (see Notes) |

**Score:** 6/6 truths verified (0 present-but-behavior-unverified)

### Behavioral Spot-Checks

| Behavior | Command | Result | Status |
|---|---|---|---|
| Release gate at HEAD | `python tooling/check_release.py` | exit 0 | PASS |
| Byte-stable replay | `python tooling/generate_capability_map.py --generated-on 2026-08-27 --check` | exit 0 | PASS |
| Tag identity | `git cat-file -t v1.20.0` + peel | `tag` / `ffe385a` | PASS |
| Trio agreement | `check_release` trio check | enforced, gate PASS | PASS |
| Catalog freeze | catalog packs + packs/ dir count | 63 / 65 | PASS |

### Requirements Coverage

| Requirement | Source Plan | Description | Status | Evidence |
|---|---|---|---|---|
| MAP-21-05 | 21-01-PLAN.md | CONTRACT section 4 names the generator; section 8 residual reduced to the committed note-override file | SATISFIED | Truths 1-4, 6 |
| REL-21-01 | 21-01-PLAN.md | check_release PASS at frozen 63/65; map_version 1.20.0; no new packs | SATISFIED | Truths 1, 4, 5 |
| REL-21-02 | 21-02-PLAN.md | Version surfaces + CHANGELOG [1.20.0] honest; annotated tag; GitHub Release when the product surface is ready | SATISFIED | Truths 3, 4, 6; release half scoped to the ship handoff |

No orphaned requirements: ROADMAP maps only MAP-21-05, REL-21-01, REL-21-02 to Phase 21.

### Notes for the Record

Known open tail (not a phase criterion failure): the GitHub Release is pending the user-gated publish (Decision 4 of the P8 spec). ROADMAP SC4 conditions the release on "when the product surface is ready", and REL-21-02 scopes it to this package's ship step. Recorded in master_flow as `verify: passed_with_notes:gh_release_pending_user_go`. This verdict string is a historical record and must not be rewritten after wave 2.

---

_Verified: <EXEC_TS>_
_Verifier: gsd phase verification (P8 ledger close)_
```

- [ ] **Step 5: Record the gates in the phase master_flow**

Edit `.planning/phases/21-contract-rewrite-release-surfaces/master_flow_state.json` with these exact replacements:

Old:

```json
  "current_gate": "gap_analysis",
```

New:

```json
  "current_gate": "doc_check",
```

Old:

```json
    "security_audit"
  ],
```

New:

```json
    "security_audit",
    "gap_analysis",
    "verify"
  ],
```

Old:

```json
    "security_audit": "passed:secured"
  },
```

New:

```json
    "security_audit": "passed:secured",
    "gap_analysis": "passed",
    "verify": "passed_with_notes:gh_release_pending_user_go"
  },
```

Old:

```json
    "security_audit": ".planning/phases/21-contract-rewrite-release-surfaces/21-SECURITY_AUDIT.md"
  },
```

New:

```json
    "security_audit": ".planning/phases/21-contract-rewrite-release-surfaces/21-SECURITY_AUDIT.md",
    "gap_analysis": ".planning/phases/21-contract-rewrite-release-surfaces/21-GAP_ANALYSIS.md",
    "verify": ".planning/phases/21-contract-rewrite-release-surfaces/21-VERIFICATION.md"
  },
```

Old:

```json
  "updated_at": "2026-09-15T02:10:53.000Z",
```

New:

```json
  "updated_at": "<EXEC_TS>",
```

Old:

```json
  "notes": "Initialized master_flow for phase 21"
```

New:

```json
  "notes": "Phase 21 closed 2026-09-14: gap_analysis passed; verify passed_with_notes (GitHub Release pending user go, ship handoff). Milestone ledger closed in P8."
```

Leave `skipped` (it already contains `doc_check`, `milestone_audit`, `complete`, `retrospective`), `config_snapshot`, `regate_attempts`, and all other verdicts untouched. `doc_check` stays in `skipped` because the gate is disabled; parking `current_gate` there mirrors phases 19/20.

- [ ] **Step 6: Clear the root pointer**

Replace the entire content of `.planning/master_flow_state.json` with:

```json
{
  "schema_version": 1,
  "kind": "pointer",
  "active_phase": null,
  "active_phase_dir": null,
  "active_state": null,
  "lock": null,
  "updated_at": "<EXEC_TS>",
  "notes": "v1.20.0 milestone closed 2026-09-14; GitHub Release pending user go"
}
```

No gsd-core script reads this pointer (zero references under the gsd-core bin/workflows/references/templates, verified in the spec); agent-side skills consume it, and a future `/gsd:new-milestone` rewrites it.

- [ ] **Step 7: Verify the JSON end state**

```bash
python - <<'EOF'
import json, os
m = json.load(open('.planning/phases/21-contract-rewrite-release-surfaces/master_flow_state.json'))
assert 'gap_analysis' in m['completed'] and 'verify' in m['completed']
assert m['verdicts']['gap_analysis'] == 'passed'
assert m['verdicts']['verify'] == 'passed_with_notes:gh_release_pending_user_go'
assert m['current_gate'] == 'doc_check'
assert os.path.isfile(m['artifacts']['gap_analysis'])
assert os.path.isfile(m['artifacts']['verify'])
assert 'doc_check' in m['skipped'] and 'milestone_audit' in m['skipped']
r = json.load(open('.planning/master_flow_state.json'))
assert r['active_phase'] is None and r['active_phase_dir'] is None
assert r['active_state'] is None and r['lock'] is None
print('TASK 1 END STATE OK')
EOF
```

Expected: `TASK 1 END STATE OK`. No commit (gitignored paths).

---

### Task 2: Wave-1 ledger edits (closed, ship pending)

**Files:**
- Modify: `.planning/STATE.md`
- Modify: `.planning/PROJECT.md`
- Modify: `.planning/ROADMAP.md` (lines 5, 20-22, 34, 103, 105)
- Modify: `.planning/GAP.md` (full rewrite)

**Interfaces:**
- Consumes: Task 1 end state (gates passed).
- Produces: wave-1 posture on every shared surface; no shipped claim and no release URL anywhere. Task 3 asserts it; Task 5's no-go branch terminates in it; Task 6 rewrites parts of it.

**Model:** flash

- [ ] **Step 1: STATE.md frontmatter**

Old:

```yaml
status: planning
stopped_at: Phase 20 complete, ready to plan Phase 21
last_updated: "2026-08-27T14:57:36.504Z"
last_activity: 2026-08-27
last_activity_desc: Phase 20 complete, transitioned to Phase 21
```

New:

```yaml
status: shipping
stopped_at: v1.20.0 ledger closed, GitHub Release pending user go
last_updated: "<EXEC_TS>"
last_activity: 2026-09-14
last_activity_desc: v1.20.0 milestone closed; publish handoff pending user go
```

Old:

```yaml
progress:
  total_phases: 3
  completed_phases: 2
  total_plans: 3
  completed_plans: 3
  percent: 67
```

New:

```yaml
progress:
  total_phases: 3
  completed_phases: 3
  total_plans: 5
  completed_plans: 5
  percent: 100
```

Leave `state_head` and all other frontmatter fields unchanged.

- [ ] **Step 2: STATE.md body**

Old:

```markdown
**Current focus:** Phase 19, Machine-readable classification rules (MAP-21-01)
```

New:

```markdown
**Current focus:** v1.20.0 milestone closed; publish handoff pending user go
```

Old:

```markdown
Phase: 21 of 21 (CONTRACT rewrite + release surfaces)
Plan: Not started
Status: Ready to plan
Last activity: 2026-08-27 — Phase 20 complete, transitioned to Phase 21

Progress: [███░░░░░░░] 33%
```

New:

```markdown
Phase: 21 of 21 (CONTRACT rewrite + release surfaces)
Plan: 21-01, 21-02 complete
Status: Phase complete (gap_analysis + verify passed 2026-09-14)
Last activity: 2026-09-14, v1.20.0 milestone closed; publish handoff pending user go

Progress: [██████████] 100%
```

Old:

```markdown
FUT-05 generator residual is this milestone, not deferred.
```

New:

```markdown
FUT-05 generator residual closed in v1.20.0.
```

Old:

```markdown
Last session: 2026-08-27T12:52:40.008Z
Stopped at: Phase 20 complete, ready to plan Phase 21
Resume file: None
**Resume:** `/gsd:plan-phase 19`
```

New:

```markdown
Last session: <EXEC_TS>
Stopped at: v1.20.0 ledger closed, ship handoff pending user go
Resume file: None
**Resume:** `/gsd:new-milestone` (no open phase)
```

The Shipped section keeps its `## Shipped (v1.19.1)` heading and block unchanged in wave 1.

- [ ] **Step 3: PROJECT.md Current Milestone posture**

Insert directly under the `**Goal:**` line of the `## Current Milestone: v1.20.0 FUT-05 byte-stable capability-map generator` section:

```markdown
**Status:** v1.20.0 milestone closed 2026-09-14; GitHub Release pending user go (ship handoff; no shipped URL yet).
```

Change nothing else in PROJECT.md this wave except the Current State deferred list: the clause `full FUT-05 byte-stable map generator (mechanical slice + CONTRACT residual only)` becomes `FUT-05 byte-stable map generator — closed in v1.20.0` (STATE and GAP now close FUT-05; PROJECT must not still list it as open). The `**Shipped:** v1.19.1 ...` line and the `*Last updated:*` footer stay for wave 2.

- [ ] **Step 4: ROADMAP edits**

Line 5 overview. Old: `map_version **1.19.1**`; new: `map_version **1.20.0**` (the rest of the line, including `63 catalog packs / 65 dirs` and `644 entries / 32 clusters`, is already correct and unchanged).

Lines 20-22 Next section. Old:

```markdown
## Next

v1.20.0: FUT-05 byte-stable capability-map generator (SEED-002 / OBJ-1). Phases 19-21 below.
```

New:

```markdown
## Next

v1.20.0 executed; ledger closed 2026-09-14; GitHub Release in ship handoff (user-gated).
```

Line 34. Old:

```markdown
- [ ] **Phase 21: CONTRACT rewrite + release surfaces** - Refresh path names the generator; residual closed; 1.20.0 surfaces, CHANGELOG, tag, GitHub Release
```

New:

```markdown
- [x] **Phase 21: CONTRACT rewrite + release surfaces** - Refresh path names the generator; residual closed; 1.20.0 surfaces, CHANGELOG, tag, GitHub Release (completed 2026-09-14)
```

Line 103 progress row. Old:

```markdown
| 21. CONTRACT rewrite + release surfaces | 2/2 | Executed | - |
```

New:

```markdown
| 21. CONTRACT rewrite + release surfaces | 2/2 | Complete | 2026-09-14 |
```

Line 105 note. Old:

```markdown
Phase 21 product gates PASS; impl_review re-gated 2026-09-14. Phase close (gap_analysis, verify, milestone ledger): P8.
```

New:

```markdown
Phase 21 closed 2026-09-14 (gap_analysis + verify passed). GitHub Release: ship handoff.
```

Do not touch the coverage table (`Complete (gh release: P8)` clears only in Task 6) or the shipped-milestones list.

- [ ] **Step 5: GAP.md full rewrite**

Replace the entire content of `.planning/GAP.md` with exactly:

```markdown
FUT-05 byte-stable capability-map generator: CLOSED in v1.20.0.

OBJ-1 satisfied. A stdlib generator (`tooling/generate_capability_map.py`)
regenerates `docs/capability-pack-map.json` from committed inputs
(classification rules plus the mandatory 644-row note-overrides file), replays
byte-stable, and stays CI-validated beside the mechanical gates. CONTRACT
section 4 names the generator as the refresh path; the section 8 residual is
the mandatory note-overrides input only. map_version 1.20.0, schema 2, 644
entries, 32 clusters, catalog frozen at 63 packs / 65 dirs. Annotated tag
`v1.20.0` on `ffe385a`.

Remaining human input: the note-overrides file is mandatory (the generator
fails closed without it). It records per-row judgment already made; it demands
no new judgment per release.

Still deferred (carried, not FUT-05): FUT-04 Army CBA (403, no grant), AAF
Product Support + Software (not vetted), IO-05/06 packs, se-agents sibling-repo
refresh, DoDM 5000.102 (unverified). See STATE Deferred Items. Post-1.20.0
CI and tooling work lives in CHANGELOG [Unreleased] for the next release.
```

- [ ] **Step 6: Sanity read-back**

```bash
grep -n "pending user go" .planning/STATE.md .planning/PROJECT.md
# Expected: the new wave-1 lines in both files
grep -n "1.19.1\|1.20.0" .planning/ROADMAP.md | head -5
# Expected: line 5 says 1.20.0; 1.19.1 only in the Shipped Milestones section
cat .planning/GAP.md
# Expected: the CLOSED rewrite, no "Follow-up: Finish FUT-05"
```

No commit (gitignored paths).

---

### Task 3: Wave-1 verification asserts

**Files:**
- Read-only: `.planning/STATE.md`, `.planning/PROJECT.md`, `.planning/ROADMAP.md`, `.planning/GAP.md`, both `master_flow_state.json` files

**Interfaces:**
- Consumes: Task 1 and Task 2 end states.
- Produces: `WAVE-1 ASSERTS: ALL PASS`. Task 4 proceeds only on this; Task 5's no-go branch re-runs this exact block to confirm the ledger still tells the truth.

**Model:** flash

- [ ] **Step 1: Run the assert block**

Run from the repo root; any non-zero exit or `FAIL` line means fix the offending Task 1/2 edit and re-run before proceeding:

```bash
# STATE: shipping posture, planning residue gone, 3 phases / 5 plans / 100 percent
test "$(grep -c '^status: shipping' .planning/STATE.md)" = 1
test "$(grep -c 'status: planning' .planning/STATE.md)" = 0
test "$(grep -c 'plan-phase 19' .planning/STATE.md)" = 0
grep -q 'completed_phases: 3' .planning/STATE.md
grep -q 'total_plans: 5' .planning/STATE.md
grep -q 'completed_plans: 5' .planning/STATE.md
grep -q 'percent: 100' .planning/STATE.md
grep -q 'pending user go' .planning/STATE.md
# PROJECT: ship-pending posture, no premature shipped URL, Shipped still ends at v1.19.1
grep -q 'milestone closed' .planning/PROJECT.md
grep -q 'GitHub Release pending user go' .planning/PROJECT.md
test "$(grep -c 'releases/tag/v1.20.0' .planning/PROJECT.md)" = 0
grep -q 'Shipped:\*\* v1.19.1' .planning/PROJECT.md
# ROADMAP: overview, phase list, progress row, shipped-history scoping
test "$(sed -n '5p' .planning/ROADMAP.md | grep -c '1\.20\.0')" = 1
test "$(sed -n '5p' .planning/ROADMAP.md | grep -c '1\.19\.1')" = 0
test "$(grep -c '^- \[x\] \*\*Phase 21' .planning/ROADMAP.md)" = 1
test "$(grep -c '^- \[ \] \*\*Phase 21' .planning/ROADMAP.md)" = 0
grep -q '| 21. CONTRACT rewrite + release surfaces | 2/2 | Complete | 2026-09-14 |' .planning/ROADMAP.md
awk '/^## Shipped Milestones/{s=1} /^## Next/{s=0} /1\.19\.1/ && !s && !/Depends on/ {print "FAIL: 1.19.1 outside shipped history: " $0; exit 1}' .planning/ROADMAP.md
# GAP.md
test "$(grep -c 'Follow-up: Finish FUT-05' .planning/GAP.md)" = 0
grep -q 'CLOSED' .planning/GAP.md
# master_flow + root pointer (Task 1 end state)
python - <<'EOF'
import json, os
m = json.load(open('.planning/phases/21-contract-rewrite-release-surfaces/master_flow_state.json'))
assert 'gap_analysis' in m['completed'] and 'verify' in m['completed']
assert m['verdicts']['gap_analysis'].startswith('passed')
assert m['verdicts']['verify'].startswith('passed')
assert m['current_gate'] == 'doc_check'
assert os.path.isfile(m['artifacts']['gap_analysis'])
assert os.path.isfile(m['artifacts']['verify'])
r = json.load(open('.planning/master_flow_state.json'))
assert r['active_phase'] is None and r['lock'] is None
print('master_flow OK')
EOF
# Product gates (local, no network)
python tooling/check_release.py > /dev/null
python tooling/generate_capability_map.py --generated-on 2026-08-27 --check > /dev/null
# Tree and tag: nothing staged, no tracked modifications, tag unmoved
git diff --cached --quiet
test -z "$(git status --short | grep -v '^??')"
test "$(git rev-parse --short "v1.20.0^{commit}")" = ffe385a
echo "WAVE-1 ASSERTS: ALL PASS"
```

Expected final line: `WAVE-1 ASSERTS: ALL PASS`.

---

### Task 4: Publish-readiness checklist (local) and release-notes file

**Files:**
- Create: `docs/superpowers/release-notes/v1.20.0.md`
- Read-only: `CHANGELOG.md`, git state

**Interfaces:**
- Consumes: Task 3 pass; CHANGELOG `[1.20.0]` section (lines 50-78 of `CHANGELOG.md`).
- Produces: the notes file consumed by Task 5's `gh release create --notes-file`; recorded `<N>` ahead count consumed by Task 5's gate question. Remote checks are NOT run here (no network before Task 5).

**Model:** flash

- [ ] **Step 1: Run the local readiness checks and record results**

```bash
git rev-list --count origin/main..HEAD          # record as <N> (29 on 2026-09-14)
git rev-list --count HEAD..origin/main          # must print: 0
git cat-file -t v1.20.0                         # must print: tag
git rev-parse --short "v1.20.0^{commit}"        # must print: ffe385a
git status --short                              # only untracked docs/superpowers/ entries
git diff --cached --quiet && echo STAGE-CLEAN   # must print: STAGE-CLEAN
python tooling/check_release.py                 # exit 0
python tooling/generate_capability_map.py --generated-on 2026-08-27 --check   # exit 0
```

All must hold before Task 5. If the ahead count differs from `<N>` recorded here, Task 5 must present the fresh number, never the stale one.

- [ ] **Step 2: Write the release-notes file**

Create `docs/superpowers/release-notes/v1.20.0.md` (create the directory if needed) with exactly this content: a title line, the CHANGELOG `[1.20.0]` section body verbatim, and the closing deferred line. Do not include anything from `[Unreleased]`.

```markdown
# v1.20.0: FUT-05 byte-stable capability-map generator

FUT-05 byte-stable capability-map generator on the same catalog 63 / dirs 65
basis as 1.19.1. No new packs. CONTRACT refresh path is the committed generator.
Note overrides remain the human residual.

### Added

- Stdlib generator `tooling/generate_capability_map.py`.
- Mandatory 644-row `docs/capability-pack-map-note-overrides.json`.
- `docs/classification-rules.json` (MAP-21-01).
- `check_classification_rules.py` on the local `check_release` path.
- Generator `--check` also on that path.

### Changed

- Version surfaces and `map_version` 1.19.1 to 1.20.0. Cluster membership still
  644; schema_version still 2. No reclassification.
- CONTRACT section 4 names the generator; section 8 residual is note overrides
  only.

### Deferred / accepted (not built)

- **FUT-04 Army CBA** DEFERRED - ASAFM PDF 403 on 2026-08-20 retry; no in-source grant.
- **AAF Product Support + Software pathway** still NOT yet vetted - do not use.
- **PACK-20-01..03** deferred-with-evidence; zero packs built this milestone.
- **IO-05 Integration** DEFERRED - AAF Software pathway still NOT yet vetted.
- **IO-06 Logistics diversity** DEFERRED - AAF Product Support still NOT yet vetted.
- **IO-07 Stakeholder Engagement** ACCEPT - no invented pack.
- **se-agents** sibling-repo work stays out of this catalogue.
- **DoDM 5000.102** UNVERIFIED - no pack built.

Tagged as `v1.20.0` on commit `ffe385a`. Still deferred beyond this release:
FUT-04 Army CBA, AAF Product Support + Software, IO-05/06 packs, se-agents
sibling-repo refresh, DoDM 5000.102.
```

The middle block must be character-identical to the `[1.20.0]` section body in `CHANGELOG.md` (verify with a diff against CHANGELOG.md lines 50-78 if in doubt).

- [ ] **Step 3: Confirm the notes file is untracked, never staged**

```bash
git status --short docs/superpowers/release-notes/
# Expected: "?? docs/superpowers/release-notes/" (untracked)
git diff --cached --quiet && echo STAGE-CLEAN
```

No commit. Do not `git add` anything.

---

### Task 5: Execution-time user gate and payoff publish

**Files:**
- Create (branch-dependent): `.planning/SHIP-HANDOFF.md`

**Interfaces:**
- Consumes: Task 4's notes file and `<N>`; Task 3's assert block (re-run on terminal branches).
- Produces: on go, `<RELEASE_URL>` (from `gh release view v1.20.0 --json url -q .url`) consumed by Tasks 6-7. On self-run with release absent, or no-go: terminal handoff-stop with `.planning/SHIP-HANDOFF.md`; Tasks 6-7 are skipped.

**Model:** standard

- [ ] **Step 1: Re-run the full readiness checklist immediately before the question**

First re-run the entire local block from Task 4 Step 1 (ahead count, behind count, tag type, tag peel, status, stage-clean, both gates), then the remote checks (first network use in this package):

```bash
git ls-remote --tags origin refs/tags/v1.20.0   # must be empty (tag not on origin)
gh release view v1.20.0                          # must fail: release not found
gh auth status                                   # must succeed
git rev-list --count origin/main..HEAD           # fresh ahead count for the question
git rev-list --count HEAD..origin/main           # must be 0
```

If any check drifts from the Task 4 state (tag now on origin, release exists, count changed), stop and re-derive before asking; never push on stale counts.

- [ ] **Step 2: Present the user gate (AskUserQuestion or any blocking three-option prompt)**

Present the exact publish block and the freshly recorded counts:

```bash
git push origin main
git push origin v1.20.0
gh release create v1.20.0 \
  --title "v1.20.0: FUT-05 byte-stable capability-map generator" \
  --notes-file docs/superpowers/release-notes/v1.20.0.md
```

Order is load-bearing: `main` first so the tag's commit is reachable, then the annotated tag (pushing cannot move it off `ffe385a`), then the release from the `[1.20.0]`-only notes file. No `--generate-notes`, no `gh pr create`.

Ask exactly one question with three options:

1. **Go: agent runs the publish.** Agent executes the three commands in order, then continues to Step 3.
2. **Self-run: user runs the publish block.** Agent waits for the user to report completion, then verifies with `gh release view v1.20.0` before capturing `<RELEASE_URL>`. If the release does not exist yet, treat as handoff-stop: the wave-1 posture holds, record in `.planning/SHIP-HANDOFF.md` (Step 5 contents, with a line noting the user took the block and the release is not yet visible) that the publish is still outstanding, and stop. Never backfill wave 2 without the release existing.
3. **No-go.** Skip the three commands and Tasks 6-7; write `.planning/SHIP-HANDOFF.md` (Step 5 contents); re-run the full Task 3 assert block to confirm the ledger still tells the wave-1 truth; stop.

- [ ] **Step 3: On go, run the publish**

```bash
git push origin main
git push origin v1.20.0
gh release create v1.20.0 \
  --title "v1.20.0: FUT-05 byte-stable capability-map generator" \
  --notes-file docs/superpowers/release-notes/v1.20.0.md
```

- [ ] **Step 4: Confirm the release and capture the URL**

```bash
gh release view v1.20.0
gh release view v1.20.0 --json url -q .url
# Record the printed URL as <RELEASE_URL>; all later edits use it verbatim.
```

If `gh release create` failed partway (for example main pushed but release create failed), do not blind-retry: re-run the failing command only, then re-run this confirmation. Proceed to Task 6.

- [ ] **Step 5: On no-go (or self-run with release absent), write the handoff note**

Write `.planning/SHIP-HANDOFF.md` with exactly (fill `<N>` from the fresh count):

```markdown
# v1.20.0 ship handoff (pending user execution)

Date: 2026-09-14. Package: P8 (phase 21 planning-ledger close). The v1.20.0
planning ledger is closed locally in the wave-1 posture: no shipped claim
exists on any surface. The GitHub Release awaits explicit user execution.

Ready state at handoff: main ahead of origin/main by <N> commits, 0 behind;
annotated tag `v1.20.0` peels to `ffe385a`; tag and release absent on origin;
`docs/superpowers/release-notes/v1.20.0.md` written from CHANGELOG [1.20.0].

Publish commands (run in order, from the repo root):

    git push origin main
    git push origin v1.20.0
    gh release create v1.20.0 --title "v1.20.0: FUT-05 byte-stable capability-map generator" --notes-file docs/superpowers/release-notes/v1.20.0.md

After the release exists, run wave-2 backfills per tasks 6-7 of
docs/superpowers/plans/2026-09-14-phase21-planning-ledger-close.md.
```

Then re-run the Task 3 block and stop. This is the package's honest terminal state on no-go.

---

### Task 6: Wave-2 backfills (only after the release exists)

**Files:**
- Modify: `.planning/STATE.md`, `.planning/ROADMAP.md`, `.planning/MILESTONES.md`, `.planning/PROJECT.md`, `.planning/REQUIREMENTS.md`
- Modify: `.planning/phases/21-contract-rewrite-release-surfaces/master_flow_state.json` (notes only), `.planning/master_flow_state.json` (notes only)

**Interfaces:**
- Consumes: `<RELEASE_URL>` from Task 5. Requires the release to exist (`gh release view v1.20.0` succeeds); never run otherwise.
- Produces: shipped posture on every surface with the URL backfilled; Task 7 asserts it.

**Model:** flash

- [ ] **Step 1: STATE.md frontmatter**

Old:

```yaml
status: shipping
stopped_at: v1.20.0 ledger closed, GitHub Release pending user go
```

New:

```yaml
status: complete
stopped_at: v1.20.0 shipped (<RELEASE_URL>)
```

Old:

```yaml
last_activity_desc: v1.20.0 milestone closed; publish handoff pending user go
```

New:

```yaml
last_activity_desc: v1.20.0 shipped; ledger backfilled
```

Bump `last_updated: "<EXEC_TS>"` again.

- [ ] **Step 2: STATE.md body, focus and position**

Old:

```markdown
**Current focus:** v1.20.0 milestone closed; publish handoff pending user go
```

New:

```markdown
**Current focus:** v1.20.0 shipped <RELEASE_URL>
```

Old:

```markdown
Plan: 21-01, 21-02 complete
Status: Phase complete (gap_analysis + verify passed 2026-09-14)
Last activity: 2026-09-14, v1.20.0 milestone closed; publish handoff pending user go
```

New:

```markdown
Plan: 21-01, 21-02 complete
Status: Phase complete; v1.20.0 shipped 2026-09-14
Last activity: 2026-09-14, v1.20.0 shipped <RELEASE_URL>
```

- [ ] **Step 3: STATE.md Shipped section**

Old heading and first lines:

```markdown
## Shipped (v1.19.1)

- **Release commit:** `6944c14`
```

New (new v1.20.0 block first, existing v1.19.1 block preserved below under a subheading):

```markdown
## Shipped (v1.20.0)

- **Release commit:** `ffe385a`
- **Annotated tag:** `v1.20.0`
- **GitHub Release:** <RELEASE_URL>
- **Basis:** catalog 63 / dirs 65; map_version 1.20.0; schema 2; 644 entries; 32 clusters
- **Gates:** RELEASE CHECK PASS · generator --check PASS
- **Audit:** none (milestone_audit disabled by config)

Honest scope: FUT-05 byte-stable capability-map generator. No new packs. Main continued after the tag with CI parity, link-policy, signpost validate_pack, and WR hardening; that work sits in CHANGELOG [Unreleased] and is not part of the tagged release.

### v1.19.1

- **Release commit:** `6944c14`
```

The rest of the v1.19.1 block (tag, URL, basis, gates, audit, honest-scope line) stays unchanged below.

- [ ] **Step 4: STATE.md Session Continuity**

Old:

```markdown
Stopped at: v1.20.0 ledger closed, ship handoff pending user go
```

New:

```markdown
Stopped at: v1.20.0 shipped <RELEASE_URL>
```

`**Resume:** `/gsd:new-milestone` (no open phase)` stays.

- [ ] **Step 5: ROADMAP shipped list and summary**

In the Shipped Milestones list, after the existing v1.19.1 bullet (line 12), add:

```markdown
- [x] **v1.20.0: FUT-05 byte-stable capability-map generator** (phases 19-21) ([release](<RELEASE_URL>) · archive: none (complete-milestone not run; ledger closed in place))
```

After the v1.19.1 summary block (after its `**Release:**` line, line 18), insert:

```markdown
### v1.20.0 summary

FUT-05 byte-stable capability-map generator shipped: cluster assignment and map JSON regenerate from committed inputs (classification rules plus the mandatory 644-row note-overrides file), replay byte-stable, and stay CI-validated; CONTRACT section 4 names the generator, section 8 residual is note overrides only; map_version 1.20.0, schema 2, 644 entries, 32 clusters; catalog frozen at 63 / 65. No new packs. Still deferred: FUT-04, AAF, IO-05/06, se-agents consumer, DoDM 5000.102.

- **Release:** `ffe385a` · tag `v1.20.0` · <RELEASE_URL>
```

- [ ] **Step 6: ROADMAP Next and coverage tail**

Old:

```markdown
## Next

v1.20.0 executed; ledger closed 2026-09-14; GitHub Release in ship handoff (user-gated).
```

New:

```markdown
## Next

None selected. v1.20.0 shipped 2026-09-14. Backlog candidates above remain.
```

Old:

```markdown
| REL-21-02 | Phase 21 | Complete (gh release: P8) |
```

New:

```markdown
| REL-21-02 | Phase 21 | Complete |
```

- [ ] **Step 7: MILESTONES.md new top entry**

Insert immediately after the `# Milestones` heading (before the existing `## v1.19.1 v1.19.1 (Shipped: 2026-08-20)` card):

```markdown
## v1.20.0 (shipped 2026-09-14)

FUT-05 byte-stable capability-map generator shipped: a stdlib generator (`tooling/generate_capability_map.py`) regenerates `docs/capability-pack-map.json` from committed inputs (classification rules plus the mandatory 644-row note-overrides file), replays byte-stable, and stays CI-validated beside the mechanical gates. CONTRACT section 4 names the generator as the refresh path; the section 8 residual is the mandatory note-overrides input only. map_version 1.20.0, schema 2, 644 entries, 32 clusters; catalog frozen at 63 packs / 65 dirs. No new packs. Phases 19-21, 5 plans.

- **Release commit:** `ffe385a` (`fix: align website product YAMLs to 1.20.0 (CR-01)`)
- **Annotated tag:** `v1.20.0` (`chore: annotate v1.20.0 generator refresh path`)
- **GitHub Release:** <RELEASE_URL>
- **Still deferred:** FUT-04 Army CBA; AAF Product Support + Software; IO-05/06 packs; se-agents sibling-repo refresh; DoDM 5000.102 UNVERIFIED
- **Honest scope:** main continued after the tag with CI parity, link-policy, signpost validate_pack, and WR hardening; that work sits in CHANGELOG [Unreleased] and is not part of the tagged release.
```

This is the clean v1.17/v1.18/v1.19.0 shape (one heading, theme paragraph, bullets), not the duplicated v1.19.1 card shape. Existing entries stay untouched.

- [ ] **Step 8: PROJECT.md Current State and Milestone**

Old Current State Shipped paragraph (as it reads after the Task 2 Step 3 wave-1 edit — the FUT-05 clause already says "closed in v1.20.0"):

```markdown
**Shipped:** v1.19.1 (2026-08-20) — Cleanup + Carried Backlog. Catalog still 63 packs / 65 dirs (+2 signposts); capability map schema 2, map_version **1.19.1**, 644 entries, 32 clusters; dual-gate includes `check_overlap` then `check_capability_map` inside `check_release`. No new packs this release. Honest deferred: FUT-04 Army CBA, AAF Product Support + Software pathway, IO-05/06 packs, FUT-05 byte-stable map generator — closed in v1.20.0, IO-07 accept, DoDM 5000.102 UNVERIFIED, se-agents consumer refresh (sibling repo).
```

New:

```markdown
**Shipped:** v1.20.0 (2026-09-14), FUT-05 byte-stable capability-map generator. Catalog frozen at 63 packs / 65 dirs (+2 signposts); map_version **1.20.0**, schema 2, 644 entries, 32 clusters; the stdlib generator regenerates the map from committed inputs and replays byte-stable; release <RELEASE_URL>. No new packs.
```

Old Prior line:

```markdown
**Prior:** v1.19.0 (2026-08-17) — Agent IO Depth (2 new packs + VV&A depth + DA remap).
```

New:

```markdown
**Prior:** v1.19.1 (2026-08-20), Cleanup + Carried Backlog.
```

Old wave-1 status line in the Current Milestone section:

```markdown
**Status:** v1.20.0 milestone closed 2026-09-14; GitHub Release pending user go (ship handoff; no shipped URL yet).
```

New:

```markdown
**Status:** v1.20.0 shipped 2026-09-14. GitHub Release: <RELEASE_URL>.
```

Old footer:

```markdown
*Last updated: 2026-08-27 after starting v1.20.0*
```

New:

```markdown
*Last updated: 2026-09-14 after v1.20.0 close and ship*
```

- [ ] **Step 9: REQUIREMENTS.md REL-21-02 tail and coverage row**

Old:

```markdown
- [x] **REL-21-02**: Version surfaces + CHANGELOG [1.20.0] record the generator honestly; annotated tag + GitHub Release when the product surface is ready (tag v1.20.0 on ffe385a; GitHub Release: P8 /gsd-ship)
```

New (checkbox stays `[x]`, only the tail changes):

```markdown
- [x] **REL-21-02**: Version surfaces + CHANGELOG [1.20.0] record the generator honestly; annotated tag + GitHub Release when the product surface is ready (GitHub Release: <RELEASE_URL>)
```

Old:

```markdown
| REL-21-02 | Phase 21 | Complete (gh release: P8) |
```

New:

```markdown
| REL-21-02 | Phase 21 | Complete |
```

No other tick or line changes.

- [ ] **Step 10: Refresh pending-release wording in both master_flow files (notes only)**

Phase `.planning/phases/21-contract-rewrite-release-surfaces/master_flow_state.json`: replace

```json
  "notes": "Phase 21 closed 2026-09-14: gap_analysis passed; verify passed_with_notes (GitHub Release pending user go, ship handoff). Milestone ledger closed in P8."
```

with

```json
  "notes": "Phase 21 closed 2026-09-14: gap_analysis passed; verify passed_with_notes (historical; GitHub Release was pending user go at close). v1.20.0 shipped 2026-09-14: <RELEASE_URL>"
```

and bump `"updated_at"` to the current `<EXEC_TS>`. All verdicts (including the historical `passed_with_notes:gh_release_pending_user_go`) and every other field stay untouched.

Root `.planning/master_flow_state.json`: replace

```json
  "notes": "v1.20.0 milestone closed 2026-09-14; GitHub Release pending user go"
```

with

```json
  "notes": "v1.20.0 shipped 2026-09-14; GitHub Release <RELEASE_URL>"
```

and bump `"updated_at"`. `active_phase`, `active_phase_dir`, `active_state`, `lock` stay `null`.

---

### Task 7: Wave-2 verification asserts

**Files:**
- Read-only: the five top-level ledger files, `MILESTONES.md`, `RELEASE-INFO.txt`, `docs/capability-pack-map.json`, git state, `gh release view`

**Interfaces:**
- Consumes: Task 6 end state and `<RELEASE_URL>`.
- Produces: `WAVE-2 ASSERTS: ALL PASS`; report `<RELEASE_URL>` and the final ledger state.

**Model:** flash

- [ ] **Step 1: Run the assert block**

```bash
URL="$(gh release view v1.20.0 --json url -q .url)"
test -n "$URL"
# MILESTONES: exactly one clean v1.20.0 entry; URL matches the live release
test "$(grep -c '^## v1.20.0 (shipped ' .planning/MILESTONES.md)" = 1
grep -qF "$URL" .planning/MILESTONES.md
# STATE and ROADMAP carry the release URL
grep -qF "$URL" .planning/STATE.md
grep -qF "$URL" .planning/ROADMAP.md
grep -qF "$URL" .planning/PROJECT.md
grep -qF "$URL" .planning/REQUIREMENTS.md
# P8 ship tails cleared everywhere
test "$(grep -c 'gh release: P8' .planning/REQUIREMENTS.md)" = 0
test "$(grep -c 'gh release: P8' .planning/ROADMAP.md)" = 0
# STATE fully shipped
test "$(grep -c '^status: complete' .planning/STATE.md)" = 1
test "$(grep -c 'shipping' .planning/STATE.md)" = 0
# Cross-surface: wave-1 ship-pending wording fully replaced (per-file grep; multi-file grep -c prints path:count lines)
for f in .planning/PROJECT.md .planning/STATE.md .planning/ROADMAP.md .planning/REQUIREMENTS.md .planning/GAP.md; do
  test "$(grep -c 'pending user go' "$f")" = 0 || { echo "FAIL: pending user go survives in $f"; exit 1; }
done
# Cross-surface contradiction sweep (top-level ledger only; milestone archives are history)
for f in .planning/PROJECT.md .planning/STATE.md .planning/ROADMAP.md .planning/REQUIREMENTS.md .planning/GAP.md .planning/MILESTONES.md; do
  test "$(grep -c 'ready to plan Phase 21' "$f")" = 0 || { echo "FAIL: stale marker in $f"; exit 1; }
  test "$(grep -c 'Phase 20 complete, ready' "$f")" = 0 || { echo "FAIL: stale marker in $f"; exit 1; }
done
# map_version agreement across surfaces
grep -q 'map_version \*\*1.20.0\*\*' .planning/ROADMAP.md
grep -q '"map_version": "1.20.0"' docs/capability-pack-map.json
grep -q '1\.20\.0' RELEASE-INFO.txt
# Tag unchanged; wave-2 edits touched only ignored and untracked paths
test "$(git rev-parse --short "v1.20.0^{commit}")" = ffe385a
test -z "$(git status --short | grep -v '^??')"
git diff --cached --quiet
echo "WAVE-2 ASSERTS: ALL PASS"
```

Expected final line: `WAVE-2 ASSERTS: ALL PASS`. Any failure means a Task 6 edit missed a surface; fix and re-run.

- [ ] **Step 2: Report**

Report `<RELEASE_URL>`, the fresh `git rev-list --count origin/main..HEAD`, and the one-line final ledger posture (STATE `status: complete`, phase master_flow parked at `doc_check`, root pointer cleared, MILESTONES `## v1.20.0 (shipped 2026-09-14)` top entry). No commit; nothing staged.
