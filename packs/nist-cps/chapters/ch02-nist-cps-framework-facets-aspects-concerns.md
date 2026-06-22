# Chapter 2: The CPS Framework — Facets, Aspects, and Concerns (Vol 1)

## Core Idea
The CPS Framework is, at heart, an **analysis methodology plus a shared vocabulary** for studying, designing, and evolving cyber-physical systems in an orderly, sufficiently complete way. It does this by crossing two orthogonal structures. **Aspects** group the stakeholders' *concerns* — the things people care about (function, trustworthiness, timing, and so on). **Facets** are the engineering *views* — conceptualization, realization, and assurance — each holding its own activities and artifacts. Every aspect is meant to be examined through every facet, so that all cross-cutting concerns get addressed at every stage of a CPS's life. Because CPS are frequently systems of systems that sense, compute, and act on the physical world, the Framework's constructs are designed to apply recursively and to be tailored — not run as a rigid waterfall.

## Frameworks Introduced
Names below are taken from the source (NIST SP 1500-201, Section 2), used as the source uses them.

- **The CPS Framework (domains, facets, aspects, concerns, activities, artifacts, properties)** — the top-level taxonomy and analysis methodology. Derived in Section 2.2 and described in full taxonomic detail (tables) in Section 2.4.
  - When to use: to structure any CPS study, design, or evolution effort, and to check that nothing important has been omitted.
- **The three facets — conceptualization, realization, assurance** — the systems-engineering views that mirror the traditional process captured by the "VEE" model. Defined in Table 2.
  - When to use: to organize the work of producing a CPS model (conceptualization), building/operating it (realization), and earning confidence in it (assurance).
- **The nine aspects — functional, business, human, trustworthiness, timing, data, boundaries, composition, lifecycle** — groupings of conceptually related concerns. Listed in Table 3, with their member concerns in Table 4.
  - When to use: to enumerate and partition stakeholder concerns so each can be tracked across all three facets.
- **The assurance-case structure (claims, evidence, argumentation, estimate of confidence)** — the elements that make up an assurance judgment in the assurance facet. Introduced in Section 2.2.3.
  - When to use: to express and substantiate that a realized CPS actually satisfies the properties asserted in its model.
- **The property tree and composition-of-concerns model** — a formal scaffold: properties of the CPS model ordered by traceability into a rooted, acyclic tree, with concern composition defined as set union of required properties. Introduced in Sections 2.2.3 and 2.4.4.
  - When to use: to trace assurance arguments and to reason about what happens when multiple concerns apply to the same CPS at once.

The Framework derives its core notions partly from two general systems-engineering references the source cites: **ISO/IEC/IEEE 42010** (for the architecture-framework, concern, view, and viewpoint conventions) and **ISO/IEC/IEEE 15288** (for system life-cycle processes). Domain-specific standards such as **ISO 26262** are cited as examples of how a facet specializes to a domain (here, functional safety in ground transportation).

