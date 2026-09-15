# ARL triage log: 2026-09-14-validate-pack-signpost-parity (plan)

| Finding | First seen | Last seen | Verdict | Rationale |
|---------|------------|-----------|---------|-----------|
| M1: CONTENT_SKILL chapter link makes case 3 exact-list assert fail before and after fix; Step 2 prediction wrong | R1 | R1 | Genuine | Verified: fixture links (chapters/ch01-intro.md), validator L92-94 emits missing-chapter error when chapters=False, so case 3 gets two errors not one; red point is case (3), not (4) |
| A1: Step 7 expected AssertionError shows unescaped "source's" vs Step 2's escaped form | R1 | R1 | Advisory-skipped | Illustrative output only; cheap to align but non-blocking |
| A2: Step 3 item 5 `git diff --name-only` assumes clean tree | R1 | R1 | Advisory-skipped | Precondition nit; one-line note would fix but not blocking |

## Round 1 Summary

| Finding | Lens | Severity | Verdict | Action |
|---------|------|----------|---------|--------|
| CONTENT_SKILL chapter link breaks case-3 exact assert; red point is case 3 not 4 | saboteur | MAJ | Genuine | Fixed (Round 1): link line removed from fixture; pre-fix red point stays case (4) |
| Step 7 unescaped "source's" vs Step 2 escaped form | auditor | ADV | Genuine | Fixed (Round 1): matched Step 2's repr-escaped form |
| git diff precondition unstated | auditor | ADV | Genuine | Fixed (Round 1): precondition added |

Note: new_hire's first wave return was malformed (no JSON); retried once per protocol and returned a valid clean JSON.

Fixes applied: 3
Inflation rate: 0% (this round's CRITICAL+MAJOR findings triaged FP, Recurring FP, or Design, divided by this round's CRITICAL+MAJOR findings).
Validation: SKIP

## Round 2 Summary

Confirmation wave: prompted locs L86-92, L325 (reported as L323 after a line shift; parent aliased), and L393 returned `resolved by this change` from all three lenses; no `still stands`, no new findings.

Fixes applied: 0
Inflation rate: n/a (0 CRITICAL+MAJOR findings this round)
Validation: SKIP

## Converged: Round 2

Track 1: Merged verdict NO_CRITICAL_OR_MAJOR.
Total rounds: 2  |  Total fixes: 3
Document is ready.
