# Phase 12: Map regen + hygiene + gate wiring — Research

**Researched:** 2026-08-17
**Domain:** Capability-pack map agent regen + MAP-19-02 floor + `check_release` wiring + v1.18 hygiene backlog
**Confidence:** HIGH on map regen vs apply, live floor counts, remap table, wiring shape, hygiene file locations, and Phase 13 fence. MEDIUM on exact post-regen chapter→cluster placements for the 16 unmapped chapters (judgment pass; hints below, not a generator).

<user_constraints>
## User Constraints (from STATE / REQUIREMENTS / ROADMAP / Phase 11; no CONTEXT.md)

**CRITICAL:** Discuss was skipped. There is no `12-CONTEXT.md`. Locked decisions below are taken from REQUIREMENTS MAP-19 + HYG, ROADMAP Phase 12, STATE.md, SEED-001, and the Phase 11 remap/handoff artifacts — these MUST be honored.

### Locked Decisions

- **MAP-19-01 is an agent pass + gate, not a script.** There is no committed map generator. FUT-05 (deterministic generator) stays deferred. [VERIFIED: `.planning/REQUIREMENTS.md:31` — "Regenerate capability-pack-map.json (agent pass + `check_capability_map.py`)"; `.planning/REQUIREMENTS.md:55` — "FUT-05 deterministic map generator | Still agent-judgment; keep FUT-05"]
- **MAP-19-03 apply list is AUTHORITATIVE** — do not re-pick chapters. Move only `federal-bca` `ch04-uncertainty-and-sensitivity.md` + `ch06-reporting-and-decision-use.md` and `dod-vva-rpg` `ch06-accreditation-agent-role.md` into Decision Analysis & Trade Studies (cluster 16). Leave federal-bca ch01–ch03, ch05 (+ support files) in Opportunity; leave dod-vva-rpg ch08 in Validation and ch10 in Risk. [VERIFIED: `.planning/phases/11-io-unlocking-packs-decision-analysis-remap/11-02-SUMMARY.md:163-171`]
- **MAP-19-02 floor is conjunctive:** no listed competency *primary* remains at **count < 4 AND 1 pack**. Listed primaries that must each *move*: Decision Analysis, Validation, Integration, Interfaces, Ops/Maint. [VERIFIED: `.planning/REQUIREMENTS.md:32`]
- **MAP-19-04 wires the existing gate** into `check_release.py`. Do not invent a second map checker. Do not bump version surfaces to make the wire pass. [VERIFIED: `.planning/REQUIREMENTS.md:34`; `.planning/ROADMAP.md:68`]
- **MAP-19-05 is one paragraph in `docs/capability-map-CONTRACT.md`:** live snapshot is 628+; 502 is residue; Cybersecurity + Digital Engineering remain unbound (se-agents-side). Do not bind those clusters here. [VERIFIED: `.planning/REQUIREMENTS.md:35`]
- **HYG-03 may be "record as external-repo PR"** — sibling `jgs-reference-skill` is not this execute tree. [VERIFIED: `.planning/ROADMAP.md:70` — "vet_source EXCLUDED sync done or recorded as external-repo PR"]
- **Phase 13 owns REL-19-01/02.** Do not steal catalog `dod-vva-rpg.chapters` 10→13, README catalogue rows, plugin/CHANGELOG version bump, tag, or GitHub Release. Thin-register already keeps `check_release` green at 1.18.0. [VERIFIED: `.planning/ROADMAP.md:74-82`; `.planning/phases/11-io-unlocking-packs-decision-analysis-remap/11-GAP_ANALYSIS.md:114`]
- **Do not build** Army CBA / AAF / stakeholder / `dodm-5000-102`. IO-05/06 DEFERRED; IO-07 ACCEPT. [VERIFIED: `.planning/phases/11-io-unlocking-packs-decision-analysis-remap/11-GAP_ANALYSIS.md:112`]
- Stay on `main`. No branches / worktrees.

### Claude's Discretion

- Whether MAP-19-02 extra assert is encoded in `check_capability_map.py` THRESHOLDS or verified by a one-shot python print in the plan (see §MAP-19-02). Recommendation: **name-keyed minimums of 4 entries** on the five listed primaries (matches existing THRESHOLDS style); pack-diversity of the conjunct is a verify print, not a second gate dimension, because none of the five is 1-pack after Phase 11+remap.
- `map_version` string during Phase 12: keep `"1.18.0"` (matches plugin/CHANGELOG/RELEASE-INFO) **or** write `"1.19.0"` early. Recommendation: **keep `1.18.0`** so `check_release` version-single-source stays green; Phase 13 bumps all version surfaces together. `generated_on` updates to execution day.
- Whether new packs include support-file rows. Recommendation: **omit** — both `nasa-std-8719-14` and `is-gps-200n` will be multi-cluster (Ops vs Safety/Governance; Interfaces vs CM/Traceability).
- HYG-03: open sibling PR now vs record-only. Recommendation: **record as external PR/issue** unless the sibling tree is already writable in the same session; do not block Phase 12 close on an external merge.

### Deferred Ideas (OUT OF SCOPE)

- REL-19-01 full registration (catalog chapter integer, README live-pack table rows, NOTICE/SKILLS already thin-registered)
- REL-19-02 `v1.19.0` tag + GitHub Release + CHANGELOG `[1.19.0]` entry
- FUT-05 deterministic map generator
- Committed overlap checker (7-CODE-REVIEW IN-02)
- se-agents consumer refresh (502 docs, `thin: 3` align, 20-ref cap, Cyber/DE *bindings*)
- 881F/VV&A DIST-A in-PDF revisit (7-GAP R4)
- Building AAF / Army CBA / stakeholder / DoDM / SP-7084 / IS-300
</user_constraints>

<architectural_responsibility_map>
## Architectural Responsibility Map

Single-tier content library — no Browser/Client, API, or Database runtime. Phase 12 capabilities live in committed map artifacts, two stdlib gates, and cosmetic pack/docs edits.

