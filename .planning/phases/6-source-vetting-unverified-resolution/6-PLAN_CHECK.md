# Phase 6 Plan Check

**Phase:** 6-source-vetting-unverified-resolution
**Plans checked:** 1 (`6-01-PLAN.md`)
**Checked:** 2026-08-16
**Method:** Goal-backward verification against ROADMAP Phase 6 goal + SC1-SC3, REQUIREMENTS VET-01/VET-02, `docs/SOURCE-VETTING.md` Link Policy + date-stamp house style, `6-RESEARCH.md` (authoritative verdicts), REL-1x pack arithmetic (56 + 7 = 63), and live re-measurement of every `claim_verification` row.

**Verdict:** PASS_WITH_FIXES

The four edit tasks will record the research verdicts into SOURCE-VETTING / REQUIREMENTS / ROADMAP / STATE and will achieve VET-01, VET-02, and SC1-SC3 if the executor follows the actions. Link Policy (zero `http` in `docs/SOURCE-VETTING.md`) is tasked, not just listed. GP-08 is an explicit descope, not a silent v1 cut, and the 63-pack target is the correct 56 + 7 arithmetic. Several verify blocks cannot measure what `<done>` claims -- one is a syntax error (false-fail), others false-pass. Fix those before execute if the verifier scores the written commands strictly. Do not treat this as a rewrite.

---

## Goal-backward trace

Phase goal: *Every v1.18 candidate has a definitive tier decision; newly dead/gated sources permanently excluded.*

| Success criterion | Required truth | Covering task | Provably delivered? |
|---|---|---|---|
| SC1 / VET-01 -- All 5 UNVERIFIED items resolved to Tier 1/2/Excluded with evidence (URL + licence statement) | MIL-STD-40051, NASA SP-7084, VV&A RPG, MIL-STD-881F, AFOTEC each have a dated record + licence evidence; URLs live in `6-RESEARCH.md` (Link Policy) | Task 1 (4 Tier-1 rows) + Task 2 (AFOTEC Excluded) | **Yes, on the Phase-2 BL-01(b) reading.** Task 1 writes four dated Vetted rows with 17 U.S.C. section 105 / NTRS / DIST-A caveats. Task 2 writes AFOTEC Excluded. Pointer paragraph sends URLs to `6-RESEARCH.md`. A verifier that demands URLs *inside* SOURCE-VETTING will still fail SC1 -- that is the Link Policy trade, not an unfixed gap. |
| SC2 / VET-02 -- DoD DAG, CMU SEI, and any failing candidates in the Excluded table with dated rationale | Three new dated Excluded rows | Task 2 | **Yes in the action.** Rows, date-stamp convention, and no-URL rule are specified. Verify is an OR-grep and does not assert the date-stamp increment -- see W2. |
| SC3 -- Each GP pack candidate confirmed or dropped; stretch (GP-08) decided | GP-01..GP-07 stay in the build list with recorded caveats; GP-08 struck + Out-of-Scope + NPR 7150.2 / NASA-STD-8739.8 alternative | Tasks 1, 3, 4 | **Yes for GP-01..05, GP-07, GP-08.** GP-08 strike + Phase 7 = 7 packs + STATE 63 is tasked. **Partial for GP-06** (`federal-bca` / OMB A-94 + Army CBA): no RESEARCH section, no SOURCE-VETTING row, kept in Phase 7 only by not being dropped. Gap-report already marked it live Tier 1 (not UNVERIFIED). See W6. |
| Link Policy -- no source-material URL in packs **or the docs** | `grep -c http` on `docs/SOURCE-VETTING.md` stays 0 | Tasks 1, 2, 5 | **Yes.** Live count is already 0. Actions forbid `http`/`https`. `17 U.S.C. section 105` is plain text. |
| REL-1x arithmetic -- GP-08 strike must not invent a 64-pack or leave 7-8 as the target | 56 shipped + 7 GP = 63; Phase 7 requirements drop GP-08 | Task 4 + Task 5 | **Yes on STATE + Phase 7 Details.** 56 + 7 = 63 is correct. REL-1x-01/02 do not hard-code 64. Overview bullet (ROADMAP:77 `GP-01..GP-08`) and `MILESTONES.md` `7-8 Tier-1` are not tasked -- see W3. |
| Date-stamp house style | `(Verified 2026-08-14.)` on new Excluded rows; v1.18 Vetted rows dated the same way | Tasks 1, 2 | **Yes for Excluded** (matches live table). **Extra on Vetted** -- live v1.17 Vetted table has **no** date stamps. Harmless inconsistency, not a contradiction. |

