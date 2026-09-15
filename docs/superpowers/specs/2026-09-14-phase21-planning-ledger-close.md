# Phase 21 planning-ledger close and v1.20.0 ship handoff

Date: 2026-09-14. Package: P8 (FINAL package, size M), promoted backlog id b-08.
Scope source: packages.md P8 as narrowed by the P3 outcome (2026-09-14). Where
packages.md in_scope prose still lists REQUIREMENTS ticks, the P3 outcome wins;
this spec does not re-tick anything P3 closed.

## Research

research: skipped (in-repo GSD ledger close plus a documented release-command handoff; no external APIs, libraries, or version-sensitive choices beyond the repo's own release procedure)

## Codebase context

This is a GSD-managed content repo. The milestone v1.20.0 (FUT-05 byte-stable
capability-map generator) ran phases 19 to 21. Phase 21 product work is done:
both plans complete, four review gates recorded, impl_review re-gated by P3 on
2026-09-14, REQUIREMENTS MAP-21-05 / REL-21-01 / REL-21-02 all ticked, ROADMAP
plan boxes and coverage updated by P3. What remains is the shared planning
ledger and the payoff publish.

Facts pinned live on 2026-09-14 (re-verified this session):

| Fact | Value |
|------|-------|
| Branch / HEAD | `main` @ `5b2183c` |
| Annotated tag | `v1.20.0`, type `tag`, peel `ffe385a` (`fix: align website product YAMLs to 1.20.0 (CR-01)`) |
| Tag message | `chore: annotate v1.20.0 generator refresh path` |
| origin/main | `55ef575`, 29 commits behind HEAD (14 origin-to-tag, 15 tag-to-HEAD), 0 behind |
| Tag on remote | absent; `gh release view v1.20.0` not found |
| Working tree | clean except untracked `docs/superpowers/` (this drain's drafts) |
| `.planning/` | gitignored (commit `55ef575` policy); all ledger edits are local-only |

Because every file this package edits is either gitignored (`.planning/`) or
untracked (`docs/superpowers/`), the publish pushes exactly the 29 existing
commits plus the tag. Nothing in this package creates a commit.

Phase 19 and 20 set the completion precedent: both authored `GAP_ANALYSIS.md`
and `VERIFICATION.md`, recorded verdicts `passed`, appended `gap_analysis` and
`verify` to `completed`, and parked `current_gate` at `doc_check` (the next
disabled gate) with `doc_check`, `milestone_audit`, `complete`, and
`retrospective` in `skipped`. Phase 21 must match that shape or document why
not.

Stock `/gsd-ship` (`~/.codex/gsd-core/workflows/ship.md`) is a PR bridge:
verify gate, push branch, `gh pr create`. It never touches tags or
`gh release create`. This repo's own handoff (`21-02-PLAN.md`,
`21-02-SUMMARY.md`) defines `/gsd-ship` as "create the GitHub Release for the
existing annotated tag v1.20.0". The repo meaning wins; running stock ship
would open a junk PR for all of main.

## Problem

After P3, the product surfaces tell the truth about v1.20.0 and the shared
ledger does not. Every stale statement below must be fixed or the next reader
(the user, a future agent, `/gsd:resume-work`) resumes a milestone that already
ended.

| Surface | Stale statement today | Required truth |
|---------|----------------------|----------------|
| `.planning/STATE.md` | `status: planning`; `stopped_at: Phase 20 complete, ready to plan Phase 21`; `completed_phases: 2`, `percent: 67`; body bar 33%; "Current focus: Phase 19"; Resume `/gsd:plan-phase 19`; Shipped section ends at v1.19.1 | Milestone closed; 3/3 phases; ship posture; v1.20.0 shipped facts after release |
| `.planning/ROADMAP.md` L5 | overview `map_version **1.19.1**` | `1.20.0` (63/65, 644 entries, 32 clusters unchanged) |
| `.planning/ROADMAP.md` L20-22 | `## Next` frames v1.20.0 as upcoming | shipped or ship-handoff framing |
| `.planning/ROADMAP.md` L34 | `- [ ] **Phase 21 ...` | `- [x]` with completion date |
| `.planning/ROADMAP.md` L103 | Phase 21 row `2/2 / Executed / -` | `Complete` with date; L105 note updated |
| `.planning/MILESTONES.md` | no v1.20.0 entry | v1.20.0 entry in the v1.17-to-v1.19.1 shipped shape |
| `.planning/GAP.md` | whole file: "Follow-up: Finish FUT-05 ..." | FUT-05 closed; carried deferrals kept |
| phase 21 `master_flow_state.json` | `current_gate: gap_analysis` with no gap/verify verdicts or artifacts while `enable_gap_analysis`/`enable_verify` are `true` | gates executed and recorded (this spec, Decision 1) |
| `.planning/master_flow_state.json` | root pointer `active_phase: 21` locked | pointer cleared once phase 21 is complete |
| `.planning/PROJECT.md` | Current State "Shipped: v1.19.1"; Current Milestone v1.20.0 in progress | v1.20.0 shipped (after release) |
| `CHANGELOG.md` | `[Unreleased]` sits above `[1.20.0]`; Unreleased content is post-tag CI work | release notes built from `[1.20.0]` only (Decision 3) |

Do-not-redo list (P3 already closed, verified in live files): 21-IMPL_REVIEW
regate, master_flow review wave through `security_audit`, REQUIREMENTS ticks
and MAP-21-05 wording, ROADMAP plan boxes, progress 2/2, coverage table,
REL-21-02 "Complete (gh release: P8)" tail (cleared only after a real release
exists).

## Goals

1. Phase 21 reaches the same completion posture as phases 19 and 20, honestly:
   gap_analysis and verify executed with artifacts, or a documented waiver.
   This spec executes them (Decision 1).
2. Every shared ledger statement matches reality at all times: no premature
   "shipped" claims, no contradiction left between any two planning surfaces.
3. The v1.20.0 GitHub Release exists as the payoff, published only after an
   explicit user go, with the exact command sequence recorded in advance.
4. Post-release URL backfills land so no surface still says "pending".

## Non-goals

- Product code, version trio, packs, CI edits (P1/P4/P5/P6/P7 done; P8 out of scope).
- Re-gating, re-running the six P3 product probes, rewriting 21-IMPL_REVIEW.
- Retagging or moving `v1.20.0` off `ffe385a`; no force-push.
- Folding CHANGELOG `[Unreleased]` into `[1.20.0]`; cutting a `1.20.1`.
- Running stock `/gsd-ship` as written (it would create a PR, not a release).
- Enabling `milestone_audit` or `complete` in phase 21 config; the milestone
  narrative lands in STATE/ROADMAP/MILESTONES/GAP, mirroring 19/20 which
  skipped those gates.
- Any new commit. All edits are to gitignored or untracked paths.

## Design

### Decision 1: Execute gap_analysis and verify for phase 21

Chosen: execute both gates and author the artifacts. Waiver rejected.

Rationale. The phase config still enables both gates, phases 19 and 20 passed
them, ROADMAP L105 explicitly assigns "gap_analysis, verify, milestone ledger"
to this package, and stock ship preflight treats a missing verification as
`PHASE_VERIFICATION_INCOMPLETE`. A waiver would leave `enable_gap_analysis` /
`enable_verify: true` claiming work that was skipped, break the 19/20 precedent
for no compensating gain, and save almost nothing, because neither gate
requires new product work here.

What execution means when the product is already reviewed:

- `21-GAP_ANALYSIS.md` is a review inventory plus requirement cross-check, not
  a new hunt. Inputs: the four existing review artifacts
  (21-IMPL_REVIEW, 21-CODE_REVIEW, 21-INTEGRATION_CHECK, 21-SECURITY_AUDIT)
  and the recorded verdicts in master_flow. Frontmatter and section shape
  mirror `19-GAP_ANALYSIS.md` (phase, analyzed date, requirement scope
  MAP-21-05 + REL-21-01 + REL-21-02, review table, criterion cross-check,
  residuals, rejected-as-non-gaps, verdict rationale). Verdict: CLOSED, with
  two named non-gaps stated explicitly: the absent GitHub Release is a
  ship-handoff item owned by Decision 4, not a phase gap; the post-tag CI and
  tooling commits in CHANGELOG `[Unreleased]` are out of phase scope.
- `21-VERIFICATION.md` re-runs the observable truths live, SUMMARY claims not
  trusted. Frontmatter `status: passed` (this is what downstream tooling
  reads), matching the 19/20 shape. Behavioral checks, all cheap and local:
  `python tooling/check_release.py` exit 0 at HEAD;
  `python tooling/generate_capability_map.py --generated-on 2026-08-27 --check`
  exit 0; tag peel equals `ffe385a` and type is `tag`; version trio and
  map_version 1.20.0 agree; catalog 63 / dirs 65; the three ROADMAP success
  criteria for phase 21 each mapped to evidence. The VERIFICATION records one
  known open tail in its notes: the GitHub Release is pending the user-gated
  publish (Decision 4) and is not a phase criterion failure, because ROADMAP
  SC4 says "when the product surface is ready" and REL-21-02 already scopes
  the release to this package's ship step.
- master_flow end state for phase 21 (mirror of 19/20):

| Field | End value |
|-------|-----------|
| `completed` | existing nine entries plus `gap_analysis`, `verify` |
| `verdicts.gap_analysis` | `passed` |
| `verdicts.verify` | `passed_with_notes:gh_release_pending_user_go` |
| `artifacts.gap_analysis` | path to `21-GAP_ANALYSIS.md` |
| `artifacts.verify` | path to `21-VERIFICATION.md` |
| `current_gate` | `doc_check` (parked exactly like 19/20; `doc_check` stays in `skipped` since it is disabled) |
| `skipped`, `enable_complete: false`, `enable_milestone_audit: false` | unchanged |
| `updated_at`, `notes` | bumped; notes record the close and the pending publish |

- Root pointer (`.planning/master_flow_state.json`): cleared. `active_phase`,
  `active_phase_dir`, `active_state`, and `lock` become `null`; `updated_at`
  bumped; `notes` records "v1.20.0 milestone closed 2026-09-14; GitHub Release
  pending user go". No gsd-core script reads this pointer (verified: zero
  references to `active_phase` or `master_flow_state` under
  `~/.codex/gsd-core/bin|workflows|references|templates`), so null is safe; the
  pointer is consumed by agent-side skills only. If a later `/gsd:new-milestone`
  wants a different shape, that run rewrites the pointer itself.

