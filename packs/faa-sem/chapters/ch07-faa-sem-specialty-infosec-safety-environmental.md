# Chapter — Specialty Engineering II: Information Security, System Safety, and Hazardous Materials and Environmental Engineering

> Scope note: This chapter is a civil-agency SE process companion drawn from the FAA Systems Engineering Manual, Sections 5.5–5.7. It shows how the FAA threads three specialty disciplines through its Acquisition Management System (AMS), leaning heavily on the NIST 800-series, FIPS standards, and FAA's own Safety Management System rather than reinventing them. Read it alongside the broader NASA/DAU SE canon, not as a replacement for it.

## Core Idea

The FAA treats Information Security Engineering (ISE), System Safety Engineering (SSE), and Hazardous Materials Management / Environmental Engineering (HMM/EE with EOSH) as three distinct specialty disciplines that share one organizing conviction: each runs its own closed-loop risk-management cycle that begins at the earliest acquisition phase and feeds the mainstream SE processes. All three are framed as cheaper and more effective when started during concept and requirements work and far costlier when bolted on after fielding. ISE manages risk to the confidentiality, integrity, and availability of a system's IT assets; SSE manages risk of harm to people, property, equipment, and the environment from system hazards; and HMM/EE manages the two-way relationship between a program and its environment, including regulatory compliance, occupational safety, and sustainability across the whole lifecycle through disposal.

Critically, the manual positions each discipline as conducting risk management *separately from* — yet *in support of* — the program's central Risk Management process. ISE and SSE each run their own risk loop and then hand outputs (requirements, vulnerability assessments, hazard mitigations) back to Requirements Management, Functional Analysis, Synthesis, and Risk Management. The specialty work is not a parallel silo; it is an upstream feeder whose products become integral to the system's SE artifacts.

## Frameworks Introduced

Listed with the exact names the source uses and the role each plays.

**Information Security Engineering (5.5)**
- **Clinger-Cohen Act of 1996, FISMA (2002), FISAA (2012)** — the federal legislative basis cited for managing information security risk on federal IT resources.
- **Federal Information Processing Standards (FIPS)** — mandatory standards issued by NIST under FISMA; no longer waivable once FISMA passed. Two are named as defining the agency's security risk management process: **FIPS 199** (security categorization of federal information and systems) and **FIPS 200** (minimum security requirements).
- **FAA Order 1370.82A, Information Systems Security Program** — how the FAA implements FISMA; establishes the Security Authorization process and the governance roles around it.
- **NIST Risk Management Framework (RMF)**, drawn from **NIST SP 800-37** — the six-step lifecycle the FAA folds into its own Risk Management model: Categorize, Select, Implement, Assess, Authorize, Monitor.
- **Supporting NIST Special Publications**, each introduced for a specific role: **SP 800-39** (organization/mission/system risk view), **SP 800-37** (applying the RMF), **SP 800-53** and **SP 800-53A** (recommended controls and assessing them), **SP 800-27 Rev. A** (the 33 IT security principles mapped against lifecycle phases), **SP 800-30** (risk assessment, cited for POA&M remediation-vs-acceptance judgments), **SP 800-34 Rev. 1** (contingency planning and ISCP testing), **SP 800-137** (Information System Continuous Monitoring, ISCM), and **SP 800-55** (performance measurement / security metrics).
- **Authorization document set** — the products that flow through the FAA security-authorization process: System Characterization Document (SCD), Privacy Threshold Analysis (PTA) and Privacy Impact Analysis (PIA), System Security Plan (SSP), Information System Contingency Plan (ISCP) plus its test plan and results, Security Control Assessment (SCA) and Security Assessment Report (SAR), Risk Assessment Report (RAR), Plan of Action and Milestones (POA&M), and the Executive Summary or Annual Security Status Report (ASSR).
- **Information System Security Plan (ISSP)** — the FAA's evolving lifecycle ISE output product, initiated during shortfall analysis and updated as the system develops.
- Supporting authorities and tools named: **FAA Order 1280.1B** (protecting PII), **OMB Circular A-130**, **OMB Memorandum M-02-01** (POA&M requirement), the **E-Government Act of 2002**, the annual **Information Systems Security Authorization Handbook** (separate NAS and non-NAS versions), and the **Cyber Security Assessment and Management (CSAM)** tool of record.

