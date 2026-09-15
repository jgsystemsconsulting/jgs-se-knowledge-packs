# Context: close-phase21-ship-surface (2026-09-14)

## Context brief

**Primary question**: What ledger fields, gate shapes, and product evidence does an honest Phase 21 re-gate need so MAP-21-05 / REL-21-01 / REL-21-02 can be marked complete without lying about CR-01 or inventing a GitHub Release?

**Sub-questions**:
1. Exact stale master_flow / ROADMAP / REQUIREMENTS / STATE / IMPL_REVIEW fields (quoted + line refs).
2. Completed-phase `master_flow_state.json` shape (Phase 19/20) to mirror after a real re-gate.
3. What "re-gate impl_review" means mechanically here (artifact, verdict rewrite, state fields).
4. MAP-21-05 / REL-21-01 / REL-21-02 wording vs today's on-disk mechanical evidence.
5. Exact tick targets and hard constraints (no gh release; no product code; ledger + gate evidence only).

**Success criteria**: SC1 stale quotes; SC2 completed-phase gate shape; SC3 re-gate semantics; SC4 requirement evidence map; SC5 tick targets + constraints.

**Out of scope** (packages.md P3, X1 resolved 2026-09-14: P8 owns `/gsd-ship`):
- Creating the GitHub Release (P8).
- Website YAML bump (P1 done on `ffe385a`).
- `check_release` 4a gate (landed with P1).
- WR-01/02/03 residuals (P7 done: `73adda3`, `a9bfae4`, `1b037b4`).
- CI coverage (P5 done).
- Product code edits in this package; ledger edits + gate evidence only.
- Full P8 ledger close (STATE/ROADMAP/GAP milestone narrative beyond the Phase 21 product ticks this package needs).

**Budget**: single-pass context gate.

**Workspace baseline**: HEAD `5b2183c` on `main`. Annotated tag `v1.20.0` peels to `ffe385a` (`fix: align website product YAMLs to 1.20.0 (CR-01)`). No GitHub Release for v1.20.0 (`gh release view v1.20.0` → release not found).

**Parent-verified package facts** (packages.md P3): Phase 21 product work + CR-01 fix on disk; impl_review still `needs_work:cr_01`; ROADMAP Phase 21 0/2 Not started; REL-21-01/02 and MAP-21-05 unchecked; master_flow pre-fix needs_work markers. X1: P8 owns ship; P3 narrows to re-gate + remaining product gates.

## Findings

Grades: CORROBORATED 14, SINGLE-SOURCE 4, CONFLICTED 0, STALE 6 (ledger fields that contradict live product).

| # | Claim | Grade |
|---|-------|-------|
| 1 | Phase master_flow `current_gate` = `impl_review`, `blocked_by` = `impl_review` | CORROBORATED |
| 2 | Verdict `impl_review` = `needs_work:cr_01:_docs/products/website/01_jgs_se_knowledge_packs.yaml_still_version_1.19.1;_retag_after_bump` | CORROBORATED (STALE vs product) |
| 3 | `regate_attempts.impl_review` = 1; completed stops at `execute`; no post-execute gates in `completed` | CORROBORATED |
| 4 | Root pointer still active_phase 21 / lock on phase 21 | CORROBORATED |
| 5 | ROADMAP progress table: Phase 21 `0/2` / `Not started` | CORROBORATED (STALE) |
| 6 | ROADMAP phase list + plan checkboxes for 21 still open; coverage MAP/REL Pending | CORROBORATED (STALE) |
| 7 | REQUIREMENTS MAP-21-05 / REL-21-01 / REL-21-02 all unchecked | CORROBORATED (STALE vs product evidence) |
| 8 | MAP-21-05 wording still says "optional note overrides" | CORROBORATED (STALE vs CONTRACT + generator) |
| 9 | 21-IMPL_REVIEW.md status `issues_found`, Verdict NEEDS_WORK on CR-01 1.19.1 YAML | CORROBORATED (STALE vs live YAML 1.20.0) |
| 10 | WR-01/02/03 described as open in IMPL_REVIEW; live code closed them (P7) | STALE review text / CORROBORATED live fix |
| 11 | Website YAMLs both `version: "1.20.0"`; check_release 4a covers them | CORROBORATED |
| 12 | Tag `v1.20.0` annotated on `ffe385a`; HEAD is later CI work, not the tag tip | CORROBORATED |
| 13 | No `21-VERIFICATION.md`; later gates (code_review, integration, security) exist as PASS_* artifacts but are absent from master_flow `completed` | CORROBORATED |
| 14 | Phase 19/20 completed shape: `impl_review` in `completed`, verdict `passed`/`passed_with_notes`, `blocked_by: null`, `current_gate` advanced past reviews to `doc_check` | CORROBORATED |
| 15 | 21-02-SUMMARY handoff: phase.complete ticks MAP/REL; `/gsd-ship` owns gh release; fix "optional" wording on MAP-21-05 tick | CORROBORATED |
| 16 | STATE.md still `status: planning`, `stopped_at: Phase 20 complete...`, progress 2/3 phases | CORROBORATED (STALE; P8 primary) |
| 17 | Live MAP-21-05 evidence: CONTRACT §4 names generator; §8 residual = required note-overrides only | CORROBORATED |
| 18 | Live REL-21-01 evidence: map_version 1.20.0; trio 1.20.0; check_release path ready (not re-run this gate) | CORROBORATED |
| 19 | Live REL-21-02 partial: surfaces + CHANGELOG + local annotated tag present; GitHub Release absent by design (P8) | CORROBORATED |

