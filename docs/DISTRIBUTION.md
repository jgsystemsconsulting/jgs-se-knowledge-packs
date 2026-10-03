# Distribution ledger

Status vocabulary per RR-B-36: submitted / in progress / deferred / deliberate N-A /
planned. Every row carries its decision and date. Revisit at every release. Channel
mechanics were verified against live sites on 2026-09-24; re-verify a row before
acting on it. Operational working state (waiting-on, next actions, submission drafts)
lives in the maintainer-only `.zcode/` tree and is deliberately not published.

| Channel | Status | Decision and date |
|---|---|---|
| skills.sh | in progress | Auto-indexed since 2026-09-08. Directory-page coverage partial on 2026-09-24 (`sebok`, `dod-digital-engineering`, `nasa-systems-modeling`, `omg-signpost` observed of 63 packs) and still partial on 2026-10-03 (no page for `nhtsa-vehicle`): the skills CLI's well-known containers do not include `packs/`, so page indexing falls back to a partial crawl. Installs are unaffected: `npx skills add jgsystemsconsulting/jgs-se-knowledge-packs --list` discovers all 69 skills including the three v1.22.0 entries (verified 2026-10-03). README documents the `-l` / `--skill` / `--all` install forms and carries the skills.sh badge. Structural options await an owner decision: add a `skills/` container, or rename `packs/`. |
| claude-plugins.dev | in progress | Auto-crawl registry, no submission needed. No listing verified on 2026-09-24; re-checked 2026-10-03, still absent (search path 404s, homepage exposes browse/sort only). Re-check at next release. |
| Smithery (skills section) | planned | Publish flow at smithery.ai/publish requires an account: user action. Not listed as of 2026-09-24. |
| skillsdirectory.com | planned | Free directory, GitHub-login submission form at /submit with human review before listing (assessed 2026-10-03). Auto-index presence not confirmed: search is client-side, so the repo may or may not already be crawled. Submission is a user action (GitHub login). Operator is anonymous (GitHub/X handles only in the footer); treat as a discoverability channel, not an endorsement. |
| LobeHub skills market (market.lobehub.com) | planned | Marketplace at market.lobehub.com with `@lobehub/market-cli` search/install; listings carry GitHub source URLs, so repos are ingested, but no publish flow is documented and search requires a registered client (probed 2026-10-03). Assess the publish path before acting; not blocking. |
| Agensi (agensi.io) | deliberate N-A | Paid marketplace (creators keep 70%, 30% fee, dashboard submit, creator vetting; assessed 2026-10-03). Selling conflicts with non-commercial pack licences (CC BY-NC-SA and other source-licensed content) and the free-distribution model; no free listing path. Revisit only if a paid tier is ever wanted, with a per-pack licence screen. |
| Anthropic community plugin marketplace | planned | Submit at platform.claude.com/plugins/submit. The repo already carries `.claude-plugin/marketplace.json` and `plugin.json`, so the plugin-shaped intake fits. Submission awaits an account login: user action. |
| ClawHub | deliberate N-A | OpenClaw-only audience, not a target for this catalogue (2026-09-24). |
| ComposioHQ/awesome-claude-skills | deferred | Gate: real use, docs, tested. Repo at 6 stars on 2026-09-24. Revisit at 25+ stars or at first documented external use. |
| VoltAgent/awesome-agent-skills | deferred | Gate: existing usage. Same revisit trigger as above. |
| hesreallyhim/awesome-claude-code | deferred | Gate: 14+ days of activity or 100 stars; issue form only, one recommendation at a time. |
| r/claudecode and r/AI_Agents posts | planned | Value-first post with disclosure, install one-liner, one demo. Draft pending; user posts. |
| agentskills Discord and spec-repo Show-and-tell | planned | Showcase post pending. |
| LinkedIn via jgs-announce | planned | Post pack pending at the next release. |
| Show HN | deferred | Needs a one-command install story and a fully hand-written post. Revisit after the skills.sh coverage question closes. |
| npm package | deliberate N-A | Distribution runs through `install.py` and the skills CLI; no package planned (2026-09-24). |
