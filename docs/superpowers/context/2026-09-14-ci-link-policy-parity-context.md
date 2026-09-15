# Context: ci-link-policy-parity (2026-09-14)

## Context brief

**Primary question**: Align CI link-policy HOSTS with local SOURCE_HOSTS without executing checked-out repo Python in CI.

**Sub-questions**:
1. Exact HOSTS vs SOURCE_HOSTS regexes and four-host delta.
2. Every host-list copy location.
3. Signpost exemption semantics.
4. CI trust boundary, triggers, failure idioms, scan-scope diffs.
5. Policy rules + package constraints + design choices.

**Success criteria**: SC1 regexes; SC2 copy census; SC3 signposts; SC4 trust/failure; SC5 design constraints.

**Out of scope**: leak rewrites; PyYAML/third-party actions; pack edits; P5 CI expansion.

**Budget**: single-pass context gate.

**Workspace baseline**: HEAD ffe385abca97efc7a50b3939f930f78ec5666935 on main; untracked docs/superpowers/ only.

**Parent-verified package facts** (packages.md P4): CI weaker by four hosts; prefer data file or parity check; keep trust boundary.

## Findings

Grades: CORROBORATED 6, SINGLE-SOURCE 11, CONFLICTED 0, STALE 1 (CONCERNS line refs).

| # | Claim | Grade |
|---|-------|-------|
| 1 | CI HOSTS validate.yml:43-45 is 14-token list ending dau.edu | SINGLE-SOURCE |
| 2 | Local SOURCE_HOSTS check_release.py:54 is 18-token list + four hosts | SINGLE-SOURCE |
| 3 | Delta = cisa.gov, energy.gov, nde-ed.org, everyspec.com | CORROBORATED |
| 4 | Exactly two executable banlists | CORROBORATED |
| 5 | Documentary enums: INTEGRATIONS/CONCERNS/package/CHANGELOG | SINGLE-SOURCE |
| 6 | No shared data file yet | CORROBORATED |
| 7 | Signpost skip identical in both gates | CORROBORATED |
| 8 | Live signposts: omg-signpost, se-standards-signpost | SINGLE-SOURCE |
| 9 | Local also uses signpost_dirs for pack validate + SKILLS count | SINGLE-SOURCE |
| 10 | CI never executes repo Python; local may; permissions read-all | CORROBORATED |
| 11 | CI: push main + all PRs; four inline steps | SINGLE-SOURCE |
| 12 | Local fail idiom [links] + RELEASE CHECK: FAIL | SINGLE-SOURCE |
| 13 | CI ::error + sys.exit(1 if fails) | SINGLE-SOURCE |
| 14 | Scan-scope residual differs (suffixes/SKIP_DIRS) | CORROBORATED |
| 15 | LICENSING: no source-material download links | SINGLE-SOURCE |
| 16 | Package: stdlib-only, no PyYAML, no third-party actions, no pack/P5 | SINGLE-SOURCE |
| 17 | CONCERNS proposes data-file or parity; L44-47 stale | STALE/SS |
| 18 | Data-file alone can self-weaken CI without pin/parity | SINGLE-SOURCE |

## Exact current state (quoted)

### CI - .github/workflows/validate.yml lines 43-45

```python
HOSTS = re.compile(r"https?://[^\s)\"']*(sebokwiki|nasa\.gov|ntrs|nist\.gov|"
                   r"govinfo\.gov|omg\.org|ocw\.mit|dodcio|dod\.mil|dla\.mil|"
                   r"eur-lex|europa\.eu|nato\.int|dau\.edu)")
```

Token set (14): sebokwiki, nasa.gov, ntrs, nist.gov, govinfo.gov, omg.org, ocw.mit, dodcio, dod.mil, dla.mil, eur-lex, europa.eu, nato.int, dau.edu.

### Local - tooling/check_release.py line 54

```python
SOURCE_HOSTS = re.compile(r"https?://[^\s)\"']*(sebokwiki|nasa\.gov|ntrs|nist\.gov|govinfo\.gov|omg\.org|ocw\.mit|dodcio|dod\.mil|dla\.mil|eur-lex|europa\.eu|nato\.int|dau\.edu|cisa\.gov|energy\.gov|nde-ed\.org|everyspec\.com)")
```

Token set (18): CI 14 plus cisa.gov, energy.gov, nde-ed.org, everyspec.com.

### Shared match shape

Both require https?:// scheme prefix then host-token substring. Bare domains without scheme do not match.

## Host-list copy census

### Executable banlists (must converge)

| Location | Symbol | Role |
|----------|--------|------|
| .github/workflows/validate.yml:43-45 | HOSTS | PR/main CI link-policy (weaker) |
| tooling/check_release.py:54 | SOURCE_HOSTS | local release gate check 3 (full) |

