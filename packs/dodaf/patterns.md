# DoDAF 2.02 Vol II Patterns & Techniques

---

## Pattern 1: Fit-for-Purpose Model Selection

**When:** Starting any architecture effort; when determining which DoDAF models to produce.

**How:**
1. Identify the decisions that the architecture must support (decision-maker needs, process milestones).
2. Map each decision to the data it requires using the DM2 data-group-to-process table (Table 3.3-1).
3. Select only the viewpoint models that present that data for those decisions.
4. Produce AV-1 and AV-2 for every architecture (DARS registration requirement).
5. Produce additional models only when they are needed for identified decision-maker needs.

**Trade-offs:** Producing fewer models reduces cost and time but risks gaps if decision needs are under-identified. Producing all models wastes effort. Err toward discussing needs with stakeholders before committing to a model set.

---

## Pattern 2: Performer-Activity-Resource Triad

**When:** Modeling any operational, system, or service behavior; whenever the question is "who does what with what?"

**How:**
1. Identify the activity (what transformation occurs).
2. Identify the performer(s) assigned or allocated to the activity.
3. Identify the resources consumed and produced by the activity.
4. Express exchanges as resource flow triples: producing activity → resource → consuming activity.
5. Apply rules, conditions, measures, and locations as attributes of the triad elements.

**Trade-offs:** This model is exhaustive but can produce large data sets. Focus on architecturally significant activities and interfaces; not every sub-activity needs to be modeled.

---

## Pattern 3: Three-Level Information Modeling (DIV Stack)

**When:** Specifying information or data needs for an architecture; when designing data exchanges or databases.

**How:**
1. Produce DIV-1 first: identify and relate the concepts decision-makers need to understand using DoDAF genus terms as roots.
2. Produce DIV-2: for each DIV-1 concept, specify exactly what decision-makers need to know (completeness, accuracy, authority, timeliness, place, form).
3. Produce DIV-3: specify the physical data structures, schemas, and exchange formats that satisfy every DIV-2 requirement. Comply with StdV-1 metadata standards.
4. Verify that DIV-3 satisfies every DIV-2 requirement; DIV-3 may not introduce concepts not grounded in DIV-2.

**Trade-offs:** All three levels are needed for rigorous data management. DIV-1 alone is sufficient for early stakeholder communication; DIV-3 alone without DIV-1/DIV-2 backing is untraceable implementation.

---

## Pattern 4: Capability-to-Delivery Traceability Chain

**When:** Portfolio management; linking PPBE investments to operational needs; capability gap analysis.

**How:**
1. CV-1: Define desired effects (resource states) and measures of effect/desire.
2. CV-2: Organize capabilities into a hierarchy.
3. CV-6: Map activities to capabilities.
4. OV-5b: Detail those activities with performers, resources, and conditions.
5. PV-3: Map projects to the capabilities they deliver.
6. PV-2: Show when projects deliver milestones.
7. SV-5b or SvcV-5: Show which systems or services support which activities.

**Trade-offs:** Full traceability requires populating multiple viewpoints. For early portfolio decisions, CV-1 + PV-3 may suffice. Full chain is required for milestone reviews (DAS) and PPBE justification.

---

## Pattern 5: Standards-Activity Binding

**When:** Documenting compliance requirements; specifying acquisition standards; planning technology transitions.

**How:**
1. From StdV-1: identify each standard applicable to the architecture.
2. For each standard, identify the activities it constrains (not the performers directly).
3. Model conditions under which each standard applies to each activity.
4. For future standards, produce StdV-2 with before-after relationships showing standard succession timelines.
5. Align StdV-2 succession timelines with PV-2 project delivery schedules to ensure systems are built to the correct standards generation.

**Trade-offs:** Activity-centric standards binding is more precise than performer-centric but requires a complete OV-5b or SV-4 activity decomposition. Without activities, standards cannot be bound.

---

## Pattern 6: Interface Identification and Configuration Management

**When:** Defining system or service interfaces; specifying interoperability requirements; managing interface change.

**How:**
1. SV-1/SvcV-1: Identify interfacing systems/services and the resource flows between them (the resource flow triple).
2. SV-2/SvcV-2: Detail the interface means — what moves, in what format, with what QoS.
3. SV-6/SvcV-6: Add measures (timeliness, throughput, reliability) to resource flows.
4. Document formal agreements (ICDs, IRSs) for critical interfaces as Agreement elements in the Rules data group.
5. Place interfaces under configuration control; track changes against the DM2 data.

**Trade-offs:** For legacy point-to-point interfaces, ICDs are the standard artifact. For SOA/net-centric environments, publish-subscribe agreements replace ICDs. Both are modeled as Agreements in the DM2 Rules group.

---

## Pattern 7: Operational-to-System Traceability

**When:** Verifying that systems satisfy operational needs; performing functional allocation; writing system specifications.

**How:**
1. OV-5b: Establish all operational activities with their performers, resources, rules, and conditions.
2. SV-4: Decompose system functions.
3. SV-5a: Map each system function to the operational activities it supports or enables.
4. Verify that every system function traces to at least one operational activity; orphaned system functions signal scope creep.
5. Verify that every operational activity has at least one system function allocated to it (no capability gaps).

