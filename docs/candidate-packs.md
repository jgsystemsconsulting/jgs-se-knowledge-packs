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
| 1 | `fda-med-device` | full | built 2026-10-12. FDA guidance is public domain, high volume, zero competition, large audience |
| 2 | `functional-safety-signpost` | signpost | built 2026-09-27. ISO 26262 / IEC 61508 are the most-demanded paywalled standards; the repo already ships their free public cousins |
| 3 | `avionics-signpost` plus `faa-8110-49` | signpost + full | built 2026-10-12. DO-178C demand is proven; FAA Order 8110.49 is its free public-domain counterpart and fits the existing faa family |
| 4 | `uk-defence` family (JSP series first) | full | partially built 2026-10-28 (jsp-815, jsp-376, jsp-936, and jsp-912 done, other JSPs and DEF-STANs pending). OGL-licensed, no open competitor, and UK sourcing matches the consultancy's identity |
| 5 | `med-device-eu` | full | built 2026-10-13. MDCG guidance is free to reuse with attribution; MHRA is OGL |
| 6 | `nhtsa-vehicle` plus `automotive-signpost` | full + signpost | built 2026-09-27 (nhtsa-vehicle and automotive-signpost). NHTSA material is public domain; the signpost maps ISO 26262 / ISO-SAE 21434 to open paths |
| 7 | `nrc-nuclear`, `easa-rules` | full | built 2026-10-13 (nrc-nuclear 2026-10-12, easa-rules 2026-10-13). NRC guides are public domain; EASA Easy Access Rules are free downloads |
| 8 | `rail-signpost` (built 2026-10-14), `space-signpost` (built 2026-10-14), `maritime-signpost` (built 2026-10-14) | signpost | Cheap to build, each takes a day, and together they close the sector map |
| 9 | `fhwa-its-se` | full | built 2026-10-28. Tier-1 civil infrastructure, pinned to Systems Engineering for ITS, fourth generation (December 2022) |

A signpost pack is one SKILL.md and one PACK.yaml with no reproduced source content, which is why items 2, 6, and 8 were cheap to land. They are built. The ranked full-pack builds from the 2026-10-14 research gate are complete (rows 1, 3, 5-9 above, and the ranked UK defence JSPs in row 4). The unranked remainder of the uk-defence family (JSP 940, DEF-STANs) and telecom-3gpp need a new ranking pass. Full packs follow the existing pack spec with no new tooling.

## Where the catalogue stands

The catalogue holds 83 packs: 74 full reconstructed content packs, eight signpost packs (`automotive-signpost`, `avionics-signpost`, `functional-safety-signpost`, `maritime-signpost`, `omg-signpost`, `rail-signpost`, `se-standards-signpost`, `space-signpost`), and one `/se` orchestrator. Its sourcing is concentrated in six US federal publishers (NASA, DoD, FAA, NIST, GAO, DOE) plus SEBoK and OMG. Three expansion axes follow from that profile:

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
| Automotive (UNECE) | UNECE R155 / R156 texts | Free download, © UNECE, no redistribution grant | SIGNPOST (verified 2026-09-25) |
| Civil infrastructure | FHWA guidance incl. ITS systems-engineering material, FEMA docs | US public domain | FULL |
| Telecom | 3GPP specifications, ETSI standards, IETF RFCs | Free downloads (3GPP and ETSI confirmed) | FULL (different audience) |
| Functional safety / automotive standards | ISO 26262, IEC 61508, ISO-SAE 21434 | Paywalled, hard stop | SIGNPOST |
| Avionics | DO-178C / DO-254, ARP4754A / ARP4761 | Paywalled (RTCA / SAE) | SIGNPOST |
| Rail | EN 50126 / 50128 / 50129 paywalled; CSM regulations free on EUR-Lex; RSSB view-only | Mixed | SIGNPOST |
| Space (Europe) | ECSS standards | Free after registration under ECSS licence; repo vetting already excludes ECSS from packaging | SIGNPOST |
| Maritime | IMO and class-society rules paywalled or unclear; USCG material public domain | Mixed | SIGNPOST (built 2026-10-14) |
| Oil and gas | HSE offshore / COMAH guidance (OGL); NORSOK unverified | Thin SE tie beyond existing process-safety packs | LATER |
| Semiconductors | NIST electronics publications | Component specs, off-scope for SE agents | NOT NOW |