### Documentary / planning enumerations

| Location | What |
|----------|------|
| .planning/codebase/CONCERNS.md:14-17 | duplication + data-file/parity fix; stale L44-47 |
| .planning/codebase/INTEGRATIONS.md:47 | weaker 14-host CI enum ending dau.edu |
| .planning/codebase/CONVENTIONS.md:29,109 | SOURCE_HOSTS name + policy |
| .planning/codebase/ARCHITECTURE.md:54,113,158,165 | architecture notes |
| .planning/codebase/TESTING.md:15,17,66 | testing surfaces |
| .planning/codebase/STRUCTURE.md:33,92,98 | structure pointers |
| docs/superpowers/packages/2026-09-14-jgs-se-knowledge-packs-packages.md P4 | problem/evidence |
| CHANGELOG.md four-host extension bullet | bare-domain history |
| .planning/milestones/** v1.17.0 phases | historical; out of ship path |

### Non-copies

- Pack prose/PACK.yaml/LICENSE/NOTICE provenance mentions (everyspec/nde-ed/energy.gov bare).
- docs/LICENSING.md policy without token enum.
- Leak sentinels (separate duplicate; P4 out_scope).

## Signpost exception semantics

| Aspect | CI | Local |
|--------|----|-------|
| Detection | packs/*/SKILL.md + kind: signpost frontmatter | same |
| Skip | p.parent in signpost_dirs before HOSTS search | same before SOURCE_HOSTS |
| Live packs | packs/omg-signpost, packs/se-standards-signpost | same |
| Extra | none | also exclude from validate_pack + SKILLS count |

## Trust boundary and surfaces

### CI (.github/workflows/validate.yml)

- Triggers: push main; all pull_request. permissions: read-all. ubuntu-latest.
- Steps: checkout@v4; leak sentinels; link policy heredoc; frontmatter lint; catalog.json.
- Header: inline bash+python3 stdlib only; never executes checked-out repo code; .planning skipped.

### Local (tooling/check_release.py)

- Eleven checks; stdlib only; LOCAL/trusted may import tooling/*.py.
- Link hits: fail() with [links] tag; report RELEASE CHECK: FAIL; exit 1.

### Why CI must not execute repo Python

Malicious PR could run arbitrary checked-out code if workflow called check_release.py. Reading data is safe; importing/executing tooling/*.py is not.

## Policy rules

From docs/LICENSING.md section 4 + PACK-SPEC/SOURCE-VETTING:
1. Pack content upstream-licensed; tooling MIT.
2. Only Tier 1/2 sources packaged.
3. No source-material download links in packs/docs; attribution without download URI.
4. Mechanical ban on http(s) matching host tokens except kind: signpost packs.
5. .planning/ skipped (vetting evidence).

## Package constraints

- Identical 18-token lists.
- Prefer plain data file both read as data, or explicit parity check.
- Keep CI trust boundary.
- Out: leak rewrite; third-party actions; PyYAML; pack edits; P5.
- Stdlib-only.

## Design considerations the spec must settle

1. Canonical SoT: (A) shared data file both read; (B) dual inline + parity assert; (C) hybrid data file + CI trusted pin/parity.
2. Data-file trust tradeoff: PR can edit banlist and add banned URL in same PR if CI trusts checkout-only list without pin.
3. Parse-do-not-execute: read txt/json/splitlines OK; import/run tooling/*.py forbidden; no PyYAML.
4. Scope: host-list parity only; leave scan-scope residual and leak sentinels and P5 alone.
5. Failure UX: keep [links]; new parity tag e.g. [links-parity]; CI ::error naming both sides.
6. Doc sync: INTEGRATIONS 14-host enum if hard-coded.

## Synthesis

SC1-SC5 covered. Spec must choose A/B/C with explicit pin/parity answer. Minimum fix = 18-token identity on both gates.

## Evidence index

| Loc | Kind |
|-----|------|
| .github/workflows/validate.yml:1-88 | config |
| .github/workflows/validate.yml:43-45 | code (HOSTS) |
| tooling/check_release.py:4-29 | doc |
| tooling/check_release.py:54 | code (SOURCE_HOSTS) |
| tooling/check_release.py:97-107 | code (signpost+links) |
| tooling/check_release.py:319-326 | code (report) |
| .planning/codebase/CONCERNS.md:14-17 | doc |
| .planning/codebase/CONCERNS.md:60-64 | doc |
| .planning/codebase/INTEGRATIONS.md:47 | doc |
| docs/LICENSING.md | doc |
| docs/superpowers/packages/2026-09-14-jgs-se-knowledge-packs-packages.md P4 | doc |
| packs/omg-signpost/SKILL.md:3 | config |
| packs/se-standards-signpost/SKILL.md:3 | config |