| Capability | Primary Tier | Secondary Tier | Rationale |
|------------|-------------|----------------|-----------|
| Agent classification + MAP-19-03 apply | `docs/capability-pack-map.json` | `docs/capability-pack-map.md` | CONTRACT refresh path: JSON + md committed together |
| MAP-19-02 floor | `tooling/check_capability_map.py` THRESHOLDS | one-shot verify print | Name-keyed, never array index |
| MAP-19-04 wire | `tooling/check_release.py` | `tooling/check_capability_map.py:main()` | Import + call; no subprocess |
| MAP-19-05 consumer note | `docs/capability-map-CONTRACT.md` | optional one-liner in map.md changelog | Pack-side contract only |
| HYG-01 BOM + pin | `CHANGELOG.md` + new `.gitattributes` | — | File encoding / checkout hygiene |
| HYG-02 topic-index | 4 shipped `packs/*/SKILL.md` | `validate_pack.py` re-run | Cosmetic; revalidate after touch |
| HYG-03 EXCLUDED sync | sibling `jgs-reference-skill` | Phase 12 SUMMARY record | External repo; record-as-PR is a valid close |
| HYG-04 "(c)" wording | `packs/federal-bca/PACK.yaml` notes | — | Cosmetic; substance already clean |
| Version / catalog / tag | **Phase 13** | — | Do not steal |
</architectural_responsibility_map>

<research_summary>
## Summary

Phase 12 is **map apply + regen + floor + wire + hygiene**, not pack construction. The live map is still the Phase 8 artifact: schema 2, `map_version` `"1.18.0"`, `generated_on` `"2026-08-17"`, **628 entries / 32 clusters / 61 mapped packs**. Phase 11 left it untouched on purpose. `check_capability_map.py` is **RED (19 issues)**: two new slugs (`nasa-std-8719-14`, `is-gps-200n`) plus 16 on-disk-only chapters (7 + 6 + `dod-vva-rpg` ch11–ch13). `check_release.py` is **PASS** and does **not** import the map gate. [VERIFIED: live `python tooling/check_capability_map.py` exit 1, 19 issues, 2026-08-17; `python tooling/check_release.py` → `RELEASE CHECK: PASS`; `tooling/check_capability_map.py:16-17`]

There is **no generator**. Regeneration is the Phase 8 pattern: agent classification per `docs/capability-pack-map.md` rules of construction, then the stdlib gate. MAP-19-03 is a *move*, not a new pack: three named chapters change cluster. After that move Decision Analysis goes **2→5 entries / 2→4 packs**, which satisfies both "leaves 2" and the MAP-19-02 conjunct for that primary. The other four listed primaries move by *adding* the Phase 11 chapters/packs (Validation +ch11–ch13 if classified there; Interfaces +`is-gps-200n`; Ops/Maint +`nasa-std-8719-14`; Integration has no new pack — AAF deferred — so it must move by honest classification of existing leftover chapters **or** the planner must record that Integration already sits at 4/4 and is not `<4 AND 1 pack`). Hygiene is four small in-tree nits plus an external-repo EXCLUDED sync that may close as a recorded PR.

**Primary recommendation:** Two execute plans. Plan 12-01 = map regen (classify 16 new chapters + apply the three-row remap + bump `generated_on` + sync md + MAP-19-02 thresholds + CONTRACT paragraph). Plan 12-02 = wire `check_capability_map.main()` into `check_release` + HYG-01..04. Do not bump `1.18.0` version surfaces. Do not write PLAN.md here.
</research_summary>

<standard_stack>
## Standard Stack

This repo does not add a library for map work. Copy the Phase 8 analog.

### Core

| Artifact | Version / location | Purpose | Why standard |
|---------|--------------------|---------|--------------|
| Agent classification pass | Phase 8 pattern | Chapter → exactly one of 32 named clusters | Judgment required; FUT-05 deferred |
| `docs/capability-pack-map.json` | schema 2, `map_version` `"1.18.0"`, 628 entries | Machine consumer for se-agents | FR-2.1 reads `name` → `{pack, chapter}` |
| `docs/capability-pack-map.md` | living human table | Rules of construction + summary counts | Must stay byte-aligned with JSON counts |
| `docs/capability-map-CONTRACT.md` | v2 contract | Schema / versioning / refresh / thresholds | MAP-19-05 home |
| `tooling/check_capability_map.py` | stdlib, standalone today | Envelope, bidirectional staleness, uniqueness, name-keyed floors | Phase 8 AE-01 |
| `tooling/check_release.py` | stdlib aggregator | Local release gate; already imports `validate_pack` + `gen_packs_page` | MAP-19-04 host |
| `tooling/validate_pack.py` | repo | Re-run after HYG-02 SKILL.md edits | PACK-SPEC |

`$REF` = `C:/Users/gower/OneDrive/Documents/GitHub/jgs-reference-skill` (HYG-03 only). On Windows/Git Bash use `python`.

### Supporting

| Artifact | Purpose | When to use |
|---------|---------|-------------|
| 11-02-SUMMARY remap table | AUTHORITATIVE MAP-19-03 apply list | Do not re-guess |
| Phase 11 SKILL.md When-to-use | Classification spot-check | Per new pack / leftover chapter |
| `.gitattributes` (new) | `*.md text eol=lf` | HYG-01 |
| Sibling `tools/vet_source.py` | EXCLUDED keyword dict | HYG-03; out of tree |

### Alternatives Considered

| Instead of | Could Use | Tradeoff |
|------------|-----------|----------|
| Deterministic map generator | Agent pass (locked) | FUT-05 stays future; Phase 8 already shipped this way |
| New Decision Analysis pack | MAP-19-03 three-chapter move | Army CBA NO-GO; table already written |
| Subprocess to map gate | `import check_capability_map; rc = check_capability_map.main()` | Matches existing `validate_pack` import style; no shell |
| Bump `map_version` to 1.19.0 now | Keep `"1.18.0"` until Phase 13 | Avoids inventing a version surface `check_release` does not even read; keeps envelope honest to the unreleased tree |
| Bind Cyber/DE in this repo | One CONTRACT paragraph | Binding is se-agents-side (SEED-001) |

