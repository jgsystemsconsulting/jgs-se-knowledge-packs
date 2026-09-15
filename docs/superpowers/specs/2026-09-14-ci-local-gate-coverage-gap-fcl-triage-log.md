# FCL triage log: 2026-09-14-ci-local-gate-coverage-gap

| Finding | First seen | Last seen | Verdict | Rationale |
|---------|------------|-----------|---------|-----------|
| C1 map set equality ignores support-file exclusion (spec:L76) | R1 | R1 | Genuine | check_capability_map.py:191-196 strips SUPPORT_SUFFIX rows before chapter-set equality; spec L76 compares raw clusters[].chapters[] to disk, so support rows cause false CI red |
| M1 red-always-drift claim broken by L76 as written (spec:L72-L76) | R1 | R1 | FP | Prerequisite-task FP: same defect as C1, one fix covers both |
| M2 website YAMLs claimed to lack version field (spec:L42) | R1 | R1 | FP | 01-jgs-se-knowledge-packs.yaml:15 and catalog.yaml:13 both carry version "1.20.0"; spec L42 path is the correct hyphenated filename |
| M3 extras 5b/5c/6b claimed nonexistent (spec:L11) | R1 | R1 | FP | check_release.py L194, L206, L231 define the sub-checks; lens grep missed comment-anchored blocks |
| A1 L11 omits 5c among module-importing checks (spec:L11) | R1 | R1 | Advisory-skipped | Correct (5c imports gen_packs_page at check_release.py:216); cheap one-word fix beside 5/8-11 |
| A2 CI map_version pin weaker than local N.N.N fullmatch (spec:L74) | R1 | R1 | Design | Spec L79 states the CI subset is deliberately weaker and must stay a strict subset |

## Round 1 Summary

| Finding | Lens | Severity | Verdict | Action |
|---------|------|----------|---------|--------|
| Map set equality ignores support-file exclusion | skeptic | CRIT | Genuine | Fixed (Round 1) |
| "red always real drift" broken by L76 | skeptic | MAJ | FP | Skipped (Round 1): same defect as C1, one fix covers both (Prerequisite-task FP) |
| Website YAMLs claimed to lack version field | source | MAJ | FP | Skipped (Round 1): parent grep shows version "1.20.0" at 01-jgs-se-knowledge-packs.yaml:15 and catalog.yaml:13 |
| Extras 5b/5c/6b claimed nonexistent | correspondent | MAJ | FP | Skipped (Round 1): check_release.py L194/L206/L231 define them |
| L11 omits 5c among module-importing checks | skeptic | ADV | Genuine | Fixed (Round 1) |
| map_version CI pin weaker than local N.N.N | skeptic | ADV | Design | Wontfix (Round 1): spec L79 states the CI subset is deliberately weaker |

Fixes applied: 2
Inflation rate: 67% (this round's CRITICAL+MAJOR findings triaged FP, Recurring FP, or Design, divided by this round's CRITICAL+MAJOR findings).
Validation: SKIP

## Round 2 Summary

Confirmation wave: L76 resolved by all three lenses. L11: the parent's fix over-grouped 5b (pure SKILL.md regex, no repo import) with module-importing checks — skeptic MAJOR genuine; corrected to "Checks 5, 5c, 8, 9, 10, 11 import; 5b stdlib-only (CI-closable in principle, not added here)". Source and correspondent confirmations again read "still stands" with evidence text confirming the fixed state (enum inversion, parent-adjudicated).

| Finding | Lens | Severity | Verdict | Action |
|---------|------|----------|---------|--------|
| 5b wrongly grouped with module-importing checks | skeptic | MAJ | Genuine | Fixed (Round 2) |

Fixes applied: 1
Inflation rate: 0% (this round's CRITICAL+MAJOR findings triaged FP, Recurring FP, or Design, divided by this round's CRITICAL+MAJOR findings).
Validation: SKIP

## Round 3 Summary

Confirmation wave: prompted loc L11 returned `resolved by this change` from all three lenses (correct enum); no `still stands`, no new findings.

Fixes applied: 0
Inflation rate: n/a (0 CRITICAL+MAJOR findings this round)
Validation: SKIP

## Converged: Round 3

Track 1: Merged verdict NO_CRITICAL_OR_MAJOR.
Total rounds: 3  |  Total fixes: 3
Document is ready.
