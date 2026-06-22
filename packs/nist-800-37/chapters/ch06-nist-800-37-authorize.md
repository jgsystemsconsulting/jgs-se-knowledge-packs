# Chapter 6 — The Authorize Step

## Core Idea
The Authorize step exists to put a name on the risk. After a system is categorized, controls are selected, implemented, and assessed, a single senior official must look at the residual security and privacy risk — including supply chain risk — and decide whether it is acceptable for the organization to operate the system or to offer the common controls for others to inherit. The purpose is organizational *accountability*: someone with the authority to commit the organization explicitly owns the decision to accept (or refuse) the risk to operations, assets, individuals, other organizations, and the Nation. This is the RMF's deliberate hand-off from engineering and assessment evidence to executive risk judgment.

> **Caveat (RMF / security-engineering edge of SE):** Authorize is a governance and risk-acceptance gate, not a design or build activity. It sits at the security/privacy risk-management boundary of systems engineering — it consumes the artifacts that engineering produces and turns them into an accountable go/no-go, rather than producing system functionality itself.

## Frameworks Introduced
The source names these constructs and where they enter the step:

- **The five Authorize tasks (R-1 through R-5)** — the step decomposes into Authorization Package (R-1), Risk Analysis and Determination (R-2), Risk Response (R-3), Authorization Decision (R-4), and Authorization Reporting (R-5). Each task is defined by potential inputs, expected outputs, a primary responsibility, supporting roles, and an SDLC phase.
- **The authorization package** — assembled in R-1 and submitted to the authorizing official. It bundles the security and privacy plans, the security and privacy assessment reports, the plan of action and milestones (POA&M), and an executive summary; the authorizing official may request more. Used throughout the step as the evidence base for the decision.
- **Cybersecurity Framework (NIST CSF) constructs** — the source maps outcomes to CSF. R-3 references the CSF Identify function (ID.RA-6 for risk response), and R-5 lets deficiencies be reported using CSF Subcategories, Categories, and Functions (Identify, Protect, Detect, Respond, Recover).
- **Ongoing authorization** — a mode in which a sufficiently robust and mature continuous monitoring program lets the organization replace a fixed authorization termination date with a time-driven authorization *frequency*, supporting near real-time risk management.
- **Three authorization types (R-4 outputs)** — authorization to operate, authorization to use, and common control authorization, each with a matching denial. Appendix F (referenced) carries the detailed guidance on these types and on package preparation.
- **Supply Chain Risk Management plans** — R-1 references SP 800-161 for SCRM plans, since the acceptable-risk judgment explicitly includes supply chain risk.
- **Governance, Risk, and Compliance (GRC) / automated security/privacy management and reporting tools** — named as the means to prepare, assemble, transmit, and continuously maintain authorization packages, especially under ongoing authorization.

## Key Concepts

- **R-1 — Authorization Package.** The system owner, common control provider, and (for systems handling PII) the senior agency official for privacy assemble the package and submit it. Version and change control are maintained as plans, assessment reports, and POA&M are updated; keeping those current on an ongoing basis is what enables ongoing authorization and reauthorization. When controls come from an external provider (contracts, interagency agreements, licensing, supply chain), the organization must ensure the provider supplies the information needed for a risk-based decision. For PII systems, the privacy official reviews the package for privacy compliance and risk *before* the authorizing official renders a determination.

- **R-2 — Risk Analysis and Determination.** The authorizing official (or designated representative), working with the senior agency information security officer and — for PII — the privacy official, analyzes the package and finalizes the risk determination. Organization-level context is fed in by the risk executive (function) — equivalently, the senior accountable official for risk management — covering risk tolerance, dependencies among systems and controls, mission/business criticality, and the risk management strategy. Any such input is documented and carried, where relevant, into the authorization decision (R-4). The expected output is simply the **risk determination**.

- **R-3 — Risk Response.** Once risk is determined, the organization chooses a course of action. The source names two response paths explicitly: **mitigation** and **acceptance**. When the response is mitigation, planned actions are tracked in the POA&M; once remediated, assessors *reassess* the affected controls and update the assessment reports with new findings — without overwriting the original results — and the security and privacy plans are updated to reflect the post-remediation state, including any compensating controls. When the response is acceptance, the deficiencies stay documented in the assessment reports and are monitored for changes in risk factors. Only the authorizing official can accept risk. Response can be prioritized — higher-priority risks may draw more resources — but prioritization does not mean ignoring lower-priority risks. The chapter stresses that some **residual risk always remains**, and acceptable residual risk is set by organizational risk tolerance.