**Installation:** none.
</standard_stack>

<architecture_patterns>
## Architecture Patterns

### System Architecture Diagram

```text
  packs/ on disk (Phase 11 complete)
    nasa-std-8719-14 (7 ch)     -- unmapped
    is-gps-200n (6 ch)          -- unmapped
    dod-vva-rpg ch11-ch13       -- unmapped
    federal-bca ch04, ch06      -- mapped, WRONG cluster (Opportunity)
    dod-vva-rpg ch06            -- mapped, WRONG cluster (Assurance)
           |
           v
  Agent pass (MAP-19-01)
    classify 16 new chapters (1 cluster each)
    apply MAP-19-03 three-row MOVE (do not duplicate rows)
    omit support files for multi-cluster new packs
    set generated_on = execution day; keep map_version 1.18.0
    sync capability-pack-map.md summary + changelog line
           |
           +-- extra THRESHOLDS for five listed primaries (>=4 entries)
           v
  check_capability_map.py  --> must PASS (staleness 0, uniqueness, floors)
           |
           +-- CONTRACT.md paragraph (628+ live; 502 residue; Cyber/DE unbound)
           |
           v
  check_release.py imports check_capability_map.main()   (MAP-19-04)
           |
           +-- HYG-01 BOM + .gitattributes
           +-- HYG-02 four SKILL.md nits + validate_pack
           +-- HYG-03 sibling EXCLUDED or recorded external PR
           +-- HYG-04 PACK.yaml "(c)" wording
           |
           v
  Phase 13: REL-19 catalog/version/tag  (do not start)
```

### Recommended Project Structure (Phase 12 outputs)

```
docs/capability-pack-map.json          # regen + remap
docs/capability-pack-map.md            # summary counts + v1.19 changelog line
docs/capability-map-CONTRACT.md        # MAP-19-05 paragraph + refresh-path wire note
tooling/check_capability_map.py        # MAP-19-02 extra THRESHOLDS; docstring no longer "standalone"
tooling/check_release.py               # invoke map gate
CHANGELOG.md                           # strip BOM + LF only (NO new [1.19.0] section)
.gitattributes                         # NEW: *.md text eol=lf
packs/mil-std-881f/SKILL.md            # HYG-02 alpha
packs/dafman-63-119/SKILL.md           # HYG-02 alpha
packs/mil-std-40051/SKILL.md           # HYG-02 drop circular target
packs/federal-bca/SKILL.md             # HYG-02 label
packs/federal-bca/PACK.yaml            # HYG-04 wording
```

Do **not** create a generator script. Do **not** edit catalog.json / plugin.json / RELEASE-INFO.txt / README live-pack table.

### Pattern 1: Agent regen (MAP-19-01) — copy Phase 8

**What:** Hand-edit the JSON envelope + cluster chapter arrays. Every `packs/<slug>/chapters/*` file is assigned to exactly one cluster. Support files (`glossary.md` / `patterns.md` / `cheatsheet.md` marked `"<file> (support file)"`) only for essentially single-cluster packs. Process definitions → cluster 30 (Standards, Tailoring & Process Models); performing the capability → the capability cluster. Cross-cutting chapters keep a secondary-fit remark in `note`. [VERIFIED: `docs/capability-pack-map.md:6-12`]

**When to use:** Any time packs/chapters are added, renamed, or deleted.

**How Phase 8 did it:** write JSON, sync md summary table + changelog bullet, run the gate twice (idempotent stdout), commit json+md together. [VERIFIED: `docs/capability-map-CONTRACT.md:66-79`; `.planning/phases/8-agent-enablement-surface/8-01-SUMMARY.md:95-100`]

**Live start state (must go GREEN):**

| Check | Live value |
|---|---|
| Envelope | `schema_version` 2, `map_version` `"1.18.0"`, `generated_on` `"2026-08-17"` [VERIFIED: `docs/capability-pack-map.json:2-4`] |
| Totals | 32 clusters, 628 entries, 61 mapped packs [VERIFIED: live python query 2026-08-17] |
| Disk not mapped | `is-gps-200n`, `nasa-std-8719-14` |
| On-disk-only chapters (16) | `dod-vva-rpg` ch11–ch13; `is-gps-200n` ch01–ch06; `nasa-std-8719-14` ch01–ch07 |
| Map-only chapters | 0 |
| Gate | FAIL 19 issues [VERIFIED: live `python tooling/check_capability_map.py`] |

Expected post-regen arithmetic (if remap applied and 16 chapters added, no new support rows): **628 + 16 = 644 entries**, 63 chapter-bearing packs mapped. Opportunity drops 2 (ch04+ch06 move). Decision Analysis +3. Assurance −1. Other deltas depend on classification (see hints).

### Pattern 2: MAP-19-03 apply — move, do not copy

Uniqueness is on `(pack, chapter)` across *all* clusters. Copying a row into cluster 16 without deleting the old row fails the gate. [VERIFIED: `tooling/check_capability_map.py:138-147`]

Authoritative table [VERIFIED: `11-02-SUMMARY.md:163-171`]:

| Pack | Chapter | From (today, live) | To |
|---|---|---|---|
| `federal-bca` | `ch06-reporting-and-decision-use.md` | Opportunity/Benefit Management (`docs/capability-pack-map.json:1115-1117`, note already says "also decision analysis") | Decision Analysis & Trade Studies |
| `federal-bca` | `ch04-uncertainty-and-sensitivity.md` | Opportunity/Benefit Management (`:1105-1107`) | Decision Analysis & Trade Studies |
| `dod-vva-rpg` | `ch06-accreditation-agent-role.md` | Assurance & System Assurance (`:3260-3262`) | Decision Analysis & Trade Studies |

Leave in place: federal-bca ch01–ch03, ch05 + 3 support files (Opportunity stays ≥2, currently 10→8). dod-vva-rpg ch08 stays Validation; ch10 stays Risk.

