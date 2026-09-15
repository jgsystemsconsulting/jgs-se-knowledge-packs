# Context: align-website-yaml-versions (2026-09-14)

## Context brief

**Primary question**: What exact repo facts must the align-website-yaml-versions spec get right so the run can bump the two public website product YAMLs to 1.20.0, re-run `python tooling/check_release.py` green, and recreate the local annotated tag v1.20.0 on the fix commit without creating new drift on derived surfaces?

**Sub-questions**:
1. Where exactly do `docs/products/website/01-jgs-se-knowledge-packs.yaml` and `docs/products/website/catalog.yaml` declare `version`, with what syntax and surrounding structure (enough for an exact one-line edit each)?
2. How is `tooling/check_release.py` organized (check list, parse style, exit codes), and where would an optional one-line YAML-version-vs-RELEASE-INFO consistency check slot in? What dependency posture applies (stdlib-only? PyYAML ban? CI never executes repo Python?)
3. What consumes the two website YAMLs — is there a derived artifact (catalog.json, packs.html, map envelope) that embeds the version and would drift after a bump?
4. What does Phase 21 impl review CR-01 demand verbatim, and what gate does master_flow_state.json record?
5. Does any other file in the repo still say 1.19.1 in a release surface this run must not miss (or must deliberately leave alone, e.g. historical CHANGELOG entries)?

**Success criteria**:
- SC1 (decision-bearing): exact location, current value, and surrounding structure of the `version` field in both website YAMLs; CORROBORATED.
- SC2 (decision-bearing): check_release.py version single-source check behavior + where a YAML consistency check slots + dependency posture; CORROBORATED.
- SC3 (decision-bearing): local tag v1.20.0 state (annotated, target commit, not pushed); CORROBORATED.
- SC4: CR-01 verbatim requirements and master_flow gate state; CORROBORATED or SINGLE-SOURCE with status named.
- SC5 (decision-bearing): consumers/derived surfaces of the two YAMLs identified, and a repo-wide 1.19.1 residual census; CORROBORATED or framed as open question.

**Out of scope**: `.planning/` ledger ticks (package P8); WR-01/WR-02/WR-03 generator residuals (P7); pack content; git push / gh release create; new packs.

**Budget**: full tier, round cap 3, expect 1 round; lens target ~12 tool calls each.

**Workspace baseline**: porcelain sha256 `a943b791de3bfb9072ae32ec8cd64db72f8361288c47815b59ac7090816d25fd` (HEAD 8a503cb7f94c8f8df9d7a49050fa731a56e97487, informational).

**Parent-verified facts entering the round** (from `git for-each-ref` / `git branch -r --contains`, 2026-09-14): tag `v1.20.0` is annotated (tag object 61fd653) pointing at commit 046799b, message `chore: annotate v1.20.0 generator refresh path`; no remote branch contains it.

## Findings

Grades from ctx-triage Round 1 (log: `2026-09-14-align-website-yaml-versions-context-log.md`). CORROBORATED 3, SINGLE-SOURCE 14, CONFLICTED 0, STALE 0.

