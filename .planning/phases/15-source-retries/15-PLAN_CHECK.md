# Phase 15 Plan Check

**Checked:** 2026-08-20
**Checker:** gsd-plan-checker
**Plan:** `.planning/phases/15-source-retries/15-01-PLAN.md`
**Research:** `15-RESEARCH.md` (host-200 for armypubs; plan overrides with ASAFM PDF 403)
**Patterns:** `15-PATTERNS.md`
**CONTEXT.md:** absent (discuss skipped)
**Phase goal:** Every carried source has dated evidence; AAF and Army CBA stay unused unless an in-source redistribution grant is quoted

**Goal-backward:** PASS
**Verdict:** PASS_WITH_FIXES

---

## Coverage table (VET-20-01..03)

IDs taken from live `.planning/REQUIREMENTS.md` and ROADMAP Phase 15.

| ID | Requirement (live SoT) | Task | Done condition | Status |
|----|------------------------|------|----------------|--------|
| VET-20-01 | Retry FUT-04 Army CBA Guide (ASAFM PDF). Dated evidence. Pack only with in-source grant; else FUT-04 deferred with fresh evidence (not a silent tick) | 15-01 Task 1 (tracer) | Dated 2026-08-20 DEFERRED in 15-RESEARCH + SOURCE-VETTING unless a verbatim in-source grant is quoted; no pack; GP-06 stays A-94-only | COVERED |
| VET-20-02 | Licence spot-check AAF Product Support Manager Guidebook + Software pathway. Quote grant or keep Excluded-pending / NOT yet vetted — do not use | 15-01 Task 2 | Excluded-pending row + Not-cleared bullet dated 2026-08-20; unused sentence kept; no AAF pack | COVERED |
| VET-20-03 | Optional ROSAP Rev E vs faa-std-025 Rev F — document only; no forced rebuild | 15-01 Task 2 | Document-only ROSAP note + GP-02 one-liner; PACK.yaml / packs/faa-std-025 untouched | COVERED |

Roadmap success criteria map 1 to VET-20-01, 2 to VET-20-02, 3 to VET-20-03, 4 to no packs (all three tasks + threat-model fence). PACK-20-01..03 stay Phase 16. Live VET-20 boxes stay unchecked (Task 3).

---

## Goal-backward

What must be TRUE after execute:

1. Army CBA has a 2026-08-20 retry record: quoted in-source grant or FUT-04 deferred with fresh 403-class evidence — not a silent tick, not a new Vetted Tier 1 row, not a new hard-Excluded cell.
2. AAF Product Support + Software pathway remain unused / Excluded-pending unless an opened-PDF grant is quoted.
3. ROSAP Rev E vs shipped faa-std-025 Rev F is documented only; no rebuild.
4. No pack is created or edited.
5. Published docs/SOURCE-VETTING.md stays locator-free (http count 0).
6. Live VET-20-01..03 and PACK-20-01..03 boxes stay unchecked; VET-20 lines carry 2026-08-20 parentheticals; STATE records Phase 15 deviations without touching YAML progress.

Plan Task 1 delivers 1+5 (FUT-04 slice), Task 2 delivers 2+3+5 (AAF/ROSAP + Phase 16 handoff), Task 3 delivers 6. All three plus files_modified / git diff packs empty deliver 4. Deferred-with-evidence is ROADMAP-legal, not a silent v1 cut. Quoted-grant flip is allowed only from an opened official PDF; still no pack this phase.

---

## First principles / inversion

Current assumptions challenged: (1) VET-20-01 requires a pack this phase — false: ROADMAP SC-4 and PACK-20-* are Phase 16. (2) A publications-host 200 is clearance — false: plan treats it as HTML, not a grant. (3) PATTERNS.md insert Vetted candidates is the right heading — false: these sources are not cleared; Not-cleared + Phase 16 handoff is the honest analog.

Guaranteed failure modes avoided: treating 403/404/301/Cloudflare or a landing-page 200 as Tier 1; copyright footer as grant; scheme strings in SOURCE-VETTING; creating packs/; ticking VET-20/PACK-20; git add -A; inventing a CBA/AAF pack.

Remaining risk: Task 1 automated python is not runnable as written (tab indent then SyntaxError). Executor following action still delivers the goal; a strict execute verify gate will fail until tabs are stripped.

