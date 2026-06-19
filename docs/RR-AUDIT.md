<!--
Copyright (c) 2026 JG Systems Consulting Ltd. — MIT License (see ../LICENSE).
SPDX-License-Identifier: MIT
-->

# Release-Standard Audit (RR-B + RR-S)

Audit of `jgs-se-knowledge-packs` against the **JGS Release Repo Standard**.

- **Profile:** Base (`RR-B`) + Skills-pack (`RR-S`), including `RR-S-08..14` as MUST
  (new reference-grade pack).
- **Posture:** released **open-source/MIT** (like `jgs-goal-spec`), so the **OSS override**
  applies — the proprietary EULA/office requirements are swapped for MIT, and the community
  files (`CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`) are **added**, not omitted.
- **Mechanical gate:** `python tooling/check_release.py` → PASS.

Status key: ✅ PASS · ⚠️ PARTIAL (path-to-green noted) · 🔁 N-A (adapted/optional, justified).

## Base — RR-B

| ID | MUST/SHOULD | Status | Notes |
|----|-------------|--------|-------|
| RR-B-00 | MUST | 🔁 | No stager/`releases/` split — repo is authored directly. Self-verify intent met by `tooling/check_release.py` + CI. (Adaptation 3.) |
| RR-B-01 | MUST | ✅ | OSS override: root `LICENSE` = MIT, © JG Systems Consulting Ltd. 2026. |
| RR-B-02 | MUST | ✅ | `COPYRIGHT` + `NOTICE` present, name JG Systems Consulting Ltd.; `NOTICE` carries per-pack source attributions. |
| RR-B-03 | MUST | ✅ | JGSC + SPDX header on every authored file (README, docs, tooling, installers). **Pack content excluded by design** — it carries the source's licence, not a JGSC header. (Adaptation 1.) |
| RR-B-04 | MUST | ✅ | `SPDX-License-Identifier: MIT` in every authored-file header. |
| RR-B-05 | MUST | ✅ | README has Install / Usage / Licensing / Support & security headings; no internal URLs. |
| RR-B-06 | MUST | ✅ | Copy-paste install (`python install.py`) + manual clone path. |
| RR-B-07 | MUST | ✅ | `SECURITY.md` + README give `support@jgsystemsconsulting.com`. |
| RR-B-08 | MUST | ✅ | `CHANGELOG.md` (Keep a Changelog); top entry `1.1.0` == plugin.json == RELEASE-INFO. |
| RR-B-09 | MUST | ✅ | SemVer `1.1.0` single-source; `check_release.py` asserts agreement. |
| RR-B-10 | MUST | ✅ | `RELEASE-INFO.txt`: product, version, UTC timestamp, `Tag: v1.1.0` (no internal SHA — public-repo rule). |
| RR-B-11 | MUST | ✅ | Governance at root, docs under `docs/`; no scratch/build/`__pycache__` shipped. |
| RR-B-12 | SHOULD | ✅ | OSS override: `CONTRIBUTING.md` + `CODE_OF_CONDUCT.md` **added** (flipped from proprietary out-of-scope). |
| RR-B-13 | MUST | ✅ | Root `.gitignore` (OS cruft, env, build, `.build/`, raw `full_text.txt`). |
| RR-B-14 | MUST | ✅ | No secrets/keys/internal IP; `check_release.py` leak scan green. |
| RR-B-15 | MUST | ✅ | `tooling/check_release.py` runs required-files + forbidden-content + version + header checks, exits non-zero on failure. (Adaptation 3 — standalone gate, not embedded in a stager.) |
| RR-B-16 | SHOULD | ✅ | README "Install with your AI agent" block; embedded repo URL + version (1.1.0) match RELEASE-INFO; command matches installer. |
| RR-B-17 | MAY | 🔁 | `llms.txt`/`AGENTS.md` not shipped (optional). |

## Skills-pack — RR-S

