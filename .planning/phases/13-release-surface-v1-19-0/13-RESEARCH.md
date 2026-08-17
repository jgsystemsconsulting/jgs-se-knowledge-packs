# Phase 13: Release surface + v1.19.0 — Research

**Researched:** 2026-08-17
**Domain:** Version-surface bump, REL-19 leftovers, dual-gate, annotated tag + GitHub Release
**Confidence:** HIGH on the 11 analog surfaces, leftovers, tag/push procedure, `map_version` decision, and what not to redo. MEDIUM only on the exact CHANGELOG paragraph wording (must be competency-led; draft below is a planner starting point, not locked prose).

<user_constraints>
## User Constraints (from STATE / REQUIREMENTS / ROADMAP / Phase 11–12; no CONTEXT.md)

**CRITICAL:** Discuss was skipped. There is no `13-CONTEXT.md`. Locked decisions below are taken from REQUIREMENTS REL-19, ROADMAP Phase 13, STATE.md, and Phase 11/12 handoffs — these MUST be honored.

### Locked Decisions

- **REL-19-01 + REL-19-02 are this phase.** Catalog/docs/manifests synchronized; both gates PASS at the updated catalog/directory basis; `v1.19.0` tagged + GitHub Release; CHANGELOG lists IO-unlocks **by competency**, not just pack slugs. [VERIFIED: `.planning/REQUIREMENTS.md:46-47` — "REL-19-01: Full registration of any new packs; both gates PASS" / "REL-19-02: v1.19.0 tagged + GitHub Release"; `.planning/ROADMAP.md:74-82`]
- **Phase 9 analog is AUTHORITATIVE** for sequence, surface list, tag style, and push. Structure reuses Phase 5 via Phase 9. One execute plan. [VERIFIED: `.planning/phases/9-release-surface-v1-18-0/9-01-PLAN.md:54-55` — "Structure reuses the proven Phase 5 template"; `9-01-SUMMARY.md:58` — "Release surface phase: bump → CHANGELOG → doc carry-forwards → dual-gate → release commit/tag/push/gh → .planning records"]
- **Tag + GitHub Release ARE the phase requirement.** Document exact commands. Phase 9 analog **did** push (`git push origin main --follow-tags`). Do not invent a no-push variant. [VERIFIED: `9-01-PLAN.md:132` — `git push origin main --follow-tags`; `9-01-SUMMARY.md:182-190` — origin tag + `gh release view` succeeded]
- **Branch protection stays admin-bypass.** Do not "fix" protection as part of REL-19. [VERIFIED: `.planning/STATE.md:61` — "Branch protection left at admin-bypass (2026-08-16)"; `.planning/REQUIREMENTS.md:58` — "Branch-protection enforcement | User opted to keep admin bypass"]
- **Live map 644 / DA 5/4 / floors / CONTRACT §6 / MAP-19-04 wire are frozen inputs.** Do not re-classify the 16 chapters or reverse the MOVE. [VERIFIED: `.planning/phases/12-map-regen-hygiene-gate-wiring/12-INTEGRATION_CHECK.md:33-36`; `12-GAP_ANALYSIS.md:118`]
- **Do not build** Army CBA / AAF / stakeholder / `dodm-5000-102` / SP-7084 / IS-300. IO-05/06 DEFERRED; IO-07 ACCEPT. [VERIFIED: `12-INTEGRATION_CHECK.md:40`; `.planning/REQUIREMENTS.md:25-27`]
- **Do not add a CI repo-Python map step.** `.github/workflows/validate.yml` never executes checked-out repository code. [VERIFIED: `12-INTEGRATION_CHECK.md:111`; `.github/workflows/validate.yml:4-5`]
- Stay on `main`. No branches / worktrees.

### Claude's Discretion

- **`map_version` 1.18.0 → 1.19.0:** yes — bump with the rest of the release surfaces (see §6). Phase 12 kept `"1.18.0"` on purpose so Phase 13 ships a consistent trio + envelope.
- **CHANGELOG shape:** competency-led IO narrative first (REL-19-02 SC-2), then pack one-liners with live PACK.yaml chapter counts. No em dashes, no URLs.
- **Optional REQUIREMENTS annotation refresh** for IO-01 ("Live count leave-2 is Phase 12" is stale; live DA is 5/4) when ticking REL boxes. Not a blocker.

### Deferred Ideas (OUT OF SCOPE)

- Rebuilding or re-vetting packs (Phase 10/11 done)
- Re-running map regen / remap / THRESHOLDS / CONTRACT §6 (Phase 12 done)
- FUT-05 deterministic map generator
- Committed overlap checker (7-CODE-REVIEW IN-02)
- se-agents consumer refresh (502 docs, `thin: 3`, 20-ref cap, Cyber/DE *bindings*)
- Branch-protection enforcement
- Building AAF / Army CBA / stakeholder / DoDM / SP-7084 / IS-300
- Vendoring `vet_source.py`; waiting on sibling PR #2 merge
</user_constraints>

<architectural_responsibility_map>
## Architectural Responsibility Map

Single-tier content library — no Browser/Client, API, or Database runtime. Phase 13 is version/docs/release metadata plus the public tag act.

| Capability | Primary Tier | Secondary Tier | Rationale |
|------------|-------------|----------------|-----------|
| Version single-source | `.claude-plugin/plugin.json` + `CHANGELOG.md` + `RELEASE-INFO.txt` | cursor plugin, README, index, packs.html, website YAMLs | Gate §4 reads the trio only; analog still bumps all 11 display surfaces |
| Catalog honesty | `catalog.json` `dod-vva-rpg.chapters` | README live-pack table | REL-19-01 leftover; gate does not assert the integer |
| Generated pack index page | `RELEASE-INFO.txt` then `tooling/gen_packs_page.py` | `docs/packs.html` | Never hand-edit packs.html |
| Map envelope version | `docs/capability-pack-map.json` `map_version` | CONTRACT example envelope | Tracks the *release* that last regenerated the map |
| Dual gate | `tooling/check_release.py` | `tooling/check_capability_map.py` (already imported) | REL-19-01; do not unwire |
| Public release act | annotated tag `v1.19.0` + `gh release create` | origin push | REL-19-02 |
| Post-tag records | `.planning/STATE.md` / `MILESTONES.md` / `ROADMAP.md` | REQUIREMENTS REL ticks | Separate commit after tag |
</architectural_responsibility_map>

