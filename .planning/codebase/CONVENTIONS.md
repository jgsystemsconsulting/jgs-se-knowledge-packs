# Coding Conventions

**Analysis Date:** 2026-08-14

## Repository Character

This is primarily a **content repository** (50 Markdown knowledge packs under `packs/`)
with a small amount of Python/JavaScript tooling under `tooling/`. Conventions split into
(1) tooling code conventions and (2) pack content conventions enforced by
`docs/PACK-SPEC.md` and CI.

## Naming Patterns

**Files (tooling):**
- Python: `snake_case.py` — e.g. `tooling/validate_pack.py`, `tooling/build_pack.py`, `tooling/check_release.py`, `tooling/gen_packs_page.py`
- JavaScript: kebab/dot-case — e.g. `tooling/build_all_packs.workflow.js`
- Scripts are executable with shebang `#!/usr/bin/env python3` (Python) or run via `Workflow({scriptPath: ...})` (JS)

**Files (packs):**
- Chapters: `chapters/chNN-<topic-slug>.md` (zero-padded two-digit number), e.g. `packs/dau-se-guidebook/chapters/ch04-technical-management-processes.md`
- Fixed names per pack: `SKILL.md`, `PACK.yaml`, `LICENSE`, plus optional `glossary.md`, `patterns.md`, `cheatsheet.md`
- Pack folders and frontmatter `name` MUST be kebab-case matching regex `[a-z0-9]+(-[a-z0-9]+)*` — enforced by CI (`.github/workflows/validate.yml`)

**Functions:**
- `snake_case` in Python; `check_pack`, `parse_simple_yaml`, `deslop`
- Functions returning validation results return `list[str]` of error strings (empty = pass)

**Variables:**
- `snake_case` Python; `SCREAMING_SNAKE` module constants (e.g. `REQUIRED_PACK_FIELDS`, `VALID_TIERS`, `SOURCE_HOSTS`, `LEAK_SENTINELS` in `tooling/check_release.py`)

## Code Style

**Formatting:**
- Python tooling follows ruff-compatible style (`.ruff_cache/` present; ruff is the de facto formatter/linter even though no `pyproject.toml` is committed)
- `from __future__ import annotations` at top of Python modules
- Type hints used (`dict[str, str]`, `list[str]`, `Path`)

**Linting:**
- Ruff (cache present at `.ruff_cache/`); no committed config file — defaults assumed
- Content "lint" is done by `tooling/validate_pack.py` and CI frontmatter lint, not a code linter

## Mandatory File Headers

Every JGSC-authored tooling/config file starts with the copyright + SPDX block (RR-B-03/04, checked by `tooling/check_release.py`):

```python
#!/usr/bin/env python3
# Copyright (c) 2026 JG Systems Consulting Ltd. — MIT License (see LICENSE).
# SPDX-License-Identifier: MIT
```

```javascript
/*
 * Copyright (c) 2026 JG Systems Consulting Ltd. — MIT License (see ../LICENSE).
 * SPDX-License-Identifier: MIT
 */
```

Markdown docs use the HTML comment form:
```markdown
<!--
Copyright (c) 2026 JG Systems Consulting Ltd. MIT License (see LICENSE).
SPDX-License-Identifier: MIT
-->
```
Pack content files do NOT carry this header (they carry the source's licence).

## Import Organization

- Python: stdlib only (`re`, `sys`, `json`, `argparse`, `pathlib.Path`). **No third-party dependencies in any tooling script.** Even YAML is parsed with a minimal hand-rolled parser (`parse_simple_yaml` in `tooling/validate_pack.py`) to avoid a PyYAML dependency.
- Order: `from __future__ import annotations`, then blank line, then stdlib imports

## Error Handling

**Patterns:**
- Validation scripts collect errors into a list and print each with `::error file=...::` (GitHub Actions annotation format) or plain text, then `sys.exit(1)` on any failure — fail-closed
- Exit codes: 0 = pass, 1 = at least one failure (documented in module docstrings)
- The release gate `tooling/check_release.py` aggregates all mechanical checks and exits non-zero on any failure
- CI workflow (`.github/workflows/validate.yml`) is deliberately self-contained: it inlines its checks and **never executes checked-out repository code** (security boundary vs the local `check_release.py`, which is trusted)

## Comments

**When to Comment:**
- Every tooling module has a substantial docstring header: purpose, numbered checks performed, usage line
- Inline comments cite governance rule IDs: `# RR-S-12 CI quality gate`, `# (RR-B-28)` em-dash stripping, `# RR-B-00` no-drift
- `TODO:` markers in scaffolded `PACK.yaml`/`LICENSE` stubs (from `tooling/build_pack.py`) flag required manual provenance steps

## Tooling Design Patterns

**Deterministic vs judgement split** (`tooling/build_pack.py`):
- Licence vetting, scaffolding, validation are deterministic scripts
- Content synthesis (extraction, chapter generation) is delegated to an agent following `docs/PACK-SPEC.md`

**Single-source + regeneration (RR-B-00):**
- `SKILLS.md` is the source table; `docs/packs.html` is regenerated from it by `tooling/gen_packs_page.py` after any change
- Version single-sourcing: `plugin.json` == `CHANGELOG.md` top == `RELEASE-INFO.txt` (checked by `tooling/check_release.py`)

**Leak-sentinel self-exemption:** sentinels assembled from fragments (`"CONFI" + "DENTIAL"`, `"PRIVATE" + " KEY"`) so scanner files do not flag themselves — replicate this in any new scanning code.

**Em-dash ban in generated UI copy (RR-B-28):** `deslop()` in `tooling/gen_packs_page.py` replaces ` — ` with `, ` in emitted HTML.

## Content Conventions (packs)

Per `docs/PACK-SPEC.md`:
- `SKILL.md`: YAML frontmatter (`name`, `description`); body order: `## How to Use This Skill`, `## Core Frameworks & Mental Models` (~2,000 tokens), `## Chapter Index`, `## Topic Index`, `## Supporting Files`, `## Scope & Limits`. Keep body < ~4,000 tokens (hosts truncate from the end).
- `description` must state coverage AND scope limits honestly
- Chapters follow structure: `Core Idea`, `Frameworks Introduced`, `Key Concepts`, `Mental Models`, `Anti-patterns`, `Key Takeaways`, `Connects To`
- `PACK.yaml` mandatory fields: `slug`, `title`, `publisher`, `license`, `license_tier` (1|2|3), `commercial_use`
- **No source-material URLs anywhere** except inside `kind: signpost` packs (link policy, `docs/LICENSING.md`); enforced in CI and `tooling/check_release.py`
- Synthesize, never copy long verbatim passages (quality + licence-safety rule)
- PRs: one pack per PR; source, version, licence, tier, and not-Excluded confirmation in the description

---

*Convention analysis: 2026-08-14*
