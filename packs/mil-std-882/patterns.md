# MIL-STD-882E Patterns & Techniques

---

## Pattern 1: Hazard Identification Breadth-First Search

**When:** Starting any hazard identification effort (PHL, PHA) on a new or modified system.

**How:** Systematically scan across all hazard source categories before assessing any one hazard in depth: (1) system components, (2) energy sources, (3) ordnance, (4) HAZMAT, (5) interfaces and controls, (6) SoS interfaces, (7) material compatibilities, (8) inadvertent activation, (9) COTS/GOTS/NDI/GFE, (10) software, (11) operating environment, (12) procedures for all modes (operation, maintenance, test, emergency, disposal), (13) health hazards, (14) environmental impacts, (15) human factors and error analysis.

**Trade-offs:** Breadth-first identification catches more hazards early but can overwhelm analysis capacity; triage by severity potential immediately after identification to focus resource allocation.

---

## Pattern 2: Risk Assessment Code Assignment

**When:** Assessing each identified hazard at initial, target, and event stages.

**How:** (1) Determine severity category (I–IV) from Table I using worst-case outcome for death/injury, environmental impact, or monetary loss — pick the highest severity among all three dimensions. (2) Determine probability level (A–F) from Table II qualitatively or quantitatively; use Appendix A Table A-II for quantitative thresholds. (3) Combine to form RAC (e.g., 2C). (4) Map RAC to risk level (High/Serious/Medium/Low) using Table III. (5) Document all three RAC sets (initial, target, event) in HTS.

**Trade-offs:** Qualitative probability assessment introduces assessor subjectivity; quantitative data should be used whenever representative historical frequency data are available.

---

## Pattern 3: Design Order of Precedence Application

**When:** Selecting mitigation measures for any identified hazard that cannot be immediately eliminated.

**How:** Work through the five levels in order, documenting rationale for each level not selected before proceeding to the next: (1) design selection to eliminate, (2) design alteration to reduce severity/probability, (3) engineered features or devices, (4) warning devices, (5) signage/procedures/training/PPE. For Cat I/II hazards, document especially carefully why administrative controls (level 5) were not supplemented by engineering controls.

**Trade-offs:** Higher-precedence mitigations typically cost more in design/manufacturing; lower-precedence mitigations shift risk burden to operators and maintainers and are not permissible as sole mitigations for Cat I/II hazards.

---

## Pattern 4: Hazard Tracking System as Programme Record

**When:** From first hazard identification through programme end.

**How:** Every hazard record must contain: hazard description, system/subsystem, version applicability, requirements references, system mode(s), causal factor(s), effects, mishap description, initial RAC, target RAC, event RAC(s), mitigation measures (identified and selected with version traceability), hazard status, V&V method, action person(s)/org, risk acceptance record (authority, date, signed document location), hazard management log. Government access is mandatory. Data rights are "Government purpose rights."

**Trade-offs:** Comprehensive HTS maintenance is resource-intensive but creates the legal and audit trail that protects both contractor and Government in mishap investigations and programme reviews.

---

## Pattern 5: Progressive Hazard Analysis Hierarchy

**When:** Sequencing analysis tasks across programme phases.

**How:** Follow the natural design maturity progression: PHL (concept) → PHA (concept/TD) → SRHA (requirements through CDR) → SSHA (EMD detailed design) → SHA (integrated system, EMD) → O&SHA (operational environment, EMD through O&S). FHA should run in parallel to SRHA/SSHA to enable early identification of SCFs and software SCC/SwCI assignments. SoSHA and EHA are parallel tracks when applicable. Update each analysis as design changes occur.

**Trade-offs:** Maintaining multiple parallel analyses requires coordination discipline; establish a master HTS cross-reference table to prevent the same hazard from being tracked independently in multiple analysis reports.

---

## Pattern 6: Functional Hazard Analysis as Software Safety Trigger

**When:** Any system with software controlling or influencing safety-significant hardware functions.

**How:** (1) Decompose system to major component level. (2) Describe all subsystem and component functions with their interfaces. (3) For each function, identify failure modes (loss of function, degraded function, malfunction, out-of-time/sequence) and classify severity. (4) Map functions to implementing hardware, software, or human control. (5) For software-implemented functions, assign SCC (Table IV). (6) Cross SCC with severity to get SwCI (Table V). (7) Define LOR tasks from SwCI. (8) Feed SwCI assignments into SSPP/HMP software safety section and SDP.

