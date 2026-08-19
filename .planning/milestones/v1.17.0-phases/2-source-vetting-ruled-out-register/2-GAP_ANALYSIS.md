# Phase 2 Gap Analysis — Source Vetting + Ruled-Out Register

**Phase:** 2-source-vetting-ruled-out-register
**Date:** 2026-08-14
**Inputs reviewed:** 2-IMPL_REVIEW.md (PASS_WITH_NOTES), 2-CODE_REVIEW.md (PASS_WITH_NOTES), 2-INTEGRATION_CHECK.md (NEEDS_WORK), 2-SECURITY_AUDIT.md (SECURED), plus 2-RESEARCH.md, 2-01-PLAN.md, 2-01-SUMMARY.md, 2-PLAN_CHECK.md (incl. re-check), 2-PLAN_REVIEW.md, .planning/ROADMAP.md, .planning/REQUIREMENTS.md, docs/SOURCE-VETTING.md.
**Method:** All four required post-execute reviews present. Every prior finding re-verified against the live tree (greps + gate re-runs), not against review claims.

**Verdict:** NEEDS_WORK

Narrow re-entry: one surgical fix (CI gate half of the integration blocker, G-1 below). Phase 2's own success criteria SC1–SC3 are all TRUE and both phase requirements are correctly recorded — the phase goal itself is delivered. The single blocking defect is a TOOL-02 regression (red CI on next push) introduced by Phase 2's committed evidence artifacts and only half-remediated after the integration check.

---

## 1. Post-review remediations already landed (verified in tree — no action)

The four commits b40668b, eb51854, c8b4a89, 0584a15 discharged most open findings. Each was independently re-verified on the live tree:

| Prior finding | Remediation commit | Verified state |
|---|---|---|
| Integration BLOCKER-1 (local gate) | b40668b — check_release.py exempts `.planning` | `python tooling/check_release.py` → **PASS, exit 0** (re-run 2026-08-14) |
| Code-review MA-01 (SUMMARY frontmatter claimed T2-03 completed) | eb51854 | 2-01-SUMMARY.md:52 reads `requirements-completed: [RO-01]` — T2-03 dropped |
| Code-review MI-01..MI-03 (STATE.md metadata) | c8b4a89 | `milestone_name: Source Expansion (v1.17.0)`; `status: executing`; `[Phase 2]` decision tags |
| Code-review MI-04/MI-05 (ROADMAP plan count; 54/56 basis ambiguity) | 0584a15 | ROADMAP Phase 2 `Plans: 1 (complete)`; Phase 5 SC1 = "54 packs … minus 2 signpost packs / 56 directory basis" |
| Impl MA-01 residual (stamp count 7 vs plan's `-ge 8`) | Recorded in SUMMARY deviation N1 + key-decisions | Stamps = **7** (truthful); no dummy 8th stamp — security audit confirmed this was correct |

---

## 2. Blocking gap (open) — drives the verdict

### G-1. CI validate workflow still reds on the next push (integration BLOCKER-1, CI half — NOT closed)

**Where:** `.github/workflows/validate.yml` content-integrity job (leak-sentinel step + link-policy step).
**Evidence (CI simulation over `git ls-files`, re-run 2026-08-14):**
- Leak-sentinel step: **2 tracked-file violations** — `2-SECURITY_AUDIT.md` (quotes the private-key block sentinel literal it scanned for) and `2-INTEGRATION_CHECK.md` (quotes the same sentinel again in its gate-output transcript; the integration artifact itself re-introduced the trip while documenting the first one).
- Link-policy step: **2 tracked-file violations** — `2-RESEARCH.md` (two NIST CSRC source URLs; host not repeated here by design) and `2-INTEGRATION_CHECK.md` (quotes one of them in its gate transcript).

**Diagnosis:** b40668b exempted `.planning` in `tooling/check_release.py` (local gate → green) but the CI workflow's two inline scans — whose own header says they "mirror tooling/check_release.py" — received no matching exemption. The local and CI gates now disagree about whether `.planning` evidence is committable. Every push to `main` and every Phase 3 PR will fail the content-integrity job until this lands. This is a TOOL-02 regression (Phase 1 baseline requirement: "CI validate gate blocks non-conforming releases" — here it blocks conforming ones) and re-breaks the Phase 2 → Phase 5 gate chain the integration check flagged.

**Remediation (pick one; recommend A):**
- **A (recommended, matches the recorded b40668b design decision):** add the `.planning` exclusion to validate.yml's two scan steps (leak-sentinel grep `--exclude-dir=.planning`; link-policy python skip `.planning` parts), mirroring check_release.py. Orchestrator-owned — `.github/` is outside subagent write scope.
- **B (works without touching .github/):** fragment the sentinel text in 2-SECURITY_AUDIT.md and 2-INTEGRATION_CHECK.md, and host-elide the source URLs in 2-RESEARCH.md and 2-INTEGRATION_CHECK.md. Executable as a docs-only gaps commit, but it contradicts the b40668b rationale (.planning legitimately holds vetting URL evidence) and would have to be re-applied to every future phase's research/review artifacts — worse ergonomics.

**Re-verify after fix:** re-run the CI simulation over tracked files (expect 0/0) plus `python tooling/check_release.py` (expect PASS). After G-1 closes, no further Phase 2 execute re-entry is required — everything else in this analysis is a routed precondition or an accepted residual.

Note: this file deliberately avoids the sentinel literal and source-URL strings so it does not add a fifth CI trip point.

---

## 3. Adjudication: integration WARNING-1 (vet_source.py classifier drift) — NOT a Phase 2 gap; routed to Phase 3

Phase 2's deliverable is the human rubric record (docs/SOURCE-VETTING.md), which is complete and verified by all four reviews. The mechanical classifier lives in the **external** jgs-reference-skill repo; Phase 2 SC1–SC3 do not reach it, and the integration check itself classes the drift as "defence-in-depth losses, not active breaks" (none of ECSS / Def Stan / IEEE 15288.2 appear in any Phase 3 build list). Split into:

- **P3-PRE-1 (must-do Phase 3 precondition, in-repo):** `cisa` is absent from the tool's US_GOV signals — with title/publisher alone it classifies Tier 3. The Phase 3 build META entry for `cisa-cpg` **must carry a statute-bearing license string** (US Government work, 17 U.S.C. § 105) or the external vet step mis-gates the build. Encode this in the Phase 3 plan's build-workflow META spec.
- **P3-PRE-2 (should-do / accepted-gap decision, external repo):** add `ecss`/`esa` (and consider `def stan`/`dstan`) to vet_source.py EXCLUDED signals and sync the external companion rubric with the Phase 2 rows. If deliberately not done, record the accepted gap (human rubric governs; tool under-blocks) in the Phase 3 plan so the divergence is documented rather than rediscovered. Def Stan 00-051's tool behavior (Tier 3 + "treat as Excluded" warning, exit 0) is directionally consistent with the recorded deferral and folds into this item.

---

## 4. Residuals accepted (ship-able; rejected as gaps)

| ID | Finding | Disposition |
|---|---|---|
| R-1 | Commit-count deviation: 4 task commits + 2 fixups vs plan's "4 independent commits" (impl MI-01) | Accept — final state correct; wrong-then-right churn is history-only; retro note |
| R-2 | ROADMAP SC2 text still reads "with source URL" without the by-reference annotation (impl MI-02) | Accept — SC2 satisfied under the agreed BL-01(b) reading (pointer line in SOURCE-VETTING.md); verified PASS by code-review contract matrix and integration check. Optional one-line ROADMAP annotation may ride the G-1 commit |
| R-3 | Bare domain "ecss.nl" in SOURCE-VETTING.md:81 (code IN-01, security note 1) | Accept — compliant as verified (`http` count = 0); plan-prescribed wording; optional future tightening to "the ECSS portal" |
| R-4 | Plan verify stamp gate `-ge 8` vs truthful count 7 (impl MA-01) | Accept — already recorded in SUMMARY deviation N1; audit-milestone re-runs of the plan's literal verify will false-fail, and the SUMMARY record is the authoritative answer |
| R-5 | master_flow_state.json (root + phase) modified-uncommitted, mid-gate (code MI-06) | Accept for this artifact — orchestrator-owned; advance past this gate and commit with the next docs commit |
| R-6 | Integration WARNING-2: SOURCE-VETTING.md:162 overstates CI enforcement (CI never runs validate_pack.py) | Accept — pre-existing wording, not a Phase 2 regression; fix opportunistically with G-1's docs rider |
| R-7 | Untracked parallel-workstream files (docs/capability-pack-map.*, docs/ROLE-AGENTS-REQUIREMENTS-V2.md) | Out of Phase 2 scope; untracked so no CI impact; review before any commit that includes them |

---

## 5. Phase 2 success-criteria and requirements cross-check (ROADMAP / REQUIREMENTS)

| Criterion | Status | Evidence |
|---|---|---|
| SC1 — Excluded table contains the 4 named sources, each with rationale and date | **TRUE** | Rows at SOURCE-VETTING.md:71-72, 80-83 all dated "(Verified 2026-08-14.)"; ISO row names 29148 + 21839; confirmed by impl review, code review, security audit |
| SC2 — 11 candidates each with recorded tier decision + URL + licence evidence | **TRUE (by reference)** | 8 Tier-1 Vetted rows + IEEE 15288.2/ECSS Excluded + Def Stan 00-051 UNVERIFIED = 11; URL half via the 2-RESEARCH.md pointer line (BL-01 option (b)); `grep -c http` on the doc = **0** |
| SC3 — Def Stan 00-051 outcome recorded as deferred-excluded pending registered DSTAN in-document check | **TRUE** | SOURCE-VETTING.md:112-127; REQUIREMENTS T2-03 `- [ ]` with "deferred-excluded … never resolved" wording; FUT-03 revival path preserved |
| RO-01 delivered | **TRUE** | REQUIREMENTS.md:45 `[x]`; rows + dated rationale verified by all four reviews |
| T2-03 deferred-unchecked (correct posture) | **TRUE** | REQUIREMENTS.md:41 `- [ ]`; checkbox auto-check was reverted (311621c, eb51854); SUMMARY frontmatter corrected to `[RO-01]` |

Phase 2 goal — "Every candidate source has a definitive tier decision with evidence; rejected sources permanently recorded" — is met by the artifacts. The NEEDS_WORK verdict rests solely on G-1 (repo-level CI gate regression), not on any unmet Phase 2 criterion.

---

## 6. Next commands

1. Close G-1 (orchestrator): apply option A — exempt `.planning` in `.github/workflows/validate.yml`'s leak-sentinel and link-policy steps to match check_release.py (b40668b). One small commit.
2. Re-verify: CI simulation over tracked files → 0 leak / 0 link violations; `python tooling/check_release.py` → PASS.
3. Fold P3-PRE-1 (cisa-cpg statute-bearing license string in build META) and P3-PRE-2 (vet_source.py ECSS/Def Stan encoding, or recorded accepted gap) into the Phase 3 plan as explicit preconditions.
4. Optional riders on the G-1 commit: R-2 ROADMAP SC2 annotation ("source URLs by reference in 2-RESEARCH.md per Link Policy"), R-6 CI-enforcement wording fix, R-5 state-file advance.
5. After G-1 verifies clean, Phase 2 closes as COMPLETE; Phase 3 may plan against the 8 Tier-1 candidates and the 54-catalog / 56-directory basis.

---

_Reviewer: ZCode (gap analysis)_<br>
_Method: live-tree verification; gates re-run 2026-08-14_