### Decision 2: Ledger edit inventory, in two waves

The publish needs an explicit user go (Decision 4), so the ledger moves in two
waves to keep every statement true at every moment. Wave 1 says "closed, ship
pending". Wave 2, only after `gh release create` succeeds, says "shipped" and
backfills URLs. If the user answers no-go, wave 2 never runs and the package
ends in the wave-1 posture, which is honest.

Wave 1 (local truth, before any publish):

| File | Edit |
|------|------|
| STATE frontmatter | `status: shipping`; `stopped_at: v1.20.0 ledger closed, GitHub Release pending user go`; `last_updated` / `last_activity` / `last_activity_desc` bumped; `progress`: `completed_phases: 3`, `total_plans: 5`, `completed_plans: 5`, `percent: 100` |
| STATE body | Current focus: "v1.20.0 milestone closed; publish handoff pending user go". Current Position: Plan "21-01, 21-02 complete", Status "Phase complete (gap_analysis + verify passed 2026-09-14)", Last activity dated. Progress bar full 100%. Deferred note line becomes "FUT-05 generator residual closed in v1.20.0." Session Continuity: "Stopped at: v1.20.0 ledger closed, ship handoff pending user go"; Resume: `/gsd:new-milestone` (no open phase); delete the stale `/gsd:plan-phase 19` line |
| PROJECT.md | Current Milestone section: v1.20.0 milestone closed 2026-09-14, GitHub Release pending user go (ship pending posture, no shipped URL yet); Shipped list unchanged until Wave 2 backfills the URL |
| ROADMAP L5 | overview `map_version` 1.19.1 to **1.20.0**; counts unchanged |
| ROADMAP L20-22 | Next becomes "v1.20.0 executed; ledger closed 2026-09-14; GitHub Release in ship handoff (user-gated)." |
| ROADMAP L34 | `- [x] **Phase 21: CONTRACT rewrite + release surfaces** - ... (completed 2026-09-14)` |
| ROADMAP L103, L105 | Phase 21 row: `2/2`, `Complete`, `2026-09-14`; note line becomes "Phase 21 closed 2026-09-14 (gap_analysis + verify passed). GitHub Release: ship handoff." |
| GAP.md | full rewrite (target below) |
| gap/verify artifacts + phase master_flow + root pointer | per Decision 1 |