<research_summary>
## Summary

Phase 13 is the **Phase 9 analog** for v1.19.0: bump every version surface, land a competency-led CHANGELOG, close the two catalog/README leftovers Phase 11/12 deliberately left, re-run both gates (map is now inside `check_release`), then one release commit + annotated tag + push + GitHub Release.

Live start state is already mechanically green at the **63 catalog / 65 dirs** basis. `check_capability_map.py` PASS (schema 2, `map_version` `"1.18.0"`, 644 entries). `check_release.py` PASS (imports the map gate). Thin-register already put `nasa-std-8719-14` and `is-gps-200n` on catalog / SKILLS / NOTICE / cursor / packs.html. What is *not* done: version trio still **1.18.0**, no `## [1.19.0]`, no `v1.19*` tag, `catalog.json` `dod-vva-rpg.chapters` still **10** vs disk **13**, README live-pack table still ends at `mil-std-40051` and still says VV&A "10 chapters".

**Primary recommendation:** ONE execute plan (`13-01`), six tasks cloned from `9-01-PLAN.md`: bump 11 surfaces + `map_version` → CHANGELOG `[1.19.0]` competency narrative → catalog/README leftovers → dual-gate + residual-version sweep → release commit / annotated tag / push / `gh release create` → post-tag STATE/MILESTONES/ROADMAP. Do not write PLAN.md here.
</research_summary>

<standard_stack>
## Standard Stack

Copy Phase 9. No new library.

### Core

| Artifact | Version / location | Purpose | Why standard |
|---------|--------------------|---------|--------------|
| Gate trio | plugin `1.18.0` / CHANGELOG `## [1.18.0]` / RELEASE-INFO `1.18.0` | `check_release` §4 single-source | [VERIFIED: `tooling/check_release.py:103-117`] |
| 11 display surfaces | Phase 9 Task 1 file list | Consumer-facing REV strings | [VERIFIED: `9-01-PLAN.md:96-100`] |
| `tooling/gen_packs_page.py` | reads RELEASE-INFO `version()` | Regenerates `docs/packs.html` | Gate §5c fails on drift [VERIFIED: `tooling/check_release.py:144-157`] |
| `tooling/check_release.py` | now includes map §5d | Local ship gate | [VERIFIED: `tooling/check_release.py:215-222`] |
| `tooling/check_capability_map.py` | schema 2 / 644 / floors | Map freshness | [VERIFIED: live 2026-08-17 `PASS … TOTAL: 644`] |
| `gh` CLI | authenticated (`jgsystemsconsulting`) | GitHub Release | [VERIFIED: `gh auth status` + `gh release view v1.18.0`] |
| Annotated git tag | colon-style one-liner | Tamper-evident public pin | [VERIFIED: `git tag -l -n3 v1.18.0` → `v1.18.0: 7 gap-driven…`] |

### Supporting

| Artifact | Purpose | When to use |
|---------|---------|-------------|
| `9-01-PLAN.md` / `9-01-SUMMARY.md` | AUTHORITATIVE analog | Task order, commit/tag/notes style, Windows notes-file path |
| `5-RESEARCH.md` | First-principles surface inventory | Confirms the 11-count |
| `11-02-SUMMARY.md` / `11-INTEGRATION_CHECK.md` | Thin-register + leftover notes | Do not re-register SKILLS/NOTICE/cursor |
| `12-INTEGRATION_CHECK.md` / `12-GAP_ANALYSIS.md` P13-* | Frozen map + leftover table | Do not re-classify |
| `catalog.json` / `README.md` | REL-19-01 leftovers | Chapter integer + two missing rows |

### Alternatives Considered

| Instead of | Could Use | Tradeoff |
|------------|-----------|----------|
| Two plans (bump vs tag) | One plan like 9-01 | Split would leave an untagged 1.19.0 commit on main; analog forbids that |
| Skip `git push` | Tag local-only | REL-19-02 and Phase 9 analog require origin tag + GitHub Release |
| Leave `map_version` at 1.18.0 | Bump to 1.19.0 | CONTRACT says it tracks the *release* that regenerated the map; Phase 12 deferred the bump to this phase |
| Hand-edit `docs/packs.html` | `gen_packs_page.py` after RELEASE-INFO | Gate §5c fails on drift |
| Add CI map step | Keep local/trusted `check_release` | `validate.yml` must not exec repo Python |

**Installation:** none. On Windows/Git Bash use `python`. Write `gh --notes-file` under the phase dir, not `/tmp`.
</standard_stack>

<architecture_patterns>
## Architecture Patterns

### System Architecture Diagram

```text
  Phase 11/12 already landed
    packs/nasa-std-8719-14 (7) + packs/is-gps-200n (6)
    dod-vva-rpg disk 13 / PACK.yaml 13 / catalog 10   <-- leftover
    SKILLS / NOTICE / cursor / packs.html thin-registered
    map 644 GREEN; check_release imports map
    version trio + map_version still 1.18.0
           |
           v
  13-01 Task 1  bump 11 surfaces 1.18.0 → 1.19.0
                RELEASE-INFO first → gen_packs_page.py
                also map_version + CONTRACT example → 1.19.0
           |
           v
  13-01 Task 2  CHANGELOG ## [1.19.0] competency-led IO narrative
           |
           v
  13-01 Task 3  catalog dod-vva-rpg.chapters 10→13
                README rows nasa-std-8719-14 + is-gps-200n
                README dod-vva-rpg "10 chapters" → 13
           |
           v
  13-01 Task 4  both gates PASS; residual 1.18.0 whitelist-only
           |
           v
  13-01 Task 5  one release commit (explicit paths)
                git tag -a v1.19.0 -m "v1.19.0: …"
                git push origin main --follow-tags
                gh release create v1.19.0 --title "…" --notes-file <phase-dir tmp>
           |
           v
  13-01 Task 6  STATE / MILESTONES / ROADMAP (separate .planning commit)
```

