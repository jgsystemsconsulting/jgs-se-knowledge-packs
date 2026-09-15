# FCL triage log: 2026-09-14-ci-local-gate-coverage-gap (plan)

| Finding | First seen | Last seen | Verdict | Rationale |
|---------|------------|-----------|---------|-----------|
| C1 heredoc success print corrupted at L936 | R1 | R1 | FP | Inflation-FP: `[map-data]/[rules-data] data invariants OK` is valid Python and runs; slash replaces an em dash per the plan's zero-em-dash rule, and the probe asserts only named substrings. |
| M1 demo count breakdown wrong at L959 | R1 | R1 | Genuine | Probe source has 2 version, 1 index, 2 overlap, 4 map/rules negatives (9 total); plan says two index and three overlap, which misleads the executor. |
| M2 CI version message omits `{rel}:` at L717 | R1 | R1 | Design | WONTFIX: CI carries the path via the `::error file=<rel>::` annotation, which Global Constraint L37 sanctions; the parity contract is regex literals, not message bodies, and the probe is self-consistent. |
| M3 WHITELIST line refs off by one at L27 | R1 | R1 | FP | Actual file has the comment at L31 and the constant at L32-34, so the block is lines 31-34 exactly as the plan states. |
| M4 quoted banner has extra period at L1004 | R1 | R1 | FP | check_release.py:368 ends with a period; the plan quote matches the source byte for byte. |
| A1 website YAML version 1.20.0 unverified at L24 | R1 | R1 | FP | Both YAMLs verified: 01-jgs-se-knowledge-packs.yaml:15 and catalog.yaml:13 carry version "1.20.0". |

## Round 1 Summary

| Finding | Lens | Severity | Verdict | Action |
|---------|------|----------|---------|--------|
| Demo-count breakdown wrong (two index / three overlap) | skeptic | MAJ | Genuine | Fixed (Round 1): one index, two overlap |
| Heredoc success print "corrupted" | skeptic | CRIT | FP | Skipped (Round 1): `[map-data]/[rules-data] ...` is valid Python; slash is a deliberate zero-em-dash style choice |
| CI version message omits `{rel}:` | skeptic | MAJ | Design | Wontfix (Round 1): path carried via ::error file= annotation; parity contract is regex literals |
| WHITELIST line refs off by one | source | MAJ | FP | Skipped (Round 1): block is lines 31-34 (comment L31 + constant L32-34) as stated |
| Banner quote has extra period | source | MAJ | FP | Skipped (Round 1): check_release.py:368 ends with the period; quote matches byte-for-byte |
| Website YAML version unverified | source | ADV | FP | Skipped (Round 1): both YAMLs verified carrying version "1.20.0" |

Fixes applied: 1
Inflation rate: 80% (this round's CRITICAL+MAJOR findings triaged FP, Recurring FP, or Design, divided by this round's CRITICAL+MAJOR findings).
Validation: SKIP

## Round 2 Summary

Confirmation wave: prompted loc L959 returned `resolved by this change` from all three lenses; no `still stands`, no new findings.

Fixes applied: 0
Inflation rate: n/a (0 CRITICAL+MAJOR findings this round)
Validation: SKIP

## Converged: Round 2

Track 1: Merged verdict NO_CRITICAL_OR_MAJOR.
Total rounds: 2  |  Total fixes: 1
Document is ready.
