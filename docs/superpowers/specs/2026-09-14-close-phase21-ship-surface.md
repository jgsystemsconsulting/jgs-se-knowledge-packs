# Spec: close-phase21-ship-surface (2026-09-14)

Package P3, size M. Phase 21 product work and the CR-01 fix are on disk, but the GSD ledger still advertises the pre-fix blocker: `master_flow` carries `needs_work:cr_01`, ROADMAP shows Phase 21 `0/2 Not started`, REQUIREMENTS leaves MAP-21-05 / REL-21-01 / REL-21-02 unchecked, and `21-IMPL_REVIEW.md` still says NEEDS_WORK on the 1.19.1 YAML drift that `ffe385a` fixed. This package re-gates impl_review against live product truth, repairs the phase ledger to the phase 19/20 shape, and ticks the three requirements on fresh mechanical evidence. It does not create the GitHub Release; P8 owns `/gsd-ship` (X1 resolved 2026-09-14).

## Research

research: skipped (in-repo GSD ledger re-gate only; no external APIs, libraries, platforms, or version-sensitive choices)

Grounding: context gate 2026-09-14 (`docs/superpowers/context/2026-09-14-close-phase21-ship-surface-context.md` + log), packages ledger P3/P8/X1, and live probes run while writing this spec: tag `v1.20.0` is annotated and peels to `ffe385a`; both website YAMLs read `version: "1.20.0"` (`catalog.yaml:13`, `01-jgs-se-knowledge-packs.yaml:15`); `docs/capability-pack-map.json` has `map_version: "1.20.0"`; CHANGELOG carries `## [1.20.0]: 2026-08-27`; WR-01 forbid lists live at `tooling/generate_capability_map.py:39,88` and `tooling/check_classification_rules.py:28,99`; WR-02 fidelity date compare lives at `check_classification_rules.py:257-261`; WR-03 md freshness compare lives in the generator `--check` path (`render_md` at `:365`). Phase 21 has no `21-GAP_ANALYSIS.md` and no `21-VERIFICATION.md`.

## Codebase context

- `.planning` is gitignored. Planning files are local-only ledger state; nothing here is committed.
- Phase 21 state (`.planning/phases/21-contract-rewrite-release-surfaces/master_flow_state.json`): `current_gate: "impl_review"`, `blocked_by: "impl_review"`, `completed` stops at `execute`, `verdicts.impl_review` is the stale `needs_work:cr_01:...1.19.1...` string, `regate_attempts.impl_review: 1`, `failed: []`.
- Mirror template: phases 19/20 state files show the completed-phase shape. After a review wave: `impl_review`/`code_review`/`integration_check`/`security_audit` in `completed`, verdicts in the `passed...` family (`passed_with_notes:review_wave`, `passed:secured...`), `blocked_by: null`, `current_gate` advanced to the next gate in sequence (`doc_check`, which is disabled), `failed: []`.
- Phase 21 already has three review artifacts on disk that the state file never recorded: `21-CODE_REVIEW.md` (verdict `PASS_WITH_NOTES`), `21-INTEGRATION_CHECK.md` (`PASS_WITH_NOTES`), `21-SECURITY_AUDIT.md` (`SECURED`, 16/16 threats closed, 0 open).
- Requirement evidence is mechanical and on disk today; only the fresh run receipt is missing (see Evidence set).

## Design decision 1: Re-gate evidence set and where the run record lives

### Commands run fresh at re-gate time

All run from repo root, branch `main`, before any ledger edit. Expected receipts:

| # | Command | Expected |
|---|---------|----------|
| 1 | `python tooling/check_release.py` | exit 0; final line `RELEASE CHECK: PASS (v<version> @ <sha>)`; no `[version]` failure lines (4a website-YAML consistency is silent on success); the nested 5g generator run prints its two map PASS lines |
| 2 | `python tooling/check_capability_map.py` | exit 0; TOTAL 644; 32 clusters |
| 3 | `python tooling/check_classification_rules.py` | exit 0; `PASS: classification rules OK` (the generated_on fidelity check of WR-02 runs inside, silent on success) |
| 4 | `python tooling/generate_capability_map.py --generated-on 2026-08-27 --check` | exit 0; byte-stable JSON plus md freshness compare (WR-03) |
| 5 | `git cat-file -t v1.20.0` then `git rev-list -n 1 v1.20.0` | `tag`; peel `ffe385a...` (CR-01 retag) |
| 6 | Static greps (cite file:line in the record) | both website YAMLs `version: "1.20.0"`; `_CLUSTER_NAME_FORBIDDEN` and reject loops present in generator and `check_rules`; pipe escape in `render_md` |

No network calls. No `gh` commands: the absent GitHub Release is documented from the X1 resolution, not probed. REL-21-02's ship tail is carried as text, not as a probe result.

