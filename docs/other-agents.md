<!--
Copyright (c) 2026 JG Systems Consulting Ltd. — MIT License (see ../LICENSE).
SPDX-License-Identifier: MIT
-->

# Using the packs with other agents

The packs follow the open [Agent Skills](https://agentskills.io) `SKILL.md` format. Some
agents read that format **natively** (the pack folder is copied unchanged, with full
on-demand chapter loading); others need a **format transform** into their own prompt, command,
or rule convention (the always-loaded `SKILL.md` index is inlined into a single file).

`install.py` handles both. Pick an agent with `--agent`, preview with `--dry-run`, and list
everything with `--list-agents`.

```bash
python install.py --list-agents        # show every agent + its target
python install.py --agent openclaw     # install for one agent
python install.py --agent all          # install for all user-global agents
python install.py --agent codex --dry-run   # preview a transform install
```

## Per-agent targets

| Agent | `--agent` | Format | Target |
|-------|-----------|--------|--------|
| Claude Code | `claude` (default) | native (folder) | `~/.claude/skills/jgs-se-knowledge-packs/<slug>/` — honours `$CLAUDE_CONFIG_DIR` |
| OpenClaw | `openclaw` | native (folder) | `~/.openclaw/skills/jgs-se-knowledge-packs/<slug>/` |
| GitHub Copilot CLI | `copilot` | native (folder) | `~/.copilot/skills/jgs-se-knowledge-packs/<slug>/` |
| OpenAI Codex CLI | `codex` | transform (prompt) | `~/.codex/prompts/<slug>.md` |
| Gemini CLI | `gemini` | transform (TOML command) | `~/.gemini/commands/jgs-se-knowledge-packs/<slug>.toml` |
| Cursor | `cursor` | transform (project rule) | `./.cursor/rules/<slug>.mdc` (project-local) |

`--agent all` covers the five **user-global** agents (claude, openclaw, copilot, codex, gemini).
Cursor is **project-local** — its rules install into the current repo's `.cursor/rules/`, so run
it explicitly per project (`python install.py --agent cursor`); it is excluded from `--agent all`.

## Native vs. transform — what differs

> [!IMPORTANT]
> **Native** agents get the whole pack — `SKILL.md` plus `chapters/`, `glossary.md`,
> `patterns.md`, `cheatsheet.md` — with **progressive disclosure**: the agent loads only the
> one chapter your question routes to. This is the full experience.
>
> **Transform** agents get the always-loaded `SKILL.md` **index only**, inlined into a single
> prompt/command/rule file. That index carries each pack's core frameworks, the chapter map,
> and the topic routing — enough to answer most questions — but the on-demand `chapters/` are a
> Claude-native progressive-disclosure feature and are **not** bundled into the single-file form
> (it would bloat every prompt). For deep, chapter-level depth on a transform agent, consult the
> source body of knowledge the pack names, or use a native agent.

Each transformed file carries a one-line provenance comment noting it was generated from the
agentskills.io `SKILL.md` and pointing back here.

## Notes

- **Flat install** (`--flat`) drops the `jgs-se-knowledge-packs/` vendor namespace for native
  agents, installing each pack directly under the agent's skills dir. Transform agents are
  unaffected (Codex prompts are already top-level; Gemini keeps the namespace as a command group).
- **Custom target** (`--target DIR`) overrides the destination for a single agent (not valid with
  `--agent all`).
- No third-party dependencies — the installer is stdlib-only Python.
