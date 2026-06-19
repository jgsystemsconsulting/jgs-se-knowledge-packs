<h1 align="center">se-knowledge-packs</h1>

<p align="center">
  <strong>Installable knowledge-pack skills for coding agents, built from genuinely open
  systems-engineering bodies of knowledge.</strong><br>
  Every pack ships its source's licence and provenance — shareable by construction.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/License-MIT%20(tooling)-blue" alt="MIT tooling">
  <img src="https://img.shields.io/badge/Packs-1%20live%20%2F%204%20planned-blueviolet" alt="Packs">
  <img src="https://img.shields.io/badge/Agent%20Skills-open%20standard-green" alt="Agent Skills">
  <img src="https://img.shields.io/badge/scope-systems%20engineering-orange" alt="Scope">
</p>

---

## Why

A great body of knowledge — SEBoK, the NASA SE Handbook, a spec — is something you read
once and then forget exists when you actually need it mid-task. A **knowledge pack** turns
it into a skill your coding agent loads on demand: ask `/sebok systems of systems` and the
agent reads the right chapter and answers from the actual source, not from a hazy
recollection.

This repo curates those packs for **systems engineering**, with one rule that makes it
different from "point a tool at a PDF":

> **Only genuinely open sources go in.** Public-domain (NASA, NIST, DoD) and
> open-licensed (SEBoK, OMG specs, CC content) — never paywalled or all-rights-reserved
> material. "Free to download" is not "free to redistribute," and the difference is
> enforced, not assumed. See [docs/SOURCE-VETTING.md](docs/SOURCE-VETTING.md).

So every pack here is safe to install, share with a colleague, and publish — by design.

## Catalog

| Pack | Source | Licence | Tier | Status |
|------|--------|---------|------|--------|
| [`sebok`](packs/sebok) | Guide to the SE Body of Knowledge v2.13 | CC BY-NC-SA 3.0 | 🟡 2 | ✅ live (41 chapters) |
| `nasa-se-handbook` | NASA Systems Engineering Handbook (SP-2016-6105) | Public domain (US gov) | 🟢 1 | 🔜 planned |
| `omg-sysml` | OMG Systems Modeling Language spec | OMG licence | 🟡 2 | 🔜 planned |
| `dodaf` | DoD Architecture Framework 2.02 | Public release, unlimited | 🟢 1 | 🔜 planned |
| `mit-ocw-se` | MIT OCW 16.842 Fundamentals of SE | CC BY-NC-SA | 🟡 2 | 🔜 planned |

Roadmap and source vetting for each candidate: [docs/SOURCE-VETTING.md](docs/SOURCE-VETTING.md).

## Install a pack

```bash
git clone https://github.com/<owner>/se-knowledge-packs.git
cp -r se-knowledge-packs/packs/sebok ~/.claude/skills/sebok    # Claude Code
# then, in a session:
/sebok lifecycle model selection
```

Packs follow the open [Agent Skills](https://github.com/agentskills/agentskills)
`SKILL.md` standard, so the same folder works in Claude Code, GitHub Copilot CLI
(`~/.copilot/skills` or `~/.agents/skills`), and Amp.

## How a pack is built

1. **Vet the source** against [docs/SOURCE-VETTING.md](docs/SOURCE-VETTING.md) — tier it,
   name its licence, confirm it is not on the Excluded list.
2. **Extract** the text (built on the MIT-licensed
   [`book-to-skill`](https://github.com/virgiliojr94/book-to-skill) engine).
3. **Map structure** to chapter offsets, then **generate** reference-depth chapter files
   in parallel (one per knowledge area), plus glossary / patterns / cheatsheet and the
   master `SKILL.md` index.
4. **Attach provenance** — `PACK.yaml` + a `LICENSE` reproducing the source's terms.
5. **Validate** — `python tooling/validate_pack.py packs/<slug>`.

Pack contract: [docs/PACK-SPEC.md](docs/PACK-SPEC.md). Contributing a pack:
[CONTRIBUTING.md](CONTRIBUTING.md).

## Licensing

- **Repository tooling and scaffolding:** [MIT](LICENSE).
- **Pack *content*:** each pack carries its **source's** licence in `packs/<slug>/LICENSE`,
  independent of the repo MIT licence. A CC BY-NC-SA source (like SEBoK) produces a
  CC BY-NC-SA pack — non-commercial, attribution and share-alike carried forward.

This separation is deliberate: the *machinery* is permissively licensed; the *knowledge*
keeps whatever obligations its open source attached.

## Status

Early release. One exemplar pack (`sebok`) is live and validated; the SE catalogue above
is the near-term roadmap. Issues and pack proposals welcome.
