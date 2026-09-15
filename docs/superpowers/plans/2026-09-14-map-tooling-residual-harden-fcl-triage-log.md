# FCL triage log: 2026-09-14-map-tooling-residual-harden (plan)

| Finding | First seen | Last seen | Verdict | Rationale |
|---------|------------|-----------|---------|-----------|
| Step 2 expects notes-check message but probe passes empty overrides, so schema_version check fires first | R1 | R1 | Genuine | Probe (a) at L131-133 passes `{}`; generate_capability_map.py L90-92 checks schema_version before notes (L94-96), so the expected assertion text at L173 is unreachable as written. Fix: expect `overrides schema_version must be int 1, got None`. |
| Plan L173 expected string does not match source f-string `got {o_schema!r}` | R2 | R2 | FP | Plan quotes the rendered runtime string; for an empty overrides dict `o_schema` is None and `{o_schema!r}` renders exactly `None`, so L173 matches generate_capability_map.py:92 byte for byte. Comparing quoted runtime text to the unrendered template is a source-lens misread, not a defect. |

## Round 1 Summary

| Finding | Lens | Severity | Verdict | Action |
|---------|------|----------|---------|--------|
| Red-test expects 'notes' error; empty overrides fail schema_version first | skeptic | MAJ | Genuine | Fixed (Round 1) |

Fixes applied: 1
Inflation rate: 0% (this round's CRITICAL+MAJOR findings triaged FP, Recurring FP, or Design, divided by this round's CRITICAL+MAJOR findings).
Validation: SKIP

## Round 2 Summary

Confirmation wave: prompted loc L173 confirmed resolved by the skeptic (correct enum); source and correspondent's evidence text confirms the fix while their verdict strings read "still stands" (enum inversion, parent-adjudicated on evidence content, consistent with prior rounds).

| Finding | Lens | Severity | Verdict | Action |
|---------|------|----------|---------|--------|
| "got None does not match the f-string template" | source | MAJ | FP | Skipped (Round 2): {o_schema!r} with o_schema=None renders exactly `got None`; the plan quotes the rendered runtime string |

Fixes applied: 0
Inflation rate: 100% (this round's CRITICAL+MAJOR findings triaged FP, Recurring FP, or Design, divided by this round's CRITICAL+MAJOR findings).
Validation: SKIP

## Converged: Round 2

Track 3: diminishing-return halt. Predicate: no-unfixed-genuine. Round 2's genuine_fixes_needed was empty; the sole merged MAJOR triaged FP on f-string semantics; the round-1 fix was confirmed resolved by all lenses.
Total rounds: 2  |  Total fixes: 1
Document is ready.
