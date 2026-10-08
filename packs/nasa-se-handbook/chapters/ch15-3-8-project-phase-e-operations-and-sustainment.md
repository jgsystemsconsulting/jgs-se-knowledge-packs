# Chapter 15: 3.8 Project Phase E: Operations and Sustainment

## Core Idea
Phase E executes the prime mission to meet initially identified stakeholder needs while maintaining system support, with systems engineering personnel continuing to oversee integration, anomaly resolution, and evolution — but only within the existing architecture; major architectural changes trigger a new project lifecycle.

## Frameworks Introduced
- **Mission Operations Plan**: The operational directive that guides Phase E execution
  - When to use: as the governance document for all operational activities, modifications, and support strategy during the mission
  - Key INPUTS: The validated, as-built system delivered from Phase D (verification and validation results, as-built documentation), the ConOps, prime mission objectives and success criteria, and the approved sustainment strategy.
  - Key ACTIVITIES: Execute the prime mission per plan; convene PLAR, CERR, and upgrade and safety reviews; route anomalies through SE root-cause diagnosis; approve and implement configuration changes within the current architecture; request and justify mission extensions.
  - Key OUTPUTS: Executed prime mission objectives, dispositioned anomalies with root causes, approved configuration changes and uplinks, updated operations documentation, and an extension recommendation or a decommissioning handoff to Phase F.
  - Governance rule: an activity, modification, or objective not in the mission operations plan does not happen until the plan is updated and approved.
- **Sustainment Support Strategy**: Planned maintenance, spares provisioning, operator training, and system evolution within the current architecture
  - When to use: to ensure continuity of mission capability and readiness for extended operations or follow-on mission objectives
  - Key INPUTS: The enablement package delivered at transition (manuals, training, support equipment), as-built configuration documentation, spares and maintenance plans, and the operator training baseline.
  - Key ACTIVITIES: Execute planned maintenance and spares provisioning, train operators, evolve the system within the current architecture, and re-verify and re-validate every change (regression testing after software corrections).
  - Key OUTPUTS: Sustained mission capability and readiness for extended operations or follow-on objectives, configuration documentation kept current, and lessons learned captured for follow-on missions.
  - When to update: at each approved configuration change, mission extension, or increment boundary, so support provisioning tracks the system actually flying.

## Key Concepts
- **Prime Mission**: The initially planned mission objectives and operational period, distinguished from extensions or evolved objectives
- **On-Orbit Assembly**: Extended operational configuration activities (e.g., space station increments) that may require reiteration of SE processes during Phase E
- **Mission Extension**: A formal request and approval process to continue mission activities or pursue additional objectives beyond the originally planned duration
- **In-Flight Anomaly Resolution**: Systems engineering involvement in diagnosing and resolving unexpected failures or degraded performance during operations
- **Configuration Changes**: Modifications and new mission objectives that may recur with repeated operations (e.g., multiple flights of the same platform)
- **Sustainment Evolution**: System improvements and upgrades that remain within the existing architecture; changes exceeding this scope constitute new needs and restart the lifecycle
- **Cruise/Orbit Insertion Phase**: Extended initial operational period for complex systems (e.g., planetary probes) involving commissioning, instrument activation, and shakedown operations
- **Software Uplink**: Continued software development and deployment post-launch (e.g., for planetary probes or space station modules)
- **Mission-Extension Approval Mechanics**: An extension is a formal request evaluated for technical and programmatic feasibility (residual risk posture, remaining spares, funding, staffing) and approved through program governance before operations pursue additional objectives; approval updates the mission operations plan and sustainment strategy rather than silently stretching them.
- **PLAR and CERR Under Review Discipline**: Post-Launch Assessment Review and Critical Event Readiness Reviews are Standing Review Board-convened reviews, so they carry the same entrance and success criteria discipline as earlier gates; findings disposition through the same RID/RFA-style tracking toward closure.
- **Software-Uplink SE Oversight**: Post-launch software development stays under SE oversight; changes route through configuration control as change requests, are verified and validated before uplink, and corrections ship with regression testing so previously accepted function is not broken in flight.
- **V&V Continues Into Operations**: Verification and validation do not end at launch; every modification, upgrade, and anomaly fix is re-verified against requirements and re-validated against stakeholder expectations in the operational environment, which is the environment the ConOps described.
- **Specialty Engineering Stays Engaged**: Maintainability, logistics, software, and human factors engineering remain active in Phase E because operational experience generates change requests; their design-input role from earlier phases flips to a change-evaluation role.
- **Repeated-Operations Configuration Cycles**: Systems operated in repeated increments (space station assemblies, multiple flights of one platform) re-enter configuration change cycles each increment; every new configuration gets the same change-control and re-verification discipline as the first.
- **Decommissioning Handoff Preparation**: Phase E ends at the decommissioning and disposal boundary; KDP F and the Phase F disposal review (DR/DRR) consume Phase E's configuration documentation and operational history.

## Mental Models
- **Think of Phase E as "architecture-constrained evolution"**: the system evolves to meet new operational demands, but only within its original architectural bounds; any change that breaks the architecture is a new project.
- **Use in-flight anomaly resolution as an SE responsibility hook**: if operations encounter unexpected failures, SE personnel are engaged to diagnose root causes and evaluate system-level implications, not just tactical fixes.
- **Recognize software as a continuous Phase E activity**: unlike hardware, software development often continues well into operations, requiring active SE oversight for integration, validation, and traceability.
- **Treat Phase E changes as a compressed realization loop**: every approved modification runs a miniature engine pass (requirements for the change, design within the architecture, implement, verify, validate, transition back to operations), which is why specialty engineering and V&V stay staffed in Phase E.

## Anti-patterns
- **Treating anomaly resolution as purely tactical**: Closing an in-flight anomaly purely inside the operations team, without SE engagement for root cause, system interactions, and mission-level implications, leaves latent defects in the fleet and invites repeat failures. The same discipline as verification discrepancies applies: stop, diagnose whether the product or the procedure and environment are at fault, disposition formally, and re-verify the fix (with regression testing for software) before returning to operations.
- **Treating descope planning as an operations afterthought**: Descope options are developed alongside NGO documentation during formulation and baselined only if needed; a program that waits until Phase E resource shortfalls force scope reduction has no pre-agreed degradation paths, so success criteria get renegotiated mid-crisis with stakeholders. The upgrade and evolution strategy in the sustainment plan follows the same rule: plan it before Phase E, execute it by the mission operations plan.

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
- **Program Implementation (Section 3.2)**: Phase E executes inside program implementation governance; mission-extension requests and any descope activation route through the same review and KDP discipline as earlier phases.
- **Product Implementation (Section 5.1)**: The as-built documentation and enablement package handed off at transition are what sustainment maintains against; configuration documentation current at launch stays current through operations.
- **Product Verification (Section 5.3)**: Anomaly diagnosis reuses discrepancy management (product fault versus procedure or environment fault), and every fix is re-verified before return to flight or uplink.
- **Product Validation (Section 5.4)**: Operations is the real validation environment; anomalies and workarounds observed in flight are validation evidence against the ConOps and feed follow-on mission planning.
- **Technical Assessment (Section 6.7)**: PLAR and CERR readiness and anomaly-burndown tracking run on the same review and assessment machinery as earlier gates.
- **Phase F (Section 3.9)**: Decommissioning and disposal closeout consumes Phase E records; the KDP F gate ends what KDP E began.
