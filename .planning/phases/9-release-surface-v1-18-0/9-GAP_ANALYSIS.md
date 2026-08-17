# Phase 9 Gap Analysis — Release surface + v1.18.0

Date: 2026-08-14 (verification pass)
Inputs: 9-PLAN_CHECK, 9-PLAN_REVIEW, 9-01-PLAN/SUMMARY, 9-IMPL_REVIEW (PW_NOTES), 9-CODE_REVIEW (PW_NOTES), 9-INTEGRATION_CHECK (PASS_WITH_NOTES), 9-SECURITY_AUDIT (SECURED), STATE.md, ROADMAP.md Phase 9, REQUIREMENTS.md REL-1x.

**Verdict:** CLOSED

All four review lanes passed with zero blockers and zero MAJOR findings. Every identified gap is either adjudicated as residual (accepted), deferred to the v1.19 doc-pass, or already tracked on the v1.19 backlog in STATE.md. No open gap blocks closing Phase 9 / milestone v1.18.0.

## Gap adjudications

| # | Gap | Source | Adjudication |
|---|-----|--------|--------------|
| 1 | MI-01 — planning-record hygiene: 9-01-PLAN Task 6 file-list undercount | 9-CODE_REVIEW | **Residual, accepted.** Record-keeping nit only; the actual shipped artifacts (tag, release, records) are correct and verified. No action. |
| 2 | CR-INFO-01 — CHANGELOG.md UTF-8 BOM (pre-existing, not introduced by v1.18.0) | 9-CODE_REVIEW | **Deferred to v1.19 doc-pass.** Confirmed still present (byte check 2026-08-14). Cosmetic; does not affect parsing by check_release or GitHub rendering. |
| 3 | CR-INFO-02 — CHANGELOG.md mixed CRLF line endings (620 CRLF occurrences; pre-existing) | 9-CODE_REVIEW | **Deferred to v1.19 doc-pass**, bundled with BOM strip + `.gitattributes` pin (see carry-forward). |
| 4 | Map gate standalone — `check_capability_map.py` not wired into `check_release.py` (integration warning) | 9-INTEGRATION_CHECK | **Confirmed tracked.** STATE.md "v1.19 backlog (carried)" line: "Optional map-gate wiring into check_release (Phase 8 deferred)". Both gates were run independently at release time and both PASS, so v1.18.0 correctness is unaffected. |
| 5 | REL-1x-01/02 delivery — tag + GitHub Release on origin | Task brief | **Re-verified cheaply 2026-08-14:** `git ls-remote --tags origin` shows `v1.18.0` (annotated, `^{}` = d19be1a); `gh release view v1.18.0` → tagName v1.18.0, isDraft false, name "v1.18.0 — 7 gap-driven Tier-1 packs + capability map v2". |

## v1.19 carry-forward list

Carried in STATE.md §"v1.19 backlog (carried)" plus doc-pass items from this analysis:

1. **FUT-04** — federal-bca Army CBA Guide second source (retry if ASAFM PDF becomes reachable)
2. **FUT-05** — deterministic map generator (as recorded at bdc6c9e)
3. **7-CODE-REVIEW IN-02** — minimal committed overlap checker (qualify source; distinct from 8-series IN-02)
4. **Thin-cluster fattening** — clusters 3 / 5 / 15
5. **Map-gate wiring** — run `check_capability_map.py` from `check_release.py` (or a wrapper) so a single gate covers both
6. **CHANGELOG hygiene** — strip UTF-8 BOM + normalize CRLF→LF (doc-pass)
7. **`.gitattributes` pin** — `*.md text eol=lf` (or equivalent) to prevent CRLF recurrence
8. **AAF vetting before any use** — AAF remains deferred non-candidate; must complete source vetting before any future inclusion (carried from Phase 6 rescope)
9. Optional (from 7-GAP_ANALYSIS R1/R2/R5): PACK.yaml note additions, ROSAP Rev E retry, federal-bca "(c)" wording polish
