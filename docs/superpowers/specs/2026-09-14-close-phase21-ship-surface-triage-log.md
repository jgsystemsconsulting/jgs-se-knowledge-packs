# ARL triage log: 2026-09-14-close-phase21-ship-surface

| Finding | First seen | Last seen | Verdict | Rationale |
|---------|------------|-----------|---------|-----------|
| M1 Expected demands strings check_release never prints | R1 | R1 | Genuine | check_release.py:387 prints only `RELEASE CHECK: PASS (vX @ sha)`; catalog 63/dirs 65, map_version, step 4a/5g lines are phantom receipts that would stall an executor on output that never appears. |
| M2 commits_reviewed omits ffe385a | R1 | R1 | FP | Re-gate section plus the fresh live-tree command table is the reconciliation; commits_reviewed is a dated historical scope field the spec deliberately preserves. |
| M3 artifacts after-state lacks concrete path strings | R1 | R1 | FP | Phase 20 state and spec L16 fix the deterministic convention `.planning/phases/21-.../21-<GATE>.md`; no implementer choice exists. |
| A1 Commands 2-3 Expected wording mismatches live PASS lines | R1 | R1 | Advisory-skipped | Subsumed by the M1 fix rewriting the Expected column for the whole table. |
| A2 Static greps give no exact rg patterns | R1 | R1 | Advisory-skipped | Grounding section already pins each target at file:line; exact commands are derivable without spec bloat. |
| A3 Coverage row "Complete (gh release: P8)" self-contradicts | R1 | R1 | Design | Explicit parenthetical marks the open tail per decision 3; the REQUIREMENTS text carries the same tail, so no silent claim. |
| A4 Tag remediation rests on unprovable "not pushed" | R1 | R1 | FP | Remediation trigger is the local peel probe (command 5), not a network claim; remote tag reconciliation belongs to P8's push. |
| A5 CR-01 retag recipe lacks inline git commands | R1 | R1 | Advisory-skipped | Standard `git tag -d` / `git tag -a` sequence; inlining adds bloat with no correctness gain. |
| A6 21-CODE_REVIEW status/verdict mismatch unaddressed | R1 | R1 | Design | The state file mirrors verdicts, which is the truthful field; editing the original wave's status without a re-review would fabricate. |

## Round 1 Summary

| Finding | Lens | Severity | Verdict | Action |
|---------|------|----------|---------|--------|
| Command 1 Expected lists strings check_release never prints | new_hire | MAJ | Genuine | Fixed (Round 1): exit 0 + PASS banner line + per-check 4a/5g lines |
| commits_reviewed omits ffe385a | saboteur, auditor | MAJ | FP | Skipped (Round 1): fresh live-tree command table is the reconciliation; dated scope field deliberately preserved |
| artifacts after-state lacks concrete path strings | new_hire | MAJ | FP | Skipped (Round 1): phase 20 + spec L16 fix the deterministic 21-<GATE>.md convention |
| Commands 2-3 Expected wording | new_hire | ADV | Advisory-skipped | Skipped (Round 1): subsumed by M1 table rewrite |
| Static greps lack exact patterns | new_hire | ADV | Advisory-skipped | Skipped (Round 1): grounding section pins targets at file:line |
| Coverage row "Complete (gh release: P8)" | saboteur | ADV | Design | Wontfix (Round 1): explicit parenthetical marks the open tail; REQUIREMENTS carries the same tail |
| Tag "not pushed" unprovable | saboteur | ADV | FP | Skipped (Round 1): remediation trigger is the local peel probe; remote reconciliation is P8's |
| Retag recipe not inlined | new_hire | ADV | Advisory-skipped | Skipped (Round 1): standard sequence, no correctness gain |
| CODE_REVIEW status/verdict mismatch | auditor | ADV | Design | Wontfix (Round 1): state file mirrors verdicts; editing the wave's status without re-review would fabricate |

Fixes applied: 1
Inflation rate: 67% (this round's CRITICAL+MAJOR findings triaged FP, Recurring FP, or Design, divided by this round's CRITICAL+MAJOR findings).
Validation: SKIP

## Round 2 Summary

Confirmation wave: L27 half-resolved — banner and 5g halves fixed, but all three lenses caught the residual phantom: 4a is silent on success (fail-only), so a "4a PASS line" cannot exist; command 3's fidelity wording same class; artifact path strings advisory folded.

| Finding | Lens | Severity | Verdict | Action |
|---------|------|----------|---------|--------|
| 4a PASS line phantom (silent on success) | saboteur, new_hire, auditor | CRIT | Genuine | Fixed (Round 2): 4a success = no [version] failures + final banner |
| Command 3 fidelity wording same class | new_hire | MAJ | Genuine | Fixed (Round 2): PASS line named, fidelity silent-on-success noted |
| Artifact path strings unstated | new_hire | ADV | Genuine | Fixed (Round 2): concrete 21-*.md names added |

Fixes applied: 3
Inflation rate: 0% (this round's CRITICAL+MAJOR findings triaged FP, Recurring FP, or Design, divided by this round's CRITICAL+MAJOR findings).
Validation: SKIP

## Round 3 Summary

Confirmation wave: prompted locs L27, L29, L61 returned `resolved by this change` from all three lenses; no `still stands`, no new findings.

Fixes applied: 0
Inflation rate: n/a (0 CRITICAL+MAJOR findings this round)
Validation: SKIP

## Converged: Round 3

Track 1: Merged verdict NO_CRITICAL_OR_MAJOR.
Total rounds: 3 (at the round cap)  |  Total fixes: 4
Document is ready.
