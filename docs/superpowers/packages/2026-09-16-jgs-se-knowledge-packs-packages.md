---
date: 2026-09-16
project: jgs-se-knowledge-packs
mode: light
rounds: 1
input_digest: 3347c22b9ee38b0f0974a13cb3c4aa4d900953d274f918ab3561cb7b9ac746b4
open_objections: []
---

# Work packages - jgs-se-knowledge-packs (2026-09-16, light re-run)

Context: bare package-loop after visual cut merged to main (`d62e352`). P9-P14 done. User noticed public landing still says **54 packs** while live catalogue is **65 skills (63 content + 2 signposts)**. RELEASE CHECK PASS; no gate locks landing family counts to `packs/`.

## Carry-forward status

| id | name | status |
|----|------|--------|
| P1-P7 | tooling/CI cut | done |
| P8 | phase21-planning-ledger-close | in-flight (frozen) |
| P9-P14 | visual website cut | done |

Done packages are out of the candidate space. New work starts at **P15**.

## P15 - landing-catalogue-count-truth

- **id**: P15
- **name**: landing-catalogue-count-truth
- **size**: M
- **status**: done
- **promoted_ids**: []
- **corroboration**: 3 (value, risk, cohesion)
- **deps**: none

**problem**: After the visual cut shipped, the public landing and its catalogue still still advertise **54 packs · 2 signposts**. Live inventory is **65** pack dirs (**63** content + **2** signposts). `docs/packs.html` already says 65 skills; README badge says 63 packs. The falsehood is hand-edited `docs/index.html` §06 (heading, family chips summing to 54, figcaption) plus `docs/assets/still-catalogue.svg` / `.png`. Nothing in `check_release` fails when those strings drift.

**evidence**:
- docs/index.html:226 `<h2>54 packs · 2 signposts</h2>`
- docs/index.html:228-235 family chips hand-sum to 54
- docs/index.html:241 figcaption "Fifty-four packs..."
- docs/assets/still-catalogue.svg:12 and :24 "54 packs · 2 signposts"
- docs/packs.html:12,103 "65 skills"
- SKILLS.md / packs/: 63 content + 2 signposts
- tooling/check_release.py index check compares SKILLS.md to packs only, not landing chips

**in_scope**:
- Recount live `packs/` (signpost-aware) into §06 totals and family chips; align wording with packs.html / README conventions (63 content + 2 signposts, or 65 skills)
- Rewrite docs/index.html §06 heading, chips, and FIG.06 figcaption
- Update docs/assets/still-catalogue.svg labels and regenerate still-catalogue.png so art matches
- Minimal fail-closed assert in check_release (and CI twin if required by existing pattern) so landing catalogue count strings cannot regress vs live packs/ / SKILLS.md

**out_scope**: P8 ledger/ship; reopening P9-P14; catalog.json rewrite (P16); packs.html SPA redesign; installer/OneDrive/perf pets; version bump unless needed to publish

**why_now**: Highest public falsehood left after visual ship; user already noticed. Gate gap means a one-off text fix will rot on the next pack add.

**first_prompt**: `/superpowers-process full fix landing §06 and still-catalogue pack counts to live 63+2/65 and add minimal drift gate`

## P16 - catalog-live-set-parity

- **id**: P16
- **name**: catalog-live-set-parity
- **size**: M
- **status**: ready
- **promoted_ids**: [b-03]
- **corroboration**: 1 (risk)
- **deps**: none
- **triage notes**: single-lens; kept as bounded machine-catalogue honesty, parallel to P15 public copy

**problem**: `catalog.json` is a required release artifact but is only existence- and JSON-parse-checked. `updated` is still **2026-08-17** while RELEASE-INFO stages **2026-08-27** (open backlog **b-03**). No gate diffs live slugs to `packs/*` (signpost policy included). Same drift class as landing counts, on the machine-readable catalogue.

**evidence**:
- catalog.json:5 `"updated": "2026-08-17"`
- RELEASE-INFO.txt:5 staged 2026-08-27
- docs/superpowers/backlog.md b-03 open
- tooling/check_release.py REQUIRED_FILES includes catalog.json; no slug-set parity
- .github/workflows/validate.yml Catalog JSON valid is parse-only

**in_scope**:
- Refresh catalog.json live inventory/metadata to match current packs/ policy (signposts explicit)
- Fail-closed local gate: catalog live slug set vs packs/; verify updated vs staging convention
- CI twin or documented residual if CI stays no-repo-code

**out_scope**: landing HTML/still (P15); P8; adding planned sources as packs; ATTR scanner residual

**why_now**: b-03 survived tooling and visual cuts; public and SKILLS surfaces moved while catalog stayed parse-only.

**first_prompt**: `/superpowers-process full refresh catalog.json to live packs and gate slug-set parity`

## Dependency order (triage, light round 1)

P15, P16 (independent; either may start first. Prefer **P15** first: user-visible lie.)

## Human forks

None. P8 remains frozen outside this cut.

## Backlog

See [backlog.md](../backlog.md). Delta: b-03 promoted into P16; b-23 evidence note that docs/assets images now exist (LFS still needs-info); no other status deletes.
