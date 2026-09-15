# IVL triage log: ci-local-gate-coverage-gap

## Check commands

1. python tooling/test_ci_gate.py  (expect OK, exit 0)
2. python tooling/check_overlap.py  (expect OVERLAP: PASS, exit 0)
3. python tooling/check_release.py  (expect RELEASE CHECK: PASS (v1.20.0 @ <sha>), exit 0)

## Baseline

| Finding | First seen | Last seen | Verdict | Rationale |
|---------|------------|-----------|---------|-----------|

## Round 1 Summary

All three lenses (behavior, regression, contract) returned NO_CRITICAL_OR_MAJOR with 11/7/3 recorded checks, all exit 0 (fail-closed demos exit 1 as designed). Zero findings; triage dispatch skipped with zero rows to classify.

Fixes applied: 0
Inflation rate: n/a (0 CRITICAL+MAJOR findings this round)
Validation: PASS
Commands: python tooling/test_ci_gate.py -> exit 0; python tooling/check_overlap.py -> exit 0; python tooling/check_release.py -> exit 0

## Converged: Round 1

Track 1: Merged verdict NO_CRITICAL_OR_MAJOR.
Total rounds: 1  |  Total fixes: 0
Implementation verification ready.
