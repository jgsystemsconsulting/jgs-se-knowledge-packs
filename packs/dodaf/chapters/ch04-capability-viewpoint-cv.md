# Chapter 4: Capability Viewpoint (CV)

## Core Idea
The Capability Viewpoint addresses the concerns of **capability portfolio managers**. It frames capabilities as structured relationships between desired resource states (effects), the activities that produce those states, the performers and resources involved, the conditions under which activities are carried out, and the rules that constrain them. Seven CV models provide progressively more detailed perspectives on capability effects, hierarchies, schedules, dependencies, deployments, constituent activities, and service realization.

## Frameworks Introduced
- **CV-1: Capability Effects**: Identifies effects caused by capabilities and specifies measures for those effects (Measures of Effect and Measures of Desire). Emphasizes responsible performers, desired resource states, and the activities that produce them.
  - When to use: For strategic portfolio analysis — understanding what capabilities deliver and how much decision-makers value those deliveries.
- **CV-2: Capability Hierarchies**: Shows capability taxonomy — whole-part (decomposition) and super-subtype (categorization) relationships among capabilities.
  - When to use: When building or validating a capability taxonomy for portfolio investment decisions; to compare capabilities by their shared activities, conditions, and resource states.
- **CV-3: Capability Schedules**: Presents deployment schedules in terms of timelines — temporal ordering of activities and resource availability linked to project types.
  - When to use: When analyzing the temporal dimensions of capability delivery; to identify schedule gaps between need and availability.
- **CV-4: Capability Dependencies**: Shows dependencies among the effects caused by capabilities — which capability effects are prerequisites for others.
  - When to use: When sequencing capability investments; for risk analysis of capability interdependencies.
- **CV-5: Capability Deployments**: Shows schedules for capability deployment in terms of organizations and locations — where and with whom capabilities will be deployed over time.
  - When to use: When planning organizational transitions or geographic deployment of capabilities.
- **CV-6: Capability Activities**: Maps activities to capabilities — which activities are part of which capability, showing the activity structure that produces desired effects.
  - When to use: When tracing from capability requirements down to trainable activities and performers; for DOTMLPF analysis.
- **CV-7: Capabilities and Services**: Maps capabilities to services — showing how services realize or support capabilities.
  - When to use: When analyzing service-oriented architectures in relation to capability requirements; to identify service reuse opportunities.

## Key Concepts
- **Capability** — The ability to achieve a desired effect under specified standards and conditions through combinations of ways (guidance and rules) and means (resources and performers) to perform a set of tasks. Defined consistently with the JCIDS Instruction.
- **Desired Effect (Desired Resource State)** — The resource state to be achieved by a capability. Ontologically synonymous with goals, objectives, and outcomes in the DM2. Incorporates: (a) initial resource state, (b) desired resource state, (c) measures of the difference between them.
- **Measure of Effect** — A measure of the difference between an initial (less-desired) resource state and a desired (more-desired) resource state; quantifies what the capability achieves.
- **Measure of Desire** — How much a responsible performer wants a desired effect; may be expressed as priority, budget commitment, or risk calculus.
- **Responsible Performer (PerformerCapableOfResponsibility)** — An organization or person in a role that envisions a desired effect and is accountable for it. In CV-1, only responsible performers are modeled (not general performers).
- **Vision Statement** — A documentation of the desired effect envisioned by a responsible performer; links strategic intent to measurable capability effects.
- **DOTMLPF** — Doctrine, Organization, Training, Materiel, Leadership and Education, Personnel, Facilities — the DoD framework for capability analysis. The DM2 models each DOTMLPF factor through rules, performers, activities, materiel, skills, persons in roles, and locations respectively.
- **Condition** — The context under which activities are performed (e.g., environment, threat density, weather). Different conditions require different activities and different performers to achieve the same desired effect.

## Mental Models
- Use CV-1 when Y = "what does this capability achieve and how much do we want it?" — start with effects and measures of desire, not with systems or organizations.
- Use CV-2 when Y = "how do capabilities relate to each other structurally?" — decompose (whole-part) to find what capabilities comprise, categorize (super-subtype) to find what capabilities share.
- Use CV-6 as the bridge from strategic to operational: capabilities decompose into activities; activities are then the starting point for Operational Viewpoint models.

## Anti-patterns
- Modeling activities and performers in CV-1 beyond what is needed to show the relationship to capabilities and effects — CV-1 is effects-focused; detailed activity and performer data belongs in OV and SV models.
- Conflating capabilities with systems: a capability is a combination of activities, conditions, rules, and resources; a system is one type of performer that may be part of a capability configuration, not the capability itself.
- Distinguishing goals from objectives from outcomes: the DM2 treats these as ontologically equivalent (desired resource states); do not introduce a separate hierarchy.

## Key Takeaways
1. The CV is the bridge between strategic intent (vision, desired effects) and operational/system design (activities, performers).
2. Desired effects are resource states, not vague outcomes — they must be measurable via Measures of Effect.
3. The seven CV models form a progression: effects (CV-1) → hierarchy (CV-2) → schedule (CV-3) → dependencies (CV-4) → deployment (CV-5) → activities (CV-6) → services (CV-7).
4. DOTMLPF factors are all expressible in DM2 terms, making the CV the DoDAF integration point for capability-based analysis.
5. Conditions are first-class citizens in the CV: the same capability may require completely different activities and performers depending on operational conditions.

## Connects To
- **Chapter 7 (Operational Viewpoint)**: CV-6 activities feed OV-5b; OV models detail how activities are performed by organizations and persons in roles.
- **Chapter 8 (Project Viewpoint)**: PV-3 maps projects to capabilities — CV defines what capabilities are needed; PV-3 shows which projects deliver them.
- **Chapter 9 (Services Viewpoint)**: CV-7 maps capabilities to services; SvcV models detail how those services are structured and resourced.
- **Chapter 11 (Systems Viewpoint)**: SV-5b maps systems to capabilities, showing the system-level implementation of CV-defined capability requirements.
