# Close Phase 21 Ship Surface (Re-gate + Ledger Repair) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Re-gate Phase 21 impl_review against live 1.20.0 product truth, repair the phase GSD ledger to the phase 19/20 shape, and tick MAP-21-05 / REL-21-01 / REL-21-02 in REQUIREMENTS and ROADMAP on fresh mechanical evidence.

**Architecture:** Evidence first, then verdict, then state, then ticks (spec decision 3 ordering, absolute). The four map/release gates, the tag peel, and static greps are re-run fresh; the receipts rewrite `21-IMPL_REVIEW.md` in place (dated re-gate section on top, original 2026-08-27 findings preserved below and closed with evidence); the phase `master_flow_state.json` is transitioned field-by-field; then REQUIREMENTS and ROADMAP are ticked. Nothing is ticked that the fresh run did not just prove.

**Tech Stack:** Local `python` (stdlib tooling), Git Bash on Windows, GSD ledger markdown/JSON under `.planning/`. No new dependencies, no network.

**Spec:** `docs/superpowers/specs/2026-09-14-close-phase21-ship-surface.md`

## Research

research: skipped (in-repo GSD ledger re-gate only; no external APIs, libraries, platforms, or version-sensitive choices)

## Global Constraints

- `.planning/` is gitignored by repo policy. All `.planning/` edits are applied on disk and never committed. The `docs/superpowers/` spec/plan artifacts are also not committed by this package. This plan contains no commit steps anywhere; do not run `git add` or `git commit`.
- Task order is absolute: Task 1 (evidence) before Task 2 (verdict) before Task 3 (state) before Tasks 4-5 (ticks). Any Task 1 failure stops everything before Task 2. Never tick REQUIREMENTS while the active impl_review verdict says NEEDS_WORK.
- No network, no `gh` commands, no push, no `git ls-remote`. The absent GitHub Release is documented from the X1 resolution (P8 owns `/gsd-ship`), not probed.
- No product code edits: `packs/`, `.github/workflows/validate.yml`, website YAMLs, `tooling/*` are read-only in this package. The tag is untouched unless the single sanctioned remediation in the Failure policy fires.
- `gap_analysis` and `verify` gates: not run, no artifacts written, not added to `completed`. Root pointer `.planning/master_flow_state.json`: not edited.
- All gate commands run from repo root (`C:/Users/gower/OneDrive/Documents/GitHub/jgs-se-knowledge-packs`), branch `main`.

## Codebase context

- Phase 21 dir: `.planning/phases/21-contract-rewrite-release-surfaces/`. Current phase `master_flow_state.json`: `current_gate: "impl_review"`, `blocked_by: "impl_review"`, `completed` stops at `execute`, `verdicts.impl_review` is the stale `needs_work:cr_01:...1.19.1...` string, `regate_attempts.impl_review: 1`, `failed: []`, `updated_at: "2026-08-27T19:49:22.836Z"`.
- Mirror shape (phases 19/20 after a review wave): `impl_review`/`code_review`/`integration_check`/`security_audit` in `completed`, verdicts in the `passed...` family, `blocked_by: null`, artifact paths for each completed gate, `failed: []`. Phase 21 diverges deliberately: `gap_analysis`/`verify` stay out of `completed` and `current_gate` stops at `"gap_analysis"` because those gates have no artifacts (spec decision 2).
- Phase 21 already has on-disk review artifacts the state file never recorded: `21-CODE_REVIEW.md` (verdict `PASS_WITH_NOTES`), `21-INTEGRATION_CHECK.md` (`PASS_WITH_NOTES`), `21-SECURITY_AUDIT.md` (`SECURED`). No `21-GAP_ANALYSIS.md`, no `21-VERIFICATION.md`.
- Live product truth verified 2026-09-14 while pinning this plan: tag `v1.20.0` is annotated and peels to `ffe385abca97efc7a50b3939f930f78ec5666935`; `docs/products/website/01-jgs-se-knowledge-packs.yaml:15` and `docs/products/website/catalog.yaml:13` both read `version: "1.20.0"`; guard line numbers: `_CLUSTER_NAME_FORBIDDEN` at `tooling/generate_capability_map.py:39` (define) and `:88` (reject loop) and `tooling/check_classification_rules.py:28` / `:99`; cluster-name pipe escape in `render_md` at `tooling/generate_capability_map.py:269` and `:275`; rules-vs-map `generated_on` fidelity at `tooling/check_classification_rules.py:257-261`; md freshness compare in the generator `--check` path at `tooling/generate_capability_map.py:361-376`; generator PASS prints are `PASS: generated map matches on-disk capability-pack-map.json` (`:359`) and `PASS: capability-pack-map.md is fresh` (`:376`); `check_release.py` step 4a website-YAML gate is silent on success; final banner is `RELEASE CHECK: PASS (<receipt>)` (`check_release.py:387`); the nested 5g replay calls `generate_capability_map.main(["--generated-on", disk_on, "--check"])` so its two PASS lines are the two prints above.
- `21-02-SUMMARY.md` is a historical execution record and is not edited in this package; the live handoff moves to the re-gate section of `21-IMPL_REVIEW.md`.

