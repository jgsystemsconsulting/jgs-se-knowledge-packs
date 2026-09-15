# Context log: validate-pack-signpost-parity

| Finding | First seen | Last seen | Verdict | Rationale |
|---------|-----------|-----------|---------|-----------|
| check_pack LICENSE+chapters hard req L67-74 | R1 | R1 | CORROBORATED | whole-file read + live FAIL strings |
| --all iterates every packs dir L117-118 | R1 | R1 | CORROBORATED | code + --all run |
| exit 1 iff any FAIL L127-138 | R1 | R1 | CORROBORATED | code + EXIT:1 |
| docstring requires LICENSE+chapters always | R1 | R1 | SINGLE-SOURCE | module header |
| signpost_dirs regex on SKILL.md L134-135 | R1 | R1 | CORROBORATED | check_release + live kind lines |
| pack loop pre-filters signposts L184-185 | R1 | R1 | CORROBORATED | code; packages :141 stale |
| only two live signposts | R1 | R1 | CORROBORATED | dir listing + kind grep |
| signpost shape = SKILL.md + PACK.yaml only | R1 | R1 | CORROBORATED | ls both dirs |
| content pack has LICENSE+chapters | R1 | R1 | CORROBORATED | requirements-writing ls |
| --all 63/65 exit 1 vs check_release exit 0 | R1 | R1 | CORROBORATED | live runs same HEAD |
| per-signpost errors only LICENSE+chapters | R1 | R1 | CORROBORATED | targeted validate run |
| docs commands: docstring/CONTRIBUTING/PACK-SPEC | R1 | R1 | SINGLE-SOURCE | rg + reads |
| CONCERNS concern true; counts/line refs stale | R1 | R1 | STALE/SS | 46/48 vs 63/65 |
| P6 in/out scope + stdlib minimal diff | R1 | R1 | CORROBORATED | packages.md P6 |
| PACK.yaml already has kind + required fields | R1 | R1 | SINGLE-SOURCE | both PACK.yaml reads |

## Round 1

Single context-gate pass. CORROBORATED 8, SINGLE-SOURCE 7, STALE 2, CONFLICTED 0. Coverage 5/5. CONTEXT_COMPLETE.

## What was read

| Path | When | Notes |
|------|------|-------|
| tooling/validate_pack.py | R1 | whole file (142 lines) |
| tooling/check_release.py | R1 | header + L120-250 pack/signpost paths; rg hits |
| .planning/codebase/CONCERNS.md | R1 | L1-80 tech debt + known bugs |
| packs/omg-signpost/* | R1 | SKILL.md + PACK.yaml only |
| packs/se-standards-signpost/* | R1 | SKILL.md + PACK.yaml only |
| packs/requirements-writing/* | R1 | content-pack contrast |
| packages.md P6 | R1 | problem/evidence/in_scope/out_scope |
| CONTRIBUTING.md, docs/PACK-SPEC.md | R1 | documented validate commands |
| README.md signpost blurb | R1 | product meaning |
| P4 context pair | R1 | format mirror |
| live validate_pack / check_release runs | R1 | exit-code disagreement |

Fixes applied: 0
Coverage: 5/5
Validation: PASS

Track 1: Merged verdict CONTEXT_COMPLETE.