Requirements frontmatter: `[VET-01, VET-02]` -- both present. No ROADMAP requirement ID is missing from the plan.

`claim_verification` is present (7 rows). Six match the live tree. One command path is wrong (W5).

---

## Dimension results

| Dim | Result | Notes |
|---|---|---|
| 1 Requirement coverage | PASS with gap | VET-01 and VET-02 claimed and tasked. SC3 GP-06 has no recorded verdict (W6). |
| 2 Task completeness | PASS | `verify.plan-structure`: 5 auto tasks, all have Files + Action + Verify + Done. Task 1 `<automated>` is not parseable bash (W1). |
| 3 Dependencies | PASS | Single plan, `depends_on: []`, wave 1. Intra-plan order 1->2 (same file, sequential append) -> 3 -> 4 -> 5 is acyclic. |
| 4 Key links | PASS | `6-RESEARCH.md` -> SOURCE-VETTING pointer is in Task 1 action + `must_haves.key_links`. REQUIREMENTS GP-01/GP-03/GP-08 notes are wired to research sections. ROADMAP Phase 7 / STATE 63 are wired, not just listed. |
| 5 Scope sanity | WARN | 5 tasks (threshold 5+). 4 files. `estimate-check --calibrated` on 45000: budget 100000, ratio 0.45, `over_budget: false`, `confidence: low` (`sample_count: 0`; plan says `med`). Do not split: Tasks 1-2 edit the same SPDX-headed file; Task 5 is a read-only sweep. |
| 6 Verification derivation | WARN | `must_haves` truths are user-observable. Several automated blocks cannot distinguish the required edit from the pre-phase tree (W1-W4). |
| 7 Context compliance | SKIPPED | No CONTEXT.md (discuss skipped). |
| 7b Scope reduction | PASS | GP-08 descope is explicit in RESEARCH section 4 and tasked as strike + Out-of-Scope + alternatives. Not a silent v1/static stub. |
| 7c Architectural tier | SKIPPED | No Architectural Responsibility Map in `6-RESEARCH.md`. |
| 8 Nyquist | SKIPPED | No VALIDATION.md; `nyquist_audit` skipped in phase `master_flow_state.json`; RESEARCH has no Validation Architecture section. |
| 9 Cross-plan contracts | PASS | Single plan; no conflicting transforms. |
| 10 CLAUDE.md | SKIPPED | No `./CLAUDE.md`. |
| 11 Research resolution | PASS | No Open Questions section. |
| 12 Pattern compliance | SKIPPED | No PATTERNS.md. |

---

## Targeted checks (orchestrator brief)

### SC to task mapping

| SC | Planned delivery | Gap |
|---|---|---|
| 5 UNVERIFIED -> evidence rows | Task 1: 40051-2C, SP-7084, VV&A (chapter-wise), 881F. Task 2: AFOTEC Excluded | None. NASA SP-7084 is correctly recorded even though it is not a GP pack. |
| Rule-outs -> Excluded table | Task 2: AFOTEC, DoD DAG, CMU SEI after the DAU/WARU row, `(Verified 2026-08-14.)` | Verify is one OR-grep (W2). |
| GP decisions | Task 3: GP-08 strike + Out-of-Scope + NPR/8739.8; GP-01 chapter-wise; GP-03 8.02. Task 4: Phase 7 = GP-01..07, STATE 63 | GP-06 never confirmed in SOURCE-VETTING (W6). |

### Link Policy -- no source URLs into SOURCE-VETTING

Live `grep -c http docs/SOURCE-VETTING.md` = **0**. Task 1/2 actions forbid `http`/`https`. Task 1 says the DOT&E fallback URL lives only in `6-RESEARCH.md`. Task 5 asserts `test "$(grep -c 'http' ...)" = "0"`. T-6-01 mitigates Information Disclosure the same way.

