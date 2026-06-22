<!--
Copyright (c) 2026 JG Systems Consulting Ltd. — MIT License (see ../LICENSE).
SPDX-License-Identifier: MIT
-->

# Release-Standard Audit (RR-B + RR-S)

Audit of `jgs-se-knowledge-packs` against the **JGS Release Repo Standard** (Draft 5).

- **Version audited:** 1.3.0 · **Catalogue:** 16 live packs + 2 signposts.
- **Profile:** Base (`RR-B`) + Skills-pack (`RR-S`), including `RR-S-08..15` as MUST
  (new reference-grade pack).
- **Posture:** released **open-source/MIT** (like `jgs-goal-spec`), so the **OSS override**
  applies — the proprietary EULA/office requirements are swapped for MIT, and the community
  files (`CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`) are **added**, not omitted.
- **Mechanical gate:** `python tooling/check_release.py` → PASS.
- **CI gate:** `.github/workflows/validate.yml` (active) — mirrors the mechanical gate.

Status key: ✅ PASS · ⚠️ PARTIAL (path-to-green noted) · 🕓 DEFERRED (publish-time platform
state; file-side artifact ready) · 🔁 N-A (adapted/optional, justified).

## Base — RR-B

| ID | MUST/SHOULD | Status | Notes |
|----|-------------|--------|-------|
| RR-B-00 | MUST | 🔁 | No stager/`releases/` split — repo is authored directly. Self-verify intent met by `tooling/check_release.py` + CI (`validate.yml`). (Adaptation 3.) |
| RR-B-01 | MUST | ✅ | OSS override: root `LICENSE` = MIT, © JG Systems Consulting Ltd. 2026. |
| RR-B-02 | MUST | ✅ | `COPYRIGHT` + `NOTICE` present; `NOTICE` carries per-pack source attributions. |
| RR-B-03 | MUST | ✅ | JGSC + SPDX header on every authored file. **Pack content excluded by design** — it carries the source's licence. (Adaptation 1.) |
| RR-B-04 | MUST | ✅ | `SPDX-License-Identifier: MIT` in every authored-file header. |
| RR-B-05 | MUST | ✅ | README has Install / Usage / Licensing / Support & security headings; no internal URLs. |
| RR-B-06 | MUST | ✅ | Copy-paste install (`python install.py`) + manual clone path. |
| RR-B-07 | MUST | ✅ | `SECURITY.md` + README give `support@jgsystemsconsulting.com`. |
| RR-B-08 | MUST | ✅ | `CHANGELOG.md` (Keep a Changelog); top entry `1.3.0` == plugin.json == RELEASE-INFO. |
| RR-B-09 | MUST | ✅ | SemVer `1.3.0` single-source; `check_release.py` asserts agreement. |
| RR-B-10 | MUST | ✅ | `RELEASE-INFO.txt`: product, version, UTC timestamp, `Tag: v1.3.0` (no internal SHA). |
| RR-B-11 | MUST | ✅ | Governance at root, docs under `docs/`; no scratch/build/`__pycache__` shipped. |
| RR-B-12 | SHOULD | ✅ | OSS override: `CONTRIBUTING.md` + `CODE_OF_CONDUCT.md` added. |
| RR-B-13 | MUST | ✅ | Root `.gitignore` (OS cruft, env, build, `.build/`, `.playwright-mcp/`). |
| RR-B-14 | MUST | ✅ | No secrets/keys/internal IP; `check_release.py` leak scan green. |
| RR-B-15 | MUST | ✅ | `tooling/check_release.py` runs required-files + forbidden-content + version + header checks, exits non-zero on failure. (Adaptation 3.) |
| RR-B-16 | SHOULD | ✅ | README "Install with your AI agent" block; embedded repo URL + version (1.3.0) match RELEASE-INFO. |
| RR-B-17 | MAY | 🔁 | `llms.txt`/`AGENTS.md` not shipped (optional). |
| RR-B-18 | MUST | ✅/🕓 | `v1.2.0` tag applied at prior release; **`v1.3.0` tag to apply at publish** (PR #1 merge). `RELEASE-INFO.txt` records `Tag: v1.3.0`. |
| RR-B-19 | MUST | ✅ | `docs/products/website/01-jgs-se-knowledge-packs.yaml` + `catalog.yaml` (features/positioning, no pricing). |
| RR-B-20 | MUST | ✅/🕓 | `docs/index.html` + `docs/.nojekyll` present, self-contained, brand-compliant. **Pages enablement** deferred to publish via `scripts/configure_repo.sh`. |
| RR-B-21 | MUST | 🕓 | About description/homepage/topics applied at publish by `scripts/configure_repo.sh` (13 topics incl. product-class + agent tags). |
| RR-B-22 | MUST | 🕓 | GitHub Release for `v1.3.0` created at publish by `scripts/configure_repo.sh` (notes from CHANGELOG). |
| RR-B-23 | SHOULD | 🕓 | Branch protection (PR + `content-integrity` CI, no force-push/delete) applied at publish by `scripts/configure_repo.sh`. |
| RR-B-24 | MUST(new) | ✅ | Landing page matches the JGS design system (tokens, self-host `@font-face`, `§NN`, square corners, `gap:1px` grid, ghosted numerals, paper/ghost buttons, drafting sheet). Designed per `ui-ux-pro-max` rules; **Playwright MCP screenshots captured at desktop 1280 + mobile 390** (`.playwright-mcp/landing-desktop-1280.png`, `…/landing-mobile-390.png`); no emoji; `:focus-visible` + `prefers-reduced-motion` present; content claims cross-checked (16 packs, agent list == `install.py --list-agents`, REV 1.3.0). |
| RR-B-25 | MUST | ✅/🕓 | Relative links + anchors resolve; README/docs links checked. Published `blob/main`/Pages deep links re-checked after publish (per the publish-time note). |
| RR-B-26 | SHOULD | ✅ | Docs use GFM tables + `> [!IMPORTANT]` callouts (`docs/other-agents.md`); no ASCII diagrams. No multi-step flow currently warrants a Mermaid diagram; add one if a pipeline doc is introduced. |

## Skills-pack — RR-S

| ID | MUST/SHOULD | Status | Notes |
|----|-------------|--------|-------|
| RR-S-01 | MUST | ✅ | Every `packs/<slug>/SKILL.md` has `name` + `description`. (Adaptation 4 — packs under `packs/`.) |
| RR-S-02 | MUST | ✅ | `install.py` + `install.sh` + `install.ps1`, all support `--dry-run`. |
| RR-S-03 | MUST | ✅ | Default target `~/.claude/skills/jgs-se-knowledge-packs/`; honours `$CLAUDE_CONFIG_DIR`; `--flat` documented. |
| RR-S-04 | MUST | ✅ | `SKILLS.md` index; entry count == shipped packs (16). |
| RR-S-05 | MUST | ✅ | `docs/skill-usage.md` present. |
| RR-S-06 | SHOULD | ✅ | Pack slugs are source-named (documented exception); vendor namespace at install-target level. (Adaptation 5.) |
| RR-S-07 | MAY | 🔁 | No MCP-bridge tool reference (packs don't orchestrate a bridge). |
| RR-S-08 | MUST | ✅ | `.claude-plugin/marketplace.json` + `plugin.json`; JSON parses; `version` = 1.3.0. |
| RR-S-09 | MUST | ✅ | README badge cluster (license, version, packs, tested-with-Claude-Code). |
| RR-S-10 | MUST | ✅ | Standalone `SECURITY.md` with private reporting address + response-time; no bug-bounty. |
| RR-S-11 | MUST | ✅/🕓 | Version single-source (1.3.0) PASS; `v1.3.0` git tag applied at publish (PR #1 merge). |
| RR-S-12 | MUST | ✅ | `.github/workflows/validate.yml` **active**: `permissions: read-all`, push + pull_request, inline bash + python3 stdlib, no repo-code execution, leak-sentinel + link-policy (signpost-aware) + frontmatter lint + catalog check; neutral step names. |
| RR-S-13 | MUST | ✅ | Each pack `SKILL.md` has a literal `## When to use` heading + `Prerequisites` marker. |
| RR-S-14 | MUST | ✅ | Frontmatter conforms to agentskills.io: `name` kebab-case matching dir + non-empty `description`. |
| RR-S-15 | MUST | ✅ | `install.py` exposes `--agent`/`--list-agents`; native (claude/openclaw/copilot) + transform (codex prompt, gemini TOML, cursor `.mdc`); `--agent all` for user-global; defaults to Claude Code; `--dry-run` shows per-agent targets. README "Use with other agents" + `docs/other-agents.md` document it. |

## §5 Release-readiness checklist

1. Self-verify gate runs clean — ✅ `check_release.py` → PASS.
2. All applicable `RR-B-*` MUSTs — ✅ (publish-time RR-B-20..23 staged in `configure_repo.sh`).
3. All `RR-S-*` MUSTs — ✅ (RR-S-12 CI active; RR-S-15 multi-agent install shipped).
4. Leak checks — ✅ no forbidden paths/content; required files + headers present.
5. Version agreement — ✅ 1.3.0 across plugin.json / CHANGELOG / RELEASE-INFO.
6. Agent-install prompt present + accurate — ✅ (RR-B-16).
7. Multi-agent install (RR-S-15) — ✅ `--agent`/`--list-agents`; dry-run lists per-agent targets.
8. Landing page (RR-B-20/24) — ✅ file-side; Pages enablement at publish.
9. Link integrity (RR-B-25) — ✅ file-side; re-run against published Pages/`blob/main` after publish.
10. Documentation presentation (RR-B-26) — ✅ callouts/tables; no ASCII diagrams.
11. Human spot-check of README tone / working install / no internal URLs — ✅.

## Adaptations (flagged, see also the README)

1. **RR-B-03 headers** — JGSC headers on authored files only; pack content carries the source licence.
2. **RR-B-01/02** — OSS override (MIT tooling; `NOTICE` carries per-pack source attributions).
3. **RR-B-00/15** — no stager; direct-authored; `check_release.py` + `validate.yml` are the self-verify gates.
4. **RR-S-01/02/03** — skills under `packs/`; install target `~/.claude/skills/jgs-se-knowledge-packs/`.
5. **RR-S-06** — source-named pack slugs (documented exception); vendor namespace at target level.
6. **Signpost link exemption** — `kind: signpost` packs cite source URLs (citation, not redistribution);
   both `check_release.py` and `validate.yml` exempt them from the source-link ban.

## Remaining items — apply at PUBLIC publish

The repo is private; these are GitHub **platform state** (not tracked files) and are applied by the
checked-in, idempotent `scripts/configure_repo.sh` once the v1.3.0 PR merges and the repo goes public:

- **RR-B-18 / RR-S-11** — apply the `v1.3.0` git tag.
- **RR-B-20** — enable GitHub Pages (`main:/docs`); drop the brand woff2 into `docs/fonts/` (page
  degrades gracefully to the system font stack until then).
- **RR-B-21** — set About description / homepage / topics.
- **RR-B-22** — publish the `v1.3.0` GitHub Release (notes from CHANGELOG).
- **RR-B-23** — enable branch protection (PR + `content-integrity` CI; no force-push/delete).
- **RR-B-25** — re-run the link check against the live Pages + `blob/main` URLs.

Run `scripts/configure_repo.sh --dry-run` to preview, then `scripts/configure_repo.sh` to apply.
Re-run `python tooling/check_release.py` after any change.