## Failure policy (binding, from spec)

If any gate command exits nonzero, or any static grep mismatches (a website YAML not at 1.20.0, a WR guard missing, tag peel not `ffe385a...`): stop, write nothing in any ledger file, and report the failing command and its output. The single sanctioned remediation inside this package: only if a live probe proves `v1.20.0` points at the wrong commit, delete and recreate the local annotated tag on the correct commit per the CR-01 recipe (`git tag -d v1.20.0 && git tag -a v1.20.0 -m "chore: annotate v1.20.0 <one-line substance>" <correct-commit>`), then rerun the full evidence set from command 1. Every other failure belongs to a product-fix package, not this one.

---

### Task 1: Re-gate evidence run (all six probes, receipts recorded)

**Files:**
- Modify: none (read-only evidence gathering)

**Interfaces:**
- Consumes: nothing.
- Produces: ten receipt lines, in this exact shape, returned in the task output and consumed by Task 2: (1) command 1 exit code; (2) command 1 final `RELEASE CHECK: PASS (...)` line; (3) the two nested 5g map PASS lines from command 1 output; (4) command 2 exit code plus its `TOTAL:` line; (5) command 3 exit code plus its PASS line; (6) command 4 exit code plus its two PASS lines; (7) tag type plus peel sha; (8) the website YAML grep hits; (9) the guard grep hits (forbid lists, reject loops, pipe escape, fidelity block, md compare); (10) the MAP-21-05 grep hits: `docs/capability-map-CONTRACT.md` required-input/fails-closed/§8 wording plus the generator's overrides fail-closed raises.

**Model:** flash