**System Safety Engineering (5.6)**
- **FAA Safety Management System (SMS) Manual** — the integrated body of principles, policies, and processes for identifying and monitoring safety risk in Air Traffic Management and Communication/Navigation/Surveillance services.
- **Safety Risk Management Guidance for System Acquisitions (SRMGSA)** — the required guide for applying Safety Risk Management to NAS-affecting acquisitions across the AMS phases.
- **FAA Order 8040.4** — directs all FAA organizations to use safety risk management in decision making; the SMS Manual gives the method for complying.
- **Safety Risk Management (SRM) five-phase loop** — (1) describe the system; (2) identify its hazards; (3) analyze each risk; (4) assess that risk; (5) treat — i.e., mitigate — it.
- **Safety analysis product set** named by the manual, including the Operational Safety Assessment (OSA), Comparative Safety Assessment (CSA), Preliminary Hazard Analysis (PHA), Hazard Analysis Worksheet (HAW), Subsystem Hazard Analysis (SSHA), System Hazard Analysis (SHA), Operating and Support Hazard Analysis (O&SHA), System Safety Assessment Report (SSAR), Safety Risk Management Tracking System (SRMTS), and Safety Requirements Verification Table (SRVT).
- **Program Safety Plan (PSP)** and **System Safety Program Plan (SSPP)** — the government program plan and the vendor/contractor plan, respectively; the analysis is documented in a **Safety Risk Management Document (SRMD)**.

**Hazardous Materials Management / Environmental Engineering and EOSH (5.7)**
- **EOSH (Environmental, Occupational Safety and Health) requirements integration** — the SE process ensuring ongoing compliance with environmental, occupational-safety, and sustainability (energy/water) mandates.
- **AMS policy and guidance hooks** — Policy Section 3.6.3, Guidance Section T3.6.3, and Policy Section 4.8 — that require EOSH and sustainability consideration in acquisitions.
- **Governing FAA Orders** named: 1050.10C (pollution prevention/control at FAA facilities), 1050.1E / 1050.1 (environmental impacts policies and procedures), 1050.17 (Airway Facilities Environmental and Safety Compliance Program), 3900.19B (FAA Occupational Safety and Health Program), and 4600.27B (Personal Property Management).
- **Regulatory statutes** introduced as compliance drivers: the Clean Air Act (CAA, including NESHAP), Clean Water Act (CWA, including NPDES), National Environmental Policy Act (NEPA), the Resource Conservation and Recovery Act (RCRA), and OSHA requirements; plus sustainability authorities (Energy Policy Act of 2005, Energy Independence and Security Act of 2007, Executive Orders 13423 and 13514, and the federal Guiding Principles for sustainable, high-performance buildings).
- **FAA specifications and tools** — the general electronic-equipment spec **FAA-G-2100** (design standards for seismic and temperature extremes), the FAA Acquisition System Toolset (FAST), EPA's Significant New Alternatives Policy (SNAP) program, and each region's Environmental Compliance Plan (ECP) covering 19 environmental areas.

## Key Concepts

**Three-tiered risk management.** ISE frames information-security risk as a holistic, whole-organization activity addressed at three levels: the organization, the mission/business process, and the individual information system. Risk management is meant to be integrated into every part of the organization, not delegated to a security team alone.

**Security categorization drives controls.** Under FIPS 199/200, a system is categorized by impact (low, moderate, high), and that categorization selects the baseline of controls. Controls are then tailored, supplemented, and assigned as system-specific, common (inherited), or hybrid. Common controls are favored because they cost less and allow shared monitoring across many systems.