## Stale ledger (exact quotes)

### Phase master_flow (`.planning/phases/21-contract-rewrite-release-surfaces/master_flow_state.json`)

| Field | Live quote | Lines (approx) |
|-------|------------|----------------|
| `current_gate` | `"impl_review"` | L10 |
| `completed` | `["research","plan","plan_check","plan_review","execute"]` only | L11-17 |
| `blocked_by` | `"impl_review"` | L34 |
| `verdicts.impl_review` | `"needs_work:cr_01:_docs/products/website/01_jgs_se_knowledge_packs.yaml_still_version_1.19.1;_retag_after_bump"` | L55 |
| `artifacts.impl_review` | `".planning/phases/21-contract-rewrite-release-surfaces/21-IMPL_REVIEW.md"` | L63 |
| `regate_attempts.impl_review` | `1` | L65-67 |
| `updated_at` | `"2026-08-27T19:49:22.836Z"` | L104 |

Config still has `enable_impl_review`, `enable_code_review`, `enable_integration_check`, `enable_security_audit`, `enable_gap_analysis`, `enable_verify` true. Those gates never advanced in this file even though on-disk review artifacts exist for code/integration/security.

### Root pointer (`.planning/master_flow_state.json`)

```json
"active_phase": 21,
"active_phase_dir": ".planning/phases/21-contract-rewrite-release-surfaces",
"active_state": ".planning/phases/21-contract-rewrite-release-surfaces/master_flow_state.json",
"lock": { "phase": 21, "session_hint": "master-flow", "updated_at": "2026-08-27T19:49:22.838Z" }
```

### ROADMAP (`.planning/ROADMAP.md`)

- Overview still: `map_version **1.19.1**` (L5) while live map is 1.20.0.
- Phase list: `- [ ] **Phase 21: CONTRACT rewrite + release surfaces**` (L34).
- Plans still open (L98-99 area): `21-01-PLAN.md` / `21-02-PLAN.md` unchecked.
- Progress table (L107-110):

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 21. CONTRACT rewrite + release surfaces | 0/2 | Not started | - |

- Coverage (L119-121): MAP-21-05 / REL-21-01 / REL-21-02 all `Pending`.

### REQUIREMENTS (`.planning/REQUIREMENTS.md` L18-22)

```
- [ ] **MAP-21-05**: `docs/capability-map-CONTRACT.md` §4 names the generator as the refresh path; §8 residual is closed or reduced to documented optional note overrides only
- [ ] **REL-21-01**: `python tooling/check_release.py` PASS at frozen 63 catalog / 65 dirs; `map_version` is 1.20.0; no new packs
- [ ] **REL-21-02**: Version surfaces + CHANGELOG [1.20.0] record the generator honestly; annotated tag + GitHub Release when the product surface is ready
```