- [ ] **Step 1: Preflight**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/jgs-se-knowledge-packs"
git branch --show-current
git status --porcelain
```

Expected: `main`; untracked `docs/superpowers/` entries allowed, zero tracked-file modifications. If any tracked product file shows as modified, stop and report (product tree must be clean for the re-gate to measure landed work).

- [ ] **Step 2: Command 1, release gate**

```bash
python tooling/check_release.py; echo "EXIT=$?"
```

Expected: `EXIT=0`; final line matches `RELEASE CHECK: PASS (v1.20.0 @ <sha>)` (record the actual banner verbatim); zero `[version]` failure lines anywhere in the output (the 4a website-YAML consistency check is silent on success); the nested 5g replay prints `PASS: generated map matches on-disk capability-pack-map.json` and `PASS: capability-pack-map.md is fresh`. Record exit code, banner, and the two PASS lines.

- [ ] **Step 3: Command 2, capability map check**

```bash
python tooling/check_capability_map.py; echo "EXIT=$?"
```

Expected: `EXIT=0`; output contains `TOTAL: 644` (the checker prints per-cluster count lines, then `  TOTAL: {total}` with a colon and indent; there is no separate one-line cluster total such as `32 clusters`). Record exit code plus the `TOTAL:` line.

- [ ] **Step 4: Command 3, classification rules check**

```bash
python tooling/check_classification_rules.py; echo "EXIT=$?"
```

Expected: `EXIT=0`; output contains `PASS: classification rules OK` (the WR-02 generated_on fidelity check runs inside and is silent on success). Record exit code plus the PASS line.

- [ ] **Step 5: Command 4, generator replay with frozen date**

```bash
python tooling/generate_capability_map.py --generated-on 2026-08-27 --check; echo "EXIT=$?"
```

Expected: `EXIT=0`; output contains `PASS: generated map matches on-disk capability-pack-map.json` (byte-stable JSON) and `PASS: capability-pack-map.md is fresh` (WR-03 md compare). Record exit code plus both PASS lines.

- [ ] **Step 6: Command 5, tag peel**

```bash
git cat-file -t v1.20.0
git rev-list -n 1 v1.20.0
```

Expected: `tag`; peel `ffe385abca97efc7a50b3939f930f78ec5666935`. Record both. If the peel differs, apply the Failure policy remediation (recreate the local annotated tag on the correct commit), then rerun from Step 2. If the type is not `tag`, stop and report.

- [ ] **Step 7: Command 6, static greps**

```bash
grep -n 'version:' docs/products/website/01-jgs-se-knowledge-packs.yaml docs/products/website/catalog.yaml
grep -n '_CLUSTER_NAME_FORBIDDEN' tooling/generate_capability_map.py tooling/check_classification_rules.py
grep -n 'cluster\["name"\]\.replace("|"' tooling/generate_capability_map.py
grep -n 'live_on' tooling/check_classification_rules.py
grep -n 'md is stale\|md is fresh\|md check' tooling/generate_capability_map.py
grep -n 'committed inputs\|fails closed\|FUT-05 residual' docs/capability-map-CONTRACT.md
grep -n 'raise ValueError' tooling/generate_capability_map.py | grep -i overrides
```

Expected hits for the MAP-21-05 pair (added for the requirement tick):

6. `docs/capability-map-CONTRACT.md` lines naming the note-overrides file as a committed, required generator input that fails closed when missing (`:72-82`) and the §8 FUT-05 residual (`:136-144`)
7. `generate_capability_map.py` overrides fail-closed raises at `:62`, `:101`, `:105` (a missing overrides file surfaces as the missing-file error from `_load_json`, whose raise line does not contain the word "overrides" and so is not listed by this grep)

Expected hits (record the actual file:line lines):

1. `01-jgs-se-knowledge-packs.yaml:15:version: "1.20.0"` and `catalog.yaml:13:    version: "1.20.0"`
2. Four lines: `generate_capability_map.py:39` and `:88`, `check_classification_rules.py:28` and `:99` (forbid list define plus reject loop in each file)
3. Two lines at `generate_capability_map.py:269` and `:275` (cluster-name pipe escape in `render_md`)
4. `check_classification_rules.py:257` (`live_on = live.get("generated_on")`), `:258` (`if live_on != generated_on:`), `:261` (fail message naming the date drift)
5. The md compare block: `generate_capability_map.py:361` / `:367` FAIL paths, the stale-md FAIL print, and `:376` `PASS: capability-pack-map.md is fresh`

- [ ] **Step 8: Gate the run**

Every expectation in Steps 2-7 holds: return the ten receipt lines and the words `EVIDENCE_OK`. Anything else: stop, write nothing, report the failing command and output per the Failure policy.

---

### Task 2: Rewrite 21-IMPL_REVIEW.md in place (re-gate section on top, original preserved below)

**Files:**
- Modify: `.planning/phases/21-contract-rewrite-release-surfaces/21-IMPL_REVIEW.md`

**Interfaces:**
- Consumes: Task 1's ten receipt lines. If they are not in your brief, re-run Task 1 Steps 2-7 now with the same commands and record the outputs before editing.
- Produces: `21-IMPL_REVIEW.md` with `status: passed`, verdict `PASS_WITH_NOTES`, and a dated re-gate section; this is the file `master_flow.artifacts.impl_review` points at, so Task 3 may only run after this task verifies clean.

**Model:** standard

- [ ] **Step 1: Frontmatter edits** (four exact replacements)

Edit A, add the regate stamp and the historical note for `commits_reviewed`. Old:

```
phase: 21-contract-rewrite-release-surfaces
reviewed: 2026-08-27T21:05:00Z
mode: IMPL REVIEW (diff-scope: Phase 21 commits only)
base: c69da65
commits_reviewed:
```

New:

```
phase: 21-contract-rewrite-release-surfaces
reviewed: 2026-08-27T21:05:00Z
regated: 2026-09-14
mode: IMPL REVIEW (diff-scope: Phase 21 commits only; 2026-09-14 re-gate measured the live working tree on main)
base: c69da65
# commits_reviewed is the historical 2026-08-27 review scope, preserved as-is; the 2026-09-14 re-gate ran against the live tree, not this commit list
commits_reviewed:
```

Edit B, findings counts. Old:

```
findings:
  critical: 1
  warning: 3
  info: 2
  total: 6
