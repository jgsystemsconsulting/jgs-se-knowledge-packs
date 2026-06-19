# Chapter 3: All Viewpoint (AV)

## Core Idea
The All Viewpoint provides overarching context for an entire architectural description. Its two models — the Executive Summary (AV-1) and the Dictionary (AV-2) — capture scope, intent, assumptions, constraints, and the vocabulary needed to understand every other model in the architecture. AV models are also the registration artifacts for the DoD Architecture Repository System (DARS), making them the discovery interface for the broader enterprise.

## Frameworks Introduced
- **AV-1: Executive Summary**: A narrative and graphic overview of the architecture's purpose, scope, subjects, period of coverage, and significant organizations. Required for DARS registration; enables quick comparison across architectural descriptions.
  - When to use: At the start of every architecture effort to establish scope and for DARS registration; also used when briefing executive-level decision-makers.
- **AV-2: Glossary (Integrated Dictionary)**: Defines all terms needed to understand a described architecture, their definitions, and their architecturally significant relationships. Organizes concepts using the DoDAF genus terms (activity, resource, project, location, guidance, vision, property) as root categories, then extends them via super-subtype and whole-part relationships.
  - When to use: Whenever multiple communities of interest share an architecture — AV-2 establishes the authoritative vocabulary, reducing ambiguity; also used to document authoritative sources for term definitions.

## Key Concepts
- **AV-1 Model** — Presents purpose, scope, and subjects of an architecture effort. No prescribed content beyond what is needed for DARS registration (which does impose format requirements). Should be consistent with OV-1.
- **AV-2 Model** — A data model of terms and their definitions and relationships within the architecture. Not a data dictionary of data elements (that is DIV-3 scope); rather, a conceptual-level dictionary of enterprise concepts.
- **Genus-Differentia Definition** — The classical definition style used by AV-2: a term is defined by stating its genus (broader category in the DoDAF taxonomy) and its differentia (how it differs from other concepts in the same genus). Example: "a human being is a featherless biped" where "biped" is the genus and "featherless" is the differentia.
- **DARS (DoD Architecture Repository System)** — The DoD registry for architectural descriptions. AV-1 models are the registration artifact; AV-2 supports discovery by establishing the vocabulary.
- **DoDAF Genus Terms** — The seven root categories provided by DoDAF for taxonomical classification: activity, resource, project, location, guidance, vision, property. Every AV-2 term must be rooted in one of these.
- **Authoritative Source** — An AV-2 model may cite authoritative sources for term meanings it does not define itself, enabling federation of vocabulary across communities.

## Mental Models
- Use AV-1 as the architecture's title page and table of contents: it anchors every subsequent model to a named scope and purpose.
- Use AV-2 as the Rosetta Stone: when two communities of interest use different terms for the same concept, AV-2 makes the mapping explicit by assigning both terms to the same genus-differentia definition.

## Anti-patterns
- Confusing AV-2 with DIV-3: AV-2 defines conceptual terms and their relationships; DIV-3 defines data elements and their physical implementations. Putting data element specifications in AV-2 creates scope confusion.
- Skipping AV-1 because "it is just a summary": AV-1 is the DARS registration artifact; without it, the architecture is invisible to the broader DoD enterprise and cannot be discovered or referenced by other architectures.

## Key Takeaways
1. All Viewpoint models are the only DoDAF models required for DARS registration; all other models are fit-for-purpose choices.
2. AV-2 uses the DoDAF genus terms as mandatory root categories, ensuring all vocabulary is grounded in the DM2 ontology.
3. AV-1 has no prescribed content beyond DARS requirements; architects have full latitude over format and detail level.
4. AV-2 synonyms are permitted only when their meanings are identical to the corresponding DoDAF term — the AV-2 is not a place for terminological creativity.
5. The AV models together preserve architecture continuity through leadership and organizational changes by documenting intent, not just content.

## Connects To
- **Chapter 2 (DM2 Data Groups)**: AV-2 is the viewpoint expression of the DM2 glossary; genus terms map directly to DM2 principle concepts.
- **Chapter 7 (Operational Viewpoint)**: AV-1 correlates with OV-1 (Operational Concept Graphic) — both provide overview; they must be consistent.
- **All other viewpoints**: Every model in the architecture must be interpretable using the vocabulary established by AV-2.
