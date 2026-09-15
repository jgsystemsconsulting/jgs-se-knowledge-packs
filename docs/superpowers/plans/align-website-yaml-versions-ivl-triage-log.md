# IVL triage log: align-website-yaml-versions

plan_or_spec: docs/superpowers/plans/2026-09-14-align-website-yaml-versions.md
Target: implemented worktree at commit ffe385abca97efc7a50b3939f930f78ec5666935 (branch main)
Round cap: 3 (full tier)

## Check commands

- `python tooling/check_release.py` (primary gate; expect exit 0, last line starts `RELEASE CHECK: PASS`)
- `git grep -n '1.19.1' -- docs/products/website` (expect no output, exit 1)
- `git grep -n 'version: "1.20.0"' -- docs/products/website` (expect exactly 2 hits: 01-jgs-se-knowledge-packs.yaml:15 top-level, catalog.yaml:13 4-space indent)
- `git cat-file -t v1.20.0` (expect `tag`) and `git rev-parse "v1.20.0^{commit}"` (expect ffe385ab...)
- `git branch -r --contains ffe385abca97efc7a50b3939f930f78ec5666935` (assert EMPTY output; exit code informational on this git build)
- `git status --porcelain` (expect exactly `?? docs/superpowers/`)
- `sed -n '44p' CHANGELOG.md`, `sed -n '35p' docs/capability-map-CONTRACT.md`, `sed -n '18p' docs/capability-pack-map.md` (keep-class, expect 1.19.1 strings)

## Baseline

- `python tooling/check_release.py` -> exit 0, last line `RELEASE CHECK: PASS — repo is release-ready against the mechanical gate.` (full pass including capability map/classification/replay checks; TOTAL 644)
- `git status -s` -> `?? docs/superpowers/` only
- Worktree integrity fingerprints (sha256, first 16): 01-jgs-se-knowledge-packs.yaml 4f9c3fafa03f0edd, catalog.yaml f1c9cc0e683e00fb, check_release.py 8d5054184bdce1bf

| Finding | First seen | Last seen | Verdict | Rationale |
|---------|------------|-----------|---------|-----------|

## Round 1 Summary

| Finding | Lens | Severity | Verdict | Action |
|---------|------|----------|---------|--------|
| (no findings; all three lenses clean with live checks_run evidence) | behavior, regression, contract | n/a | n/a | none |

Fixes applied: 0
Inflation rate: n/a (0 CRITICAL+MAJOR findings this round)
Validation: PASS
Commands: python tooling/check_release.py -> exit 0 (PASS, run independently by behavior + regression lenses); git grep/tag/porcelain checks -> as logged in each lens checks_run

Worktree integrity: post-wave sha256 fingerprints identical to baseline (4f9c3fafa03f0edd, f1c9cc0e683e00fb, 8d5054184bdce1bf); porcelain unchanged.

## Converged: Round 1

Track 1: Merged verdict NO_CRITICAL_OR_MAJOR.
Total rounds: 1  |  Total fixes: 0
Implementation verification ready.