Result quoted by Phase 11 (Decision Analysis only): **2 → 5 entries, 2 → 4 packs**. [VERIFIED: `11-02-SUMMARY.md:171`] Live DA today [VERIFIED: `docs/capability-pack-map.json:1136-1148`]:

- `nasa-ceh` / `ch06-nasa-ceh-decision-support-analyses.md`
- `nasa-se-handbook` / `ch34-6-8-decision-analysis.md`

### Pattern 3: MAP-19-02 floor — conjunct, not "every primary ≥4"

SEED-001 / REQUIREMENTS wording: extra assert vs v1.18 SC-2 — **no competency primary remains at count < 4 AND 1 pack**. Listed primaries that **must each move**: Decision Analysis, Validation, Integration, Interfaces, Ops/Maint. [VERIFIED: `.planning/REQUIREMENTS.md:32`; `.planning/seeds/SEED-001-agent-io-pack-depth.md:34`]

Live counts AFTER Phase 11 packs exist on disk but BEFORE remap/regen (map still 1.18):

| Primary cluster | Entries | Packs | `<4 AND 1 pack` today? | How it moves in Phase 12 |
|---|---:|---:|---|---|
| Decision Analysis & Trade Studies | 2 | 2 | No (2 packs) but **count < 4** and listed | MAP-19-03 → 5 / 4 |
| Validation | 5 | 4 | No | Classify leftover RPG ch11–ch13 here (depth) |
| Integration | 4 | 4 | No | **No new pack** (IO-05 DEFERRED). Already not `<4 AND 1 pack`. "Must move" cannot mean a new pack. |
| Interface Management & ICIDs | 4 | 3 | No | Classify `is-gps-200n` here (IO-04) |
| Operations, Maintenance & Disposal | 6 | 4 | No | Classify `nasa-std-8719-14` here (IO-03) |

None of the five is currently 1-pack. The dangerous case the conjunct names (`<4 entries AND 1 pack`) is **vacuous today**. The listed-primary "must each move" clause is the real planning constraint:

- DA moves via remap (locked).
- Interfaces / Ops move via new-pack classification (locked targets).
- Validation moves via leftover RPG classification (prefer ch12+ch13 Validation; ch11 is T&E-facing — see hints).
- Integration: **do not invent a pack**. Planner should treat "move" as "floor still held at 4/4; AAF remains deferred" and **not** raid other clusters to decorate Integration. Encoding `THRESHOLDS["Integration"] = 4` preserves the floor without forcing a fake move.

Existing THRESHOLDS (do not weaken) [VERIFIED: `tooling/check_capability_map.py:34-39`]:

```
Training & Documentation Delivery: 1
Requirements Traceability & Allocation: 3
Interface Management & ICIDs: 3
Opportunity/Benefit Management: 2
```

Recommended additions (name-keyed, never index):

```
Decision Analysis & Trade Studies: 4
Validation: 4
Integration: 4
Operations, Maintenance & Disposal: 4
```

Interfaces already has minimum 3; raise to **4** so MAP-19-02 is mechanically enforced for that listed primary. Opportunity minimum 2 still holds after losing ch04+ch06 (8 remaining).

The "AND 1 pack" half is **not** expressible as a single integer THRESHOLD. Verify with a one-shot print of `(count, n_packs)` for the five names; fail the plan if any pair is `(count < 4 and n_packs == 1)`.

### Pattern 4: Wire map gate into check_release (MAP-19-04)

Phase 8 deferred this; Phase 9 confirmed it still standalone. [VERIFIED: `tooling/check_capability_map.py:16-17` — "Standalone — not imported by check_release.py (Phase 9 may wire it)."; `.planning/phases/9-release-surface-v1-18-0/9-INTEGRATION_CHECK.md:37`]

`check_release.py` already does in-process imports, not subprocess [VERIFIED: `tooling/check_release.py:119-154`]:

```python
sys.path.insert(0, str(ROOT / "tooling"))
import validate_pack
import gen_packs_page
```

**Do this:** after the existing pack / SKILLS / cursor / header checks (or as a new numbered bullet before the final report), call `check_capability_map.main()` and `fail()` if it returns non-zero. Capture or let it print its own cluster-count block (duplicate stdout is fine). **Do not** subprocess. **Do not** duplicate THRESHOLDS.

**Do not break Phase 13 version surfaces:**

- `check_release` §4 compares `.claude-plugin/plugin.json` == CHANGELOG top `## [N.N.N]` == `RELEASE-INFO.txt`. All three are **1.18.0** today. [VERIFIED: live plugin 1.18.0; `CHANGELOG.md:12` — `## [1.18.0]: 2026-08-17`]
- Map `map_version` is **not** in that trio. Wiring the map gate does **not** require bumping 1.18.0 → 1.19.0.
- CI `.github/workflows/validate.yml` "never executes checked-out repository code" [VERIFIED: `.github/workflows/validate.yml:4-6`]. Do **not** add a CI step that runs `tooling/check_capability_map.py`. Local `check_release` is the wire target.
- After wiring, `python tooling/check_release.py` will FAIL until the map is GREEN. Sequence the plans so regen lands before (or in the same plan before) the wire, or the wire commit is allowed to go red only if it is not the last commit — prefer **regen first, wire second**.

Update CONTRACT §4 sentence "The gate is standalone (not wired…)" [VERIFIED: `docs/capability-map-CONTRACT.md:81-82`] when the wire lands.

### Pattern 5: Hygiene four-pack

**HYG-01** — CHANGELOG has a UTF-8 BOM and CRLF. `.gitattributes` does not exist. [VERIFIED: first bytes `ef bb bf 3c`; no `.gitattributes` on disk; REQUIREMENTS:39 — `*.md text eol=lf`]

- Strip BOM from `CHANGELOG.md`; normalize that file to LF.
- Add `.gitattributes` with `*.md text eol=lf` (and nothing else unless needed). Do not rewrite the whole repo's line endings in this phase.
- Do **not** add a `## [1.19.0]` section (Phase 13).

