<!-- refreshed: 2026-08-14 -->
# Architecture

**Analysis Date:** 2026-08-14

## System Overview

This is a **content-first repository**, not an application: it produces 48 installable
"knowledge packs" (Agent Skills in the agentskills.io `SKILL.md` format) synthesized
from licence-vetted systems-engineering sources. Python stdlib tooling orchestrates
scaffolding/validation; an agent workflow performs content synthesis.

```text
┌──────────────────────────────────────────────────────────────────────────┐
│                        Sources (staged inputs)                           │
│  sources/<slug>/<slug>.pdf  +  sources/<slug>/.build/{full_text.txt,     │
│  outline.json, metadata.json}                                            │
└──────────────────────────────┬───────────────────────────────────────────┘
                               │  (extraction + offset-mapped synthesis,
                                │   driven by an agent per docs/PACK-SPEC.md)
                               ▼
┌──────────────────────────────────────────────────────────────────────────┐
│                     Packs (the shipped product)                          │
│  packs/<slug>/{SKILL.md, PACK.yaml, LICENSE, chapters/chNN-*.md,         │
│               glossary.md, patterns.md, cheatsheet.md}                   │
└──────────────────────────────┬───────────────────────────────────────────┘
                               │  tooling/build_pack.py (scaffold)
                               │  tooling/build_all_packs.workflow.js (pipeline)
                               │  tooling/validate_pack.py (per-pack gate)
                               ▼
┌──────────────────────────────────────────────────────────────────────────┐
│                        Registry & Release Layer                          │
│  catalog.json · SKILLS.md · NOTICE · README.md · CHANGELOG.md            │
│  tooling/gen_packs_page.py → docs/packs.html                             │
│  tooling/check_release.py (local gate) · .github/workflows/validate.yml  │
└──────────────────────────────┬───────────────────────────────────────────┘
                               │
                               ▼
┌──────────────────────────────────────────────────────────────────────────┐
│                    Consumers (installation/delivery)                     │
│  install.py / install.sh / install.ps1 → ~/.claude/skills/<ns>/<slug>/   │
│  (native: claude, openclaw, copilot; transform: other agents)            │
│  .claude-plugin/ + .cursor-plugin/ (marketplace/plugin manifests)        │
└──────────────────────────────────────────────────────────────────────────┘
```

## Component Responsibilities

| Component | Responsibility | File |
|-----------|----------------|------|
| Pack scaffolder | Create `packs/<slug>/` skeleton with pre-filled `PACK.yaml` + `LICENSE` stub; forces licence/tier declaration | `tooling/build_pack.py` |
| Batch build orchestrator | Workflow script: vet → extract → outline → scaffold → chapters → verify, then registry update; fail-closed per pack | `tooling/build_all_packs.workflow.js` |
| Pack validator | Structural + licence checks (required files, frontmatter, chapter-link resolution, tier 1–3); stdlib-only mini-YAML parser | `tooling/validate_pack.py` |
| Release gate | Aggregates all release checks: required files, leak sentinels, link policy, version single-sourcing, SKILLS.md count | `tooling/check_release.py` |
| Docs page generator | Emits `docs/packs.html` from `SKILLS.md` (single source; regenerate to avoid drift) | `tooling/gen_packs_page.py` |
| Installer | Copy/transform packs into agent skill directories (native copy vs. inlined transform per agent) | `install.py`, `install.sh`, `install.ps1` |
| Pack index (per pack) | Always-loaded `SKILL.md`: frontmatter, core frameworks, chapter/topic routing indexes | `packs/<slug>/SKILL.md` |
| Pack provenance | Licence, tier, publisher, source version, build metadata | `packs/<slug>/PACK.yaml` |
| Machine catalog | JSON registry of all packs (slug, licence, tier, chapters, status) | `catalog.json` |
| Human catalog | Markdown table of skills; upstream of `docs/packs.html` | `SKILLS.md` |
| Spec | Pack layout, SKILL.md body-order rules, PACK.yaml schema | `docs/PACK-SPEC.md` |
| Vetting policy | Licence tiers (1=public domain, 2=CC, 3=other), exclusion rules | `docs/SOURCE-VETTING.md` |
| CI gate | Self-contained inline checks mirroring `check_release.py`; never executes repo code | `.github/workflows/validate.yml` |

## Pattern Overview

**Overall:** Pipeline / content-registry architecture with gated quality checks and
progressive disclosure at the consumer.

