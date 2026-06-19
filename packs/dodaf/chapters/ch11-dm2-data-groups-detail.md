# Chapter 11: DM2 Data Groups — Detailed Reference

## Core Idea
This chapter provides a detailed reference for each of the eight principle DM2 data groups, covering their internal structure, key relationships, and specific uses across DoD core processes. Each data group is both a semantic cluster and a reusable building block — understanding their internal mechanics is essential for correctly populating the shared DM2 data store that underpins all DoDAF viewpoint models.

## Frameworks Introduced
- **Performers Data Group**: The "who" of architectures — persons in roles, organizations, systems, services, and their combinations. Central to every viewpoint; the activity-performer assignment/allocation relationship is the primary structural mechanism.
  - When to use: Whenever the architecture must specify who performs what; for JCIDS TTP documentation, DAS WBS development, SE functional allocation.
- **Resource Flows Data Group**: The "how things connect" of architectures — models all flows of materiel, information, persons, and performers as triples: producing activity + consuming activity + resource.
  - When to use: For interface definition, interoperability analysis, SOA publish/subscribe specifications, and configuration management of interfaces.
- **Information and Data Group**: The "what is known" at three abstraction levels — conceptual (meaning), logical (structure), physical (encoding). Drives DIV models.
  - When to use: For COI harmonization, information sharing requirements, data model generation, and standards establishment.
- **Rules Data Group**: The "what constrains behavior" — rules, standards, agreements, guidance. Always constrains activities, never performers directly.
  - When to use: For doctrine, TTP, standards, and business rule documentation across all processes.
- **Capabilities Data Group**: The "what effects are sought" — links activities, performers, resources, and conditions to desired resource states via capability configurations.
  - When to use: For DOTMLPF analysis, capability-based assessment, and portfolio investment decisions.
- **Services Data Group**: The "what is offered through prescribed interfaces" — services as performers with self-descriptions, business services distinct from enabling services.
  - When to use: When designing SOA, documenting net-centric services, or analyzing service-capability relationships.
- **Projects Data Group**: The "what is being built and by whom" — temporary activities with WBS structures, milestones, and PPBE program elements.
  - When to use: For DAS/PPBE integration, WBS development, earned value management support.
- **Organizational Structures Data Group**: The "how entities are organized" — types of organizations, specific organizations, persons in roles, and their whole-part hierarchies.
  - When to use: When the architecture must model organizational mandates, command structures, or workforce compositions.

## Key Concepts
- **Assignment vs. Allocation** — Assignment: a performer is specifically designated to carry out an activity (concrete). Allocation: a performer is associated with an activity in an abstract, preliminary way as a precursor to assignment. Allocation occurs early in design; assignment occurs when the design is sufficiently mature to declare an allocated baseline.
- **Activity-Performer Overlap** — The DM2's spatio-temporal representation of "a performer performs an activity": at some place and time, the activity and performer overlap. Two types: (1) activityPerformedByPerformer (direct assignment), and (2) activityPartOfCapability with activityPerformableUnderCondition (allocated context).
- **Resource Flow Triple** — The core relationship for all exchanges: (producing activity) → (resource) → (consuming activity). All resource flows require this triple; direct performer-to-performer transfers are not modeled — they must go through activities.
- **Publication-Subscription Model** — A specific resource flow pattern: a publishing activity produces a resource at one time/place; a subscribing activity consumes it at a different time/place. Both are modeled as overlaps with the resource.
- **Desired Resource State** — The ontological representation of a goal, objective, or outcome. Because the DM2 is four-dimensional and meronymic, any future state of any resource (including complex aggregates like PMESII environments) can be modeled as a desired resource state.
- **Capability Configuration** — A specific combination of performers (typically aggregates of air, space, and cyber assets at specified locations with specified measures) that can provide a capability.
- **Service Self-Description** — A first-class DM2 element: a service description provides all information needed to use the service (visible functionality, QoS, interface, data, and policy) without exposing internal workings.
- **WBS as Architecture** — The WBS is not just a project management tool; it is the primary DoDAF-to-DAS/PPBE integration artifact, connecting architecture performers and activities to cost structures and contract requirements.
- **Organizational Mandate** — In the DM2, organizations have missions; these missions are modeled as activities the organization is mandated to perform; organizational structure (whole-part) represents command and subordination relationships.
- **Person in Role** — A type of performer in the DM2 that includes the materiel assigned to carry out the role (per Army CTA standards). Temporal whole-parts (states like in-garrison, deployed) may have different materiel compositions.

## Mental Models
- The resource flow triple is the atomic interoperability element: if you cannot express an exchange as "activity A produces resource R; activity B consumes resource R," the flow is either not modeled or is modeled incorrectly.
- Allocation precedes assignment: never assign performers to activities before sufficient architectural definition exists; allocation is the placeholder, assignment is the commitment.
- Services self-describe; systems do not: the presence of a ServiceDescription class in the DM2 is a functional difference between services and systems — services are designed to be discovered and used without knowing their internals.

## Anti-patterns
- Modeling resource transfers directly between performers: all resource movements must go through producing and consuming activities. A system "sending" data to another system is modeled as activity-produces-data / activity-consumes-data, not system-to-system.
- Creating rules for performers rather than activities: rules constrain activities; performers are affected only by virtue of the activities they perform. A rule that "system X must encrypt data" is modeled as a rule constraining the activity of transmitting data, not as a property of the system.
- Using Organizational Structures as an org-chart substitute: OV-4 is the viewpoint model for organizational relationships; the Organizational Structures data group provides the underlying data. The data group captures formal organizational definitions; OV-4 presents them.

## Key Takeaways
1. All eight principle data groups are semantically linked through the performer-activity-resource triad; no data group is standalone.
2. Assignment vs. allocation is a lifecycle distinction: allocation is for preliminary design; assignment is for committed design.
3. The resource flow triple (producing activity → resource → consuming activity) is the invariant structural pattern for all data exchanges across all viewpoints.
4. Desired resource states are the DM2's formal treatment of goals and outcomes; the four-dimensional ontology makes complex effect modeling (PMESII) tractable.
5. Services are more than IT constructs: the DM2 service type covers any capability realized by a performer through a prescribed interface, from web APIs to search and rescue operations.
6. The WBS is the primary DAS/PPBE integration artifact; the Projects data group makes the WBS an architectural element with full traceability to performers, activities, and resource flows.

## Connects To
- **Chapters 3–10 (Viewpoints)**: Each viewpoint selectively surfaces specific data groups; this chapter provides the data-level reference underlying every viewpoint model.
- **Chapter 1 (Introduction)**: The IDEAS Foundation types (Individual, Type, IndividualType, TupleType) govern how all data group elements are typed and related.
- **Chapter 2 (DM2 Overview)**: The summary table of data groups to viewpoints and processes is the navigation index; this chapter provides the detail.