**HYG-02** — 7-GAP R6 / IN-01, still live [VERIFIED: `.planning/phases/7-gap-driven-pack-builds/7-CODE_REVIEW.md:83-88` + live files]:

| File | Nit | Live line | Fix |
|---|---|---|---|
| `packs/mil-std-881f/SKILL.md` | `"PM / measurement / EVMS mapping"` last, out of alpha (belongs between Missile/ordnance and Program Element) | `:89` | Re-sort |
| `packs/dafman-63-119/SKILL.md` | `"AFOTEC / …"` after `"Agile / …"` | `:64-65` | Re-sort AFOTEC before Agile |
| `packs/mil-std-40051/SKILL.md` | `"Training & Documentation" → ch01, ch07, ch08, Topic Index` circular | `:77` | Drop `, Topic Index` |
| `packs/federal-bca/SKILL.md` | `"Opportunity/Benefit Analysis"` invented label | `:74` | Rename to `Opportunity cost / benefit identification` |

Re-run `python tooling/validate_pack.py` on the four slugs after edits.

**HYG-03** — sibling `vet_source.py` `EXCLUDED` has iso/iec/ieee/incose/swebok/mitre/omg/togaf/wiley… and **does not** list `afotec`, `dod dag`/`defense acquisition guidebook`, or `cmu`/`sei`. [VERIFIED: `C:/Users/gower/OneDrive/Documents/GitHub/jgs-reference-skill/tools/vet_source.py:41-56`; `.planning/phases/6-source-vetting-unverified-resolution/6-GAP_ANALYSIS.md:52-61`]

Valid close: land keys in the sibling repo **or** record an external issue/PR URL + the three keywords in the Phase 12 SUMMARY. Do not vendor `vet_source.py` into this repo.

**HYG-04** — `packs/federal-bca/PACK.yaml:20` says `no third-party copyright / (c) / all-rights-reserved notices`. Substance is clean (8 literal `(c)` hits in the A-94 extract are enumeration markers). [VERIFIED: `.planning/phases/7-gap-driven-pack-builds/7-GAP_ANALYSIS.md:41`; `packs/federal-bca/PACK.yaml:19-20`]

Fix: reword to something like `no third-party copyright / all-rights-reserved notices (literal "(c)" hits in A-94 are enumeration markers, not copyright claims)`.

### Classification hints (16 new chapters — judgment, not locked)

Hints from 11-RESEARCH chapter strategy + SKILL.md When-to-use. Spot-check each chapter lead before assigning.

**`nasa-std-8719-14` → Ops/Maint/Disposal primary (IO-03).** Support files: omit (likely multi-cluster if ch04 leans Safety or ch07 leans Governance).

| Chapter | Hint cluster |
|---|---|
| ch01-scope-and-applicability.md | Ops/Maint/Disposal (or Standards if read as process-definition) |
| ch02-assessment-overview.md | Ops/Maint/Disposal |
| ch03-debris-released-normal-operations.md | Ops/Maint/Disposal |
| ch04-explosions-breakups-collisions.md | Ops/Maint/Disposal; note Safety secondary |
| ch05-postmission-disposal.md | **Ops/Maint/Disposal (primary gold)** |
| ch06-reentry-surviving-debris.md | Ops/Maint/Disposal |
| ch07-special-classes-odar-eomp.md | Ops/Maint/Disposal; note Governance secondary |

**`is-gps-200n` → Interface Management & ICIDs primary (IO-04).** Support files: omit (ch01 is CM/change-control). Complementary to `faa-std-025` (prep vs live ICD).

| Chapter | Hint cluster |
|---|---|
| ch01-is-scope-and-change-control.md | Configuration Management (IRN/CCB) **or** Interfaces if read as "what an ICD is" |
| ch02-interface-definition-and-identification.md | **Interface Management & ICIDs** |
| ch03-interface-criteria-pattern.md | **Interface Management & ICIDs** |
| ch04-nav-data-as-payload.md | Interface Management |
| ch05-time-and-definition-hygiene.md | Interface Management |
| ch06-appendices-as-a-map.md | Interface Management (or Standards if "how the IS is structured") |

Do not dump into Requirements Traceability just because the Topic Index mentions it.

**`dod-vva-rpg` leftovers (IO-02 chapters-not-a-pack):**

| Chapter | Hint cluster | Do not |
|---|---|---|
| ch11-te-vv-checklist.md | Test & Evaluation (integration of T&E and V&V) **or** Verification | Do not force Integration (IO-05 is AAF, not this checklist) |
| ch12-developing-the-referent.md | **Validation** | |
| ch13-conceptual-model-development-and-validation.md | **Validation** | |

ch08 stays Validation. ch06 *moves* to Decision Analysis (MAP-19-03). ch10 stays Risk.

### Anti-Patterns to Avoid

- **Writing a map generator.** FUT-05 is explicitly out of scope.
- **Copying remap rows** so a chapter sits in two clusters. Gate uniqueness fails.
- **Re-picking IO-01 chapters** (e.g. moving all of federal-bca, or dod-vva ch08/ch10).
- **Collapsing Opportunity** below its floor by moving ch01–ch03/ch05/support files.
- **Inventing an Integration pack** or rematching SEBoK to "move" Integration.
- **Binding Cyber/DE** or refreshing se-agents 502 docs in this repo.
- **Bumping plugin / CHANGELOG / RELEASE-INFO / tag** so the new wire "looks like 1.19".
- **CI executing repo Python** (`validate.yml` contract).
- **Vendoring `vet_source.py`** to fake HYG-03 in-tree.
- **Stealing P13-REG-1** (catalog `dod-vva-rpg.chapters` 10→13, README new-slug rows).
</architecture_patterns>

