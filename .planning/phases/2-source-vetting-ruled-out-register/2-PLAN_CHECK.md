# Phase 2 Plan Check

**Phase:** 2-source-vetting-ruled-out-register
**Plans checked:** 1 (`2-01-PLAN.md`)
**Checked:** 2026-08-14
**Method:** Goal-backward verification against ROADMAP Phase 2 success criteria (SC1-SC3), REQUIREMENTS RO-01 / T2-03 (vetting half), `docs/SOURCE-VETTING.md`, and `2-RESEARCH.md`.

**Verdict:** PASS_WITH_FIXES

Execution may proceed. Warnings below will not by themselves prevent the phase goal, but several will let a weak verify pass while SC1/SC2 remain only partially true. Fix before execute if the verifier will score the original ROADMAP wording strictly.

---

## Goal-backward trace

Phase goal: *Every candidate source has a definitive tier decision with evidence; rejected sources permanently recorded.*

| Success criterion | Required truth | Covering task | Provably delivered? |
|---|---|---|---|
| SC1 Excluded table contains INCOSE Handbook, INCOSE GWR, ISO/IEC/IEEE 15288/29148/21839, DAU/WARU 2022 duplicate -- each with rationale and date | Four named sources present, dated, with rationale | Task 1 | Partial. New GWR + DAU rows are dated. ISO row is amended to name 29148/21839 but not dated. Handbook row is left as-is (research allows this) and stays undated. Task 1 verify does not assert dates or 21839. |
| SC2 Each of the 11 candidates has a recorded tier decision with source URL and licence evidence | 8 Tier-1 + IEEE 15288.2 + ECSS-E-ST-10C + Def Stan 00-051 | Task 1 | Partial. Task 1 adds a 4-column Vetted table for the 8 Tier-1 sources (URL + 17 U.S.C. section 105). IEEE/ECSS land in the 2-column Excluded table using research prescribed rationale (licence evidence, no source URL). Def Stan is UNVERIFIED -- no inspected in-document licence evidence. |
| SC3 Def Stan 00-051 redistribution terms resolved (build-or-exclude decision recorded) | A recorded build vs exclude decision | Tasks 1-3 | Yes, under the planner conservative reading. Task 1 records UNVERIFIED / excluded-for-this-milestone pending a registered DSTAN check. Task 2 marks T2-03 deferred-excluded. Task 3 rewrites SC3 so a recorded decision counts as satisfaction. In-document terms are not actually read. |

Requirements frontmatter: RO-01, T2-03 -- both present. RO-01 rows are tasked. T2-03 vetting-half is tasked as milestone-exclude, not as a completed licence read.

claim_verification is present (10 live-checked claims). Not a gap.

---

## Dimension results

| Dim | Result | Notes |
|---|---|---|
| 1 Requirement coverage | PASS with gaps | RO-01 + T2-03 claimed and tasked. SC1 dates and SC2 URLs for the 3 non-Tier-1 candidates are incomplete. |
| 2 Task completeness | PASS | All 4 auto tasks have Files + Action + Verify + Done. Actions are specific enough to execute. |
| 3 Dependencies | PASS | Single plan, depends_on empty, intra-plan preconditions Task 1->2->3->4. Acyclic. |
| 4 Key links | PASS | Research -> SOURCE-VETTING -> REQUIREMENTS -> ROADMAP -> STATE is tasked, not just listed. |
| 5 Scope sanity | PASS | 4 tasks / 4 files. Estimate 24k / 100k budget (ratio 0.24). estimate.confidence high in the plan is uncalibrated (estimate-check sample_count=0). Not over budget. |
| 6 Verification derivation | WARN | must_haves exist and are observable. Several automated greps cannot distinguish the required edit from an incidental 00-056 / substring hit. |
| 7 Context compliance | SKIPPED | No CONTEXT.md (discuss skipped). |
| 7b Scope reduction | WARN | T2-03 / SC3 rewritten to deferred-excluded / excluded-pending-DSTAN instead of an inspected-terms decision. Not silent: the planner is explicit. Still a goal-post move. |
| 7c Architectural tier | SKIPPED | No Architectural Responsibility Map in 2-RESEARCH.md. |
| 8 Nyquist | SKIPPED | No Validation Architecture section; nyquist_audit skipped in master_flow. |
| 9 Cross-plan contracts | PASS | One plan. |
| 10 CLAUDE.md | SKIPPED | No ./CLAUDE.md. |
| 11 Research resolution | PASS | No Open Questions section. Remaining items live under Verification gaps and are either tasked (00-051) or correctly deferred to Phase 3 (PDF footers / page counts). |
| 12 Pattern compliance | SKIPPED | No PATTERNS.md. |