### Pattern 1: Eleven version surfaces (Phase 9 analog) + map_version

Phase 9 Task 1 listed **11 surfaces** as string occurrences across 8 files (README ×3, index.html ×2, six singles). CHANGELOG heading is Task 2 (gate trio member). [VERIFIED: `9-01-PLAN.md:96-100`; `5-RESEARCH.md:30-43`]

Live `1.18.0` hits outside `.planning` / `.git` / `sources` (2026-08-17):

| # | File | Line(s) | Current | Action |
|---|---|---|---|---|
| 1 | `.claude-plugin/plugin.json` | 4 | `"version": "1.18.0"` | Bump (GATE) |
| 2 | `CHANGELOG.md` | 12 | `## [1.18.0]: 2026-08-17` | Insert `[1.19.0]` **above** (GATE; Task 2) |
| 3 | `RELEASE-INFO.txt` | 3–5 | `Version: 1.18.0` / `Tag: v1.18.0` / `Staged: 2026-08-17T00:59:27Z` | Bump Version + Tag; refresh Staged to execution timestamp (GATE on Version) |
| 4 | `.cursor-plugin/plugin.json` | 5 | `"version": "1.18.0"` | Bump |
| 5 | `README.md` | 10 | badge `version-1.18.0-green` + alt | Bump |
| 6 | `README.md` | 58 | `(version 1.18.0)` | Bump |
| 7 | `README.md` | 224 | `Current: 1.18.0.` | Bump |
| 8 | `docs/index.html` | 110 | `REV: <span>1.18.0</span>` | Bump |
| 9 | `docs/index.html` | 226 | `REV: <span style="color:var(--text)">1.18.0</span>` | Bump |
| 10 | `docs/packs.html` | 86 | `REV: <span>1.18.0</span>` | **Regenerate**, never hand-edit |
| 11 | `docs/products/website/catalog.yaml` | 13 | `version: "1.18.0"` | Bump |
| — | `docs/products/website/01-jgs-se-knowledge-packs.yaml` | 15 | `version: "1.18.0"` | Bump (11th display file; Phase 9 counted README×3 + index×2 + these) |

Phase 9 counted 11 as: plugin, cursor plugin, RELEASE-INFO, README×3, index×2, packs.html, two website YAMLs. Same set. CHANGELOG is the 12th string and a gate authority.

**Order (locked by analog):** edit `RELEASE-INFO.txt` first, run `python tooling/gen_packs_page.py`, then hand-edit the rest. [VERIFIED: `9-01-PLAN.md:98`; `9-01-SUMMARY.md:28`]

`install.py` / `install.sh` / `install.ps1` / `.claude-plugin/marketplace.json`: still no version field to bump (Phase 5 inventory; no new evidence they gained one).

### Pattern 2: Historical 1.18.0 / 1.17.0 whitelist (do not "clean")

After the bump, residual `1.18.0` outside `.planning`/`.git`/`sources` must be **history**, not live REV:

- `CHANGELOG.md` `## [1.18.0]` region (entire shipped entry)
- `docs/capability-pack-map.md:16` — `Changelog (v1.18.0): added dod-vva-rpg…` [VERIFIED]
- `docs/SOURCE-VETTING.md:116` — `### Vetted candidates (v1.18.0)` [VERIFIED]
- CONTRACT example/`e.g.` lines: update the **live example envelope** `map_version` if the JSON is bumped (line 15 is the current-shape example). Leave line 54 historical `1.17.0` alone. Line 35 "`e.g. "1.18.0"`" may stay as an example or be refreshed to `1.19.0` — planner choice; do not treat it as a 12th gate surface.

Historical `1.17.0` whitelist (must survive, same as Phase 9):

- `docs/capability-map-CONTRACT.md:54` — pre-envelope (v1) map corresponds to release `1.17.0`
- `docs/capability-pack-map.md:17` — Changelog (v1.17.0)
- `docs/SOURCE-VETTING.md:94`, `:182`, `:187` — v1.17.0 candidate / exclusion history

[VERIFIED: live grep 2026-08-17; `9-01-PLAN.md:79`]

### Pattern 3: REL-19-01 leftovers (catalog + README only)

Thin-register already done in 11-02. Do **not** re-touch SKILLS/NOTICE/cursor skill paths / packs.html rows except via regeneration after RELEASE-INFO.

| Surface | Live | Need |
|---------|------|------|
| `catalog.json` pack count | **63** (includes both GO slugs) | Keep 63; no new slugs |
| `catalog.json` `nasa-std-8719-14.chapters` | **7** | already correct |
| `catalog.json` `is-gps-200n.chapters` | **6** | already correct |
| `catalog.json` `dod-vva-rpg.chapters` | **10** | **13** [VERIFIED: `catalog.json:612`; disk 13 files; `packs/dod-vva-rpg/PACK.yaml:13` `chapters: 13`] |
| `SKILLS.md` header | `63 packs (+2 signposts)` + both slugs | already done [VERIFIED: `SKILLS.md:9,74-75`] |
| `NOTICE` | both pack attributions | already done [VERIFIED: `NOTICE:704,713`] |
| `.cursor-plugin/plugin.json` skills | **64** (includes both; excludes `sebok`) | already done [VERIFIED: `11-02-SUMMARY.md:138`; cursor version still 1.18.0] |
| `docs/packs.html` rows | both slugs present; REV 1.18.0 | regenerate only |
| `README.md` badge | `packs-63` | already correct [VERIFIED: `README.md:11`] |
| `README.md` live-pack table | ends at `mil-std-40051`; `dod-vva-rpg` "10 chapters"; **no** 8719/200N rows | add two live rows; RPG 10→13 [VERIFIED: `README.md:164,170`; `11-INTEGRATION_CHECK.md:91`; `12-INTEGRATION_CHECK.md:105`] |
| dirs | **65** (`dirs−catalog` = `{omg-signpost, se-standards-signpost}`) | unchanged |

