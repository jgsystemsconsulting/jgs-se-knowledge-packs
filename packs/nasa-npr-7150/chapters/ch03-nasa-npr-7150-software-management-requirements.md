# Chapter — Software Management Requirements

> Source caveat: This chapter is synthesized from NASA Procedural Requirements (NPR) 7150.2D, Chapter 3, a NASA Procedural Requirement issued through the NASA Online Directives Information System (NODIS) and rendered here from the NODIS HTML. It is a software-engineering requirements directive that complements the broader software-for-systems area: it governs how NASA project managers plan, classify, cost, secure, and assure flight and ground software across the life cycle. Requirement identifiers in brackets (e.g., [SWE-013]) are the directive's own "shall" statement tags. All claims below are grounded in the Chapter 3 text; nothing is copied verbatim in runs longer than a short phrase.

## Core Idea

Chapter 3 is the management spine of NPR 7150.2D. Where engineering chapters specify *how* to build software, this chapter binds the **project manager** to a set of "shall" obligations that govern the *management* of software as a whole — from inception through retirement and decommissioning. The unifying premise is that software is not an afterthought bolted onto a system but a coordinated effort that must be scoped, planned, classified, costed, scheduled, assured, secured, and traced as a first-class engineering discipline within the project.

Every major activity is gated by a single mechanism: a project's **software classification** (Classes A through F), combined with the **Requirements Mapping Matrix**, determines exactly which of the chapter's requirements actually apply to a given system or subsystem. This makes Chapter 3 fundamentally a *tailoring-and-applicability* engine — the same directive lands very differently on a human-rated flight system (Class A) than on a one-off analysis script (Class E/F).

## Frameworks Introduced

The chapter names several external frameworks, standards, and instruments and specifies when and how each is invoked:

- **Software classification (Classes A–F), via Appendix D** — The project manager classifies each system and subsystem containing software at the highest applicable class [SWE-020]. The class definitions rest on five factors named in the text: how the software is used with or within a NASA system, the criticality of that system to NASA's major programs, the degree of human dependence on it, developmental and operational complexity, and the size of the Agency's investment. Classification is the master switch that turns other requirements on or off.

- **Requirements Mapping Matrix (RMM), via Appendix C** — Each project with software maintains one or more RMMs that map this NPR's requirements (including those delegated by contract or Space Act Agreement) against the project [SWE-125]. Requirements marked with an "X" in Appendix C for a given class are mandatory [SWE-139]; relief from an "X" requirement is granted only by the designated Technical Authorities (Engineering and SMA), or by the NASA CIO for security matters, with the approval recorded by authority signature in the RMM. The CIO holds institutional authority over all Class F projects.

- **NASA-HDBK-2203 (NASA Software Engineering Handbook)** — Cited repeatedly as the source of recommended practices and content guidance for planning documents [SWE-013], for cyclomatic-complexity guidance, and for locating Agency software reuse repositories. It is guidance, not a binding requirement, but it is the directive's primary "how-to" companion.

- **NASA-STD-8739.8 (Software Assurance and Software Safety Standard)** — The binding standard for planning and implementing software assurance, software safety, and IV&V [SWE-022]; it also defines the criteria for determining whether a component is safety-critical [SWE-205] and carries the safety-critical software requirements themselves [SWE-023].

- **CMMI® (Capability Maturity Model Integration), CMMI®-DEV model** — Used as the industry-accepted yardstick for whether a development organization has the skills, practices, and processes to deliver reliably within cost and schedule. The directive requires a non-expired CMMI®-DEV rating, appraised by a CMMI® Institute Certified Lead Appraiser: Maturity Level 3 or higher for Class A software, Level 2 or higher for Class B [SWE-032], against model version 1.3 or 2.0, with a defined exception path for a "best-in-class" Class B provider that lacks the rating.

- **IV&V framework: NASA IV&V, the IPEP, and the IV&V Advisory Board** — For projects reaching Key Decision Point A, the program manager ensures software IV&V on Category 1 projects (per NPR 7120.5), on Category 2 projects with Class A/B payload risk (per NPR 8705.4), and on projects selected by the Mission Directorate Associate Administrator [SWE-141]. When IV&V applies, an IV&V Project Execution Plan (IPEP) is developed and executed [SWE-131], and the IV&V team is granted access to artifacts in original electronic (non-PDF) format [SWE-178].

- **MC/DC (Modified Condition/Decision Coverage)** — The mandated test-coverage criterion for safety-critical components: 100 percent coverage is required [SWE-219], meaning each condition in a decision is exercised independently for both true and false outcomes while holding the other conditions fixed, demonstrating that each condition independently affects the decision.

- **Cybersecurity and protection standards** — NASA-STD-1006 (Space System Protection Standard) governs protection of software systems with communications capabilities against unauthorized access [SWE-157]; Project Protection Plans, framed by NPR 1600.1 / NPD 1600.2 / NPD 2810.1 / NPR 2810.1, describe the security planning approach.

