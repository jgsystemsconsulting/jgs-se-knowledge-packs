# ARL triage log: 2026-09-14-map-tooling-residual-harden

| Finding | First seen | Last seen | Verdict | Rationale |
|---------|------------|-----------|---------|-----------|
| M1: probe (c) degrades on out-of-ROOT MAP_PATH and unpatched RULES_PATH/OVERRIDES_PATH | R1 | R1 | FP | Inflation-FP: probe paths hit only the is_file/read_text/render branch, never relative_to (that fires only in _load_json error text for a missing map, unprobed); reading real rules in check mode is correct since the temp JSON is written to match |
| A1: read_text universal newlines lets CRLF md pass freshness gate | R1 | R1 | Advisory-skipped | Real edge but repo md is LF-written with newline="\n"; a one-line LF-only note is optional polish |
| A2: --check prints JSON PASS before md FAIL in one run | R1 | R1 | Advisory-skipped | Exit code is correct; only a scraping consumer reading lines instead of the code misreads it |
| A3: quoted missing-heading message differs from _split_md_header text | R1 | R1 | FP | Message matches _split_md_header L283 verbatim; spec L168 already states the FAIL: md check: prefix comes from the caller |

## Round 1 Summary

| Finding | Lens | Severity | Verdict | Action |
|---------|------|----------|---------|--------|
| Probe (c) degrades on out-of-ROOT MAP_PATH; unpatched RULES/OVERRIDES | saboteur, auditor | MAJ | FP | Skipped (Round 1): probe paths hit only the is_file/read_text/render branch; relative_to fires only in _load_json's missing-map error text, unprobed; temp JSON written to match |
| CRLF md passes freshness compare | saboteur | ADV | Advisory-skipped | Skipped (Round 1): repo md is LF-written with newline="\n"; optional polish |
| --check mixes JSON PASS then md FAIL lines | saboteur | ADV | Advisory-skipped | Skipped (Round 1): exit code is correct; line-scraping consumer concern only |
| Quoted missing-heading message mismatch | auditor | ADV | FP | Skipped (Round 1): message matches _split_md_header L283 verbatim; caller adds the prefix |

Fixes applied: 0
Inflation rate: 100% (this round's CRITICAL+MAJOR findings triaged FP, Recurring FP, or Design, divided by this round's CRITICAL+MAJOR findings).
Validation: SKIP

## Converged: Round 1

Track 3: diminishing-return halt. Predicate: no-unfixed-genuine. Round 1's genuine_fixes_needed was empty; the sole merged MAJOR triaged FP on code verification.
Total rounds: 1  |  Total fixes: 0
Document is ready.