Wave 2 (only after the release exists):

| File | Edit |
|------|------|
| STATE frontmatter | `status: complete`; `stopped_at: v1.20.0 shipped (<release URL>)` |
| STATE body | Current focus and Current Position lines from Wave 1 ("publish handoff pending user go", "ship handoff pending user go") rewritten to the shipped wording of this wave — no line may still say "pending user go" |
| STATE Shipped | heading becomes `## Shipped (v1.20.0)`; new v1.20.0 block first (release commit `ffe385a`, tag `v1.20.0`, GitHub Release URL, basis: catalog 63 / dirs 65, map_version 1.20.0, 644 entries, 32 clusters, gates: release check and generator replay PASS; audit: none, milestone_audit disabled by config); v1.19.1 block stays below |
| STATE Session Continuity | "Stopped at: v1.20.0 shipped <URL>" |
| ROADMAP | shipped-milestones list gains `- [x] **v1.20.0: FUT-05 byte-stable capability-map generator** (phases 19-21)` with release link and "archive: none (complete-milestone not run; ledger closed in place)"; a short v1.20.0 summary paragraph in the v1.19.1-summary shape; Next becomes "None selected. v1.20.0 shipped 2026-09-14. Backlog candidates above remain."; coverage REL-21-02 tail "Complete (gh release: P8)" becomes "Complete" |
| MILESTONES.md | new top entry `## v1.20.0 (shipped 2026-09-14)` in the clean v1.17/v1.18/v1.19.0 shape (not the duplicated v1.19.1 card shape): theme paragraph (generator, mandatory 644-row note-overrides, classification rules, CONTRACT section 4 names the generator and section 8 residual is note overrides only, map_version 1.20.0 / schema 2 / 644 entries / 32 clusters, catalog frozen 63/65, no new packs, phases 19-21 with 5 plans) then bullets: Release commit `ffe385a` with subject; Annotated tag `v1.20.0` with message; GitHub Release URL; Still deferred: FUT-04 Army CBA, AAF Product Support + Software, IO-05/06, se-agents sibling-repo refresh, DoDM 5000.102 UNVERIFIED; one honesty line: main continued after the tag with CI parity, link-policy, signpost validate_pack, and WR hardening, that work sits in CHANGELOG `[Unreleased]` and is not part of the tagged release |
| PROJECT.md | Current State: Shipped v1.20.0 (date, one-line theme), Prior v1.19.1; Current Milestone section rewritten — the wave-1 "closed, GitHub Release pending user go" lines are replaced with shipped + release URL wording (no "pending user go" line survives anywhere); `Last updated` line bumped |
| REQUIREMENTS.md | REL-21-02 note: drop the "(tag v1.20.0 on ffe385a; GitHub Release: P8 /gsd-ship)" tail, replace with the release URL. Coverage row "Complete (gh release: P8)" becomes "Complete". Checkbox stays `[x]`. No other tick touched |
| phase master_flow + root pointer notes | the Decision-1 "GitHub Release pending user go" notes are updated to shipped with the release URL (fields that P3 left honestly open stay structurally as recorded; only the pending-release wording is refreshed) |

