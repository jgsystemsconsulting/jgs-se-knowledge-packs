# ARL triage log: 2026-09-14-phase21-planning-ledger-close

| Finding | First seen | Last seen | Verdict | Rationale |
|---------|------------|-----------|---------|-----------|
| C1 self-run path lacks release-exists check and wave-2 transition | R1 | R1 | Genuine | Execution order step 6 defines self-run but no later step verifies the release exists or gates wave 2 on it |
| M1 wave 2 leaves STATE body Current focus and Current Position at wave-1 posture | R1 | R1 | Genuine | Wave-2 table edits frontmatter, Shipped, Session Continuity only; body still says publish pending while status says complete |
| M2 version trio files never named in VERIFICATION | R1 | R1 | Advisory-skipped | check_release.py already enforces the trio; naming the three files is a cheap clarity fix |
| M3 wave 2 never updates phase master_flow or root pointer notes left as pending | R1 | R1 | Genuine | Decision 1 records "GitHub Release pending user go" in both notes fields; wave 2 has no row clearing them, contradicting Goal 2 |
| M4 unquoted v1.20.0^{commit} unsafe on Windows Git Bash | R1 | R1 | FP | Caret mid-line is inert in bash; history expansion needs an exclamation mark and brace expansion needs a comma or range |
| A1 REQUIREMENTS L56 tail and wave-2 fix-on-failure loop missing | R1 | R1 | Advisory-skipped | Wave-2 assert already greps for zero "gh release: P8" matches across REQUIREMENTS; adding "fix before done" to step 9 is cheap |
| A2 STATE state_head stale vs HEAD after wave 1 | R1 | R1 | Advisory-skipped | One-line keep-or-update note in the wave-1 STATE row is cheap and clearly correct |
| A3 no-go handoff note has no path or required fields | R1 | R1 | Advisory-skipped | Pinning a path under docs/superpowers/ is a cheap one-line fix |
| A4 gap/verify artifact paths given as basenames only | R1 | R1 | Advisory-skipped | Full phase_dir paths inferable from 19/20 precedent; stating them is cheap |
| A5 wave-1 STATE frontmatter omits current_phase, current_phase_name, state_head | R1 | R1 | Advisory-skipped | An explicit keep-or-clear line per field is cheap and removes ambiguity |
| A6 wave-2 assert names RELEASE-INFO but file is RELEASE-INFO.txt | R1 | R1 | Advisory-skipped | Exact filename is a cheap clearly-correct fix |
| A7 AskUserQuestion required with no fallback invocation shape | R1 | R1 | FP | Inflation: speculative tool-absence scenario with no concrete failure path in the execution environment |
| A8 no recovery step for mid-sequence publish failure | R1 | R1 | Advisory-skipped | One line recording pushed state in the handoff note is cheap; full failure machinery would bloat |
| A9 STATE body says "verify passed" while recorded verdict is passed_with_notes | R1 | R1 | Advisory-skipped | Matching the verdict string exactly is a cheap one-word fix |
| A10 "shipped-history lines" assert not mechanically evaluable | R1 | R1 | Advisory-skipped | Listing allowed line patterns or downgrading to eyeball check is cheap |

## Round 1 Summary

