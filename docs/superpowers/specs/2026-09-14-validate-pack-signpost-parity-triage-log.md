# ARL triage log: 2026-09-14-validate-pack-signpost-parity

| Finding | First seen | Last seen | Verdict | Rationale |
|---------|------------|-----------|---------|-----------|
| M1: Verification hardcodes 65/65 and 2/2 counts (L116-L118) | R1 | R1 | Genuine | Not an implementer blocker, but the acceptance gate fails spuriously if a pack lands before implementation; fix is one line, assert exit 0 and passed equals total. |
| A1: Whole-file regex lets a prose-quoted `kind: signpost` line skip content checks (L49) | R1 | R1 | Design | D1 deliberately matches check_release's whole-file regex so Goal 4 parity holds by construction; both tools share the false positive, and scoping to frontmatter would fork the detectors. |
| A2: Sketch reads strict UTF-8 while check_release uses errors='ignore', so 'classify identically by construction' overstates parity (L100) | R1 | R1 | Genuine | Verified check_release L125/L135 uses errors='ignore'; one-word fix in the sketch restores the by-construction claim. |
| A3: Citation drift, spec cites check_release regex at L132-135, actual match is L134-135 (L37) | R1 | R1 | Advisory-skipped | Verified L132-133 is a comment; two-character citation fix, apply only if the line is touched anyway. |

## Round 1 Summary

| Finding | Lens | Severity | Verdict | Action |
|---------|------|----------|---------|--------|
| Verification hardcodes 65/65 and 2/2 | saboteur, auditor | MAJ | Genuine | Fixed (Round 1) |
| Sketch strict UTF-8 vs check_release errors='ignore' | saboteur | ADV | Genuine | Fixed (Round 1) |
| Whole-file regex loophole for quoted 'kind: signpost' | saboteur | ADV | Design | Wontfix (Round 1): accepted shared edge case recorded in D1; parity-by-construction outranks it |
| Citation L132-135 should be L134-135 | auditor | ADV | Genuine | Fixed (Round 1) |

Fixes applied: 4
Inflation rate: 0% (this round's CRITICAL+MAJOR findings triaged FP, Recurring FP, or Design, divided by this round's CRITICAL+MAJOR findings).
Validation: SKIP

## Round 2 Summary

Confirmation wave: prompted locs L37, L49, L99, L116-118 returned `resolved by this change` from all three lenses; no `still stands`, no CRITICAL/MAJOR, no advisories. Coverage complete.

Fixes applied: 0
Inflation rate: n/a (0 CRITICAL+MAJOR findings this round)
Validation: SKIP

## Converged: Round 2

Track 1: Merged verdict NO_CRITICAL_OR_MAJOR.
Total rounds: 2  |  Total fixes: 4
Document is ready.