---

## Dimension results

| Dimension | Result | Notes |
|-----------|--------|-------|
| 1 Requirement coverage | PASS | All three VET-20 IDs in plan requirements frontmatter; each has a covering task done condition. PACK-20 is Phase 16 and is only annotated as still open. |
| 2 Task completeness | PASS | 3 tasks; tracer + auto + auto each have files, action, verify, done, acceptance_criteria. Actions name exact headings, insert point, and strings. |
| 3 Dependency correctness | PASS | Single plan, depends_on empty, wave 1. |
| 4 Key links planned | PASS | Pointer paragraph to 15-RESEARCH.md; Phase 16 handoff table; REQUIREMENTS parentheticals must match register verdicts. |
| 5 Scope sanity | PASS | 3 tasks / 4 files_modified / estimate 24000 tokens vs 100000 budget (ratio 0.24, over_budget false, confidence low / uncalibrated, sample_count 0) |
| 6 Verification derivation | WARN | Truths are command-checkable and user-observable. Task 1 automated block does not compile (W1). Several automated conjuncts are already true on the pre-phase tree (W2, W3). |
| 7 Context compliance | SKIPPED | No CONTEXT.md. Locked constraints from ROADMAP + REQUIREMENTS + 15-RESEARCH user_constraints are honored. |
| 7b Scope reduction | PASS | Deferral is ROADMAP SC text, not a planner-invented v1 stub. Grant path is fully tasked if a PDF actually opens. |
| 7c Architectural tier | SKIPPED | No Architectural Responsibility Map in RESEARCH.md |
| 8 Nyquist | SKIPPED | No RESEARCH Validation Architecture section; no VALIDATION.md expected. Every task still has a fast automated python assert (T1 currently broken — W1). |
| 9 Cross-plan data contracts | PASS | One plan; single writer on SOURCE-VETTING then REQUIREMENTS/STATE. |
| 10 CLAUDE.md | SKIPPED | No CLAUDE.md |
| 11 Research resolution | PASS | No Open Questions section |
| 12 Pattern compliance | PASS | Link Policy / pointer / honest-deferral / dated-row / explicit-path staging match PATTERNS.md. Plan correctly does not insert a Vetted-candidates table or edit ROADMAP.md (stale PATTERNS rows). |
| Verify command format | WARN | No caret-anchored package-manager greps; no swallowed error defaults. Task 1 mixed tabs make the python -c payload a SyntaxError (W1). |
| files_modified vs tasks | PASS | SOURCE-VETTING.md, 15-RESEARCH.md, REQUIREMENTS.md, STATE.md. Matches all task files. No packs/. Task 3 leak-strip exception already listed at plan level. |
| Prohibitions | PASS | No packs/; no extract/catalog/vet_source/build_pack; no scheme strings in SOURCE-VETTING; no live VET-20/PACK-20 ticks; no git add -A; stay on main. |
| claim_verification | PASS | Present, non-empty, live-accurate on file/git rows. Curl HEADs are planner-session evidence; not re-run here. |
| Research/plan conflict | PASS (plan wins) | RESEARCH Fresh Evidence curled the Army publications host 200. Plan claim_verification + Task 1 re-fetch the ASAFM PDF (403 Akamai). Plan already tells the executor not to treat host-200 as a grant. |

### Smart-zone estimate

| Plan | estimate.tokens | budget | over_budget | plan confidence | tool confidence |
|------|-----------------|--------|-------------|-----------------|-----------------|
| 15-01 | 24000 | 100000 | false | low | low (sample_count: 0) |

### Dimension 8: Nyquist Compliance

SKIPPED (no Validation Architecture in 15-RESEARCH.md). Advisory task table:

| Task | Plan | Wave | Automated Command | Status |
|------|------|------|-------------------|--------|
| T1 FUT-04 tracer | 15-01 | 1 | python asserts v1.19.1 heading order + pointer + FUT-04/DEFERRED/2026-08-20 + http absent + 403 in RESEARCH | FAIL SyntaxError (tabs) |
| T2 AAF + ROSAP | 15-01 | 1 | python asserts Phase 16 handoff order + unused sentence + ROSAP/no-rebuild + 2x NO-GO + AAF row dated | compiles |
| T3 REQUIREMENTS/STATE | 15-01 | 1 | python asserts three open VET-20 lines dated, three open PACK-20, STATE Phase 15 bullet, http absent | compiles |

