# Distribution ledger

Status vocabulary per RR-B-36: submitted / in progress / deferred / deliberate N-A /
planned. Every row carries its decision and date. Revisit at every release. Channel
mechanics were verified against live sites on 2026-09-24; re-verify a row before
acting on it. Operational working state (waiting-on, next actions, submission drafts)
lives in the maintainer-only `.zcode/` tree and is deliberately not published.

| Channel | Status | Decision and date |
|---|---|---|
| skills.sh | in progress | Auto-indexed since 2026-09-08. Directory-page coverage partial on 2026-09-24 and 2026-10-26 (6 of 80 pages observed at the 2026-10-26 crawl; the catalogue has since grown to 83 skills, all declared in the plugin manifests): the crawler's well-known containers do not include `packs/`. Resolved structurally 2026-10-26 without renaming: vercel-labs/skills honours skill paths declared in plugin manifests (`src/plugin-manifest.ts`), so `.claude-plugin/plugin.json` now declares all 83 `./packs/<slug>` paths, and a local emulation of the crawler's discovery walks all 83. Installs were never affected. Keep this row open until directory coverage is re-checked after the next crawl. |
| claude-plugins.dev | in progress | Auto-crawl registry, no submission needed. No listing verified on 2026-09-24; re-checked 2026-10-03, still absent (search path 404s, homepage exposes browse/sort only). Re-check at next release. |
| Smithery (skills section) | planned | Publish flow at smithery.ai/publish requires an account: user action. Not listed as of 2026-09-24. |
| skillsdirectory.com | planned | Free directory, GitHub-login submission form at /submit with human review before listing (assessed 2026-10-03). Auto-index presence not confirmed: search is client-side, so the repo may or may not already be crawled. Submission is a user action (GitHub login). Operator is anonymous (GitHub/X handles only in the footer); treat as a discoverability channel, not an endorsement. |
| LobeHub skills market (market.lobehub.com) | planned | Marketplace at market.lobehub.com with `@lobehub/market-cli` search/install; listings carry GitHub source URLs, so repos are ingested, but no publish flow is documented and search requires a registered client (probed 2026-10-03). Assess the publish path before acting; not blocking. |
| Agensi (agensi.io) | deliberate N-A | Paid marketplace (creators keep 70%, 30% fee, dashboard submit, creator vetting; assessed 2026-10-03). Selling conflicts with non-commercial pack licences (CC BY-NC-SA and other source-licensed content) and the free-distribution model; no free listing path. Revisit only if a paid tier is ever wanted, with a per-pack licence screen. |
| Anthropic community plugin marketplace | planned | Submit at platform.claude.com/plugins/submit. The repo already carries `.claude-plugin/marketplace.json` and `plugin.json`, so the plugin-shaped intake fits. Submission awaits an account login: user action. |
| ClawHub | deliberate N-A | OpenClaw-only audience, not a target for this catalogue (2026-09-24). |
| ComposioHQ/awesome-claude-skills | deliberate N-A | Star gate (25+) fired at 26 stars, but the list hosts skills inside its own tree (fork, add a SKILL.md folder), which conflicts with catalogue distribution from this repo. Revisit only if it accepts external links (2026-10-26). |
| VoltAgent/awesome-agent-skills | submitted | PR 1272 opened 2026-10-26 under jgsystemsconsulting, Specialized Domains entry. Outcome pending maintainer review. |
| hesreallyhim/awesome-claude-code | in progress | Age/activity gate cleared (repo live since 2026-06-19). Issue-form content prepared 2026-10-26, package in `.zcode/distribution/human-submissions.md`; the form is human-filed by the list's rule, submission pending. |
| travisvn/awesome-claude-skills | in progress | PR line and title prepared 2026-10-26, package in `.zcode/distribution/human-submissions.md`; the list closes AI-submitted PRs, so the PR is human-filed. Star gate met (26). List last pushed 2026-04; expect slow review. |
| ccplugins/awesome-claude-code-plugins | deliberate N-A | Owner has disabled opening pull requests and issues (verified logged-in 2026-10-26: banner "An owner of this repository has disabled the ability to open pull requests"; no Issues tab). No contribution path exists. The prepared External Marketplaces row stays on the fork branch `add-jgs-se-marketplace` of jgsystemsconsulting/awesome-claude-code-plugins, harmless. |
| r/claudecode and r/AI_Agents posts | planned | Value-first post with disclosure, install one-liner, one demo. Draft pending; user posts. |
| agentskills Discord and spec-repo Show-and-tell | planned | Showcase post pending. |
| LinkedIn via jgs-announce | planned | Post pack pending at the next release. |
| Per-pack landing pages (SEO) | in progress | tooling/gen_pack_pages.py emits docs/packs/<slug>/index.html keyed to each source document's name. All 74 catalog packs live 2026-10-26 (jgsystemsconsulting.github.io/jgs-se-knowledge-packs/packs/<slug>/); sitemap and packs.html cover the full set. The 8 signposts and the /se orchestrator stay GitHub-linked until their metadata gets a catalog entry. |
| Show HN | deferred | Needs a one-command install story and a fully hand-written post. Revisit after the skills.sh coverage question closes. |
| npm package | deliberate N-A | Distribution runs through `install.py` and the skills CLI; no package planned (2026-09-24). |