status: issues_found
```

New:

```
findings:
  critical: 0
  warning: 0
  info: 2
  total: 2
status: passed
```

- [ ] **Step 2: Body verdict and re-gate section**

Replace the opening of the body. Old:

```
# Phase 21 Implementation Review

**Verdict: NEEDS_WORK**

One release-surface blocker:
```

New (insert the full re-gate section between the verdict line and the historical divider; the old narrative paragraph follows the divider):

```
# Phase 21 Implementation Review

**Verdict: PASS_WITH_NOTES** (re-gate 2026-09-14; supersedes NEEDS_WORK of 2026-08-27)

## Re-gate 2026-09-14

Fresh verification pass against live product truth: branch `main`, working tree clean of product edits, all four map/release gates re-run exit 0, tag and static checks confirm CR-01 and WR-01/02/03 closed. No network calls and no `gh` commands; the absent GitHub Release for v1.20.0 is documented from the X1 resolution (2026-09-14: P8 owns `/gsd-ship`), not probed.

### Evidence run (this session)

| # | Command | Expected | Actual (recorded) |
|---|---------|----------|-------------------|
| 1 | `python tooling/check_release.py` | exit 0; final line `RELEASE CHECK: PASS (v1.20.0 @ <sha>)`; no `[version]` failure lines; nested 5g replay prints its two map PASS lines | <paste exit code, banner, and the two 5g PASS lines from Task 1> |
| 2 | `python tooling/check_capability_map.py` | exit 0; output contains `TOTAL: 644` | <paste> |
| 3 | `python tooling/check_classification_rules.py` | exit 0; `PASS: classification rules OK` (generated_on fidelity silent on success) | <paste> |
| 4 | `python tooling/generate_capability_map.py --generated-on 2026-08-27 --check` | exit 0; byte-stable JSON plus md freshness PASS | <paste> |
| 5 | `git cat-file -t v1.20.0` then `git rev-list -n 1 v1.20.0` | `tag`; peel `ffe385abca97efc7a50b3939f930f78ec5666935` | <paste> |
| 6 | Static greps (file:line below) | website YAMLs at 1.20.0; WR-01/02/03 guards present | <paste grep hit lines> |

Command 6 evidence (current tree, file:line):

- `docs/products/website/01-jgs-se-knowledge-packs.yaml:15` and `docs/products/website/catalog.yaml:13` both `version: "1.20.0"`; enforced by `check_release.py` step 4a, silent on success (CR-01 surface truth)
- `tooling/generate_capability_map.py:39` and `:88`, `tooling/check_classification_rules.py:28` and `:99`: `_CLUSTER_NAME_FORBIDDEN` define plus reject loop (WR-01)
- `tooling/generate_capability_map.py:269` and `:275`: cluster-name pipe escape in `render_md` (WR-01 defense in depth)
- `tooling/check_classification_rules.py:257-261`: rules-vs-map `generated_on` fidelity fail path (WR-02)
- `tooling/generate_capability_map.py:361-376`: `--check` md freshness compare, fails closed on stale or missing md (WR-03)

### Findings closed

- **CR-01 CLOSED 2026-09-14**: tag `v1.20.0` is annotated and peels to `ffe385a` (the CR-01 fix commit), not the pre-fix `046799b`; both website YAMLs read `version: "1.20.0"`; command 1's step 4a now enforces the pair on every gate run.
- **WR-01 CLOSED 2026-09-14**: `_CLUSTER_NAME_FORBIDDEN` reject loops live in both validator paths; `render_md` pipe-escapes the cluster name.
- **WR-02 CLOSED 2026-09-14**: the `check_rules` fidelity block fails when rules `generated_on` differs from the live map.
- **WR-03 CLOSED 2026-09-14**: generator `--check` compares rendered md against disk and fails on drift.

