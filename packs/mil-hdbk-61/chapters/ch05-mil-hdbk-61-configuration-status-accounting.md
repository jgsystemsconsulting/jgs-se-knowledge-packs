# Chapter 5: Configuration Status Accounting (CSA)

> Source basis: MIL-HDBK-61B, Section 7. Use the current **MIL-HDBK-61B**, not the 2001 MIL-HDBK-61A(SE).

## Core Idea
Configuration Status Accounting is the function that builds and maintains the knowledge base CM runs on. MIL-HDBK-61B casts CSA as the process of creating and organizing the information needed to perform configuration management, and — beyond serving CM itself — as the supplier of a high-reliability source of configuration information to every part of a program. That reach is deliberately broad: the handbook names program management, systems engineering, manufacturing, software development and maintenance, logistics support, modification, and maintenance as consumers of CSA output. In other words, CSA is not a CM clerical task; it is the authoritative record of what the configuration *is*, *was*, and is *becoming*, made available to the whole enterprise.

## Frameworks Introduced
- **CSA inputs-and-outputs model (Figure 7, "Status accounting objects")** — the handbook frames CSA as a set of generic input and output categories whose specific content changes as the item moves through its life cycle. The same object types are accounted for throughout, but the particulars differ in each phase.
  - When/how: use it to reason about *what* status data exists at a given moment. The figure stresses that CSA evolves over the life cycle, capturing progressively more detailed information and growing in value as an information resource as the system matures across Material Solution Analysis, Engineering & Manufacturing Development, Production & Deployment, and Operations & Support.
- **CSA process / activity model (Figure 8, "Configuration Status Accounting Activity Model")** — a high-level summary of CSA tasks that spans both Government and contractor activity, driven by contractual provisions and CM planning, and resting on a documented CM process and an automated CM system built around a CM data model and data element dictionary.
  - When/how: use it as the task checklist for standing up status accounting on a program — it enumerates the records and reports CSA must produce (see Key Concepts).
- **Typical-information table over the life cycle (Table I)** — a phase-by-phase mapping of typical CSA *information sources* to typical *outputs* for MSA/TMRR, EMD, Production & Deployment, and Operational Support phases.
  - When/how: use it to scope what CSA must capture and report in a specific acquisition phase, and to see how each phase inherits and extends the prior phase's items.

## Key Concepts
- **Purpose of CSA**: organize the configuration knowledge base so CM can function, and supply reliable configuration information to all program activities — management, engineering, manufacturing, software, logistics, modification, and maintenance.
- **The core CSA tasks** (from the activity model) — record and report on:
  - the current approved configuration documentation and configuration identifiers tied to each system/CI;
  - the status of proposed engineering changes from initiation through approval to contractual implementation;
  - the status of critical and major requests for deviation affecting a system/CI;
  - the results of configuration audits, including disposition of discrepancies and action items;
  - the implementation status of authorized changes, with full traceability back to each item's originally released documentation;
  - the effectivity and installation status of changes across all system/CI copies at every location — covering design, production, modification, retrofit, and maintenance changes;
  - the digital data file identifiers and document representations for every revision/version of each document and software item delivered or made electronically accessible under the contract.
- **CSA tools**: the handbook states the complete CSA function can be captured and supplied with commercial CM and product data-management tools; linking those to logistics and maintenance systems is what lets CSA information evolve coherently across the life cycle.
- **Division of CSA data between Government and contractor**: the Government's range of CSA information is normally bounded by what it has configuration control over and the items it supports logistically; the contractor monitors data for the items it supports.
- **Shared warranty data**: warranty information is a named case of data that must be shared. The Government needs to know each item's warranty period and the warranty start date per serial number; logistics personnel using that data to prioritize return-for-repair shipments can save the Government money. The handbook flags this as an example of Government adapting to standard industry practice.
- **Baselines as queryable states**: Table I outputs repeatedly call for configuration as of *any prior date* and *current* — as-designed, as-built, as-delivered, and (in later phases) as-modified/as-maintained — plus FBLs, ABLs, and PBLs for both Government and contractor.
- **Phase inheritance**: each life-cycle phase's CSA scope explicitly includes all items from the prior phase and adds its own (e.g., Production & Deployment carries forward "all development phase items" and adds location-by-serial-number, support equipment, spares, trainers, and the rest).

## Mental Models
- **CSA is the system's memory, not its filing cabinet.** Its job is not to store documents but to answer questions — *what is the approved configuration of this serial number right now? what was it on this date? which changes are incorporated where?* If a question about configuration can't be answered from CSA, the function is incomplete.
- **Same questions, different answers per phase.** The input/output categories are generic and stable; what changes across MSA → EMD → Production → Operations is the specific content. Think of CSA as one ledger whose entries grow richer, not as a new system per phase.
- **As-X is a query, not a document.** As-designed, as-built, as-delivered, as-modified/as-maintained are different *views* the same status accounting system must be able to render — current and retrospectively to any prior date.
- **CSA value compounds over time.** The handbook explicitly frames CSA as growing in value as an information resource as detail accumulates over the life cycle — the longer it is fed faithfully, the more it can answer.
- **One ledger, two custodians.** Government and contractor each own the slice they control or support; the seams (warranty being the canonical one) are where data must be shared deliberately rather than assumed.

## Key Takeaways
1. CSA creates and organizes the CM knowledge base and serves as the reliable configuration-information source for the entire program, not just CM.
2. Its inputs and outputs are generic categories whose specifics evolve phase by phase (Figure 7).
3. The activity model (Figure 8) spans Government and contractor work and rests on a documented CM process plus an automated CM system built on a data model and data element dictionary.
4. The core deliverables are *records and reports*: approved configuration, change status, deviation status, audit results, change implementation with traceability, effectivity/installation status, and digital data file identifiers.
5. CSA must render configuration both currently and as of any prior date — as-designed, as-built, as-delivered, as-modified/as-maintained.
6. Commercial CM and product DM tools, linked to logistics and maintenance systems, are sufficient to perform the full function.
7. Government and contractor each account for the data they control or support; warranty data is a key shared item where industry practice is adopted.
8. For activity guides, templates, and further detail, MIL-HDBK-61B points to **GEIA-HB-649, Configuration Status Accounting Function**.

## Connects To
- **CM identification and change management chapters (this pack)**: CSA records the very things identification establishes (approved documentation, configuration identifiers, baselines) and tracks the things change management produces (ECPs, RFVs, effectivity).
- **Configuration audit chapter (this pack)**: CSA records and reports audit results and the disposition of discrepancies and action items.
- **GEIA-HB-649**: the handbook's named reference for CSA activity guides, templates, and additional detail.
- **`dau-se-guidebook` pack**: situates CSA inside the broader configuration management and technical-data-management discipline.
- **`nasa-npr-7123` / `nasa-se-handbook` packs**: parallel configuration management and status accounting expectations in the NASA SE framework.