Sampling: Wave 1: 2/3 runnable automated verifies. Wave 0 N/A.
Overall: SKIPPED as dimension; W1 remains.

---

## Targeted checks (orchestrator musts)

| Check | Result |
|-------|--------|
| Every VET-20 + success criterion covered | PASS |
| claim_verification present | PASS (non-empty; live file/git rows re-measured 2026-08-20) |
| No pack builds | PASS (files_modified docs+planning only; git diff packs empty required) |
| Deferred-with-evidence allowed | PASS (explicit default path; ROADMAP-legal) |
| Zero-URL SOURCE-VETTING | PASS (whole-file http ban in action + verify) |
| No tick live VET boxes | PASS (Task 3 forbids; verify asserts unchecked VET-20 and PACK-20) |
| files_modified complete | PASS (four paths; matches task files) |

### claim_verification accuracy (live re-run, 2026-08-20)

File/git rows only (no application / no curl).

| Claim | Live | Status |
|-------|------|--------|
| Branch is main | main | Accurate |
| No 15-CONTEXT.md | phase dir has RESEARCH, PATTERNS, PLAN, master_flow_state.json | Accurate |
| VET-20-01..03 unchecked | three open lines; PACK-20-01..03 also open | Accurate |
| grep -c http docs/SOURCE-VETTING.md | 0 | Accurate |
| No 2026-08-20 stamp in register yet | 0 | Accurate |
| Insert point Phase 11 then Def Stan | headings line 168 then 179 | Accurate |
| FUT-04 still 2026-08-17 DEFERRED | Not-cleared bullet line 158; GP-06 cell line 136 | Accurate |
| AAF Excluded-pending present | Excluded table line 87; Not-cleared bullet line 162 | Accurate |
| faa-std-025 pack is Rev F | packs/faa-std-025/PACK.yaml source_version Rev F; ROSAP rev E blocked at build | Accurate |
| No Army CBA / AAF / ROSAP pack dirs | none | Accurate |
| packs/ working tree clean | git diff --name-only -- packs/ empty | Accurate |
| 15-RESEARCH already contains 403 | WarU PSM 403 in Fresh Evidence | Accurate (also why T1 assert 403 in rs is weak — W2) |

Curl HEADs (ASAFM PDF 403, host 200, WarU 403, AAF 301, FAA 200, guessed Rev F 404, ROSAP 403) are planner-session claims. Not re-executed. No numeric conflict that required prescribing RESEARCH over the plan.

### Verify-command audit

| Task | Distinguishes pre-phase tree? | Residual |
|------|------------------------------|----------|
| T1 | Heading v1.19.1 retry is absent live — that conjunct would distinguish if the script compiled. | Tabs on assert/find lines then SyntaxError (W1). 403 in rs already true. GP-06 2026-08-20 suffix and packs-empty not asserted. |
| T2 | Phase 16 handoff heading is absent live — distinguishes. Unused sentence already present. | Hard-codes NO-GO count == 2 (breaks the allowed quoted-grant GO path). Does not uniquely require a new dated AAF Not-cleared bullet. |
| T3 | 2026-08-20 absent on live VET-20 lines; Phase 15 (2026-08-20) absent in STATE — distinguishes. | Does not assert STATE YAML frontmatter byte-stability (acceptance-only). |

---

## Findings

### Blockers (must fix)

None.

### Warnings (should fix; execution can proceed after a one-line detab)

**W1. [task_completeness / verify command] Task 1 automated python does not compile**
- Plan: 15-01 Task 1
- Eight lines after the Path reads are tab-indented. python -c payload raises IndentationError: unexpected indent. Execute verify cannot go green even when the action succeeded.
- Fix: detab those lines to column 0 (same as Task 2/3). Do not wrap them in a block.