### Still open (honest carry-forward)

- IN-01 and IN-02 remain informational, no action (see below).
- No GitHub Release exists for v1.20.0. By design: P8 owns `/gsd-ship` (X1 resolved 2026-09-14); the REL-21-02 tick carries the P8 tail.
- `gap_analysis` and `verify` were not run in this re-gate and have no artifacts; the phase `master_flow_state.json` leaves them open. P8's close owns them.

---

## Original review 2026-08-27 (preserved below; verdict superseded by the re-gate above; finding headings annotated CLOSED)

One release-surface blocker:
```

The `<paste>` cells take the literal recorded output lines from Task 1; every other line is written verbatim. The old narrative paragraph starting `One release-surface blocker:` stays intact below the divider.

- [ ] **Step 3: Annotate the four finding headings** (four exact replacements, one evidence line each; original body text below each heading stays intact)

CR-01 heading. Old:

```
### CR-01: v1.20.0 release surface misses the public-website product YAMLs (still 1.19.1)
```

New:

```
### CR-01: v1.20.0 release surface misses the public-website product YAMLs (still 1.19.1) [CLOSED 2026-09-14]

**Closed:** see Re-gate 2026-09-14 above: tag `v1.20.0` peels to `ffe385a`; both YAMLs at `version: "1.20.0"`; step 4a enforces the pair.
```

WR-01 heading. Old:

```
### WR-01: cluster_names is the remaining unvalidated, unescaped md cell class
```

New:

```
### WR-01: cluster_names is the remaining unvalidated, unescaped md cell class [CLOSED 2026-09-14]

**Closed:** generator `:39`/`:88` and check_rules `:28`/`:99` forbid lists plus reject loops; `render_md` `:269`/`:275` pipe escape.
```

WR-02 heading. Old:

```
### WR-02: map-replay date truth source is the map itself; rules-vs-map generated_on never cross-checked
```

New:

```
### WR-02: map-replay date truth source is the map itself; rules-vs-map generated_on never cross-checked [CLOSED 2026-09-14]

**Closed:** check_rules fidelity block `:257-261` fails on `generated_on` drift between rules and live map.
```

WR-03 heading. Old:

```
### WR-03: capability-pack-map.md has no freshness gate
```

New:

```
### WR-03: capability-pack-map.md has no freshness gate [CLOSED 2026-09-14]

**Closed:** generator `--check` md freshness compare `:361-376`; fails closed on stale or missing md.
```

IN-01 and IN-02 headings stay exactly as they are (still informational, no action).

- [ ] **Step 4: Verify the rewrite**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/jgs-se-knowledge-packs/.planning/phases/21-contract-rewrite-release-surfaces"
grep -c 'regated: 2026-09-14' 21-IMPL_REVIEW.md                 # expect 1
grep -c '^status: passed$' 21-IMPL_REVIEW.md                    # expect 1
grep -c 'CLOSED 2026-09-14' 21-IMPL_REVIEW.md                   # expect 8 (4 headings + 4 bullets)
grep -c 'Verdict: NEEDS_WORK' 21-IMPL_REVIEW.md                 # expect 0
grep -c 'Verdict: PASS_WITH_NOTES' 21-IMPL_REVIEW.md            # expect 1
grep -c 'critical: 0' 21-IMPL_REVIEW.md                         # expect 1
grep -c 'warning: 0' 21-IMPL_REVIEW.md                          # expect 1
grep -c 'total: 2' 21-IMPL_REVIEW.md                            # expect 1
grep -c 'CR-01: v1.20.0 release surface misses' 21-IMPL_REVIEW.md   # expect 1 (original heading preserved)
grep -c '### IN-01' 21-IMPL_REVIEW.md                           # expect 1
grep -c '### IN-02' 21-IMPL_REVIEW.md                           # expect 1
```

All counts must match. Any mismatch: fix the edit, rerun. When clean, report `IMPL_REVIEW_REGATED`.

---

### Task 3: Phase master_flow_state.json field-by-field transition

