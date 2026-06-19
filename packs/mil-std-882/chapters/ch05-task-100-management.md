# Chapter 5: Task Section 100 — Management Tasks

## Core Idea
The 100-series tasks establish the programmatic infrastructure for system safety: planning documents, tracking systems, progress reporting, government interface support, and hazardous materials management. These tasks are invoked selectively by contract; each must be explicitly called out by task number in the RFP and SOW. Management tasks span all programme phases and create the organisational spine through which analysis, evaluation, and verification results flow.

## Frameworks Introduced

- **Task 101 — Hazard Identification and Mitigation Effort Using the System Safety Methodology**: the integrating task that establishes and executes hazard ID/mitigation within SE; covers roles/responsibilities, flow-down to subcontractors, reporting at technical reviews, and HTS operation.
  - When to use: generally applicable across all programme phases; the foundational management task from which others derive.

- **Task 102 — System Safety Program Plan (SSPP)**: the primary planning document that describes the contractor's approach to system safety as an integral part of the SEMP. Required sections: scope/objectives, interfaces, organisation, milestones, general safety requirements, hazard analysis approach, supporting data, V&V methods, audit programme, training, and incident reporting.
  - When to use: any programme where a formal system safety plan is contractually required; the SSPP is the basis of understanding between contractor and PM.

- **Task 103 — Hazard Management Plan (HMP)**: structurally parallel to the SSPP but oriented toward programmes using the system safety methodology across multiple functional disciplines (not only system safety). Includes all SSPP sections plus explicit coverage of functional discipline interfaces.
  - When to use: programmes where multiple SE functional disciplines (fire protection, environmental, occupational health, software safety) apply MIL-STD-882E methodology; the HMP provides cross-discipline coordination.

- **Task 104 — Support of Government Reviews/Audits**: contractor support for programme technical reviews, munitions safety boards, laser safety boards, nuclear safety boards, flight readiness reviews, NEPA hearings, and mishap investigations.
  - When to use: whenever Government-led reviews with a safety component are scheduled.

- **Task 105 — Integrated Product Team/Working Group Support**: active participation in designated IPTs and WGs; includes summarising hazard analyses, presenting incident assessments, responding to action items, and requiring key subcontractors to participate.
  - When to use: programmes with defined IPT/WG structures; ensures safety voice is present in cross-functional decision meetings.

- **Task 106 — Hazard Tracking System (HTS)**: establishes and maintains the closed-loop HTS with defined minimum data elements.
  - When to use: mandatory infrastructure for any programme using MIL-STD-882E; feeds data to all other tasks.

- **Task 107 — Hazard Management Progress Report**: periodic progress reports summarising hazard management activities, newly recognised hazards, mitigation implementation status, and cost/schedule/performance impacts.
  - When to use: whenever periodic programme reporting on safety status is contractually required.

- **Task 108 — Hazardous Materials Management Plan (HMMP)**: implements HAZMAT identification, categorisation (prohibited/restricted/tracked), data tracking, and reporting procedures.
  - When to use: whenever the system design or support operations involve materials with hazard potential; should be imposed as early in the programme life-cycle as possible.

## Key Concepts

- **SSPP vs. HMP**: both are programme safety planning documents, but the SSPP is system-safety-discipline-centric while the HMP explicitly coordinates multiple functional disciplines using MIL-STD-882E methodology. Many programmes need only one; the choice depends on programme structure.
- **SSPP as SEMP annex**: the standard states the SSPP should be an integral part of the Systems Engineering Management Plan (SEMP); system safety is a SE function, not a separate programme.
- **HTS minimum data elements (Task 106)**: hazard, system, subsystem, applicability (version-specific), requirements references, system mode, causal factor, effects, mishap, initial RAC, target RAC, event RAC(s), mitigation measures (identified and selected with version traceability), hazard status, V&V method, action person(s) and org element, record of risk acceptance(s) (authority title/org, date, location of signed document), hazard management log, HAZMAT data elements.
- **HAZMAT categorisation**: prohibited (Government approval required before inclusion), restricted (targeted for elimination or minimisation), tracked (tracking and reporting only).
- **Government purpose rights over HTS data**: mandatory per 4.3.1.d; the Government retains all rights to HTS data and associated studies, analyses, test data generated under the contract.
- **Flow-down requirement**: Task 101 explicitly requires flow-down of system safety requirements and methodology to all subcontractors, associate contractors, vendors, and suppliers.

## Mental Models

- **"SSPP is the contract"** for how safety will be done — before any analysis tasks start, the SSPP establishes the rules, personnel, tools, and criteria that all subsequent work must follow.
- **"HTS is the audit trail"** — every risk acceptance, every mitigation selection, every verification result must be recorded; in a mishap investigation, the HTS is the primary documentary evidence of the programme's hazard management performance.
- **"Technical reviews are hazard gates"** — Task 101 requires presentation of hazard status at SRR, PDR, CDR, TRR, and PRR; these are the contractual moments when hazard risk data must be visible to programme leadership.

## Anti-patterns

- **Treating the SSPP as a document deliverable rather than a living plan**: the SSPP must describe the process that is actually being executed; a template-filled document that does not reflect reality is non-compliant and creates liability at mishap investigations.
- **Maintaining the HTS only at the prime contractor level**: Tasks 101 and 106 require subcontractor hazard tracking data to be integrated into the prime HTS; isolated subcontractor tracking systems without integration are non-compliant.

## Key Takeaways

1. All 100-series tasks must be individually and explicitly invoked in the contract — invoking the standard without specifying tasks imposes only Sections 3 and 4.
2. Task 102 (SSPP) and Task 103 (HMP) are alternatives for the primary planning document; the choice depends on whether a single safety discipline or multiple disciplines are employing the methodology.
3. The HTS minimum data fields (Task 106) are the contractual baseline; programmes may add but not subtract data elements without formal approval.
4. HAZMAT must be categorised as prohibited, restricted, or tracked — the three-tier system drives different contractor obligations for each category.
5. The SSPP must include a risk acceptance communication plan: how the contractor will notify the Government, and how the Government will communicate acceptance decisions back to the contractor.
6. Task 108 (HMMP) should be imposed as early in the programme life-cycle as possible because early HAZMAT identification has the highest leverage on design decisions.

## Connects To

- **Chapter 2 (System Safety Process)**: the 100-series tasks implement Element 1 (document the approach) and Element 8 (manage life-cycle risk).
- **Chapter 6 (Task 200 — Analysis)**: all analysis tasks feed results into the HTS established under Task 106.
- **Chapter 7 (Task 300 — Evaluation)**: SAR (301) and HMAR (302) draw on HTS data accumulated under Task 106 management.
- **DoDI 5000 series**: defines the specific risk acceptance authorities that Tasks 101, 102, and 103 must reference in their risk acceptance communication plans.
