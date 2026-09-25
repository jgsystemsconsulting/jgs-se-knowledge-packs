<!--
Copyright (c) 2026 JG Systems Consulting Ltd. - MIT License (see LICENSE).
SPDX-License-Identifier: MIT
-->

# Candidate knowledge packs: industry expansion

Research-backed shortlist for growing the catalogue beyond its US federal systems-engineering core. Prepared 2026-09-24 from three research passes: a format audit of this repo, a scan of the agent-skills and awesome-list supply on GitHub, and licence verification against primary sources for thirteen candidate sectors. Status: proposal for discussion, not a committed roadmap.

## Recommendation

Build in this order:

| # | Pack | Kind | Why first |
|---|------|------|-----------|
| 1 | `fda-med-device` | full | FDA guidance is public domain, high volume, zero competition, large audience |
| 2 | `functional-safety-signpost` | signpost | ISO 26262 / IEC 61508 are the most-demanded paywalled standards; the repo already ships their free public cousins |
| 3 | `avionics-signpost` plus `faa-8110-49` | signpost + full | DO-178C demand is proven; FAA Order 8110.49 is its free public-domain counterpart and fits the existing faa family |
| 4 | `uk-defence` family (JSP series first) | full | OGL-licensed, no open competitor, and UK sourcing matches the consultancy's identity |
| 5 | `med-device-eu` | full | MDCG guidance is free to reuse with attribution; MHRA is OGL |
| 6 | `nhtsa-vehicle` plus `automotive-signpost` | full + signpost | NHTSA material is public domain; the signpost maps ISO 26262 / ISO-SAE 21434 to open paths |
| 7 | `nrc-nuclear`, `easa-rules` | full | NRC guides are public domain; EASA Easy Access Rules are free downloads |
| 8 | `rail-signpost`, `space-signpost`, `maritime-signpost` | signpost | Cheap to build, each takes a day, and together they close the sector map |

The signposts first among these cost almost nothing: a signpost pack is one SKILL.md and one PACK.yaml with no reproduced source content, so items 2 and the signpost half of 6 and 8 are the fastest visible progress. The full packs follow the existing pack spec with no new tooling.

## Where the catalogue stands

The catalogue holds 66 packs. Its sourcing is concentrated in six US federal publishers (NASA, DoD, FAA, NIST, GAO, DOE) plus SEBoK and OMG, organised as full reconstructed packs, two signpost packs (`se-standards-signpost`, `omg-signpost`), and one `/se` orchestrator. Three expansion axes follow from that profile:

- New sectors the current sources cannot reach: medical devices, automotive, rail, nuclear, maritime, telecom, civil infrastructure.
- New geographies: UK and European sources complement the US federal core, and OGL / EU-reuse material slots into licence tier 2 under the existing vetting rules.
- Signpost coverage for paywalled-cored domains, where the honest move is to point at the owner and name the free public analogue, exactly as `se-standards-signpost` does for ISO 15288 and friends.

## Ecosystem finding

