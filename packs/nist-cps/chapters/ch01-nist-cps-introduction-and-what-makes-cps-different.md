# Chapter — Introduction: What CPS Are and What Makes Them Different

## Core Idea

Cyber-physical systems (CPS) are smart systems built from engineered, interacting networks of physical and computational components. The defining trait is that the cyber and the physical are fused and connected, with sensing, computation, and actuation working together — and crucially, with timing constraints that bridge the information-technology and operational-technology worlds. NIST SP 1500-201 (Volume 1) frames CPS this way precisely because conventional product, system, and application design assumed little or no pervasive interconnectedness, an assumption that no longer holds.

The document gives a working definition that combines four capabilities — computation, communication, sensing, and actuation — with physical systems to deliver functions whose correctness depends on timing. The degree to which such a system engages its surroundings (people included) varies from one CPS to the next. The definition places three things at the center: the physical world, the computational layer that observes and acts on it, and time as a first-class concern rather than an afterthought.

A second core idea is recursion and scale. A CPS can be as small as a single device, or it can be a system, or a full system of systems (SoS) such as an entire infrastructure. Whether something counts as a "device" or a "system" depends on your perspective — a device from one viewpoint is a system from another. What a CPS must always contain is a decision flow paired with at least one of two physical-world flows: an information flow (a digital measurement of the physical state) or an action flow (an impact on the physical state). That minimal structure is what lets CPS thinking scale from a single component up to city, national, and global collaborations.

The third core idea is purpose. The source positions the Framework as a tool for comprehensive analysis of CPS — a way to capture the generic functionalities CPS provide and the activities and artifacts needed to conceptualize, realize, and assure them. It deliberately addresses both concerns unique to CPS and concerns shared with any device or system, so that two CPS architectures derived independently from the Framework end up in substantial alignment and can be mutually understood.

## Frameworks Introduced (exact source names, when/how)

- **CPS Framework** — the central artifact of the document. Its core is described as a common vocabulary, structure, and analysis methodology. It is introduced in Section 1.1 and explicitly intended as a *living document* that will be revised over time as stakeholder input and public comments arrive; the source notes some sections are incomplete at the time of writing. As a process method, the CPS analysis methodology is meant to support CPS systems engineering across a range of development approaches the document names: waterfall, agile, spiral, and iterative.

- **CPS Public Working Group (CPS PWG)** — the open NIST forum, named in Section 1.1.1, established to gather input on CPS both nationally and globally. The source states it launched in mid-2014 with five subgroups. Their charters covered, in turn: the CPS vocabulary plus a reference architecture; use cases; the joint cybersecurity-and-privacy concern; timing together with synchronization; and the interoperability of data. Each subgroup produced initial "Framework Element" documents in December 2014, which were then integrated, reorganized, and refined into this draft Framework.

- **TOGAF** and **CMMI** — named in Section 1.1.1 as examples of well-documented systems engineering process documents and flows. The source's stance is explicit: the CPS Framework does *not* compete with these; it focuses on the detailed scope of CPS and the specific concerns of CPS implementers and analysts, and it claims the CPS concepts map cleanly onto these more general methods, making them complementary rather than competitive.

- **CPS Conceptual Model (Figure 1)** — introduced in Section 1.2 to highlight the potential interactions of devices and systems within a system of systems, and to ground the recursive device/system/SoS pattern and the decision/information/action flows described above.

> Caveat honored per pack instructions: the two permission-licensed third-party figures referenced in this section — the M2M sector map (Figure 2, courtesy of Beecham Research) and the smart-transportation illustration (Figure 3, courtesy of ETSI) — are intentionally not reproduced or depended upon here. The scope and smart-traffic discussion below is conveyed in prose drawn from the surrounding text instead. This pack bundles Volume 1 as a single unit.

## Key Concepts

- **Cyber-physical fusion.** The combination of cyber and physical, plus their connectedness, is essential. A CPS generally involves sensing, computation, and actuation. It draws on traditional IT (moving data from sensors into computation) and traditional OT (control and actuation), and the joining of these two worlds *with their associated timing constraints* is what the source calls a particularly new feature.

- **System of systems (SoS).** A CPS may be an SoS, spanning multiple purposes and different time and data domains. That spread forces methods of translation or accommodation between domains — for example, different time domains may use different time scales, granularities, or accuracies.

- **Emergent behavior.** Because CPS composition is open, behaviors arise that cannot be reduced to any single subsystem but instead come about through the interaction of many. The source treats understanding such behavior as a key analysis challenge, and stresses that emergence can be negative or positive: a traffic jam is given as a detrimental emergent behavior, while a smart grid balancing producers and consumers for optimal energy distribution is given as a desirable one.

- **Trustworthiness.** Because CPS touch the physical world and are deeply connected, the source raises a heightened, more urgent need for security, privacy, safety, reliability, and resilience — plus assurance for these properties across pervasive, interconnected devices and infrastructures. It notes that third-party-owned brokers, aggregators, and infrastructure devices (publish/subscribe messaging, certificate authorities, type and object registries) introduce trust issues.

- **Free composability.** Components should be combinable into systems dynamically, with the architecture even modifiable at runtime to meet changing concerns. The source flags challenges — timing composability is called out as potentially difficult — and observes that systems may be assembled from services purchased per-use rather than from owned assets.