- **Cost-model and reporting instruments** — The directive requires established, documented, maintained software cost-estimate models with associated parameters [SWE-015], with the *number* of models keyed to class and dollar threshold (notably two models for Class A/B projects estimated at $2 million or more). Planning parameters feed the **Center measurement repository** at major milestones [SWE-174].

- **Acquisition-type taxonomy: COTS, GOTS, MOTS, OSS, reused, and auto-generated code** — Off-the-shelf and reused components carry their own acceptance conditions [SWE-027], and are explicitly in scope for cybersecurity assessment [SWE-156].

## Key Concepts

**Software life cycle planning as an organizing process.** Section 3.1 frames planning as a coordinating activity spanning acquisition, supply, development, operation, maintenance, retirement, and decommissioning. The project manager must first assess buy-versus-build options — off-the-shelf acquisition, internal development, contracted development, enhancement of an existing product, reuse, or external source code [SWE-033] — then develop and execute software plans (including security plans) across the full life cycle with approved tailoring [SWE-013].

**Plan-to-actuals control loop.** Planning is not a one-time artifact. The project manager tracks actual software performance against the plans [SWE-024], drives corrective actions to closure, and manages agreed changes to commitments. Acceptance criteria for the software are defined and documented up front [SWE-034].

**Insight and electronic access.** A recurring theme is NASA's right to *see into* developer work. Developers periodically report status and grant the project manager and software assurance personnel the ability to monitor integration, review verification adequacy, examine trade studies, audit processes, and join technical interchange meetings [SWE-039]. Beyond reports, NASA requires electronic delivery of products, traceability, change-tracking, and metrics [SWE-040], plus electronic access to source code in modifiable format [SWE-042] — explicitly extending to MOTS, ground, simulation, analysis, control, science-data-processing, and Class E/F software.

**Off-the-shelf and reused-component discipline.** When a COTS, GOTS, MOTS, OSS, or reused component is used, the project must identify the requirements it meets, ensure adequate documentation, resolve proprietary/license/ownership matters with Center Intellectual Property Counsel, plan for future support, verify and validate the component to the *same level* as an equivalent developed component, and periodically assess vendor-reported defects [SWE-027].

**Cost estimation scaled to risk.** Estimates cover the entire life cycle and rest on project attributes — size, functionality, complexity, criticality, reuse and modified code, and process/product risk — plus technology maturity, cybersecurity end-state and threat assessments, software assurance cost, and other direct costs [SWE-151]. For significant risk exposure, performing at least two estimates is the recommended posture.

**Scheduling and training as managed commitments.** The software schedule coordinates with the overall project schedule, documents cross-discipline milestone interactions, and captures critical and cross-program dependencies [SWE-016], with regular stakeholder reviews tracking issues to resolution [SWE-018]. Project-specific software training is planned, tracked, and ensured for project personnel, including assigned software assurance staff [SWE-017].

**Safety-critical software behaviors.** Section 3.7 enumerates concrete behavioral requirements for safety- or mission-critical software [SWE-134]: initialize to a known safe state at start and restart; transition safely between predefined states; terminate to a safe state; require two independent operator actions for overrides; reject hazardous out-of-sequence commands; detect inadvertent memory modification and recover; perform input/output integrity checks; run prerequisite checks before safety-critical commands; ensure no single event initiates a hazard; respond to off-nominal conditions within the time needed to prevent harm; provide error handling; and be able to place the system in a safe state. These are reinforced by the 100% MC/DC coverage rule [SWE-219] and a cyclomatic-complexity ceiling of 15 for safety-critical components, with exceedances reviewed and waived with rationale [SWE-220].

**Auto-generated code held to the same bar.** When source code is auto-generated, the project defines its approach including tool V&V, configuration management of tools and data, scope limits, V&V of generated code under the same standards as hand-written code, monitoring of actual versus planned use, manual-change policy, and CM of inputs and outputs [SWE-146]. NASA also gets electronic access to the models, simulations, and input data driving generation [SWE-206].

**Cybersecurity woven through development.** Software defects are framed as a central source of security vulnerabilities (implementation bugs like buffer overflows, design flaws like inconsistent error handling). The project performs cybersecurity assessments including risks from off-the-shelf and reused components [SWE-156], identifies and plans mitigations for flight and ground systems [SWE-154], tests and records results for mitigation implementations [SWE-159], identifies and implements secure coding practices [SWE-207], verifies code against the secure coding standard using static analysis results [SWE-185], and identifies requirements for collecting and reporting data on adversarial-action detection [SWE-210].

**Bi-directional traceability by class.** Section 3.12 mandates traceability that runs both directions across the software element chain — higher-level requirements to software requirements, requirements to system hazards, requirements to design components, design components to code, requirements to verifications, and requirements to non-conformances [SWE-052] — with a class-keyed table (Table 1) specifying which links are required for Class A/B/C, Class D, and Class F. Hazard traceability explicitly spans hazardous controls, mitigations, conditions, and events.

