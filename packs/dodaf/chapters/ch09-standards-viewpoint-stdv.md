# Chapter 9: Standards Viewpoint (StdV)

## Core Idea
The Standards Viewpoint captures the **rules governing the arrangement, interaction, and interdependence** of parts of a described architecture. It translates organizational-level standards profiles into architecture-specific rule sets, ensuring solutions comply with operational, business, technical, and industry requirements. Two models — a current profile (StdV-1) and a forecast (StdV-2) — together describe both the present standards landscape and its anticipated evolution.

## Frameworks Introduced
- **StdV-1: Standards Profile**: Identifies and describes the rules currently constraining activities and their performers within the described architecture. Includes doctrinal, operational, business, technical, and industry standards. Technical standards portions must be drawn from the DoD Information Technology Standards and Profile Registry (DISR).
  - When to use: When documenting current compliance requirements; at any architecture milestone to establish the standard-to-activity traceability; for acquisition specifications and systems engineering standards compliance.
- **StdV-2: Standards Forecast**: Identifies and describes rules that will constrain activities in the future — foreseeable successions of standards. Adds before-after temporal relationships to the StdV-1 base. May also look at historical successions.
  - When to use: During technology refresh planning, long-term acquisition strategy, and systems evolution planning; to anticipate standards retirement and emergence.

## Key Concepts
- **Standards Profile** — A collection of doctrinal, operational, business, technical, or industry standards, implementation conventions, standards options, rules, and criteria organized to govern solution elements for a given architecture.
- **Technical Standard** — A type of rule (subtype of Standard) governing technical implementation; typically drawn from the DISR for DoD IT systems.
- **Functional Standard** — A type of rule governing the functional behavior of activities and performers; may be doctrinal, operational, or business in nature.
- **DISR (DoD Information Technology Standards and Profile Registry)** — The authoritative source for technical standards in DoD IT architectures; StdV-1 technical standards must come from the DISR.
- **Standards-Activity Relationship** — In StdV, standards are related directly to activities, not to performers: a performer is bound by a standard only through the activity it performs. The same performer in different roles for different activities may be governed by different standards.
- **Condition on Standards** — Standards may apply conditionally: a given rule applies to an activity under specified conditions. Conditions must be modeled when constraints are environment-dependent.
- **BeforeAfter in StdV-2** — Temporal ordering relationships showing that one standard succeeds another at a specified future time; enables transition planning from deprecated to replacement standards.

## Mental Models
- Use StdV-1 as the compliance checklist: for every activity in the architecture, identify the standards that govern it and the conditions under which each applies.
- Use StdV-2 as the standards migration roadmap: map the succession from current standards (StdV-1) to future standards, aligned with project delivery timelines from PV-2.

## Anti-patterns
- Relating standards to performers rather than activities: DoDAF explicitly routes standards to activities; performers inherit standards constraints only through the activities they perform. Direct performer-standard relationships are a modeling error in the Standards Viewpoint.
- Producing a StdV-1 without DISR traceability for technical standards: for DoD IT architectures, technical standards that cannot be traced to the DISR are non-compliant.
- Using StdV as a substitute for a Configuration Management plan: StdV documents architectural standards constraints; it is not a full configuration management artifact.

## Key Takeaways
1. Standards are a subtype of Rule in the DM2 — StdV models are technically a focused view of the Rules data group applied to activities.
2. Standards bind performers only through activities: the same organization using the same system in different activity roles may be subject to completely different standards.
3. StdV-1 is current-state; StdV-2 is future-state. Together they provide a temporal span of standards applicability aligned with the architecture's lifecycle.
4. DISR is mandatory for technical standards in DoD IT architectures — this is a compliance requirement, not a recommendation.
5. StdV-2 can look backward (historical standard successions) as well as forward — useful for understanding legacy standard evolution and for grandfathering analysis.

## Connects To
- **Chapter 2 (DM2 Data Groups)**: StdV is a focused expression of the Rules data group — standards are a subtype of rules in the DM2.
- **Chapter 6 (Operational Viewpoint)**: OV-6a captures operational rules including doctrine; StdV-1 captures the technical and industry standards complement — together they provide full rule coverage.
- **Chapter 5 (DIV)**: DIV-3 data implementations must comply with metadata standards established in StdV-1.
- **Chapter 7 (Project Viewpoint)**: PV-2 project schedules should align with StdV-2 standards transition timelines to ensure systems are built to the correct generation of standards.
- **Chapter 11 (Systems Viewpoint)**: SV-10a (System Rules) and StdV-1 are complementary — SV-10a focuses on system-specific rules; StdV-1 focuses on doctrinal, business, and technical standards at the architectural level.