<dont_hand_roll>
## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| Map freshness | New generator / schema 3 | Agent pass + existing gate | FUT-05 deferred; v2 envelope already consumed |
| Decision Analysis depth | New CBA / trade-study pack | MAP-19-03 three-row move | Army CBA NO-GO; table locked |
| Release-time map drift | Separate CI workflow that runs repo code | `check_release` import of `main()` | CI must not exec repo Python; local gate is the contract |
| EXCLUDED sync | Copy of vet_source into `tooling/` | Sibling PR or recorded external issue | 6-GAP Thread 3: human rubric + `validate_pack` already block Excluded from shipping |
| Topic-index "smart" rewrite | Regenerating whole SKILL.md bodies | Four one-line edits | IN-01 listed exact lines + exact fixes |
| Floor encoding | New pack-count schema field | Existing name-keyed THRESHOLDS + verify print | Gate already fails loud on unknown names |

**Key insight:** Phase 12 is almost entirely *apply already-decided deltas*. The only judgment is classifying 16 new chapters. Everything else is a move, a wire, or a wording nit.
</dont_hand_roll>

<common_pitfalls>
## Common Pitfalls

### Pitfall 1: Regen without applying the remap (or remap without classifying new packs)
**What goes wrong:** Gate still RED on 16 missing chapters, *or* DA stays at 2/2 while new packs are mapped.
**Why it happens:** MAP-19-01 and MAP-19-03 look like two tasks; Phase 11 forbade touching JSON so both land now.
**How to avoid:** One agent pass does both. Verify DA = 5/4 and on_disk_only = 0 in the same gate run.
**Warning signs:** `git diff` on the map moves ch04/ch06 but still lists `staleness: pack on disk not in map: nasa-std-8719-14`.

### Pitfall 2: Wiring check_release before the map is GREEN
**What goes wrong:** `check_release.py` flips from PASS → FAIL on `main` mid-phase; thin-register value is lost.
**Why it happens:** MAP-19-04 is a one-liner and looks cheap.
**How to avoid:** Plan 12-01 regen+floor+CONTRACT first (gate GREEN standalone); Plan 12-02 wire + hygiene. After wire, both commands PASS.
**Warning signs:** First commit of the phase touches only `check_release.py`.

### Pitfall 3: Bumping `map_version` / plugin to 1.19.0
**What goes wrong:** `check_release` version-single-source fails (plugin 1.19 vs CHANGELOG 1.18) *or* Phase 13 has nothing left to tag.
**Why it happens:** CONTRACT says `map_version` tracks the release that regenerated the map.
**How to avoid:** Keep `map_version` `"1.18.0"`; update `generated_on` only. Phase 13 sets `map_version` `"1.19.0"` with the rest of the version surfaces.
**Warning signs:** Diff includes `.claude-plugin/plugin.json` or a new CHANGELOG `## [1.19.0]`.

### Pitfall 4: Treating Integration "must move" as a pack-build
**What goes wrong:** Invented AAF/integration pack, or random chapters stolen into Integration to show a delta.
**Why it happens:** REQUIREMENTS lists Integration among primaries that "must each move"; IO-05 is deferred.
**How to avoid:** Integration is already 4/4 — the conjunct floor holds. Record IO-05 deferred; set THRESHOLDS Integration ≥ 4; do not raid.
**Warning signs:** New slug under `packs/` or SEBoK rematch sold as Integration depth.

### Pitfall 5: Support-file over-inclusion
**What goes wrong:** New packs get 3 support-file rows each even though they are multi-cluster, polluting counts and violating rules of construction.
**Why it happens:** Phase 8 included support files for single-cluster `federal-bca` / `mil-std-40051`.
**How to avoid:** Omit support files unless the pack is essentially one cluster after classification.
**Warning signs:** +6 unexpected entries from `glossary/patterns/cheatsheet` on 8719/200N.

### Pitfall 6: HYG-03 blocking close
**What goes wrong:** Phase 12 stays open waiting on a sibling merge.
**Why it happens:** REQUIREMENTS says "add … to jgs-reference-skill" without repeating ROADMAP's "or recorded as external-repo PR".
**How to avoid:** Prefer a recorded issue/PR with the three keywords; in-tree close does not require the sibling merge.
**Warning signs:** Plan task `done` requires `git -C $REF log` to show a merge on `main`.

### Pitfall 7: Stealing Phase 13 leftovers
**What goes wrong:** catalog `dod-vva-rpg.chapters` bumped 10→13; README gains 8719/200N rows; those look like "map-adjacent hygiene".
**Why it happens:** 11-GAP / 11-INTEGRATION listed them as leftovers in the same breath as map RED.
**How to avoid:** Those leftovers are **P13-REG-1**. Map apply does not read catalog chapter integers.
**Warning signs:** `catalog.json` or `README.md` in a Phase 12 commit.

### Pitfall 8: Weakening Opportunity or existing THRESHOLDS to pass remap
**What goes wrong:** Moving too much of federal-bca; Opportunity drops toward the old baseline of 1.
**Why it happens:** "also decision analysis" notes exist on more than the two locked chapters.
**How to avoid:** Move only the three locked files. Opportunity 10→8 still ≫ 2.
**Warning signs:** Opportunity count < 8 after regen, or THRESHOLDS Opportunity raised/lowered.
</common_pitfalls>

<code_examples>
## Code Examples

### Live map envelope (do not change schema)
```json
{
  "schema_version": 2,
  "map_version": "1.18.0",
  "generated_on": "2026-08-17",
  "clusters": []
}
```
Source: `docs/capability-pack-map.json:2-4`.

### Existing import style to copy for MAP-19-04
```python
# Source: tooling/check_release.py:119-126
sys.path.insert(0, str(ROOT / "tooling"))
try:
    import validate_pack  # type: ignore
    packs = sorted(p for p in (ROOT / "packs").iterdir() if p.is_dir() and p not in signpost_dirs)
    for pack in packs:
        perrs = validate_pack.check_pack(pack)
        for e in perrs:
            fail(errs, f"[pack:{pack.name}] {e}")
```

Recommended map-gate block (illustrative — planner writes the exact insertion point):