**Trade-offs:** Full traceability requires maintaining SV-4 and OV-5b in sync; this is ongoing effort. Partial coverage of SV-5a is better than none — even incomplete traceability reveals gaps.

---

## Pattern 8: Project WBS as Architecture Element

**When:** DAS milestone reviews; PPBE program justification; earned value management setup.

**How:**
1. PV-1: Identify individual organizations performing individual projects; establish the WBS hierarchy using whole-part relationships.
2. PV-2: Add temporal structure — before-after relationships, milestones, happens-in links to budget years.
3. Attach measures (cost, schedule) and rules (contractual requirements) at each WBS level.
4. Derive contract WBS from program WBS at the appropriate DAS milestone.
5. As projects mature, evolve the WBS to reflect growing definition — the WBS is a continually evolving instrument.

**Trade-offs:** The WBS is a DoDAF-to-acquisition integration artifact; it must be kept in sync with both the architecture and the contract. Divergence between architectural WBS and contract WBS signals integration failure.

---

## Pattern 9: Service Self-Description for Discovery

**When:** Designing SOA or net-centric architectures; enabling service discovery and reuse.

**How:**
1. SvcV-1: Model each service with its ServiceDescription element.
2. The ServiceDescription specifies: visible functionality, QoS, interface descriptions, data descriptions, and service policy (rules). It does not expose internal workings.
3. Relate ServiceDescriptions to DIV-2 information requirements to specify what data is accessible through the service.
4. Relate service standards (StdV-1 EnablingServiceStandard or BusinessServiceStandard) to service activities.
5. Register the ServiceDescription in a service registry for discovery.

**Trade-offs:** Self-description requires up-front investment in formalizing service interfaces. Without it, service consumers must depend on informal knowledge, creating fragile integrations.

---

## Pattern 10: DOTMLPF Analysis via DM2

**When:** Capability-based assessment; JCIDS analysis; identifying non-materiel solutions.

**How:**
- Doctrine → model as Rules constraining Activities.
- Organization → model as Organization types performing Activities.
- Training → model as Activities increasing Performer capability under specified Conditions to specified Standards.
- Materiel → model as Materiel (subtype of Resource) that is part of a Performer.
- Leadership → model as Rules affecting the applicability of other rules (judgment in application of doctrine).
- Personnel → model as Persons in Roles with Skills and MeasurableSkills.
- Facilities → model as Location types or geo-political extents where Performers are sited.

**Trade-offs:** Full DOTMLPF modeling in the DM2 is comprehensive but data-intensive. Focus DOTMLPF modeling on the factors that are trade-off candidates in the analysis; model others at a higher level of abstraction.

---

## Pattern 11: Publication-Subscription Resource Flow

**When:** Modeling net-centric data sharing; specifying publish/subscribe interfaces.

**How:**
1. Identify the publishing activity (produces the resource) and the subscribing activity (consumes the resource).
2. Model the overlap as a resource flow triple: publishing activity → resource → subscribing activity.
3. Note that publishing and subscribing do not have to occur at the same time or place (the overlap is a logical dependency, not a physical co-location).
4. Attach Agreement elements (formal publish/subscribe agreements) as Rules constraining both activities.
5. Specify QoS measures (timeliness, format, update rate) in SvcV-6 or SV-6.

**Trade-offs:** Publish-subscribe decouples producers and consumers but requires formal agreements to avoid semantic mismatches. Without a formal Agreement element in the Rules data group, publish/subscribe interfaces are undocumented and hard to change control.

---

## Pattern 12: Architecture Evolution and Standards Transition

**When:** Planning system modernization; managing technology obsolescence; aligning architecture with future standards.

**How:**
1. StdV-1: Document current standards profile.
2. StdV-2: Document anticipated standards succession with before-after temporal relationships.
3. SV-8: Plan system migration increments aligned with standards transitions.
4. SV-9: Identify emerging technologies that enable migration.
5. PV-2: Schedule migration milestones with happens-in links to PPBE fiscal years.
6. Cross-check: every SV-8 migration step should align with a StdV-2 standards succession and a PV-2 project milestone.

**Trade-offs:** Standards transition planning requires alignment across three viewpoints (StdV, SV, PV). Misalignment means systems may be built to obsolete standards or programs may be resourced before standards are available.

---

## Pattern 13: Cross-COI Information Harmonization

**When:** Integrating architectures from multiple communities of interest; establishing shared data standards.

**How:**
1. DIV-1: Produce a conceptual information model for each COI's information needs, rooted in DoDAF genus terms.
2. AV-2: Use the Integrated Dictionary to map COI-specific terminology to common DoDAF concepts using genus-differentia definitions.
3. Identify overlapping information needs across COIs; harmonize concepts using super-subtype and whole-part relationships.
4. Identify divergent information needs; document as separate concepts with explicit distinction.
5. DIV-3: Specify exchange formats that satisfy both COIs' DIV-2 requirements.

**Trade-offs:** Full harmonization is time-consuming and requires stakeholder consensus. Partial harmonization (agreeing on shared concepts for the most critical information exchanges) delivers most of the interoperability value at lower cost.
