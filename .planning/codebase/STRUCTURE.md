# Codebase Structure

**Analysis Date:** 2026-08-14

## Directory Layout

```
jgs-se-knowledge-packs/
├── packs/                  # THE PRODUCT: 48 knowledge packs, one per source
│   └── <slug>/             #   installable Agent Skill
│       ├── SKILL.md        #   always-loaded index (frontmatter + frameworks + indexes)
│       ├── PACK.yaml       #   provenance + licence metadata
│       ├── LICENSE         #   the SOURCE's licence terms (not MIT)
│       ├── chapters/       #   chNN-<slug>.md on-demand reference chapters
│       ├── glossary.md     #   optional: terms with chapter refs
│       ├── patterns.md     #   optional: techniques (when/how/trade-offs)
│       └── cheatsheet.md   #   optional: decision rules, tables
├── sources/                # staged source PDFs + build artifacts (29 slugs)
│   └── <slug>/
│       ├── <slug>.pdf      #   the vetted source document
│       └── .build/         #   full_text.txt, outline.json, metadata.json,
│                           #   OLD_PACK.yaml / OLD_LICENSE (prior builds)
├── tooling/                # MIT-licensed build/validate/release scripts
│   ├── build_pack.py       #   scaffold one new pack
│   ├── build_all_packs.workflow.js  # agent pipeline orchestrator
│   ├── validate_pack.py    #   per-pack structural + licence validator
│   ├── check_release.py    #   full release-readiness gate
│   ├── gen_packs_page.py   #   SKILLS.md -> docs/packs.html
│   └── eval/               #   eval harness (tests/ holds only .pyc caches)
├── docs/                   # specs, policy, generated pages
│   ├── PACK-SPEC.md        #   required pack layout + SKILL.md rules
│   ├── SOURCE-VETTING.md   #   licence tier policy
│   ├── LICENSING.md        #   dual-licence + link policy
│   ├── other-agents.md     #   transform-agent install matrix
│   ├── skill-usage.md      #   usage guidance
│   ├── index.html, packs.html  # generated browsable pages
│   ├── fonts/              # self-hosted fonts (no CDN)
│   └── products/website/   # website product YAML
├── .claude-plugin/         # plugin.json + marketplace.json (version source of truth)
├── .cursor-plugin/         # Cursor plugin manifests
├── .github/                # workflows/validate.yml + ISSUE_TEMPLATE/
├── scripts/                # configure_repo.sh
├── catalog.json            # machine-readable pack registry
├── SKILLS.md               # human pack catalogue (source for packs.html)
├── install.py / .sh / .ps1 # consumer installer (multi-agent)
├── build_retirement_pptx.js # one-off PPTX generator + 2 .pptx artifacts
├── CHANGELOG.md, NOTICE, LICENSE, COPYRIGHT, README.md,
│   CONTRIBUTING.md, SECURITY.md, CODE_OF_CONDUCT.md, RELEASE-INFO.txt
└── .planning/              # GSD planning docs (not part of the product)
```

## Directory Purposes

**`packs/<slug>/`:**
- Purpose: the shipped knowledge packs; each is a self-contained installable skill
- Contains: `SKILL.md`, `PACK.yaml`, `LICENSE`, `chapters/chNN-*.md`, optional `glossary.md`/`patterns.md`/`cheatsheet.md`
- Key files: exact layout mandated by `docs/PACK-SPEC.md`; validated by `tooling/validate_pack.py`
- 48 packs: `sebok`, `nasa-se-handbook`, `faa-rma`, `nist-csf`, `mil-std-882`, `dodaf`, `eu-ai-act`, `gao-*`, `se-standards-signpost`, etc.

**`sources/<slug>/`:**
- Purpose: staged input material for pack synthesis
- Contains: source PDF plus `.build/` extraction artifacts
- Note: 29 sources staged vs 48 packs — signpost/curated packs exist without staged PDFs

**`tooling/`:**
- Purpose: deterministic build, validation, release, and docs-generation mechanics (MIT)
- Contains: Python (stdlib-only) scripts + one `.workflow.js` orchestrator

**`docs/`:**
- Purpose: normative specs and policy that the tooling enforces
- Key files: `docs/PACK-SPEC.md`, `docs/SOURCE-VETTING.md`, `docs/LICENSING.md`

**`.claude-plugin/` / `.cursor-plugin/`:**
- Purpose: plugin marketplace manifests; `.claude-plugin/plugin.json` `version` is the release version single-source