```python
try:
    import check_capability_map  # type: ignore
    rc = check_capability_map.main()
    if rc != 0:
        fail(errs, "[map] check_capability_map.py failed (see output above)")
except Exception as e:
    fail(errs, f"[map] check_capability_map failed to run: {e}")
```

`main()` already prints `FAIL: N issue(s)` / `PASS: capability map OK` and returns 0/1. [VERIFIED: `tooling/check_capability_map.py:238-245`]

### MAP-19-02 verify print (AND-1-pack half)
```python
# one-shot; not a new committed tool
import json
from collections import defaultdict
data = json.load(open("docs/capability-pack-map.json", encoding="utf-8"))
want = [
    "Decision Analysis & Trade Studies",
    "Validation",
    "Integration",
    "Interface Management & ICIDs",
    "Operations, Maintenance & Disposal",
]
by = {c["name"]: c for c in data["clusters"]}
for name in want:
    ch = by[name]["chapters"]
    packs = {e["pack"] for e in ch}
    bad = len(ch) < 4 and len(packs) == 1
    print(f"{name}: {len(ch)} entries / {len(packs)} packs  floor_fail={bad}")
```

### HYG-01 pin
```gitattributes
*.md text eol=lf
```
</code_examples>

<sota_updates>
## State of the Art (this repo, 2026-08-17)

| Old approach (v1.18 / Phase 8–9) | Phase 12 approach | When changed | Impact |
|----------------------------------|-------------------|--------------|--------|
| Map gate standalone; both commands run by hand at release | `check_release` invokes map gate | MAP-19-04 (this phase) | One local command proves freshness |
| v1.18 SC-2 thin floors (Training ≥1, C3/C5/C15 ≥2–3) | Extra listed-primary floor (no `<4 AND 1 pack`) | SEED-001 / MAP-19-02 | DA cannot ship at 2/2 |
| 502 figure in ROLE-AGENTS-REQUIREMENTS-V2 | CONTRACT notes live 628+; 502 is residue | MAP-19-05 | Pack-side only; se-agents still has its own refresh |
| Cyber 69 / DE 25 unbound | Same; document, do not bind | SEED-001 | Binding is consumer-side |
| CHANGELOG BOM + no `.gitattributes` | Strip + pin | HYG-01 | Checkout EOL hygiene |

**Deprecated/outdated:**
- CONTRACT line "The gate is standalone (not wired into `check_release.py` in this milestone)" — update when MAP-19-04 lands.
- ROLE-AGENTS-REQUIREMENTS-V2 "502 chapter references" [VERIFIED: `docs/ROLE-AGENTS-REQUIREMENTS-V2.md:7,92`] — **not** a Phase 12 edit target (historical draft; MAP-19-05 lives in CONTRACT.md).
</sota_updates>

<open_questions>
## Open Questions

1. **Should Integration be forced to "move" despite 4/4 and IO-05 DEFERRED?**
   - What we know: REQUIREMENTS lists it among primaries that must move; there is no cleared Integration source.
   - What's unclear: whether verify will demand a count delta.
   - Recommendation: encode THRESHOLDS Integration ≥ 4; record "floor held; AAF still deferred; no raid." Do not invent chapters.

2. **`map_version` 1.18.0 vs 1.19.0 during Phase 12?**
   - What we know: CONTRACT says map_version tracks the release that regenerated the map; release is Phase 13.
   - What's unclear: a purist reading wants 1.19.0 the moment the JSON changes.
   - Recommendation: keep `"1.18.0"` + fresh `generated_on`. Phase 13 updates `map_version` with plugin/CHANGELOG/RELEASE-INFO.

3. **HYG-03 in-tree vs record-only?**
   - What we know: ROADMAP SC-4 allows either; sibling EXCLUDED dict is still missing the three keys.
   - What's unclear: whether the sibling repo is writable in the execute session.
   - Recommendation: try a sibling commit/PR; if not, record the external PR/issue and close.

