# Chapter 8: Services Viewpoint (SvcV)

## Core Idea
The Services Viewpoint describes **services as a specific type of performer** — they compose (have parts), consume and produce resources, interface with systems and other services, perform activities, obey rules, transition through states, and evolve over time. The SvcV mirrors the Systems Viewpoint (SV) in structure but focuses on services rather than systems. Twelve SvcV models provide the full behavioral and structural specification of services, from composition and interfaces through to evolution and dynamic behavior.

## Frameworks Introduced
- **SvcV-1: Service Composition**: Shows service composition (parts) and service-to-service and service-to-system interfaces. Each service is related to a service description.
  - When to use: As the foundational SvcV model; defines which services exist, how they are composed, and what resources flow between them.
- **SvcV-2: Service Resources**: Identifies resource flows between services, with detail on the resources consumed and produced, grouped by service and service part.
  - When to use: When detailing interface content between services; uses only systems and services already identified in SvcV-1.
- **SvcV-3a: Services and Systems**: Shows interface relationships between services and systems.
  - When to use: For cross-domain interface analysis where systems and services co-exist; derived from SvcV-1 and SV-1 data.
- **SvcV-3b: Service Relationships**: Shows interface relationships among services only (no systems).
  - When to use: For pure service-to-service interface analysis within a service-oriented architecture; systems must not appear.
- **SvcV-4: Service Functions**: Shows the hierarchical decomposition of service activities and their resource flows. Analogous to SV-4 for systems.
  - When to use: When specifying the internal functional structure of a service; to decompose service activities into parts.
- **SvcV-5: Service Operational Activities**: Maps service activities to the operational activities (from OV-5b) that they support or provide.
  - When to use: As the SvcV-to-OV traceability link; shows which services support which operational needs.
- **SvcV-6: Service Resource Flows**: Detailed view of service resource flows including the activities performed, resources exchanged, and associated rules and measures.
  - When to use: When QoS specifications, timeliness, or throughput measures must be attached to service interfaces.
- **SvcV-7: Service Measures**: Documents measures (metrics) of service model elements for specified timeframes.
  - When to use: For SLA definition and service performance analysis.
- **SvcV-8: Service Evolution**: Shows planned incremental steps to migrate a suite of services to a more efficient suite or to evolve current services.
  - When to use: During technology refresh planning; for SOA modernization roadmaps.
- **SvcV-9: Service Technology and Skills Forecast**: Identifies emerging technologies, software/hardware products, and skills expected to influence future service development.
  - When to use: For technology horizon scanning and workforce planning in service-oriented environments.
- **SvcV-10a: Service Rules**: Documents rules that constrain services and the activities they perform.
  - When to use: For documenting service policies, access constraints, and operational rules governing service behavior.
- **SvcV-10b: Service State Transitions**: Shows how services change state in response to events.
  - When to use: For modeling dynamic service behavior, especially in real-time or event-driven service architectures.
- **SvcV-10c: Service Activity Sequences**: Event-trace models showing sequences of service activities.
  - When to use: For sequence analysis, protocol verification, and choreography specification of service interactions.

## Key Concepts
- **Service (DM2)** — A type of performer that enables access to a set of capabilities through a prescribed interface, exercised consistent with service policies. Services are not limited to IT/web services; they include non-IT services such as search and rescue.
- **Service Description** — A self-describing artifact that provides all information needed to use a service and no more: visible functionality, QoS, interface descriptions, data descriptions, and references to standards. Does not expose internal workings.
- **Business Service** — A service providing business functions (writing checks, ordering parts); contrasted with enabling services that support technical functions.
- **Enabling Service** — A technical service that supports business services or operational activities; governed by EnablingServiceStandard constraints.
- **Service Composition** — The structural whole-part relationship of services: a service may be a composite of other services and systems, enabling orchestration and choreography.
- **QoS (Quality of Service)** — Measures attached to service resource flows in SvcV-6; examples include timeliness, throughput, reliability, and accuracy.
- **SvcV-1/SV-1 Parallel Structure** — SvcV and SV models examine the same subject (performers and interfaces) but emphasize different performer types. Organizations may choose to emphasize systems (SV) or services (SvcV) depending on their architectural style; DoDAF does not prescribe the emphasis.

## Mental Models
- Use SvcV-1 before SvcV-2 through SvcV-10c: all subsequent SvcV models are derived from SvcV-1; none may introduce services, systems, or activities not already in SvcV-1.
- Use SvcV-3a when the architecture contains both systems and services; use SvcV-3b when the architecture is purely service-oriented.
- Use SvcV-5 as the accountability link: it answers "which services deliver which operational activities?" — the SOA traceability question.

## Anti-patterns
- Treating SvcV-2 through SvcV-10c as independent models: they are all derivative of SvcV-1 and may not introduce new elements.
- Assuming services are software-only: DoDAF services include human and organizational services; the service concept is broader than SOA or web services.
- Using SvcV models without a corresponding OV: services exist to support operational activities; without OV-5b, SvcV-5 has nothing to trace to.

## Key Takeaways
1. Services are performers in the DM2 — everything true of performers (activities, resources, rules, measures, locations) applies to services.
2. The twelve SvcV models parallel the SV models in structure; the choice between SV and SvcV emphasis is architectural style, not DoDAF prescription.
3. SvcV-1 is the foundation: all other SvcV models draw from it and may not extend its scope.
4. Service descriptions are first-class DM2 elements — self-description is a defining characteristic of services in DoDAF, enabling discovery and use in net-centric environments.
5. SvcV-8 and SvcV-9 are the service-layer technology planning tools, analogous to SV-8/SV-9 for systems.

## Connects To
- **Chapter 4 (Capability Viewpoint)**: CV-7 maps capabilities to services; SvcV-1 provides the service-composition detail.
- **Chapter 6 (Operational Viewpoint)**: SvcV-5 maps to OV-5b activities — the primary traceability link from services to operational needs.
- **Chapter 10 (Standards Viewpoint)**: Business service standards (BusinessServiceStandard) and enabling service standards (EnablingServiceStandard) constrain service activities.
- **Chapter 11 (Systems Viewpoint)**: SvcV-3a shows the service-system interface; SV-3 shows the system-system equivalent.