Stale wording inside MAP-21-05: **"optional note overrides"**. Generator and CONTRACT treat the 644-row overrides file as **required** (fails closed if missing). 21-01-SUMMARY / 21-02-SUMMARY handoff already require fixing that wording when ticking.

### STATE (`.planning/STATE.md`) — stale, primarily P8

- Frontmatter: `current_phase: 21`, `status: planning`, `stopped_at: Phase 20 complete, ready to plan Phase 21`, `completed_phases: 2`, `percent: 67`.
- Body still says Plan Not started / Ready to plan / progress bar 33%.
- P3 may touch Phase 21 product-tick adjacency; full STATE/GAP/MILESTONES narrative close is P8.

### 21-IMPL_REVIEW.md (stale verdict artifact)

- Frontmatter: `status: issues_found`; `findings.critical: 1` (CR-01).
- Body L39: `**Verdict: NEEDS_WORK**`.
- CR-01 cites `docs/products/website/01-jgs-se-knowledge-packs.yaml` and `catalog.yaml` still `version: "1.19.1"`, tag on `046799b`.
- WR-01/02/03 listed as open warnings with fix guidance.
- Recommended next actions: fix CR-01, fold WR-01, defer WR-02/03.

**Live contradiction (product truth since review)**:

| Finding | Review claim | Live truth |
|---------|--------------|------------|
| CR-01 | YAML still 1.19.1; tag on 046799b | Both YAMLs `version: "1.20.0"`; `check_release` 4a enforces them; tag `v1.20.0` → `ffe385a` |
| WR-01 | cluster_names unvalidated / unescaped | `_CLUSTER_NAME_FORBIDDEN` + reject loops in generator and check_rules; `render_md` pipe-escapes cluster name (P7 `73adda3`) |
| WR-02 | no rules-vs-map `generated_on` fidelity | `check_classification_rules` fidelity fails on date drift (P7 `a9bfae4`) |
| WR-03 | `--check` JSON-only | `--check` also compares rendered md (P7 `1b037b4`) |

## Completed-phase gate shape (mirror target)

### Phase 19 / 20 `master_flow_state.json` (post-review wave)

Common shape after a successful review wave:

| Field | Completed-phase value |
|-------|------------------------|
| `current_gate` | `"doc_check"` (next disabled gate; not stuck on `impl_review`) |
| `blocked_by` | `null` |
| `completed` | includes `execute`, `impl_review`, `code_review`, `integration_check`, `security_audit`, `gap_analysis`, `verify` (phase 19/20) |
| `verdicts.impl_review` | `"passed_with_notes:review_wave"` (19) or `"passed_with_notes"` (20) |
| `verdicts.code_review` / `integration_check` | `"passed_with_notes..."` |
| `verdicts.security_audit` | `"passed..."` |
| `verdicts.gap_analysis` / `verify` | `"passed"` |
| `artifacts` | paths for impl_review (20), code_review, integration_check, security_audit, gap_analysis, verify |
| `failed` | `[]` |

Phase 21 already has on-disk:

| Artifact | Disk path | Documented verdict |
|----------|-----------|--------------------|
| impl_review | `21-IMPL_REVIEW.md` | NEEDS_WORK / issues_found (**stale**) |
| code_review | `21-CODE_REVIEW.md` | PASS_WITH_NOTES |
| integration_check | `21-INTEGRATION_CHECK.md` | PASS_WITH_NOTES |
| security_audit | `21-SECURITY_AUDIT.md` | SECURED |
| gap_analysis | **missing** | n/a |
| verify / VERIFICATION | **missing** (`21-VERIFICATION.md` absent) | n/a |

Honest re-gate for **this package** must at minimum clear `impl_review`. Advancing the rest of the review wave (recording code/integration/security already-written PASS artifacts into `completed`/`verdicts`, and deciding gap/verify) is in scope only insofar as it is required to stop lying about the CR-01 block and to unlock product ticks. Do not invent gap/verify files without running those gates. Do not mark `impl_review` passed while CR/WR claims in the review body still describe fixed defects as open.

## Re-gate impl_review semantics

**What it is here**: not a green checkbox on the old file. An honest re-gate is a fresh verification pass against **current** product truth, then a rewritten (or superseding) impl_review verdict and matching master_flow fields.

### Required mechanical steps (spec/plan must encode; this context does not run them)