GAP.md rewrite target (whole file, compact):

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

### Decision 3: CHANGELOG [Unreleased] handling

Keep `[Unreleased]` separate. The GitHub Release notes are built from the
`[1.20.0]` section only, because the tag points at `ffe385a` and everything in
`[Unreleased]` landed after it. Folding would claim tag content that the tag
does not contain. Cutting a `1.20.1` now would mint new surfaces and a new tag
for work this package did not touch; YAGNI.

Mechanics: write the notes file to
`docs/superpowers/release-notes/v1.20.0.md` (untracked directory, never
staged): a title line, the `[1.20.0]` section body verbatim, and a closing
line naming the deferred list. `CHANGELOG.md` itself is not edited in this
package; `[Unreleased]` stays as the next release's staging area.

### Decision 4: Ship handoff (the payoff publish)

This is not stock `/gsd-ship`. Stock ship would push a branch and open a PR;
main is 29 commits ahead of origin and the deliverable is a GitHub Release on
an existing annotated tag, per the 21-02 handoff. The spec keeps stock ship's
gate spirit (verification passed, clean tracked tree, `gh` authenticated,
remote present) and replaces the PR step with the release sequence.

The publish is outward-facing. It runs only after an explicit user go via
AskUserQuestion at execution time. The executor prepares and verifies
everything locally first, then presents the command block. The alternative
path, handing the block to the user to run themselves, is offered in the same
question.

