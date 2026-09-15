# Context: phase21-planning-ledger-close (2026-09-14)

## Context brief

**Primary question**: What shared planning-ledger fields are still stale after P3, what does an honest Phase 21 / v1.20.0 close require (gap/verify posture, STATE/ROADMAP/MILESTONES/GAP, master_flow complete), and what procedure does the payoff GitHub Release need given stock `/gsd-ship` vs this repo's release meaning?

**Sub-questions**:
1. Exact remaining stale STATE / ROADMAP overview+phase-list / MILESTONES / GAP / master_flow fields (quoted + line refs), excluding work P3 already finished.
2. What P3 already did (do-not-redo list) vs packages.md P8 in_scope.
3. Phase 19/20 gap_analysis + verify shape; what "Phase 21 complete" means with `current_gate: gap_analysis` and missing artifacts.
4. What stock `gsd-ship` actually does (steps, gates, ledger needs) vs 21-02's "gh release" meaning of `/gsd-ship`.
5. Git/tag/remote posture and the CHANGELOG `[Unreleased]` vs tagged `1.20.0` mismatch.
6. Design choices: execute vs waive gap/verify; agent-run vs user-run publish; MILESTONES wording; GAP rewrite shape.

**Success criteria**: SC1 remaining stale quotes; SC2 P3 do-not-redo; SC3 gap/verify honesty options; SC4 ship procedure summary; SC5 git/CHANGELOG facts + human-decision surface.

**Out of scope**:
- Product code under `docs/products/`, `tooling/`, version trio, packs, CI (P1/P4/P5/P6/P7 done).
- Re-ticking REQUIREMENTS MAP-21-05 / REL-21-01 / REL-21-02 (P3 done).
- Re-writing 21-IMPL_REVIEW or re-running the six P3 product probes unless a live check fails.
- Retagging or moving `v1.20.0` off `ffe385a`.
- Folding post-tag CI commits into the annotated tag without an explicit human retag decision (default: do not).

**Budget**: single-pass context gate.