1. **Verify CR-01 fix live**
   - `docs/products/website/01-jgs-se-knowledge-packs.yaml` and `catalog.yaml` both `version: "1.20.0"`.
   - `tooling/check_release.py` includes step 4a scoped to those two paths.
   - Local annotated tag `v1.20.0` points at the CR-01 fix commit (`ffe385a`), not the pre-fix `046799b`.
2. **Verify WR-01/02/03 fixes live** (P7 landed; re-gate must not re-open them)
   - WR-01: forbidden char reject in generator + check_rules; pipe escape in `render_md`.
   - WR-02: fidelity `rules generated_on != live map` fail path present.
   - WR-03: generator `--check` md freshness compare present.
3. **Re-run product gates** (evidence for MAP/REL; do not skip)
   - `python tooling/check_release.py` → PASS, catalog 63 / dirs 65, map_version 1.20.0.
   - `python tooling/check_capability_map.py` → PASS, TOTAL 644.
   - `python tooling/check_classification_rules.py` → PASS.
   - `python tooling/generate_capability_map.py --generated-on 2026-08-27 --check` → PASS (JSON + md freshness).
   - Confirm no new packs; version trio + website YAMLs + CHANGELOG [1.20.0] honest; `git cat-file -t v1.20.0` → `tag`.
4. **Write the new verdict**
   - Update `21-IMPL_REVIEW.md` (or add a dated re-gate addendum the flow treats as the gate artifact) so status is no longer `issues_found` / NEEDS_WORK on CR-01.
   - Record CR-01 CLOSED with evidence (YAML lines, tag peel, 4a).
   - Record WR-01/02/03 CLOSED with commit or live code refs (do not leave the old open-warning body as the active verdict).
   - Frontmatter findings counts and `status` must match the new body.
5. **Repair phase master_flow fields**
   - `verdicts.impl_review` → `passed` or `passed_with_notes:...` (no `needs_work:cr_01`).
   - Add `impl_review` to `completed` if not present.
   - Clear `blocked_by` if nothing else blocks.
   - Advance `current_gate` off `impl_review` toward the next real gate (mirror 19/20 only as far as artifacts exist; do not fabricate gap/verify).
   - Bump `regate_attempts.impl_review` (already 1 → next integer).
   - Refresh `updated_at`.
   - Optionally attach later review artifact paths already on disk (`code_review`, `integration_check`, `security_audit`) if the re-gate wave records them; only with matching verdicts from those files.

### What re-gate is **not**

- Not silent master_flow surgery without a new review verdict.
- Not ticking REQUIREMENTS while IMPL_REVIEW still says NEEDS_WORK.
- Not creating a GitHub Release.
- Not rewriting product tooling "to satisfy the gate" (product already fixed).
- Not claiming REL-21-02 fully closed if the requirement text is read as requiring the GitHub Release now; see requirement split below and X1 (P8 owns ship).

## MAP / REL requirements and today's evidence

### MAP-21-05

**Wording today**: CONTRACT §4 names generator as refresh path; §8 residual closed or reduced to documented **optional** note overrides only.

**Product evidence already on disk** (re-gate must re-confirm, not rebuild):

| Clause | Evidence |
|--------|----------|
| §4 names generator | `docs/capability-map-CONTRACT.md` §4: `python tooling/generate_capability_map.py --generated-on YYYY-MM-DD` (+ optional `--sync-md`); rules + note-overrides are committed inputs; cluster assignment mechanical |
| §8 residual | §8 title `FUT-05 residual (note overrides only)`; remaining human input is the committed 644-row overrides file |
| Overrides not optional to omit | CONTRACT §4: generator fails closed if overrides missing; generator code requires the file |
| REQUIREMENTS checkbox text | Still says "optional"; **must be corrected on tick** (21-01-SUMMARY PR-05 / W-3; 21-02-SUMMARY handoff) |

**Tick condition**: evidence above + wording fix `optional` → required/mandatory note-overrides (or equivalent accurate phrase). No product rewrite needed if CONTRACT already matches.

### REL-21-01

**Wording**: `python tooling/check_release.py` PASS at frozen 63 catalog / 65 dirs; `map_version` is 1.20.0; no new packs.

