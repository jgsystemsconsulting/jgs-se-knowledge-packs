# FCL triage log: 2026-09-14-close-phase21-ship-surface

| Finding | First seen | Last seen | Verdict | Rationale |
|---------|------------|-----------|---------|-----------|
| M1: L61 basis claims 19/20 record artifact paths for completed gates | R1 | R1 | Genuine | Phase 19 artifacts map lists only plan through verify and omits the four review-gate paths; phase 20 is the real template. Cite phase 20 only. |
| M2: L14 truncates the stale verdict string misleadingly | R1 | R1 | FP | Spec uses ellipsis abbreviation of the L55 needs_work string and calls it stale, which is accurate; no misquote. Quote-accuracy FP. |
| A1: L9 cites render_md at :365, def is :254 | R1 | R1 | Advisory-skipped | :365 is the render_md call inside the --check path, so the citation is defensible; naming :254 def or calling :365 the call site is a cheap clarity fix. |
| A2: L42 says 19/20 keep one artifacts path per gate | R1 | R1 | Advisory-skipped | Same fact error as M1; phase 19 artifacts map never lists the review gates. Fix alongside M1 by citing phase 20 (and 21). |

## Round 1 Summary

| Finding | Lens | Severity | Verdict | Action |
|---------|------|----------|---------|--------|
| Artifacts basis over-cites phase 19 (no review-gate paths there) | skeptic | MAJ | Genuine | Fixed (Round 1): phase-20-only citations at L42 and L61 |
| Truncated verdict string quote at L14 | source | MAJ | FP | Skipped (Round 1): paraphrase with explicit file:55 pointer; not misleading |
| WR-03 line cite :365 is the call site | skeptic | ADV | Advisory-skipped | Skipped (Round 1): call-site citation is accurate for the claim |
| L42 same over-cite as M1 | skeptic | ADV | Genuine | Fixed (Round 1): covered by the M1 edit |

Fixes applied: 1 (two lines)
Inflation rate: 50% (this round's CRITICAL+MAJOR findings triaged FP, Recurring FP, or Design, divided by this round's CRITICAL+MAJOR findings).
Validation: SKIP

## Round 2 Summary

Confirmation wave: prompted locs L42 and L61 returned `resolved by this change` from all three lenses; no `still stands`, no CRITICAL/MAJOR. The skeptic's residual advisory (drop the "stops at plan/execute" clause) was applied by the parent immediately after the merge (cheap, clearly correct — phase 19's map also lists gap/verify).

| Finding | Lens | Severity | Verdict | Action |
|---------|------|----------|---------|--------|
| "stops at plan/execute" clause imprecise (map also lists gap/verify) | skeptic | ADV | Genuine | Fixed (Round 2, post-merge) |

Fixes applied: 1
Inflation rate: n/a (0 CRITICAL+MAJOR findings this round)
Validation: SKIP

## Converged: Round 2

Track 1: Merged verdict NO_CRITICAL_OR_MAJOR.
Total rounds: 2  |  Total fixes: 2
Document is ready.