**Files:**
- Modify: `.planning/phases/21-contract-rewrite-release-surfaces/master_flow_state.json`

**Interfaces:**
- Consumes: Task 2 complete (the artifact the state file points at must carry the PASS verdict before the state says passed).
- Produces: phase ledger at the 19/20 shape minus gap/verify; Tasks 4-5 require this task done first (tick ordering).

**Model:** flash

- [ ] **Step 1: Apply the seven edits**

Edit 1, current gate. Old:

```
  "current_gate": "impl_review",
```

New:

```
  "current_gate": "gap_analysis",
```

Edit 2, completed array. Old:

```
  "completed": [
    "research",
    "plan",
    "plan_check",
    "plan_review",
    "execute"
  ],
```

New:

```
  "completed": [
    "research",
    "plan",
    "plan_check",
    "plan_review",
    "execute",
    "impl_review",
    "code_review",
    "integration_check",
    "security_audit"
  ],
```

Edit 3, blocker cleared. Old:

```
  "blocked_by": "impl_review",
```

New:

```
  "blocked_by": null,
```

Edit 4, verdicts (replace the stale needs_work line, add the three recorded review gates). Old:

```
    "impl_review": "needs_work:cr_01:_docs/products/website/01_jgs_se_knowledge_packs.yaml_still_version_1.19.1;_retag_after_bump"
  },
```

New:

```
    "impl_review": "passed_with_notes:regate_cr01_wr01_wr02_wr03_closed",
    "code_review": "passed_with_notes",
    "integration_check": "passed_with_notes",
    "security_audit": "passed:secured"
  },
```

Edit 5, artifacts (add the three on-disk review artifact paths). Old:

```
    "impl_review": ".planning/phases/21-contract-rewrite-release-surfaces/21-IMPL_REVIEW.md"
  },
```

New:

```
    "impl_review": ".planning/phases/21-contract-rewrite-release-surfaces/21-IMPL_REVIEW.md",
    "code_review": ".planning/phases/21-contract-rewrite-release-surfaces/21-CODE_REVIEW.md",
    "integration_check": ".planning/phases/21-contract-rewrite-release-surfaces/21-INTEGRATION_CHECK.md",
    "security_audit": ".planning/phases/21-contract-rewrite-release-surfaces/21-SECURITY_AUDIT.md"
  },
```

Edit 6, regate counter. Old:

```
  "regate_attempts": {
    "impl_review": 1
  },
```

New:

```
  "regate_attempts": {
    "impl_review": 2
  },
```

Edit 7, timestamp. Old:

```
  "updated_at": "2026-08-27T19:49:22.836Z",
```

New: the current UTC timestamp in the same format. Generate it first:

```bash
date -u +%Y-%m-%dT%H:%M:%S.000Z
```

and use that literal output as the new value. All other fields (`skipped`, `config_snapshot`, `execute`, `checkpoint_log`, `notes`, `started_at`, `milestone`, `failed`) stay unchanged.

- [ ] **Step 2: Verify the transition**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/jgs-se-knowledge-packs"
python - <<'EOF'
import json
p = ".planning/phases/21-contract-rewrite-release-surfaces/master_flow_state.json"
s = json.load(open(p, encoding="utf-8"))
assert s["current_gate"] == "gap_analysis"
for g in ("research", "plan", "plan_check", "plan_review", "execute",
          "impl_review", "code_review", "integration_check", "security_audit"):
    assert g in s["completed"], g
assert s["blocked_by"] is None
assert s["verdicts"]["impl_review"] == "passed_with_notes:regate_cr01_wr01_wr02_wr03_closed"
assert s["verdicts"]["code_review"] == "passed_with_notes"
assert s["verdicts"]["integration_check"] == "passed_with_notes"
assert s["verdicts"]["security_audit"] == "passed:secured"
assert s["regate_attempts"]["impl_review"] == 2
for k in ("code_review", "integration_check", "security_audit"):
    expected = "/21-" + k.upper() + ".md"
    assert s["artifacts"][k].endswith(expected), (k, s["artifacts"][k])