`check_release` does **not** assert `catalog.json` chapter integers or README table rows. REL-19-01 still owns them as "full registration" honesty. [VERIFIED: `11-INTEGRATION_CHECK.md:91` — "Gate does not require those rows (`check_release` PASS). Phase 13 / REL-19-01 owns full surface sync."]

Suggested README rows (match table style at `README.md:164-170`; titles from PACK.yaml / SKILLS):

```markdown
| `nasa-std-8719-14` | NASA-STD-8719.14C: Process for Limiting Orbital Debris (Approved 2021-11-05) | Public domain (US gov) | 🟢 1 | ✅ live (7 chapters) |
| `is-gps-200n` | IS-GPS-200N: NAVSTAR GPS Space Segment / Navigation User Segment Interfaces | Public domain (US gov) | 🟢 1 | ✅ live (6 chapters) |
```

Place with the other live rows (after `mil-std-40051`, before `mit-ocw-se` planned). Also change line 164 `(10 chapters)` → `(13 chapters)`.

### Pattern 4: CHANGELOG `[1.19.0]` — competency, not just slugs

ROADMAP SC-2: "CHANGELOG lists IO-unlocks by competency, not just pack slugs." [VERIFIED: `.planning/ROADMAP.md:82`]

House format (from `[1.18.0]`): `## [x.y.z]: YYYY-MM-DD`, `### Added` / `### Fixed` / `### Changed`, compact `**slug** (N ch):` one-liners, **no em dashes**, **no URLs**, "Catalogue now N packs (+2 signposts)". [VERIFIED: `CHANGELOG.md:12-78`; `9-01-PLAN.md:106`]

v1.19 is **not** "7 new packs". It is two new packs + one extend-in-place + one remap + three honest non-builds. Leading with slugs alone would fail SC-2.

Draft shape (planner may tighten; do not copy em dashes; re-read PACK.yaml `chapters:` immediately before writing):

```markdown
## [1.19.0]: <execution date>

Agent IO Depth (SEED-001): competency primaries fattened so se-agents can
execute IOs. Two new Tier-1 packs, leftover VV&A chapters, and a Decision
Analysis remap. Integration and Logistics stay deferred (AAF not vetted).
Stakeholder Engagement accepted with no invented pack.

### Added

- **IO-03 Ops/Maintenance/Disposal** (`nasa-std-8719-14`, 7 ch): NASA-STD-8719.14C
  Process for Limiting Orbital Debris — ODAR/EOMP assessment, normal-ops debris
  limits, passivation/collision, postmission disposal, reentry casualty.
  Tier 1 (US-gov public domain).
- **IO-04 Interface Management** (`is-gps-200n`, 6 ch): IS-GPS-200 Rev N ICD
  exemplar complementary to `faa-std-025` — IRN/CCB change control, definition vs
  identification, criteria pattern, NAV payload families, time/definition hygiene.
  Exemplar only; Apps II-IV not transcribed. Tier 1 (US-gov public domain).
- **IO-02 Validation depth** (chapters, not a pack): leftover RPG special topics
  added to existing `dod-vva-rpg` (10 -> 13 ch) — T&E/V&V Checklist, Developing
  the Referent, Conceptual Model Development and Validation. DoDM 5000.102 still
  deferred; no `dodm-5000-102` pack.
- Capability-pack map regenerated to 644 entries / 63 mapped packs (schema 2);
  MAP-19-02 floors >=4 on Decision Analysis, Validation, Integration, Interfaces,
  Ops/Maint; `check_release.py` now invokes `check_capability_map.main()`.

Catalogue now 63 packs (+2 signposts).

### Changed

- **IO-01 Decision Analysis remap:** `federal-bca` ch04 + ch06 and `dod-vva-rpg`
  ch06 MOVEd into Decision Analysis & Trade Studies (cluster now 5 entries / 4
  packs). No Army CBA pack (FUT-04 still deferred).
- Registered `nasa-std-8719-14` and `is-gps-200n` on every registered surface
  (catalog.json, SKILLS.md, docs/packs.html, NOTICE, README, Cursor manifest).
  `dod-vva-rpg` catalog/README chapter count 10 -> 13.

### Fixed

(none required unless a wording leftover is closed here)

### Deferred / accepted (not built)

- **IO-05 Integration** DEFERRED — AAF Software pathway still NOT yet vetted.
- **IO-06 Logistics diversity** DEFERRED — AAF Product Support still NOT yet vetted.
- **IO-07 Stakeholder Engagement** ACCEPT — no clean Tier-1/2 candidate; no invented pack.
```

Hard constraints (copy Phase 9):

- Chapter counts = live `packs/<slug>/PACK.yaml` `chapters:` — **7 / 6 / 13**, never a uniform 8. [VERIFIED: `nasa-std-8719-14` `:13` = 7; `is-gps-200n` `:13` = 6; `dod-vva-rpg` `:13` = 13]
- Zero em-dash characters; zero `http` in the new entry (link-policy scans CHANGELOG).
- Do **not** restate the `.planning/` CI skip (already in 1.17.0 Changed).
- Do **not** claim catalog grew 61→63 *as if it happened at tag time only* without noting thin-register already listed the slugs — "Catalogue now 63" is the honest now-count (1.18.0 entry correctly said 61).
- Keep publisher names bare. No source-host links.

### Pattern 5: Dual gates at the updated basis

Commands (Windows Git Bash / `python`):

```bash
python tooling/gen_packs_page.py          # after RELEASE-INFO; then empty git diff on packs.html
python tooling/check_capability_map.py    # expect PASS; TOTAL 644; map_version 1.19.0 after bump
python tooling/check_release.py           # expect RELEASE CHECK: PASS (prints map cluster block first)
python -c "import json;print(len(json.load(open('catalog.json'))['packs']))"  # 63
ls packs | wc -l                          # 65
python tooling/validate_pack.py packs/nasa-std-8719-14
python tooling/validate_pack.py packs/is-gps-200n
python tooling/validate_pack.py packs/dod-vva-rpg
```