**Evidence today** (static; re-gate must re-run the gate for a fresh PASS receipt):

| Clause | Evidence |
|--------|----------|
| map_version 1.20.0 | `docs/capability-pack-map.json` `"map_version": "1.20.0"` |
| Version trio 1.20.0 | `.claude-plugin/plugin.json`, `CHANGELOG.md` `## [1.20.0]`, `RELEASE-INFO.txt` |
| Website YAML 1.20.0 + 4a | both product YAMLs; `check_release.py` step 4a |
| Catalog freeze | Phase plans and prior PASS runs: 63 / 65; no pack adds in Phase 21 commits |
| Replay / map path | generator `--check` (JSON+md), check_capability_map, check_classification_rules, check_release 5e/5f/5g |

**Tick condition**: fresh `check_release.py` PASS in the re-gate session with the freezes above. Do not tick on memory of 2026-08-27 SUMMARY alone.

### REL-21-02

**Wording**: Version surfaces + CHANGELOG [1.20.0] record the generator honestly; **annotated tag + GitHub Release when the product surface is ready**.

**Split (X1 resolved)**:

| Clause | Owner | Status today |
|--------|-------|--------------|
| Version surfaces honest (trio, README, packs.html, plugins, index, SECURITY cadence, website YAMLs) | Phase 21 product / P1 | On disk at 1.20.0 |
| CHANGELOG [1.20.0] names generator | Phase 21 Plan 02 | Present (`## [1.20.0]: 2026-08-27`) |
| Annotated tag `v1.20.0` | Phase 21 Plan 02 + CR-01 retag | Local annotated tag on `ffe385a` |
| GitHub Release | **P8 / `/gsd-ship`** | **Not created** (`release not found`) |

**Tick policy for P3**:
- Product-gate portion of REL-21-02 (surfaces + CHANGELOG + local annotated tag) is satisfiable after re-gate evidence.
- Do **not** create the GitHub Release in P3.
- If REQUIREMENTS is ticked in P3, the tick note must state GitHub Release remains P8 `/gsd-ship`, consistent with 21-02-SUMMARY handoff and ROADMAP "when the product surface is ready". Prefer coordinating the checkbox moment with P8 if a bare `[x]` would imply the Release already exists. packages.md P3 in_scope says "finish remaining Phase 21 product gates needed to mark MAP-21-05 / REL-21-01 / REL-21-02 complete"; read that as product-gate readiness + honest tick text, not as running `gh release create`.

## Exact tick targets

| Target | Path | Change |
|--------|------|--------|
| IMPL_REVIEW verdict | `.planning/phases/21-.../21-IMPL_REVIEW.md` | Rewrite/re-gate to passed (CR/WR closed with live evidence) |
| Phase master_flow | `.planning/phases/21-.../master_flow_state.json` | Clear `needs_work:cr_01`; `impl_review` completed; `blocked_by` null or next real block; advance `current_gate`; bump regate counter |
| Root pointer | `.planning/master_flow_state.json` | Keep phase 21 active until phase close; refresh lock timestamps if touching; do not pretend milestone complete |
| ROADMAP phase table | `.planning/ROADMAP.md` ~L107-110 | Phase 21 plans complete **2/2**, status reflecting execute+re-gate reality (not `0/2 Not started`). Full milestone/overview 1.19.1 prose may stay for P8 if split cleanly |
| ROADMAP phase list + plan boxes | L34, L98-99 | Tick Phase 21 and 21-01/21-02 plan rows when product gates pass |
| ROADMAP coverage | L119-121 | MAP-21-05 / REL-21-01 / REL-21-02 → Complete when REQUIREMENTS ticked |
| REQUIREMENTS | L18-22 | Tick MAP-21-05 (fix optional wording), REL-21-01, REL-21-02 with ship-tail note if Release still open |
| STATE | `.planning/STATE.md` | Minimal touch only if required for gate honesty; full planning/stopped_at close is P8 |

## Constraints