### Where the record lives: rewritten `21-IMPL_REVIEW.md`, not a new `21-03-RE-GATE.md`

Pick: the re-gate appends a dated "Re-gate 2026-09-14" section at the top of `21-IMPL_REVIEW.md` carrying the verdict and the command table above; the original findings text stays below, intact, with each finding heading annotated `CLOSED 2026-09-14` plus one line of evidence.

Why in place, and why not a second artifact:

1. `master_flow.artifacts.impl_review` names exactly one path, and phase 20 keeps one file per gate (phase 19's artifacts map never lists the review gates). A second file either leaves the pointed-to artifact shouting NEEDS_WORK (the lie survives) or forces an artifacts-map shape the template does not have.
2. The constraint "never mark impl_review passed while the NEEDS_WORK body is the active story" is only satisfiable by changing that file's active verdict.
3. `.planning` is gitignored, so superseding in place while preserving the original text below is the only history-preserving option. A separate file would strand the CR-01 record in an orphaned NEEDS_WORK document.

Frontmatter changes: keep `reviewed: 2026-08-27...`; add `regated: 2026-09-14`; `status: issues_found` to `status: passed`; findings become `critical: 0, warning: 0, info: 2, total: 2` (IN-01 and IN-02 remain informational no-actions). Body verdict line: `**Verdict: PASS_WITH_NOTES** (re-gate 2026-09-14; supersedes NEEDS_WORK of 2026-08-27)`. Each closed finding gets its evidence in the re-gate section: CR-01 via command 5 plus the two YAML lines plus 4a; WR-01 via the forbid-list and escape lines; WR-02 via the fidelity block; WR-03 via the `--check` md compare.

## Design decision 2: master_flow field-by-field transition

Target file: `.planning/phases/21-contract-rewrite-release-surfaces/master_flow_state.json`. Every changed field uses the 19/20 vocabulary. One deliberate divergence, documented below.

| Field | Current | After re-gate | Basis |
|-------|---------|---------------|-------|
| `current_gate` | `"impl_review"` | `"gap_analysis"` | Next gate in sequence with no on-disk artifact. 19/20 show `doc_check` only because their gap/verify artifacts exist. |
| `completed` | `research, plan, plan_check, plan_review, execute` | adds `impl_review`, `code_review`, `integration_check`, `security_audit` | impl_review by the fresh re-gate; the other three by their on-disk PASS artifacts. |
| `blocked_by` | `"impl_review"` | `null` | The CR-01 block is closed. Nothing else fails; gap/verify are pending, not blocking. 19/20 use `null`. |
| `verdicts.impl_review` | `"needs_work:cr_01:..."` | `"passed_with_notes:regate_cr01_wr01_wr02_wr03_closed"` | 19/20 underscore style; notes name what closed. |
| `verdicts.code_review` | absent | `"passed_with_notes"` | `21-CODE_REVIEW.md` verdict. |
| `verdicts.integration_check` | absent | `"passed_with_notes"` | `21-INTEGRATION_CHECK.md` verdict. |
| `verdicts.security_audit` | absent | `"passed:secured"` | `21-SECURITY_AUDIT.md` frontmatter `SECURED`, 16/16 closed. Mirrors 19 (`passed:review_wave`) / 20 (`passed:secured...`). |
| `artifacts` | through `impl_review` | adds `21-CODE_REVIEW.md`, `21-INTEGRATION_CHECK.md`, `21-SECURITY_AUDIT.md` paths (the on-disk files named in the verdict rows above) | Files exist on disk; phase 20 records artifact paths for completed gates. |
| `regate_attempts.impl_review` | `1` | `2` | Counter bump on every re-gate. |
| `updated_at` | `2026-08-27T19:49:22.836Z` | re-gate timestamp | Normal refresh. |
| `failed` | `[]` | `[]` unchanged | Nothing failed at re-gate. |
| `skipped`, `config_snapshot`, `execute`, `checkpoint_log`, `notes` | unchanged | unchanged | No gate was skipped or enabled/disabled; plan counts are historical. |

Deliberate divergence from the full 19/20 shape: `completed` does not gain `gap_analysis` or `verify`, and `current_gate` does not reach `doc_check`. Phase 21 has no gap or verify artifacts. Running those gates or writing stand-in files is fabrication, banned by the same constraint that demands the mirror. The mirror rule resolves cleanly: copy the 19/20 shape for every field that has evidence; leave the two fields that would need invented evidence in an honest open state. P8's close (master_flow "Phase 21 complete") inherits them.

Root pointer (`.planning/master_flow_state.json`): no edit. `active_phase: 21` is still true; the phase is not complete. P8 closes it.

## Design decision 3: Tick order and wording

Order: evidence, then verdict, then state, then ticks. The ordering rules are absolute: never tick REQUIREMENTS while the active impl_review verdict says NEEDS_WORK, and never let ROADMAP coverage contradict REQUIREMENTS.

1. **Run the evidence set** (decision 1). Any failure stops everything before step 2.
2. **Rewrite `21-IMPL_REVIEW.md`** per decision 1.
3. **Update phase `master_flow_state.json`** per decision 2.
4. **REQUIREMENTS.md** (`L18-23` plus traceability `L54-56`):
   - MAP-21-05, tick and fix the false wording. New text: `docs/capability-map-CONTRACT.md` §4 names the generator as the refresh path; §8 residual is closed or reduced to the committed note-override file, which the generator requires (fails closed if missing). The word "optional" is gone.
   - REL-21-01, tick, text unchanged; the fresh PASS receipt is the evidence.
   - REL-21-02, tick with an explicit tail so the box never silently claims a missing release: `... annotated tag + GitHub Release when the product surface is ready (tag v1.20.0 on ffe385a; GitHub Release: P8 /gsd-ship)`.
   - Traceability rows: MAP-21-05 and REL-21-01 `Complete`; REL-21-02 `Complete (gh release: P8)`.
5. **ROADMAP.md**:
   - Plan boxes `L91-92`: tick `21-01-PLAN.md` and `21-02-PLAN.md` (both executed, SUMMARYs on disk).
   - Progress row `L103`: `| 21. CONTRACT rewrite + release surfaces | 2/2 | Executed | - |`, plus one line under the table: `Phase 21 product gates PASS; impl_review re-gated 2026-09-14. Phase close (gap_analysis, verify, milestone ledger): P8.` "Executed" is honest; "Complete" is not, yet.
   - Coverage rows `L113-115`: MAP-21-05 and REL-21-01 `Complete`; REL-21-02 `Complete (gh release: P8)`.

**21-02-SUMMARY pointer: not needed.** The SUMMARY is a historical execution record; rewriting its handoff would rewrite history. The live handoff now lives in the re-gate section of `21-IMPL_REVIEW.md`, which `master_flow.artifacts.impl_review` points at. P8 reads the re-gate, finds the ticks done, and proceeds to ledger close and `/gsd-ship`.

Left for P8, deliberately: ROADMAP overview `map_version 1.19.1` prose (`L5`), the Phase 21 phase-list checkbox (`L34`) and Completed date, STATE.md, MILESTONES/GAP.md, phase-21 completion in master_flow, root pointer, `/gsd-ship`, push.

One wording artifact left as-is: MAP-21-02's already-ticked text says "optional note-override file". That is a closed historical requirement; CONTRACT §4 and the generator are the source of truth for requiredness, and retroactively editing ticked requirements is worse than the stale adjective. Recorded here so a reviewer does not re-flag it.

## Design decision 4: Deliberately not done here

- GitHub Release creation: P8 owns `/gsd-ship` (X1).
- Any network operation: no `gh`, no push, no `git ls-remote`.
- gap_analysis and verify gates: not run, no artifacts written, not recorded in `completed`.
- STATE.md and the milestone narrative: P8.
- Product code, `packs/`, `.github/workflows/`, website YAMLs, `check_release` gate code, WR-01/02/03 fixes: all landed in P1/P5/P7; this package only measures them.
- Retag: the live peel is `ffe385a`, the CR-01 fix. Tag untouched.

## Failure policy

If any command in the evidence set exits nonzero, or any static grep mismatches (a YAML not at 1.20.0, a WR guard missing, tag peel not `ffe385a`): stop. Write nothing in any ledger file. Report the failing command and output. The single sanctioned remediation inside this package is the context-gate conditional on the tag: only if a live probe proves `v1.20.0` points at the wrong commit, delete and recreate the local annotated tag on the correct commit per the CR-01 recipe, then rerun the full evidence set from command 1. Every other failure belongs to a product-fix package, not to P3.

## Approach

One session, local only. Re-run the four gates plus tag and static checks; record receipts in a dated re-gate section on top of `21-IMPL_REVIEW.md` with the original findings kept below and closed with evidence; repair the phase `master_flow_state.json` fields to the 19/20 shape as far as evidence exists (impl_review plus the three recorded review gates, `blocked_by: null`, `current_gate: "gap_analysis"`, regate counter to 2); then tick MAP-21-05 (with the optional-to-required wording fix), REL-21-01, and REL-21-02 (with the P8 ship-tail note) in REQUIREMENTS and mirror them into ROADMAP plan boxes, the progress row, and coverage. STATE, the roadmap overview, the phase-list close, gap/verify, and the GitHub Release stay with P8. Nothing is ticked that the fresh run did not just prove.

## Open questions

None.
