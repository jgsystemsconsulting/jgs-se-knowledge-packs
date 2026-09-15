# ARL triage log: 2026-09-14-ci-local-gate-coverage-gap (plan)

| Finding | First seen | Last seen | Verdict | Rationale |
|---------|------------|-----------|---------|-----------|
| C1 wrong Task 2 red-state message (L609) | R1 | R1 | Genuine | Parity section runs before extraction and current validate.yml has no version/map regex literals, so the first failure is the parity drift assert, not the extraction assert the plan quotes. |
| M1 parity check is presence-only containment (L36) | R1 | R1 | Design | Presence-level parity detects literal drift between twins; extraction plus negative demos pin per-step behavior, so location-level byte identity is unnecessary. |
| M2 Task 6 Step 3 grep hits Task 3 header comment (L1360-1363) | R1 | R1 | Genuine | New header line "run `python tooling/check_release.py`" matches the grep pattern, so the "no line invokes tooling/*.py" expectation can never pass as written. |
| M3 HEAD~4 footprint assumption (L1359) | R1 | R1 | Advisory-skipped | Four plan commits on a solo linear repo is the stated shape; a wrong base shows up as a mismatched file list at the same step, and the name-only diff variant is an optional tidy-up. |
| A1 len(bodies) assert is dead (L510) | R1 | R1 | Advisory-skipped | Not fully dead: it fails if PINNED_STEPS ever contains a duplicate name, since dict keys collapse; keeping one line is cheaper than rekeying by index. |
| A2 demo B clobbers untracked whitelist (L232-235) | R1 | R1 | Advisory-skipped | Copy-aside restore as demo A does is cheap and clearly correct; manual re-typing invites transcription drift. |
| A3 Edit 4 line span off by start (L174) | R1 | R1 | Advisory-skipped | Content match is authoritative; widening the citation to L45-52 is a one-line clarification. |
| A4 Task 5 line numbers shift after row insert (L1153-1178) | R1 | R1 | Advisory-skipped | Match-the-block instruction is cheap; fixed line cites will mislead after the first insert. |
| A5 gh CLI prerequisite unstated (L1368-1369) | R1 | R1 | Advisory-skipped | One "gh required, or check the Actions tab" note; no structural gap. |
| A6 em dash in new probe copyright header (L282) | R1 | R1 | Design | New-file headers copy the repo-standard copyright line verbatim; the em dash ban targets authored prose, matching the existing-header carve-out's intent. |

## Round 1 Summary

| Finding | Lens | Severity | Verdict | Action |
|---------|------|----------|---------|--------|
| Task 2 red-state message wrong (parity fires before extraction) | saboteur, auditor | CRIT | Genuine | Fixed (Round 1) |
| Parity check presence-only, not per-heredoc | saboteur | MAJ | Design | Wontfix (Round 1): presence detects literal drift; per-step behavior pinned by extraction + negative demos |
| Task 6 grep hits header comment | saboteur | MAJ | Genuine | Fixed (Round 1): expectation restricted to executable lines |
| HEAD~4 footprint assumption | new_hire, auditor | MAJ | Advisory-skipped | Skipped (Round 1): solo linear repo; mismatch shows as wrong file list at the same step |
| len(bodies) assert tautological | saboteur | ADV | Advisory-skipped | Skipped (Round 1): catches duplicate names in PINNED_STEPS; cheaper than rekeying |
| Demo B clobbers untracked whitelist | saboteur | ADV | Advisory-skipped | Skipped (Round 1): single-token file, Step 2 content authoritative |
| Edit 4 line span off by start | new_hire | ADV | Advisory-skipped | Skipped (Round 1): content match authoritative |
| Task 5 line numbers shift after insert | new_hire | ADV | Advisory-skipped | Skipped (Round 1): match-the-block guidance stands |
| gh CLI prerequisite unstated | new_hire | ADV | Advisory-skipped | Skipped (Round 1): one-note item |
| Em dash in new probe copyright header | auditor | ADV | Design | Wontfix (Round 1): new-file headers copy the repo-standard line verbatim; ban targets authored prose |

Fixes applied: 2
Inflation rate: 50% (this round's CRITICAL+MAJOR findings triaged FP, Recurring FP, or Design, divided by this round's CRITICAL+MAJOR findings).
Validation: SKIP

## Round 2 Summary

Confirmation wave: prompted locs L609 and L1360-1363 returned `resolved by this change` from all three lenses; no `still stands`, no CRITICAL/MAJOR. Four residual advisories (extraction binding, workflow-wide parity backstop, em-dash header, HEAD~4 assumption) noted for the executor; the plan's Task 4 already names the twin files for parity and Task 6 states the linear-repo assumption implicitly.

Fixes applied: 0
Inflation rate: n/a (0 CRITICAL+MAJOR findings this round)
Validation: SKIP

## Converged: Round 2

Track 1: Merged verdict NO_CRITICAL_OR_MAJOR.
Total rounds: 2  |  Total fixes: 2
Document is ready.