Local ship-readiness checklist, all must hold before the go question:

```bash
git rev-list --count origin/main..HEAD          # record N (29 on 2026-09-14)
git rev-list --count HEAD..origin/main          # must be 0
git cat-file -t v1.20.0                         # must print: tag
git rev-parse --short v1.20.0^{commit}          # must print: ffe385a
git ls-remote --tags origin refs/tags/v1.20.0   # must be empty
gh release view v1.20.0                         # must fail: not found
gh auth status                                  # must succeed
git status --short                              # only untracked docs/superpowers/
git diff --cached --quiet                       # exit 0, nothing staged
python tooling/check_release.py                 # exit 0
python tooling/generate_capability_map.py --generated-on 2026-08-27 --check  # exit 0
```

Exact publish sequence, run in this order on user go:

```bash
git push origin main
git push origin v1.20.0
gh release create v1.20.0 \
  --title "v1.20.0: FUT-05 byte-stable capability-map generator" \
  --notes-file docs/superpowers/release-notes/v1.20.0.md
```

`main` first so the tag's commit is reachable, then the annotated tag (peel
stays `ffe385a`; pushing it cannot move it), then the release from the
`[1.20.0]`-only notes file. No `--generate-notes` (it would draft from the
wrong range). No `gh pr create` at all.

If any readiness check drifts at execution time (remote state changed, count
differs from N), stop and re-derive before asking; never push on stale counts.

No-go path: skip the three commands, leave the ledger in the wave-1 posture,
and end the package with a handoff note recording that the publish commands
await user execution. No shipped claim exists anywhere in that state.

### Decision 5: Verification

One runnable check per wave, executed as a single inline script or command
block in the plan (assert-based, no permanent tool, no new test files).

Wave 1 asserts:

- STATE: exactly one of `status: shipping`; zero matches for `status: planning`
  and `plan-phase 19`; `completed_phases: 3`; `total_plans: 5`;
  `completed_plans: 5`; `percent: 100`.
- PROJECT.md: Current Milestone says the v1.20.0 milestone is closed with the
  GitHub Release pending user go; the Shipped list still ends at v1.19.1 (no
  premature shipped URL).
- ROADMAP: line 5 contains `1.20.0` and not `1.19.1`; exactly one
  `- [x] **Phase 21`; zero `- [ ] **Phase 21`; progress row shows
  `Complete`; `1.19.1` appears only in shipped-history lines.
- GAP.md: zero matches for `Follow-up: Finish FUT-05`; contains `CLOSED`.
- Phase master_flow: JSON parses; `gap_analysis` and `verify` in `completed`;
  both verdicts start with `passed`; `current_gate == "doc_check"`; both
  artifact paths exist on disk.
- Root pointer: JSON parses; `active_phase is None`; `lock is None`.
- Product gates: `check_release.py` exit 0; generator `--check` exit 0.
- Tree: `git diff --cached --quiet` exit 0; `git status --short` shows no
  tracked modifications; tag still peels to `ffe385a`.