`check_release` §4 will FAIL if plugin / CHANGELOG top / RELEASE-INFO disagree. §5d will FAIL if `map_version` is malformed or the map is stale. `map_version` is **not** compared to the trio — only N.N.N shape + staleness/floors. [VERIFIED: `tooling/check_capability_map.py:74-81`; `tooling/check_release.py:103-117,215-222`]

Re-run `check_release` immediately before the release commit (OneDrive sync-lag; Phase 5/9). [VERIFIED: `9-01-PLAN.md:123`; `5-RESEARCH.md:209-211`]

Do not add `.github/workflows/validate.yml` map execution.

### Pattern 6: Tag + GitHub Release — what Phase 9 actually ran

Phase 9 Task 5 (executed, not theoretical) [VERIFIED: `9-01-PLAN.md:129-135`; `9-01-SUMMARY.md:127-194`]:

1. `git status --short` — STOP on surprise untracked (do not stage `master_flow_state.json`, `.edge-coverage.json`, or this research file into the release commit).
2. Stage **explicit paths only**. Never `git add -A` / `git add docs/` / `git add .`.
3. Single release commit is the **last content commit** on `main`. Intermediate task commits were soft-reset into one `release(v1.18.0): …` commit (`d19be1a`). Repeat that consolidation if GSD per-task commits would otherwise precede the tag. [VERIFIED: `9-01-SUMMARY.md:221-226`]
4. Annotated tag, **colon** style matching live tags (not the older em-dash tag message from 5-RESEARCH draft):

```bash
git tag -a v1.19.0 -m "v1.19.0: 2 IO-unlock packs + VV&A chapters + DA remap (63 +2 signposts)"
```

Live precedents [VERIFIED: `git tag -l -n3`]:

- `v1.17.0: 8 Tier-1 public-domain packs (54 +2 signposts)`
- `v1.18.0: 7 gap-driven Tier-1 packs (61 +2 signposts), capability map v2`

5. **Push — Phase 9 did this:**

```bash
git push origin main --follow-tags
```

Admin-bypass is still in force, so the push is expected to succeed without a PR. [VERIFIED: `.planning/STATE.md:61`]

6. GitHub Release. Title uses an **em dash** (public title only; CHANGELOG body stays em-dash-free). Body = CHANGELOG `[1.19.0]` entry body.

```bash
# Windows: do NOT write notes to /tmp (Phase 9 first gh attempt failed)
# Write then delete:
#   .planning/phases/13-release-surface-v1-19-0/_v1.19.0-notes.tmp.md
gh release create v1.19.0 \
  --title "v1.19.0 — Agent IO Depth (2 packs + VV&A chapters + DA remap)" \
  --notes-file .planning/phases/13-release-surface-v1-19-0/_v1.19.0-notes.tmp.md
```

Live v1.18.0 title: `v1.18.0 — 7 gap-driven Tier-1 packs + capability map v2`. [VERIFIED: `gh release view v1.18.0 --json name,tagName,url`]

7. REL-19-02 is **not** done until both succeed:

```bash
git ls-remote --tags origin | grep v1.19.0
gh release view v1.19.0 --json name,tagName,url
```

`gh` is authenticated as `jgsystemsconsulting` with `repo` scope (2026-08-17).

Suggested release-commit subject (analog style):

```
release(v1.19.0): Agent IO Depth — 2 packs + VV&A chapters + DA remap (63 +2 signposts)
```

### Pattern 7: Post-release records (not in the release commit)

After the tag exists, separate `.planning/`-only commit [VERIFIED: `9-01-PLAN.md:139-143`; `9-01-SUMMARY.md:125`]:

- `STATE.md` — shipped record (release SHA, tag, GitHub Release URL); close REL-19; carry remaining backlog (FUT-04, FUT-05, 7-CODE-REVIEW IN-02, AAF still deferred, ROSAP optional).
- `MILESTONES.md` — convert "v1.19.0 (in planning…)" to shipped format matching the v1.18.0 entry (`d19be1a` / tag / URL bullets).
- `ROADMAP.md` — tick Phase 13; fill `**Plans**: 13-01-PLAN.md`.
- Tick REQUIREMENTS `REL-19-01` / `REL-19-02` (and optionally refresh the stale IO-01 "leave-2 is Phase 12" parenthetical).

### Anti-Patterns to Avoid

- Rebuilding packs or re-classifying the 16 map chapters.
- Unwiring `check_capability_map.main()` from `check_release`.
- Adding CI repo-Python.
- Hand-editing `docs/packs.html`.
- Staging with `-A` (untracked `master_flow_state.json` / `.edge-coverage.json` must not ship).
- Writing `gh --notes-file` under `/tmp` on Windows.
- Tagging on a red gate.
- Pushing a lightweight tag.
- Claiming IO-05/06/07 built.
- Putting URLs or em dashes in the CHANGELOG entry body.
- Waiting on sibling PR #2 merge.
</architecture_patterns>

<dont_hand_roll>
## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| Version bump script | New `bump_version.py` | Explicit edits + `gen_packs_page.py` | Analog is 11 known lines; a script is gold-plate |
| Release notes generator | Template engine | Copy CHANGELOG body to a phase-dir tmp file | Phase 9 already proved this |
| Catalog chapter linter | New gate assert | One integer edit + README rows | REL-19-01 leftover is two files |
| Second map regen | Agent re-classify | Bump `map_version` string only | Membership is frozen at 644 |
| CI map job | `python tooling/check_capability_map.py` in validate.yml | Local `check_release` §5d | CI must not exec repo Python |
| Protection / PR flow | Branch + CODEOWNERS | Direct push on admin-bypass | User opted to keep bypass |

**Key insight:** Phase 13 is almost entirely *apply already-decided deltas* plus the public tag act. The only judgment is CHANGELOG wording (competency-led) and the exact tag/title one-liners.
</dont_hand_roll>