4. **ch11 T&E/V&V Checklist → Validation or Test & Evaluation?**
   - What we know: chapter is an integration checklist between T&E and V&V, not Validation fundamentals (that's ch08).
   - What's unclear: MAP-19-02 "Validation must move" is already satisfied if ch12+ch13 go to Validation (5→7).
   - Recommendation: classify by reading the chapter (T&E likely); do not force-fit to Validation to show a bigger delta.
</open_questions>

<recommended_plan_shape>
## Recommended plan shape (do NOT write PLAN.md here)

Two execute plans. Regen before wire. One scoped commit per concern.

**Plan 12-01 — Map regen + remap + floor + CONTRACT (MAP-19-01/02/03/05)**

1. Agent-classify the 16 unmapped chapters (hints above). Omit support files for the two new packs unless classification proves single-cluster.
2. Apply the three-row MAP-19-03 **move** (delete old cluster membership).
3. Keep `schema_version` 2 and `map_version` `"1.18.0"`; set `generated_on` to execution day. Sync `docs/capability-pack-map.md` summary table + a v1.19 changelog bullet (new slugs + remap + leftover RPG).
4. Add MAP-19-02 name-keyed THRESHOLDS (≥4) for Decision Analysis, Validation, Integration, Interfaces (raise 3→4), Ops/Maint. Do not weaken existing floors.
5. One paragraph in `docs/capability-map-CONTRACT.md`: live snapshot 628+ (post-regen 644 if 16 adds / 0 support); 502 is residue; Cybersecurity (69/10) + Digital Engineering (25/4) remain unbound — binding is se-agents-side.
6. `python tooling/check_capability_map.py` PASS. One-shot print: none of the five primaries is `<4 AND 1 pack`. DA = 5 entries / 4 packs.

Out of this plan: `check_release` wire, HYG-*, version bump, catalog/README.

**Plan 12-02 — Gate wire + hygiene (MAP-19-04, HYG-01..04)**

1. Import `check_capability_map.main()` from `check_release.py` (Pattern 4). Update CONTRACT §4 "standalone" sentence and the map-gate docstring.
2. HYG-01: strip CHANGELOG BOM; LF; add `.gitattributes` `*.md text eol=lf`.
3. HYG-02: four SKILL.md nits; `validate_pack` on those slugs.
4. HYG-04: federal-bca PACK.yaml "(c)" wording.
5. HYG-03: sibling EXCLUDED keys **or** SUMMARY record of external PR/issue (afotec / dod-dag / cmu-sei).
6. `python tooling/check_release.py` PASS (now includes map). `python tooling/check_capability_map.py` still PASS.

**Must-NOT across both plans:** generator script; version/tag/CHANGELOG `[1.19.0]`; catalog `dod-vva-rpg.chapters` bump; README new-slug rows; AAF/CBA/DoDM/stakeholder packs; Cyber/DE bindings; CI exec of repo Python; copying remap rows.

Analog: `.planning/phases/8-agent-enablement-surface/8-01-PLAN.md` (agent classify + gate GREEN + CONTRACT) plus a small hygiene plan — not Phase 11 pack-build.
</recommended_plan_shape>

<validation_architecture>
## Validation Architecture

Phase 12 is docs + two stdlib gates. No runtime, no UI.

| Layer | What it proves | Command / check |
|---|---|---|
| Map envelope | schema 2, semver map_version, ISO generated_on | `check_capability_map.py` envelope block |
| Staleness | every chapter-bearing pack + every chapter file ↔ map | same gate; expect 0 on_disk_only / 0 map_only |
| Uniqueness | no duplicated (pack, chapter) after remap | same gate |
| Legacy thin floors | Training ≥1; C3 ≥3; C5 ≥3 (raise to 4); C15 ≥2 | THRESHOLDS |
| MAP-19-02 | listed primaries ≥4 entries; none `<4 AND 1 pack` | new THRESHOLDS + one-shot print |
| MAP-19-03 | DA 5/4; Opportunity still has ch01–ch03/ch05; ch08 Validation; ch10 Risk | python membership query |
| MAP-19-04 | `check_release` invokes map gate | `rg check_capability_map tooling/check_release.py`; turning map RED must fail release |
| MAP-19-05 | CONTRACT paragraph present | grep `628` + `502` + `Cybersecurity` + `Digital Engineering` in CONTRACT |
| HYG-01 | no BOM; `.gitattributes` pin | `python -c` first-bytes; `test -f .gitattributes` |
| HYG-02 | four nits gone | file greps + `validate_pack` ×4 |
| HYG-03 | sibling keys or recorded PR | sibling file grep **or** SUMMARY URL |
| HYG-04 | wording no longer claims zero `(c)` literals | PACK.yaml grep |
| Phase 13 fence | plugin/CHANGELOG/RELEASE-INFO still 1.18.0; no `v1.19*` tag | version trio + `git tag` |
| Link policy | still 0 `http` in SOURCE-VETTING | `grep -c http docs/SOURCE-VETTING.md` → 0 |

Human judgment (spot-check, not a silent skip): for each new pack, re-read SKILL.md When-to-use vs assigned clusters (Phase 8 protocol). Remap chapters are **not** judgment — they are locked.
</validation_architecture>

<sources>
## Sources

### Primary (HIGH confidence)
- `.planning/REQUIREMENTS.md:29-47` — MAP-19 + HYG + REL-19 split
- `.planning/ROADMAP.md:60-82` — Phase 12/13 success criteria
- `.planning/STATE.md:31-60` — current phase 12; Phase 11 deviations
- `.planning/seeds/SEED-001-agent-io-pack-depth.md` — floor definition; 502 residue; Cyber/DE unbound
- `11-02-SUMMARY.md:163-171` — AUTHORITATIVE remap table
- `11-GAP_ANALYSIS.md:107-114` + `11-INTEGRATION_CHECK.md` — Phase 12/13 routing; map RED start state
- Live `docs/capability-pack-map.json` + `python tooling/check_capability_map.py` (FAIL 19) + `python tooling/check_release.py` (PASS)
- `tooling/check_capability_map.py` + `tooling/check_release.py`
- `docs/capability-map-CONTRACT.md`
- `8-RESEARCH.md` §2 regen approach; `8-01-SUMMARY.md` Phase 8 analog
- `7-CODE_REVIEW.md:83-88` + live SKILL.md lines — HYG-02
- `7-GAP_ANALYSIS.md:41,65-66` — HYG-04 / R6
- `6-GAP_ANALYSIS.md:52-61` + sibling `vet_source.py:41-56` — HYG-03
- `packs/federal-bca/PACK.yaml:19-20` — HYG-04 locus
- CHANGELOG first bytes `ef bb bf`; no `.gitattributes`

### Secondary (MEDIUM confidence)
- 11-RESEARCH IO-03/IO-04 cluster vocab tables — classification *hints* only
- CONTRACT `map_version` tracks release — interpreted as "keep 1.18.0 until Phase 13"

### Tertiary (LOW confidence)
- Post-regen total 644 assumes 16 chapter adds and 0 new support-file rows
</sources>

<metadata>
## Metadata

**Research scope:**
- Core technology: committed JSON map + two stdlib Python gates
- Ecosystem: Phase 8 analog, Phase 11 remap handoff, sibling vet_source, se-agents contract
- Patterns: agent regen, move-not-copy remap, import-not-subprocess wire, record-as-PR hygiene
- Pitfalls: wire-before-green, version steal, Integration pack invention, Opportunity collapse

**Confidence breakdown:**
- Standard stack: HIGH — live files and Phase 8 analog
- Architecture: HIGH — regen vs apply vs wire vs Phase 13 fence
- Pitfalls: HIGH — named from Phase 8/9/11 reviews
- Classification hints: MEDIUM — judgment pass remains

**Research date:** 2026-08-17
**Valid until:** 2026-09-16 (or until map JSON is regenerated)
</metadata>

---

*Phase: 12-map-regen-hygiene-gate-wiring*
*Research completed: 2026-08-17*
*Ready for planning: yes*
