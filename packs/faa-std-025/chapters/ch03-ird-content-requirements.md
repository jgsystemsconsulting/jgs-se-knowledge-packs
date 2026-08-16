# Chapter 3: IRD Content Requirements

## Core Idea
FAA-STD-025f details what an IRD must specify so interface *requirements* are complete across common, medium-specific (analog/discrete), service/web, and facility cases—covering functions, security, physical/power factors, and performance with tolerances.

## Frameworks Introduced
- **Common IRD requirements block**: General functions/services/options/physical needs; interconnectivity identity; functional, security, physical, and electrical/electronic requirement groups.
- **Medium-specific IRD slices**: Analog interface requirements; discrete interface requirements.
- **Service IRD slices**: General service (application process + protocol implementation) and web service (required web services + protocol implementation).
- **Facility IRD slice**: Physical/space/electrical/environmental and project-unique site preparation requirements (no ICD counterpart required).

## Key Concepts
- **Interface requirements section**: Specify general functions, services, options, and physical requirements among interfacing subsystems/services; align detailed protocol-layer features with the governing functional specification; include performance with tolerance measures.
- **General requirements / demarcation**: Identify interfacing subsystem(s), points of interface (including cable terminations), and connectivity functions/services. Document end systems, intermediate systems, upper/lower protocol layers, and the physical demarcation point.
- **Functional requirements**: Required in every IRD; content varies by interface purpose (analog, discrete, general service, web service). Facility IRDs emphasize physical requirements in the corresponding slot.
- **Security requirements**: Based on joint risk assessment by end-users and service providers; address data sensitivity/criticality, exposure at both ends, and all security disciplines. Document every layer used for security. Align with applicable FAA orders spanning information security, sensitive unclassified information, personnel, contractor, facility, NAS data, access control, network, internet, and web management.
- **Physical requirements**: When one subsystem supplies electrical, mechanical, or environmental support to another, document performance and tolerances as appropriate.
- **Electrical power and electronic requirements**: Only when one subsystem provides power to another. Factors include voltage, frequency, current, transients, harmonics, polarity/phases, overload protection, power factor, noise, load balancing, impedance, grounding/shielding—plus connectors, wire/cable limits, grounding, fasteners, and EMC as applicable (often referencing FAA-G-2100, FAA-C-1217, FAA-STD-019). Select a single FAA-G-2100 revision (g or h) per document.
- **Service/web depth**: Application-process and protocol-implementation subsections capture message/structure and stack choices for general and web services.

## Mental Models
- **Specify the boundary, not the internals**: IRD content stops at what each side must provide/accept at the interface.
- **Risk-driven security**: Security shalls come from a bilateral risk picture, not a generic checklist dump.
- **Facility IRD as site-readiness contract**: Iterations (initial through final) progressively firm space/power/environment data for transition planning.

## Anti-patterns
- Protocol detail inconsistent with the cited functional specification.
- Security section that ignores one end of the interface or omits layers actually used.
- Mixing both FAA-G-2100g and 2100h power baselines in one IRD.
- Facility IRDs that never mature beyond the initial reservation iteration.

## Key Takeaways
1. IRDs specify shall-requirements with performance/tolerances across a typed outline.
2. Demarcation, functions, security, physical, and power blocks are the common technical spine.
3. Analog/discrete/service/web/facility variants add or emphasize medium-specific slots.
4. Power/EMC/connector detail is conditional but rigorous when applicable.

## Connects To
- **ch02**: Outline and common sections that frame these details.
- **ch04**: ICD mirrors these slots as design characteristics.
- **ch05**: Every shall maps into the VRTM.
- **ch06**: IRD approval path and CM baselining.