<common_pitfalls>
## Common Pitfalls

### Pitfall 1: Listing only slugs in CHANGELOG
**What goes wrong:** REL-19-02 / ROADMAP SC-2 fail review even if the tag exists.
**Why it happens:** 1.17.0 / 1.18.0 entries are pack-slug catalogues; v1.19's value is IO outcomes (including three non-builds).
**How to avoid:** Lead with IO-01..07 by competency; slugs are evidence, not the headline.
**Warning signs:** `### Added` is only `nasa-std-8719-14` / `is-gps-200n` with no IO-05/06/07 lines.

### Pitfall 2: Forgetting `dod-vva-rpg.chapters` 10→13
**What goes wrong:** Catalog lies about a shipped pack; REL-19-01 leftover NOTE-1 survives the tag.
**Why it happens:** Thin-register added *new slugs* but left the existing slug's integer; gates stay green either way.
**How to avoid:** Task 3 is a named leftover, not "if you notice it."
**Warning signs:** `grep '"chapters": 10' catalog.json` still hits `dod-vva-rpg` after the release commit.

### Pitfall 3: Hand-editing packs.html or bumping RELEASE-INFO last
**What goes wrong:** Gate §5c `docs/packs.html is stale`.
**Why it happens:** REV span looks like the index.html hand-edit.
**How to avoid:** RELEASE-INFO first → `python tooling/gen_packs_page.py` → confirm idempotent re-run.
**Warning signs:** `docs/packs.html` in `git diff` after a second gen run.

### Pitfall 4: Leaving `map_version` at 1.18.0 (or bumping it in Phase 12 leftovers)
**What goes wrong:** Envelope still claims the map belongs to the previous release, contradicting CONTRACT §2; or Phase 12 already stole the bump and the trio disagrees.
**Why it happens:** Phase 12 research Q2 deferred the bump here; CONTRACT example still shows `1.18.0`.
**How to avoid:** Bump JSON `map_version` to `"1.19.0"` in Task 1 with the surfaces. Do not regenerate membership. Update CONTRACT example envelope to match.
**Warning signs:** Release commit touches plugin/CHANGELOG/RELEASE-INFO but not `docs/capability-pack-map.json:3`.

### Pitfall 5: `/tmp` notes file on Windows
**What goes wrong:** `gh release create --notes-file` cannot see the path; REL-19-02 looks done locally and is not.
**Why it happens:** Phase 9 first attempt failed exactly this way. [VERIFIED: `9-01-SUMMARY.md:228-232`]
**How to avoid:** Write `_v1.19.0-notes.tmp.md` under the phase directory; delete after `gh release view` succeeds; never commit it.
**Warning signs:** `open C:/Users/…/Temp/… The system cannot find the file specified`.

### Pitfall 6: Tagging without push, or tagging a red / dirty tree
**What goes wrong:** Local `v1.19.0` with no GitHub Release; or junk (`master_flow_state.json`) in the public commit.
**Why it happens:** "Don't push unless analog pushed" misread as don't push; analog **did** push.
**How to avoid:** Explicit-path `git add`; `git status --short` audit; gates green; then commit → tag → `git push origin main --follow-tags` → `gh release create`.
**Warning signs:** `git ls-remote --tags origin` has no `v1.19.0`; working tree shows `?? .planning/phases/13-…/master_flow_state.json` staged.

### Pitfall 7: Redoing Phase 11/12
**What goes wrong:** Double-build, reversed MOVE, or invented AAF pack sold as "full registration."
**Why it happens:** REL-19-01 says "full registration of any new packs" and sounds like a rebuild.
**How to avoid:** Registration leftover = catalog integer + README rows. Packs, map membership, hygiene, and thin-register are done.
**Warning signs:** Diff includes `packs/*/chapters/*` or map cluster arrays (other than the `map_version` string).

### Pitfall 8: CI elevation or sibling wait
**What goes wrong:** `validate.yml` starts executing repo Python; or Phase 13 blocks on HYG-03 PR merge.
**Why it happens:** "both gates PASS" is misread as "CI must run the map gate."
**How to avoid:** Local `check_release` is the ship gate. Sibling PR #2 is already recorded.
**Warning signs:** `.github/workflows/validate.yml` in the release commit.
</common_pitfalls>

<code_examples>
## Code Examples

### Gate trio (must agree after Task 1+2)

```json
// .claude-plugin/plugin.json:4
"version": "1.19.0",
```

```text
# RELEASE-INFO.txt
Version:    1.19.0
Tag:        v1.19.0
Staged:     <actual 2026-08-17T…Z>
```

```markdown
## [1.19.0]: 2026-08-17
```

Source of the check: `tooling/check_release.py:103-117`.

### map_version bump (do not touch clusters)

```json
{
  "schema_version": 2,
  "map_version": "1.19.0",
  "generated_on": "2026-08-17",
  "clusters": []
}
```

Live start: `docs/capability-pack-map.json:2-4` is `"1.18.0"` / `"2026-08-17"` / 644 entries. `generated_on` may stay (regen day) or refresh to execution day — informational only. [VERIFIED: `docs/capability-map-CONTRACT.md:36`]

### catalog leftover

```json
"slug": "dod-vva-rpg",
"chapters": 13,
```

Live: `catalog.json:612` is `10`.

### Exact release commands (Phase 9 analog, version swapped)

```bash
# after Tasks 1-4 green; explicit paths only
git add -- .claude-plugin/plugin.json .cursor-plugin/plugin.json \
  CHANGELOG.md RELEASE-INFO.txt README.md catalog.json \
  docs/index.html docs/packs.html \
  docs/products/website/01-jgs-se-knowledge-packs.yaml \
  docs/products/website/catalog.yaml \
  docs/capability-pack-map.json docs/capability-map-CONTRACT.md
# add any other Task 3 files actually edited; never -A

git commit --no-verify -m "release(v1.19.0): Agent IO Depth — 2 packs + VV&A chapters + DA remap (63 +2 signposts)"

git tag -a v1.19.0 -m "v1.19.0: 2 IO-unlock packs + VV&A chapters + DA remap (63 +2 signposts)"
git push origin main --follow-tags

# notes file = CHANGELOG [1.19.0] body; path under this phase dir
gh release create v1.19.0 \
  --title "v1.19.0 — Agent IO Depth (2 packs + VV&A chapters + DA remap)" \
  --notes-file .planning/phases/13-release-surface-v1-19-0/_v1.19.0-notes.tmp.md

git ls-remote --tags origin | grep v1.19.0
gh release view v1.19.0 --json name,tagName,url
```

