# ARL triage log: 2026-09-14-ci-link-policy-parity (plan)

| Finding | First seen | Last seen | Verdict | Rationale |
|---------|------------|-----------|---------|-----------|
| C1: test (d) asserts inverted parity lists | R1 | R1 | FP | Inflation-FP: parity_diff(file, workflow) returns (file-workflow, workflow-file); drifted removes dau.edu and adds acme.example, so only_in_file=[acme.example], only_in_workflow=[dau.edu], matching the asserts at L393-394 |
| M1: L27 exact fail-closed message contradicts loader suffix | R1 | R1 | Genuine | Loader (L224) emits `host list empty (tooling/link-policy-hosts.txt has no tokens)`; L27's "exactly `[links-parity] host list empty`" omits the parenthesized suffix |
| A1: sed -i without backup extension on Win32 Git Bash | R1 | R1 | Advisory-skipped | Git Bash sed -i works here and every probe restores via git checkout or mv; swap adds no correctness |
| A2: CI parse_host_file does not de-duplicate | R1 | R1 | Advisory-skipped | Duplicate token line is harmless: parity uses sets both sides and the regex join is unaffected; one-line format note optional |
| A3: Step 3 extraction anchored on next step name and 10-space indent | R1 | R1 | Advisory-skipped | Fragile only if a later task renames "Pack frontmatter lint"; one-line dependency note would do, not blocking |
| A4: PR-description cross-reference one-directional | R1 | R1 | Advisory-skipped | Cosmetic pointer between Task 4 Step 4 and Task 6 Step 3; both name the same evidence set already |

Parent triage override on C1: the triage agent's FP rationale swapped the argument roles (it treated `drifted` as the file set). The plan's call is `parity_diff(EXPECTED, drifted)`, so only_in_file = EXPECTED − drifted = `["dau.edu"]` while the assert expects `["acme.example"]`; the kept test would raise on every run. C1 reclassified FP → Genuine and fixed by the parent.

## Round 1 Summary

| Finding | Lens | Severity | Verdict | Action |
|---------|------|----------|---------|--------|
| Test (d) asserts inverted parity lists (test can never exit 0) | saboteur, new_hire | CRIT | Genuine (parent override of FP) | Fixed (Round 1) |
| L27 exact fail-closed message contradicts loader suffix | saboteur, new_hire, auditor | MAJ | Genuine | Fixed (Round 1) |
| sed -i without backup extension on Win32 | new_hire | ADV | Advisory-skipped | Skipped (Round 1) |
| CI parse_host_file does not de-duplicate | auditor | ADV | Advisory-skipped | Skipped (Round 1) |
| Task 4 Step 3 extraction anchor fragile | saboteur | ADV | Advisory-skipped | Skipped (Round 1) |
| PR-description cross-reference one-directional | auditor | ADV | Advisory-skipped | Skipped (Round 1) |

Fixes applied: 2
Inflation rate: 0% (this round's CRITICAL+MAJOR findings triaged FP, Recurring FP, or Design, divided by this round's CRITICAL+MAJOR findings; parent override counts C1 Genuine).
Validation: SKIP

Dropped out of scope: 0. Scope unchecked (non-line loc): 0.

## Round 2 Summary

Confirmation wave: prompted locs L27 and L393-394 returned `resolved by this change` from all three lenses; no `still stands`, no CRITICAL/MAJOR. Coverage complete.

| Finding | Lens | Severity | Verdict | Action |
|---------|------|----------|---------|--------|
| Malformed-line gist colon placement vs loader "(line N)" | saboteur | ADV | Advisory-skipped | Skipped (Round 2): gist ellipsis already covers appended detail |

Fixes applied: 0
Inflation rate: n/a (0 CRITICAL+MAJOR findings this round)
Validation: SKIP

## Converged: Round 2

Track 1: Merged verdict NO_CRITICAL_OR_MAJOR.
Total rounds: 2  |  Total fixes: 2
Document is ready.
