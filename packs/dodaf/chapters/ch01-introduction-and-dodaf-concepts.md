# Chapter 1: Introduction and DoDAF Concepts

## Core Idea
DoDAF 2.02 Volume II is a practitioner's reference for architects who develop, use, and maintain architectural descriptions within the Department of Defense. Its organizing premise is that architecture work should be **data-first and fit-for-purpose**: the DoDAF Meta-Model (DM2) provides a shared ontology, and viewpoint models are optional presentation lenses over that data — chosen by decision-maker need, not by DoDAF mandate.

## Frameworks Introduced
- **DoDAF Meta-Model (DM2)**: The formal ontology underpinning all DoDAF architectural data. Grounded in the IDEAS Foundation and expressed via Sparx Enterprise Architect with IDEAS stereotypes. Provides standard glossary terms, types, and relationships usable across all six DoD core processes.
  - When to use: As the shared data foundation whenever creating or exchanging architectural descriptions within the DoD enterprise.
- **Fit-for-Purpose Architecture**: DoDAF does not require architects to produce all viewpoint models; only those models needed to support identified decision-maker needs are required.
  - When to use: When scoping any architecture effort — start with the decisions that must be made, then select only the models that address those decisions.
- **Six DoD Core Processes**: JCIDS, DAS, PPBE, Systems Engineering, Operations, and Portfolio Management (IT and Capability). DoDAF data groups and viewpoints are designed to serve all six simultaneously.
  - When to use: When mapping an architecture effort to DoD acquisition or planning cycles.

## Key Concepts
- **Architectural Description** — A set of products (models, data) that document an architecture. Two subtypes are called out: the AV-1 executive summary and the manifest (for discovery and exchange).
- **DM2 (DoDAF Meta-Model)** — The formal ontology specifying all types, relationships, and naming conventions used in DoDAF architectural data. Available as a Sparx Enterprise Architect model file using the IDEAS add-in.
- **IDEAS Foundation** — The four-dimensional, meronymic ontological foundation underlying the DM2. Instances are spatio-temporal extents; the ontology is meronymic (wholes and parts).
- **Stereotypes (IDEAS UML)** — Color-coded UML class symbols used in DM2 diagrams: «Individual» (grey), «Type» (pale blue), «IndividualType» (light orange), «TupleType» (light green), «Powertype» (lavender), «Name» (tan), «NamingScheme» (yellow).
- **Fit-for-Purpose** — The guiding principle that DoDAF architecture products should be selected based on the decisions to be supported, not on completeness for its own sake.
- **Viewpoint** — A presentation perspective on architectural data designed for a specific audience and purpose. DoDAF defines eight viewpoints: AV, CV, DIV, OV, PV, StdV, SvcV, SV.
- **Data Group** — A semantically cohesive cluster of DM2 concepts forming a building block of architectural descriptions. Eight principle data groups and three supporting data groups.

## Mental Models
- Use the DM2 as a lingua franca: all DoDAF products are views over a common data store — produce the data once, present it many ways.
- Use fit-for-purpose as the first filter: ask "what decision does this architecture support?" before selecting any model.

## Key Takeaways
1. Volume II serves architects and technical professionals, not general readers; it assumes familiarity with enterprise architecture concepts.
2. The DM2 is the ontological foundation — without it, viewpoint models have no shared semantic grounding.
3. The IDEAS Foundation gives the DM2 its four-dimensional (spatio-temporal) and meronymic (whole-part) character, which makes the model more rigorous than typical UML-based frameworks.
4. Fit-for-purpose is not a waiver — it is the designed intent; architects must justify model selection against decision-maker needs.
5. All six DoD core processes (JCIDS, DAS, PPBE, SE, Ops, PfM) are served by the same underlying DM2 data; viewpoints are the process-specific presentations.

## Connects To
- **Chapter 2 (DM2 Data Groups)**: The DM2 concepts introduced here are elaborated in detail as eight principle data groups.
- **Chapter 3 (All Viewpoint)**: The AV models (AV-1, AV-2) are the first presentation layer over DM2 data.
- **Chapter 4–11 (Viewpoints)**: Each viewpoint selectively draws on DM2 data groups for its specific audience.