If GSD created per-task commits before Task 5: `git reset --soft` to pre-task HEAD, restage the same explicit paths, one `release(v1.19.0)` commit — Phase 9 deviation #1, required by "last content commit." [VERIFIED: `9-01-SUMMARY.md:221-226`]
</code_examples>

<sota_updates>
## State of the Art (this repo, 2026-08-17)

| Old approach (v1.18 / Phase 9) | Phase 13 approach | When changed | Impact |
|--------------------------------|-------------------|--------------|--------|
| Dual gates run independently; map not inside `check_release` | `check_release` §5d imports map `main()` | MAP-19-04 / Phase 12 | Cannot ship 1.19.0 against a stale map |
| CHANGELOG is a pack-slug catalogue | Competency-led IO-01..07 narrative | REL-19-02 / ROADMAP SC-2 | Deferrals/accept are first-class release notes |
| `map_version` already matched the new tag (Phase 8 wrote 1.18.0) | Phase 12 left `map_version` 1.18.0; Phase 13 bumps it | Phase 12 Q2 + this phase | Envelope tracks the release that *published* the regen |
| Catalog 61 / dirs 63 | Catalog 63 / dirs 65 (thin-register already) | Phase 11-02 | Release does not add slugs; it versions them |
| CHANGELOG BOM / no `.gitattributes` | Already stripped + pinned | HYG-01 / Phase 12 | Do not re-do hygiene |

**Deprecated/outdated:**

- PROJECT.md "Current State" still says v1.18.0 / 628 entries — refresh in Task 6 or leave for milestone close; not a gate surface.
- REQUIREMENTS IO-01 parenthetical "Live count leave-2 is Phase 12" — live DA is 5/4. Optional annotation when ticking REL boxes. [VERIFIED: `12-INTEGRATION_CHECK.md:109`]
- `docs/capability-pack-map.md:15` already has a human "Changelog (v1.19)" bullet — do not rewrite classification; optional tidy to `v1.19.0` when `map_version` bumps.
</sota_updates>

<open_questions>
## Open Questions

1. **Does REL-19 bump `map_version` to 1.19.0?**
   - What we know: CONTRACT §2 — "`map_version` tracks the knowledge-pack **release** that regenerated the map." Phase 12 kept `"1.18.0"` so the unreleased regen would not spoof a tag. [VERIFIED: `docs/capability-map-CONTRACT.md:53`; `12-RESEARCH.md:514-517`; `STATE.md:67` — "map_version stays 1.18.0"]
   - What's unclear: a pedant could leave 1.18.0 because the *classification* happened under the 1.18 tree.
   - Recommendation: **YES — bump to `1.19.0`.** This is the release that publishes the regen. Leaving 1.18.0 would repeat the IN-04 class problem Phase 9 closed (map_version != tag).

2. **Should Integration "move" appear in CHANGELOG as a count delta?**
   - What we know: IO-05 is DEFERRED; Integration held 4/4; no raid. [VERIFIED: `12-01-SUMMARY.md:43`]
   - Recommendation: record **deferred**, not a fake "Integration +0" added line.

3. **Tick REQUIREMENTS IO/MAP/HYG boxes here?**
   - What we know: Phase 11/12 verify owned those ticks; some boxes may still read `- [ ]` depending on host `phase.complete`. REL-19 boxes are still open by design.
   - Recommendation: tick **REL-19-01/02** after tag. Do not silently tick VET/IO/MAP/HYG unless verify already did.
</open_questions>

<recommended_plan_shape>
## Recommended plan shape (do NOT write PLAN.md here)

**ONE execute plan (`13-01`)** — clone `9-01-PLAN.md` (6 tasks). Do not split bump vs tag.

**Plan 13-01 — Release surface + v1.19.0 (REL-19-01/02)**

1. **Version bump.** All 11 Phase-9 surfaces 1.18.0 → 1.19.0. RELEASE-INFO first (Version / Tag / live Staged timestamp) → `python tooling/gen_packs_page.py` → plugins / README ×3 / index.html ×2 / two website YAMLs. Also set `docs/capability-pack-map.json` `map_version` to `"1.19.0"` and align the CONTRACT example envelope. Do not touch historical changelog bullets or SOURCE-VETTING section headings.
2. **CHANGELOG `[1.19.0]`.** Competency-led IO-01..07 narrative (remap, leftover chapters, 8719, GPS, IO-05/06 deferred, IO-07 accept) plus live chapter counts 7/6/13. No em dashes / URLs. Catalogue now 63 (+2 signposts).
3. **REL-19-01 leftovers.** `catalog.json` `dod-vva-rpg.chapters` 10→13. README live-pack rows for `nasa-std-8719-14` + `is-gps-200n`; RPG "10 chapters" → 13. Do not re-edit SKILLS/NOTICE/cursor skill lists (already thin-registered).
4. **Final validation.** Both gates PASS; catalog 63 / dirs 65; packs.html idempotent; residual `1.18.0` whitelist-only; spot `validate_pack` on the three touched slugs; re-run `check_release` immediately before commit.
5. **Release commit + annotated tag + push + GitHub Release.** Explicit paths; last content commit; colon-style tag; `git push origin main --follow-tags`; `gh release create` with phase-dir notes file. Verify `git ls-remote` + `gh release view`.
6. **Post-release records.** STATE / MILESTONES / ROADMAP / REL ticks. Separate `.planning` commit.

