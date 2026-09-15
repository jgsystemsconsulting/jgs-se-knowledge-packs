# ARL triage log: 2026-09-14-map-tooling-residual-harden (plan)

| Finding | First seen | Last seen | Verdict | Rationale |
|---------|------------|-----------|---------|-----------|
| C1 probe (c) stale case tampers preserved header only | R1 | R1 | Genuine | Verified: _split_md_header returns tampered header, render_md rebuilds from it, fresh equals existing, rc 1 unreachable |
| M1 probe (e) hardcodes 32 names and 2026-08-27 | R1 | R1 | Design | Snapshot pinning is the point of a byte-stability probe; legitimate changes update the probe with the tree |
| A1 Task 1 fail message cites overrides schema_version | R1 | R1 | Advisory-skipped | Wording nit in an expected-failure prediction; probe asserts nonzero rc, not the message text |
| A2 probe (c) write_text lacks newline=\n | R1 | R1 | Advisory-skipped | Read-back normalizes CRLF so the probe is self-consistent; add a one-line carve-out note only |
| A3 L508 note claims full-text compare catches header edits | R1 | R1 | Genuine | Header is preserved verbatim by _split_md_header so header edits pass by construction; note states the opposite |

## Round 1 Summary

| Finding | Lens | Severity | Verdict | Action |
|---------|------|----------|---------|--------|
| Probe (c) stale case tampers header, which round-trips; rc==1 unreachable | saboteur, new_hire, auditor | CRIT | Genuine | Fixed (Round 1): body tamper after ## Summary marker |
| Probe (e) hardcodes 32 names / 2026-08-27 | saboteur, new_hire | MAJ | Design | Wontfix (Round 1): HEAD-pinned probe, matching the repo's current-tree-annotation philosophy |
| L173 red-test message guarantees only first forbidden char | new_hire | ADV | Advisory-skipped | Skipped (Round 1): assert is containment by design, noted in plan |
| Probe (c) temp writes lack newline='\n' | saboteur | ADV | Advisory-skipped | Skipped (Round 1): CRLF-on-disk carve-out accepted; local gate reads with universal newlines too |
| L508 note wrongly claims header edits fail the gate | auditor | ADV | Genuine | Fixed (Round 1): note corrected to body-drift-only with rationale |

Fixes applied: 2
Inflation rate: 50% (this round's CRITICAL+MAJOR findings triaged FP, Recurring FP, or Design, divided by this round's CRITICAL+MAJOR findings).
Validation: SKIP

## Round 2 Summary

Confirmation wave: prompted locs L448-456 and L508 returned `resolved by this change` from all three lenses; no `still stands`, no new findings.

Fixes applied: 0
Inflation rate: n/a (0 CRITICAL+MAJOR findings this round)
Validation: SKIP

## Converged: Round 2

Track 1: Merged verdict NO_CRITICAL_OR_MAJOR.
Total rounds: 2  |  Total fixes: 2
Document is ready.