assert "gap_analysis" not in s["completed"] and "verify" not in s["completed"]
assert "gap_analysis" not in s["artifacts"] and "verify" not in s["artifacts"]
assert s["failed"] == []
print("MASTER_FLOW_OK")
EOF
grep -c 'needs_work' .planning/phases/21-contract-rewrite-release-surfaces/master_flow_state.json   # expect 0
grep -n '"active_phase"' .planning/master_flow_state.json                                           # expect 21, root pointer untouched
```

Expected: `MASTER_FLOW_OK`, count `0`, root pointer still `"active_phase": 21`. When clean, report `STATE_TRANSITIONED`.

---

### Task 4: REQUIREMENTS.md ticks (MAP-21-05 wording fix, REL-21-01, REL-21-02 ship tail)

**Files:**
- Modify: `.planning/REQUIREMENTS.md:18-23` and `.planning/REQUIREMENTS.md:54-56`

**Interfaces:**
- Consumes: Task 3 complete (state no longer says needs_work; ordering rule).
- Produces: ticked requirements that Task 5 mirrors into ROADMAP coverage.

**Model:** flash

- [ ] **Step 1: Tick MAP-21-05 with the optional-to-required wording fix.** Old (line 18):

```
- [ ] **MAP-21-05**: `docs/capability-map-CONTRACT.md` §4 names the generator as the refresh path; §8 residual is closed or reduced to documented optional note overrides only
```

New:

```
- [x] **MAP-21-05**: `docs/capability-map-CONTRACT.md` §4 names the generator as the refresh path; §8 residual is closed or reduced to the committed note-override file, which the generator requires (fails closed if missing)
```

- [ ] **Step 2: Tick REL-21-01, text unchanged.** Old (line 22):

```
- [ ] **REL-21-01**: `python tooling/check_release.py` PASS at frozen 63 catalog / 65 dirs; `map_version` is 1.20.0; no new packs
```

New:

```
- [x] **REL-21-01**: `python tooling/check_release.py` PASS at frozen 63 catalog / 65 dirs; `map_version` is 1.20.0; no new packs
```

- [ ] **Step 3: Tick REL-21-02 with the explicit P8 ship tail.** Old (line 23):

```
- [ ] **REL-21-02**: Version surfaces + CHANGELOG [1.20.0] record the generator honestly; annotated tag + GitHub Release when the product surface is ready
```

New:

```
- [x] **REL-21-02**: Version surfaces + CHANGELOG [1.20.0] record the generator honestly; annotated tag + GitHub Release when the product surface is ready (tag v1.20.0 on ffe385a; GitHub Release: P8 /gsd-ship)
```

- [ ] **Step 4: Traceability rows.** Old (lines 54-56):

```
| MAP-21-05 | Phase 21 | Pending |
| REL-21-01 | Phase 21 | Pending |
| REL-21-02 | Phase 21 | Pending |
```

New:

```
| MAP-21-05 | Phase 21 | Complete |
| REL-21-01 | Phase 21 | Complete |
| REL-21-02 | Phase 21 | Complete (gh release: P8) |
```

- [ ] **Step 5: Deliberate non-edit.** MAP-21-02 (line 15) keeps its already-ticked "optional note-override file" wording. It is a closed historical requirement; CONTRACT §4 and the generator are the source of truth for requiredness, and retroactively editing ticked requirements is worse than the stale adjective. Do not touch it. Recorded here so a reviewer does not re-flag it.

- [ ] **Step 6: Verify**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/jgs-se-knowledge-packs"
grep -n 'MAP-21-05\|REL-21-01\|REL-21-02' .planning/REQUIREMENTS.md
grep -c 'optional note overrides' .planning/REQUIREMENTS.md          # expect 0
grep -c '| Pending |' .planning/REQUIREMENTS.md                      # expect 0
grep -c 'GitHub Release: P8 /gsd-ship' .planning/REQUIREMENTS.md     # expect 1
grep -c 'requires (fails closed if missing)' .planning/REQUIREMENTS.md   # expect 1
```

Expected: all six mention lines either `- [x]` requirement lines or `Complete` traceability rows; MAP-21-05 line has no `optional`; REL-21-02 line carries the P8 tail. When clean, report `REQUIREMENTS_TICKED`.

---

### Task 5: ROADMAP.md ticks (plan boxes, progress row, coverage) plus final consistency sweep