- **Heterogeneity and complexity.** CPS span a wide complexity range: sensors from basic to smart, static and adaptive control, single-mode and multi-faceted sensing, and control that may be local, distributed, federated, or centralized. Interactions may be loosely coupled (such as repurposing existing distributed sensing) or tightly coupled (such as telemedicine or smart-grid operation). The sensing-and-control feedback loop is described as central and must be addressed in any design.

- **Co-design.** As a way to manage complexity, the source describes co-design: considering hardware and software design jointly so that tradeoffs between a system's cyber and physical components can be informed.

- **Timing as architecture.** Timing is treated as a central architectural concern. Two distinct properties are separated: a *time interval* (for example, a bound on the latency between when a sensor event occurs and when the data becomes available) and *timestamp accuracy* (the gap between the actual event time and the recorded value). Accurate intervals help coordinate actions across large spatial extents; accurate timestamps support root-cause analysis and, sometimes, legal or regulatory needs.

- **Environment and the human.** CPS are characterized by interaction with their operating environment through closed-loop sensing and control — they measure, compute, and act, typically changing the very properties they observe. The environment usually includes humans, who behave differently from other components. The source enumerates the roles a human can play: controller or partner in control, user, consumer of output, and the direct object being measured and acted upon.

- **Other distinguishing traits.** The source additionally notes that CPS may be repurposed beyond their original design basis (a phone in a car serving as a traffic sensor; energy-usage data used for fault diagnosis), enable cross-domain applications (manufacturing, energy distribution, smart cities, consumer sensing), accommodate a broad range of computational models, and support modes of communication from standalone to highly networked and from power-constrained to resource-rich.

## Mental Models

- **Decision flow + at least one physical flow.** The smallest viable mental picture of a CPS: a decision flow joined to either an information flow (digitally measuring physical state) or an action flow (changing physical state), or both. Strip away everything else and this is the irreducible core.

- **The recursive lens.** Don't ask "is this a device or a system?" in the abstract — ask "from whose perspective?" The same artifact is a device, a system, or an SoS depending on where you stand. This is what lets one analysis vocabulary stretch across scales.

- **IT meets OT under a clock.** Picture CPS as the overlap of three circles: the IT world (data and computation), the OT world (control and actuation), and timing constraints binding them. The novelty is the intersection, not any one circle alone.

- **Closed-loop participant, not passive observer.** A CPS does not just watch its environment; it acts on it and thereby changes what it next observes. Model it as a feedback participant whose own actions feed back into its inputs — and remember the environment usually contains humans in one of several roles.

- **Smart traffic as the worked archetype.** The source repeatedly uses smart traffic to make CPS concrete: autonomous vehicles (themselves systems of CPS) whose steering, braking, and powertrain are orchestrated; on-location intersection controllers sensing local conditions and applying signal commands; regional control centers fusing traffic, weather, events, and accident data to optimize routing; and vehicles forming ad hoc communities to communicate braking or lane changes and avoid collisions. Use this scenario as a reference instance when an abstract CPS concept needs grounding.

- **Orchestration vs. collaboration vs. emergence.** Three distinct multi-CPS interaction patterns appear: *orchestration* (a cyber system logically directing others, e.g., a traffic unit signaling vehicles through an intersection), *collaboration* (peers combining to produce effects greater than the sum of parts, e.g., vehicles cooperating to avoid collisions), and *emergence* at the SoS level (complex management that supports behavior arising from the whole).

## Key Takeaways

- A CPS fuses computation, communication, sensing, and actuation onto physical systems to carry out *time-sensitive* functions; how deeply it engages its surroundings — humans among them — differs by system.
- What makes CPS different is the fusion of cyber and physical under timing constraints, joining the IT and OT worlds; this combination is the genuinely new feature the source highlights.
- CPS scale recursively from a single device to a full system of systems; the irreducible core is a decision flow plus at least one of an information or action flow.
- The CPS Framework's core is a shared vocabulary, structure, and analysis methodology; it is a living document meant to support waterfall, agile, spiral, and iterative development alike.
- The Framework is positioned as complementary to general SE methods such as TOGAF and CMMI, not competitive with them, and claims its concepts map cleanly onto them.
- Emergence, trustworthiness (security, privacy, safety, reliability, resilience), free composability, heterogeneity, co-design, and timing are the recurring concerns that distinguish CPS analysis.
- Timing is an architectural concern with two separable facets — interval bounds and timestamp accuracy — each serving different coordination, forensic, and regulatory needs.
- CPS and IoT overlap heavily and are sometimes used interchangeably; the source says the Framework should be considered equally applicable to IoT.

## Connects To

- **CPS Public Working Group subgroups** — the five subgroups (covering the vocabulary-and-reference-architecture work, use cases, the cybersecurity-and-privacy concern, timing plus synchronization, and the data-interoperability problem) preview the concern areas the rest of the Framework develops.
- **Section 2 (The CPS Framework)** — where the analysis methodology is built out, including its core concepts of *facets* (activity-organized views of the engineering process, each carrying its own activities and artifacts) and *aspects* (groupings of related cross-cutting concerns); cross-cutting functions named here as scope examples include safety, security, and interoperability.
- **Appendix B (Definitions and Acronyms)** — the source notes the Framework borrows many terms from other standards and records its own usage there, acknowledging that words such as "precision" carry different meanings across contexts.
- **Appendix C (Applying the CPS Framework)** — the smart-traffic and emergency-response scenario introduced in scope is carried forward there as a worked example of exercising the analysis methodology.
- **Adjacent SE process frameworks** — TOGAF and CMMI as the general systems-engineering methods this Framework intends to complement rather than replace.