## Key File Locations

**Entry Points:**
- `tooling/build_pack.py`: scaffold a new pack (argparse CLI)
- `tooling/build_all_packs.workflow.js`: batch build pipeline (agent-invoked)
- `tooling/validate_pack.py`: pack validator (`packs/<slug>` or `--all`)
- `tooling/check_release.py`: pre-tag release gate
- `install.py`: consumer installer (`--agent`, `--dry-run`, `--list-agents`, `--target`)

**Configuration:**
- `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`: plugin identity/version
- `catalog.json`: pack registry with `$schema` (JSON Schema 2020-12)
- `RELEASE-INFO.txt`: version record (must match plugin.json + CHANGELOG top)

**Core Logic:**
- `tooling/validate_pack.py`: `parse_simple_yaml()` minimal YAML parser + structural checks
- `tooling/check_release.py`: `REQUIRED_FILES` list, leak sentinels, link policy
- `tooling/gen_packs_page.py`: `parse_skills()` / `deslop()` for HTML generation

**Specs (read before modifying packs):**
- `docs/PACK-SPEC.md`: layout + SKILL.md body-order rules
- `docs/SOURCE-VETTING.md`: licence tiers
- `docs/LICENSING.md`: link policy, dual licensing

**Testing:**
- `tooling/eval/tests/`: pytest cache artifacts only (`.pyc`); test sources not present in tree
- `.github/workflows/validate.yml`: the effective executable quality gate

## Naming Conventions

**Packs (slugs):**
- Lowercase kebab-case derived from the source: `nasa-se-handbook`, `faa-req-handbook`, `dod-mq-bok`, `nist-800-37`, `mil-hdbk-61`, `se-standards-signpost`
- Pack slug MUST equal the `name` field in `SKILL.md` frontmatter and the folder name (CI-checked)

**Chapters:**
- `chapters/chNN-<slug>.md` — zero-padded two-digit number + kebab slug, e.g. `packs/sebok/chapters/ch03-sebok-nature-of-systems.md`

**Pack files:**
- UPPERCASE required files: `SKILL.md`, `PACK.yaml`, `LICENSE`
- lowercase optional files: `glossary.md`, `patterns.md`, `cheatsheet.md`

**Tooling scripts:**
- snake_case Python: `build_pack.py`, `validate_pack.py`, `check_release.py`, `gen_packs_page.py`
- kebab/dot for workflow JS: `build_all_packs.workflow.js`

## Where to Add New Code

**New pack:**
- Stage source at `sources/<slug>/<slug>.pdf`
- Scaffold: `python tooling/build_pack.py --slug X --title ... --publisher ... --version ... --license ... --tier N --commercial-use ...`
- Content lands in `packs/<slug>/chapters/` per `docs/PACK-SPEC.md`
- Register in `catalog.json`, `SKILLS.md`, `NOTICE`, `README.md`, `CHANGELOG.md` (or let `tooling/build_all_packs.workflow.js` do it)
- Validate: `python tooling/validate_pack.py packs/<slug>`

**New tooling script:**
- `tooling/<name>.py`, stdlib only, SPDX MIT header (JGSC copyright + `SPDX-License-Identifier: MIT`)
- If release-relevant, add its checks to `tooling/check_release.py` and mirror inline in `.github/workflows/validate.yml`

**New install target (agent):**
- Add to the agent matrix in `install.py` and document in `docs/other-agents.md`

**Docs pages:**
- Never hand-edit `docs/packs.html`; edit `SKILLS.md` then run `tooling/gen_packs_page.py`

**Tests:**
- pytest under `tooling/eval/tests/` (restore/create `test_*.py` sources; currently only `.pyc` caches exist)

## Special Directories

**`sources/<slug>/.build/`:**
- Purpose: extraction intermediates (`full_text.txt`, `outline.json`, `metadata.json`) and prior-build snapshots (`OLD_PACK.yaml`, `OLD_LICENSE`)
- Generated: Yes (by extraction pipeline)
- Committed: Yes

**`.ruff_cache/`, `tooling/eval/.pytest_cache/`, `tooling/__pycache__/`:**
- Purpose: linter/pytest/compiler caches
- Generated: Yes; safe to delete

**`.playwright-mcp/`:**
- Purpose: Playwright MCP session artifacts (website work)

**`docs/fonts/`:**
- Purpose: self-hosted fonts so generated pages need no CDN

---

*Structure analysis: 2026-08-14*
