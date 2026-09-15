# FCL triage log: 2026-09-14-validate-pack-signpost-parity

| Finding | First seen | Last seen | Verdict | Rationale |
|---------|------------|-----------|---------|-----------|
| C1: L60 table keeps chapters/>=1 ch*.md as signpost requirement, contradicts D1 L51, sketch L103-109, and D3 case 4 | R1 | R1 | Genuine | Table cell contradicts the design it summarizes; fix to no |
| M1: L38 PACK.yaml REQUIRED_PACK_FIELDS claim called unverified | R1 | R1 | FP | Parent-verified ground truth: both signpost PACK.yaml carry all six fields with tier 2 and matching slugs |
| M2: L39 65-dir claim challenged by lens Glob count of 66 SKILL.md | R1 | R1 | FP | Parent-verified ground truth: 65 dirs and 65 SKILL.md; lens Glob miscounted |
| M3: L112 says frontmatter reuses body then claims L76 onward untouched | R1 | R1 | Genuine | Internal contradiction; L78 read must change to reuse body, delete untouched claim |
| A1: Goal 4 share one predicate overstates duplicated-regex design | R1 | R1 | Advisory-skipped | Wording nit; D1 L49 already states the identical-regex contract precisely |
| A2: L129 cites three negative cases, D3 lists four | R1 | R1 | Advisory-skipped | Count drift in open questions; D3 case list is authoritative, one-word fix if touched |

## Round 1 Summary

| Finding | Lens | Severity | Verdict | Action |
|---------|------|----------|---------|--------|
| D1 table marks chapters required for signposts | skeptic, correspondent | CRIT | Genuine | Fixed (Round 1) |
| REQUIRED_PACK_FIELDS claim called unverified | source | MAJ | FP | Skipped (Round 1): parent verified claim true (both PACK.yaml carry all six fields) |
| 65-dir claim challenged by lens count of 66 | source | MAJ | FP | Skipped (Round 1): parent verified 65/65; lens Glob miscounted |
| L112 "L76 onward untouched" contradicts body reuse | skeptic | MAJ | Genuine | Fixed (Round 1) |
| Goal 4 "share one predicate" wording | skeptic | ADV | Genuine | Fixed (Round 1) |
| "three negative cases" vs D3's four | skeptic | ADV | Genuine | Fixed (Round 1) |

Fixes applied: 4
Inflation rate: 50% (this round's CRITICAL+MAJOR findings triaged FP, Recurring FP, or Design, divided by this round's CRITICAL+MAJOR findings).
Validation: SKIP

## Round 2 Summary

Confirmation wave: prompted locs L16, L60, L112, L129 confirmed resolved by all three lenses. Adjudication note: the source and correspondent agents inverted the confirmation enum (verdict string "still stands" with evidence text explicitly confirming the fixed state, e.g. "D1 table L60 shows chapters/ 'no' ... matches live packs"); the parent adjudicated the wave on evidence content, corroborated by the skeptic's correctly-strung returns. No `still stands` defect remains; no new findings.

Fixes applied: 0
Inflation rate: n/a (0 CRITICAL+MAJOR findings this round)
Validation: SKIP

## Converged: Round 2

Track 1: Merged verdict NO_CRITICAL_OR_MAJOR.
Total rounds: 2  |  Total fixes: 4
Document is ready.