**Must-NOT:** pack rebuild; map reclassify / reverse MOVE; unwire map gate; CI repo-Python; `git add -A`; `/tmp` notes; lightweight tag; AAF/CBA/DoDM/stakeholder packs; Cyber/DE bindings; branch-protection "fix."

Analog: `.planning/phases/9-release-surface-v1-18-0/9-01-PLAN.md` (not Phase 11 pack-build, not Phase 12 map regen).
</recommended_plan_shape>

<validation_architecture>
## Validation Architecture

Phase 13 is docs + two stdlib gates + public git/GitHub metadata. No runtime, no UI.

| Layer | What it proves | Command / check |
|---|---|---|
| Version trio | plugin == CHANGELOG top == RELEASE-INFO | `check_release.py` §4 |
| 11 surfaces | no live 1.18.0 REV left | `grep -rn "1\.18\.0"` excl `.planning`/`.git`/`sources` → history whitelist only |
| Generated page | packs.html == fresh gen | `python tooling/gen_packs_page.py` then empty diff; gate §5c |
| Catalog leftover | RPG chapters integer matches disk | `catalog.json` `dod-vva-rpg.chapters == 13`; PACK.yaml `chapters: 13`; 13 files |
| README leftover | new slugs + RPG 13 | grep `nasa-std-8719-14` / `is-gps-200n` / `13 chapters` in README table |
| Thin-register not regressed | SKILLS 63 / cursor 64 / NOTICE both slugs | already green; `check_release` §6 / §6b |
| Map freshness | 644 / floors / uniqueness; `map_version` 1.19.0 | `python tooling/check_capability_map.py` |
| Ship gate includes map | stale map fails release | `python tooling/check_release.py` → `RELEASE CHECK: PASS` (prints TOTAL 644) |
| Basis | catalog 63 / dirs 65 | independent python + `ls packs \| wc -l` |
| CHANGELOG policy | competency IO lines; no em dash; no URL | grep IO-01..07 / `—` / `http` in the new entry |
| Tag | annotated colon-style on origin | `git cat-file -t $(git rev-parse v1.19.0)` == `tag`; `git ls-remote --tags origin \| grep v1.19.0` |
| GitHub Release | published, notes = CHANGELOG body | `gh release view v1.19.0` |
| Phase 11/12 fence | no pack/map-membership rewrite | `git show --stat` on release commit: version/docs only (+ catalog integer + README + `map_version` string) |
| CI fence | validate.yml untouched | not in the release commit |
| Link policy | SOURCE-VETTING still 0 `http` | `grep -c http docs/SOURCE-VETTING.md` → 0 |

Human judgment: CHANGELOG reads as IO-unlocks-by-competency (SC-2). Tag/title one-liners are analog-style, not marketing fluff.
</validation_architecture>

<sources>
## Sources

### Primary (HIGH confidence)
- `.planning/REQUIREMENTS.md:46-58` — REL-19-01/02; out-of-scope branch protection
- `.planning/ROADMAP.md:74-84` — Phase 13 goal + SC
- `.planning/STATE.md:31-68` — Phase 13 ready to plan; admin-bypass; Phase 12 leftovers; `map_version` stayed 1.18.0
- `.planning/phases/9-release-surface-v1-18-0/9-01-PLAN.md` — AUTHORITATIVE analog (11 surfaces, 6 tasks, push, tag style)
- `.planning/phases/9-release-surface-v1-18-0/9-01-SUMMARY.md` — what actually ran (`d19be1a`, colon tag, `gh` title em dash, `/tmp` failure, soft-reset)
- `11-INTEGRATION_CHECK.md:89-92` + `11-02-SUMMARY.md:178,219` — catalog 10; README missing rows; thin-register already green
- `12-INTEGRATION_CHECK.md:29-43,103-111` + `12-GAP_ANALYSIS.md:110-118` — P13 leftovers; frozen map; no CI Python
- Live files 2026-08-17: plugin/cursor/RELEASE-INFO/CHANGELOG/README/index/packs.html/website YAMLs all `1.18.0`; `catalog.json:612` chapters 10; map envelope `1.18.0` / 644; SKILLS 63; NOTICE both slugs
- `tooling/check_release.py:103-117,144-157,215-222` — trio, packs.html, map import
- `tooling/check_capability_map.py:74-81` — `map_version` shape only (not trio-equal)
- `docs/capability-map-CONTRACT.md:15,53-54,81-83` — map_version tracks release; historical 1.17.0; wired check_release
- Live `python tooling/check_capability_map.py` → PASS TOTAL 644
- Live `git tag -l -n3 v1.17.0 v1.18.0`; `gh release view v1.18.0`; `gh auth status`

### Secondary (MEDIUM confidence)
- `5-RESEARCH.md` — original 11-surface inventory + OneDrive warning
- CHANGELOG draft wording above — planner may tighten; competency coverage is locked, prose is not

### Tertiary (LOW confidence)
- PROJECT.md pack-count prose still says 628 / v1.18.0 — optional Task 6 refresh
</sources>

<metadata>
## Metadata

**Research scope:**
- Core technology: version surfaces + two stdlib gates + git annotated tag + `gh release`
- Ecosystem: Phase 9 analog, Phase 11 thin-register leftovers, Phase 12 frozen map
- Patterns: RELEASE-INFO-first gen, explicit-path release commit, colon tag, phase-dir notes file, push-then-gh
- Pitfalls: slug-only CHANGELOG, leftover chapter integer, `/tmp` notes, map_version orphan, redoing 11/12

**Confidence breakdown:**
- Standard stack: HIGH — live files + Phase 9 analog
- Architecture: HIGH — 11 surfaces + leftovers + tag procedure
- `map_version` decision: HIGH recommendation (bump), CONTRACT-backed
- CHANGELOG exact sentences: MEDIUM — competency coverage locked

**Research date:** 2026-08-17
**Valid until:** 2026-09-16 (or until v1.19.0 is tagged)
</metadata>

---

*Phase: 13-release-surface-v1-19-0*
*Research completed: 2026-08-17*
*Ready for planning: yes*
