# External Integrations

**Analysis Date:** 2026-08-14

## APIs & External Services

**GitHub Platform (via `gh` CLI):**
- `scripts/configure_repo.sh` — applies publish-time platform state: repo About metadata (description/homepage/topics), GitHub Pages enablement (`gh api repos/.../pages`), GitHub Releases for the tag from `.claude-plugin/plugin.json` version, branch protection. Idempotent; `--dry-run` supported. Requires `gh auth login` with `repo` and `workflow` scopes.

**Claude Code `Workflow()` API:**
- `tooling/build_all_packs.workflow.js` — launched via Claude Code's Workflow tool; orchestrates pack build pipeline (vet → extract → outline → scaffold → chapters → verify → register). Not a network API; an in-agent integration.

**Source material (offline, not runtime):**
- Public-domain US Government PDFs staged under `sources/<slug>/` (NASA, FAA, DoD, GAO, NIST, DAU) — build inputs only, gitignored, never distributed. No code fetches them at runtime.

## Data Storage

**Databases:**
- None. `catalog.json` (repo root) is the only registry; YAML frontmatter in `packs/*/SKILL.md` and `packs/*/PACK.yaml` carry per-pack metadata.

**File Storage:**
- Local filesystem only (`packs/`, `docs/`, `sources/`)

**Caching:**
- None

## Authentication & Identity

**Auth Provider:**
- None for the repository/product itself
- `gh` CLI auth is the only credential mechanism (interactive `gh auth login`, not stored in repo)

## Monitoring & Observability

**Error Tracking:**
- None

**Logs:**
- `console`/stdout prints from Python tooling; GitHub Actions annotations (`::error::`) from `.github/workflows/validate.yml`

## CI/CD & Deployment

**Hosting:**
- GitHub Pages serving `docs/` from branch `main` (per `scripts/configure_repo.sh`)

**CI Pipeline:**
- `.github/workflows/validate.yml` — job `content-integrity` on push to `main` and all PRs; `permissions: read-all`; four gates: leak sentinels (assembled fragments like `"CONFI""DENTIAL"`), source-material URL link policy (banned hosts: sebokwiki, nasa.gov, ntrs, nist.gov, govinfo.gov, omg.org, ocw.mit, dodcio, dod.mil, dla.mil, eur-lex, europa.eu, nato.int, dau.edu — exempted inside `kind: signpost` packs), SKILL.md frontmatter lint (kebab-case `name`, non-empty `description`), `catalog.json` JSON validity. Mirrors `tooling/check_release.py`; deliberately self-contained (inline bash + python3 stdlib; never executes checked-out code).

**Releases:**
- `scripts/configure_repo.sh` creates the GitHub Release for `v<version>` from `.claude-plugin/plugin.json`; `tooling/check_release.py` is the local release gate.

**Installers (distribution integration):**
- `install.py` / `install.sh` / `install.ps1` — multi-agent targets defined in the `AGENTS` dict in `install.py`: claude (`~/.claude/skills/`, honours `CLAUDE_CONFIG_DIR`), openclaw (`~/.openclaw/skills/`), copilot (`~/.copilot/skills/`) — native copies; codex (`~/.codex/prompts/<slug>.md`), gemini (`~/.gemini/commands/<ns>/<slug>.toml`), cursor (project-local `.cursor/rules/<slug>.mdc`) — format transforms.

## Environment Configuration

**Required env vars:**
- None required
- Optional: `CLAUDE_CONFIG_DIR` (Claude install target override)

**Secrets location:**
- None in repo; `gh` CLI credential store (outside repo)

## Webhooks & Callbacks

**Incoming:**
- None

**Outgoing:**
- None

---

*Integration audit: 2026-08-14*
