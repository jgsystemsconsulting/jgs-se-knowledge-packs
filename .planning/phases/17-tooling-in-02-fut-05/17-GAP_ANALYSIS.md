# Phase 17 Gap Analysis — Tooling (IN-02 + FUT-05)

**Phase:** 17-tooling-in-02-fut-05  
**Date:** 2026-08-20  
**Analyzer:** gsd-gap-analyzer  
**Inputs:** 17-01-PLAN.md, 17-01-SUMMARY.md, 17-IMPL_REVIEW.md, 17-CODE_REVIEW.md, 17-INTEGRATION_CHECK.md, 17-SECURITY_AUDIT.md, ROADMAP Phase 17 success criteria, REQUIREMENTS TOOL-20-01..03, live gate re-runs

**Verdict:** CLOSED

---

## Review rollup

| Artifact | Verdict | Blockers |
|----------|---------|----------|
| 17-IMPL_REVIEW.md | PASS_WITH_NOTES | 0 |
| 17-CODE_REVIEW.md | PASS_WITH_NOTES | 0 (WR-01, WR-02 warnings only) |
| 17-INTEGRATION_CHECK.md | PASS | 0 |
| 17-SECURITY_AUDIT.md | SECURED | 0 open threats (4 CLOSED + 2 ACCEPTED) |

All four required post-execute reviews present. No missing review without skip reason.

---

## ROADMAP success criteria

| # | Criterion | Status | Evidence |
|---|-----------|--------|----------|
| 1 | Minimal overlap checker under `tooling/` (stdlib preferred); detects multi-pack chapter collisions | **MET** | `tooling/check_overlap.py`; AST imports `__future__`/`sys`/`pathlib` only; `OVERLAP: PASS` rc=0; dups assert `{ch01-introduction.md: 3 packs}` |
| 2 | Checker on release path; fails on violations; thresholds documented; support files no false-fail | **MET** | `check_release.py` `# 5d` in-process `check_overlap.main()` before map `# 5e`; CONTRACT §7 scope/threshold/WHITELIST; chapters/ scan excludes pack-root support files; `RELEASE CHECK: PASS` |
| 3 | Deterministic map generator **or** largest deterministic slice + residual agent procedure in CONTRACT; no false full FUT-05 close | **MET** | No `tooling/generate*`; CONTRACT §8 names `check_capability_map` mechanical slice + agent cluster/note residual + explicit "does **not** claim a byte-stable full-map generator"; map still PASS TOTAL 644 |

---

## TOOL-20 coverage

| ID | Intent | Status | Notes |
|----|--------|--------|-------|
| TOOL-20-01 | Stdlib overlap checker | **SATISFIED** | Live gate green; WHITELIST = `{ch01-introduction.md}` |
| TOOL-20-02 | Wire + thresholds | **SATISFIED** | In-process wire; CONTRACT §7 |
| TOOL-20-03 | FUT-05 honest partial | **SATISFIED** | CONTRACT §8 residual; no generator claim |

Live REQUIREMENTS boxes remain `- [ ]` (intentional — verify does not tick; phase.complete owns ticks).

---

## Live re-run (this analysis)

```
python tooling/check_overlap.py
→ OVERLAP: PASS  (exit 0)

python tooling/check_release.py
→ OVERLAP: PASS
→ … TOTAL: 644
→ PASS: capability map OK
→ RELEASE CHECK: PASS — repo is release-ready against the mechanical gate.  (exit 0)

python tooling/check_capability_map.py
→ PASS: capability map OK  TOTAL: 644  (exit 0)

grep -n "check_overlap" tooling/check_release.py
→ 17:  8. Multi-pack chapter-basename overlap via check_overlap.main() …
→ 218:        import check_overlap
→ 219:        rc = check_overlap.main()
→ 221:            fail(errs, "[overlap] check_overlap.py failed …")
→ 223:        fail(errs, f"[overlap] check_overlap failed to run: {e}")

rg -n "FUT-05|overlap|WHITELIST" docs/capability-map-CONTRACT.md | head -40
→ §7 Chapter basename overlap gate (WHITELIST, thresholds, scan scope)
→ §8 FUT-05 residual (mechanical slice vs agent classification; no byte-stable full-map generator)
```

