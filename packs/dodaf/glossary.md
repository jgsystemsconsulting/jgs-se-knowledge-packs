# DoDAF 2.02 Vol II Glossary

**Activity** — A transformation that produces new resources from existing resources; the "what" in architectural descriptions. Named by verbs. Distinct from Rule (which prescribes how an activity is carried out) and from Project (which is a type of activity producing desired resource states). Ontologically synonymous with Task in the DM2.

**Agreement** — A type of rule in the DM2 representing formal consent among parties to terms and conditions of activities they participate in. Examples: interface control documents, publish/subscribe agreements, service contracts.

**Allocated Baseline** — The point at which allocation of performers to activities is sufficiently mature to be formally declared; precedes assignment.

**Allocation** — The organized cross-association (mapping) of elements within various structures or hierarchies, used early in design as a precursor to assignment. Preliminary, potentially tentative. Distinct from Assignment.

**Assignment** — The committed designation of a specific performer to carry out a specific activity; more definitive than allocation. Used when architectural design is mature.

**AV-1 (Executive Summary)** — All Viewpoint model presenting the purpose, scope, and subjects of an architecture effort. Required for DARS registration. No prescribed content beyond DARS requirements.

**AV-2 (Glossary/Integrated Dictionary)** — All Viewpoint model presenting terms, definitions, and architecturally significant relationships within an architecture. Rooted in seven DoDAF genus terms.

**Before-After Relationship** — A DM2 temporal ordering relationship (BeforeAfterType) indicating that one thing temporally precedes another. Used in Resource Flows, Projects, and SvcV-10c/SV-10c models.

**Capability** — The ability to achieve a desired effect under specified standards and conditions through combinations of ways (guidance and rules) and means (resources) to perform a set of tasks. Consistent with JCIDS definition.

**Capability Configuration** — A specific combination of performers (aggregate of systems, organizations, and locations) that can provide a stated capability.

**Condition** — The operational environment or context under which an activity is performed; may affect which activities, performers, and rules apply. Modeled in accordance with UJTL conditions.

**Configuration Item (CI)** — A system or software item under configuration control. Hardware CIs follow MIL-STD-196E taxonomy; software CIs are CSCIs (Computer Software Configuration Items) per MIL-STD-881C.

**DARS (DoD Architecture Repository System)** — The DoD registry for architectural descriptions. AV-1 is the registration artifact.

**Data** — The representation of information in a formalized manner suitable for communication, interpretation, or processing by humans or automatic means; the physical encoding of information.

**Data Group** — A semantically cohesive cluster of DM2 concepts forming a building block of architectural descriptions. Eight principle groups and three supporting groups.

**Desired Effect (Desired Resource State)** — The resource state to be achieved by a capability. Ontologically synonymous with goals, objectives, and outcomes. Comprises: initial resource state, desired resource state, and measures of the difference.

**DISR (DoD Information Technology Standards and Profile Registry)** — The authoritative source for technical standards in DoD IT architectures. StdV-1 technical standards must be drawn from the DISR.

**DM2 (DoDAF Meta-Model)** — The formal ontology providing standard glossary terms, types, and relationships for all DoDAF architectural descriptions. Based on IDEAS Foundation; available as a Sparx Enterprise Architect model.

**DOTMLPF** — Doctrine, Organization, Training, Materiel, Leadership and Education, Personnel, Facilities. The DoD capability analysis framework; all factors are expressible in DM2 terms.

**Enabling Service** — A technical service supporting business services or operational activities; contrasted with Business Service.

**Fit-for-Purpose** — The guiding principle that DoDAF architecture products are selected based on decision-maker needs, not on prescriptive completeness requirements.

**Functional Standard** — A type of rule governing the functional behavior of activities and performers.

**Genus Term** — One of seven DoDAF root categories for AV-2 taxonomical classification: activity, resource, project, location, guidance, vision, property.

**Guidance** — A category of rule in the DM2 that shapes behavior; less prescriptive than a Rule per se. Includes security classification criteria, marking rules, and other advisory constraints.

**happensIn Relationship** — A DM2 relationship associating activities or project temporal parts with time periods (e.g., budget years); used in PV-2 to align schedules with fiscal cycles.

**IDEAS Foundation** — The four-dimensional, meronymic ontological foundation underlying the DM2. All instances have spatio-temporal extent; the ontology supports whole-part decomposition of complex aggregates.

**Individual** — In IDEAS, an instance of something with spatio-temporal extent; the basic unit of the ontology. Stereotyped «Individual» (grey) in DM2 diagrams.

**IndividualType** — A type whose members are Individuals. Stereotyped «IndividualType» (light orange) in DM2 diagrams.

**Information** — The state of a something-of-interest that is materialized in any medium and communicated or received. A subtype of Resource; can describe other information (metadata). More general than text strings.

**Interface Control Document (ICD)** — A formal agreement documenting the specific data elements and implementation tables at a system interface; managed and controlled by the SoS or system project manager.

