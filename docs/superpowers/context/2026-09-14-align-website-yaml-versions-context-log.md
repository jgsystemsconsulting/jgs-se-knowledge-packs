# Context log: align-website-yaml-versions

| Finding | First seen | Last seen | Verdict | Rationale |
|---------|-----------|-----------|---------|-----------|
| 01-jgs-se-knowledge-packs.yaml:15 top-level `version: "1.19.1"` | R1 | R1 | SINGLE-SOURCE | Re-read matches; three lens sites all cite the same single loc, no code site |
| catalog.yaml:13 nested `version: "1.19.1"` under products[0], contradicts RELEASE-INFO 1.20.0 | R1 | R1 | SINGLE-SOURCE | Re-read matches; same single loc across lenses, no code site; contradiction confirmed by RELEASE-INFO.txt:3 |
| Naive YAML scrape must handle asymmetric shapes (top-level vs nested indent), both quoted | R1 | R1 | SINGLE-SOURCE | One site; asymmetry confirmed by triage re-read of both YAMLs, first-party files |
| check_release check 4 parses plugin.json via json.loads+.get (L111), CHANGELOG re (L115), RELEASE-INFO re (L118); no YAML paths, CR-01 holds | R1 | R1 | CORROBORATED | Lines 108-122 re-read; quotes match; multiple code sites in the gate itself |
| check_release stdlib-only, no yaml import, ROOT=Path(__file__).resolve().parent.parent (L36); YAML slot after check 4, no PyYAML | R1 | R1 | CORROBORATED | L36 and L24 docstring re-read and match; imports are json/re/sys/pathlib only |
| RELEASE-INFO.txt:3 Version 1.20.0; plugin.json:4 1.20.0; CHANGELOG.md:12 [1.20.0] trio | R1 | R1 | SINGLE-SOURCE | Cited sites all point at RELEASE-INFO.txt:3 only (verified); plugin.json:4 and CHANGELOG.md:12 also verified by triage but carry no listed evidence site |
| check_release docstring names single-source convention plugin.json == CHANGELOG top == RELEASE-INFO.txt | R1 | R1 | SINGLE-SOURCE | One doc site at L13, re-read matches; no second independent site |
| No tooling or CI reads the two website YAMLs; packs.html version from RELEASE-INFO (gen_packs_page.py:42-43); validate.yml cannot break on the bump | R1 | R1 | CORROBORATED | Code sites verified (check_release.py:254 map_path, gen_packs_page.py:42-43); triage grep of tooling/ and .github/ for the YAML names returns nothing; validate.yml:87 only validates catalog.json |
| Recent bumps touched plugin/CHANGELOG/README not website YAMLs; residual is the two YAMLs only | R1 | R1 | SINGLE-SOURCE | One doc site (the context brief itself); git history not re-checkable by triage, but current on-disk state (YAMLs at 1.19.1, trio at 1.20.0) is consistent |
| CONTRACT meaning-table example 1.19.1 is plan-allowed residual, keep | R1 | R1 | SINGLE-SOURCE | capability-map-CONTRACT.md:35 re-read, quote matches; illustrative semver example, not a live surface |
| capability-pack-map.md:18 v1.19.1 changelog line is historical, keep | R1 | R1 | SINGLE-SOURCE | Line 18 re-read, quote matches; historical changelog list also carries v1.20.0 at line 17 |
| CHANGELOG.md:44 [1.19.1] link-ref is prior-basis history, keep, whitelist in residual grep | R1 | R1 | SINGLE-SOURCE | Line 44 re-read, quote matches; Keep-a-Changelog history |
| packs/*/PACK.yaml source_version keys are a different class; census must scope to the two website YAMLs or false-fail | R1 | R1 | SINGLE-SOURCE | build_pack.py:48 re-read matches; per-pack source-document version field, distinct from product release version |
| No tooling/.github reference to v1.20.0 or 046799b; retag cannot break a commit pin | R1 | R1 | SINGLE-SOURCE | One code site; triage grep of tooling/ and .github/ for v1.20.0 and 046799b returns nothing, confirming the negative |
| Tag v1.20.0 annotated object 61fd653 -> commit 046799b, local-only | R1 | R1 | SINGLE-SOURCE | .git/refs/tags/v1.20.0 re-read, hash 61fd653c77e47766f7ed31f8627a95c6d372c52b matches; parent git probe, not re-checkable by triage, covered by parent_verified |
| graphify post-commit hook no-ops on this tree because .planning/ is gitignored (check-ignore guard L22); residual risk if carve-out removed | R1 | R1 | SINGLE-SOURCE | post-commit:22/44 and .gitignore:37 all re-read and match; all sites are config kind, no code site |
| CR-01 fix path: bump both YAMLs, check_release PASS, delete+recreate local tag; gate add optional hardening | R1 | R1 | SINGLE-SOURCE | 21-IMPL_REVIEW.md:67 re-read, quote matches; fix steps at lines 68-71 name the same sequence |

## Round 1

Round 1 graded 17 merged claims. CORROBORATED 3, SINGLE-SOURCE 14, CONFLICTED 0, STALE 0. Every cited loc was re-read and every quote matched. Coverage is 5/5 against the brief sub-questions: SC1 claims rest on the exact YAML lines themselves, SC2 on the gate source, SC3 corroborated by code plus negative grep, SC4 on the readable tag ref and the impl-review text, SC5 on direct first-party doc lines. No claim is CONFLICTED or STALE.

## Round 1 Summary

| Claim | Lenses | Grade | Action |
|-------|--------|-------|--------|
| 01-*.yaml:15 version 1.19.1, only live drift | cartographer, prospector, skeptic | SS | Resourced (Round 1) |
| catalog.yaml:13 version 1.19.1, contradicts trio | cartographer, prospector, skeptic | SS | Resourced (Round 1) |
| YAML scrape asymmetry (top-level vs nested) | skeptic | SS | Resourced (Round 1) |
| check 4 parse idioms L111/115/118, no YAML path | cartographer, prospector, skeptic | CORR | Resourced (Round 1) |
| stdlib-only, no yaml import, slot after check 4 | cartographer, skeptic | CORR | Resourced (Round 1) |
| trio already 1.20.0 (RELEASE-INFO/plugin/CHANGELOG) | cartographer, prospector, skeptic | SS | Resourced (Round 1) |
| docstring names single-source convention | prospector | SS | Resourced (Round 1) |
| nothing reads the two YAMLs; CI safe on bump | cartographer, skeptic | CORR | Resourced (Round 1) |
| residual is the two YAMLs only | prospector | SS | Resourced (Round 1) |
| CONTRACT example 1.19.1 keep | skeptic | SS | Resourced (Round 1) |
| map changelog v1.19.1 keep | skeptic | SS | Resourced (Round 1) |
| CHANGELOG link-ref 1.19.1 keep | skeptic | SS | Resourced (Round 1) |
| PACK.yaml source_version different class | skeptic | SS | Resourced (Round 1) |
| no commit-pin refs to v1.20.0/046799b | skeptic | SS | Resourced (Round 1) |
| tag annotated -> 046799b, local-only | skeptic + parent probe | SS | Resourced (Round 1) |
| graphify hook no-op via gitignore guard | skeptic | SS | Resourced (Round 1) |
| CR-01 fix path; gate add optional | skeptic | SS | Resourced (Round 1) |

Fixes applied: 0
Coverage: 5/5 criteria met
Validation: PASS

Track 1: Merged verdict CONTEXT_COMPLETE.