**W2. [verification_derivation] Task 1 verify assert 403 in rs is already true; GP-06 dated suffix untested**
- Plan: 15-01 Task 1
- 15-RESEARCH Fresh Evidence already records WarU 403. Acceptance also wants GP-06 still A-94-only and 2026-08-20, plus packs empty.
- Fix: assert an ASAFM/FUT-04 execute-day marker in 15-RESEARCH; assert 2026-08-20 on the GP-06 table row; optionally git diff packs empty.

**W3. [verification_derivation] Task 2 verify leans on pre-existing unused sentence**
- Plan: 15-01 Task 2
- Unused sentence already exists at line 87/162. A skipped AAF Not-cleared bullet still passes. NO-GO count == 2 fights the action quoted-grant GO exception (unlikely on 403 HEADs).
- Fix: assert the v1.19.1 Not-cleared section contains both AAF and ROSAP plus 2026-08-20; allow GO on FUT-04/AAF only when 15-RESEARCH contains a verbatim grant quote.

**W4. [numeric/factual claim authority] 15-RESEARCH Army evidence is host-200; plan is PDF-403**
- File: 15-RESEARCH.md Fresh Evidence vs 15-01 claim_verification
- Plan is more current and already instructs the executor. RESEARCH is stale on the PDF path, not on the deferral decision.
- Fix: optional RESEARCH note that the publications host 200 is not the Cost Benefit Analysis PDF (still 403). Do not change verdicts.

### Non-issues (checked, not raised)

- claim_verification present, non-empty, live-accurate on file/git rows.
- VET-20 / PACK-20 boxes left unchecked — correct; verify / phase.complete owns ticks.
- Army CBA not hard-Excluded — reachability miss, same house pattern as Phase 10.
- No pack builds, no catalog, no extract.py / vet_source.py / build_pack.py.
- SPDX / scoped Edit (never wholesale Write) is in Task 1.
- Insertion point matches live file (after Phase 11 handoff / before Def Stan).
- PATTERNS Vetted candidates / ROADMAP.md rows correctly ignored.
- No CONTEXT.md / CLAUDE.md — those dimensions skipped, not failed.
- Idempotency (update in place) and concurrency (single writer) are explicit must_haves.
- Estimate over_budget is false; low confidence is uncalibrated (sample_count 0), not a defect.

---

## Structured issues

```yaml
issues:
  - plan: "15-01"
    dimension: task_completeness
    severity: warning
    task: 1
    description: "Task 1 automated python -c payload has tab-indented asserts and raises IndentationError, so the tracer verify cannot pass."
    fix_hint: "Detab the eight tab-prefixed lines in Task 1 automated block to match Task 2/3 column-0 style."

  - plan: "15-01"
    dimension: verification_derivation
    severity: warning
    task: 1
    description: "assert 403 in 15-RESEARCH.md is already true from the WarU host check; GP-06 2026-08-20 suffix and packs-empty are acceptance-only."
    fix_hint: "Assert an ASAFM/FUT-04 execute-day status line in 15-RESEARCH.md and 2026-08-20 on the GP-06 row."

  - plan: "15-01"
    dimension: verification_derivation
    severity: warning
    task: 2
    description: "Unused-sentence grep is satisfied by the v1.19.0 Excluded row; NO-GO count == 2 conflicts with the allowed quoted-grant GO path."
    fix_hint: "Scope asserts to the v1.19.1 Not-cleared / Phase 16 handoff sections; condition NO-GO vs GO on whether 15-RESEARCH quotes a grant."

  - plan: null
    dimension: numeric_factual_claim_authority
    severity: warning
    description: "15-RESEARCH Fresh Evidence records armypubs host 200; plan claim_verification records ASAFM PDF 403. Plan is authoritative and already warns against treating host-200 as a grant."
    fix_hint: "Optional: stamp RESEARCH that host-200 is not PDF clearance. Do not flip FUT-04 to cleared."
```

---

## Recommendation

0 blockers. 4 warnings. Verdict **PASS_WITH_FIXES**.

Highest-leverage pre-execute nit: detab Task 1 automated verify so the tracer gate can run. Remaining warnings are verify-strictness and RESEARCH host-vs-PDF hygiene, not missing VET-20 coverage.

Plans reduce 0 locked user decisions (no CONTEXT.md). No phase split required. Goal will be achieved if the executor follows the actions; fix W1 before or during execute so verify is not a false fail.

**Verdict:** PASS_WITH_FIXES