**JCIDS (Joint Capabilities Integration and Development System)** — One of six DoD core processes served by DoDAF data; focuses on identifying and validating capability requirements.

**Location** — A point or extent in space (physical or logical). A supporting data group applied to performers, activities, and resources.

**Materiel** — A type of resource in the DM2; has whole-part relationships. May be a weapon system, vehicle, equipment, or other physical item assigned to performers.

**Measure** — The magnitude of some attribute of an individual. Supporting data group. Subtypes: Measure of Effect, Measure of Desire, Performance Measure, Needs Satisfaction Measure, Physical Measure, Temporal Measure, Service Level.

**Measure of Desire** — How much a responsible performer wants a desired effect; expressed as priority, budget commitment, or risk calculus.

**Measure of Effect** — A measure of the difference between an initial (less-desired) resource state and a desired resource state; quantifies capability achievement.

**Mesodata** — Data about the internal structure of an information resource.

**Metadata** — Data that guides the interpretation of data values (units, scale, authority); distinguished from mesodata and microdata in DIV-2 modeling.

**Microdata** — Data characterizing the integrity of specific data values (pedigree, confidence level).

**Milestone** — In PV-2, the overlap between a project temporal boundary and a resource state produced by a project part; has cardinal and physical measures.

**Normalization** — Structural modification of a data model to ensure freedom from insertion/update/deletion anomalies; uncovers additional business rules (DIV-2/DIV-3 context).

**Organization** — A specific real-world assemblage of people and other resources organized for an ongoing purpose. A type of Performer in the DM2. Has whole-part relationships.

**Pedigree** — The origin and history of a resource; the background and provenance of an item within an architectural description. A supporting data group.

**Performer** — Any entity (human, automated, or composite) that performs an activity and provides a capability. The "who" in architectural descriptions. Subtypes: Person in Role, Organization, System, Service.

**PerformerCapableOfResponsibility** — A DM2 type for performers who can be held accountable for desired effects: organizations and persons in organizational roles. Required in CV models.

**Person in Role** — A type of performer including the materiel assigned for the role. Has temporal whole-parts (e.g., in-garrison, deployed) with potentially different materiel compositions.

**PMESII** — Political, Military, Economics, Social, Infrastructure, Information — a framework for characterizing complex operational environments as resource states in the DM2.

**Program Element (PE)** — The basic building block of the FYDP (Future Years Defense Program); identifies program mission, responsible organization, and associated resources. The PPBE primary construct.

**Project** — A temporary endeavor (a type of individual activity in the DM2) undertaken to create desired states of resources. Has whole-part, temporal whole-part, and super-subtype relationships.

**Publication/Subscription** — A resource flow pattern in the DM2: a publishing activity produces a resource at one time/location; a subscribing activity consumes it at a different time/location.

**QoS (Quality of Service)** — Measures attached to service or system resource flows; examples include timeliness, throughput, reliability, and accuracy. Modeled in SvcV-6 and SV-6.

**Resource** — Anything that can be located in space and time and whose state can be described. Supertypes: Information, Data, Materiel, Performer. Produced and consumed by activities.

**Resource Flow Triple** — The core DM2 relationship pattern: (producing activity) + (resource) + (consuming activity). The invariant structural unit for all data exchanges.

**Rule** — A principle or condition that governs behavior; prescribes how an activity may be carried out. Subtypes: Guidance, Standard (Technical Standard, Functional Standard), Agreement. Constrains Activities, not Performers directly.

**Service** — A type of Performer that enables access to capabilities through a prescribed interface exercised consistent with service policies. Includes non-IT services. Always has a Service Description.

**Service Description** — A self-describing element that provides all information needed to use a service without exposing its internal workings. First-class DM2 element.

**Standard** — A type of Rule specifying required conformance; subtyped as Technical Standard or Functional Standard. Technical standards for DoD IT must come from the DISR.

**super-subtype Relationship** — A DM2 relationship between a type and one of its subtypes (generalization). Used for capability taxonomies, activity categorization, and type hierarchies.

**Technical Standard** — A type of Standard governing technical implementation; must be drawn from the DISR for DoD IT architectures.

**TupleType** — An IDEAS type whose members are tuples (n-ary relationships). Used for relationship reification in the DM2.

**Type** — In IDEAS, the specification of a category of things. Stereotyped «Type» (pale blue) in DM2 diagrams.

**Vision** — A statement of the desired resource state(s) envisioned by a responsible performer; the strategic intent behind a capability.

**WBS (Work Breakdown Structure)** — A product-oriented family tree of hardware, software, services, data, and facilities. The primary DAS/PPBE integration artifact; governed by MIL-STD-881C.

**whole-part Relationship** — A DM2 aggregation relationship between an individual and one of its parts (WholePart or TemporalWholePart). Used across all data groups for decomposition.