- **R-4 — Authorization Decision.** Explicit risk acceptance belongs to the authorizing official and **cannot be delegated**. The decision balances security and privacy against mission and business needs, and the official consults the senior accountable official for risk management / risk executive before finalizing. The decision conveys the terms and conditions, the authorization termination date *or* (under ongoing authorization) the time-driven frequency, any risk-executive input, and — for common controls — the system impact level the controls support. It is transmitted to the system owner or common control provider, who acknowledges and implements the terms; the official then verifies adherence on an ongoing basis through continuous monitoring (Task M-2).

- **R-5 — Authorization Reporting.** The authorizing official reports the decision to designated officials so individual risk decisions can be seen in the organization-wide risk context, and reports exploitable deficiencies (vulnerabilities) representing significant security or privacy risk. The source is specific: this reporting occurs only where authorization has been delegated below the head of agency. What counts as "significant" is set by organizational policy. The status may be annotated in the organizational system registry (linking back to Task P-18).

- **Inheritance and external dependencies.** Common control authorization tells inheriting system owners whether they may rely on those controls, and at what impact level — making one authorization decision a dependency for many systems. Because dependencies run across organizational and external systems, individual decisions must weigh current residual risk, POA&M, and organizational risk tolerance.

## Mental Models

- **The package is the case file; the authorizing official is the judge.** Engineering and assessment build the evidentiary record (plans, assessment reports, POA&M, executive summary); the authorizing official reads the record and rules. The decision is only as good — and as current — as the package.
- **Accountability concentrates to a single point.** Many roles support the step, but risk *acceptance* is one person's signature that cannot be passed off. The whole machinery exists to make that one judgment informed and defensible.
- **From snapshot to stream.** The classic model is a dated authorization (a snapshot with a termination date). Ongoing authorization converts it into a continuous stream: a mature continuous monitoring program lets the official re-judge at a defined frequency and either reaffirm acceptance or pull the authorization. Reauthorization becomes a by-product of keeping the package live.
- **Residual risk is the deliverable you can't eliminate.** Every response leaves something behind; the job is not to reach zero but to land residual risk inside the organization's tolerance — and to write down what was accepted.
- **Automate the paperwork, not the judgment.** GRC and automated reporting tools speed package assembly, transmission, and refresh (and even automated authorization decisions under ongoing authorization), but the source still treats acceptance as a human accountability that tools serve rather than replace; some controls aren't suited to automation, and manual methods remain acceptable there.

## Anti-patterns
The source does not frame these as named "anti-patterns"; it states the corresponding rules, so treat the following as guardrails drawn from those rules:

- Treating risk acceptance as delegable — R-4 is explicit that the authorizing official alone accepts risk and cannot delegate it.
- Letting the authorization package go stale — the step depends on timely updates to plans, assessment reports, and POA&M; without them ongoing authorization and reauthorization break down.
- Overwriting original assessment results during reassessment — assessors add reassessment findings; they do not erase the initial results.

## Key Takeaways
1. Authorize converts engineering and assessment evidence into an **accountable risk-acceptance decision** by a senior official — security/privacy risk, including supply chain risk.
2. The step runs as **five tasks**: assemble the package (R-1), determine risk (R-2), respond to risk (R-3), decide (R-4), and report (R-4 → R-5).
3. **Risk response** is mitigation or acceptance; mitigation is tracked in the POA&M and triggers control reassessment, and **residual risk always remains** within organizational tolerance.
4. **Risk acceptance cannot be delegated** — it is the authorizing official's personal accountability.
5. **Ongoing authorization** (backed by mature continuous monitoring) replaces a termination date with a defined frequency, enabling near real-time risk management and reauthorization.
6. Outputs are **authorization to operate / to use / common control authorization** (or their denials); common control authorizations cascade to every inheriting system.

## Connects To
- **ch05 — Assess step (R upstream):** the security and privacy assessment reports and the POA&M that feed the authorization package come from Assess.
- **ch07 — Monitor step (downstream):** continuous monitoring (Task M-2) verifies the terms and conditions and supplies the evidence that ongoing authorization re-judges.
- **Prepare step (P-18):** authorization status can be tracked through the organization-wide system registration process.
- **`nist-sse` (SP 800-160 v1):** referenced across R-2/R-3/R-4/R-5 (Risk Management, Decision Management, Project Assessment and Control processes) — SSE supplies the protection engineering; Authorize governs whether the residual risk is accepted.
- **`nist-csf`:** CSF Functions/Categories/Subcategories used for risk response (ID.RA-6) and for reporting significant deficiencies (R-5).
- **SP 800-39 / SP 800-30 / SP 800-137 / SP 800-161:** organization-tier risk management, risk assessment, continuous monitoring, and supply chain risk that frame the determination, response, and ongoing decision.