| ID | MUST/SHOULD | Status | Notes |
|----|-------------|--------|-------|
| RR-S-01 | MUST | ✅ | Every `packs/<slug>/SKILL.md` has `name` + `description` frontmatter. (Adaptation 4 — packs live under `packs/`, not `skills/`.) |
| RR-S-02 | MUST | ✅ | `install.py` (canonical) + `install.sh` + `install.ps1`, all support `--dry-run`. |
| RR-S-03 | MUST | ✅ | Default target `~/.claude/skills/jgs-se-knowledge-packs/` (vendor-namespaced), honours `$CLAUDE_CONFIG_DIR`; `--flat` fallback documented in README. |
| RR-S-04 | MUST | ✅ | `SKILLS.md` index; entry count == shipped packs (regenerated at release). |
| RR-S-05 | MUST | ✅ | `docs/skill-usage.md` present. |
| RR-S-06 | SHOULD | ✅ | Pack slugs are **source-named** (`sebok`, `nasa-se-handbook`…) — deliberate, documented exception; vendor namespace is at install-target level. (Adaptation 5.) |
| RR-S-07 | MAY | 🔁 | No MCP-bridge tool reference (packs don't orchestrate a bridge). |
| RR-S-08 | MUST | ✅ | `.claude-plugin/marketplace.json` + `plugin.json`; JSON parses; `version` = 1.1.0. |
| RR-S-09 | MUST | ✅ | README badge cluster (license, version, packs, tested-with-Claude-Code). |
| RR-S-10 | MUST | ✅ | Standalone `SECURITY.md` with private reporting address + response-time; no bug-bounty. |
| RR-S-11 | MUST | ✅ | Version single-source (1.1.0) PASS; git tag `v1.1.0` applied at the v1.1.0 release commit. |
| RR-S-12 | MUST | ⚠️ | `.github/workflows/validate.yml` authored to spec (`permissions: read-all`, push + pull_request, inline bash + python3 stdlib, no repo-code execution, sentinel scan + frontmatter lint, neutral step names). **Path-to-green:** shipped as `validate.yml.disabled`; activate with `gh auth refresh -h github.com -s workflow` then rename to `validate.yml` (OAuth workflow scope can't be granted non-interactively). |
| RR-S-13 | MUST | ✅ | Each pack `SKILL.md` has a literal `## When to use` heading + a `Prerequisites` marker. |
| RR-S-14 | MUST | ✅ | Frontmatter conforms to agentskills.io: `name` kebab-case matching dir + non-empty `description`. |

## §5 Release-readiness checklist

1. Self-verify gate runs clean — ✅ `check_release.py` → PASS.
2. All applicable `RR-B-*` MUSTs — ✅ (RR-B-00/15 satisfied by adaptation).
3. All `RR-S-*` MUSTs — ✅ (RR-S-11 git tag `v1.1.0` applied at release). RR-S-12 (CI activation) — ⚠️ pending the workflow OAuth scope.
4. Leak checks — ✅ no forbidden paths/content; required files + headers present.
5. Version agreement — ✅ 1.1.0 across plugin.json / CHANGELOG / RELEASE-INFO.
6. Agent-install prompt present + accurate — ✅ (RR-B-16).
7. Human spot-check of README tone / working install / no internal URLs — ✅.

## Multi-pack catalogue adaptations (flagged, see also the README)

1. **RR-B-03 headers** — JGSC headers on authored files only; pack content carries the source licence.
2. **RR-B-01/02** — OSS override (MIT tooling; `NOTICE` carries per-pack source attributions).
3. **RR-B-00/15** — no stager; direct-authored; `check_release.py` is the self-verify gate.
4. **RR-S-01/02/03** — skills under `packs/`; install target `~/.claude/skills/jgs-se-knowledge-packs/`.
5. **RR-S-06** — source-named pack slugs (documented exception); vendor namespace at target level.
6. **RR-S-13** — `## When to use` + prerequisites added to each pack `SKILL.md`.

## Residual item before PUBLIC release

The repo is private at v1.1.0 (tagged). One item remains before flipping public:

- **RR-S-12** — grant the workflow OAuth scope (`gh auth refresh -h github.com -s workflow`)
  and activate `validate.yml` (rename from `.disabled`). The checks already pass locally via
  `tooling/check_release.py`; this only switches on the automated CI gate.

Everything else is ✅. Re-run `python tooling/check_release.py` after any change.