Publish-safety asserts (re-run immediately before the go question): the full
readiness checklist from Decision 4.

Wave 2 asserts:

- MILESTONES: exactly one `## v1.20.0 (shipped `; its GitHub Release URL equals
  `gh release view v1.20.0 --json url`.
- STATE and ROADMAP contain the release URL; zero matches for
  `gh release: P8` across `.planning/REQUIREMENTS.md` and `.planning/ROADMAP.md`.
- STATE: `status: complete`; zero matches for `shipping`.
- Cross-surface: zero matches for `pending user go` across `.planning/*.md`
  top-level ledger files (PROJECT, STATE, ROADMAP, REQUIREMENTS, GAP); the
  wave-1 ship-pending wording is fully replaced by shipped + release URL.
- Cross-surface contradiction sweep: zero matches for
  `ready to plan Phase 21` and `Phase 20 complete, ready` across
  `.planning/*.md` (top-level ledger only; milestone archives are history and
  excluded).
- map_version agreement: ROADMAP overview, `docs/capability-pack-map.json`,
  and RELEASE-INFO all say 1.20.0 (`check_release` already enforces the trio;
  the grep covers ROADMAP).
- Tag unchanged: peel still `ffe385a`; `git status --short` still shows no
  tracked modifications (wave 2 edits touched only ignored and untracked
  paths).

### Execution order

1. Author `21-GAP_ANALYSIS.md` and `21-VERIFICATION.md`; run the behavioral
   checks; record results.
2. Update phase 21 `master_flow_state.json` and clear the root pointer
   (Decision 1 end-state tables).
3. Wave 1 ledger edits: STATE, PROJECT.md, ROADMAP L5 / Next / L34 / L103-105,
   GAP.md.
4. Run wave-1 verification asserts; fix any failure before proceeding.
5. Run the publish-readiness checklist; write the release-notes file.
6. AskUserQuestion: present the three publish commands and the recorded commit
   counts; user picks go (agent runs), self-run (user runs the block), or no-go.
7. On go: run the three commands in order; confirm with
   `gh release view v1.20.0` and capture the URL. On self-run (user runs the
   publish block): wait for the user to report completion, verify with
   `gh release view v1.20.0` before capturing the URL; if the release does not
   exist yet, treat as handoff-stop (wave 1 posture holds) and record that the
   publish is still outstanding. Never backfill wave 2 without the release
   existing. On confirmed release: proceed to step 8.
8. Wave 2 backfills: STATE, ROADMAP (shipped list, summary, Next, coverage
   tail), MILESTONES entry, PROJECT.md, REQUIREMENTS REL-21-02 tail, phase
   master_flow/root-pointer pending-release notes.
9. Run wave-2 verification asserts; report the release URL and the final
   ledger state.

On no-go at step 6: skip steps 7-8, write the handoff note, re-run wave-1
asserts to confirm the ledger still tells the truth, and stop.

## Approach

Execute phase 21's enabled gap_analysis and verify gates with real artifacts
review-inventory and live-gate re-runs rather than waiving them, park the phase
at `doc_check` exactly like phases 19 and 20, and clear the root pointer. Close
the shared ledger in two honest waves: wave 1 moves STATE, PROJECT, ROADMAP,
and GAP.md
to a "closed, ship pending" posture with no shipped claims; the user-gated
publish pushes the 29 existing commits plus the annotated tag and creates the
GitHub Release from the CHANGELOG `[1.20.0]` section only; wave 2 backfills
URLs into STATE, ROADMAP, MILESTONES, PROJECT, and REQUIREMENTS. Assert-based
verification after each wave proves no two planning surfaces disagree.

## Open questions

None blocking. The publish go/no-go is an execution-time user gate handled by
AskUserQuestion inside this package (Decision 4, step 6), not an open design
question; the spec fixes the commands, the readiness checks, and both outcomes.
Minor items are settled in-spec: gap/verify execute rather than waive
(Decision 1), `[Unreleased]` stays separate from the release notes (Decision
3), and the notes file lives at `docs/superpowers/release-notes/v1.20.0.md`.