## Proposed packs

Full packs follow docs/PACK-SPEC.md: SKILL.md, PACK.yaml, LICENSE, and chapters under packs/&lt;slug&gt;/chapters/. Signpost packs are SKILL.md and PACK.yaml only, kind signpost, with tables of designation, owner, status, and official catalogue URL, and no reproduced content.

### Full packs

- `fda-med-device` (tier 1). Built 2026-10-12. Sources: FDA guidance documents on device software, the Quality Management System Regulation (21 CFR 820 as amended by the QMSR), premarket submission guidance, and cybersecurity guidance. All US government works. This is the strongest single opportunity: high publication volume, clear chapter boundaries, an audience that already asks agents about IEC 62304, and no open competitor.
- `med-device-eu` (built 2026-10-13) (tier 2/3, vet per doc). Sources: MDCG endorsed guidance (free, EU reuse with attribution), MHRA guidance (OGL v3). Chapter candidates: clinical evaluation, post-market surveillance, software as a medical device.
- `uk-defence-*` (tier 2/3, vet per doc). Built 2026-10-28 (jsp-815, jsp-376, jsp-936, and jsp-912). Sources: JSP publications on gov.uk (OGL v3) for safety, assurance, and requirements practice; selected DEF-STANs from UK Defence Standardization, which downloads free but carries per-document licence terms. Note SOURCE-VETTING.md already lists Def Stan 00-051 as unvetted, which is the right caution: each document gets its own licence statement before packaging. Start with one JSP pack and expand the family.
- `faa-8110-49` (tier 1). Built 2026-10-12. FAA Order 8110.49, software certification guidance for DO-178C usage. Public domain, sits naturally beside the existing faa family, and gives the avionics audience a real pack to land on from the signpost.
- `nhtsa-vehicle` (built 2026-09-27) (tier 1). Sources: FMVSS selections, NHTSA Cybersecurity Best Practices for the Safety of Modern Vehicles (final 2022), automated-vehicles guidance. Public domain. Gives automotive engineers open primary content despite the ISO paywall.
- `nrc-nuclear` (tier 1). Built 2026-10-12. Sources: NRC regulatory guides and selected NUREGs (digital systems, software assurance: NUREG-0800 chapters, RG 1.168 and siblings). Public domain, and a sibling to `nasa-system-safety` and the DOE packs already in the catalogue.
- `easa-rules` (built 2026-10-13) (tier 2/3, vet per doc). Sources: EASA Easy Access Rules volumes and certification specs. Free downloads; reuse terms need per-document confirmation. Start with one volume relevant to software and systems (for example the rules covering 1309 safety objectives) rather than the whole library.
- `fhwa-its-se` (built 2026-10-28) (tier 1). FHWA/USDOT systems-engineering guidance for intelligent transportation systems. Public domain, extends the catalogue into civil infrastructure with genuinely SE-shaped content rather than construction codes.
- `telecom-3gpp` (tier 2, later). 3GPP and ETSI publish freely, but the audience (network engineering) overlaps systems-engineering agents less than the other sectors. Hold until earlier packs land; a signpost is the cheaper first step.

### Signpost packs

Each is one working day or less: SKILL.md with tables mapping the paywalled standard to its free public analogue in this catalogue, plus official catalogue URLs.

