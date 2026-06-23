# Chapter — Use Cases for Establishing MBE Elements and Interoperability Requirements

> **Pairing caveat:** This pack covers NASA-HDBK-1004 (the Digital Engineering Acquisition Framework Handbook). It pairs with **NASA-HDBK-1009A**; consult that companion handbook alongside this material when establishing model-based enterprise (MBE) elements and interoperability requirements, and treat the two as complementary rather than substitutable.

## Core Idea

Appendix G of NASA-HDBK-1004 supplies four worked use cases that a program or project should reason through before fixing MBE elements and interoperability requirements, working in correlation with the handbook's Table 6. The animating premise is that you cannot pick the right tools, exchange mechanisms, or access levels until you understand how neutral-format data will actually be used. Get that understanding first, and tool selection becomes cost-efficient, data exchange becomes efficient, and everyone who needs data can reach it at the level they require. The four use cases — Viewing, Data Exchange, Data Integrity, and Data Interoperability Formats — are deliberately ordered from the lightest demand on the data (just looking at it) to the heaviest (round-trip, bi-directional, standards-governed exchange across organizational boundaries). Each one raises the bar on what the underlying format and the processing application must support, which in turn drives what you write into the Data Requirements Description (DRD) and what you negotiate with suppliers and partners.

## Frameworks Introduced

- **Four MBE use cases (NASA-HDBK-1004, Appendix G.2).** The appendix names exactly four use cases to weigh when establishing MBE elements and interoperability requirements: (a) Viewing, (b) Data Exchange, (c) Data Integrity, and (d) Data Interoperability Formats. Use them as a structured checklist during acquisition planning, mapped against Table 6, so that the chosen neutral-format data, tools, and access arrangements match real downstream needs rather than assumptions.

- **Table 6 (MCAD data formats).** Referenced as the source from which mechanical CAD (MCAD) data formats may currently be selected, and as the table against which the four use cases are correlated. The appendix directs you to use it as the format menu when scoping interoperability requirements.

- **Table 8 — Format Maturity Levels (NASA-HDBK-1004).** Assigns a maturity level to each data format so the dynamics of each can be judged against its intended utilization. It frames a four-level progression — Traditional/Paper, ePaper, XML Data Objects, and EXTL Application/Database — with project-based, transitional, and enterprise-based positioning. Apply it when deciding how mature a format must be for the reuse and interoperability you actually need; the appendix cross-references NIMA-RPT-004 for the underlying treatment and cautions that users should still check current technology trends from other sources before committing.

- **Four format-application levels (Table 8 guidance).** A companion set of "specify when" rules attached to the maturity table: Level 1 (Paper), Level 2 (Formatted Documents / electronic paper), Level 3 (Standard XML data descriptions in NASA standard format), and Level 4 (digital data transferred between a source and a target repository using a format the program/project has specified). Each level states the conditions under which to apply it. Levels 1 and 2 are explicitly flagged as neither recommended nor supported under MBE.

- **NIMA-RTP-002, *Data Integrity in NASA Programs and Projects*.** Cited as the white paper behind the Data Integrity use case. It traces data-integrity requirements to NASA Procedural Requirements and explains how data integrity underpins the integrity of a program's integrated design and the readiness of operational flight and ground data systems, and records data-management lessons learned. Refer to it when justifying or scoping data-integrity controls.

- **STEP / ISO 10303 application protocols and requirements-interchange standards.** For requirements interoperability the appendix points to STEP AP 242, AP 239, and AP 233 within ISO 10303, and to the Regulated Qualifications Framework (RQF) or Requirements Interchange Format (RIF). These are named as the standards to follow when establishing requirements interoperability; XML and STEP are cited as the general standards data interoperability should follow where applicable.

- **NASA common data dictionary.** Invoked as the shared reference that all producers and consumers of standard XML digital data must point to for Level 3 descriptions to be usable; where a NASA standard does not apply, a contractor-defined common data dictionary plays the same role, with a catalog of XML schema descriptions in place before contractor data is delivered.

## Key Concepts

- **Neutral-format data.** Understanding how neutral-format data is used is the precondition for selecting tools, exchange mechanisms, and access levels efficiently. The whole appendix is organized around that understanding.

- **Simplified representations (Viewing).** When a CAD system is not wanted, 3D viewers handle visualization for product-data presentation, information-only model display (e.g., design reviews, marketing), and virtual-reality realism. Where assemblies or design spaces are large, high-performance visualization matters, and simplified representations become especially important. Their key needs: source-system-independent representation of geometry and metadata at the required level of detail; the ability to filter product structure (views or layers); simple measurement; representation of PMI; textures and light sources for VR; and easy-to-use, cross-system viewers.