Residual: Task 1 closing note includes the bare host `swehb.nasa.gov` (no scheme). `grep http` will not catch it. Not a URL under the Phase-2 reading; leave it, or say "NASA SWEHB wiki" if the executor wants zero locators in `docs/`.

`verify.plan-structure` region-scope warnings (#968) on the file-wide `http` bans are **false positives** -- no sibling task requires an `http` string in that file.

### Date-stamp conventions

Live Excluded rows use `(Verified 2026-08-14.)` (7 stamps today). Live v1.17 Vetted table has **none**. Plan applies the Excluded convention to both new Vetted rows and new Excluded rows. Correct for SC2. Extra dating on v1.18 Vetted is acceptable.

Task 5 action: expect pre-phase count + 10 = **17**. Task 1/2/5 verifies never assert `= 17` or `-ge 17`. `grep -c` alone exits 0 on the existing 7. See W2.

### GP-08 strike vs REL-1x / 63-pack arithmetic

- Shipped now: 56 (54 catalog + 2 signposts). Target if GP-08 stays: 63-64. Target if GP-08 drops: **63**. Plan writes that.
- REL-1x-01/02 and Phase 9 SC do not hard-code 64. Safe.
- Task 4 updates Phase 7 **Details** Goal + Requirements and STATE pack target.
- Not updated: ROADMAP overview bullet line 77 (`Build GP-01..GP-08 packs`); `MILESTONES.md` line 18 (`7-8 Tier-1 packs`). Task 5 grep `63-64` or `7-8 packs` matches neither `7-8 public-domain packs` (live Goal, different suffix) nor hyphenated `7-8 Tier-1`. See W3.

### claim_verification accuracy (live re-run)

| Claim | Live | Status |
|---|---|---|
| RESEARCH Verdict/DEFER for 40051, SP-7084, VV&A, 881F, AFOTEC, DAG, SEI, GP-08; section 5 has 11 rows | Hits at 1a-1e, 2b, 2c, 4, section 5 header | Accurate |
| SOURCE-VETTING has `Vetted candidates (v1.17.0)` and `(Verified 2026-08-14.)` | Section at line 91; 7 dated **Excluded** rows; v1.17 Vetted rows undated | Accurate for existence; "rows carry" overstates the Vetted table |
| `grep -c http` = 0; section 105 is not a URL | 0 | Accurate |
| REQUIREMENTS GP-08 stretch line | line 87, exact text | Accurate |
| ROADMAP Phase 7 Goal 7-8 + Requirements include GP-08 | lines 97 and 99 | Accurate |
| STATE `63-64` | line 40 | Accurate |
| `sed -n '/1c/,/1d/p' 6-RESEARCH.md` shows chapter-wise rescope | File not at repo root; command fails. Same sed on `.planning/phases/6-source-vetting-unverified-resolution/6-RESEARCH.md` matches the claim | **Command path wrong** (W5). Observed text is real. |

### Verify commands -- false-pass / false-fail

| Task | Command problem | Effect |
|---|---|---|
| 1 | Unquoted parenthetical after `grep -c`. Live `bash -c` -> `syntax error near unexpected token '('` | **False-fail.** Task 1 cannot go green as written. |
| 2 | One OR-grep of three names; `grep -c Verified` has no threshold | **False-pass** on a single name / the pre-existing 7 stamps. |
| 3 | `GP-08` already present; saved by the `NPR 7150.2` / `chapter-wise` / `8.02` conjuncts | OK if those three strings are written. |
| 4 | `GP-08 descoped` + `63 -- 7 GP packs` are distinctive; `Phase 7 -A 3` always matches the existing header | Partial. Core strings are enough. |
| 5 | `grep -c Verified` no `= 17`; `7-8 packs` does not match live `7-8 public-domain packs`; `GP-07` is **not** in the Task 1 row text (`MIL-STD-40051-2C`); `git diff --stat` always exits 0 | **False-pass** on dates and leftover 7-8. **False-fail** if the executor does not invent a `GP-07` token. |

---

## Findings

### Warnings (should fix; execution can proceed)

**W1. [verification_derivation] Task 1 `<automated>` is not valid bash**
- Plan: 6-01 Task 1
- Live: `bash -c` of the written pipeline -> `syntax error near unexpected token '('` because the parenthetical comment after `grep -c` is unquoted.
- Fix: drop the parenthetical from the command. Assert `test "$(grep -c 'Verified 2026-08-14' docs/SOURCE-VETTING.md)" -ge 14` after Task 1 (7 existing + 7 new Vetted; Task 2 then brings it to 17), plus the heading and `6-RESEARCH.md` greps.

**W2. [verification_derivation] Task 2 / Task 5 date-stamp and name checks false-pass**
- Plan: 6-01 Tasks 2, 5
- Task 2 is one OR-grep (`AFOTEC|Defense Acquisition Guidebook|CMU SEI`) -- one hit passes. `grep -c "Verified 2026-08-14"` prints 7 on the current tree and exits 0.
- Task 5 repeats the unasserted `grep -c` (action wants pre + 10 = 17).
- Fix: three separate name greps in Task 2; `test "$(grep -c 'Verified 2026-08-14' docs/SOURCE-VETTING.md)" -eq 17` in Task 5.

**W3. [verification_derivation / key_links] Task 5 `7-8 packs` grep cannot catch the live leftover strings**
- Plan: 6-01 Tasks 4-5
- Live Goal is `7-8 public-domain packs` (does not match `7-8 packs`). Overview bullet line 77 is `Build GP-01..GP-08 packs`. `MILESTONES.md:18` is `7-8 Tier-1 packs` and is outside `files_modified`.
- After a correct Task 4 Details edit, the overview + MILESTONES still advertise 8 / 7-8. Task 5 still goes green.
- Fix: Task 4 also rewrites the Phase 7 overview bullet. Task 5 grep leftover `7-8` / `GP-01..GP-08` / `63-64`. Optional: add `MILESTONES.md` to `files_modified` and set it to 7 packs / 63.

**W4. [verification_derivation] Task 5 greps `GP-07` but Task 1 never writes that token**
- Plan: 6-01 Tasks 1, 5
- Task 1 rows are document names (`MIL-STD-40051-2C`, ...), matching the v1.17 Vetted table (no `T1-0x` / `GP-0x` IDs). Faithful execution false-fails Task 5.
- Fix: grep `40051-2C` (and the other six short names) instead of `GP-07`, or tell Task 1 to tag rows `[GP-07]` etc.

**W5. [claim_verification] VV&A `sed` path is repo-root `6-RESEARCH.md`**
- Plan: `claim_verification` last row
- Live: `sed: can't read 6-RESEARCH.md: No such file or directory`. The file is `.planning/phases/6-source-vetting-unverified-resolution/6-RESEARCH.md`. The quoted verdict text is real.
- Fix: correct the path. Do not treat RESEARCH as wrong.

**W6. [requirement_coverage] GP-06 (`federal-bca`) has no Phase 6 verdict**
- Plan: 6-01 Tasks 1, 3, 4
- SC3: each GP pack candidate confirmed or dropped. RESEARCH section 5 has no A-94 / Army CBA row (spot-checks were FAA, DOT&E, DAFMAN). Task 1's "7 rows covering the confirmed GP packs" is factually the 4 confirmed UNVERIFIED + 3 spot-checks (includes SP-7084, excludes GP-06). Phase 7 still lists GP-06.
- Not a blocker: VET-01's five named items do not include A-94; the gap report already marked it live Tier 1.
- Fix: add a dated SOURCE-VETTING row (or an explicit "already-ranked; not re-opened" note pointing at the gap report) so SC3 is visible to execute-phase. Do not silently drop GP-06.

**W7. [scope_sanity] 5 tasks / estimate.confidence overstated**
- 5 tasks is the split threshold; Task 5 is read-only. Estimate 45k/100k is inside budget; `estimate-check` confidence is `low` (`sample_count: 0`), not the plan's `med`.
- Fix: none required. Do not split.

### Non-issues (checked, not raised)

- VET-01/VET-02 stay unchecked in Task 3 -- correct; this phase records, verification ticks.
- AFOTEC is the fifth VET-01 item in REQUIREMENTS (not DAU AAF from gap-report section 4 numbered list). Plan follows REQUIREMENTS + RESEARCH 1e. Correct.
- NASA SP-7084 recorded but not built -- it is a VET-01 item, not a GP pack. 63 = 56 + 7 GP, not 56 + 7 vetted rows.
- GP-08 alternatives (NPR 7150.2 + NASA-STD-8739.8) are recorded as v1.19 / Phase 7 stretch, not built here.
- No pack builds. `files_modified` is the four integrity surfaces.
- SPDX / scoped Edit (never wholesale Write) is in Task 1 and implied for 2-4.
- Insertion point (v1.18 Vetted immediately after v1.17; Excluded rows after DAU/WARU) matches the live file.
- Single-plan `depends_on: []` is valid. No CONTEXT.md / CLAUDE.md / PATTERNS.md / VALIDATION.md / responsibility map -- those dimensions skipped, not failed.

---

## Structured issues

```yaml
issues:
  - plan: "6-01"
    dimension: verification_derivation
    severity: warning
    task: 1
    description: "Task 1 automated verify contains an unquoted parenthetical after grep -c and is a bash syntax error (false-fail)."
    fix_hint: "Remove the parenthetical comment from the command; assert a numeric Verified-stamp floor plus the v1.18 heading and 6-RESEARCH.md pointer."

  - plan: "6-01"
    dimension: verification_derivation
    severity: warning
    task: 2
    description: "Task 2 OR-greps three Excluded names (one hit passes) and greps Verified stamps with no threshold (pre-existing 7 already exits 0)."
    fix_hint: "Three conjunct greps; Task 5 test stamp count -eq 17 (7 existing + 7 Vetted + 3 Excluded)."

  - plan: "6-01"
    dimension: verification_derivation
    severity: warning
    task: 5
    description: "Task 5 grep for leftover 7-8 packs does not match live 7-8 public-domain packs; ROADMAP overview GP-01..GP-08 and MILESTONES 7-8 Tier-1 are unaddressed. grep GP-07 will false-fail because Task 1 writes MIL-STD-40051-2C, not GP-07."
    fix_hint: "Task 4 also edits the Phase 7 overview bullet; Task 5 greps leftover 7-8 / GP-01..GP-08 / 63-64 and the document short names (40051-2C, SP-7084, VV&A, 881F, FAA-STD-025, DOT&E, DAFMAN)."

  - plan: "6-01"
    dimension: requirement_coverage
    severity: warning
    task: 1
    description: "SC3 requires each GP candidate confirmed or dropped. GP-06 federal-bca (OMB A-94 + Army CBA) has no 6-RESEARCH.md verdict and no SOURCE-VETTING row; it stays in Phase 7 only by omission."
    fix_hint: "Add a dated Vetted row or an explicit already-ranked note pointing at the gap report. Do not drop GP-06."

  - plan: "6-01"
    dimension: verification_derivation
    severity: warning
    description: "claim_verification VV&A sed runs against repo-root 6-RESEARCH.md, which does not exist. The verdict text is real at the phase-dir path."
    fix_hint: "Point the command at .planning/phases/6-source-vetting-unverified-resolution/6-RESEARCH.md."

  - plan: "6-01"
    dimension: scope_sanity
    severity: warning
    description: "5 tasks and estimate.confidence med vs estimate-check confidence low (sample_count 0). 45k/100k, not over budget."
    fix_hint: "Do not split. Keep one sequential integrity-doc plan."
```

---

## Recommendation

0 blockers. 6 warnings. Verdict **PASS_WITH_FIXES**.

Highest-leverage pre-execute nits (same plan, no split): make Task 1 verify parse; assert stamp count 17 and three Excluded names; retarget Task 5 away from the `GP-07` token and the non-matching leftover 7-8 packs pattern; rewrite the Phase 7 overview bullet so GP-08 does not linger; add a one-line GP-06 confirmation so SC3 is complete on the page.

Plans reduce 0 locked user decisions (no CONTEXT.md). No phase split required.

**Verdict:** PASS_WITH_FIXES
