# Technology Stack

**Analysis Date:** 2026-08-14

## Languages

**Primary:**
- Markdown — the product itself: each pack is `packs/<slug>/SKILL.md` + `chapters/*.md` + `cheatsheet.md` + `glossary.md` + `patterns.md` + `PACK.yaml`
- Python 3.13/3.14 — all tooling (`tooling/*.py`, `install.py`); stdlib-only imports (`argparse`, `json`, `re`, `sys`, `pathlib`, `shutil`, `html`)

**Secondary:**
- JavaScript (Node.js) — one-off generators: `build_retirement_pptx.js` (uses global `pptxgenjs`), `tooling/build_all_packs.workflow.js` (Claude Code `Workflow()` API script)
- Bash — `scripts/configure_repo.sh` (drives `gh` CLI)
- YAML — `packs/*/PACK.yaml`, `packs/*/SKILL.md` frontmatter, `.github/workflows/validate.yml`
- PowerShell — `install.ps1` (Windows wrapper around `install.py`)

## Runtime

**Environment:**
- Python 3.13+ (bytecode tags `cpython-313`/`cpython-314` in `__pycache__`); CI uses `python3` on `ubuntu-latest`
- Node.js for the pptx generator and the Workflow orchestrator (no `package.json` — deps installed globally)

**Package Manager:**
- None. No `package.json`, `requirements.txt`, or `pyproject.toml`. Python tooling is deliberately stdlib-only; the only Node dependency (`pptxgenjs`) is loaded by absolute global path in `build_retirement_pptx.js`
- Lockfile: not applicable

## Frameworks

**Core:**
- None — this is a content repository (Agent Skills knowledge packs), not an application

**Testing:**
- pytest 9.x — `tooling/eval/tests/` (test source files currently absent; only `__pycache__`/`.pytest_cache` remain from a removed eval harness)
- ruff 0.15.x — linting (`.ruff_cache/` present; no config file, defaults used)

**Build/Dev:**
- GitHub Actions — `.github/workflows/validate.yml` (content-integrity gate)
- GitHub Pages — static site from `docs/` (`index.html`, `packs.html`, `docs/fonts/`, `docs/products/`)
- Claude Code `Workflow()` API — `tooling/build_all_packs.workflow.js` orchestrates pack synthesis

## Key Dependencies

**Critical:**
- Python 3 stdlib only — enforced by design (`tooling/check_release.py`, `tooling/validate_pack.py`, `tooling/gen_packs_page.py`, `tooling/build_pack.py`, `install.py`)
- `gh` CLI — required by `scripts/configure_repo.sh` (scopes: repo, workflow)
- `pptxgenjs` — global npm package used by `build_retirement_pptx.js`

**Infrastructure:**
- GitHub Actions `actions/checkout@v4` — only CI action used
- `catalog.json` — repo-level pack registry (schema: json-schema.org draft 2020-12)

## Configuration

**Environment:**
- `CLAUDE_CONFIG_DIR` — honoured by `install.py` for the `claude` agent target
- No `.env` files required; no secrets in repo

**Build:**
- `.claude-plugin/plugin.json` + `.claude-plugin/marketplace.json` — Claude plugin manifest; `plugin.json` `version` is the single source of truth for releases
- `.cursor-plugin/plugin.json` + `.cursor-plugin/marketplace.json` — Cursor plugin manifest
- `.github/workflows/validate.yml` — CI gate (leak sentinels, link policy, frontmatter lint, catalog JSON validity)
- `.gitignore` excludes `sources/`, `**/.build/`, caches

## Platform Requirements

**Development:**
- Windows-friendly (paths in `tooling/build_all_packs.workflow.js` are `C:/Users/...` style; `install.ps1` for PowerShell), Python 3.13+, optional Node.js + global `pptxgenjs`, optional `gh` CLI authenticated

**Production:**
- GitHub repo `jgsystemsconsulting/jgs-se-knowledge-packs`; GitHub Pages at `https://jgsystemsconsulting.github.io/jgs-se-knowledge-packs/`; distributed as Claude/Cursor plugins and via `install.py`

---

*Stack analysis: 2026-08-14*