**Trade-offs:** FHA requires early availability of functional architecture, which may not be complete at programme start; performing FHA iteratively as architecture matures is preferable to waiting for completeness.

---

## Pattern 7: Software Criticality Assessment Workflow

**When:** Assessing any software function that interacts with safety-significant hardware.

**How:** (1) Identify SSSF via FHA outputs. (2) Determine worst-case severity if the software function fails, operates incorrectly, or operates out-of-time (Cat I–IV). (3) Assess the degree of software control over that hardware function (SCC 1–5). (4) Cross SCC × severity in Table V to derive SwCI. (5) If SwCI 5: document as "Not Safety" and stop. (6) If SwCI 1–4: define required LOR tasks in the SDP and STP. (7) If LOR tasks cannot be funded/scheduled: default the system risk contribution to the Table VI risk level and escalate to PM for formal acceptance decision.

**Trade-offs:** Conservative SCC assignment (lower number = higher control) is safer but increases LOR task burden; over-assigning SCC 1 to all software inflates programme cost; under-assigning can leave safety-critical software under-analysed.

---

## Pattern 8: Event Risk Management for Test and Evaluation

**When:** Preparing for any developmental or operational test event.

**How:** (1) Update HTS with current event-specific system configuration. (2) Assess event risk (RAC) for each known hazard in the specific test configuration. (3) Identify event-unique mitigation measures (range safety zones, personnel limitations, test-specific PPE). (4) Prepare Safety Release documenting: known hazards, event risk RACs, event-unique mitigations, and formal risk acceptance status. (5) Communicate Safety Release to all test participants before event. (6) After event: analyse results for mitigation effectiveness and new hazard identification; update HTS.

**Trade-offs:** Test-unique mitigations may mask system-level risk that will reappear in operational use; distinguish clearly between mitigations that will be present operationally versus test-only controls.

---

## Pattern 9: Engineering Change Safety Gate

**When:** Any engineering change proposal, change notice, deficiency report, or waiver/deviation request.

**How:** Apply the 8-element system safety process to each change: (1) identify any new hazards introduced or existing hazards potentially modified by the change, (2) assess revised RACs, (3) identify additional mitigation measures if risk increases, (4) determine if existing formal risk acceptances remain valid post-change, (5) if new or increased risk: obtain new formal risk acceptance before implementing the change. Document all findings in HTS.

**Trade-offs:** Thorough change safety review slows change implementation velocity; risk-tier the change review effort (trivial administrative changes vs. design changes with potential safety impact) to focus resources appropriately.

---

## Pattern 10: Risk Acceptance Authority Identification

**When:** Any hazard reaches High or Serious risk level or requires formal acceptance.

**How:** (1) Consult applicable DoDI 5000 series to determine the acceptance authority level for the risk level in question. (2) Obtain user representative formal concurrence for all Serious and High risks before acceptance decision. (3) Ensure the specific system configuration and supporting documentation are provided to the Government for retention through system life. (4) After fielding: if new data reveals risk is higher than previously assessed, initiate new acceptance process under applicable DoDI 5000 series.

**Trade-offs:** DoDI 5000 series acceptance authority requirements change with programme phase; the authority sufficient for a pre-fielding test event may not be sufficient for operational fielding risk acceptance.

---

## Pattern 11: COTS/GOTS/NDI Hazard Analysis Integration

**When:** Any COTS, GOTS, NDI, or GFE item is incorporated into the system design.

**How:** (1) Obtain all available safety data from the supplier/source programme. (2) Do not assume safety compliance from prior use in a different application. (3) Assess COTS/NDI items for hazard contribution in the specific system context (PHA, SSHA, SHA levels as appropriate). (4) Re-evaluate all SCCs for legacy software incorporated into a SoS environment. (5) Include COTS/NDI interface hazards in SHA interface analysis.

**Trade-offs:** Safety data for commercial items may be incomplete or proprietary; document data gaps and address them as uncertainty in probability assessments.

