# Chapter 15: 3.8 Project Phase E: Operations and Sustainment

## Core Idea
Phase E executes the prime mission to meet initially identified stakeholder needs while maintaining system support, with systems engineering personnel continuing to oversee integration, anomaly resolution, and evolution — but only within the existing architecture; major architectural changes trigger a new project lifecycle.

## Frameworks Introduced
- **Mission Operations Plan**: The operational directive that guides Phase E execution
  - When to use: as the governance document for all operational activities, modifications, and support strategy during the mission
- **Sustainment Support Strategy**: Planned maintenance, spares provisioning, operator training, and system evolution within the current architecture
  - When to use: to ensure continuity of mission capability and readiness for extended operations or follow-on mission objectives

## Key Concepts
- **Prime Mission**: The initially planned mission objectives and operational period, distinguished from extensions or evolved objectives
- **On-Orbit Assembly**: Extended operational configuration activities (e.g., space station increments) that may require reiteration of SE processes during Phase E
- **Mission Extension**: A formal request and approval process to continue mission activities or pursue additional objectives beyond the originally planned duration
- **In-Flight Anomaly Resolution**: Systems engineering involvement in diagnosing and resolving unexpected failures or degraded performance during operations
- **Configuration Changes**: Modifications and new mission objectives that may recur with repeated operations (e.g., multiple flights of the same platform)
- **Sustainment Evolution**: System improvements and upgrades that remain within the existing architecture; changes exceeding this scope constitute new needs and restart the lifecycle
- **Cruise/Orbit Insertion Phase**: Extended initial operational period for complex systems (e.g., planetary probes) involving commissioning, instrument activation, and shakedown operations
- **Software Uplink**: Continued software development and deployment post-launch (e.g., for planetary probes or space station modules)

## Mental Models
- **Think of Phase E as "architecture-constrained evolution"**: the system evolves to meet new operational demands, but only within its original architectural bounds; any change that breaks the architecture is a new project.
- **Use in-flight anomaly resolution as an SE responsibility hook**: if operations encounter unexpected failures, SE personnel are engaged to diagnose root causes and evaluate system-level implications, not just tactical fixes.
- **Recognize software as a continuous Phase E activity**: unlike hardware, software development often continues well into operations, requiring active SE oversight for integration, validation, and traceability.

## Key Takeaways
1. **SE doesn't end at launch**: systems engineering remains active during Phase E to manage integration overlaps, anomalies, and architectural consistency — particularly for complex systems with repeated operations or extended initial shakedown periods.
2. **Distinguish prime mission from extension**: the prime mission is pre-planned; extensions are formal requests evaluated for technical and programmatic feasibility, requiring mission extension authorization.
3. **Sustaining support is planned, not reactive**: the spares plan, operator training, maintenance procedures, and upgrade strategy are prepared before Phase E and executed according to the mission operations plan.
4. **Specialty engineering continues in Phase E**: maintainability, logistics, software development, and human factors engineering remain active and may require reiteration of common SE processes as operational experience informs design improvements.
5. **Architectural changes restart the lifecycle**: evolution within the current architecture is Phase E work; major changes (new subsystems, fundamental redesign) constitute new needs and initiate a new project cycle.
6. **Anomaly resolution is SE-level work**: in-flight failures or degraded performance engage systems engineers to assess root causes, system interactions, and mission-level implications before operational corrective actions are approved.
7. **Multiple review gates ensure mission readiness**: Post-Launch Assessment Review (PLAR), Critical Event Readiness Reviews (CERR), system upgrade reviews, and safety reviews maintain SE rigor and traceability throughout Phase E.

## Connects To
- **NPR 7120.5 (NASA Procedural Requirements for Safety and Mission Assurance)**: defines the Phase E technical activities and review entrance/success criteria that SE must satisfy.
- **NPR 7123.1 (NASA Procedural Requirements for Systems Engineering)**: specifies the Phase E review structure and SE governance checkpoints.
- **ISO/IEC/IEEE 15288 (System and Software Engineering — System Lifecycle Processes)**: Phase E aligns with the "Operation and Support" stage of the system lifecycle, where deployed systems are operated and maintained.
- **Post-Flight Evaluation and Lessons Learned**: Phase E captures operational data, identifies failure modes, and documents lessons for application in follow-on missions or architecture refreshes.