**The Security Authorization process and residual risk.** Every system must be risk-assessed per FIPS 199/200 before it goes operational. The Authorizing Official accepts any residual risk, which the agency tracks and works down through POA&Ms. Systems are reassessed at least annually, fully reauthorized every three years, and immediately reevaluated after any significant change. An Information Systems Security Manager (ISSM) runs the independent assessment and prepares recommendations for the Authorizing Official.

**The 33 IT security principles (NIST SP 800-27 Rev. A).** The manual maps these principles against AMS lifecycle phases, marking which principles merely support a phase versus which are key to it. They are grouped into themes — security foundation, risk-based, ease of use, increasing resilience, and designing with the network in mind — and include layered security, least privilege, isolating public-access systems from mission-critical resources, minimizing trusted elements, and not implementing unnecessary security mechanisms.

**Continuous monitoring and ongoing authorization (ISCM).** Per SP 800-137, continuous monitoring maintains ongoing awareness of security state at a frequency sufficient for risk-based decisions. Its aim is *ongoing* authorization: if the Authorizing Official has enough current knowledge of security state, formal reauthorization may be unnecessary. A three-year assessment cycle assesses core controls every year and the remaining controls at least once across the three years, all tracked on the FAA Three-Year Assessment Cycle Tracking Form.

**Contingency planning by impact level.** SP 800-34 Rev. 1 distinguishes the Information System Contingency Plan (recovery at original or alternate location) from the broader Disaster Recovery Plan (relocation after major long-term disruption, which activates one or more ISCPs). Testing scales with impact: tabletop exercises suffice for low-impact systems, functional exercises with recovery-from-backup for moderate, and full-scale failover-to-alternate-location exercises for high-impact systems. OMB requires testing at least annually.

**Hazard as the unit of safety work.** SSE defines a hazard as any condition, actual or potential, capable of causing injury, illness, or death; of damaging or destroying a system, equipment, or property; or of harming the environment. The goal is to find the highest-risk hazards and their causes early and control that risk before harm occurs. Risk is characterized by severity and likelihood.

**EOSH's two-directional and cradle-to-grave framing.** HMM/EE addresses both the program's impact on the environment and the environment's impact on the program (site-specific conditions like seismic zones or temperature extremes that affect operability). Compliance spans the whole lifecycle: requirements identification up front, SOW and system-spec shaping during implementation, field-change and regulatory-change analysis in service, and compliant decommissioning and disposal at end of life. FAA is described as carrying "cradle to grave" liability for hazardous wastes under RCRA, making a hazardous-materials inventory of fielded equipment a required HMM/EE product.

## Mental Models

