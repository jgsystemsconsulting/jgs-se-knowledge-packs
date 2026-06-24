# Chapter — ConOps Template with Model Content

## Core Idea

A Concept of Operations describes, in plain narrative, what a system is for and how it will be used across its life. NASA-HDBK-1009A's Appendix F takes that narrative skeleton and shows, section by section, where a model can do the talking. It does this by reproducing the annotated ConOps outline already published in the NASA Systems Engineering Handbook (its Appendix S), then dropping in example MBSE diagrams and tables wherever a model view supports that section. The outline text itself is left unchanged — the appendix's contribution is the overlay: representative diagrams pulled from the handbook's own modeling sections (8 and 9), plus commentary in callout boxes explaining which model views earn their place where.

The result is a worked bridge between a required document and a system model. Instead of authoring ConOps prose and a model as two disconnected efforts, the appendix demonstrates that the same model content can populate the document — a context block diagram drawn once can serve the system overview, the interfaces section, and more; a requirements table can carry the needs, goals, and objectives; state machines can stand in for the modes-of-operations description. The caveat that governs the whole handbook applies here too: this is tool-agnostic SysML tied to NPR 7123.1, current as Rev A (2025). The diagrams happen to be expressed in SysML, but the appendix presents them as one way to satisfy each ConOps section, not as a mandate, and the modeling choices are repeatedly described as the modeler's or stakeholders' to make.

## Frameworks Introduced (exact source names, when/how)

- **ConOps Annotated Outline (drawn from the NASA Systems Engineering Handbook, Appendix S)** — The structural backbone of the chapter. Appendix F states it is a replica of the outline and descriptions from Appendix S, with the outline shown in bold and the descriptions in italics; the MBSE material is added around it. This keeps the document structure authoritative to the SE Handbook while the model content is layered on top.
- **NASA Systems Engineering Handbook** — Named as the home of the original ConOps outline that Appendix F reproduces.
- **Sections 8 and 9 of NASA-HDBK-1009A** — Cited as the origin of every example diagram and table. The appendix repeatedly annotates a figure with "shown in section 8.x," signalling that the ConOps views are not bespoke to the appendix but reuse the handbook's core modeling examples (system context bdd in 8.3, system context ibd in 8.4, requirements diagram in 8.2, use cases in 8.5, activity diagrams in 8.6, structural interconnection ibd in 8.8).
- **Design Reference Mission (DRM)** — Introduced in Section 6.0 as one of the three thread-level constructs (alongside scenarios and use cases) used to walk through how the system functions along a single timeline. The appendix recommends labelling each thread for traceability, giving the example tags [DRM-0100] and [DRM-0200].
- **SysML behavior and structure diagram kinds** — Used throughout as the modeling vocabulary: block definition diagram (bdd), internal block diagram (ibd), requirements table and requirements diagram, state machine, activity diagram, sequence diagram, and use case diagram. Each is matched to the ConOps section it best serves.
- **Measures of Effectiveness (MOEs) and Measures of Performance (MOPs)** — Named in the Section 3.2 commentary; a bdd of system and subsystem blocks can carry value properties tied to MOEs and MOPs (Figure F.2-6).

## Key Concepts

**The outline is fixed; the model fills it.** Appendix F does not rewrite the ConOps. It preserves the Appendix S outline verbatim and inserts diagrams, tables, and callout commentary only where modeling adds value. Sections without a strong model story (for example, the Documents section, or the impact and risk narratives) stay primarily textual.

**One diagram, many sections.** The same model element is reused across the document rather than redrawn. The system context bdd appears for the envisioned-system overview (Section 1.2) and again for the overview of system and key elements (Section 3.2), and the appendix explicitly suggests referencing the earlier figure instead of repeating the image. The actors-traced-to-activities-and-use-cases table appears in both Section 3.2 and Section 3.5, because the same use cases and activities that describe users also describe capabilities.

**Section-to-view mapping.** The appendix's working pattern is a recommended pairing of ConOps section to model view:
- *Introduction / overview (1.2)* — context bdd for hierarchy and interface ports; context ibd for element interactions via ports, connectors, and item flows.
- *Needs, goals, objectives (3.1)* — requirements table and requirements diagram of the NGOs.
- *Overview of system and key elements (3.2)* — context bdd; a bdd with value properties tied to MOEs/MOPs; a table of elements with descriptions and allocated activities; a table of actors traced to activities and use cases.
- *Interfaces (3.3)* — context ibd; tables of context interfaces and of interface items; an ibd of structural interconnections.
- *Modes of operations (3.4)* — state machines for modes and transitions; activity or sequence diagrams for systems active in each mode; a table of modes; matrices tracing modes to mission phases and to scenarios/use cases.
- *Proposed capabilities (3.5)* — use case diagrams; functional/activity decomposition diagrams; activity diagram of mission phases; a bdd of mission-phase and activity decomposition; tables of actors and of activities with allocated elements.
- *Physical and support environment (4.0, 5.0)* — environment bdds (a subset of the structural bdd); activity diagrams for maintenance and updates in the support section.
- *Operational scenarios / use cases / DRMs (6.0)* — use case, activity, state machine, and sequence diagrams to capture each thread, both nominal and off-nominal.
- *Risks and potential issues (8.0)* — risk represented as a block with value properties for impact or likelihood, associated to the affected model parts and reported in a table.