| # | Claim (short) | Sites | Grade |
|---|---------------|-------|-------|
| 1 | `01-jgs-se-knowledge-packs.yaml:15` is `version: "1.19.1"`, top-level; only live 1.19.1 release-surface drift; bump required | 3 lenses, one loc | SINGLE-SOURCE |
| 2 | `catalog.yaml:13` is `version: "1.19.1"` under products[0]; contradicts RELEASE-INFO 1.20.0 | 3 lenses, one loc | SINGLE-SOURCE |
| 3 | YAML version scrape must handle asymmetric shapes: top-level vs nested indent; both quoted | skeptic; confirmed by triage re-read | SINGLE-SOURCE |
| 4 | check_release check 4 parses plugin.json (json.loads+get, L111), CHANGELOG (`^##\s*\[(\d+\.\d+\.\d+)\]`, L115), RELEASE-INFO (`Version:\s*([0-9]+\.[0-9]+\.[0-9]+)`, L118); no YAML paths; CR-01 holds | 3 lenses, code | CORROBORATED |
| 5 | check_release is stdlib-only (json/re/sys/pathlib), never imports yaml; ROOT at L36; natural slot for YAML check after check 4; regex idiom, no PyYAML | 2 lenses, code | CORROBORATED |
| 6 | Version trio already 1.20.0: RELEASE-INFO.txt:3, plugin.json:4, CHANGELOG.md:12 | 3 lenses | SINGLE-SOURCE (plugin/CHANGELOG sites re-verified by triage, unlisted) |
| 7 | check_release docstring names the single-source convention (L13) | prospector, doc | SINGLE-SOURCE |
| 8 | No tooling or CI reads the two website YAMLs; no derived artifact embeds their version; packs.html version comes from RELEASE-INFO (gen_packs_page.py:42-43); validate.yml only checks catalog.json → bump cannot break CI | 2 lenses, code; negative grep by triage | CORROBORATED |
| 9 | Recent bumps touched plugin/CHANGELOG/README, not the website YAMLs; residual is the two YAMLs only | context brief (doc); on-disk state consistent | SINGLE-SOURCE |
| 10 | CONTRACT meaning-table example `"1.19.1"` (L35) is illustrative, keep | skeptic, doc re-read | SINGLE-SOURCE |
| 11 | capability-pack-map.md:18 v1.19.1 changelog line is historical, keep (v1.20.0 already at L17) | skeptic, doc re-read | SINGLE-SOURCE |
| 12 | CHANGELOG.md:44 `[1.19.1]` link-ref is history, keep; whitelist in residual grep | skeptic, doc re-read | SINGLE-SOURCE |
| 13 | packs/*/PACK.yaml `source_version` is a different version class; census must scope to the two website YAMLs or false-fail | skeptic, code | SINGLE-SOURCE |
| 14 | No tooling/.github reference to v1.20.0 or 046799b; retag cannot break a commit pin | skeptic code site + triage negative grep | SINGLE-SOURCE |
| 15 | Tag v1.20.0 annotated, object 61fd653, peels to commit 046799b, local-only (no remote branch contains it) | `.git/refs/tags/v1.20.0` + parent git probe | SINGLE-SOURCE (parent probe not re-checkable by triage) |
| 16 | graphify post-commit hook auto-commits only when graphs are tracked; `.planning/` gitignore makes it no-op here; risk only if carve-out removed (hook guard at post-commit:22) | 3 config sites re-read | SINGLE-SOURCE |
| 17 | CR-01 fix path: bump both YAMLs, check_release PASS, delete+recreate local tag; gate add is optional hardening; fix steps named at IMPL_REVIEW lines 68-71 | skeptic, doc re-read | SINGLE-SOURCE |

## Synthesis

Five of five brief criteria covered in one round. The three CORROBORATED claims (4, 5, 8) rest on multiple independent code sites in the gate, the generator, and CI. Decision-bearing SINGLE-SOURCE claims are named here per Track 1: SC1 (claims 1-3) rests on the exact first-party YAML lines themselves, which triage re-read and quote-matched; SC5's census claims (10-13) rest on direct first-party doc/code lines re-read by triage; SC3 (claim 15) rests on the readable `.git/refs/tags/v1.20.0` ref plus parent git probes (`for-each-ref`, `branch -r --contains`) that triage cannot re-run. No claim is CONFLICTED or STALE; the three skeptic read_errors are tool-limit artifacts on git/network probes, compensated by the parent probes. One self-referential site (prospector citing this context doc) is flagged and carries no decision weight.

Operational cautions for the spec/plan: (a) the fix commit should be tagged explicitly by hash after confirming `HEAD` equals it, because the graphify post-commit hook can in principle append a second commit; (b) if the optional gate check is added, it must use the existing regex idiom (stdlib-only, no PyYAML) and scope to the two website YAML files only, since `packs/*/PACK.yaml` carries a different `source_version` class; (c) historical 1.19.1 strings (CHANGELOG history, CONTRACT example, map changelog) are keep-classified and must not be bumped.

## Evidence index

| Loc | Kind |
|-----|------|
| docs/products/website/01-jgs-se-knowledge-packs.yaml:15 | config |
| docs/products/website/catalog.yaml:13 | config |
| tooling/check_release.py:13 | doc |
| tooling/check_release.py:24 | code |
| tooling/check_release.py:27 | code |
| tooling/check_release.py:36 | code |
| tooling/check_release.py:108 | code |
| tooling/check_release.py:111 | code |
| tooling/check_release.py:115 | code |
| tooling/check_release.py:118 | code |
| tooling/check_release.py:254 | code |
| tooling/gen_packs_page.py:42 | code |
| tooling/gen_packs_page.py:43 | code |
| tooling/build_pack.py:48 | code |
| RELEASE-INFO.txt:3 | config |
| .github/workflows/validate.yml:87 | config |
| .gitignore:37 | config |
| .git/hooks/post-commit:22 | config |
| .git/hooks/post-commit:44 | config |
| .git/refs/tags/v1.20.0:1 | config |
| .planning/phases/21-contract-rewrite-release-surfaces/21-IMPL_REVIEW.md:67 | doc |
| docs/capability-map-CONTRACT.md:35 | doc |
| docs/capability-pack-map.md:18 | doc |
| CHANGELOG.md:44 | doc |
| parent git probe (for-each-ref, branch -r --contains) | config |
