# Chapter 8: Task Section 400 — Verification Tasks

## Core Idea
The 400-series tasks close the safety loop by confirming that mitigation measures actually work as intended and that system hardware, software, and procedures comply with identified safety requirements. Task 401 (Safety Verification) is the general verification task applicable to any system; Tasks 402 and 403 address specialised explosives and EOD domains. Verification uses multiple methods — analysis, test, demonstration, inspection — and the results feed directly into the SAR/HMAR (Task 300) and the formal risk acceptance process.

## Frameworks Introduced

- **Task 401 — Safety Verification**: defines and performs tests, analyses, demonstrations, or other verification methods on safety-significant hardware, software, and procedures to confirm compliance with safety requirements. Results are documented in a verification report.
  - When to use: whenever the adequacy of risk mitigation measures cannot be established through design review alone; integrated into system T&E plans.

- **Task 402 — Explosives Hazard Classification Data**: performs tests and analyses to support compliance with DoD Ammunition and Explosives Hazard Classification Procedures (DAEHCP); provides hazard classification approval documentation for new or modified explosives and energetic-containing commodities.
  - When to use: any programme developing or acquiring explosives, energetics, or packages containing explosive materials.

- **Task 403 — Explosive Ordnance Disposal (EOD) Data**: provides detailed EOD source data, recommended render-safe procedures, disposal courses of action, test ordnance for EOD validation, and training aids for EOD training.
  - When to use: any programme involving explosive ordnance, weapons systems, or unmanned systems that may require EOD response.

## Key Concepts

- **Verification methods**: analysis, test (including induced/simulated failures), demonstration, inspection, and analogies/models/simulations. All methods are valid; the selection depends on feasibility, cost, and the nature of the mitigation being verified.
- **Induced or simulated failures**: Task 401 specifically states that "induced or simulated failures shall be considered to demonstrate the acceptable safety performance of the equipment and software" — fault injection and failure mode testing are required considerations, not optional enhancements.
- **Safety-specific testing (in LOR context)**: required for SwCI 1–4 as the minimum verification activity for software; "in-depth safety-specific testing" (SwCI 1–3) goes beyond standard functional testing to exercise safety-critical boundaries, fault conditions, and interface failure modes.
- **Independent Verification and Validation (IV&V)**: mentioned in Appendix B as a test task consideration for safety-significant software; provides independent assessment separate from the developer's own testing.
- **Verification integration with T&E**: Task 401 requires safety verification to be integrated into appropriate system T&E plans, including verification and validation plans; safety tests are not stand-alone activities but are scheduled within the broader T&E programme.
- **Non-feasibility alternatives**: when safety tests are not feasible (hazard too great, cost prohibitive, no test facility), Task 401 requires the contractor to recommend verification through engineering analyses, analogies, laboratory tests, functional mockups, or models and simulations — non-testable requirements are not automatically waived.
- **DAEHCP compliance**: Task 402 references Army Technical Bulletin 700-2, Naval Sea Systems Command Instruction 8020.8, Air Force Technical Order 11A-1-47, and Defense Logistics Agency Regulation 8220.1 as the specific classification procedures governing explosives hazard classification.
- **EOD data scope (Task 403)**: covers explosive ordnance design, functioning, safety features, render-safe procedures, disposal courses of action, test assets for EOD validation, and training aids — provides the EOD community with the information needed to safely respond to accidents or emergencies involving the ordnance.

## Mental Models

- **"Verification closes the design order of precedence loop"** — every mitigation selected under Element 4 and implemented under Element 5 must be verified under Element 6; no mitigation is complete until verification evidence is in the HTS.
- **"Can't test it? Analyse it. Can't analyse it? Document why."** — Task 401's fallback hierarchy (analysis → analogy → laboratory test → mockup → simulation) means there is always an alternative to live testing; the only unacceptable path is leaving a safety requirement unverified without documented rationale.
- **"EOD data is a life safety deliverable"** — Task 403 data is used by EOD personnel in emergency situations; the quality and accuracy of render-safe procedures and disposal guidance directly affects the safety of explosive ordnance disposal personnel.

## Anti-patterns

- **Treating software "safety-specific testing" as identical to functional testing**: LOR tasks for SwCI 1–3 require "in-depth safety-specific testing" — this means fault injection, boundary testing, out-of-bounds testing, failure modes and effects testing, and interface failure testing, not just nominal functional testing.
- **Scheduling safety verification after T&E rather than within it**: Task 401 is explicit that safety tests be "integrated into appropriate system T&E plans"; a safety verification programme that runs after the test phase is not compliant and may miss the window where design changes are still feasible.
- **Assuming inherited COTS/NDI safety verification**: verification of COTS, GOTS, NDI, and GFE components for safety requirements in the specific system context is the contractor's responsibility; supplier test data for the original application does not automatically satisfy verification for the new system context.

## Key Takeaways

1. Task 401 applies to safety-significant hardware, software, AND procedures — procedure compliance with safety requirements is a verifiable and contractually required output.
2. Induced and simulated failure testing is a required consideration for safety-significant items, not an optional enhancement.
3. When live testing is not feasible, a documented verification alternative (analysis, analogy, mockup, or simulation) is required — unverified safety requirements are not compliant.
4. Tasks 402 and 403 are specialised domain tasks for explosive and ordnance programmes; they are distinct from the general safety verification task and address specific regulatory compliance and operational safety data requirements.
5. Safety verification results must be submitted in a formal report containing test procedures, analysis methods used, T&E reports, and a summary of results.
6. All verification results feed the HTS and form the evidentiary basis for the SAR/HMAR assessment reports that support formal risk acceptance decisions.

## Connects To

- **Chapter 2 (System Safety Process)**: Task 401 implements Element 6 (Verify, Validate, and Document Risk Reduction) of the 8-element process.
- **Chapter 4 (Software Safety)**: LOR tasks specified in Table V (SwCI 1–4) define minimum software verification requirements; Task 401 is the contractual vehicle for performing these tasks.
- **Chapter 7 (Task 300 Evaluation)**: Task 303 (T&E Participation) and Task 401 overlap in test events; Task 401 provides the formal verification report that Task 301 (SAR) references.
- **DAEHCP references (Army TB 700-2, NAVSEA Instruction 8020.8, AF TO 11A-1-47, DLA Reg 8220.1)**: the specific documents that govern explosives hazard classification procedure compliance under Task 402.