---

## Findings

### Warnings (fix recommended; not blocking)

**W1. [requirement_coverage] SC1 dates missing on the two pre-existing Excluded rows**
- Plan: 2-01 / Task 1
- ROADMAP SC1 requires Handbook + ISO/IEC/IEEE 15288/29148/21839 each with rationale and date. Task 1 dates only new rows (GWR, DAU, plus IEEE/ECSS). Research says the Handbook row may be left as-is; the plan follows research and therefore will not satisfy the dated-Handbook / dated-ISO half of SC1.
- Fix: In Task 1, append (Verified 2026-08-14.) to the existing INCOSE SE Handbook and ISO / IEC / IEEE standards rows when the ISO example list is extended. Assert Verified 2026-08-14 in verify for those four SC1 names.

**W2. [requirement_coverage] SC2 source URLs not planned for IEEE 15288.2, ECSS-E-ST-10C, or Def Stan 00-051**
- Plan: 2-01 / Task 1
- SC2 is each of the 11 candidates with source URL and licence evidence. The Vetted table covers 8. Excluded-table format is Source | Why excluded; research prescribed IEEE/ECSS rationale has no URL. Def Stan has no public PDF URL.
- Fix: Put the research URLs (IEEE https://standards.ieee.org/ieee/15288.2/5705/, ECSS https://ecss.nl/standard/ecss-e-st-10c-rev-1-..., DSTAN/gov.uk portal for 00-051) into each outcome record, or state in Task 1 that SC2 URLs for excluded/UNVERIFIED sources live only in 2-RESEARCH.md and that SOURCE-VETTING records textual identification. Do not leave this implicit.

**W3. [scope_reduction] T2-03 / SC3 satisfied by rewriting the criterion, not by reading in-document terms**
- Plan: 2-01 / Tasks 1-3
- Planner-flagged risk (T2-03 resolved strictness). Research still says the tier decision is UNVERIFIED -- pending manual retrieval. The plan records exclude-for-v1.17.0 and then edits Phase 2 SC3 so a recorded deferral counts as resolved. That is a valid conservative process decision; it is not a completed vet of redistribution terms.
- Fix: Keep the milestone-exclude. Do not check T2-03 [x] as fully resolved. Word it as deferred-excluded (in-document terms still UNVERIFIED; no DSTAN retrieval this phase). Do not weaken SC3 into a tautology; leave a one-line note that the licence read remains open if 00-051 is ever revived.

**W4. [claude_md_compliance / conventions] Vetted-section source URLs vs Link Policy**
- Plan: 2-01 / Task 1 + threat T-2-03
- Planner-flagged risk (URL/link-policy nuance). docs/SOURCE-VETTING.md Link Policy: source-material URLs are not published anywhere in a pack or the docs. Task 1 still adds a Source | Tier | URL | Licence evidence table to that doc and calls it consistent with Link Policy. It is not, as written. Current SOURCE-VETTING.md contains no source URLs.
- Fix: Either (a) add an explicit Link Policy exception: vetting URLs may appear in this integrity doc only, or (b) keep URLs in .planning/phases/2-.../2-RESEARCH.md and identify sources in SOURCE-VETTING by title + publisher + version. Pick one in the task action so the executor is not told both add URLs and respect the policy that forbids URLs in docs.

**W5. [verification_derivation] Automated greps can false-pass**
- Plan: 2-01 / Tasks 1, 2, 4
- Task 2 verify grep -c 56 on REQUIREMENTS.md passes if Task 2 writes the required 00-056 subject-mismatch note and never updates REL-01/REL-02 to 56 packs.
- Task 4 verify grep -c 56 on STATE.md has the same hole (00-051/00-056 is in the Task 4 action).
- Task 1 verify never checks 21839, dated rows, the 8 named Tier-1 sources, or any URL/licence-evidence column.
- Fix: Assert distinctive strings, e.g. 56 (48 baseline + 8 Tier-1) / target after v1.17.0: 56, 21839, Verified 2026-08-14, and one grep per Tier-1 short name. Keep the Task 3 59+ absence check.

**W6. [key_links_planned] Phase 4 closed-by-vetting can leave vacuous build criteria**
- Plan: 2-01 / Task 3
- Planner-flagged risk (Phase-4 closed-by-vetting judgment). Keeping the phase for depends-on stability is the right churn trade. Current Phase 4 success criteria still say each pack LICENSE reproduces source terms for 3 packs. If Task 3 only retitles the phase and leaves those criteria, a later executor can treat Phase 4 as still buildable (licence-breaching).
- Fix: Task 3 must rewrite Phase 4 Goal / Requirements / Success Criteria to 0 packs / no execution, and drop T2-01/T2-02/T2-03 from an active Requirements list (point at the SOURCE-VETTING outcome). Prefer keep-the-slot over renumber.

### Info

**I1. [scope_sanity]** 4 tasks is the warning threshold; not split-worthy here (1 file per task, sequential doc propagation, 24% of token budget).

**I2. [verification_derivation]** claim_verification block is present and the 10 cited measurements match the current tree (Handbook row at SOURCE-VETTING:72, ISO examples at :71, 59+ at ROADMAP:60 and STATE:33, dau-se-guidebook pack count = 1).

**I3.** PROJECT.md / MILESTONES.md still say 11 researched candidate packs (8 Tier-1, 3 Tier-2). Out of Phase 2 SC scope; will drift after Task 3 unless a later phase touches them.

---

## Structured issues

```yaml
issues:
  - plan: "2-01"
    dimension: requirement_coverage
    severity: warning
    task: 1
    description: "SC1 requires dated rationale on INCOSE Handbook and ISO/IEC/IEEE 15288/29148/21839; Task 1 dates only new rows and does not date the existing Handbook or ISO rows."
    fix_hint: "Append a 2026-08-14 verification date to those two existing Excluded rows and grep for the date stamp plus 21839."
  - plan: "2-01"
    dimension: requirement_coverage
    severity: warning
    task: 1
    description: "SC2 requires source URL + licence evidence for all 11 candidates; only the 8 Tier-1 Vetted rows are planned with URLs. IEEE/ECSS/Def Stan records omit URLs; Def Stan has no inspected licence text."
    fix_hint: "Record research URLs on the three non-Tier-1 outcomes, or explicitly locate SC2 URLs in 2-RESEARCH.md only."
  - plan: "2-01"
    dimension: scope_reduction
    severity: warning
    task: 2
    description: "T2-03/SC3 are marked resolved via deferred-excluded + ROADMAP wording change; in-document Def Stan terms remain UNVERIFIED."
    fix_hint: "Keep milestone-exclude; do not [x] T2-03; do not rewrite SC3 into a tautology."
  - plan: "2-01"
    dimension: claude_md_compliance
    severity: warning
    task: 1
    description: "Task 1 publishes source URLs in docs/SOURCE-VETTING.md while that doc Link Policy forbids publishing source-material URLs in packs or docs."
    fix_hint: "Add an explicit integrity-doc exception to the Link Policy, or keep URLs only in 2-RESEARCH.md."
  - plan: "2-01"
    dimension: verification_derivation
    severity: warning
    task: 2
    description: "Task 2 and Task 4 grep -c 56 can pass on the 00-056 subject-mismatch note without the 56-pack REL/STATE count update. Task 1 verify omits 21839, dates, and the 8 Tier-1 names."
    fix_hint: "Match distinctive phrases (56 (48 baseline + 8 Tier-1), Verified 2026-08-14, each Tier-1 short name, 21839)."
  - plan: "2-01"
    dimension: key_links_planned
    severity: warning
    task: 3
    description: "Phase 4 keep-the-slot / closed-by-vetting is fine only if Goal, Requirements, and Success Criteria are rewritten to 0 packs / no execution."
    fix_hint: "Replace Phase 4 build criteria; do not leave each-pack LICENSE language live."
```

---

## Recommendation

0 blockers. 6 warnings. Verdict **PASS_WITH_FIXES**.

Highest-leverage pre-execute edits (same plan, no split): date the two existing SC1 rows; disambiguate Link Policy vs Vetted URLs; tighten Task 2/4 greps so 00-056 cannot satisfy the 56-pack count; keep T2-03 unchecked as UNVERIFIED milestone-exclude; make Phase 4 success criteria explicitly empty.

Planner-flagged risks confirmed as warnings, not blockers: T2-03 resolved strictness (W3), Phase-4 closed-by-vetting (W6), URL/link-policy nuance (W4).

---

## Re-check (post-remediation)

**Plan:** `2-01-PLAN.md` at `e828f0b` (`docs(2): plan_remediate — BL-01 + MA/MI fixes`)
**Re-checked:** 2026-08-14
**Method:** Goal-backward. For each of the 11 `2-PLAN_REVIEW.md` findings, ask whether the remediated task text now *provably* delivers ROADMAP Phase 2 SC1–SC3 without publishing source-material URLs in `docs/SOURCE-VETTING.md` (Link Policy: not in a pack **or the docs**). Credit only executable action / verify / done / must_haves / threat-model text, not intent.

**Updated Verdict:** PASS_WITH_FIXES

All 11 original findings are **cleared in substance**. Execution may proceed. Three residuals introduced or left by the remediation will not by themselves prevent SC1–SC3, but one leftover sentence can re-create MI-01 if the executor follows Task 2 step 5 after step 2, and Task 1's date-stamp assert is off-by-one against the live tree.

### Goal-backward re-trace (SC1–SC3 + Link Policy)

| Required truth | Covering task after e828f0b | Provably delivered? |
|---|---|---|
| SC1 — Excluded table contains Handbook, GWR, ISO/IEC/IEEE 15288/29148/21839, DAU/WARU 2022, each with rationale **and date** | Task 1 items 1–2: four new dated rows; ISO example list extended to 29148 + 21839; existing ISO and Handbook rows dated `(Verified 2026-08-14.)`; verify asserts `21839` and `Verified 2026-08-14` ≥ 8 | **Yes** (dating is tasked). Verify threshold ≥ 8 is one too high vs live count — see N1. |
| SC2 — each of 11 candidates has a recorded tier decision with source URL and licence evidence | Task 1 items 1/3/4 + pointer line to `2-RESEARCH.md` as the sole URL store; must_haves truth states SC2 URL half is satisfied by that pointer; 8 Tier-1 rows carry 17 U.S.C. § 105 evidence; IEEE/ECSS rationale carries licence evidence; Def Stan recorded UNVERIFIED | **Yes, by the agreed BL-01(b) reading.** URLs stay out of `docs/`. A verifier that demands URLs *inside* SOURCE-VETTING will still fail SC2 — that is the Link Policy trade, not an unfixed gap. |
| SC3 — Def Stan 00-051 build-or-exclude decision recorded | Task 1 item 4 UNVERIFIED/excluded-for-this-milestone; Task 2 keeps T2-03 **UNCHECKED** and forbids the word "resolved"; Task 3 annotates SC3 as deferred-excluded | **Yes.** Decision is recorded; in-document terms remain unread (explicit). |
| Link Policy — no source-material URL in packs **or the docs** | Task 1.3: no URL column; title+publisher+version only; do not copy research URLs; verify `[ "$(grep -c "http" docs/SOURCE-VETTING.md)" -eq 0 ]`; T-2-03 disposition is now **mitigate** | **Yes.** Live tree already has `http` count = 0; the plan keeps it there. |

### Per-finding status

| ID | Original issue | Status | Evidence in remediated plan |
|---|---|---|---|
| **BL-01** | Task 1.3 publishes source URLs in `docs/SOURCE-VETTING.md` against Link Policy | **CLEARED** | Task 1.3 drops the URL column; "do NOT put any source URL in docs/SOURCE-VETTING.md"; pointer to `2-RESEARCH.md`; must_haves truth no longer says "with source URL"; T-2-03 is mitigate + `http` count = 0. Option (b) implemented. |
| **MA-01** | SC1 dates missing on pre-existing Handbook + ISO rows; plan claimed SC1–SC3 all satisfied | **CLEARED** | Task 1 item 2 dates both pre-existing rows; done requires ≥8 `Verified 2026-08-14` stamps including those two. Residual: the ≥8 assert itself is off-by-one (N1). |
| **MA-02** | `grep -c "56"` false-passes via `00-056`; REQUIREMENTS has no pack count today | **CLEARED** | Task 2 writes and greps the literal `56 (48 baseline + 8 Tier-1)`; Task 4 greps `target after v1.17.0: 56`; Task 1 adds `21839`, date stamps, and Tier-1 short names. Residual: the eight names are one OR-grep, so one hit passes (N2). |
| **MA-03** | Phase 4 "rewrite the phase entry" left the :12 bullet and Goal/SC live | **CLEARED** | Task 3.1 enumerates (a) Phases bullet and (b) Details Goal / Requirements / Success Criteria; verify asserts `Build the 3 Tier-2 packs` count = 0 and `closed by vetting` present. |
| **MA-04** | "Mark T2-03 resolved" invited ticking an unread licence | **CLEARED** | Task 2 step 3: checkbox **UNCHECKED**; "do not use the word resolved"; Future Candidates + SC3 annotation kept as UNVERIFIED-deferral. Residual: the Task 2 `<name>` still says "resolve T2-03" (N4). |
| **MA-05** | SC2 URL half unmet for IEEE / ECSS / Def Stan | **CLEARED** | Joint with BL-01(b). Pointer line explicitly covers vetted/excluded/UNVERIFIED candidates; must_haves truth says SC2 URL half is satisfied by reference. |
| **MI-01** | ECSS mirrored under "Paywalled standards full texts" | **CLEARED** (residual N3) | Task 2 step 2 forbids the Paywalled label for ECSS and names the free-download / no-redistribution-grant reason or a second umbrella row; done repeats "not paywalled". Step 5 still says "the two new entries cite" the Paywalled row — leftover that can undo step 2. |
| **MI-02** | PROJECT.md / MILESTONES.md still said "3 Tier-2" and were out of `files_modified` | **CLEARED** | Both files added to frontmatter + Task 4 files; Task 4 steps 2–3 rewrite the strings; verify asserts `3 Tier-2` count = 0 in each. |
| **MI-03** | Edit-only mandated only on Task 3 | **CLEARED** | "Use Edit (scoped replacements), never whole-file Write" is now the first sentence of Tasks 1, 2, 3, and 4. Task 1 also names the SPDX/MIT header risk. |
| **MI-04** | Verbatim-copy would propagate the truncated ECSS URL | **CLEARED** | Task 1.3: "Do not copy URLs from research even as evidence: the ECSS URL in 2-RESEARCH.md is abbreviated/truncated". URLs are not copied into the doc at all. |
| **MI-05** | Bare "Vetted candidates" heading overclaims checklist item 2 | **CLEARED** | Section title is now `Vetted candidates (v1.17.0) — statute-basis; confirm in-source at build`; verify greps that heading; action requires a pending in-PDF confirmation note. |

### New / residual issues (not in the original 11)

**N1. [WARNING] [verification_derivation] Task 1 `Verified 2026-08-14` ≥ 8 is off-by-one against the live tree**
- Live `docs/SOURCE-VETTING.md` already has **1** stamp (INCOSE Competency Framework, e5f01bc). Task 1 adds 4 new dated rows + dates the 2 pre-existing SC1 rows = **+6 → 7**. The original MA-01 fix hint double-counted GWR+DAU inside the "4 new". Correct execution therefore **fails** Task 1 verify (false-fail), or tempts the executor to mint a dummy eighth stamp.
- Fix: change the assert and the `<done>` line to `-ge 7` (or `-ge 6` if the existing Competency row is out of scope). Do not add a fake date to pass.

**N2. [WARNING] [verification_derivation] Task 1 Tier-1 name check is a single OR-grep**
- `grep -c "800-171\|800-61\|338B\|516C\|7009\|413.3B\|CPG 2.0\|SEM3" … | grep -qv '^0$'` passes if **any one** of the eight names is present. MA-02 asked for one short name per source. An executor can land NIST 800-171 only and skip the other seven.
- Fix: eight separate `grep -c … | grep -qv '^0$'` conjuncts (same pattern already used for `29148` / `21839`).

**N3. [WARNING] [doc_consistency] Task 2 step 5 still tells the executor both new Out-of-Scope entries cite the Paywalled umbrella**
- Step 2 + `<done>` clear MI-01. Step 5 ("Leave the existing Out of Scope row … as the umbrella rationale; **the two new entries cite it**") is leftover pre-remediation text. Last-step-wins execution re-labels ECSS as paywalled.
- Fix: rewrite step 5 to "keep the Paywalled umbrella for T2-01 only; T2-02 uses the non-redistributable free-download reason / second umbrella from step 2."

**N4. [INFO] [scope_reduction] Task 2 `<name>` still says "resolve T2-03"**
- Action body, must_haves, Task 3.3, and Task 4 all forbid "resolved" and keep the checkbox unchecked. Risk is name-only.
- Fix: rename to "record T2-03 as deferred-excluded".

### What the remediation did *not* break

- Requirement coverage still claims `[RO-01, T2-03]`; both remain tasked.
- Four auto tasks still have Files + Action + Verify + Done (`verify.plan-structure` valid, 0 errors).
- Intra-plan preconditions 1->2->3->4 remain acyclic.
- Research -> SOURCE-VETTING -> REQUIREMENTS -> ROADMAP -> STATE (+ now PROJECT / MILESTONES) is still wired, not just listed.
- Scope: 4 tasks / 6 files / estimate 24k of 100k (`estimate-check --calibrated`: ratio 0.24, `over_budget: false`, `confidence: low` because `sample_count=0`).
- No deferred ideas pulled in. No CONTEXT.md. No new URL-in-docs path. No whole-file Write instruction reintroduced.
- Threat T-2-03 no longer "accepts" the Link Policy breach.

### Structured residuals

```yaml
issues:
  - plan: "2-01"
    dimension: verification_derivation
    severity: warning
    task: 1
    description: "Task 1 verify requires >=8 Verified 2026-08-14 stamps; correct execution yields 7 (1 existing Competency Framework + 4 new + 2 amended SC1 rows). False-fail or dummy-stamp risk."
    fix_hint: "Change the assert and <done> to -ge 7."
  - plan: "2-01"
    dimension: verification_derivation
    severity: warning
    task: 1
    description: "Eight Tier-1 short names are checked with one OR-grep; a single hit passes."
    fix_hint: "Assert each of 800-171, 800-61, 338B, 516C, 7009, 413.3B, CPG 2.0, SEM3 separately."
  - plan: "2-01"
    dimension: doc_consistency
    severity: warning
    task: 2
    description: "Task 2 step 5 still says both new Out-of-Scope entries cite the Paywalled umbrella, contradicting step 2 / <done> for ECSS."
    fix_hint: "Limit the Paywalled cite to T2-01; keep T2-02 on the free-download no-redistribution-grant reason."
  - plan: "2-01"
    dimension: scope_reduction
    severity: info
    task: 2
    description: "Task 2 <name> still says resolve T2-03 after the action forbade that verb."
    fix_hint: "Rename the task to record T2-03 as deferred-excluded."
```

### Recommendation

11/11 original findings **cleared**. 0 blockers. 3 new/residual warnings + 1 info. Verdict **PASS_WITH_FIXES**.

Highest-leverage pre-execute nits (optional, same plan, no split): drop the date-stamp floor from 8 to 7; split the Tier-1 OR-grep; delete the "two new entries cite it" clause in Task 2 step 5. None of these block SC1-SC3 if the executor follows the more specific action/done text and the Link Policy verify.

**Verdict:** PASS_WITH_FIXES

