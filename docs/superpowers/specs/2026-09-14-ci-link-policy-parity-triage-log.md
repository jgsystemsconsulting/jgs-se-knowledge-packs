# ARL triage log: 2026-09-14-ci-link-policy-parity

| Finding | First seen | Last seen | Verdict | Rationale |
|---------|------------|-----------|---------|-----------|
| C1 goal "one place" contradicts design C two-copy edit | R1 | R1 | Genuine | Goal L15 overpromises; design C requires data file plus workflow frozenset edit or parity fails. Reword goal. |
| M1 token format unvalidated, malformed token silently unbans host | R1 | R1 | Genuine | L59 defines line layout but no charset or fail-closed on malformed lines; escaped garbage token matches nothing while parity stays green. |
| M2 CI data-file parse and missing/unreadable file behavior unspecified | R1 | R1 | Genuine | D3 defines fail-closed for local only; CI heredoc behavior on missing or unparseable file is unstated. |
| A1 18 tokens never listed plain | R1 | R1 | Genuine | Cheap and clearly correct: add sorted 18-token inventory under D2 or rollout step 1 so first implementer need not diff two sources. |
| A2 workflow self-scan safety asserted, heredoc assembly unspecified | R1 | R1 | Advisory-skipped | D2 states tokens carry no scheme prefix; specifying heredoc string assembly adds bloat for an incidental property. |
| A3 load_banned_hosts home, path binding, strip rules unspecified | R1 | R1 | Advisory-skipped | Subsumed by M1 fix, which defines line rules and fail-closed behavior for both loaders. |
| A4 divergence demo trigger mechanism unspecified | R1 | R1 | Advisory-skipped | Throwaway commit wording is adequate; naming scratch PR versus workflow_dispatch adds no correctness. |
| A5 divergence helper tests reimplementation, not CI heredoc code | R1 | R1 | Advisory-skipped | D5(2) already records the real CI run as the authoritative check; helper checks algorithm shape only. |
| A6 test (b) hardcodes 18 tokens, breaks on future additions | R1 | R1 | Advisory-skipped | Hardcoded count intentionally pins the current set, mirroring the workflow frozenset contract; parity CI catches future drift. |

## Round 1 Summary

| Finding | Lens | Severity | Verdict | Action |
|---------|------|----------|---------|--------|
| Goal "one place" contradicts design C two-copy edit | saboteur, new_hire | CRIT | Genuine | Fixed (Round 1) |
| Token format unvalidated, malformed token silently unbans host | saboteur | MAJ | Genuine | Fixed (Round 1) |
| CI data-file parse / missing-file behavior unspecified | new_hire, auditor | MAJ | Genuine | Fixed (Round 1) |
| 18 tokens never listed plain | new_hire | ADV | Genuine | Fixed (Round 1) |
| Workflow self-scan safety asserted | saboteur | ADV | Advisory-skipped | Skipped (Round 1) |
| load_banned_hosts contract unspecified | new_hire | ADV | Advisory-skipped | Skipped (Round 1) |
| Divergence demo trigger unspecified | saboteur | ADV | Advisory-skipped | Skipped (Round 1) |
| D5(d) tests reimplementation only | auditor | ADV | Advisory-skipped | Skipped (Round 1) |
| Test (b) hardcodes 18 tokens | auditor | ADV | Advisory-skipped | Skipped (Round 1) |

Fixes applied: 4
Inflation rate: 0% (this round's CRITICAL+MAJOR findings triaged FP, Recurring FP, or Design, divided by this round's CRITICAL+MAJOR findings).
Validation: SKIP

Dropped out of scope: 0. Scope unchecked (non-line loc): 0.

## Round 2 Summary

Confirmation wave: prompted locs L15, L62, L67, L89 returned `resolved by this change` from all three lenses; no `still stands`, no CRITICAL/MAJOR. Coverage complete.

| Finding | Lens | Severity | Verdict | Action |
|---------|------|----------|---------|--------|
| Exemplar list violates stated sort (dla.mil before dod.mil/dodcio) | saboteur | ADV | Genuine | Fixed (Round 2) |

Fixes applied: 1
Inflation rate: n/a (0 CRITICAL+MAJOR findings this round)
Validation: SKIP

## Converged: Round 2

Track 1: Merged verdict NO_CRITICAL_OR_MAJOR.
Total rounds: 2  |  Total fixes: 5
Document is ready.