Additional fences (this analysis):

| Fence | Result |
|-------|--------|
| Version trio | `{1.19.0}` |
| `map_version` / schema | `1.19.0` / `2` |
| `git tag -l 'v1.19*'` | `v1.19.0` only (no v1.19.1) |
| CI fence | `never` + `executes checked-out repository code`; `check_overlap` absent from validate.yml |
| TOOL-20 boxes | three `- [ ]` still open |
| SOURCE-VETTING / CONTRACT http | 0 / 0 |
| `tooling/generate*` | absent |

---

## Finding classification

### Blocking gaps (need plan --gaps / execute --gaps-only)

None.

### Blocking defects still open in prior reviews

None. All four reviews: no BLOCKER / critical; security threats_open = 0.

### Ship-able residuals (notes — do not reopen execute)

| ID | Source | Issue | Disposition |
|----|--------|-------|-------------|
| WR-01 | CODE_REVIEW / IMPL N-01 | `errs`/`fail` in `check_overlap.main` write-only; print+return drive FAIL path | **Residual note** — exit codes and release wire correct today. Optional style cleanup later (Phase 18 or tiny fix). |
| WR-02 | CODE_REVIEW | Missing `packs/` → standalone silent OVERLAP PASS | **Residual note** — normal `check_release` path still fails without packs elsewhere. Fail-closed optional later. |
| IN-01 / N-02 | CODE / IMPL | SUMMARY `requirements-completed` vs open REQUIREMENTS boxes | **Not a gap** — plan-correct; phase.complete ticks boxes. |
| IN-02..04 | CODE_REVIEW | authored-header omit; `5d`/`5e` comment numbers; basename-only WHITELIST | **Not gaps** — intentional / YAGNI / out of TOOL-20 must-have. |
| SEC N1–N5 | SECURITY_AUDIT | ACCEPTED T-17-04 / T-17-SC docs; CI split assert; etc. | **Not gaps** — accepted or informational. |

### Rejected as non-gaps

| Claim | Why rejected |
|-------|----------------|
| Full FUT-05 byte-stable generator missing | ROADMAP/TOOL-20-03 else-branch: honest residual is legal done; CONTRACT §8 refuses claim |
| TOOL-20 boxes still unchecked | Verify must not tick; phase.complete owns ticks |
| `map_version` not 1.19.1 | Phase 18 owns bump/tag/release surface |
| CI does not run `check_overlap` | Intentional fence (T-17-02 / MJ-01); local/trusted only |
| WR-01 / WR-02 as blockers | Current-repo behavior correct; robustness nits only |

---

## Drift check (plan vs reality)

| Plan intent | Reality | Drift? |
|-------------|---------|--------|
| `check_overlap.py` + WHITELIST | Present; live PASS | No |
| In-process wire before map | `# 5d` then `# 5e` | No |
| CONTRACT §7 + §8 | Present and accurate | No |
| No version/map bump | 1.19.0 held | No |
| No packs/ / validate.yml edits | Confirmed in reviews | No |
| No full generator | No generate file; residual honest | No |
| Deviations ledger | SUMMARY `None.` + resume note | No |

No plan drift requiring re-entry.

---

## Verdict rationale

TOOL-20-01..03 and all three ROADMAP Phase 17 success criteria are live-true. Post-execute reviews agree ship-ready (PASS / PASS_WITH_NOTES / SECURED). WR-01 and WR-02 are documented residuals, not execute blockers. No OPEN_GAPS and no NEEDS_WORK defects.

**Verdict: CLOSED** — residual notes may ship; no execute re-entry required.

---

## Next commands

None for gaps-only re-entry.

Orchestrator may proceed:

1. Verification artifact (this session writes `17-VERIFICATION.md`)
2. phase.complete — safe to mark Phase 17 complete and tick TOOL-20-01..03 after verification `passed` / `passed_with_notes`
3. Phase 18 — map_version 1.19.1 + release surface; optional WR-01/WR-02 cleanup if desired

---

_Analyzed: 2026-08-20_  
_Analyzer: gsd-gap-analyzer_  
_Phase: 17-tooling-in-02-fut-05_
