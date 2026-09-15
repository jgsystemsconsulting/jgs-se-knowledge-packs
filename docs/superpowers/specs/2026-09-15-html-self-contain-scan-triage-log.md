| Finding | First seen | Last seen | Verdict | Rationale |
|---------|------------|-----------|---------|-----------|
| C1: Req 7 demands convention in failure messages; Design section excludes it | R1 | R1 | Genuine | Direct contradiction between requirement and design; amend R7 to keep convention in docstring and probe only |
| M1: Tag-slice regex [^>]* stops at first > inside quoted attribute values | R1 | R1 | Genuine | Silent fail-open on attributes containing > in quotes; quote-aware slice or documented residual required |
| M2: Meta scan covers only og/twitter image; meta refresh URLs pass | R1 | R1 | Genuine | Silent fail-open path; http-equiv refresh is a common external-redirect vector |
| M3: Pass two only matches double-quoted @import forms | R1 | R1 | Genuine | Undefined coverage blocks a first implementer; specify which @import forms are scanned |
| M4: R5 parity pins only tag-slice and meta-image literals, not pass-two regexes | R1 | R1 | Genuine | Parity check weaker than the requirement it enforces; pin pass-two literals too |
| A1: Failure example mixes context strings with bare URLs | R1 | R1 | Advisory-skipped | Cosmetic example inconsistency; URL-only or (url,context) if touched anyway |
| A2: Entity-encoded URLs bypass scanner | R1 | R1 | Design | Accepted residual; note in residuals list |
| A3: Attribute quote forms unspecified | R1 | R1 | Advisory-skipped | Covered by M1 fix; state quote forms when fixing M1 |
| A4: Asset table rows incomplete | R1 | R1 | Advisory-skipped | Add rows or declare table closed; one-line change |
| A5: Pass two under-specified | R1 | R1 | FP | Duplicate of M3/M4; fixing those resolves it |
| A6: Regexes not defined for pins | R1 | R1 | FP | Duplicate of M4; publishing parity literals covers it |
| A7: Userinfo tricks in URLs | R1 | R1 | Advisory-skipped | Edge case; document as residual if not handled |
| A8: Parity pins fewer than R5 | R1 | R1 | FP | Duplicate of M4 at same lines |
| A9: test_ci_gate docstring lists four gates | R1 | R1 | Advisory-skipped | One-line docstring update |

## Round 1 Summary

| Finding | Lens | Severity | Verdict | Action |
|---------|------|----------|---------|--------|
| C1 R7 vs failure-message convention | new_hire, auditor | CRIT | Genuine | Fixed (Round 1) |
| M1 tag-slice quote-aware | saboteur | MAJ | Genuine | Fixed (Round 1) |
| M2 meta refresh | saboteur | MAJ | Genuine | Fixed (Round 1) |
| M3 @import forms | new_hire | MAJ | Genuine | Fixed (Round 1) |
| M4 pass-two parity pins | auditor | MAJ | Genuine | Fixed (Round 1) |
| A1 message context | new_hire | ADV | Advisory-skipped | Fixed cheaply with URL-only (Round 1) |
| A2 entity-encoded residual | auditor | ADV | Design | Documented residual (Round 1) |
| A3 quote forms | new_hire | ADV | Advisory-skipped | Covered by M1 (Round 1) |
| A4 taxonomy closed | auditor | ADV | Advisory-skipped | Declared closed (Round 1) |
| A5 pass-two under-spec | saboteur | ADV | FP | Dup M3/M4 |
| A6 regex pins | new_hire | ADV | FP | Dup M4 |
| A7 userinfo | saboteur | ADV | Advisory-skipped | Handled in classification (Round 1) |
| A8 parity fewer | saboteur | ADV | FP | Dup M4 |
| A9 test_ci_gate docstring | auditor | ADV | Advisory-skipped | Files touched updated (Round 1) |

Fixes applied: 5
Inflation rate: 0% (0/5 CRITICAL+MAJOR triaged FP/Design/Recurring)
Validation: SKIP

| R2-confirm: five R1 locs all resolved | R2 | R2 | Genuine | Confirmation wave: all five R1 fixes resolved by this change |
| R2-M1: ATTR conditional empty-val for unquoted attrs | R2 | R2 | Genuine | Fixed: three-branch ATTR only; AC unquoted fixture; ATTR parity pin |

## Round 2 Summary

| Finding | Lens | Severity | Verdict | Action |
|---------|------|----------|---------|--------|
| Five R1 confirmations | saboteur, new_hire, auditor | — | resolved | Confirmed (Round 2) |
| R2-M1 ATTR unquoted empty val | auditor | MAJ | Genuine | Fixed (Round 2) |
| R2-A refresh url= case/quotes | saboteur, new_hire | ADV | Advisory-skipped | Fixed cheaply (Round 2) |
| R2-A ATTR parity pin | auditor | ADV | Advisory-skipped | Fixed cheaply (Round 2) |
| R2-A test_ci_gate four strings | auditor | ADV | Advisory-skipped | Files touched expanded (Round 2) |

Fixes applied: 1
Inflation rate: n/a (0 CRITICAL+MAJOR findings this round from lenses before fix; 1 new MAJOR from confirmation)
Validation: SKIP

## Round 3 Summary

| Finding | Lens | Severity | Verdict | Action |
|---------|------|----------|---------|--------|
| R2-M1 ATTR confirm | saboteur, new_hire, auditor | MAJ | resolved | Confirmed (Round 3) |

Fixes applied: 0
Inflation rate: n/a (0 CRITICAL+MAJOR findings this round)
Validation: SKIP

## Converged: Round 3

Track 1: Merged verdict NO_CRITICAL_OR_MAJOR.
Total rounds: 3  |  Total fixes: 6
Document is ready.
