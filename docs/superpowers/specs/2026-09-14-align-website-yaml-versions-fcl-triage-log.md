# FCL triage log: 2026-09-14-align-website-yaml-versions (spec)

Target: docs/superpowers/specs/2026-09-14-align-website-yaml-versions.md
Corpus: local-only (repo facts; web stripped)

| Finding | First seen | Last seen | Verdict | Rationale |
|---------|------------|-----------|---------|-----------|
| M1: L13 "stayed green" claim unsupported | R1 | R1 | FP | Lens inverted the claim. L12-13 states no gate covers the two YAMLs, and check_release.py reads plugin.json, CHANGELOG, RELEASE-INFO, packs, docs, never docs/products/website. Spec is supported. |
| M2: L39 cites non-existent fail(errs, f"[version] ...") idiom | R1 | R1 | FP | Idiom exists verbatim. check_release.py:61 defines fail(errs, msg); L113 and L122 call fail(errs, f"[version] ...") inside check 4 (L108-122). Lens misread the file. |
| M3: L50 cites non-existent fail idiom for optional gate | R1 | R1 | FP | Same as M2. The existing fail(errs, f"[version] ...") call sites at check_release.py:113 and :122 are the real pattern the spec references. |
| A1: L41 calls CHANGELOG.md:44 a link-ref; it is a section heading | R1 | R1 | Advisory-skipped | CHANGELOG.md:44 is `## [1.19.1]: 2026-08-20`, a Keep-a-Changelog heading, not a link-ref. One-word relabel is cheap and clearly correct, so fix it opportunistically. |

## Round 1 Summary

| Finding | Lens | Severity | Verdict | Action |
|---------|------|----------|---------|--------|
| L13 "stayed green" claim unsupported | source | MAJ | FP | Skipped (Round 1) |
| L39 cites fail(errs, f"[version] ...") idiom | source | MAJ | FP | Skipped (Round 1) |
| L50 cites fail idiom for optional gate | source | MAJ | FP | Skipped (Round 1) |
| L41 link-ref label | skeptic | ADV | Advisory-skipped | Fixed (Round 1) |

Fixes applied: 1
Inflation rate: 100% (3 of 3 CRITICAL+MAJOR findings triaged FP)
Validation: SKIP (no associated script; spec is prose)

## Round 2 Summary

| Finding | Lens | Severity | Verdict | Action |
|---------|------|----------|---------|--------|
| (confirmation wave; 0 findings) | skeptic, source, correspondent | n/a | n/a | L41 fix confirmed. Skeptic and correspondent: "resolved by this change". Source returned "still stands" but its evidence verifies the fixed state (CHANGELOG.md:44 contains `## [1.19.1]:` verbatim) and source raised no finding; the relabel defect can no longer fire, so no unfixed genuine finding exists. |

Fixes applied: 0
Inflation rate: n/a (0 CRITICAL+MAJOR findings this round)
Validation: SKIP (no associated script; spec is prose)

## Converged: Round 2

Track 1: Merged verdict NO_CRITICAL_OR_MAJOR.
Total rounds: 2  |  Total fixes: 1
Document is ready.