**Three closed loops feeding one mainstream Risk Management process.** Each discipline is a self-contained closed-loop risk cycle (ISE's assess-mitigate-monitor-control loop, SSE's five-phase SRM loop, HMM/EE's lifecycle compliance loop) that runs alongside but separate from the program's central Risk Management element — and then pours its outputs back in. The mental picture is tributaries, not silos: independent currents that all empty into the same river.

**Early-involvement cost curve.** All three sections share one figure-backed argument: the earlier in the AMS lifecycle a security, safety, or environmental issue is found and managed, the cheaper and easier it is to correct. Participating during Investment Analysis lets ISE avoid expensive specialized controls when existing system features (management procedures, boundary protection) would do; SSE reduces safety and programmatic risk before the baseline is set; HMM/EE folds compliance costs into the acquisition program baseline rather than paying for retrofits or fines later.

**The "delta is a POA&M" model.** In ISE, any gap between what the Final Program Requirements document specifies and the standard System Security Plan template represents a requirement that was added, missed, removed, or over-modified — and that delta surfaces later as residual risk and a POA&M item. The mental model: unreconciled differences between your requirements and the agency's expected control set do not disappear; they convert into tracked risk debt.

**Categorize-then-tailor.** Rather than designing controls from scratch, the FAA model starts from a categorization-driven baseline and then tailors down or supplements up. The engineer's job is to justify the deviations from baseline (scoping, parameterization, compensating controls) with documented rationale, not to author controls independently.

**Living documents on a maintenance cadence.** The Security Plan, the System Characterization Document, and the regional Environmental Compliance Plan are all framed as living artifacts started early and revised continuously as design decisions are made and conditions change — security and environmental documentation is treated as something maintained on a cadence, not produced once and shelved.

## Anti-patterns

The source names these failure modes directly.

- **Adding security controls late in the AMS lifecycle.** The manual states that programs which include security requirements early in development typically have lower costs and more effective security than those that add controls later.
- **Treating security as a standalone component.** The ISE outputs section explicitly urges teams to build security into the program's own products wherever they can, so that it is not handled as a bolted-on "standalone" component.
- **Implementing unnecessary security mechanisms.** Principle 27 of the NIST 800-27 set, carried into the manual, names this directly as something to avoid.
- **Custom solutions that conflict with mandated common/hybrid controls.** The manual warns that a custom design conflicting with an FAA-mandated common or hybrid control can cause delays, added cost, the need for a policy waiver, and a POA&M.
- **Failing to incorporate HMM/EE and EOSH principles.** Noncompliant programs are named as risking equipment removal through regulatory enforcement, costly post-fielding retrofit modifications, and fines for noncompliance — with associated budgeting shocks if EOSH and disposal costs were not considered during development.

## Key Takeaways

- Three specialty disciplines — ISE, SSE, and HMM/EE/EOSH — each run an independent closed-loop risk process that starts early in the AMS and feeds outputs back into the mainstream SE and Risk Management elements; they support Risk Management without being absorbed into it.
- ISE is anchored in federal law (Clinger-Cohen, FISMA, FISAA), mandatory FIPS 199/200 categorization, FAA Order 1370.82A's Security Authorization process, and the NIST RMF six steps, with a deep bench of supporting NIST SPs (800-39/37/53/53A/27/30/34/137/55).
- Authorization is a continuing obligation, not a one-time gate: annual reassessment, three-year reauthorization, immediate reevaluation on significant change, residual-risk acceptance by the Authorizing Official, POA&M tracking, and ISCM aiming at ongoing authorization.
- SSE optimizes system safety by identifying, evaluating, and controlling hazards through the SMS Manual and SRMGSA, executing a five-phase SRM loop and producing a defined ladder of hazard analyses (OSA, CSA, PHA, SSHA, SHA, O&SHA) culminating in the SSAR.
- HMM/EE/EOSH manages compliance bidirectionally and cradle-to-grave across CAA, CWA, NEPA, RCRA, OSHA, and sustainability mandates, folding full compliance and disposal costs into the acquisition program baseline and producing a hazardous-materials inventory of fielded equipment.
- The unifying lesson across all three: early, integrated involvement lowers cost and risk; late, bolt-on treatment converts into residual risk, POA&Ms, retrofits, enforcement actions, and fines.

## Connects To

- **NIST 800-series and the RMF.** This chapter is the FAA's civil-agency application of the same NIST Risk Management Framework and SP 800-37/53/137 machinery covered in dedicated NIST packs; the FAA layers its AMS phases, Authorization Handbook, and document set on top of the federal standard rather than replacing it.
- **Prior FAA-SEM specialty chapters.** Continues the Specialty Engineering thread (Section 5) — the General Specialty Engineering Process Tasks are reused here, with SSE's tasks explicitly correlated to them, tying these disciplines back to the manual's common specialty-engineering scaffold.
- **The mainstream SE process elements.** ISE, SSE, and HMM/EE all feed and are fed by Requirements Management, Functional Analysis, Synthesis, Interface Management, Configuration Management, Verification, and Risk Management — the same core processes treated elsewhere in the FAA SEM.
- **NASA/DAU SE canon (caveat).** As a civil-agency process companion, this material complements but does not substitute for the broader systems-safety, security-engineering (e.g., NIST SP 800-160), and environmental-engineering treatments in the NASA and DAU bodies of knowledge; use those for discipline depth and this for how a civil aviation agency operationalizes them inside an acquisition system.