**Workspace baseline** (2026-09-14/15 probe):
- Branch `main`, HEAD `5b2183c`.
- Annotated local tag `v1.20.0` → `ffe385a` (`fix: align website product YAMLs to 1.20.0 (CR-01)`).
- `origin/main` = `55ef575` (29 commits behind HEAD; `0	29` left-right).
- Tag and GitHub Release **absent** on remote (`git ls-remote` no `v1.20.0`; `gh release view v1.20.0` → release not found).
- Working tree: only untracked `docs/superpowers/` (this drain's context/packages).
- `.planning/` is gitignored (STATE Notes; commit `55ef575` policy). Ledger edits are local-only.

**Parent-verified package facts** (packages.md P8 + P3 outcome):
- P3 done 2026-09-14: re-gate impl_review, master_flow review wave recorded, REQUIREMENTS + ROADMAP product ticks.
- P8 remaining delta: shared ledger close + `/gsd-ship` payoff for v1.20.0 GitHub Release (X1: P8 owns ship).
- P8 in_scope still lists some items P3 already closed; treat the **outcome** block as truth and narrow P8 to residual stale surfaces below.

## Findings

Grades: CORROBORATED 18, SINGLE-SOURCE 3, CONFLICTED 1 (stock gsd-ship vs repo `/gsd-ship` meaning), STALE 8 (ledger fields that still contradict shipped product).

| # | Claim | Grade |
|---|-------|-------|
| 1 | STATE still `status: planning`, `stopped_at: Phase 20 complete...`, `completed_phases: 2` | CORROBORATED (STALE) |
| 2 | ROADMAP overview still `map_version **1.19.1**` | CORROBORATED (STALE) |
| 3 | ROADMAP phase-list Phase 21 still `- [ ]` | CORROBORATED (STALE) |
| 4 | ROADMAP progress Phase 21 is `2/2` / `Executed`; coverage MAP/REL Complete | CORROBORATED (P3; do not redo) |
| 5 | REQUIREMENTS MAP-21-05 / REL-21-01 / REL-21-02 all `[x]` with required-override wording + P8 ship note | CORROBORATED (P3; do not redo) |
| 6 | MILESTONES has v1.17–v1.19.1 only; no v1.20.0 shipped entry | CORROBORATED (STALE gap) |
| 7 | GAP.md still "Follow-up: Finish FUT-05..." | CORROBORATED (STALE; b-08) |
| 8 | Phase 21 master_flow `current_gate` = `gap_analysis`; reviews through security_audit completed; gap/verify not in completed | CORROBORATED |
| 9 | No `21-GAP_ANALYSIS.md` / `21-VERIFICATION.md` on disk | CORROBORATED |
| 10 | Phase 19/20 ran gap+verify to `passed`, then parked `current_gate` at `doc_check` (disabled) | CORROBORATED |
| 11 | Root pointer still `active_phase: 21` locked | CORROBORATED |
| 12 | Stock `gsd-ship` = verify-gate → push branch → `gh pr create`, not `gh release create` | CORROBORATED |
| 13 | 21-02 PLAN/SUMMARY redefine `/gsd-ship` as GitHub Release owner for annotated `v1.20.0` | CORROBORATED |
| 14 | Stock ship vs repo ship meaning conflict | CONFLICTED (resolve in design) |
| 15 | Local tag on `ffe385a`; 15 commits after tag on HEAD; 14 commits origin→tag | CORROBORATED |
| 16 | CHANGELOG has both `## [Unreleased]` (P4/P5 CI) and `## [1.20.0]` (generator) | CORROBORATED |
| 17 | Unreleased body landed in commits after tag tip (`e9c1d12`, `a42e3d9`, …) | CORROBORATED |
| 18 | PROJECT.md Current State still "Shipped: v1.19.1" / milestone in progress | CORROBORATED (STALE; optional P8 touch) |
| 19 | packages.md P8 in_scope still lists REQUIREMENTS ticks already done by P3 | STALE package prose vs P3 outcome |

## Remaining stale ledger (exact quotes)

### STATE (`.planning/STATE.md`) — primary P8

Frontmatter:

```yaml
milestone: v1.20.0
current_phase: 21
current_phase_name: CONTRACT rewrite + release surfaces
status: planning
stopped_at: Phase 20 complete, ready to plan Phase 21
last_updated: "2026-08-27T14:57:36.504Z"
last_activity: 2026-08-27
last_activity_desc: Phase 20 complete, transitioned to Phase 21
progress:
  total_phases: 3
  completed_phases: 2
  total_plans: 3
  completed_plans: 3
  percent: 67
```

Body still wrong for a closed milestone:

| Location | Quote |
|----------|-------|
| Project Reference | `**Current focus:** Phase 19, Machine-readable classification rules (MAP-21-01)` |
| Current Position | `Plan: Not started` / `Status: Ready to plan` / `Last activity: 2026-08-27 — Phase 20 complete, transitioned to Phase 21` |
| Progress bar | `Progress: [███░░░░░░░] 33%` |
| Session Continuity | `Stopped at: Phase 20 complete, ready to plan Phase 21` / `**Resume:** `/gsd:plan-phase 19`` |
| Shipped section | Still only **Shipped (v1.19.1)**; no v1.20.0 ship block |

Honest close targets: `status` past planning (phase/milestone complete or shipping), `stopped_at` / resume no longer Phase 20 or plan-phase 19, `completed_phases: 3`, percent 100, Current focus cleared or next-milestone, Shipped block for v1.20.0 after release (or "ready to ship" until gh lands).

### ROADMAP (`.planning/ROADMAP.md`) — residual only

**Still stale (P8):**

| Loc | Quote |
|-----|-------|
| L5 Overview | `capability map schema 2 / map_version **1.19.1** / 644 entries / 32 clusters` |
| L20–22 Next | `## Next` / `v1.20.0: FUT-05 ... Phases 19-21 below.` (still "next", not shipped) |
| L34 phase list | `- [ ] **Phase 21: CONTRACT rewrite + release surfaces** - Refresh path names the generator; residual closed; 1.20.0 surfaces, CHANGELOG, tag, GitHub Release` |

**Already updated by P3 (do not redo product ticks):**

| Loc | Live state |
|-----|------------|
| L87–93 Plans | `**Plans:** 2/2 plans complete`; both `21-01` / `21-02` `[x]` |
| L103 progress row | `\| 21. CONTRACT rewrite + release surfaces \| 2/2 \| Executed \| - \|` |
| L105 note | `Phase 21 product gates PASS; impl_review re-gated 2026-09-14. Phase close (gap_analysis, verify, milestone ledger): P8.` |
| L115–117 coverage | MAP-21-05 / REL-21-01 Complete; REL-21-02 `Complete (gh release: P8)` |

P8 overview/phase-list work: bump overview `map_version` to **1.20.0**, tick Phase 21 list checkbox, rewrite Next/shipped narrative once release lands (or mark milestone complete pending remote release with an honest note).

### REQUIREMENTS (`.planning/REQUIREMENTS.md`) — P3 done

Do **not** re-open:

```
- [x] **MAP-21-05**: ... residual ... committed note-override file, which the generator requires (fails closed if missing)
- [x] **REL-21-01**: ...
- [x] **REL-21-02**: ... (tag v1.20.0 on ffe385a; GitHub Release: P8 /gsd-ship)
```

Coverage table already Complete / Complete (gh release: P8). After GitHub Release exists, optional one-line clear of the P8 tail on REL-21-02.

### MILESTONES (`.planning/MILESTONES.md`) — missing v1.20.0

Shipped-entry shape (v1.17–v1.19.1 pattern):

1. Heading: `## vX.Y.Z (shipped YYYY-MM-DD)` (v1.19.1 also has a duplicate top card `## v1.19.1 v1.19.1 (Shipped: ...)` — prefer the cleaner v1.17/v1.18/v1.19.0 form).
2. One paragraph: what shipped, catalog freeze, map_version, honest non-scope.
3. Bullets: **Release commit**, **Annotated tag**, **GitHub Release** URL, **Deferred** leftovers.

v1.20.0 entry needs (facts on disk today):

| Field | Value now | Notes |
|-------|-----------|-------|
| Theme | FUT-05 byte-stable capability-map generator | phases 19–21 |
| Catalog | 63 / 65 (+2 signposts) | frozen; no new packs |
| Map | schema 2, map_version 1.20.0, 644 entries, 32 clusters | generator + mandatory note-overrides residual |
| Product tip for tag | `ffe385a` | CR-01 website YAML align + check_release 4a |
| Annotated tag | `v1.20.0` local | not on origin yet |
| GitHub Release | absent | fill URL after `gh release create` |
| HEAD after tag | `5b2183c` | CI/link-policy/signpost/WR harden; **not** in tag |
| Still deferred | FUT-04, AAF, IO-05/06, se-agents, DoDM 5000.102 | same as STATE deferred table |

Do not claim the 15 post-tag commits are inside the annotated release unless the human retags (out of default scope).

### GAP.md (`.planning/GAP.md`) — full file stale (b-08)

Entire file today:

```
Follow-up: Finish FUT-05 byte-stable capability-map generator

OBJ-1. v1.19.1 shipped only the mechanical map gate plus CONTRACT §8 residual. The live catalogue still lacks a byte-stable capability-map generator. Close that residual so map_version, schema, and release checks stay CI-validated without inventing packs or touching uncleared sources.
```

Rewrite shape (recommended):

1. **Close** FUT-05 / OBJ-1 as done in v1.20.0 (generator, rules, note-overrides, CONTRACT §4/§8, map_version 1.20.0, local tag).
2. **Residual human input**: mandatory 644-row note-overrides only (not optional).
3. **Carry forward** still-deferred sources/packs (FUT-04, AAF, IO-05/06, se-agents, DoDM) — pointer to STATE deferred table, not a fake empty GAP.
4. **Optional**: note post-1.20.0 drain work (CI parity, signpost validate_pack, WR-01..03) lives in CHANGELOG `[Unreleased]` / later patch, not as open FUT-05.

### Phase master_flow (`.planning/phases/21-contract-rewrite-release-surfaces/master_flow_state.json`)

**Post-P3 live state:**

| Field | Value |
|-------|-------|
| `current_gate` | `"gap_analysis"` (L9) |
| `completed` | through `security_audit` incl. `impl_review`, `code_review`, `integration_check` (L10–19) |
| `blocked_by` | `null` |
| `verdicts.impl_review` | `passed_with_notes:regate_cr01_wr01_wr02_wr03_closed` |
| `verdicts` gap/verify | **absent** |
| `regate_attempts.impl_review` | `2` |
| `updated_at` | `2026-09-15T02:10:53.000Z` |
| `config_snapshot.enable_gap_analysis` / `enable_verify` | `true` / `true` |
| `enable_complete` / `enable_milestone_audit` / `enable_doc_check` | `false` |
| Artifacts on disk | no `21-GAP_ANALYSIS.md`, no `21-VERIFICATION.md` |

**Phase 19/20 completed shape (mirror target if executing):**

| Field | 19/20 value |
|-------|-------------|
| `completed` | includes `gap_analysis`, `verify` after security_audit |
| `verdicts.gap_analysis` / `verify` | `"passed"` |
| `artifacts.gap_analysis` / `verify` | `19|20-GAP_ANALYSIS.md`, `19|20-VERIFICATION.md` |
| `current_gate` | `"doc_check"` (next disabled gate; not a lie about work remaining) |
| `skipped` | includes `doc_check`, `milestone_audit`, `complete`, `retrospective` |

### Root pointer (`.planning/master_flow_state.json`)

```
active_phase: 21
active_phase_dir: .planning/phases/21-contract-rewrite-release-surfaces
active_state: .../master_flow_state.json
lock: { phase: 21, session_hint: master-flow, updated_at: 2026-08-27T19:49:22.838Z }
```

Phase-complete posture: clear or advance root pointer once phase 21 is honestly complete (no open phase → milestone ship / new-milestone path per gsd-master-flow "Not this skill" note).

### PROJECT.md (optional adjacency)

`## Current State` still **Shipped: v1.19.1** and **Current Milestone: v1.20.0** in progress. Not listed as hard P8 must, but an honest milestone close usually flips this with MILESTONES/STATE. Prefer include if touching the same ledger sweep.

## What P3 already did (do-not-redo)

From packages.md P3 **outcome** (2026-09-14) and live files:

| Done | Evidence | P8 action |
|------|----------|-----------|
| Re-gate 21-IMPL_REVIEW | PASS_WITH_NOTES; CR-01/WR-01/02/03 CLOSED | Do not rewrite unless product regresses |
| master_flow review wave | `impl_review`…`security_audit` in `completed`; `blocked_by` null; `regate_attempts.impl_review` 2; `current_gate` advanced to `gap_analysis` | Do not revert to impl_review |
| Fresh product probes | check_release PASS @ HEAD, map 644, rules, generator `--check`, tag peel `ffe385a` | Re-run only as verify evidence if executing verify |
| REQUIREMENTS ticks + MAP-21-05 wording | all three `[x]`; optional→required overrides | Do not untick |
| ROADMAP plan boxes + progress 2/2 Executed + coverage | L87–117 | Do not reset to 0/2 |
| GitHub Release deferred note on REL-21-02 | `Complete (gh release: P8)` | Clear only after real release |

**P8 still owns** (narrowed): STATE full close, ROADMAP overview + Phase 21 list checkbox + Next/shipped narrative, MILESTONES v1.20.0 entry, GAP.md b-08 refresh, gap_analysis + verify (execute or documented waive), root pointer / phase-complete posture, payoff publish (`git push` + tag push + `gh release create`), optional PROJECT.md + REL-21-02 tail clear after release.

packages.md P8 **in_scope** still says "tick MAP-21-05 / REL-21-01 / REL-21-02" — that prose is **stale relative to P3 outcome**. Spec/plan must follow live REQUIREMENTS, not re-tick.

## Gap / verify honesty (design)

### Facts

- Config still enables gap_analysis and verify for phase 21.
- Phases 19 and 20 **authored and passed** both gates (artifacts + master_flow).
- Phase 21 has review artifacts through security_audit; gap/verify files **missing**.
- ROADMAP L105 explicitly assigns phase close (gap_analysis, verify, milestone ledger) to **P8**.
- Stock `gsd-ship` preflight reads `verification.status` and **only `passed` may ship**; missing verification → `PHASE_VERIFICATION_INCOMPLETE`.
- gsd-master-flow: REQUIREMENTS closed via verify → `phase.complete`; host runs phase.complete after verify passed. `enable_complete` is false here (same as 19/20 — they skipped complete and parked on doc_check).

### Options

| Option | What it means | When honest |
|--------|---------------|-------------|
| **A. Execute gap + verify** (recommended default) | Author `21-GAP_ANALYSIS.md` + `21-VERIFICATION.md` from live evidence (P3 probes + CONTRACT/tag/CHANGELOG); set verdicts `passed` / `passed_with_notes`; append both to `completed`; advance `current_gate` to `doc_check` like 19/20 | Matches prior phases, satisfies stock ship verify gate, matches ROADMAP P8 note |
| **B. Waive with rationale** | Record waiver in master_flow notes + a short phase note: product gates and reviews already closed; milestone ledger is the remaining work; gap/verify skipped because … | Only if stock ship is **not** used and waive text is explicit; weaker vs 19/20 precedent; still leaves `enable_gap_analysis/verify: true` lying unless config flipped |
| **C. Hybrid** | Light gap (review inventory + requirement cross-check, no new product work) + verify that re-runs the four gates and records tag/release-not-on-remote as known open publish tail | Same cost as A with clearer "release remote still open" truth in VERIFICATION |

**Recommendation for spec:** Option A/C. Do not mark phase complete while `current_gate` stays `gap_analysis` with no artifact. Do not invent `passed` without files. Waive only if the plan explicitly abandons stock ship preflight and documents why 19/20 precedent does not apply.

**phase.complete / milestone:** 19/20 left `complete` and `milestone_audit` skipped. P8 should mirror that for the **phase** file after verify, then do **milestone** narrative in STATE/ROADMAP/MILESTONES/GAP (and optional PROJECT) rather than enabling milestone_audit unless the human asks for `/gsd-audit-milestone`.

## `/gsd-ship` procedure summary

### Skill locations

| Path | Role |
|------|------|
| `~/.agents/skills/gsd-ship/SKILL.md` | Entry: execute `ship.md` end-to-end |
| `~/.claude/skills/gsd-ship/SKILL.md` | Same skill present |
| `~/.zcode/skills/gsd-ship/SKILL.md` | **Absent** |
| `~/.codex/gsd-core/workflows/ship.md` | Real procedure |
| `~/.claude/gsd-core/workflows/ship.md` | Same family |

### Stock workflow steps (ship.md)

1. **initialize** — phase-op, branching strategy, base branch.
2. **preflight_checks**
   - `verification.status` must be **`passed`** (else block).
   - Clean working tree (`git status --short`).
   - Prefer feature branch (warn if on base).
   - `origin` remote present.
   - `gh` authenticated.
   - Optional capability `ship:pre` gates (security threats_open==0, broken-windows open_count==0, …).
3. **push_branch** — `git push origin <branch>`.
4. **generate_pr_body** — from ROADMAP / VERIFICATION / SUMMARYs / REQUIREMENTS / STATE.
5. **create_pr** — `gh pr create --base <base>`.
6. **optional_review** — external or manual.
7. **track_shipping** — STATE "Phase N shipped — PR #…"; optional commit_docs push.
8. **ship:post** hooks (best-effort).
9. **report** — PR URL; next `$gsd-complete-milestone` if last phase.

**Stock success criteria:** verification passed, branch pushed, **PR created**, STATE shipping note. **No** `git tag`, **no** `gh release create`, **no** CHANGELOG fold.

### What this repo means by `/gsd-ship` (21-02)

From `21-02-PLAN.md` / `21-02-SUMMARY.md`:

- Annotated tag `v1.20.0` created in-phase; **do not recreate lightweight**.
- **Do not push tags from executor**; ship owns publish.
- `/gsd-ship`: **create GitHub Release for v1.20.0**.
- Analog prior release: v1.19.1 tag + GitHub Release from release content commit.

### Conflict and recommended resolution

| | Stock gsd-ship | Repo Phase 21 ship |
|--|----------------|--------------------|
| Primary artifact | Pull request | GitHub Release on tag `v1.20.0` |
| Branch expectation | Feature branch → PR into main | Already on `main`, 29 commits ahead of origin |
| Tag | Not handled | Must exist remote for clean `gh release create v1.20.0` |
| Verify gate | Hard require VERIFICATION passed | Still valuable; run gap/verify first |

**Spec should prescribe a release publish procedure** (the payoff), not a blind `Skill(gsd-ship)` that opens a PR for all of main:

1. Finish ledger + gap/verify (or documented waive).
2. Ensure clean tree for publish paths (superpowers drafts either committed, ignored, or left untracked by policy).
3. **Human-gated outward publish** (see below):
   - `git push origin main` (29 commits; includes tag tip `ffe385a` and 15 post-tag commits).
   - `git push origin v1.20.0` (annotated tag only; peel stays `ffe385a`).
   - `gh release create v1.20.0 --title "…" --notes-file <from CHANGELOG [1.20.0] only>` (or `--generate-notes` constrained to tag range).
4. Record release URL in MILESTONES / STATE / ROADMAP / optional REL-21-02 tail clear.
5. Optionally run stock gsd-ship **only** if a real PR workflow is desired; default for this package is **release create**, not PR.

`gsd-complete-milestone` skill text mentions tagging a version; this milestone **already has** the annotated tag. Do not mint a second tag. Complete-milestone archive of roadmap/requirements is optional follow-on, not a substitute for the GitHub Release.

## Git / tag / remote posture

| Fact | Value |
|------|-------|
| HEAD | `5b2183c` `test: add signpost-unmarked index demo to ci-gate probe` |
| origin/main | `55ef575` `chore: stop shipping GSD planning and internal drafts` |
| Ahead of origin | **29** commits (`git rev-list --count origin/main..HEAD`) |
| Behind origin | 0 |
| Tag `v1.20.0` | annotated; message `chore: annotate v1.20.0 generator refresh path` |
| Tag peel | `ffe385a` (`fix: align website product YAMLs to 1.20.0 (CR-01)`) |
| Commits origin→tag | **14** |
| Commits tag→HEAD | **15** (CI link-policy, CI gate coverage, signpost validate_pack, WR-01..03, TESTING/CHANGELOG notes) |
| Tag on origin | **no** |
| `gh release v1.20.0` | **not found** |
| Remote | `origin` → `https://github.com/jgsystemsconsulting/jgs-se-knowledge-packs.git` |
| Dirty | `?? docs/superpowers/` only |

**Push before release:** Yes. `gh release create v1.20.0` needs the tag reachable on the remote (or explicit upload from local tag after commits exist remotely). Pushing **main** and pushing **tag `v1.20.0`** are required publish steps, independent of whether the agent or the human runs them. The 29 commits include both the v1.20.0 product history and post-tag drain work; that is correct for `main`, and does **not** move the tag.

**Do not** force-move `v1.20.0` to HEAD to "include CI" unless the human explicitly wants a retag; CR-01 fix commit is the agreed product freeze.

## CHANGELOG `[Unreleased]` question

**Facts:**

- `CHANGELOG.md` (repo root) has `## [Unreleased]` **above** `## [1.20.0]: 2026-08-27`.
- `[1.20.0]` body = generator, note-overrides, classification rules, CONTRACT, deferred list (Phase 19–21 product story).
- `[Unreleased]` body = P4/P5 CI twin steps, overlap-whitelist data file, link-policy hosts file/tests, PASS banner sha stamp, CI host parity — commits **after** `ffe385a` (e.g. `e9c1d12`, `a42e3d9`, and tooling commits in tag..HEAD).
- Tag does **not** contain Unreleased commits.

**Decision (recommend default in spec; human may override):**

| Choice | Effect |
|--------|--------|
| **Keep `[Unreleased]` separate** (recommended) | Release notes for GitHub Release = `[1.20.0]` section only. Honest: tag content ≠ later CI. Unreleased stays for next patch/minor. |
| Fold Unreleased into `[1.20.0]` | Lies about what `v1.20.0` tagged unless tag moves to HEAD. Out of scope without retag. |
| Cut a `1.20.1` now | New version surfaces + new tag; expands package beyond ledger close. YAGNI unless human asks. |

Record in plan: **do not fold**; ship notes from `[1.20.0]`; leave Unreleased for post-release mainline.

## Design considerations (for spec/plan)

1. **Gap/verify:** Default execute (A/C). Waive only with written rationale and acceptance that stock gsd-ship preflight will fail.
2. **Ship runner:** Treat packages.md "run /gsd-ship" as **payoff publish** (push main, push annotated tag, `gh release create`), not stock PR ship. Mention stock skill mismatch so the implementer does not open a junk PR.
3. **Who pushes 29 commits:** Outward-facing. Spec must surface a **human decision**: agent runs push+release with user approval, or user runs the three publish commands after ledger is local-ready. Default recommendation: prepare everything local; run publish only with explicit approval (or hand the exact command block to the user).
4. **MILESTONES wording:** Generator residual closed; catalog 63/65; map_version 1.20.0; release commit `ffe385a`; tag `v1.20.0`; GH URL filled post-create; deferred list unchanged; optional one line that main continued with CI/tooling after the tag (Unreleased).
5. **GAP.md:** Close FUT-05; keep deferred non-FUT-05 items; no empty file that pretends the backlog is gone.
6. **STATE:** Flip off Phase 20 resume; mark phase 21/milestone complete or shipping; add v1.20.0 shipped facts after release.
7. **ROADMAP:** Overview 1.20.0; tick Phase 21 `[x]`; Next becomes empty or next-milestone placeholder after ship.
8. **Clean tree for publish:** `docs/superpowers/` untracked is fine to leave local (planning-adjacent drafts); do not `git add -A`. If ship preflight demands clean tree, stash or leave and use manual gh path.
9. **REL-21-02:** Already ticked with P8 tail. After successful `gh release create`, amend note to the release URL (checkbox stays `[x]`).

## Exact P8 edit targets

| Target | Path | Change |
|--------|------|--------|
| STATE | `.planning/STATE.md` | Close planning/Phase 20 stop; 3/3 phases; resume/shipped narrative |
| ROADMAP overview + list + Next | `.planning/ROADMAP.md` L5, L20–22, L34 | 1.20.0 truth; Phase 21 `[x]`; shipped/next honesty |
| MILESTONES | `.planning/MILESTONES.md` | New v1.20.0 shipped section |
| GAP | `.planning/GAP.md` | FUT-05 closed rewrite (b-08) |
| gap + verify artifacts | `21-GAP_ANALYSIS.md`, `21-VERIFICATION.md` | Author (default) |
| phase master_flow | phase `master_flow_state.json` | Record gap/verify; advance gate off `gap_analysis` |
| root pointer | `.planning/master_flow_state.json` | Clear/advance after phase complete |
| PROJECT (optional) | `.planning/PROJECT.md` | Shipped v1.20.0 / clear current milestone |
| Publish | git + gh | push main, push tag, `gh release create` |
| REL-21-02 note (after) | REQUIREMENTS / ROADMAP coverage | Replace P8 tail with release URL |

## Constraints

1. No product code / version trio / packs / CI edits (P8 out_scope).
2. No retag/force-push of `v1.20.0` unless human orders it.
3. No folding `[Unreleased]` into `[1.20.0]` without retag decision.
4. No re-tick of REQUIREMENTS already closed by P3.
5. No silent `impl_review` regression.
6. `.planning/` stays gitignored; do not stage it.
7. Do not run stock `gh pr create` for 29-commit main as a substitute for the GitHub Release.
8. Push/release is outward-facing; require explicit approval or handoff commands.

## Synthesis

SC1–SC5 covered. After P3, product and requirement ticks are honest; the **shared ledger** still sells Phase 20 planning and map 1.19.1, GAP still open-codes FUT-05, MILESTONES lacks v1.20.0, and master_flow sits on enabled-but-empty gap_analysis. Stock `/gsd-ship` is a PR bridge that will not create the GitHub Release this package promised; the payoff is push main + push annotated tag `v1.20.0` + `gh release create` with notes from `[1.20.0]` only, after gap/verify (or an explicit waive) and STATE/ROADMAP/MILESTONES/GAP close. One human decision remains: who runs the outward 29-commit + tag publish.

## Evidence index

| Loc | Kind |
|-----|------|
| `.planning/STATE.md` | stale planning / Phase 20 stop |
| `.planning/ROADMAP.md` L5, L22, L34 vs L87–117 | residual vs P3-done |
| `.planning/REQUIREMENTS.md` L18–23, L54–56 | P3 ticks |
| `.planning/MILESTONES.md` | no v1.20.0 entry |
| `.planning/GAP.md` | stale FUT-05 follow-up |
| `.planning/PROJECT.md` Current State | still v1.19.1 shipped |
| phase 21 `master_flow_state.json` | gate gap_analysis; no gap/verify verdicts |
| `.planning/master_flow_state.json` | root active_phase 21 |
| phase 19/20 `*-GAP_ANALYSIS.md`, `*-VERIFICATION.md`, master_flow | complete-phase precedent |
| `21-02-PLAN.md` / `21-02-SUMMARY.md` handoff | `/gsd-ship` = gh release |
| `~/.agents/skills/gsd-ship/SKILL.md` + `~/.codex/gsd-core/workflows/ship.md` | stock PR ship |
| `CHANGELOG.md` Unreleased + 1.20.0 | post-tag vs tagged notes |
| git status / log / tag / ls-remote / gh release | publish posture |
| `docs/superpowers/packages/2026-09-14-jgs-se-knowledge-packs-packages.md` P3/P8/X1 | scope |
| format refs: `2026-09-14-close-phase21-ship-surface-context.md` (+ log) | structure mirror |
