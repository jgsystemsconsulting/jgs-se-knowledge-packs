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
