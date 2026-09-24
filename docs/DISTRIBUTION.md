# Distribution ledger

Status vocabulary per RR-B-36: submitted / in progress / deferred / deliberate N-A /
planned. Every row carries its decision and date. Revisit at every release. Channel
mechanics were verified against live sites on 2026-09-24; re-verify a row before
acting on it.

| Channel | Status | Decision and date |
|---|---|---|
| skills.sh | in progress | Auto-indexed since 2026-09-08. Coverage partial on 2026-09-24 (`sebok`, `dod-digital-engineering`, `nasa-systems-modeling`, `omg-signpost` observed of 63 packs): the skills CLI's well-known containers do not include `packs/`, so indexing falls back to a partial recursive crawl. Interim fix shipped 2026-09-24: README documents the `-l` / `--skill` / `--all` install forms and carries the skills.sh badge. Structural options await an owner decision: add a `skills/` container, or rename `packs/`. |
| claude-plugins.dev | in progress | Auto-crawl registry, no submission needed. No listing verified on 2026-09-24 (site exposes no stable search endpoint). Re-check at next release. |
| Smithery (skills section) | planned | Publish flow at smithery.ai/publish requires an account: user action. Not listed as of 2026-09-24. |
| Anthropic community plugin marketplace | planned | Submit at platform.claude.com/plugins/submit after confirming a skills-only catalogue qualifies for the plugin-shaped intake. Draft pending; user action. |
| ClawHub | deliberate N-A | OpenClaw-only audience, not a target for this catalogue (2026-09-24). |
| ComposioHQ/awesome-claude-skills | deferred | Gate: real use, docs, tested. Repo at 6 stars on 2026-09-24. Revisit at 25+ stars or at first documented external use. |
| VoltAgent/awesome-agent-skills | deferred | Gate: existing usage. Same revisit trigger as above. |
| hesreallyhim/awesome-claude-code | deferred | Gate: 14+ days of activity or 100 stars; issue form only, one recommendation at a time. |
| r/claudecode and r/AI_Agents posts | planned | Value-first post with disclosure, install one-liner, one demo. Draft pending; user posts. |
| agentskills Discord and spec-repo Show-and-tell | planned | Showcase post pending. |
| LinkedIn via jgs-announce | planned | Post pack pending at the next release. |
| Show HN | deferred | Needs a one-command install story and a fully hand-written post. Revisit after the skills.sh coverage question closes. |
| npm package | deliberate N-A | Distribution runs through `install.py` and the skills CLI; no package planned (2026-09-24). |