**Key Characteristics:**
- Content (packs, per-source licences) is strictly separated from tooling (MIT)
- Single-source registries with generated downstream artifacts (`SKILLS.md` → `docs/packs.html`; version pinned in `.claude-plugin/plugin.json` == CHANGELOG top == `RELEASE-INFO.txt`)
- Fail-closed gates: a pack failing vet/validation is never registered
- Stdlib-only Python tooling (no PyYAML etc.) so CI needs no dependencies
- Progressive disclosure: `SKILL.md` index (<~4,000 tokens) routes to on-demand `chapters/chNN-*.md`

## Layers

**Sources layer:**
- Purpose: staged raw source material plus extraction artifacts
- Location: `sources/<slug>/` (PDF) and `sources/<slug>/.build/` (`full_text.txt`, `outline.json`, `metadata.json`, prior `OLD_PACK.yaml`/`OLD_LICENSE`)
- Contains: 29 staged sources (subset of the 48 packs; some packs built from sources since removed or signpost-style)
- Used by: agent synthesis pipeline (`tooling/build_all_packs.workflow.js`)

**Packs layer:**
- Purpose: the shipped product — self-contained Agent Skills
- Location: `packs/<slug>/`
- Contains: `SKILL.md`, `PACK.yaml`, `LICENSE`, `chapters/chNN-*.md`, optional `glossary.md`/`patterns.md`/`cheatsheet.md`
- Depends on: nothing at runtime (plain Markdown, no MCP/API keys)
- Used by: `install.py`, validators, registry pages

**Tooling layer:**
- Purpose: deterministic build/validation/release mechanics
- Location: `tooling/`
- Contains: Python scripts + one `.workflow.js` orchestrator; `tooling/eval/` (eval harness; `tooling/eval/tests/` holds only `.pyc` caches — test sources not present)

**Registry/delivery layer:**
- Purpose: cataloguing, versioning, distribution
- Location: repo root (`catalog.json`, `SKILLS.md`, `RELEASE-INFO.txt`, `CHANGELOG.md`, `NOTICE`, `install.*`), `.claude-plugin/`, `.cursor-plugin/`, `docs/`

## Data Flow

### Pack Build Path

1. Source staged at `sources/<slug>/<slug>.pdf`; extraction writes `sources/<slug>/.build/full_text.txt` + `outline.json`
2. `tooling/build_pack.py --slug X --title ... --tier N` scaffolds `packs/X/` with `PACK.yaml` + `LICENSE` stub (licence/tier must be declared up front per `docs/SOURCE-VETTING.md`)
3. Agent-driven chapter synthesis per `docs/PACK-SPEC.md` (offset-mapped, parallel per chapter) — orchestrated by `tooling/build_all_packs.workflow.js`
4. `tooling/validate_pack.py packs/X` gates structure + licence tier
5. Passing packs registered once: `catalog.json`, `SKILLS.md`, `NOTICE`, `README.md`, `CHANGELOG.md` updated

### Release Path

1. `tooling/check_release.py` verifies required files, leak sentinels, link policy (no source-material URLs; signpost packs exempt), version agreement, all-pack validation, SKILLS.md count
2. `.github/workflows/validate.yml` re-runs the same checks self-contained in CI (push to main + PRs)
3. `tooling/gen_packs_page.py` regenerates `docs/packs.html` from `SKILLS.md`

### Install Path (consumer)

1. User runs `install.py` (or `.sh`/`.ps1`)
2. Native agents (claude, openclaw, copilot): pack folder copied unchanged to `~.<agent>/skills/<ns>/<slug>/`
3. Transform agents: `SKILL.md` index inlined into a single prompt/command/rule file (see `docs/other-agents.md`)
4. At runtime the agent loads only `SKILL.md`; topics route to `chapters/chNN-*.md` via the Chapter/Topic Index (progressive disclosure)

**State Management:** None at runtime — packs are static Markdown. Build-time state lives in `sources/<slug>/.build/` and the registry files.

## Key Abstractions

**Knowledge Pack:**
- Purpose: one installable skill derived from one vetted source
- Examples: `packs/sebok/`, `packs/nasa-se-handbook/`, `packs/faa-rma/` (48 total)
- Pattern: fixed file layout defined by `docs/PACK-SPEC.md`; enforced by `tooling/validate_pack.py`

**SKILL.md (progressive-disclosure index):**
- Purpose: always-loaded entry point with frontmatter (`name` = slug, `description` with scope limits), Core Frameworks, Chapter Index, Topic Index, Scope & Limits
- Pattern: body ordered most-important-first (hosts truncate from the end on compaction)

