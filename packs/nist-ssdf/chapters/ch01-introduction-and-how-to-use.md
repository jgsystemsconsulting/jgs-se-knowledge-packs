# Chapter 1: Introduction and How to Use the SSDF

## Core Idea
The SSDF is a high-level, outcome-focused set of secure software development practices that can be integrated into any SDLC model; it provides a common vocabulary for producers and acquirers without prescribing specific tools or techniques.

## Frameworks Introduced
- **Secure Software Development Framework (SSDF)**: A core set of fundamental, high-level practices organised into four practice groups (PO, PS, PW, RV) to reduce vulnerabilities and improve software security posture.
  - When to use: Whenever an organisation needs to integrate security into an existing SDLC model, communicate requirements to suppliers, or evaluate software acquired from third parties.

## Key Concepts
- **Software Development Life Cycle (SDLC)**: A formal or informal methodology for designing, creating, and maintaining software, including code built into hardware; SSDF applies regardless of which SDLC model is used.
- **Shifting Left**: The principle that addressing security earlier in the SDLC reduces effort, cost, and technical debt compared to finding flaws late in development or post-release.
- **Practice**: A named, uniquely identified activity (e.g., PO.1) that explains what to do and why; each practice contains tasks, notional implementation examples, and references.
- **Task**: A specific action within a practice that may be needed to accomplish that practice's goal.
- **Notional Implementation Example**: An illustrative example of tools, processes, or methods that could implement a task; examples are not required and are not the only feasible options.
- **Software Producer**: An organisation that develops software, including COTS vendors, GOTS developers, custom developers, and internal teams.
- **Software Acquirer**: A federal agency or other organisation that procures software and can use the SSDF to specify security requirements in acquisition.
- **Risk-Based Approach**: The expectation that organisations select and prioritise SSDF practices based on risk, cost, feasibility, and applicability rather than treating the framework as a mandatory checklist.
- **Shared Responsibility Model**: When software is delivered as a service (IaaS, SaaS, PaaS), responsibility for SSDF practices is distributed between the platform/service provider and the tenant organisation via formal agreement.
- **Provenance**: The chronology of origin, development, ownership, location, and changes to a system or system component and associated data, including personnel and processes involved.

## Mental Models
- Use SSDF practices as a planning and communication tool, not a prescriptive checklist: select practices appropriate to your risk profile and SDLC context.
- Use shifting left when you want to reduce the cost of security: security addressed at design time is systematically cheaper than security addressed post-release.
- Use the SSDF's common vocabulary when procuring software: reference specific practice IDs (e.g., PO.1.3, PS.2.1) in contracts to communicate security expectations to suppliers.
- Use the four practice groups (PO, PS, PW, RV) as a lifecycle map: PO prepares the foundation, PS protects artefacts, PW builds in security, RV closes the loop.

## Anti-patterns
- **Treating SSDF as a compliance checklist**: NIST explicitly states the intention is not a checklist; skipping the risk-based selection step leads to misallocated effort.
- **Assuming one-size-fits-all applicability**: Some practices are not applicable to all situations (e.g., compiler hardening is irrelevant if no compiler is used); blanket adoption without contextual filtering wastes resources.

## Key Takeaways
1. Security must be integrated throughout the entire SDLC, not bolted on at the end.
2. Shifting left on security reduces cost and technical debt.
3. The SSDF provides outcomes, not implementation prescriptions; tool and technique choices remain with the organisation.
4. Any SDLC model (waterfall, agile, DevOps) can adopt the SSDF.
5. Both software producers and acquirers have distinct but complementary uses for the framework.
6. Shared-service delivery models require explicit contractual allocation of SSDF responsibilities.

## Connects To
- **NIST Cybersecurity Framework (CSF)**: SSDF practices may support CSF Functions, Categories, and Subcategories, but they are typically the responsibility of different parties; developers adopt SSDF, operators adopt CSF.
- **EO 14028 (Improving the Nation's Cybersecurity)**: The SSDF was updated in direct response to EO 14028 Section 4; Appendix A maps EO subsections to SSDF practice/task IDs.
- **NIST SP 800-53 (Security and Privacy Controls)**: Several SSDF tasks reference SP 800-53 controls (SA-family, SR-family) as informative references.
- **NIST SP 800-161 (C-SCRM)**: Supply-chain risk management practices align with SSDF tasks for third-party component verification.
