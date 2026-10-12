# Chapter 2: Premarket Software Documentation

Sources: S1 Content of Premarket Submissions for Device Software Functions (2023-06-14), §§ V–VI and Table 1 (Documentation Level Basic/Enhanced; recommended documentation elements A–J), Appendix A (level examples), Appendix B (architecture diagram examples).

## Core Idea

Once a product carries device software functions and a premarket path is chosen, S1 answers a different question: how deep must the software evidence in the file go, and which artifacts does FDA expect to see. The driver is **Documentation Level**, Basic or Enhanced, set for the device as a whole from pre-control risk of death or serious injury if any device software function fails or is flawed. The level is not a device class, not a module-by-module score, and not a leftover "level of concern" label from the superseded 2005 software-content guidance. After the level is fixed, Table 1 lists the same element set for both levels and deepens SDS, life-cycle practice evidence, and testing detail for Enhanced. Sponsors build that package from work that should already exist under design controls; retrospective construction after coding finishes is a control problem, not a documentation strategy.

## Frameworks Introduced

- **Documentation Level (Basic or Enhanced)**: minimum recommended depth of software content in the premarket submission. Enhanced applies when failure or flaw of any device software function could present a hazardous situation with a probable risk of death or serious injury (patient, user, or others), assessed **before** risk controls. Basic is everything else. Level reflects the device as a whole.
- **Table 1 element set (Sections VI.A–J)**: Documentation Level Evaluation; Software Description; Risk Management File; Software Requirements Specification (SRS); System and Software Architecture Diagram; Software Design Specification (SDS); Software Development, Configuration Management, and Maintenance Practices; Software Testing as Part of Verification and Validation; Software Version History; Unresolved Software Anomalies.
- **Basic vs Enhanced depth rule**: several elements are shared at both levels (level statement, description, risk file, SRS, architecture, version history, unresolved anomalies). Enhanced adds SDS in the submission, fuller configuration-management and maintenance plan evidence (or a broader IEC 62304 declaration of conformity), and unit/integration test protocols and reports on top of the Basic system-level testing package.
- **Category defaults toward Enhanced**: blood donation testing devices, donor/recipient compatibility devices, automated blood cell separators for transfusion or further manufacturing, and blood establishment computer software (BECS). Combination-product device constituents and Class III devices generally get Enhanced unless the sponsor justifies Basic with a detailed rationale.
- **Verification vs validation (S1 working definitions)**: verification confirms that outputs of a life-cycle phase meet that phase's requirements (reviews, inspections, architecture/design evaluations, traceability, testing). Validation is design validation for the finished device where software is in scope: objective evidence that software specifications meet user needs and intended uses and that implemented requirements can be fulfilled consistently. S1 points sponsors to the GPSV guidance (this pack's ch03) for development, verification, and validation practice detail.

## Key Concepts

- **What S1 covers and excludes.** S1 applies to device software functions in premarket submissions (510(k), De Novo, PMA, IDE, HDE, BLA when a device software function is under review). Manufacturing and quality-system software, and software that is not a device, sit outside this premarket documentation guidance. Multi-function products still need architecture and risk treatment that show how non-device functions can affect device functions.
- **How to set Documentation Level.** Consider all known or foreseeable software hazards and hazardous situations, including reasonably foreseeable misuse, **prior to** risk controls. Include the likelihood that functionality is compromised by inadequate cybersecurity. "Probable" excludes purely hypothetical risks. The sponsor owns a proactive risk assessment; FDA may still request more information during review.
- **Documentation Level Evaluation (VI.A).** Open the software package with a statement of Basic or Enhanced and a rationale tied to intended use and the rest of the software file (risk management, software description, and related elements).
- **Software Description (VI.B).** Overview of significant features, functions, analyses, inputs, outputs, and hardware platforms. Call out OTS and other third-party software where used. The description orients reviewers before they open architecture and requirements.
- **Risk Management File (VI.C).** Risk management plan, risk assessment showing hazards and hazardous situations have been appropriately mitigated, and risk management report. Trace risk controls into software requirements, design, architecture, and testing. S1 expects verification that controls were implemented and that they work. ISO 14971 is named as the risk-management reference; this pack does not reproduce ISO text.
- **Software Requirements Specification (VI.D).** Organized needs and expectations at system or subsystem level, with enough structure to support traceability to the risk file, SDS (when present), architecture, and testing. Each requirement should be identifiable for tracing.
- **System and Software Architecture Diagram (VI.E).** Roadmap of modules, layers, interfaces, relationships, data inputs/outputs and flow, and interactions with users or external products (including IT infrastructure and peripherals). Detail must match the complexity of the device. One or more static diagrams, dynamic/state views, and cybersecurity architecture views may be needed. For multi-function products, show device and non-device software functions and their interactions. Appendix B gives illustrative layouts, not mandatory drawing styles. OTS modeling languages are acceptable if the submitted views are readable without the tool.
- **Software Design Specification (VI.F).** Basic: SDS is not recommended as a premarket deliverable; keep it in the design history file, knowing FDA may still request it. Enhanced: submit SDS detail sufficient to show how the design implements the SRS and traces to intended use, functionality, safety, and effectiveness.
- **Development, configuration management, and maintenance practices (VI.G).** Basic: summary of the life-cycle development plan plus summary of configuration management and maintenance activities, **or** a declaration of conformity to the FDA-recognized IEC 62304 covering the cited planning, maintenance, and configuration-management clauses. Enhanced: Basic package **plus** complete configuration management and maintenance plan documents, **or** a declaration of conformity that also covers the broader IEC 62304 planning set S1 lists for Enhanced.
- **Software testing as part of V&V (VI.H).** Basic: summary of unit, integration, and system testing activities, **and** system-level test protocol (expected results, observed results, pass/fail) with system-level test report. Enhanced: Basic package **plus** unit and integration protocols and reports with the same expected/observed/pass-fail structure. Passing execution and acceptable handling of unresolved anomalies are part of the story.
- **Software Version History (VI.I).** History of tested versions: date, version number, brief description of changes relative to the previously tested version.
- **Unresolved Software Anomalies (VI.J).** Remaining anomalies with impact evaluation on safety and effectiveness, work-arounds where relevant, and alignment to the risk management plan. Annotate user communication when anomalies affect field use.
- **Traceability is cross-cutting.** S1 repeatedly ties SRS, risk controls, architecture, design, and tests together. Sponsors may present a separate traceability artifact; the point is navigable links, not a preferred matrix format.
- **OTS inside the device software package.** If the device uses OTS software, expect description and possible additional information requests; deeper OTS maintenance and obsolescence treatment lives with the OTS guidance (ch08).
- **Q-Sub for level disputes.** Sponsors may use a Pre-Submission to get FDA feedback on Documentation Level and planned documentation before the marketing file.
- **Guidances recommend; design controls bind.** S1 is nonbinding recommendations unless it cites statute or regulation. 21 CFR 820.30 design controls (including software validation and risk analysis where appropriate) still generate and retain the underlying records, including after the QMSR transition framed in ch01 and detailed in ch05.

