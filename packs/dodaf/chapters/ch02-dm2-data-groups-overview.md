# Chapter 2: The DoDAF Meta-Model (DM2) — Data Groups Overview

## Core Idea
The DM2 organizes all DoDAF architectural concepts into **eleven data groups** — eight principle groups and three supporting groups. These groups are the semantic building blocks from which every viewpoint model is composed. The principle groups describe behavior and structure; the supporting groups add properties and attributes. Each group maps to specific DoD core processes and specific viewpoints, establishing a traceable path from raw architectural data to process-supporting presentations.

## Frameworks Introduced
- **Principle Data Groups (8)**: Performers, Resource Flows, Information and Data, Rules, Capabilities, Services, Projects, Organizational Structures — the core behavioral and structural building blocks.
  - When to use: When populating architectural data that must serve process decisions (JCIDS, DAS, PPBE, SE, Ops, CPM).
- **Supporting Data Groups (3)**: Measures, Locations, Pedigrees — properties applied to principle groups.
  - When to use: When adding quantitative, spatial, or provenance attributes to any principle-group element.
- **Data Group to Viewpoint/Process Mapping (Table 3.3-1)**: A cross-reference table showing which data groups appear in which viewpoints (AV, CV, DIV, OV, PV, StdV, SvcV, SV) and which DoD processes (JCIDS=J, DAS=D, PPBE=P, SE=S, OPS=O, CPM=C) each group serves.
  - When to use: When scoping an architecture to a specific process — consult the table to identify which data groups are required.

## Key Concepts
- **Performer** — Any entity (human, automated, or composite) that performs an activity and provides a capability. Subtypes include persons in roles, organizations, systems, and services. Activities are assigned or allocated to performers.
- **Resource Flow** — The behavioral and structural representation of interactions between activities, capturing connectivity, content, order, and quality-of-service attributes. Activity-based, not performer-based: resources flow because activities produce or consume them.
- **Information** — The state of a something-of-interest that is materialized and communicated or received. Describes things in a semantic form (what it means and who uses it).
- **Data** — The formalized representation of information for repeatable communication or processing. Operates at conceptual, logical, and physical abstraction levels.
- **Rule** — A principle or condition that governs behavior. Constrains activities. Subtypes include guidance, agreements, functional standards, and technical standards. Distinct from Activity: a rule prescribes how an activity may be carried out, not what is produced.
- **Capability** — The ability to achieve a desired effect under specified standards and conditions through combinations of ways (rules/guidance) and means (resources/performers) to perform a set of tasks. Desired effects are resource states.
- **Service** — A mechanism that enables access to a set of capabilities through a prescribed interface, exercised consistent with service policies. A service is a type of performer.
- **Project** — A temporary endeavor undertaken to create desired states of resources. Contains a WBS; primary instrument connecting architecture to DAS and PPBE processes.
- **Organizational Structure** — Representations of organization types, specific organizations, and persons in roles within the scope of a described architecture.
- **Measure** — The magnitude of some attribute of an individual. Subtypes: Measure of Effect, Measure of Desire, Performance Measure, Needs Satisfaction Measure, Physical Measure, Temporal Measure, Service Level.
- **Location** — A point or extent in space (physical or logical). Applied to performers, activities, and resources.
- **Pedigree** — The origin and history of a resource; the background and provenance of something in the architecture.

## Mental Models
- Use "Performer = who, Activity = what, Resource = with what/to what": this triad underlies every DM2 relationship and every viewpoint model.
- Use the process-mapping table before selecting models: if the architecture must satisfy PPBE, check which data groups carry PPBE-relevant data (performer, capability, project, rules, measures, location) and ensure those groups are populated.
- A Rule is not an Activity: activities transform resources; rules constrain how activities may be carried out.

## Anti-patterns
- Confusing information with data: information is semantic (meaning-bearing); data is syntactic (encoded for processing). The DM2 tracks both separately because requirements work needs information models and implementation work needs data models.
- Treating services as IT-only constructs: DoDAF services include non-IT services such as search and rescue; the service type is any capability realized by a service-performer.

## Key Takeaways
1. All eleven data groups feed the same shared DM2 data store; viewpoints are read-only presentations over that store.
2. The performer-activity-resource triad is the invariant kernel of every DoDAF model regardless of viewpoint.
3. Rules constrain activities, not performers directly; performers are governed by rules only through the activities they perform.
4. Capabilities are about desired resource states (effects), not about performers or activities in isolation.
5. Projects are themselves activities in the DM2 — a project produces resources and is performed by organizations; this is the integration point between architecture and acquisition/budgeting.
6. Measures, Locations, and Pedigrees are attribute groups — they do not stand alone but enrich principle-group elements.

## Connects To
- **Chapters 3–11 (Viewpoints)**: Every viewpoint selectively draws on the data groups described here.
- **Chapter 4 (All Viewpoint)**: AV-2 Dictionary is the viewpoint-level expression of the DM2 glossary.
- **Chapter 6 (DIV)**: The three-level information model (conceptual/logical/physical) directly maps to the Information and Data group's abstraction hierarchy.
