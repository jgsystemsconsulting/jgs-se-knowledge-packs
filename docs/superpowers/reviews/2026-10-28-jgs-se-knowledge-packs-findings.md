---
date: 2026-10-28
project: jgs-se-knowledge-packs
mode: light
rounds: 1
slice: []
input_digest: 984622b3f11d396b4062d072f396703b8e84b2ba8f2dae42605482c19908e266
open_objections: []
---

# Repo review findings - jgs-se-knowledge-packs (2026-10-28, light re-run #2)

Re-run after 1.24.0 (P57-P60 + site/SEO sync shipped, PR #8 merged, tag + GitHub Release live). Prior findings 2026-10-26 (I1-I12) all shipped; their advisories a-01..a-20 remain umbrella'd on backlog b-48. Ids continue at I13.

## I14 - licensing-omg-tier-contradiction

- **name**: licensing-omg-tier-contradiction
- **perspective**: Author-facing LICENSING.md still presents OMG SysML under the OMG Specification Licence as a lawful Tier-2 source ("Our packs comply with all three"), while SOURCE-VETTING.md hard-excludes all OMG formal specs as informational-use-only (no network posting, no modification; two independent licence reads 2026-06-19) and forbids packaging. Inverted eligibility guidance for anyone who opens LICENSING first.
- **evidence**: docs/LICENSING.md:L42-56 ("### Tier 2: Open licence (e.g. SEBoK, OMG SysML, MIT OpenCourseWare)" ... "Our packs comply with all three."); docs/SOURCE-VETTING.md:L49-51 ("**Not Tier 2: OMG specifications.** ... Do not classify OMG specs as Tier 2."); docs/SOURCE-VETTING.md:L79 (Excluded row).
- **blast_radius**: Pack PRs or forks built from OMG specs under a false Tier-2 reading; takedown and licence-violation risk; the omg-signpost-only design is undermined by the compliance doc.
- **severity**: HIGH
- **corroboration**: 1
- **lenses**: operate
- **deps**: []

## I13 - cursor-eligible-set-substring-commercial-use

- **name**: cursor-eligible-set-substring-commercial-use
- **perspective**: Check 6b and the CI twin `Cursor skills eligible set` decide commercial eligibility with a raw `"commercial_use: false"` substring match on PACK.yaml text, not a parsed scalar. Quoted, spaced, or cased variants miss; a missing commercial_use on a shipped pack fails to exclude; validate_pack only checks the field is non-empty (and quote-strips values), so a non-boolean value passes every other gate while the cursor gate treats it as commercial. The cursor skills array is the commercial-redistribution allowlist (MA-01).
- **evidence**: .github/workflows/validate.yml:L1383-1391; tooling/check_release.py:L1383-1390; tooling/validate_pack.py:L29-50 and L107-111; docs/PACK-SPEC.md:L63 (canonical form pinned).
- **blast_radius**: Latent, not live: all 83 packs/*/PACK.yaml carry the canonical unquoted form today (triage grep), so nothing misclassifies right now; a future non-commercial pack with a quoted or spaced `false` would land in the cursor eligible set silently, and a commercial pack whose prose embeds the substring would be wrongly excluded.
- **severity**: MEDIUM (downgraded from HIGH; triage reason: canonical unquoted form verified on all 83 PACK.yaml files - no live miss today; drift-risk defect)
- **corroboration**: 2
- **lenses**: defect, guard (guard read = contradicting kill, settled by the triage grep)
- **deps**: []

## I15 - stale-catalogue-counts-operator-docs

- **name**: stale-catalogue-counts-operator-docs
- **perspective**: Operator docs still state pre-1.24.0 catalogue sizes as current fact: SOURCE-FRESHNESS "the catalogue's 71 live packs", PACK-SPEC kind table "the 71 catalogue packs", DISTRIBUTION "all 81 claude-plugin skill paths" and "All 71 catalog packs live 2026-10-26". Shipped truth: 74 content packs, 83 skills.
- **evidence**: docs/SOURCE-FRESHNESS.md:L8; docs/PACK-SPEC.md:L109; docs/DISTRIBUTION.md:L11 and L27; shipped truth at CHANGELOG.md 1.24.0 section and SKILLS.md:L9.
- **blast_radius**: The next pack add, distribution revisit, or watchlist parity check uses the wrong inventory.
- **severity**: MEDIUM
- **corroboration**: 2
- **lenses**: rot, operator
- **deps**: []

## I16 - cursor-skills-gate-test-gap

- **name**: cursor-skills-gate-test-gap
- **perspective**: test_ci_gate pins the `Cursor skills eligible set` step and runs one mismatch demo (eligible alpha, excluded beta, manifest lists only beta), but has no negative demos for quoted or spaced commercial_use, a pack missing the field entirely, or a demo_ok for a correct eligible set. The failure modes of I13 have no automated tripwire.
- **evidence**: tooling/test_ci_gate.py:L588-596 (single demo); L61-73 (PINNED_STEPS); L1043-1048 (positive real-tree loop).
- **blast_radius**: Regressions in the eligibility step stay green in the ci-gate probe.
- **severity**: MEDIUM
- **corroboration**: 1
- **lenses**: defect
- **deps**: [I13]

## I17 - pack-spec-missing-post-p57-build-lessons

- **name**: pack-spec-missing-post-p57-build-lessons
- **perspective**: PACK-SPEC's build section and CONTRIBUTING's authoring steps still teach only the old one-line "extract + offset-map + generate" stub. The rules that just mattered - the two-PDF convention (nasa-risk), contents-list-wins over provisional chapter maps (faa-ams-vv), and a verify-what-you-wrote transport-integrity check - live only inside gitignored superpowers specs. A new pack author facing the 11-gate CI wall has no author-facing statement of them.
- **evidence**: docs/PACK-SPEC.md:L66-69 (build method stub shape); CONTRIBUTING.md:L41-43.
- **blast_radius**: The next rebuild or external contributor repeats a wrong chapter freeze, a wrong volume pin, or ships unverified extract prose while registration gates stay green.
- **severity**: MEDIUM
- **corroboration**: 1
- **lenses**: operator
- **deps**: [I15]

## Advisories (below the findings bar; packaging is package-loop's call)

| id | title | evidence |
|----|-------|----------|
| a-21 | SOURCE-VETTING L266 names validate_pack.py as the CI enforcer; CI actually runs an inline pure-data twin - enforcement substance exists, tool name imprecise, one-line doc fix (I18 triaged down to this) | docs/SOURCE-VETTING.md:L266; .github/workflows/validate.yml:L1071-1074 |
| a-22 | CONTRIBUTING pack-author TODO scaffold (carried; backlog b-46) | CONTRIBUTING.md:L44 |
| a-23 | Seven 2026-09-14 plans without EXECUTED twins (carried; backlog b-47) | docs/superpowers/plans/2026-09-14-*.md |
| a-24 | build_pack.py TODO stubs scaffold-only (carried; backlog b-48/b-10) | tooling/build_pack.py:L58-75 |
| a-25 | check_release leak/link single-read refactor deferred (carried; backlog b-44) | tooling/check_release.py:L966-996 |
| a-26 | gen_packs_page/gen_pack_pages pairing residual (carried; backlog b-40) | tooling/gen_pack_pages.py:L27 |
| a-27 | sitemap lastmod follows catalog `updated`, not run date (carried; backlog create-release-1) | tooling/gen_pack_pages.py:L279-299 |
| a-28 | install.py --target rmtree is user-run local, not CI; ownership marker skips foreign trees | install.py:L91, L175-196 |
| a-29 | jsp-912 LICENSE prose carries transport-strip awkwardness; OGL grant and full deed intact, terms not misstated | packs/jsp-912/LICENSE:L1-80 |
| a-30 | 12 tooling scripts lack dedicated unit files; live gates covered end-to-end by the 11 pinned CI steps plus 12 test modules | tooling/test_ci_gate.py:L61-73 |
| a-31 | .planning/codebase/CONCERNS.md is 2026-08 historical; items fixed or parked | .planning/codebase/CONCERNS.md:L3 |

## Kills (considered, below bar; routing input for package-loop)

CONTRIBUTING TODO (b-46); stale plans (b-47); build_pack stubs (b-48/b-10); untested scripts (pinned); sitemap lastmod (create-release-1); install.py dry-run UX fine; check_release error lines actionable; pre-tag section current post-P60; README current; SOURCE-VETTING tier tables live (aside from I14); guard kills: cursor substring per PACK-SPEC pin (settled into I13 by triage grep), install.py rmtree user-run, jsp-912 LICENSE prose, check_release git-only subprocess.