## Key Concepts
- **Domain** — an application area where CPS get deployed and where stakeholders carry both domain-specific and cross-domain concerns (Table 1 gives examples ranging from aerospace and energy to healthcare, manufacturing, and transportation).
- **Concern** — an interest in the system that matters to one or more stakeholders. Concerns are the fundamental driver of the methodology; they are addressed throughout the development cycle.
- **Aspect** — a grouping of conceptually equivalent or related concerns. There are nine. Aspects and concerns are explicitly **not orthogonal**: analyzing one concern forces you to weigh related ones (the source's example: assessing the trustworthiness aspect requires considering the trustworthiness of timing).
- **Facet** — a view encompassing a set of responsibilities in the SE process; each facet bundles well-defined activities and the artifacts they output. The three facets:
  - **Conceptualization** — what the CPS should be and should do; produces the *CPS model* via functional decomposition, requirements, and logical models. The model is the theoretical ideal of the CPS, expressed as *properties*.
  - **Realization** — how the CPS is made and operated; produces, deploys, and runs the instance, including engineering trade-offs and detailed designs. Its properties are design and test elements that strive to satisfy the conceptualization's aspirational properties.
  - **Assurance** — how to reach a desired level of confidence that the CPS will behave as intended; produces claims, evidence, and argumentation confirming the conceptualization was realized as planned.
- **Property** — a concrete assertion that addresses a concern: a requirement, design element, test, or judgment. Properties span the whole lifecycle (operation and disposal included), not just early design.
- **Activity and artifact** — facets contain generic *activities* (e.g., requirements analysis, design, manufacturing) that may be tailored into activity *groups* per aspect (e.g., a timing requirements analysis nested inside requirements analysis). Each activity produces one or more *artifacts*, the concrete technical outputs. The source tables the activity/artifact lists for each facet (Tables 5–7): conceptualization runs from mission/business-case development through interface requirements analysis; realization spans business-case analysis, lifecycle management, design, manufacturing, operations, disposal, plus a cyber-physical abstraction layer and physical-layer realization; assurance runs from identifying assurance objectives through certification and regulatory-compliance testing.
- **Assurance judgment** — the unit of assurance, phrased as: the evidence is sufficient to conclude the claims hold, via the argumentation, with a stated estimate of confidence. The full **assurance case** is the set of such judgments for every property in the CPS model.
  - *Claims* are built from the CPS-model properties; the CPS "satisfies the model" when it has each of those properties.
  - *Evidence* comes from the realization facet's artifacts (process docs, design artifacts, test plans and results).
  - *Argumentation* appeals to standards, best practices/consensus, formal methods, regulation, and expert judgment.
  - *Estimate of confidence* quantifies how strongly the evidence supports the claim.
- **Structural vs. empirical arguments** — assurance arguments come in two kinds: *branching* (structural — logical or architectural composition of sub-properties) and *leaf* (empirical — a terminating property assured by a specific design D and test T, with reference to a certification, standard, or regulation).
- **Composition of concerns** — when several concerns apply at once, their combined effect is the **union** of the properties each concern requires; the operation is commutative and associative. This same set-theoretic semantics is intended to extend across the Framework in future work. The worked example is *timing security*: composing timing and security yields all properties demanded by both, including security of the time *data* and of the physical time *signal* (the source notes GPS jamming as the timing equivalent of a denial-of-service attack).

## Mental Models
- **The prism.** Picture the aspects as light passing through a prism whose faces are the facets. To see a CPS completely, you view each aspect through each face and assemble the results — and you may navigate the faces more than once. This captures why the Framework is a grid (aspect × facet), not a checklist.
- **Facets are modes, not phases.** Because CPS analysis is rarely a clean waterfall, treat the facets as *modes of analysis* you can transition between at any point in the system's lifecycle. The same grid supports waterfall, reverse engineering, agile, service-based, and gap-analysis processes — the difference is only the order in which you traverse the facets.
- **One grid, many depths and scopes.** The Framework is a template you specialize. The same structure scales from a single device (a thermostat, a camera) up through a subsystem (an HVAC unit) to a full system of systems (a utility's demand-response program), and the analysis can run deep (a tightly-coupled critical grid) or shallow (a quick conceptual comparison) without changing the vocabulary.
- **Specialize, then feed back.** Generic facet activities are deliberately abstract; you specialize them to a domain by deciding which aspects apply and updating activities/artifacts against that domain's best practices. The flow is two-way: domain specializations can validate and improve the generic conceptions in return.
- **Concerns interact — expect trade-offs.** Concerns are not independent. Hardening cybersecurity can erode safety; restoring safety can weaken cybersecurity, resilience, or reliability. Resolving these conflicts is a core task of requirements analysis, which is why the composition-of-concerns idea exists.
- **The CPS as a cognitive extension.** CPS extend human sensing, decision-making, and action — and the assurance facet exists partly to bound that extension: to estimate the uncertainty introduced and to protect human operators from errors in judgment.

## Anti-patterns
- **Treating the facets as a strict waterfall.** The source explicitly cautions that CPS analysis need not, and often is not, a waterfall; the facets are transition-able modes. Locking into linear conceptualization → realization → assurance forfeits the Framework's iteration and feedback.
- **Treating concerns/aspects as orthogonal.** The source twice warns they are not. Analyzing a concern in isolation — ignoring its interactions with related concerns — misses the trade-offs (e.g., security vs. safety) that the composition-of-concerns model is built to surface.

## Key Takeaways
1. The Framework is fundamentally an **aspect × facet grid**: nine aspects (groupings of concerns) examined through three facets (conceptualization, realization, assurance), so every cross-cutting concern is addressed at every stage.
2. The three facets map to the classic SE process (the VEE) but are best run as **interchangeable modes of analysis**, supporting waterfall, agile, reverse-engineering, service-based, and gap-analysis flows.
3. **Concerns drive everything** and are **not orthogonal** — applying several together forces trade-offs, formalized as the *composition of concerns* (set union of required properties).
4. The **conceptualization facet** produces the *CPS model* (a tree of traceable properties); **realization** builds toward those properties; **assurance** produces the *assurance case* (claims, evidence, argumentation, estimate of confidence) showing the model was met.
5. The Framework is a **template to be specialized** to a domain and scaled across device, system, and system-of-systems scopes — at whatever depth the criticality warrants.
6. It derives from general SE references (ISO/IEC/IEEE **42010** and **15288**) while emphasizing what is distinctive about CPS.

## Connects To
- **ch01 (CPS foundations / what makes CPS distinct)**: the dimensionality of CPS — SoS nesting, well-defined components, flexibility, reliability, security, data exchange, location/time awareness, legacy migration — that the Framework is built to analyze.
- **Later Vol 1 chapters (domains, related standards)**: Section 2.5's standards landscape and the domain examples that specialize the generic grid.
- **Vols 2–3 (this same pack)**: the deeper treatment of the methodology and its application; bundled here as one pack rather than split per volume.
- **`nist-sse`**: a closely parallel structuring of a hard assurance problem into interacting contexts/views with a planned-from-the-start assurance case — useful as a cross-read on framing problem, solution, and trustworthiness.
- **`sebok`**: the ISO/IEC/IEEE 15288 life-cycle processes and architecture-description conventions (42010) that the CPS Framework draws on as its general-SE base.