No open project ships standards-derived knowledge packs in the Agent Skills format for any regulated engineering domain other than this catalogue. The scan (10+ searches across GitHub, agentskills.io, agentskills clients page, and awesome-list space, on 2026-09-24) found: general agent-skill lists with tens of thousands of stars and no engineering-regulatory content; [awesome-safety-critical](https://github.com/stanislaw/awesome-safety-critical) (1.6k stars) as a link list with no agent-usable packaging; domain code tooling such as a ROS 2 skills repo and an ISO 26262 Go checker; and nothing that reconstructs free standards into progressive-disclosure packs. The [Agent Skills spec](https://github.com/agentskills/agentskills) (25k+ stars) has client support in Claude Code, Copilot CLI, Amp, and others, so distribution is solved; supply for engineering domains is the gap. Each new sector is therefore a first-mover position, and demand is evidenced by the popularity of the link lists this catalogue supersedes.

## Sector feasibility

Verification method: direct fetches of publisher landing and download pages on 2026-09-24. "Free to read" alone never qualifies; the test is a redistribution or reuse grant, per SOURCE-VETTING.md.

| Sector | Open primary sources | Licence | Verdict |
|--------|----------------------|---------|---------|
| Medical devices | FDA guidance and regulations, MDCG guidance, MHRA publications | US public domain; EU reuse with attribution; OGL v3 | FULL |
| Defence (UK) | JSP series on gov.uk, selected DEF-STANs from UK Defence Standardization | OGL v3 / crown copyright, per-document | FULL (vet per doc) |
| Nuclear / energy | NRC NUREGs and regulatory guides, ONR publications, HSE indg/pubns series | US public domain; OGL v3 | FULL |
| Aviation (Europe) | EASA Easy Access Rules, certification specs, AMC/GM | Free download, reuse with acknowledgement | FULL (vet per doc) |
| Automotive (US) | NHTSA FMVSS, cybersecurity and guidance documents | US public domain | FULL |
| Automotive (UNECE) | UNECE R155 / R156 texts | Free on unece.org (fetch verification failed once; re-verify before build) | FULL (re-verify) |
| Civil infrastructure | FHWA guidance incl. ITS systems-engineering material, FEMA docs | US public domain | FULL |
| Telecom | 3GPP specifications, ETSI standards, IETF RFCs | Free downloads (3GPP and ETSI confirmed) | FULL (different audience) |
| Functional safety / automotive standards | ISO 26262, IEC 61508, ISO-SAE 21434 | Paywalled, hard stop | SIGNPOST |
| Avionics | DO-178C / DO-254, ARP4754A / ARP4761 | Paywalled (RTCA / SAE) | SIGNPOST |
| Rail | EN 50126 / 50128 / 50129 paywalled; CSM regulations free on EUR-Lex; RSSB view-only | Mixed | SIGNPOST |
| Space (Europe) | ECSS standards | Free after registration under ECSS licence; repo vetting already excludes ECSS from packaging | SIGNPOST |
| Maritime | IMO and class-society rules paywalled or unclear; USCG material public domain | Mixed | SIGNPOST |
| Oil and gas | HSE offshore / COMAH guidance (OGL); NORSOK unverified | Thin SE tie beyond existing process-safety packs | LATER |
| Semiconductors | NIST electronics publications | Component specs, off-scope for SE agents | NOT NOW |

## Proposed packs

Full packs follow docs/PACK-SPEC.md: SKILL.md, PACK.yaml, LICENSE, and chapters under packs/&lt;slug&gt;/chapters/. Signpost packs are SKILL.md and PACK.yaml only, kind signpost, with tables of designation, owner, status, and official catalogue URL, and no reproduced content.

### Full packs

- `fda-med-device` (tier 1). Sources: FDA guidance documents on device software, the Quality Management System Regulation (21 CFR 820 as amended by the QMSR), premarket submission guidance, and cybersecurity guidance. All US government works. This is the strongest single opportunity: high publication volume, clear chapter boundaries, an audience that already asks agents about IEC 62304, and no open competitor.
- `med-device-eu` (tier 2/3, vet per doc). Sources: MDCG endorsed guidance (free, EU reuse with attribution), MHRA guidance (OGL v3). Chapter candidates: clinical evaluation, post-market surveillance, software as a medical device.
- `uk-defence-*` (tier 2/3, vet per doc). Sources: JSP publications on gov.uk (OGL v3) for safety, assurance, and requirements practice; selected DEF-STANs from UK Defence Standardization, which downloads free but carries per-document licence terms. Note SOURCE-VETTING.md already lists Def Stan 00-051 as unvetted, which is the right caution: each document gets its own licence statement before packaging. Start with one JSP pack and expand the family.
- `faa-8110-49` (tier 1). FAA Order 8110.49, software certification guidance for DO-178C usage. Public domain, sits naturally beside the existing faa family, and gives the avionics audience a real pack to land on from the signpost.
- `nhtsa-vehicle` (tier 1). Sources: FMVSS selections, NHTSA Cybersecurity Best Practices for the Safe and Secure Design of Modern Vehicles, automated-vehicles guidance. Public domain. Gives automotive engineers open primary content despite the ISO paywall.
- `nrc-nuclear` (tier 1). Sources: NRC regulatory guides and selected NUREGs (digital systems, software assurance: NUREG-0800 chapters, RG 1.168 and siblings). Public domain, and a sibling to `nasa-system-safety` and the DOE packs already in the catalogue.
- `easa-rules` (tier 2/3, vet per doc). Sources: EASA Easy Access Rules volumes and certification specs. Free downloads; reuse terms need per-document confirmation. Start with one volume relevant to software and systems (for example the rules covering 1309 safety objectives) rather than the whole library.
- `fhwa-its-se` (tier 1). FHWA/USDOT systems-engineering guidance for intelligent transportation systems. Public domain, extends the catalogue into civil infrastructure with genuinely SE-shaped content rather than construction codes.
- `telecom-3gpp` (tier 2, later). 3GPP and ETSI publish freely, but the audience (network engineering) overlaps systems-engineering agents less than the other sectors. Hold until earlier packs land; a signpost is the cheaper first step.

### Signpost packs

Each is one working day or less: SKILL.md with tables mapping the paywalled standard to its free public analogue in this catalogue, plus official catalogue URLs.

- `functional-safety-signpost`: IEC 61508, ISO 26262, ISO-SAE 21434. Free paths: MIL-STD-882 (`mil-std-882`), NHTSA cybersecurity guidance (proposed `nhtsa-vehicle`), FDA software guidance (proposed `fda-med-device`).
- `avionics-signpost`: DO-178C, DO-254, ARP4754A, ARP4761. Free paths: FAA Order 8110.49 (proposed `faa-8110-49`), existing `faa-*` packs, EASA AMC material (proposed `easa-rules`).
- `automotive-signpost`: ISO 26262, ASPICE, SAE J3016. Free paths: UNECE R155/R156, NHTSA guidance (proposed `nhtsa-vehicle`).
- `rail-signpost`: EN 50126/50128/50129. Free paths: CSM regulations on EUR-Lex, RSSB standard summaries.
- `space-signpost`: ECSS family. Free paths: the existing NASA packs cover most ECSS-equivalent ground; the signpost names the ECSS document for each need and links to the ECSS catalogue.
- `maritime-signpost`: SOLAS, class rules. Free path: USCG material.

### Not now, with reasons

Oil and gas (thin open base beyond HSE guidance, weak tie to the agent audience), semiconductors (JEDEC free but component-level, off-scope), robotics (agent skills already exist for ROS 2; not a standards gap), finance (no SE fit).

## Vetting cautions

Three risks need handling during build, not after. First, OGL v3 and EU reuse terms require forward attribution and, for OGL, source linking inside the pack; PACK.yaml license_tier 2 conditions cover this, but each pack's LICENSE must reproduce the actual licence text. Second, per-document licences vary inside DEF-STAN, EASA, and MDCG libraries, so the pack build for those sectors must record an in-source licence statement per document, per SOURCE-VETTING.md. Third, UNECE availability rests on one failed fetch plus prior knowledge; re-verify before committing to `automotive-signpost` content that depends on it.

## Mechanics of adding a pack

Adding any pack from this list needs: the pack folder per PACK-SPEC.md, a tier assignment under SOURCE-VETTING.md rules, regeneration of SKILLS.md, a catalog.json entry, and updates to the `/se` orchestrator routing and the capability map (`docs/capability-map.json`, checked by `tooling/check_capability_map.py`). Gates: `tooling/validate_pack.py`, `tooling/check_release.py`, and the CI gate. Nothing new is required from the tooling for full or signpost kinds.

## Sources consulted

Repo: docs/PACK-SPEC.md, docs/SOURCE-VETTING.md, docs/LICENSING.md, SKILLS.md, catalog.json, tooling/. External (fetched 2026-09-24):

- [FDA medical devices](https://www.fda.gov/medical-devices)
- [MDCG endorsed guidance](https://health.ec.europa.eu/medical-devices-sector/new-regulations/guidance-mdcg-endorsed-documents-and-other-guidance_en)
- [MHRA publications](https://www.gov.uk/government/organisations/medicines-and-healthcare-products-regulatory-agency)
- [JSP collection on gov.uk](https://www.gov.uk/government/collections/joint-service-publication-jsp)
- [EASA Easy Access Rules](https://www.easa.europa.eu/en/document-library/easy-access-rules)
- [ECSS standards](https://ecss.nl/standards/)
- [NRC document collections](https://www.nrc.gov/reading-rm/doc-collections/)
- [ONR publications](https://www.onr.org.uk/publications/)
- [HSE publications](https://www.hse.gov.uk/pubns/)
- [UNECE vehicle regulations](https://unece.org/transport/vehicle-regulations-wp29)
- [NHTSA](https://www.nhtsa.gov/)
- [3GPP specifications](https://www.3gpp.org/specifications)
- [ETSI standards](https://www.etsi.org/standards)
- [EUR-Lex](https://eur-lex.europa.eu/)
- [awesome-safety-critical](https://github.com/stanislaw/awesome-safety-critical)
- [Agent Skills specification](https://github.com/agentskills/agentskills)
