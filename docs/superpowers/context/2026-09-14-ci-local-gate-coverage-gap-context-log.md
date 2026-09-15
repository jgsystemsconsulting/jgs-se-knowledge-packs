# Context log: ci-local-gate-coverage-gap

| Finding | First seen | Last seen | Verdict | Rationale |
|---------|-----------|-----------|---------|-----------|
| Docstring names eleven checks | R1 | R1 | CORROBORATED | check_release.py header + packages P5 |
| Extras 5b/5c/6b beyond eleven | R1 | R1 | SINGLE-SOURCE | main() blocks after pack validate |
| CI four steps + P4 inside link | R1 | R1 | CORROBORATED | validate.yml whole file |
| Trust boundary never exec repo py | R1 | R1 | CORROBORATED | workflow header + docstring + CONCERNS |
| Version trio + two website YAMLs | R1 | R1 | CORROBORATED | check 4/4a + live 1.20.0 files |
| SKILLS count signpost-aware | R1 | R1 | SINGLE-SOURCE | L193-199; live 63==63 |
| Overlap basename+WHITELIST pure | R1 | R1 | CORROBORATED | check_overlap.py whole |
| Map/class/replay import local tools | R1 | R1 | CORROBORATED | check_release 5e/5f/5g |
| Map/rules pure envelope+set subset | R1 | R1 | SINGLE-SOURCE | JSON envelopes + checker docs |
| validate_pack/packs.html/replay need code | R1 | R1 | CORROBORATED | imports in check_release |
| No automated pre-tag fail-closed | R1 | R1 | CORROBORATED | no hook; validate.yml no tag event; docs only |
| TESTING.md CI-gap note stale lines | R1 | R1 | STALE/SS | ~L80 true gap, old line nums |
| CONCERNS host-dupe resolved P4 | R1 | R1 | CORROBORATED | CONCERNS resolved block |
| P4 pin+parity precedent keep | R1 | R1 | CORROBORATED | validate.yml link step + packages |
| Package min closable = version/SKILLS/overlap(+map pure) | R1 | R1 | SINGLE-SOURCE | packages.md P5 in_scope |
| Live signposts omg + se-standards | R1 | R1 | SINGLE-SOURCE | packs/*/SKILL.md |
| Structural risk = CI/local algorithm drift | R1 | R1 | SINGLE-SOURCE | design; P4 history |
| CHANGELOG Unreleased above 1.20.0 | R1 | R1 | SINGLE-SOURCE | regex still picks first ## [N.N.N] |

## Round 1

Single context-gate pass. CORROBORATED 9, SINGLE-SOURCE 14, STALE 2, CONFLICTED 0. Coverage 5/5. CONTEXT_COMPLETE.

## What was read

| Path | When | Notes |
|------|------|-------|
| tooling/check_release.py | R1 | whole file (373 lines) |
| .github/workflows/validate.yml | R1 | whole file (134 lines) |
| tooling/check_overlap.py | R1 | whole (WHITELIST + scan) |
| tooling/check_capability_map.py | R1 | main/envelope rg |
| tooling/check_classification_rules.py | R1 | envelope/assignments rg |
| tooling/generate_capability_map.py | R1 | --check entry rg |
| docs/capability-pack-map.json | R1 | envelope keys |
| docs/classification-rules.json | R1 | envelope keys |
| RELEASE-INFO.txt, plugin.json, CHANGELOG, website YAMLs | R1 | version extract |
| SKILLS.md | R1 | link shape + count |
| .planning/codebase/TESTING.md | R1 | CI-gap note |
| .planning/codebase/CONCERNS.md | R1 | trust + P4 residual |
| packages.md P5 | R1 | in/out scope |
| P4 context + log pair | R1 | format reference |
| repo rg pre-tag / check_release | R1 | fail-closed census |

Fixes applied: 0
Coverage: 5/5
Validation: PASS

Track 1: Merged verdict CONTEXT_COMPLETE.