---

## Pattern 12: Life-Cycle Risk Management Continuity

**When:** Transitioning from development/fielding to operations and support (O&S).

**How:** (1) Ensure the HTS and all risk acceptance documentation are transferred to the system programme office at fielding. (2) Establish procedures connecting programme safety personnel to the configuration control process for the operational system. (3) Maintain communication channels between programme office and user community for identifying new hazards and modified risks. (4) Support Class A and B mishap investigations by providing hazard analysis and mitigation recommendations. (5) Issue revised risk acceptances under DoDI 5000 series whenever fielding data reveals risk higher than pre-fielding assessment.

**Trade-offs:** O&S safety resources are typically lower than development-phase resources; establish minimum staffing thresholds and escalation triggers (e.g., fleet mishap rates) that activate elevated safety attention.

---

## Pattern 13: Health Hazard Multi-Stressor Analysis

**When:** System involves materials, noise, vibration, radiation, or operational demands with health consequences.

**How:** (1) Identify all hazardous agents (chemical: CAS number, flammability, toxicity; physical: acoustical energy, vibration, blast, thermal; biological; ergonomic; ionising and non-ionising radiation). (2) Characterise exposure pathways (inhalation, ingestion, absorption, skin contact). (3) Assess acute and chronic health risks considering synergistic effects of combined exposures. (4) Apply RAC from standard Tables I/II/III. (5) Recommend mitigation: material substitution, engineering controls, administrative controls, PPE (in design order of precedence). (6) For noise/vibration: calculate estimated levels before final design; compare to MIL-STD-1474 and ISO 2631 limits.

**Trade-offs:** Synergistic multi-stressor effects are difficult to quantify; worst-case additive assumption is conservative and may over-specify PPE requirements.

---

## Pattern 14: Explosives Hazard Classification and EOD Data Integration

**When:** System development involves explosive materials, munitions, or energetics.

**How:** For Task 402: (1) compile narrative, technical, storage/shipping, and test data per DAEHCP requirements. (2) Support classification approval process per Army TB 700-2, NAVSEA Instruction 8020.8, AF TO 11A-1-47, or DLA Reg 8220.1 as applicable. For Task 403: (3) provide EOD source data on design, functioning, and safety features. (4) Recommend render-safe procedures and disposal courses of action. (5) Provide test ordnance and training aids for EOD validation and training.

**Trade-offs:** Explosives classification testing is destructive and costly; plan for test article quantities and schedule these activities early in EMD.

---

## Pattern 15: Cross-Discipline Hazard Coordination

**When:** Multiple SE functional disciplines (fire protection, environmental, occupational health, software safety) are applying MIL-STD-882E methodology on the same programme.

**How:** (1) Establish the HMP (Task 103) rather than an SSPP to explicitly cover multi-discipline interfaces. (2) Use clearly defined terminology (e.g., "environmental hazard risk" vs. "system safety hazard") per 4.2.3.3 to prevent confusion between discipline products. (3) Establish cross-discipline IPT/WG (Task 105) with representatives from each discipline. (4) Coordinate mitigation selection across disciplines before implementing — a mitigation optimised for one discipline may introduce hazards in another. (5) Ensure discipline-specific risk products are presented at shared HTS and programme reviews.

**Trade-offs:** Cross-discipline coordination adds schedule overhead; establish a single HMP-level coordinator role responsible for integration and conflict resolution.

---

## Pattern 16: Verification Method Selection

**When:** Defining verification approaches for safety requirements (Task 401).

**How:** For each safety-significant requirement: (1) assess whether the risk of the test event itself is acceptable. (2) Prefer test (including induced/simulated failure) when feasible. (3) Use analysis (engineering calculation, simulation, model) when test is not feasible (too dangerous, too costly, no facility). (4) Use demonstration for functional performance requirements that can be observed. (5) Use inspection for design feature compliance (material, dimensions, labelling). (6) For software: include safety-specific testing (fault injection, boundary testing, out-of-bounds, interface failure) beyond standard functional testing for SwCI 1–3.

**Trade-offs:** Analysis-based verification is faster and cheaper but provides less empirical confidence than test; document the analytical basis and assumptions thoroughly for high-criticality safety requirements.