**Modes captured as state machines.** For Section 3.4, the example state machine (Figure F.2-13) shows modes as states with "do" activities and transitions driven by signal events. The commentary is careful to note this is a minimal illustration: real models can use entry and exit activities, guards on transitions, and other event types, and mode behavior can be expressed through activities, interactions, or nested state machines.

**Decomposition links Section 3.0 to Section 6.0.** The appendix frames Section 6.0 as the next level of detail below Section 3.0. Where Section 3.0 introduces mission phases, Section 6.0 decomposes the use cases and scenarios within those phases — the same diagrams, taken one level deeper. An activity diagram for a use case such as "Execute Mission Behavior 1" elaborates the steps the use case implies.

**Implementation-free description.** For the system-and-key-elements overview (Section 3.2), the appendix insists the descriptions stay implementation-free — a general statement of what each element is expected to do, not a design. Models support this functional, pre-solution framing rather than committing to a build.

**The model carries traceability the document references.** Tables of actors-to-activities, activities-to-allocated-elements, and matrices tracing modes to phases and scenarios let the ConOps point at relationships the model already holds. Labelling scenarios and DRMs ([DRM-0100], [DRM-0200]) extends that traceability to requirements.

**Even acronyms and glossary live in the model.** The appendices to the ConOps itself (Acronyms, Glossary of Terms) are noted as capturable in model tables, so that supporting reference material is generated from the model rather than maintained separately.

## Mental Models

**The document is a set of viewpoints onto one model.** Rather than writing a ConOps and building a model in parallel, picture a single model with the ConOps sections as windows into it. Each section asks the model a question — what is the scope, what are the interfaces, what are the modes — and a diagram or table answers it. The narrative becomes the glue between views.

**Draw once, reference many.** When a view fits more than one section, the appendix's instinct is to cite the earlier figure, not re-paste it. Treat a diagram as a named asset you link to, so the system context, the use-case set, or the actor table has one authoritative home and several references.

**Pick the behavior diagram that matches the question.** Modes and triggers call for state machines; ordered interactions between components call for sequence diagrams; flow of events and allocation to structure calls for activity diagrams; capability-from-the-user's-view calls for use cases. The appendix repeatedly offers a choice and ties it to what the section is trying to communicate, leaving the selection to the modeler's judgment and the project's needs.

**Model only what drives the design.** For the physical environment section, the appendix's guidance is to capture environment content that will shape the design, not to exhaustively document every condition the system might meet. The model is a decision-support artifact, not an encyclopedia.

**Top-down decomposition is the spine.** Section 3.0 sits above Section 6.0, mission phases sit above scenarios, and a use case sits above its activity-diagram steps. Reading the ConOps top to bottom should feel like zooming progressively into the same model, each section a finer grain of the one before.

## Key Takeaways

- Appendix F overlays MBSE diagrams and tables onto the existing NASA SE Handbook (Appendix S) ConOps outline, leaving the outline text intact and adding model views where they help.
- Every example diagram is drawn from Sections 8 and 9 of the handbook, so the ConOps reuses the core model rather than inventing standalone artifacts.
- A clear section-to-view mapping is offered: context bdd/ibd for overview and interfaces, requirements table/diagram for NGOs, state machines for modes, use cases and activity decomposition for capabilities, and scenario/DRM behavior diagrams for operational threads.
- The same view legitimately serves multiple sections; the appendix recommends referencing a prior figure instead of duplicating it.
- Section 6.0 is the decomposition of Section 3.0 — scenarios, use cases, and DRMs detailed one level below the mission phases introduced earlier — and threads should be labelled (e.g. [DRM-0100]) for requirements traceability.
- State machines for modes can go well beyond the minimal example, using entry/exit activities, guards, and varied event types; the figures are deliberately simple.
- Risk content can be modeled as blocks with impact/likelihood value properties associated to affected elements, though the handbook notes other risk-modeling methods are not covered in this version.
- Reference material such as acronyms and glossary terms can be generated from model tables, keeping the ConOps consistent with the model.
- This remains tool-agnostic SysML tied to NPR 7123.1, current as Rev A (2025): the diagrams are SysML examples illustrating one acceptable way to satisfy each ConOps section, not a required method.

## Connects To

- **NASA Systems Engineering Handbook (Appendix S)** — the source of the ConOps annotated outline that this appendix reproduces and annotates; the authoritative document structure the model fills.
- **Sections 8 and 9 of NASA-HDBK-1009A** — the modeling sections that supply every example bdd, ibd, requirements view, use case, activity, state machine, and sequence diagram reused here.
- **The Metamodel (NPR 7123.1)** — the element-and-relationship schema behind the diagrams; the reason ConOps model content traces back to NASA SE process.
- **Measures of Effectiveness and Measures of Performance** — captured as value properties on system/subsystem blocks in the Section 3.2 view, linking the ConOps overview to quantified expectations.
- **Design Reference Mission, scenarios, and use cases** — the Section 6.0 thread constructs that decompose Section 3.0's mission phases into nominal and off-nominal operational walkthroughs.
- **Requirements engineering (NGOs)** — the needs, goals, and objectives rendered as requirements tables and diagrams in Section 3.1, the starting point for downstream requirements traceability.
