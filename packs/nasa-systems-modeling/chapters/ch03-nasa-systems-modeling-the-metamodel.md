# Chapter — The Metamodel: NASA SE Elements and Relationships

## Core Idea

A metamodel, in this handbook's usage, is a picture of the modeling elements you are allowed to create plus the relationships that legitimately connect them. NASA-HDBK-1009A defines its metamodel by taking the systems-engineering elements and relationships already described in NPR 7123.1 and rendering them as a connected schema (Figures 7-1 and 7-2). The point is alignment: rather than inventing a fresh vocabulary, the handbook maps each modeling construct back to an SE concept the agency already governs through its NPR, so that a model built this way is traceable to NASA's required SE processes rather than to a tool's idiosyncrasies.

The metamodel is deliberately presented as *one* viable approach, not a mandate. It exists to let any practitioner — including those with an established modeling method of their own — trace their own constructs back to three anchor activities: Stakeholder Expectations Definition, Technical Requirements Definition, and Verification & Validation. Whatever metamodel a project actually adopts, along with the assumptions baked into it, is meant to be written down in that project's modeling plan (the handbook points back to its Model Planning section for this).

A defining design choice is language-agnosticism. The handbook captures the language-specific element or relationship type inside square brackets — `[ ]` — so a reader sees, for example, `[requirement]`, `[block]`, `[activity]`, `[refines]`, or `[derives]` as the SysML expression of an underlying SE concept. The explicit rule is that those brackets are a substitution slot: the handbook fills them with SysML, but any other modeling language can be dropped into the same brackets without changing the SE-level structure. This is the mechanism by which the metamodel stays tool-agnostic SysML tied to NPR 7123.1.

## Frameworks Introduced (exact source names, when/how)