**Files:**
- Modify: `.planning/ROADMAP.md:87, 91-92, 103, 113-115`

**Interfaces:**
- Consumes: Task 4 complete (ROADMAP coverage must never contradict REQUIREMENTS).
- Produces: the fully repaired phase 21 ledger surface; P8 inherits gap/verify, STATE, milestone narrative, `/gsd-ship`.

**Model:** flash

- [ ] **Step 1: Plan count line mirrors the phase 19/20 shape.** Old (line 87):

```
**Plans:** 2 plans
```

New:

```
**Plans:** 2/2 plans complete
```

This one small addition beyond the spec's enumerated list mirrors the phase 19/20 detail blocks and avoids an internal contradiction with the 2/2 progress row below it.

- [ ] **Step 2: Tick both plan boxes.** Old (lines 91-92):

```
- [ ] 21-01-PLAN.md — CONTRACT names generator; map envelope 1.20.0; release-gate replay
- [ ] 21-02-PLAN.md — Version trio + CHANGELOG [1.20.0]; annotated tag; gh release is /gsd-ship
```

New (tick only; the existing dash and text are preserved as written):

```
- [x] 21-01-PLAN.md — CONTRACT names generator; map envelope 1.20.0; release-gate replay
- [x] 21-02-PLAN.md — Version trio + CHANGELOG [1.20.0]; annotated tag; gh release is /gsd-ship
```

- [ ] **Step 3: Progress row plus the one-line note under the table.** Old (line 103 and the following heading):

```
| 21. CONTRACT rewrite + release surfaces | 0/2 | Not started | - |

## Coverage
```

New:

```
| 21. CONTRACT rewrite + release surfaces | 2/2 | Executed | - |

Phase 21 product gates PASS; impl_review re-gated 2026-09-14. Phase close (gap_analysis, verify, milestone ledger): P8.

## Coverage
```

"Executed" is honest; "Complete" is not, yet.

- [ ] **Step 4: Coverage rows.** Old (lines 113-115):

```
| MAP-21-05 | Phase 21 | Pending |
| REL-21-01 | Phase 21 | Pending |
| REL-21-02 | Phase 21 | Pending |
```

New:

```
| MAP-21-05 | Phase 21 | Complete |
| REL-21-01 | Phase 21 | Complete |
| REL-21-02 | Phase 21 | Complete (gh release: P8) |
```

- [ ] **Step 5: Deliberate non-edits (all P8).** ROADMAP overview prose with `map_version **1.19.1**` (line 5), the phase-list checkbox `- [ ] **Phase 21: CONTRACT rewrite + release surfaces**` (line 34), the Completed column `-`, STATE.md, MILESTONES/GAP.md, root pointer, GitHub Release. Leave all untouched.

- [ ] **Step 6: Verify ROADMAP and run the final consistency sweep**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/jgs-se-knowledge-packs"
grep -c '\[x\] 21-01-PLAN\|\[x\] 21-02-PLAN' .planning/ROADMAP.md    # expect 2
grep -c '2/2 | Executed' .planning/ROADMAP.md                        # expect 1
grep -c 're-gated 2026-09-14' .planning/ROADMAP.md                   # expect 1
grep -c '| Pending |' .planning/ROADMAP.md                           # expect 0
grep -c 'Complete (gh release: P8)' .planning/ROADMAP.md             # expect 1
grep -c '\- \[ \] \*\*Phase 21' .planning/ROADMAP.md                 # expect 1 (phase-list checkbox stays open for P8)
grep -c 'needs_work' .planning/phases/21-contract-rewrite-release-surfaces/master_flow_state.json   # expect 0
grep -c 'Verdict: NEEDS_WORK' .planning/phases/21-contract-rewrite-release-surfaces/21-IMPL_REVIEW.md   # expect 0
grep -c 'optional note overrides' .planning/REQUIREMENTS.md          # expect 0
python -c "import json; json.load(open('.planning/phases/21-contract-rewrite-release-surfaces/master_flow_state.json', encoding='utf-8')); print('JSON_OK')"
```

Expected: every count matches; `JSON_OK` prints. When clean, report `ROADMAP_TICKED` and `PHASE21_REGATE_DONE`.