## Mental Models

- **Harm before paperwork.** Ask how bad failure is before mitigations. That answer picks Basic or Enhanced. Class III and combination products often land on Enhanced, but the hazardous-situation test is the rule; class is a correlation, not the definition.
- **One level for the whole device.** Do not assign Basic to "the UI module" and Enhanced to "the closed-loop module." The highest relevant software-function risk sets the device-level documentation depth.
- **Submission slice vs design history.** Table 1 is what typically goes in the file. The DHF still holds the fuller design, coding, review, and change record. Basic does not mean "no SDS exists"; it means SDS usually stays in the DHF unless FDA asks.
- **Architecture is a map, not a decoration.** If a reviewer cannot see modules, trust boundaries, data flow, and external interfaces, the diagram failed its job regardless of drawing tool.
- **Testing depth follows level.** System-level evidence is the Basic floor. Unit and integration protocols and reports are the Enhanced add-on, not a substitute for system proof.
- **2005 "level of concern" is retired here.** S1 replaces the May 11, 2005 software-content guidance. This pack's working vocabulary for premarket software depth is Documentation Level (Basic/Enhanced), not Minor/Moderate/Major level of concern.

## Anti-patterns

- **Picking Basic because the schedule is tight.** Resource pressure is not a Documentation Level input. Pre-control severity of harm is.
- **Equating Basic with "no architecture or risk file."** Both levels carry description, risk management file, SRS, architecture, version history, and unresolved anomalies.
- **Module-level Documentation Levels.** Split ratings by component undercut the device-as-a-whole rule and confuse reviewers.
- **Architecture diagrams that hide OTS, cloud, or non-device functions.** Multi-function and connected products need those interfaces visible.
- **Enhanced without SDS or without unit/integration evidence.** The Enhanced column in Table 1 is additive; skipping SDS or lower-level test reports is an incomplete Enhanced package.
- **Building the DHF after freeze.** S1 warns that reconstructing design-history evidence long after development, verification, and validation raises control concerns.
- **Ignoring cybersecurity compromise when setting level.** Inadequate cybersecurity that can take away functionality is in scope for the pre-control Documentation Level assessment.
- **Treating IEC 62304 declaration as automatic full substitute without reading which clauses S1 lists for Basic vs Enhanced.** The declaration path is real; the cited clause sets differ by level.

## Key Takeaways

1. S1 Documentation Level is Basic or Enhanced, set for the device as a whole from pre-control probable death or serious injury risk of software failure or flaw (including cybersecurity compromise of function).
2. Blood-related categories named in S1, and generally combination-product constituents and Class III devices, default toward Enhanced; a Basic choice for the latter two needs a detailed rationale.
3. Table 1 elements A–J structure the package; Enhanced adds SDS in the file, deeper CM/maintenance evidence (or a broader 62304 DOC), and unit/integration test protocols and reports.
4. Architecture diagrams must show modules, layers, interfaces, data flow, and user/external interactions at a depth matching device complexity; multi-function products must show cross-function impact paths.
5. Risk management file, SRS, design, architecture, and tests should be traceable to each other; unresolved anomalies need safety and effectiveness impact evaluation.
6. Basic still expects system-level test protocols and reports plus a summary of lower-level testing activity; it is not a test-free path.
7. Manufacturing/QMS software is out of S1 scope (see CSA in ch04); device software validation practice detail sits in GPSV (ch03).
8. This chapter is the premarket software documentation package; pathway choice is ch01, eSTAR section homes are ch12, and cybersecurity submission assembly is ch09.

## Connects To

- **ch01**: pathway choice and the Documentation Level orientation that this chapter deepens.
- **ch03**: GPSV lifecycle validation and verification principles behind the V&V evidence S1 expects.
- **ch04**: CSA for production and quality-management system software (outside S1 device-software scope).
- **ch08**: OTS/SOUP and MDDS boundary detail when description and architecture call out third-party or non-device functions.
- **ch09**: cybersecurity documentation package assembled beside this software package.
- **ch10**: software changes after clearance and when a new 510(k) is needed.
- **ch12**: eSTAR Software/Firmware section as the authoring home for this package.