## Mental Models

**Classification as the master valve.** Think of software class as the dial that sets how much of the directive flows onto a project. Set the class first (Appendix D), and the Requirements Mapping Matrix (Appendix C) then reads off which "X"-marked requirements are live. Almost every other obligation — cost-model count, CMMI level, traceability links, IV&V applicability — is downstream of this single dial.

**The RMM as a signed contract of applicability.** The Requirements Mapping Matrix is the artifact where applicability, tailoring, relief, mitigations, and risk acceptance all converge and are signed by the proper authority. If a requirement was relieved, the *why* lives in the RMM; if it applies, the RMM proves it. It is the auditable record that ties classification to obligation.

**"Same level as developed" as an anti-shortcut clamp.** Whenever software is acquired, reused, or auto-generated rather than freshly written, the directive repeatedly clamps it back to the standard a developed component would face — V&V to the same level, the same software standards and processes. The mental model: changing the *source* of code never lowers the *bar* for it.

**Insight as a continuous right, not a milestone gate.** NASA's visibility into developer work is modeled as ongoing access — monitoring, auditing, electronic copies, modifiable source — rather than a deliverable handed over once. The acquirer can always look inside.

**Defense in depth for safety and security.** Safety-critical behavior is layered (safe states, independent operator actions, integrity and prerequisite checks, single-event hazard prevention) and reinforced with quantitative gates (100% MC/DC, complexity ≤ 15). Cybersecurity is similarly layered across assessment, mitigation, testing, secure coding, static analysis, and adversarial-action monitoring. No single control is trusted alone.

## Anti-patterns

The source does not present a formal "anti-patterns" section. It does, however, explicitly name failure modes it intends to prevent, which can be read as anti-patterns:

- **Treating defects as merely quality issues rather than security issues.** The chapter explicitly identifies software defects as a central source of cybersecurity vulnerability, naming buffer overflows and inconsistent error handling as examples — a caution against ignoring the security weight of ordinary coding bugs.
- **Excessive complexity in safety-critical code.** The cyclomatic-complexity ceiling of 15 exists precisely to push back against high-complexity safety-critical components, whose extra independent paths raise testing burden and failure risk during hazardous events.
- **Self-testing of safety-critical code.** The directive recommends that someone independent of the code's developer design and run the safety-critical testing, so that misinterpreted requirements or incorrect assumptions do not slip through unchallenged.

## Key Takeaways

- Chapter 3 binds the **project manager** to manage software across its entire life cycle through enumerated "shall" requirements, each tagged with a [SWE-xxx] identifier.
- **Software classification (Appendix D)** plus the **Requirements Mapping Matrix (Appendix C)** together decide which requirements apply; relief is authority-signed and risk-documented in the RMM.
- Planning, cost estimation, scheduling, and training are all managed commitments with plan-to-actuals tracking and defined acceptance criteria.
- Acquired, reused, and auto-generated software must be verified and validated to the same level as developed software, with intellectual-property and support questions resolved up front.
- Development-organization maturity is enforced via **CMMI®-DEV** ratings keyed to class (Level 3 for Class A, Level 2 for Class B), with a defined best-in-class exception.
- Software assurance, safety, and IV&V flow through **NASA-STD-8739.8**; IV&V applicability is gated by project category, payload risk, and Mission Directorate selection.
- Safety-critical software carries concrete behavioral requirements plus hard quantitative gates: **100% MC/DC coverage** and **cyclomatic complexity ≤ 15**.
- Cybersecurity is treated as a development-through-operations concern: assessments, mitigations, secure coding, static analysis, and adversarial-action monitoring.
- **Bi-directional traceability** is required across the full requirements-to-code-to-verification chain, with the exact links scaled by class (Table 1).

## Connects To

- **The software-for-systems area within this pack and the wider SE landscape** — Chapter 3 is the software-management complement to systems-level engineering management; its classification, traceability, and assurance mechanics mirror the broader SE practices of requirements traceability, V&V, and risk-based tailoring.
- **NPR 7150.2D Appendices C and D** — The Requirements Mapping Matrix and the software class definitions are the two appendices that make this chapter operational; the chapter is effectively unusable without them.
- **NASA-HDBK-2203 (NASA Software Engineering Handbook)** — The practical companion that supplies planning-document content guidance, reuse-repository locations, and complexity guidance referenced throughout.
- **NASA-STD-8739.8** — Carries the software assurance, safety, safety-critical, and IV&V requirements that Chapter 3 invokes by reference.
- **NPR 7120.5 and NPR 8705.4** — Define the project categories and payload risk classes that gate IV&V applicability.
- **CMMI®-DEV** — The external maturity model used to qualify development organizations.
- **NASA-STD-1006 and the NPR 1600.1 / NPD 2810.1 / NPR 2810.1 security family** — The protection standards and Project Protection Plan framing that Chapter 3's cybersecurity requirements connect into.
