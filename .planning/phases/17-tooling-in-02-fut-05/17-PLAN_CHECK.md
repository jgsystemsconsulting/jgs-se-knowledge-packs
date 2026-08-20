# Phase 17 Plan Check

**Checked:** 2026-08-20
**Checker:** gsd-plan-checker
**Plan:** `.planning/phases/17-tooling-in-02-fut-05/17-01-PLAN.md`
**Research:** `17-RESEARCH.md` (HIGH; overlap checker + honest FUT-05 residual)
**Patterns:** `17-PATTERNS.md` (basename scan + whitelist; in-process gate wire; FUT-05 honesty)
**CONTEXT.md:** absent (discuss skipped)
**Phase goal:** Release tooling catches multi-pack collisions and can regenerate mechanical map fields without agent judgment (or documents the residual honestly)

**Goal-backward:** PASS
**Verdict:** PASS_WITH_FIXES

---

## Coverage table (TOOL-20-01..03)

IDs taken from live `.planning/REQUIREMENTS.md` and ROADMAP Phase 17.

| ID | Requirement (live SoT) | Task | Done condition | Status |
|----|------------------------|------|----------------|--------|
| TOOL-20-01 | Minimal committed overlap checker under tooling/ (stdlib Python preferred) | 17-01 Task 1 (tracer) | check_overlap.py exists, stdlib, WHITELIST covers live ch01-introduction.md, exits 0 | COVERED |
| TOOL-20-02 | Wire TOOL-20-01 into release path; thresholds documented; no false-fail on shared support files | 17-01 Task 1 (wire) + Task 2 (doc + assert) | in-process check_overlap.main(); CONTRACT scan/threshold/whitelist; support files out of scope via packs/*/chapters/*.md | COVERED |
| TOOL-20-03 | Deterministic map generator for mechanical fields, or largest deterministic slice + residual agent procedure in CONTRACT | 17-01 Task 3 | CONTRACT residual names mechanical slice already in check_capability_map.py and refuses a byte-stable full generator; no new generator file | COVERED (honest-residual branch) |

Roadmap SC 1 maps to TOOL-20-01, 2 to TOOL-20-02, 3 to TOOL-20-03 residual branch. Live TOOL-20 boxes stay unchecked (verify / phase.complete owns ticks). Phase 18 still owns map_version / v1.19.1 surface.

---

## Goal-backward

What must be TRUE after execute:

1. `python tooling/check_overlap.py` exits 0; the only live chapter-basename collision is `ch01-introduction.md` across `dau-se-guidebook`, `nasa-npr-7123`, `nasa-system-safety` and that name is in WHITELIST.
2. `check_release.py` imports check_overlap and calls check_overlap.main() in-process (no subprocess) and fail()s on non-zero; `python tooling/check_release.py` still prints RELEASE CHECK: PASS.
3. Overlap thresholds and the intentional-shared-name whitelist are documented (module docstring plus CONTRACT); support files under pack root are excluded by scanning only packs/*/chapters/*.md.
4. TOOL-20-03 residual is honest in CONTRACT: mechanical slice is check_capability_map uniqueness/staleness/existence/thresholds; cluster assignment and note fields remain agent procedure; no byte-stable full-map generator is claimed.
5. `python tooling/check_capability_map.py` still PASS; schema_version 2; map_version stays 1.19.0; catalog 63 / packs dirs 65.
6. Version trio stays 1.19.0; no new version heading; no new git tag; `.github/workflows/validate.yml` is not given a repo-Python step.
7. Live REQUIREMENTS.md TOOL-20-01..03 boxes remain unchecked.
8. No new Python dependencies; stdlib only; no packs/ invented or rebuilt.

Task 1 delivers 1+2+8 (checker + release wire). Task 2 delivers 3. Task 3 delivers 4-7. Honest residual is ROADMAP-legal TOOL-20-03 else-branch, not a planner-invented v1 stub. Full generator is explicitly forbidden unless proven — and research says it is not feasible.

---

## First principles / inversion

Current assumptions challenged: (1) TOOL-20-03 requires a new generate_capability_map.py this phase — false: ROADMAP SC-3 / REQUIREMENTS allow largest deterministic slice + CONTRACT residual. (2) Wiring as a documented mandatory step without check_release import is enough — plan correctly chooses the stronger in-process call already used for the map gate. (3) PATTERNS rglob("chapters/*.md") must be copied verbatim — plan glob("*/chapters/*.md") is the stated scan scope; live measurement shows identical 536/534 / one dup. (4) CI must run the new checker — false: repo policy is local/trusted Python; CI never execs checked-out repo code.

Fundamental truths: release path already composes sibling checkers via in-process main(); one live basename collision is semantically correct and must not false-fail; cluster assignment / note cannot be regenerated from committed inputs alone.

Guaranteed failure modes avoided: inventing a full FUT-05 generator; skipping the release wire; adding pip/pytest; ticking TOOL-20 boxes; bumping 1.19.0; adding a CI repo-Python step; scanning pack-root support files; git add -A.

Remaining risk: Task 3 automated CI-fence assert uses a contiguous phrase that is line-wrapped in live validate.yml, so the closing verify will false-fail unless the executor detunes that one assert (must-NOT edit validate.yml). See W1.

---

## Dimension results

| Dimension | Result | Notes |
|-----------|--------|-------|
| 1 Requirement coverage | PASS | All three TOOL-20 IDs in plan requirements frontmatter; each has a covering task done condition. TOOL-20-03 takes the honest-residual branch allowed by ROADMAP SC-3. |
| 2 Task completeness | PASS | 3 tasks; tracer + auto + auto each have files, action, verify, done. Actions name exact files, insert point (before current 5d map block), WHITELIST contents, scan glob, in-process import shape. All automated python -c payloads compile (tabs=0). |
| 3 Dependency correctness | PASS | Single plan, depends_on empty, wave 1. Sequential tasks in one plan; Task 2/3 edit CONTRACT after Task 1 exists. |
| 4 Key links planned | PASS | check_release.py to check_overlap.py via import + main(); CONTRACT to overlap whitelist/scan; CONTRACT to check_capability_map residual. Tasks implement the wiring, not just artifact creation. |
| 5 Scope sanity | PASS | 3 tasks / 4 files_modified / estimate 32000 tokens vs 100000 budget (ratio 0.32, over_budget false, confidence low / uncalibrated, sample_count 0) |
| 6 Verification derivation | WARN | Truths are command-checkable. T1/T2 automated conjuncts distinguish the pre-phase tree. T3 CI-fence contiguous-phrase assert cannot pass on live validate.yml and the plan forbids editing that file (W1). |
| 7 Context compliance | SKIPPED | No CONTEXT.md. Locked constraints from ROADMAP + REQUIREMENTS + 17-RESEARCH are honored (stdlib; in-process wire; honest residual; no version bump; no CI repo-Python). |
| 7b Scope reduction | PASS | Honest FUT-05 residual is ROADMAP SC-3 text, not a planner-invented v1 stub. Overlap checker + release wire are tasked in full. |
| 7c Architectural tier | PASS | RESEARCH Architectural Responsibility Map assigns overlap detection, map validation, and release composition to Tooling (Python stdlib). Tasks write tooling/check_overlap.py, wire tooling/check_release.py, and document in CONTRACT — no client/API mis-tier. |
| 8 Nyquist | SKIPPED | No RESEARCH Validation Architecture section; no VALIDATION.md expected. Every task still has a fast automated python assert (T3 CI conjunct broken — W1). |
| 9 Cross-plan data contracts | PASS | One plan; exclusive ownership of check_overlap.py; single writer on check_release.py then CONTRACT.md. No conflicting transforms. |
| 10 CLAUDE.md | SKIPPED | No CLAUDE.md |
| 11 Research resolution | PASS | No Open Questions section |
| 12 Pattern compliance | PASS | PATTERNS.md has no File Classification table. Plan follows overlap whitelist, in-process check_release wire (analog check_capability_map.main()), FUT-05 honesty, stdlib-only, no pytest suite (PATTERNS optional Wave 0 test file correctly omitted). Scan uses glob("*/chapters/*.md") instead of PATTERNS rglob; live dups identical — plan is the tighter scope. |
| Verify command format | PASS (compile) / WARN (T3 CI phrase) | No caret-anchored package-manager greps; no swallowed-error defaults. All six python -c payloads compile. T3 asserts a contiguous header string that is wrapped in the file (W1). |
| files_modified vs tasks | PASS | tooling/check_overlap.py, tooling/check_release.py, docs/capability-map-CONTRACT.md, 17-01-SUMMARY.md. Matches all task files. No packs/, no validate.yml, no version trio. |
| Prohibitions | PASS | No full generator; no subprocess; no pip/pytest; no CI repo-Python step; no version/tag bump; no live TOOL-20 ticks; no packs invented; no git add -A; stay on main. |
| claim_verification | PASS (file/git rows) / WARN (CI phrase) | Present, non-empty, live-accurate on overlap-absent, versions, boxes, tags, catalog/dirs, collisions, support-file counts. CI header claim quotes a contiguous phrase that is line-wrapped (W1 / W2). CONTRACT line count 113 vs live 112 (N1). |
| Research/plan conflict | PASS (plan wins) | RESEARCH/PATTERNS skeleton uses rglob; plan specifies glob("*/chapters/*.md") as the contract scan. Live measurement: same 536 files / 534 unique / one dup. Plan is authoritative for execute. |

### Smart-zone estimate

| Plan | estimate.tokens | budget | over_budget | plan confidence | tool confidence |
|------|-----------------|--------|-------------|-----------------|-----------------|
| 17-01 | 32000 | 100000 | false | low | low (sample_count: 0) |

Uncalibrated (sample_count 0) — weigh task/file thresholds more heavily. Those are inside target (3 tasks, 4 files).

### Dimension 8: Nyquist Compliance

SKIPPED (no Validation Architecture in 17-RESEARCH.md; VALIDATION.md absent as expected). Advisory task table:

| Task | Plan | Wave | Automated Command | Status |
|------|------|------|-------------------|--------|
| T1 overlap tracer | 17-01 | 1 | check_overlap.py && check_release.py + import/main() asserts | compiles; distinguishes (overlap file + import absent live) |
| T2 whitelist assert | 17-01 | 1 | overlap cmd + WHITELIST/dups assert + CONTRACT greps | compiles; distinguishes (CONTRACT lacks check_overlap live) |
| T3 FUT-05 residual | 17-01 | 1 | both gates + version trio + FUT-05 in CONTRACT + boxes open + CI fence | compiles; FUT-05 conjunct distinguishes; CI contiguous phrase false-fails (W1) |

Sampling: Wave 1: 3/3 have automated verify. Wave 0 N/A.
Overall: SKIPPED as dimension; W1 remains.

---

## Targeted checks (orchestrator musts)

| Check | Result |
|-------|--------|
| TOOL-20-01..03 covered | PASS (01 checker, 02 wire+docs, 03 honest residual) |
| Release wire present | PASS (in-process check_overlap.main() before map block; no subprocess) |
| Full FUT-05 regen invented? | PASS — forbidden (no generator file; CONTRACT must refuse byte-stable regen) |
| Non-stdlib deps? | PASS — forbidden (stdlib only; no pip/pytest) |
| claim_verification present | PASS (non-empty; live file/git rows re-measured 2026-08-20) |
| Boxes stay open | PASS (Task 3 forbids ticks; verify asserts three open TOOL-20 boxes) |
| files_modified complete | PASS (four paths; matches task files) |
| CI repo-Python step | PASS — forbidden (validate.yml unnamed; must-NOT edit) |

### claim_verification accuracy (live re-run, 2026-08-20)

File/git rows only (no application).

| Claim | Live | Status |
|-------|------|--------|
| Branch is main | main | Accurate |
| No 17-CONTEXT.md | phase dir has RESEARCH, PATTERNS, PLAN, master_flow_state.json | Accurate |
| check_overlap.py absent | no such file | Accurate |
| map_version 1.19.0 / schema 2 / 644 entries | 1.19.0 / 2 / 644 | Accurate (map gate stdout not re-run) |
| check_release imports map at ~217; no overlap import | import check_capability_map present; import check_overlap absent; sys.path.insert present | Accurate |
| Live chapter-basename collisions | glob */chapters/*.md: 536 files / 534 unique / exactly ch01-introduction.md in three named packs | Accurate |
| Support files at pack root | glossary/patterns/cheatsheet 63 each | Accurate |
| Version trio 1.19.0 | plugin / CHANGELOG top / RELEASE-INFO all 1.19.0 | Accurate |
| TOOL-20-01..03 unchecked | three open requirement lines; traceability Pending | Accurate |
| CI never execs repo Python | header wraps never then executes checked-out repository code; check_overlap absent; check_capability_map absent | Phrase split — W2 |
| Tags | v1.19.0 only | Accurate |
| Catalog / dirs | 63 catalog / 65 dirs | Accurate |
| SOURCE-VETTING http | 0 | Accurate |
| CONTRACT has no FUT-05 residual yet | 112 lines (plan said 113); no FUT-05 heading; no check_overlap | Line-count off by 1 (N1); residual claim accurate |
| estimate-calibration | factor 1, sample_count 0, confidence low | Accurate (estimate-check --calibrated) |

### Verify-command audit

| Task | Distinguishes pre-phase tree? | Residual |
|------|------------------------------|----------|
| T1 | import check_overlap / check_overlap.main() / file contents absent live — distinguishes. | Does not assert WHITELIST is a module-level set (Task 2 does). Does not assert no subprocess. |
| T2 | CONTRACT lacks check_overlap / whitelist live — distinguishes. Runnable dups=={ch01-introduction.md} is already true once the module exists. | Relies on Task 1 having exported WHITELIST (action requires it). |
| T3 | FUT-05 absent from CONTRACT live — distinguishes. Version trio / boxes / map_version already 1.19.0 (must stay). | Contiguous CI phrase never executes checked-out repository code is false on live file and stays false because validate.yml must not be edited (W1). word agent in CONTRACT already true (se-agents / agent consumption). |

---

## Findings

### Blockers (must fix)

None.

Plan does not invent a full FUT-05 generator, does not skip the release wire, and does not add non-stdlib deps.

### Warnings (should fix; execution can proceed after one assert detune)

**W1. [verification_derivation] Task 3 CI-fence assert cannot pass on live validate.yml**
- Plan: 17-01 Task 3 automated verify
- Asserts the contiguous string `never executes checked-out repository code` in validate.yml. Live header is line-wrapped after `never`. Contiguous substring is absent. Action forbids editing `.github/workflows/validate.yml`. Closing verify false-fails even when the FUT-05 residual and both gates are correct.
- Fix: Assert `executes checked-out repository code` and `never` separately (or the first-comment `never` line plus the wrapped continuation), plus keep `check_overlap` absent. Do **not** unwrap the YAML comment.

**W2. [numeric/factual claim authority] claim_verification quotes the same contiguous CI phrase**
- File: 17-01-PLAN.md claim_verification CI row
- Planner intent (CI does not exec repo Python; overlap/map unnamed) is live-true. The quoted contiguous string is not.
- Fix: optional claim_verification wording. Plan is still authoritative that CI must not gain a repo-Python step.

### Non-issues (checked, not raised)

- claim_verification present, non-empty, live-accurate on file/git rows except the wrapped CI phrase and CONTRACT 113 vs 112.
- TOOL-20 boxes left unchecked — correct; verify / phase.complete owns ticks.
- No packs/, no catalog, no version trio bump, no v1.19.1 tag, no pytest, no generator file.
- In-process wire matches check_capability_map analog at check_release.py:215-222.
- WHITELIST of the single live intro collision matches glob measurement.
- Support-file exclusion by chapters/ glob is by design (63 glossary/patterns/cheatsheet at pack root).
- PATTERNS optional tests/test_overlap.py correctly omitted.
- RESEARCH rglob vs plan glob: same live dups; plan tighter.
- No CONTEXT.md / CLAUDE.md — those dimensions skipped, not failed.
- Idempotency (update in place) and concurrency (single writer) are explicit must_haves.
- Estimate over_budget is false; low confidence is uncalibrated (sample_count 0), not a defect.
- Task type tracer accepted by verify.plan-structure (valid true, 0 errors).
- Architectural Responsibility Map honored (tooling tier).
- Link policy: CONTRACT currently 0 http; action forbids scheme strings (automated verify greps SOURCE-VETTING, not CONTRACT — residual only).

---

## Structured issues

```yaml
issues:
  - plan: "17-01"
    dimension: verification_derivation
    severity: warning
    task: 3
    description: "Task 3 automated verify asserts contiguous 'never executes checked-out repository code' in validate.yml, but the live header wraps after 'never'. Action forbids editing that file, so the closing verify false-fails on a correct execute."
    fix_hint: "Split the CI assert: 'never' present and 'executes checked-out repository code' present; keep check_overlap absent. Do not edit validate.yml."

  - plan: "17-01"
    dimension: numeric_factual_claim_authority
    severity: warning
    description: "claim_verification CI row quotes the same contiguous never-executes phrase. Live file has the wrap. Intent (CI does not exec repo Python) is true."
    fix_hint: "Optional: reword the claim_verification observed cell. Do not add a CI repo-Python step."
```

---

## Recommendation

0 blockers. 2 warnings. Verdict **PASS_WITH_FIXES**.

Highest-leverage pre-execute nit: detune Task 3 CI-fence assert to the wrapped header so the closing gate can run. Remaining warning is claim_verification wording, not missing TOOL-20 coverage.

Plans reduce 0 locked user decisions (no CONTEXT.md). No phase split required. Goal will be achieved if the executor follows the actions; fix W1 before or during execute so Task 3 verify is not a false fail.

**Verdict:** PASS_WITH_FIXES
