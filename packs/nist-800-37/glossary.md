# NIST SP 800-37 Rev. 2 (RMF) Glossary

Key terms from the Risk Management Framework, alphabetical, with the chapter that
develops each. Definitions are paraphrased from SP 800-37 Rev. 2 — consult the source
(and SP 800-53, SP 800-39, FIPS 199/200) for the controlling text.

| Term | Meaning (paraphrased) | Chapter |
|---|---|---|
| **Assess (step)** | The RMF step that determines whether controls were built correctly, run as designed, and yield the outcome the requirements demand. Six tasks A-1…A-6. | ch05 |
| **Assessment report** | The assessor's documented findings and recommendations; a living artifact that feeds the authorization package. | ch05 |
| **Assurance** | Grounds for justified confidence that a control is correct, operates as intended, and is effective — the quality dimension of design and build, not just its function. | ch05, ch03 |
| **Authorization boundary** | The set of system elements (people, processes, technologies) — or the set of common controls — that an authorizing official has authorized for operation or inheritance. Replaces the older term "system boundary." | ch02, ch03 |
| **Authorization package** | The evidence bundle (plans, assessment reports, POA&M, executive summary) submitted to the authorizing official for the risk decision. | ch06 |
| **Authorize (step)** | The RMF step where a senior official accepts (or refuses) residual risk on behalf of the organization. Five tasks R-1…R-5. The one step that cannot be done by an external provider. | ch06 |
| **Authorizing official (AO)** | The senior leader with the authority to commit the organization who personally accepts residual risk; the role cannot delegate that acceptance. | ch06 |
| **Categorize (step)** | The RMF step that fixes a system's impact level from the consequences of losing confidentiality, integrity, or availability. Tasks C-1…C-3; a precondition for control selection. | ch04 |
| **Common control** | A control provided by the organization and inherited by one or more systems; assessed once by the provider, not re-assessed per inheriting system. | ch03, ch04 |
| **Continuous monitoring strategy** | The governing artifact that sets per-control assessment frequency and reporting cadence; defined at organization level (P-7) and optionally at system level (S-5). | ch03, ch07 |
| **Control** | A safeguard or protection capability selected and implemented to satisfy a requirement; qualified "security" or "privacy" only when chosen for that objective. | ch02 |
| **Hybrid control** | A control partly satisfied centrally (common) and partly at the system level; the split between the two parts is documented. | ch03, ch04 |
| **High-water mark** | The conservative roll-up that sets a non-national-security system's single impact level to its most severe information-type impact level (per FIPS 200). | ch04 |
| **Impact level** | Low, moderate, or high — the severity of consequence from loss of a security objective, per FIPS 199. | ch04 |
| **Implement (step)** | The RMF step that installs the planned controls and records the as-built configuration. Tasks I-1 (build) and I-2 (record the delta). | ch05 |
| **Information system** | A discrete set of information resources organized to collect, process, maintain, use, share, disseminate, or dispose of information — read very broadly (from supercomputers to smartphones to paper). | ch01 |
| **Monitor (step)** | The RMF step that sustains ongoing situational awareness of posture so risk decisions rest on current evidence. Seven tasks M-1…M-7. | ch07 |
| **Ongoing authorization** | A mode where a mature monitoring program replaces a fixed authorization expiry date with a time-driven re-judgment frequency, enabling near-real-time risk management. | ch06, ch07 |
| **Plan of Action and Milestones (POA&M)** | A prioritized, scheduled remediation plan for deficiencies the organization chooses to fix later rather than now. | ch05, ch06 |
| **Posture (security and privacy)** | The current status of systems and resources given the defenses in place — the evidence base the authorizing official reads to judge acceptable risk. | ch02 |
| **Prepare (step)** | The first RMF step; organization-level (P-1…P-7) and system-level (P-8…P-18) groundwork — roles, risk strategy, common controls, baselines, boundaries, requirements. | ch03 |
| **Privacy risk** | Risk to individuals from the processing of PII; not a subset of security risk — some of it arises from fully *authorized* processing, so securing PII does not by itself protect privacy. | ch01, ch02 |
| **Reciprocity** | An agreement to accept another organization's assessment results so information can be shared without redundant re-assessment. | ch01 |
| **Requirement** | Either a legal/policy obligation or, more broadly, the expression of a stakeholder protection need; requirements drive controls, which in turn drive specification and statement-of-work requirements. | ch02, ch03 |
| **Residual risk** | The risk that remains after a response; the goal is to land it inside organizational risk tolerance, not to reach zero. | ch06 |
| **Reuse (of evidence)** | Using prior audits, vendor evaluations, product-validation programs, earlier SDLC testing, and reciprocity as assessment evidence under pre-set criteria — the efficiency engine of Assess and Monitor. | ch05, ch07 |
| **Risk Management Framework (RMF)** | The seven-step, life-cycle, risk-based process at the core of SP 800-37: Prepare, Categorize, Select, Implement, Assess, Authorize, Monitor. | ch01, ch02 |
| **Risk executive (function)** | The organization-level function (and the senior accountable official for risk management) that links system-level decisions to enterprise risk strategy and tolerance. | ch01, ch06 |
| **Risk tolerance** | The degree of risk or uncertainty an organization is willing to accept; it constrains every downstream risk decision. | ch03 |
| **Select (step)** | The RMF step that chooses, tailors, allocates, documents, and sets monitoring for the controls. Tasks S-1…S-6; baseline (top-down) or organization-generated (bottom-up) approaches. | ch04 |
| **Senior Agency Official for Privacy (SAOP)** | The official accountable for the privacy program who assesses privacy controls and reviews PII systems before the AO decides. | ch04, ch05 |
| **Supply Chain Risk Management (SCRM)** | The discipline, folded *into* the RMF, for managing risk from external providers and COTS components; every RMF step but Authorize can be done by an external provider. | ch02 |
| **System element** | A part of a system — technology/machine, human, or physical/environmental; a *system component* is specifically a hardware/software/firmware element. | ch02, ch03 |
| **Tailoring** | Adjusting a selected control baseline to the system's missions, threats, supply chain, type, and risk tolerance — scoping, compensating controls, parameter values, supplements. | ch04 |
| **Three-tier risk model** | The SP 800-39 view: organization (Level 1), mission/business process (Level 2), and information system (Level 3), with risk flowing across all three. | ch02 |
| **Vulnerability** | A deficiency that a threat agent can exploit — a finding becomes a vulnerability only when exploitable. | ch05 |
