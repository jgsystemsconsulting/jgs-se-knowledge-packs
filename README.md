<!--
Copyright (c) 2026 JG Systems Consulting Ltd. — MIT License (see LICENSE).
SPDX-License-Identifier: MIT
-->

<h1 align="center">jgs-se-knowledge-packs</h1>

<p align="center">
  <img src="https://img.shields.io/badge/license-MIT%20(tooling)-blue" alt="License: MIT (tooling)">
  <img src="https://img.shields.io/badge/version-1.4.0-green" alt="Version 1.4.0">
  <img src="https://img.shields.io/badge/packs-19-blueviolet" alt="19 packs">
  <img src="https://img.shields.io/badge/tested%20with-Claude%20Code-8A2BE2" alt="Tested with Claude Code">
  <img src="https://img.shields.io/badge/scope-systems%20engineering-orange" alt="Scope: systems engineering">
</p>

<p align="center">
  <strong>Installable knowledge-pack skills for coding agents, reconstructed from genuinely
  open systems-engineering bodies of knowledge — vetted, attributed, and shareable by
  construction.</strong>
</p>

**Copyright (c) 2026 JG Systems Consulting Ltd. — MIT License (tooling); pack content under each source's own licence (see [NOTICE](NOTICE)).**

---

## What it is / who it's for

A great body of knowledge — SEBoK, the NASA SE Handbook, a modelling spec — is something you
read once and then can't recall when you need it mid-task. A **knowledge pack** turns it into a
skill your coding agent loads on demand: ask `/sebok systems of systems` and the agent reads the
right chapter and answers from reconstructed reference notes, not a hazy recollection.

This is a curated catalogue of those packs for **systems engineers**, built to one rule that makes
it different from "point a tool at a PDF":

> **Only genuinely open sources go in.** Public-domain (NASA, DoD) and open-licensed (SEBoK, OMG
> specs, CC content) — never paywalled or all-rights-reserved material. Eligibility is enforced,
> not assumed (see [docs/SOURCE-VETTING.md](docs/SOURCE-VETTING.md)), and every pack is
> redistributable by construction (see [docs/LICENSING.md](docs/LICENSING.md)).