- `functional-safety-signpost` (built 2026-09-27): IEC 61508, ISO 26262, ISO-SAE 21434. Free paths: MIL-STD-882 (`mil-std-882`), NHTSA cybersecurity guidance (`nhtsa-vehicle` (built 2026-09-27)), FDA software guidance (`fda-med-device`, built 2026-10-12).
- `avionics-signpost` (built 2026-10-12): DO-178C, DO-254, ARP4754B, ARP4761A. Free paths: FAA Order 8110.49 (`faa-8110-49`, built 2026-10-12), existing `faa-*` packs, EASA AMC texts, named, not packed.
- `automotive-signpost` (built 2026-09-27): ISO 26262, ASPICE, SAE J3016, UNECE R155/R156 (signpost-only; © UNECE, no redistribution grant, verified 2026-09-25). Open path: `nhtsa-vehicle` (built 2026-09-27) (US Government guidance, not a UNECE equivalent).
- `rail-signpost` (built 2026-10-14): EN 50126/50128/50129. Free paths: CSM 402/2013 (as amended by 2015/1136) and ORR guidance. RSSB summaries only. EN 50128 and EN 50129 have no free full text.
- `space-signpost` (built 2026-10-14): ECSS family. ECSS is free after registration and excluded from packaging. Free paths: the existing NASA packs. Structures, mechanisms, communications, ground operations, space environment, radiation methods, and PA/QA management have no in-repo pack.
- `maritime-signpost` (built 2026-10-14): SOLAS, ISM, ISPS, and COLREGS are IMO sales publications. Free paths are USCG material (eCFR Title 46 and the Navigation Rules PDF), UK MCA notices under OGL v3.0, and class portals (DNV, ABS, Bureau Veritas). Class rules stay copyrighted. Lloyd's Register was not confirmed.

### Not now, with reasons

Oil and gas (thin open base beyond HSE guidance, weak tie to the agent audience), semiconductors (JEDEC free but component-level, off-scope), robotics (agent skills already exist for ROS 2; not a standards gap), finance (no SE fit).

## Vetting cautions

Three risks need handling during build, not after. First, OGL v3 and EU reuse terms require forward attribution and, for OGL, source linking inside the pack; PACK.yaml license_tier 2 conditions cover this, but each pack's LICENSE must reproduce the actual licence text. Second, per-document licences vary inside DEF-STAN, EASA, and MDCG libraries, so the pack build for those sectors must record an in-source licence statement per document, per SOURCE-VETTING.md. Third, UNECE R155/R156 were re-verified on 2026-09-25 and the outcome reverses the original scan verdict: the texts download free but carry © UNECE with no redistribution grant, so they are signpost-only (SOURCE-VETTING.md, post-v1.21.0 table) and `automotive-signpost` may only point at them, never reproduce them.

## Mechanics of adding a pack

Adding a pack from this list needs: the pack folder per PACK-SPEC.md, a tier assignment under SOURCE-VETTING.md rules, regeneration of SKILLS.md, an update to the `/se` orchestrator routing, and an update to the capability map (`docs/capability-pack-map.json`, checked by `tooling/check_capability_map.py`). A live catalog pack (any kind other than signpost or orchestrator) also gets a catalog.json row and a watchlist entry in `docs/source-watchlist.json` (one entry per live catalog pack; see docs/SOURCE-FRESHNESS.md). A signpost or an orchestrator gets neither a catalog row nor a watchlist entry. Gates: `tooling/validate_pack.py`, `tooling/check_release.py`, and the CI gate.

## Sources consulted

Repo: docs/PACK-SPEC.md, docs/SOURCE-VETTING.md, docs/LICENSING.md, SKILLS.md, catalog.json, tooling/. External (fetched 2026-09-24):

- [FDA medical devices](https://www.fda.gov/medical-devices)
- MDCG endorsed guidance (EU Commission)
- [MHRA publications](https://www.gov.uk/government/organisations/medicines-and-healthcare-products-regulatory-agency)
- [JSP collection on gov.uk](https://www.gov.uk/government/collections/joint-service-publication-jsp)
- EASA Easy Access Rules (EU Aviation Safety Agency)
- [ECSS standards](https://ecss.nl/standards/)
- [NRC document collections](https://www.nrc.gov/reading-rm/doc-collections/)
- [ONR publications](https://www.onr.org.uk/publications/)
- [HSE publications](https://www.hse.gov.uk/pubns/)
- [UNECE vehicle regulations](https://unece.org/transport/vehicle-regulations-wp29)
- [NHTSA](https://www.nhtsa.gov/)
- [3GPP specifications](https://www.3gpp.org/specifications)
- [ETSI standards](https://www.etsi.org/standards)
- EUR-Lex (EU legal database)
- [awesome-safety-critical](https://github.com/stanislaw/awesome-safety-critical)
- [Agent Skills specification](https://github.com/agentskills/agentskills)