**Licence tier system:**
- Purpose: govern what may be packaged and under what terms
- Tiers: 1 (public domain/US Gov), 2 (CC), 3 (other); "Excluded" tier never ships
- Recorded in: `packs/<slug>/PACK.yaml` (`license_tier`), `catalog.json`, per-pack `LICENSE`

**Registry single-sourcing:**
- `catalog.json` (machine), `SKILLS.md` (human), `docs/packs.html` (generated); version triple-sourced but gate-checked for agreement

## Entry Points

**CLI tools:**
- `tooling/build_pack.py` — scaffold a new pack (argparse: slug/title/publisher/version/license/tier)
- `tooling/validate_pack.py` — validate one pack or `--all`
- `tooling/check_release.py` — full release-readiness gate
- `tooling/gen_packs_page.py` — regenerate `docs/packs.html`
- `install.py` / `install.sh` / `install.ps1` — consumer installation

**Workflow:**
- `tooling/build_all_packs.workflow.js` — invoked via `Workflow({ scriptPath, args })`; builds staged packs and registers passers; never commits/pushes

**CI:**
- `.github/workflows/validate.yml` — content-integrity, link-policy, frontmatter, catalog checks (inline, stdlib only)

## Architectural Constraints

- **No runtime dependencies for packs:** plain Markdown; no MCP servers, API keys, or licence checks at runtime
- **Stdlib-only Python tooling:** deliberate (CI needs nothing but python3); `tooling/validate_pack.py` includes a minimal YAML subset parser rather than PyYAML
- **CI never executes repo code:** `.github/workflows/validate.yml` inlines its checks; `tooling/check_release.py` is a local/trusted gate only
- **Link policy:** source-material download URLs banned everywhere except `kind: signpost` packs (enforced in both gates)
- **Dual licensing:** MIT covers tooling only; each pack's content carries its source's licence (`packs/<slug>/LICENSE`)
- **Version single-sourcing:** `.claude-plugin/plugin.json` version == `CHANGELOG.md` top entry == `RELEASE-INFO.txt`
- **Fail-closed pipeline:** packs failing vet/overlap/validate are not registered
- **Windows-path coupling:** `tooling/build_all_packs.workflow.js` hardcodes the absolute repo path and the sibling `jgs-reference-skill` checkout path as defaults

## Anti-Patterns

### Editing registry files by hand without regenerating downstream artifacts

**What happens:** `docs/packs.html` is generated from `SKILLS.md`; `catalog.json`, `NOTICE`, `README.md` counts must stay in sync
**Why it's wrong:** `tooling/check_release.py` fails the release on drift (SKILLS.md entry count vs pack count; version disagreement)
**Do this instead:** register packs through `tooling/build_all_packs.workflow.js` and re-run `tooling/gen_packs_page.py` after any `SKILLS.md` change

### Adding chapters without updating SKILL.md indexes

**What happens:** every `chapters/chNN-*.md` must be linked from `SKILL.md`
**Why it's wrong:** `tooling/validate_pack.py` fails on unlinked chapter files; agents cannot route to them
**Do this instead:** add the chapter row to the Chapter Index (and Topic Index entries) in `packs/<slug>/SKILL.md`

### Bypassing the scaffolder to create packs manually

**What happens:** creating `packs/<slug>/` without `tooling/build_pack.py`
**Why it's wrong:** the scaffolder forces licence + tier declaration, guaranteeing provenance is on record before content exists
**Do this instead:** always start with `tooling/build_pack.py --slug ... --tier ...` per `docs/SOURCE-VETTING.md`

## Error Handling

**Strategy:** Exit-code-based gates; fail-closed.

**Patterns:**
- CLI validators exit 0/1 with per-check error output (`tooling/validate_pack.py`, `tooling/check_release.py`)
- CI uses `::error::` GitHub annotations for sentinel/policy violations (`.github/workflows/validate.yml`)
- Build pipeline registers only packs that pass all gates

## Cross-Cutting Concerns

**Logging:** Plain stdout prints from tooling scripts; CI step logs. No logging framework.
**Validation:** Three tiers — per-pack (`tooling/validate_pack.py`), repo release (`tooling/check_release.py`), CI mirror (`.github/workflows/validate.yml`)
**Authentication:** None (public content repo; no secrets, and leak sentinels actively checked for)

---

*Architecture analysis: 2026-08-14*
