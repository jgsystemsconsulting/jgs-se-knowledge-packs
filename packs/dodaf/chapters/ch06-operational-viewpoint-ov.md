# Chapter 6: Operational Viewpoint (OV)

## Core Idea
The Operational Viewpoint focuses on **what needs to happen and who needs to do it**, deliberately excluding implementation means (systems, services, materiel) except where those means act as constraints. OV models describe organizational performers, the activities they perform, the resources they consume and produce, and the rules, conditions, and sequences governing those activities. The OV is the "as-operated" or "as-required" view — technology-independent by design.

## Frameworks Introduced
- **OV-1: Operational Concept Graphic**: A free-form graphical (or video) overview of the architecture with explanatory text. No prescribed content, no meta-model. Correlates with AV-1.
  - When to use: For executive briefings, stakeholder communication, and putting a mission or scenario into context. Always produced; used throughout the architecture lifecycle.
- **OV-2: Organizations and Resources**: Shows resources consumed and produced by organizational performers, emphasizing the exchange of information and materiel between organizations. Activities are shown only at the level needed to reveal resource flows.
  - When to use: When the primary concern is which resources flow between organizations; a subset of OV-3 data with reduced activity detail.
- **OV-3: Organizations, Activities, and Resources**: The full resource-flow matrix — adds measures (performance, timeliness, physical) to OV-2's base. The superset that includes all data shown in OV-2 plus measures.
  - When to use: When resource exchanges between organizations must be quantified; for interface definition and interoperability analysis at the operational level.
- **OV-4: Organizational Relationships**: Shows structure and relationships among organizations — whole-part hierarchy, resource exchanges, and (optionally) skills of persons in roles. Activities are explicitly excluded.
  - When to use: For org-chart style analysis; to reveal command relationships, subordinate/superior structures, and inter-organizational dependencies.
- **OV-5a: Operational Activity Hierarchy**: A proper subset of OV-5b showing only the hierarchical decomposition of activities (whole-part and super-subtype) without performers, resources, or locations.
  - When to use: For a clean activity decomposition view; to analyze and validate activity hierarchies independently of who performs them.
- **OV-5b: Operational Activities**: The full activity model — activities with their performers, consumed/produced resources, rules, conditions, locations, and measures. OV-5a is a strict subset of OV-5b.
  - When to use: As the primary operational model; the source of activities that feed CV-6, SV-5a/5b, and SvcV-5.
- **OV-6a: Operational Rules**: Documents rules (business rules, doctrine, constraints) that govern organizational activities. Includes conditions under which rules apply.
  - When to use: When documenting doctrine, TTPs, or operational constraints for compliance or analysis.
- **OV-6b: Operational State Transitions**: Models states of resources consumed and produced by activities, and the transitions between states in response to events.
  - When to use: When the state-change behavior of key resources must be understood; for real-time or mission-critical operational analysis.
- **OV-6c: Operational Activity Sequences**: Sequence and event-trace models showing the temporal ordering of activities across organizational performers.
  - When to use: For mission-thread analysis; to verify that activities occur in the correct sequence and that handoffs between organizations are well-defined.

## Key Concepts
- **Organizational Performer** — An organization or person in a role; a performer capable of responsibility. The OV deals only with organizational performers, not with systems, services, or materiel as performers (those belong in SV and SvcV).
- **Operational Activity** — An activity performed by an organizational performer to consume or produce resources. Ontologically synonymous with tasks in the DM2; "operational activity" is the OV-specific label.
- **Resource Flow** — The dependency between a resource produced by one activity and consumed by another. In the OV, flows are between organizational performers, not between systems.
- **Condition** — The operational environment (environment, threat, weather) under which activities are performed; shapes which activities, which performers, and which rules apply.
- **OV-5a/5b Relationship** — OV-5a is a proper subset of OV-5b: it contains exactly the activity decomposition data from OV-5b with no additions or alterations. An OV-5a may not introduce new activities.
- **OV-2/OV-3 Relationship** — OV-2 is a proper subset of OV-3: OV-3 is the superset that adds measures of activities and resources to the OV-2 base.
- **Mission Thread** — A critical path of activities and resource exchanges that must succeed for a mission to succeed; identified and annotated in OV-6c and OV-5b models.

## Mental Models
- Use OV before SV/SvcV: the OV establishes what must happen operationally; the SV and SvcV then identify how systems and services support those operational activities. Never design systems without first establishing the operational need in the OV.
- Use OV-6c for mission-thread analysis: trace the sequence of activities from initiation to effect, identify the critical path, and find single points of failure.

## Anti-patterns
- Including systems or services as performers in OV models: the OV treats systems and services as constraints (means available) or as resources, not as primary performers. Systems as performers belong in SV; services in SvcV.
- Producing only OV-1 for executive communication and skipping OV-5b: OV-1 has no meta-model and cannot stand alone for rigorous analysis; OV-5b is the authoritative activity model.

## Key Takeaways
1. The OV is deliberately technology-independent: systems and services appear only as constraints, not as the primary subject.
2. OV-5a is always a strict, read-only subset of OV-5b — architects must produce OV-5b first, then derive OV-5a from it.
3. OV-2 and OV-3 examine the same resource flows; OV-3 adds the quantitative layer (measures) needed for interface definition.
4. OV-6a, OV-6b, and OV-6c together provide the rules, state, and sequence dimensions of operational behavior — a complete behavioral specification requires all three.
5. OV models are the primary source for CV-6 (activities in capabilities), PV-1 (organizations in projects), and SV-5a/b (system-to-operational activity mappings).

## Connects To
- **Chapter 4 (Capability Viewpoint)**: CV-6 maps capabilities to activities; those activities are defined in OV-5b.
- **Chapter 8 (Project Viewpoint)**: PV-1 references organizations identified in the OV.
- **Chapter 9 (Services Viewpoint)**: SvcV-5 maps service activities to operational activities from OV-5b.
- **Chapter 11 (Systems Viewpoint)**: SV-5a/5b maps system functions to operational activities defined in OV-5b.
- **Chapter 5 (DIV)**: OV-3 information resources flow into DIV-1 and DIV-2 as the starting point for information modeling.