1. **No GitHub Release** in this package (P8 owns `/gsd-ship`; X1 resolved 2026-09-14).
2. **No product code edits** for P3 proper: CR-01, WR-01/02/03, check_release 4a, CI already landed. Re-gate measures them.
3. **Ledger + gate evidence only**: planning files (gitignored) + review verdict rewrite + requirement/roadmap ticks.
4. **Do not retag or force-push** unless a live probe proves the tag is wrong; current peel `v1.20.0` → `ffe385a` is the CR-01 fix.
5. **Do not edit** `packs/`, `.github/workflows/validate.yml`, or invent packs.
6. **Do not mark impl_review passed** while leaving the NEEDS_WORK body as the active story.
7. **REQUIREMENTS MAP-21-05 wording** must lose the false "optional" overrides claim on tick.
8. **REL-21-02** must not silently claim a missing GitHub Release; document P8 tail.

## Phase 21 artifact inventory

| File | Role |
|------|------|
| `21-01-PLAN.md` / `21-01-SUMMARY.md` | Plan 01 execute complete (CONTRACT + envelope + replay) |
| `21-02-PLAN.md` / `21-02-SUMMARY.md` | Plan 02 execute complete (trio, CHANGELOG, tag); handoff ticks + ship |
| `21-RESEARCH.md`, `21-PATTERNS.md` | Research/patterns |
| `21-PLAN_CHECK.md` | PASS_WITH_FIXES |
| `21-PLAN_REVIEW.md` | APPROVE_WITH_NOTES |
| `21-IMPL_REVIEW.md` | **Stale NEEDS_WORK** (re-gate target) |
| `21-CODE_REVIEW.md` | PASS_WITH_NOTES (not in master_flow completed) |
| `21-INTEGRATION_CHECK.md` | PASS_WITH_NOTES (not in master_flow completed) |
| `21-SECURITY_AUDIT.md` | SECURED (not in master_flow completed) |
| `master_flow_state.json` | Stuck at impl_review needs_work:cr_01 |
| `21-VERIFICATION.md` / GAP | **Absent** |

## Synthesis

SC1-SC5 covered. Phase 21 product truth is at 1.20.0 with CR-01 and WR-01/02/03 closed on disk; the GSD ledger and `21-IMPL_REVIEW.md` still advertise the pre-fix block. An honest P3 pass re-verifies CR/WR live, re-runs the four map/release commands, rewrites the impl_review verdict, clears `needs_work:cr_01` in master_flow, and only then ticks MAP-21-05 (with wording fix), REL-21-01, and the product side of REL-21-02. GitHub Release stays P8. No product code churn.

## Evidence index

| Loc | Kind |
|-----|------|
| `.planning/phases/21-.../master_flow_state.json` | ledger (stale impl_review) |
| `.planning/master_flow_state.json` | root pointer phase 21 |
| `.planning/ROADMAP.md` L5, L34, L98-110, L119-121 | roadmap stale rows |
| `.planning/REQUIREMENTS.md` L18-22 | unchecked MAP/REL + optional wording |
| `.planning/STATE.md` | planning/Phase 20 stop (P8-heavy) |
| `.planning/phases/21-.../21-IMPL_REVIEW.md` | stale NEEDS_WORK / CR-01 / WR-01..03 |
| `.planning/phases/21-.../21-02-SUMMARY.md` L140-155 | tick + ship handoff |
| `.planning/phases/19-.../master_flow_state.json` | completed-phase shape |
| `.planning/phases/20-.../master_flow_state.json` | completed-phase shape |
| `docs/capability-map-CONTRACT.md` §4, §8 | MAP-21-05 product truth |
| `docs/products/website/01-jgs-se-knowledge-packs.yaml:15` | CR-01 closed |
| `docs/products/website/catalog.yaml:13` | CR-01 closed |
| `tooling/check_release.py` ~L171-181 | 4a website YAML gate |
| `tooling/generate_capability_map.py` cluster forbid + md check | WR-01/03 closed |
| `tooling/check_classification_rules.py` fidelity generated_on | WR-02 closed |
| `docs/capability-pack-map.json` map_version 1.20.0 | REL-21-01 |
| `CHANGELOG.md` `## [1.20.0]` | REL-21-02 surfaces |
| `git` tag `v1.20.0` → `ffe385a` | REL-21-02 local tag |
| `docs/superpowers/packages/2026-09-14-jgs-se-knowledge-packs-packages.md` P3, X1 | package scope |
| format refs: `2026-09-14-map-tooling-residual-harden-context.md` (+ log) | structure mirror |