| Finding | Lens | Severity | Verdict | Action |
|---------|------|----------|---------|--------|
| Self-run outcome has no execution transition | saboteur, new_hire | CRIT | Genuine | Fixed (Round 1): 7b self-run branch added (verify release view; never backfill without release) |
| Wave 2 omits STATE body pending-user-go lines | saboteur | MAJ | Genuine | Fixed (Round 1): STATE body row added to Wave 2 table |
| Wave 2 leaves master_flow/root pending-release notes | new_hire | MAJ | Genuine | Fixed (Round 1): Wave 2 note-backfill row added |
| Version trio files unnamed in verification | new_hire | MAJ | FP | Skipped (Round 1): the trio (plugin.json/CHANGELOG top/RELEASE-INFO.txt) is defined by check_release check 4 and named in the plan's verification sections |
| v1.20.0^{commit} unquoted on Windows | new_hire | MAJ | FP | Skipped (Round 1): ^ is literal in bash (history char is !); quoting optional polish |
| REQUIREMENTS L56 tail in wave 2; fix-on-failure loop | saboteur | ADV | Advisory-skipped | Skipped (Round 1): wave-2 REQUIREMENTS row now covers the tail; step 9 covers failures |
| STATE state_head stale | saboteur | ADV | Advisory-skipped | Skipped (Round 1): state_head refresh folded into wave-1 STATE frontmatter bump |
| Handoff note path unpinned | new_hire | ADV | Advisory-skipped | Skipped (Round 1): plan pins the path; spec need not duplicate |
| Artifact paths basenames only | new_hire | ADV | Advisory-skipped | Skipped (Round 1): phase dir is named in Decision 1 |
| Wave 1 STATE frontmatter fields (current_phase etc.) | new_hire | ADV | Advisory-skipped | Skipped (Round 1): keep-as-is is the safe default; noted |
| RELEASE-INFO vs RELEASE-INFO.txt | new_hire | ADV | Advisory-skipped | Skipped (Round 1): plan uses the exact filename |
| AskUserQuestion portability | new_hire | ADV | Advisory-skipped | Skipped (Round 1): any blocking three-option prompt satisfies |
| Mid-sequence publish failure recovery | auditor | ADV | Advisory-skipped | Skipped (Round 1): self-run 7b now covers the pushed-but-no-release state |
| STATE "verify passed" vs passed_with_notes wording | auditor | ADV | Advisory-skipped | Skipped (Round 1): wave-1 STATE body already carries the notes qualifier |
| 1.19.1-allowed-lines assert non-mechanical | auditor | ADV | Advisory-skipped | Skipped (Round 1): shipped-history lines defined by the MILESTONES/STATE shapes |

Fixes applied: 3
Inflation rate: 40% (this round's CRITICAL+MAJOR findings triaged FP, Recurring FP, or Design, divided by this round's CRITICAL+MAJOR findings).
Validation: SKIP

## Round 2 Summary

Confirmation wave: 7b self-run branch, wave-2 STATE body row, and master_flow/root notes row all confirmed resolved. Saboteur's residual MAJOR: wave 1 plants "pending user go" in PROJECT.md but wave 2's PROJECT row and sweep never cleared it — Genuine, fixed (explicit PROJECT rewrite wording + cross-surface pending-user-go zero-match grep).

| Finding | Lens | Severity | Verdict | Action |
|---------|------|----------|---------|--------|
| Wave 2 leaves PROJECT "pending user go" lines; sweep misses them | saboteur | MAJ | Genuine | Fixed (Round 2) |
| 7b placement after step 9; missing success rejoin | saboteur, new_hire, auditor | ADV | Genuine | Fixed (Round 2): 7b folded into step 7 with explicit proceed-to-8 |
| Wave 2 STATE body exact replacement sentences | new_hire | ADV | Advisory-skipped | Skipped (Round 2): shipped-wording principle stated; verbatim lines are plan-level |

Fixes applied: 3
Inflation rate: 0% (this round's CRITICAL+MAJOR findings triaged FP, Recurring FP, or Design, divided by this round's CRITICAL+MAJOR findings).
Validation: SKIP

## Round 3 Summary

Confirmation wave: prompted locs step 7 self-run, Wave2 PROJECT row, Wave2 sweep returned `resolved by this change` from all three lenses (auditor retried once with exact labels after a loc-label mismatch); no `still stands`, no new findings. Two JSON-side advisories (verify verdict string is a historical record; handoff-stop stopped_at framing) left to the plan to word correctly.

Fixes applied: 0
Inflation rate: n/a (0 CRITICAL+MAJOR findings this round)
Validation: SKIP

## Converged: Round 3

Track 1: Merged verdict NO_CRITICAL_OR_MAJOR.
Total rounds: 3 (at the round cap)  |  Total fixes: 8
Document is ready.