- **PMI versus metadata.** The appendix draws a sharp distinction. *Metadata* is text-only description — for example, author information or a model's release status. *Product and Manufacturing Information (PMI)* is richer, typically added as 3D annotations, manufacturing notes, and material specifications. This distinction recurs across viewing and exchange and drives format requirements.

- **Design in context of existing geometry (Data Exchange).** A frequently used modeling method where a development partner changes geometry after it has been exchanged. Here, merely viewing the data is insufficient; the format and processing application must support exact-geometry exchange, additional product-describing information, grouping and filter options for clarity, and the ability to process PMI after the exchange has happened.

- **Exchanging exact geometry.** Needed when authoring systems differ — for instance, when a supplier's CAD system is not the manufacturer's. The key considerations: a data format and collaborative model definitions that transfer exact geometry and the full product structure; transfer of metadata and PMI annotations (depending on the technology readiness level (TRL) in play and whether a concrete use case applies); and assured data integrity, fidelity, completeness, and one-to-one correlation between the original and target models. Intellectual-property protection is a rising concern in exchange and should be reflected in the DRD.

- **Two forms of data integrity.** (1) *Integrity of data relative to its authoritative source* — the information-security property that no unauthorized or accidental alteration, destruction, or loss has befallen the data; in NASA practice this most actionably means integrity relative to the authoritative source across and within a program/project. (2) *Integrity of data relative to an authoritative model* — the database-systems property that data accurately reflect the domain they model; in NASA practice this spans *component* integrity (a single datum against a valid type, range, or text rule) and *composite* integrity (multiple data items against each other and an authoritative model).

- **Authoritative source and the manual-copy risk.** Within a program, authoritative sources exist for many data types across discipline-specific tools and multiple instances of the same tool. Integrated analyses require integrating data from those sources. Current common practice is to copy data manually out of the authoritative source into other tools, documents, or presentations — and from the moment of copying, a staleness risk exists, because source changes do not propagate into the manual copy. The resulting discrepancies create a high-probability program risk of wrong decisions, misrepresented integrated design, or misstated readiness.

- **Automated data integration and automated data audits.** The two main approaches to better integrity. *Automated data integration* relative to authoritative sources aims to improve integrity and accessibility and raise data-management efficiency across the life cycle; it minimizes non-authoritative copies through automated aggregation, cutting discrepancy rates and letting user communities manage data in purpose-built tools while pulling directly from authoritative sources. *Automated data audits* are a proven, high-utility, relatively low-cost technique that can run daily or weekly to drive design convergence and safeguard the integrity of baseline engineering artifacts, at either the elemental or composite level.

- **Data interoperability beyond CAD.** Interoperability covers not just CAD data but non-CAD data used in innovation, preliminary design, and other pre-CAD domains such as requirements analysis. All formats deserve attention and count as part of digitalization, and all should follow applicable standards (e.g., STEP, XML).

- **Process terms and base elements.** Process definitions consist of data-object definitions, flow steps, descriptors, user roles, and decision rules; processes are realized by configuring those elements into flows. Because agreement on the base elements is what makes flows shareable, the *depth of agreement* on base elements and flow configuration is named as the primary mechanism for achieving interoperability.

## Mental Models

- **The use-case ladder.** Read the four use cases as rungs of increasing demand on data. Viewing asks the least — show geometry, maybe metadata or PMI. Data Exchange adds round-trip exact geometry and post-exchange PMI processing. Data Integrity adds correctness guarantees against an authoritative source and model. Data Interoperability Formats adds standards-governed, bi-directional, cross-organization exchange. Each rung you climb tightens what the format and the processing application must do, and therefore what you must specify in the acquisition.

- **Maturity as fitness, not prestige.** Table 8's maturity levels are a tool for matching format dynamics to intended utilization, not a scoreboard where higher is always better. Pick the level that fits the reuse and interoperability you actually need; the "specify when" conditions are the decision gate, and the appendix still tells you to validate against current technology trends from other sources.

- **The copy-out clock starts immediately.** The moment data leaves its authoritative source as a manual copy, treat it as potentially stale — a clock starts and the source's edits no longer reach it. This reframes manual copying from a convenience into a standing program risk, and reframes automated integration and audits as the way to stop or reset that clock.

- **Interoperability is agreement, not consolidation.** The depth of shared agreement on base elements and flow configuration — not the visible number of systems — is the real lever. Reducing the count of systems can look like progress while doing little for actual data sharing.

- **MBE solutions cannot rescue bad source choices.** Even a perfect MBE solution cannot overcome incompatibility decisions made at the source. Configuration, accuracy, identification, and similar settings that engineers enact inside the same tool determine how hard their data is to share. Interoperability work therefore begins outside the MBE tool and reaches into manufacturing, procurement, logistics, and mission-operations interfaces.