- **NPR 7123.1** — Named as the source of the SE elements and relationships that the metamodel is built from. Both Figure 7-1 (the general metamodel) and Figure 7-2 (the V&V metamodel) are described as depictions of those NPR-defined elements and relationships. This is the governing anchor: the metamodel earns its authority by tracing to the SE engine and processes NPR 7123.1 defines.
- **System Modeling Language (SysML), Version 1.7** — The language the handbook uses to populate the `[ ]` slots. The handbook references SysML and cites the OMG SysML 1.7 specification (the source text shows both a "1.7.9" reference in the notes and a "1.7" citation to OMG's 2024 publication). The handbook explicitly flags that the document and metamodel will be revised for future changes such as SysML version 2.0 — so the SysML 1.7 binding is current-state, not permanent.
- **OMG (Object Management Group)** — Cited as the standards body publishing the SysML specification (2024 reference).
- **NASA SE Engine** — Named as the thing the metamodel is meant to support. The metamodel is positioned as one approach to modeling in service of the SE Engine, with NASA acknowledged to have varying internal approaches to implementing it.
- **Property-Based Requirements (PBR)** — Named as one concrete variation on the metamodel, used to represent numerical requirements; the handbook directs readers to its Appendix D.2 for detail.
- **OOSEM and MBSE Grid** — Named in the behavior-pillar notes as the methods that support the association between a Mission Use Case and Mission Phases and Activities.

## Key Concepts

**The four pillars.** The metamodel's notes are organized around four element families — Requirements, Behavior, Structure (Structural), and Parametric. Each pillar carries its own annotations about how its elements behave across levels of decomposition.

**Requirements pillar.** Requirements are most often satisfied by a block, but the handbook is explicit that a requirement can also be satisfied by a behavior element or a value property — a performance requirement, for instance, can be met by a value property, while a functional requirement can be met by a function. Stakeholders may influence requirements at any level, so a trace can exist at any level; the metamodel draws the Stakeholders-to-Needs trace at one level only for clarity. Measures of Effectiveness (MOEs) carry `satisfies` relationships that can target different element kinds (behavior, structure, or a parametric element such as a value property) depending on what the MOE is about, and an MOE may hold several `satisfies` relationships at once. MOEs can appear at multiple design levels, including subsystem elements. Measures of Performance (MOPs) likewise span levels: they can derive from any requirement, any MOE, and any higher-level MOP, and they can `refine` requirements in the same way an MOE refines objectives.

**Behavior pillar.** Behaviors and interactions at every level may use any of the SysML behavior diagram kinds — use case (`uc`), activity (`act`), sequence (`sd`), and state machine (`stm`) — and these can be decomposed at each level to express expected behavior more precisely. State Machines apply at every level (including Mission Level) but are drawn at component level for simplicity; Use Cases apply at every level but are drawn at Mission Level for simplicity. The Mission Use Case to Mission Phases and Activities association is supported by OOSEM and the MBSE Grid; the handbook notes that a stronger relationship (Dependency, Trace, or Refine) can be used to carry use-case traceability.

**Structural pillar.** Decomposition from System down to Component works the same way at every step. The guidance is to decompose only to the depth a project actually needs and no further — systems can decompose into further systems, subsystems into further subsystems, and an assembly level may also exist.

**Parametric pillar.** Parametric Diagrams are not confined to the component level; they apply at other levels of decomposition too. A Technical Performance Measure (TPM) consists of one or more value properties, possibly spread across several levels, that satisfy the various MOPs defined; a TPM can be a parameter defined on a block or a parameter produced by computation.

**The V&V metamodel (Figure 7-2).** Verification and Validation are treated as distinct activities, yet they follow the same metamodel pattern. A given V&V element may be specific to Verification, specific to Validation, or shared, depending on the case or activity — and a great deal of Validation can be achieved through Verification events, in which case a validation activity may reuse work already captured in a verification description. The `verifies` relationship from a Verification Requirements/Statement element can trace to more requirement levels than any one figure shows; the `satisfies` relationship from a Validation Requirements/Statement element can trace to elements beyond the objectives shown (for instance, Stakeholder Expectation Statements and requirements at other levels). The association between a V&V Case and a V&V Case Activity can also be strengthened with a Dependency, Trace, or Refine relationship.

## Mental Models

**The bracket as a substitution slot.** Read `[ ]` as "here is where the language lives." The SE concept outside the brackets is fixed and traces to NPR 7123.1; the bracketed type is a pluggable expression of it. Today the slot holds SysML 1.7; tomorrow it could hold SysML v2 or another language entirely without disturbing the SE-level structure. This is the single idea that makes the metamodel tool-agnostic.

**Trace-back, not lock-in.** The metamodel is a reference frame you map *to*, not a cage you must build *in*. If you already have a modeling approach, the value is using the metamodel as a Rosetta Stone to demonstrate that your stakeholder, requirements, and V&V work connects to NASA's SE elements.

**The figures are simplified on purpose.** Repeatedly the notes say an element or relationship is shown at one level "for simplicity" — State Machines at component level, Use Cases at Mission level, Stakeholder-to-Needs at one level. The mental correction: read each drawn relationship as a representative instance of something that can legitimately exist at many levels. The diagram understates breadth to stay legible.

**One pattern, two purposes.** Verification and Validation share a metamodel shape even though they answer different questions. Picture a common skeleton with elements that light up for verification, validation, or both depending on the activity.

**Decompose to need, not to exhaustion.** Structural depth is a judgment call bounded by project necessity, not a target to maximize.

## Key Takeaways

- The metamodel is a depiction of NASA SE elements and their relationships, drawn from NPR 7123.1 and split across a general metamodel (Figure 7-1) and a V&V metamodel (Figure 7-2).
- It is language-agnostic by construction: `[ ]` brackets hold the language-specific type, currently SysML 1.7, and are explicitly designed to accept any other modeling language.
- It is presented as one approach among several inside NASA, and is meant to be tailored to a program's methods and recorded in that program's modeling plan along with its assumptions.
- Its job is to give you a trace-back path for Stakeholder Expectations Definition, Technical Requirements Definition, and V&V — supporting the NASA SE Engine and the generation of SE products.
- Elements live across four pillars (Requirements, Behavior, Structure, Parametric); most relationships shown at a single level can actually exist at many.
- Verification and Validation share the same metamodel pattern, and validation can frequently be discharged through verification activities.
- Named variations include Property-Based Requirements for numerical requirements (Appendix D.2) and alternate ways of capturing subsystem relationships (reference properties or abstraction relationships).
- The binding to SysML 1.7 is explicitly current-state: the handbook commits to updating itself for future changes such as SysML v2.0.

## Connects To

- **NPR 7123.1** — the upstream governing source of every element and relationship the metamodel encodes; the reason a model built this way is auditable against NASA SE process.
- **Model Planning** — the handbook's planning section, where a project records the metamodel it adopts and the assumptions behind it.
- **SysML (OMG)** — the language presently filling the `[ ]` slots; the dependency the handbook flags for future revision toward SysML v2.0.
- **OOSEM and the MBSE Grid** — the methods backing the Mission Use Case to Mission Phases and Activities association in the behavior pillar.
- **Property-Based Requirements (Appendix D.2)** — the named approach for representing numerical requirements as a metamodel variation.
- **Stakeholder Expectations Definition, Technical Requirements Definition, and V&V** — the three SE activities the metamodel is built to make traceable.
