# NASA Systems Modeling Handbook (NASA-HDBK-1009A) Glossary

Key terms as used in the handbook, alphabetical, with the chapter that develops each.
Definitions are synthesized in original words; they paraphrase the handbook's usage, not
its verbatim text. Bracketed `[type]` notation marks a SysML element/relationship type
that fills a language slot in the metamodel.

| Term | Meaning (as used in NASA-HDBK-1009A) | Chapter |
|---|---|---|
| **Activity diagram (`act`)** | SysML behavior diagram that drills into one use case, using swim lanes to allocate steps to structure elements. A colon in an action name signals the action is typed by a defined activity. | ch04, ch05 |
| **Allocate** | Relationship that assigns behavior to structure (e.g. swim lanes allocating activities to the user, system of interest, or external system). | ch04 |
| **Black box / White box** | The two rows of the MBSE Grid's problem section: black box is the conceptual representation, white box the technical description. | ch07 |
| **Block definition diagram (`bdd`)** | SysML structure diagram that catalogs blocks and their decomposition (context blocks, subsystems/components, functional decomposition). | ch04 |
| **Concept of Operations (ConOps)** | A narrative of what a system is for and how it is used across its life; in this handbook its sections are populated with model views (Appendix F overlays MBSE content onto the SE Handbook Appendix S outline). | ch06, ch08 |
| **Derive / derived requirement** | Relationship expressing flow-down (Needs→Goals→Objectives→system requirements; MOPs derive from requirements, MOEs, or higher MOPs). | ch04 |
| **Design Reference Mission (DRM)** | A thread-level construct (with scenarios and use cases) walking the system along one timeline; labelled for traceability (e.g. `[DRM-0100]`). | ch08 |
| **Internal block diagram (`ibd`)** | SysML structure diagram showing how blocks connect — interfaces, ports, connectors, and item flows between elements. | ch04, ch05 |
| **MBSE (Model-Based Systems Engineering)** | Per INCOSE: the formalized application of modeling to support requirements, design, analysis, and V&V, from conceptual design through the life cycle. | ch01 |
| **MBSE Grid** | The handbook's framework (Morkevicius et al., 2017), tailored to NASA: technical processes 1–9 on rows, SysML pillars on columns; cross-sections file the diagrams and tables. | ch01, ch07 |
| **Measure of Effectiveness (MOE)** | The (typically qualitative) measure by which a stakeholder judges satisfaction with the delivered system; refines objectives; carries `satisfies` relationships. | ch03, ch04, ch06 |
| **Measure of Performance (MOP)** | A quantitative target whose satisfaction helps ensure the corresponding MOE is met; encoded as a requirement element with a `satisfies` relationship and a trace to its MOE. | ch03, ch04, ch06 |
| **Metamodel** | A depiction of the modeling elements you may create plus the relationships that legitimately connect them; built here from NPR 7123.1 elements (Fig 7-1 general, Fig 7-2 V&V). | ch03 |
| **Model Planning** | The activity (inside SE Engine Technical Process 10) that produces the Modeling Plan. | ch02 |
| **Modeling conventions / standards / organization** | The three Setting-Up-the-Model decisions: naming (conventions), profiles/standards, and package hierarchy (organization). | ch02 |
| **Modeling Plan** | A technical plan, a subset of the SEMP, documenting how modeling supports NPR 7123.1 across the life cycle; living, updated as the system matures. | ch02 |
| **NASA SE Engine** | NASA's means of doing SE — 17 common technical processes across system design, product realization, and technical management (NPR 7123.1D Fig 3-1; handbook Fig 4.1-1). | ch01, ch07 |
| **Needs, Goals, Objectives (NGOs)** | The requirements hierarchy below stakeholder expectations: needs at top, derived goals, then derived objectives. | ch04, ch08 |
| **NPR 7123.1** | NASA Systems Engineering Processes and Requirements — the governing document the handbook models in support of (not a replacement). | ch01, ch03 |
| **OOSEM** | Object-Oriented Systems Engineering Method (INCOSE); source of the two added steps (Update Modeling Plan, Setup Model) and the methodology shape. | ch01, ch07 |
| **Parametric diagram / Parametrics pillar** | SysML view (and pillar) for constraints and mathematical statements; applies at multiple decomposition levels, not just component level. | ch03, ch04 |
| **Pillars (four)** | Structure, Behavior, Requirements, Parametrics — the conventional grouping of SysML's nine diagram types into one integrated model context. | ch01, ch03 |
| **Property-Based Requirement (PBR)** | An alternative requirements approach (Appendix D.2): a requirement carrying structure, numerical attributes, and constraints; extends SysML abstractRequirement/extendedRequirement/Block. | ch03, ch07 |
| **Refines** | Relationship by which MOEs refine objectives and MOPs refine requirements. | ch03, ch04 |
| **Requirements diagram (`req`) / Requirements Table** | SysML view (and tabular equivalent) of requirements, their properties, and traceability; the table is grounded in OMG SysML v1.7. | ch04 |
| **Satisfies** | Relationship: a requirement satisfied by a block, behavior, or value property; validation requirements carry `satisfies`. | ch03, ch05 |
| **Scenario Modeling** | An alternative behavior approach (Appendix D.3) introducing a Scenario Modeling Context Block bridging Activities and State Machines; supports nominal/off-nominal scenarios. | ch07 |
| **SEMP (Systems Engineering Management Plan)** | The program's full document for satisfying NPR 7123.1 across the life cycle; the Modeling Plan is its modeling-scoped subset. | ch02 |
| **Setting Up the Model ("Step 0")** | The model-specific step at the start of the System Design Processes establishing conventions, standards, and organization. | ch01, ch02 |
| **Sequence diagram (`sd`)** | SysML behavior diagram for ordered interactions between components. | ch04, ch08 |
| **State machine (`stm`)** | SysML behavior diagram for modes and transitions; in the ConOps it captures modes of operation with do/entry/exit activities and event-driven transitions. | ch04, ch08 |
| **Stakeholder Expectation Statement** | A stakeholder's expectation captured (stakeholders modeled as SysML actors) and traced to that stakeholder; NGOs trace up to it. | ch04 |
| **System of interest** | The system being modeled, named in the context views alongside users and external systems. | ch04 |
| **System Specification (approach)** | An alternative (Appendix D.4) bridging Structure to Requirements via Logical/Logical-Node/Physical Design and a System Specification Block. | ch07 |
| **SysML (OMG, v1.7)** | The illustrative modeling language: nine diagram types (4 behavior, 1 requirement, 4 structure), a subset of UML 2 with extensions. ISO/IEC 19514. | ch01, ch03 |
| **System Design Processes** | NASA's design-side processes (Stakeholder Expectation Definition, Technical Requirements Definition, Logical Decomposition, Design Solution Definition) onto which the MBSE Grid maps. | ch07 |
| **Technical Performance Measure (TPM)** | One or more value properties tracked over time (current vs. anticipated achievement); typically drawn from the defined MOPs. | ch03, ch04, ch06 |
| **Trace** | Relationship linking stakeholders to needs, and MOEs/MOPs/TPMs to requirements and structure; the value of the model lives in these relationships. | ch03, ch04 |
| **Use case diagram (`uc`)** | SysML behavior diagram naming system functions and actor interactions; `<<include>>` marks a use case that is a subset of another. | ch04, ch05 |
| **V&V case / V&V configuration** | A V&V case owns a V&V activity; the V&V configuration (equipment, personnel, facilities) is referenced by the case and reused across verification and validation. | ch05 |
| **Verification Modeling (approach)** | An alternative (Appendix D.5, OpenSE Cookbook) adding a Verification Context Block and parametric diagram to support V&V simulation. | ch07 |
| **Verifies / verify-method attribute** | `verifies` traces a verification requirement to a system requirement (one-to-many); `verifyMethod` is a SysML extension on the requirement (or verification requirement). | ch05 |
| **Verification vs. Validation** | Verification asks whether the system was built to its requirements; validation asks whether it meets stakeholder intent in use; they share the same metamodel machinery. | ch05 |
