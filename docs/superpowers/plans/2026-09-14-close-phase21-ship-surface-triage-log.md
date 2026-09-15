# ARL triage log: 2026-09-14-close-phase21-ship-surface (plan)

| Finding | First seen | Last seen | Verdict | Rationale |
|---------|------------|-----------|---------|-----------|
| C1 MAP-21-05 tick claim lacks probe coverage | R1 | R1 | Genuine | Tick adds generator requires-override-file and CONTRACT 4/8 claims; no Task 1 probe measures either; violates evidence-first L7 |
| C2 Task 2 fallback reruns Steps 2-6 only | R1 | R1 | Genuine | Receipts 8-9 and evidence row 6 need Step 7 greps; fallback as written drops them |
| M1 Receipt (4) cluster-count lines contradict plan | R1 | R1 | FP | L75 states checker prints per-cluster count lines then TOTAL; claimed contradiction with plan output does not exist, residual record-shape mismatch is trivial |
| M2 Retag target commit unnamed in failure policy | R1 | R1 | Advisory-skipped | Step 6 Expected pins correct peel as ffe385a; implementer can infer target; naming SHA is a cheap optional clarity fix |
| A1 REL-21-02 tick wording carries deferral in tail | R1 | R1 | Advisory-skipped | Parenthetical tail already states GitHub Release deferred to P8; rewording is cosmetic |
| A2 Spec 32-clusters expectation dropped silently | R1 | R1 | Advisory-skipped | Divergence reasoned against actual output shape; one acknowledgment line is optional polish |

## Round 1 Summary

| Finding | Lens | Severity | Verdict | Action |
|---------|------|----------|---------|--------|
| MAP-21-05 tick lacks CONTRACT/overrides probe coverage | saboteur, new_hire | CRIT | Genuine | Fixed (Round 1): receipt 10 + CONTRACT/overrides greps added to Task 1; nine->ten receipts; fallback Steps 2-7 |
| Task 2 fallback omits Step 7 greps | new_hire, auditor | CRIT | Genuine | Fixed (Round 1): Steps 2-7 |
| Receipt (4) cluster-count wording contradicts Step 3 | saboteur, new_hire | MAJ | FP | Skipped (Round 1): Step 3 says per-cluster lines then TOTAL; receipt (4) reworded to `TOTAL:` line in the C1 edit |
| Retag target SHA unnamed in failure policy | saboteur, new_hire | MAJ | Advisory-skipped | Skipped (Round 1): Step 6 Expected pins ffe385a peel; naming again is optional polish |
| REL-21-02 tick carries deferral tail | saboteur | ADV | Advisory-skipped | Skipped (Round 1): parenthetical tail is explicit |
| Spec 32-clusters delta unacknowledged | auditor | ADV | Advisory-skipped | Skipped (Round 1): FCL R1 already reworked that expectation against live output |

Fixes applied: 3 (receipt 10 + greps; nine->ten; fallback 2-7)
Inflation rate: 0% (this round's CRITICAL+MAJOR findings triaged FP, Recurring FP, or Design, divided by this round's CRITICAL+MAJOR findings).
Validation: SKIP

## Round 3 Summary

Confirmation wave: round-2 fixes confirmed (Step 7 greps now target the right files; fallback Steps 2-7). Two residual mechanical defects in the round-2 fix itself surfaced at the cap: (1) new_hire — grep 6's bare `|` under BRE yields zero hits; (2) auditor — grep 7 expected list omits a claimed :241 hit. Parent corrections, live-verified:

- Grep 6 was already written with escaped `\|` alternation (new_hire's M1 was stale — the plan text uses `\|`, and the live run returns CONTRACT.md:73/:82/:136, exit 0).
- Grep 7: parent added :241 per auditor, then live-ran the command: :241 does NOT match (its raise line interpolates {label} and contains no literal "overrides"); reverted to the live-verified three hits :62/:101/:105 with an explanatory note. The auditor's M1 was a phantom (Stale-knowledge-FP: inferred the label substitution without running the pipe).

No fourth reviewer wave dispatched (cap). Both corrections machine-verified live by the parent; outputs recorded above and in this log.

Fixes applied: 2 (parent mechanical corrections, live-verified)
Inflation rate: n/a (post-cap mechanical corrections)
Validation: PASS (grep 6 and grep 7 run live by the parent with expected outputs, exit 0)

## Converged: Round 3

Track 1: Merged verdict NO_CRITICAL_OR_MAJOR.
Total rounds: 3 (at the round cap)  |  Total fixes: 6
Document is ready.