## Anti-patterns

- **Specifying paper or formatted-document levels under MBE.** The appendix explicitly states that Level 1 (Paper) and Level 2 (Formatted Documents / electronic paper) are neither recommended nor supported under MBE. Choose them only when reuse and life-cycle maintenance of materials are genuinely not wanted — and recognize that doing so steps outside the MBE approach.

- **Treating PDM consolidation as data sharing.** Consolidating instances of product data management (PDM) can shrink the visible system count while doing little to advance the real goals of improved bi-directional internal and external sharing. Creating multiple partitions inside one installation — each owner reproducing their own processes, structures, and settings — reduces visible "systems" but does not guarantee data exchange.

- **Assuming no-customization equals no complexity.** Because process definition is integral to MBE, the flexibility built into native tools means that even a solution with no customization at all can still breed complexity and get in the way of data sharing. Minimizing customization and adapting external standards reduces complexity and eases future upgrades and external exchange, but flexibility alone is not a safeguard.

- **Globally rigid process definitions / over-specification.** Defining one rigid, globally applicable process that must accommodate every type of work is discouraged. Instead, pursue the core definition of the critical interoperability-related processes and look for commonality around collaboration and data sharing, so over-specification is avoided and adaptability is encouraged.

## Key Takeaways

1. **Run all four use cases before fixing requirements.** Viewing, Data Exchange, Data Integrity, and Data Interoperability Formats are the planning lens; correlate them with Table 6 so tool, exchange, and access decisions follow real usage rather than assumption.

2. **Let the heaviest required use case set the format bar.** Each use case raises demands on format and processing application; specify to the most demanding case you genuinely need, and capture IP-protection and PMI-processing expectations in the DRD.

3. **Keep PMI and metadata distinct.** Metadata is text-only description; PMI carries 3D annotations, manufacturing notes, and material specs. Their differing demands on the format must be reflected in what you require, including whether PMI must be processable after exchange.

4. **Attack the manual-copy problem directly.** Manual copying out of authoritative sources is the default practice and the default risk. Favor automated data integration to minimize non-authoritative copies and automated data audits (daily/weekly) to drive convergence and protect baselines — high utility at relatively low cost.

5. **Hold both forms of data integrity.** Protect integrity relative to the authoritative source (information-security view) and relative to the authoritative model (database view, spanning component and composite integrity). Automation is the primary route from manual integration and validation to reliable, automated processes.

6. **Anchor formats in standards and a common data dictionary.** Follow STEP and XML where applicable; use STEP AP 242/239/233 (ISO 10303) plus RQF/RIF for requirements; and ensure Level 3 XML and Level 4 repository-to-repository exchange reference a NASA (or contractor) common data dictionary, with a schema catalog in place before delivery.

7. **Treat interoperability as negotiated agreement on base elements.** The depth of agreement on data objects, flow steps, descriptors, roles, and decision rules — not the number of systems — is the primary interoperability mechanism. Pursue the core critical processes rather than one rigid global definition.

8. **Make the PM and Technical Authority answer the interoperability questions.** The program/project manager and delegated Technical Authority must address a defined question set: how peers share design data; what is sufficient and necessary to define at part/assembly/system levels; how parts are named to avoid conflict and redundancy; what models mean for each purpose; how alternate model versions are related and traced; what practices reduce the effort to find and reuse approved part definitions; what state labels and process steps govern allowed uses and change status across the life cycle; and what defines an approved product structure for a given use, audience, or life-cycle state.

## Connects To

- **NASA-HDBK-1009A** — the named companion handbook this material pairs with; read the two together when establishing MBE elements and interoperability requirements.
- **Table 6 (NASA-HDBK-1004)** — the MCAD format menu against which all four use cases are correlated and from which formats are currently selected.
- **Table 8, Format Maturity Levels, and NIMA-RPT-004** — the maturity-level framework and its referenced source for judging format dynamics against intended utilization.
- **NIMA-RTP-002, *Data Integrity in NASA Programs and Projects*** — the white paper grounding the Data Integrity use case and tracing data-integrity requirements to NASA Procedural Requirements.
- **STEP / ISO 10303 (AP 242, AP 239, AP 233), RQF, and RIF** — the interoperability standards for exact-geometry and requirements exchange.
- **NASA common data dictionary** — the shared semantic reference required for usable Level 3 standard XML descriptions and Level 4 repository-to-repository exchange.
- **Data Requirements Description (DRD)** — where exchange expectations, IP-protection considerations, and PMI-processing requirements derived from these use cases are formally recorded.
- **Program/Project Manager and delegated Technical Authority** — the roles accountable for answering the process-interoperability question set and for driving agreement on base elements and flow configuration.
