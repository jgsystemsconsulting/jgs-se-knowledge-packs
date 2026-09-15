# ARL triage log: 2026-09-14-ci-local-gate-coverage-gap

| Finding | First seen | Last seen | Verdict | Rationale |
|---------|------------|-----------|---------|-----------|
| C1 CI signpost set from rules.signpost_packs vs local chapters/ inference | R1 | R1 | Genuine | check_capability_map.py L176-181 derives on-disk packs from chapters/ dirs and never reads signpost_packs; spec Step 8 defines a different derivation, so a pack listed in signpost_packs with chapters/ on disk leaves CI red while local is green, breaking the "CI red always means real drift" claim |
| C2 malformed overlap-whitelist.txt undefined (charset, empty, duplicates) | R1 | R1 | FP | Inflation-FP: spec L97 says "mirroring how check_release.py handles link-policy-hosts.txt"; that reader (check_release.py L58, L65-76) defines token regex, zero-token fail, and dedup, and the ch01-introduction.md token fits the charset |
| C3 pre-tag control unevaluable, no enforcement actor | R1 | R1 | Design | Spec L109-115 disclaims mechanical enforcement explicitly, records the procedural sha-receipt rule as the sanctioned option, and assigns gsd-ship wiring to P8; it does not claim enforcement while leaving the invariant unevaluated |
| M1 CI reads PR-editable whitelist directly, no trusted inline copy | R1 | R1 | Design | Spec L99 documents the PR-editable residual as identical to today's constant posture; single shared file removes drift by construction, which is the risk P4's inline-copy pattern targeted |
| M2 on-disk coverage requires only an assignment row, not is_support:false | R1 | R1 | Advisory-skipped | Local checker (check_classification_rules.py L215-224) requires a non-support row; CI weaker here means local red with CI green, the strict-subset posture spec L79 sanctions; one-word fix to "is_support:false row" is cheap and correct |
| M3 no-git path passes while release rule requires sha match | R1 | R1 | Genuine | Spec L111 lets the banner print without a sha and pass; L112 requires a PASS line whose sha matches the tagged commit, so the no-git receipt can never satisfy the rule yet the gate emits PASS; exact banner strings also unpinned |
| A1 local twin silently skips when validate_pack import fails, framing says full check | R1 | R1 | Advisory-skipped | One comment line in the coverage map; direction is CI stricter than local, no false green |
| A2 envelope regex literals (map_version, generated_on) not pinned in CI | R1 | R1 | Advisory-skipped | Local MAP_VERSION_RE and GENERATED_ON_RE exist (check_classification_rules.py L26-27); adding both literals to the probe parity asserts is cheap |
| A3 CI never pins signpost_packs exact-value fidelity | R1 | R1 | Advisory-skipped | Local pins the exact list (check_classification_rules.py L294-300); folded into the C1 parity fix |
| A4 workflow step name strings used as extraction markers unspecified | R1 | R1 | Advisory-skipped | Pin four name strings when writing the probe; pure spec completeness |
| A5 probe heredoc extraction falls back silently to mirror functions | R1 | R1 | Advisory-skipped | Fail loudly on zero extracted heredocs preserves the test-the-real-text property; one assert |

## Round 1 Summary

| Finding | Lens | Severity | Verdict | Action |
|---------|------|----------|---------|--------|
| CI signpost set (rules.signpost_packs) diverges from local twin (chapters/ inference) | saboteur, new_hire | CRIT | Genuine | Fixed (Round 1): disk side derived as the local twin derives it |
| Whitelist format undefined | saboteur, new_hire | CRIT | FP | Skipped (Round 1): spec L97 already mirrors the link-policy-hosts.txt reader, which defines charset/zero-token/dedup |
| Pre-tag control has no enforcement actor | saboteur, auditor | CRIT | Design | Wontfix (Round 1): spec L109-115 explicitly disclaims mechanical enforcement, defers wiring to P8 |
| Step 7 reads PR-editable whitelist without trusted copy | saboteur | MAJ | Design | Wontfix (Round 1): allowlist not banlist; residual documented at L99; shared file removes accidental drift |
| Rules coverage needs is_support:false row | new_hire | MAJ | Advisory-skipped | Fixed (Round 1): one-word cheap fix taken |
| No-git banner contradicts sha-match rule; strings unpinned | saboteur, new_hire | MAJ | Genuine | Fixed (Round 1): distinct no-git banner that can never satisfy the pre-tag rule |
| Step 6 local skip condition | saboteur | ADV | Advisory-skipped | Skipped (Round 1): CI-stricter direction is safe |
| Envelope regex literals unpinned | new_hire | ADV | Advisory-skipped | Fixed (Round 1): mirror MAP_VERSION_RE / GENERATED_ON_RE |
| signpost_packs fidelity CI never pins | auditor | ADV | Advisory-skipped | Skipped (Round 1): folded into C1 fix (fidelity stays local-only, stated) |
| Step name strings unpinned for probe extraction | new_hire | ADV | Advisory-skipped | Fixed (Round 1): plan pins them; probe fails loudly on zero extractions |
| Probe extraction fallback silent | saboteur | ADV | Advisory-skipped | Fixed (Round 1): fails loudly if zero heredocs extracted |

Fixes applied: 6
Inflation rate: 33% (this round's CRITICAL+MAJOR findings triaged FP, Recurring FP, or Design, divided by this round's CRITICAL+MAJOR findings).
Validation: SKIP

## Round 2 Summary

Confirmation wave: L74/L76/L77/L111 confirmed resolved; L127 partially (step names still deferred to plan). New CRITICAL: L134 parity-assert list omits MAP_VERSION_RE / GENERATED_ON_RE mandated by L74 (three lenses, promoted).

| Finding | Lens | Severity | Verdict | Action |
|---------|------|----------|---------|--------|
| L134 parity list omits map/rules envelope regexes | saboteur, new_hire, auditor | CRIT | Genuine | Fixed (Round 2) |
| L127 step name strings not pinned in-spec | new_hire | MAJ | Genuine | Fixed (Round 2): four step names pinned in the spec |
| L76 chapters glob *.md vs local all-files scan | saboteur, new_hire | ADV | Genuine | Fixed (Round 2): all files, matching local is_file scan |
| L77 signpost_packs read-as-set clarification | new_hire | ADV | Genuine | Fixed (Round 2) |
| map_version non-empty vs N.N.N fullmatch | new_hire | ADV | Advisory-skipped | Skipped (Round 2): L74 regex-mirror wording covers the pin |

Fixes applied: 4
Inflation rate: 0% (this round's CRITICAL+MAJOR findings triaged FP, Recurring FP, or Design, divided by this round's CRITICAL+MAJOR findings).
Validation: SKIP

## Round 3 Summary

Confirmation wave: prompted locs L127, L134, L76, L77 returned `resolved by this change` from all three lenses; no `still stands`, no CRITICAL/MAJOR. Three residual advisories (rules disk-side *.md pin, split drift messages per twin pair, mirror-fallback brittleness criterion) left to the plan author to incorporate.

Fixes applied: 0
Inflation rate: n/a (0 CRITICAL+MAJOR findings this round)
Validation: SKIP

## Converged: Round 3

Track 1: Merged verdict NO_CRITICAL_OR_MAJOR.
Total rounds: 3 (at the round cap)  |  Total fixes: 7
Document is ready.
