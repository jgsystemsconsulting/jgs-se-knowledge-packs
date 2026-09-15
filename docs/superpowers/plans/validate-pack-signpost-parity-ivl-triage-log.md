# IVL triage log: validate-pack-signpost-parity

## Check commands

1. python tooling/test_validate_pack.py  (expect "validate_pack tests: OK", exit 0)
2. python tooling/validate_pack.py --all  (expect exit 0, "65/65 pack(s) passed.")
3. python tooling/check_release.py  (expect RELEASE CHECK: PASS, exit 0)

## Baseline

| Finding | First seen | Last seen | Verdict | Rationale |
|---------|------------|-----------|---------|-----------|

## Round 1 Summary

All three lenses (behavior, regression, contract) returned NO_CRITICAL_OR_MAJOR with 3/3/4 recorded checks, all exit 0. One advisory (errors="ignore" silent-byte-loss) skipped: spec D1 mandates the errors="ignore" read for parity-by-construction with check_release; the loud-failure trade was the spec's explicit choice.

Fixes applied: 0
Inflation rate: n/a (0 CRITICAL+MAJOR findings this round)
Validation: PASS
Commands: python tooling/test_validate_pack.py -> exit 0; python tooling/validate_pack.py --all -> exit 0 (65/65); python tooling/check_release.py -> exit 0

## Converged: Round 1

Track 1: Merged verdict NO_CRITICAL_OR_MAJOR.
Total rounds: 1  |  Total fixes: 0
Implementation verification ready.