Packs follow the open [Agent Skills](https://github.com/agentskills/agentskills) `SKILL.md`
standard, so they load in Claude Code, GitHub Copilot CLI, and Amp without modification.

## Prerequisites

- Python 3.9+ (for the installer and pack validator).
- A host that reads Agent Skills (Claude Code, GitHub Copilot CLI, or Amp).
- No MCP server, API key, or licence tier is needed at runtime — packs are plain Markdown.

## Install with your AI agent

Copy the block below into your coding agent (Claude Code, Cursor, etc.). It will read this repo
and install the catalogue for you.

```text
You are installing jgs-se-knowledge-packs, an open catalogue (MIT tooling) of
systems-engineering knowledge-pack skills by JG Systems Consulting Ltd.
Repository: https://github.com/jgsystemsconsulting/jgs-se-knowledge-packs (version 1.4.0).
Do this in order:
1. Read README.md, docs/skill-usage.md, and CHANGELOG.md so you understand what you are
   installing. There are NO external prerequisites — packs are plain Markdown skills.
2. Run `python install.py --dry-run` and show me the pack list and target
   (~/.claude/skills/jgs-se-knowledge-packs/). If it looks right, run `python install.py`.
3. Verify: list the installed packs under the target and confirm the count matches SKILLS.md.
4. Tell me to restart Claude Code, then try `/sebok systems of systems`.
5. Pack CONTENT is under each source's own licence (see NOTICE) — keep attribution intact.
```

## Install manually

```bash
git clone https://github.com/jgsystemsconsulting/jgs-se-knowledge-packs.git
cd jgs-se-knowledge-packs
python install.py --dry-run     # preview packs + target
python install.py               # installs to ~/.claude/skills/jgs-se-knowledge-packs/
```

Default target is the vendor-namespaced `~/.claude/skills/jgs-se-knowledge-packs/` (honours
`$CLAUDE_CONFIG_DIR`). For a flat install (each pack directly under `~/.claude/skills/`), pass
`--flat`. Restart your agent, then invoke a pack by its slug.

## Use with other agents

The packs are open [Agent Skills](https://agentskills.io); `install.py` installs them into
agents beyond Claude Code — natively where the agent reads the format, or via a format
transform where it doesn't.

```bash
python install.py --list-agents     # show every supported agent + its target
python install.py --agent openclaw  # OpenClaw / Copilot CLI — native (full pack)
python install.py --agent codex     # Codex / Gemini / Cursor — transform (SKILL.md index)
python install.py --agent all       # all user-global agents at once
```

| Agent | Format | Target |
|-------|--------|--------|
| Claude Code (default) · OpenClaw · GitHub Copilot CLI | native folder | `~/.<agent>/skills/jgs-se-knowledge-packs/<slug>/` |
| OpenAI Codex CLI | prompt | `~/.codex/prompts/<slug>.md` |
| Gemini CLI | TOML command | `~/.gemini/commands/jgs-se-knowledge-packs/<slug>.toml` |
| Cursor | project rule | `./.cursor/rules/<slug>.mdc` |

Native agents get the whole pack (chapters + progressive disclosure); transform agents get the
always-loaded `SKILL.md` index inlined into one file. Full detail and the per-agent limitations:
[docs/other-agents.md](docs/other-agents.md).

## Catalogue

| Pack | Source | Licence | Tier | Status |
|------|--------|---------|------|--------|
| `sebok` | Guide to the SE Body of Knowledge v2.13 | CC BY-NC-SA 3.0 | 🟡 2 | ✅ live (41 chapters) |
| `nasa-se-handbook` | NASA Systems Engineering Handbook | Public domain (US gov) | 🟢 1 | ✅ live (34 chapters) |
| `nasa-npr-7123` | NASA NPR 7123.1D — SE Processes & Requirements | Public domain (US gov) | 🟢 1 | ✅ live (9 chapters) |
| `nasa-risk` | NASA Risk Management Handbook | Public domain (US gov) | 🟢 1 | ✅ live (10 chapters) |
| `nasa-system-safety` | NASA System Safety Handbook v2 | Public domain (US gov) | 🟢 1 | ✅ live (7 chapters) |
| `nasa-hsi` | NASA Human Systems Integration Guide | Public domain (US gov) | 🟢 1 | ✅ live (9 chapters) |
| `nist-ai-rmf` | NIST AI Risk Management Framework 1.0 | Public domain (US gov) | 🟢 1 | ✅ live (8 chapters) |
| `nist-ssdf` | NIST Secure Software Development Framework 1.1 | Public domain (US gov) | 🟢 1 | ✅ live (5 chapters) |
| `nist-csf` | NIST Cybersecurity Framework 2.0 | Public domain (US gov) | 🟢 1 | ✅ live (8 chapters) |
| `nist-sse` | NIST SP 800-160 Vol 1+2 — Systems Security Engineering | Public domain (US gov) | 🟢 1 | ✅ live (8 chapters) |
| `nist-800-37` | NIST SP 800-37 Rev 2 — Risk Management Framework | Public domain (US gov) | 🟢 1 | ✅ live (7 chapters) |
| `nist-cps` | NIST Framework for Cyber-Physical Systems (SP 1500-201/202/203) | Public domain (US gov) | 🟢 1 | ✅ live (8 chapters) |
| `digital-systems-engineering` | Towards Digital Engineering (ODU, arXiv:2002.11672) | CC BY 4.0 | 🟡 2 | ✅ live (7 chapters) |
| `mil-std-882` | MIL-STD-882E — DoD System Safety | Public domain (US gov) | 🟢 1 | ✅ live (8 chapters) |
| `requirements-writing` | Requirements writing — EARS & quality (original guidance) | CC BY 4.0 | 🟡 2 | ✅ live (6 chapters) |
| `dau-se-guidebook` | DoD Systems Engineering Guidebook (OUSD R&E) | Public domain (US gov) | 🟢 1 | ✅ live (6 chapters) |
| `gao-tra` | GAO Technology Readiness Assessment Guide (GAO-20-48G) | Public domain (US gov) | 🟢 1 | ✅ live (7 chapters) |
| `dodaf` | DoD Architecture Framework 2.02 Vol II | Public domain (US gov) | 🟢 1 | ✅ live (11 chapters) |
| `eu-ai-act` | EU Artificial Intelligence Act (Reg 2024/1689) | EU OJ (reproducible) | 🟡 2 | ✅ live (12 chapters) |
| `mit-ocw-se` | MIT OCW Fundamentals of Systems Engineering | CC BY-NC-SA | 🟡 2 | 🔜 planned |

Machine-readable index: [SKILLS.md](SKILLS.md) · [catalog.json](catalog.json).

**Signposts** (citation-only, not packs — zero reproduced content): `omg-signpost` points to
the OMG modelling specs; `se-standards-signpost` maps the whole SE standards landscape
(ISO/IEC/IEEE, INCOSE, SAE/EIA, ECSS, NATO, CMMI, NIST SP 800-160…) with each standard's
owner, whether it can be packaged, and where to get it. They exist because most SE standards
are paywalled or all-rights-reserved (see [docs/SOURCE-VETTING.md](docs/SOURCE-VETTING.md)).

## Usage

```bash
/sebok                      # load core frameworks for reference
/sebok systems of systems   # routes to the right chapter, answers from the pack
/sebok ch20                 # load a specific chapter
```

Each pack ships an always-loaded `SKILL.md` index plus on-demand `chapters/`, a glossary,
patterns, and a cheatsheet. Full guidance: [docs/skill-usage.md](docs/skill-usage.md).

## How a pack is built

Vet the source (tier + licence, not on the Excluded list) → extract text (built on the
MIT-licensed [`book-to-skill`](https://github.com/virgiliojr94/book-to-skill) engine) → map
structure to chapter offsets → generate reference-depth chapters in parallel + glossary /
patterns / cheatsheet + the `SKILL.md` index → attach provenance (`PACK.yaml` + a `LICENSE`
reproducing the source's terms) → validate. Contract: [docs/PACK-SPEC.md](docs/PACK-SPEC.md).
Contributing: [CONTRIBUTING.md](CONTRIBUTING.md).

## Licensing

Two separable layers:

- **Tooling & scaffolding:** [MIT](LICENSE) (JG Systems Consulting Ltd.).
- **Pack content:** each pack carries its **source's** licence in `packs/<slug>/LICENSE`,
  independent of the repo MIT licence. A CC BY-NC-SA source yields a CC BY-NC-SA pack.

Per-pack source attributions are in [NOTICE](NOTICE). Why every pack is lawful to reconstitute
and redistribute — including why no source-material links are published — is set out in
[docs/LICENSING.md](docs/LICENSING.md).

## Support & security

- **Help / questions:** open an issue, or contact `support@jgsystemsconsulting.com`.
- **Security / licensing concerns:** see [SECURITY.md](SECURITY.md) — report privately to
  `support@jgsystemsconsulting.com`.

## Version

See [CHANGELOG.md](CHANGELOG.md). Current: 1.4.0.
