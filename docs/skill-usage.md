<!--
Copyright (c) 2026 JG Systems Consulting Ltd. — MIT License (see ../LICENSE).
SPDX-License-Identifier: MIT
-->

# Using the knowledge packs

## Prerequisites

- A host that reads [Agent Skills](https://github.com/agentskills/agentskills): Claude Code,
  GitHub Copilot CLI, or Amp.
- Packs installed into your skills directory (see the repo README — `python install.py`).
- No MCP server, API key, or licence tier is needed at runtime; packs are plain Markdown.

## Invoking a pack

Each pack is a skill named by its slug. After installing and restarting your agent:

```bash
/sebok                      # no argument — load the pack's core frameworks for reference
/sebok systems of systems   # a topic — the pack routes to the right chapter and answers
/sebok ch20                 # a chapter id — load that chapter directly
/sebok what chapters do you have?   # browse the index
```

In normal conversation you often don't need the slash at all: each pack's `description`
makes the agent load it when your question matches its topics (e.g. "what does SEBoK say
about traceability?").

## How a pack answers

A pack uses progressive disclosure so a large source doesn't fill your context window:

- `SKILL.md` (always loaded) holds the core frameworks plus a **topic index** and **chapter
  index**.
- `chapters/chNN-*.md` are loaded **on demand** — only the chapter your question routes to.
- `glossary.md`, `patterns.md`, `cheatsheet.md` are loaded when relevant.

So the agent reads `SKILL.md`, decides which one chapter answers your question, and loads
just that.

## Scope & honesty

Each pack's `SKILL.md` states what its source is **thin** on. Knowledge packs are reference
oracles over one source — best for "what does this body of knowledge say about X?" and
"give me X's framework for Y." They are not a substitute for your own judgement, and they
only know their one source.

## Licensing reminder

Pack **content** is licensed under its source's own terms (see each `packs/<slug>/LICENSE`
and the root `NOTICE`). Non-commercial (NC) packs may not be used for commercial purposes;
share-alike (SA) packs must keep their licence on any derivative. The repository **tooling**
is MIT. See [LICENSING.md](LICENSING.md).
