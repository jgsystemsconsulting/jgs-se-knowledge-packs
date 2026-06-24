# Chapter — Operational Technology Cybersecurity in MRL Assessments

## Core Idea

Manufacturing readiness now has to account for the security of the shop floor itself, not just the maturity of its processes. Adversaries have learned to attack the manufacturing base through software — quietly disrupting operations or degrading product quality in ways that may go unnoticed. Because of this threat, the MRL Working Group folded cybersecurity criteria into multiple threads of the MRL matrix, deliberately scoping those criteria to Operational Technology (OT): the programmable systems and devices that touch the physical world on the production floor.

The framing here is pragmatic and bounded. An MRL Assessment that exercises the cybersecurity criteria is explicitly *not* a deep cybersecurity audit. Its job is to pose simple, foundational questions — has the organization thought about OT security at all, and have basic common-sense controls been put in place — so that the team can surface risks or major gaps in OT protection. The Subject Matter Experts (SMEs) running an MRL Assessment are not expected to be cyber specialists, so the criteria are written at a top level that anyone can evaluate, with the option to pull in a cybersecurity expert when a discussion turns highly technical.

This chapter deepens the broader MRL 1-10 maturation arc that the GAO Technology Readiness Assessment material covers: OT cybersecurity is meant to be addressed *across* maturation, starting at manufacturing concept development and carrying through to full-rate-production (FRP) capability, rather than being a one-time gate.

## Frameworks Introduced (exact source names, when/how)

The source grounds the OT cybersecurity criteria in a stack of named federal standards, regulations, and programs. Each is introduced for a specific decision point in the assessment.

- **NIST SP 800-37** (revision 2), the Risk Management Framework standard for information systems and organizations — invoked as the authority that defines what "Operational Technology" means: programmable systems or devices that interact with (or manage devices that interact with) the physical environment, detecting or causing direct change by monitoring or controlling devices, processes, and events. This is the definitional anchor for the whole appendix.

- **NIST SP 800-53**, the catalog of security and privacy controls for federal information systems — named as the control set that **Federal Systems** must comply with, alongside the Federal Information Security Modernization Act (FISMA) and Federal Information Processing Standards (FIPS) 200. Used when the manufacturing facility qualifies as a system operated by or on behalf of an executive agency such as DoD.

- **NIST SP 800-171**, on protecting Controlled Unclassified Information held in non-federal systems — named as the recommended security requirements for keeping Controlled Unclassified Information (CUI) confidential on **Non-Federal Systems** (contractor-owned, contractor-operated). The source stresses that 800-171 is the actual *source* of the requirements to protect CUI.

- **NIST SP 800-82, Guide to Industrial Control Systems (ICS) Security** — named as the origin of the general cybersecurity concepts the assessor should keep in mind (network layering, DMZ architecture, redundancy, and so on).

- **FAR Clause 52.204-2, Security Requirements** — applies when classified information is involved; the facility's implementation status is recorded in the contractor's Security Plan, with the Defense Counterintelligence and Security Agency as the point of contact.

- **DFARS Clause 252.204-7012**, which covers safeguarding covered defense information and reporting cyber incidents — applies when Controlled Technical Information (CTI), including export-controlled information, is in play; when this clause is in the contract, requirements are implemented per NIST SP 800-171.

- **DFARS Clauses 252.204-7019 and 252.204-7020** — require an assessment of how well a contractor has implemented the NIST SP 800-171 requirements, with results posted to the **Supplier Performance Risk System (SPRS)** for authorized viewers.

- **FAR 52.204-21, Basic Safeguarding of Covered Contractor Information Systems** — named as a contractual vehicle that conveys safeguarding requirements for Non-Federal Systems.

- **DoD Instruction 5200.48, Controlled Unclassified Information** — governs CUI when it resides in Non-Federal Systems.

- **Cybersecurity Maturity Model Certification (CMMC)** — described as a certification *process* that leverages the NIST SP 800-171 requirements, with an explicit caveat that it is **not** the source of those requirements.

- **Support programs for small manufacturers** — Procurement Technical Assistance Centers (PTAC) via the Small Business Administration, the NIST Manufacturing Extension Partnership (MEP), and the Cybersecurity Evaluation Tool (CSET) are named as guidance and training resources.

## Key Concepts

**OT versus the other technology categories.** The source draws a deliberate boundary: Operational Technology is set apart from Information Technology (IT), Platform Information Technology (PIT) or mission data, and enterprise Management Information Systems (MIS). OT examples on the floor include numerically-controlled (NC) machines, automated inspection equipment, and sensors, alongside the 800-37 examples — industrial control systems, building-management systems, fire-control systems, and mechanisms governing physical access. The reason OT gets its own scrutiny: it may not be governed as tightly by the IT department or examined as carefully in standard IT reviews and audits — so it can fall through the cracks.

**Federal versus Non-Federal Systems — the routing question.** Before the assessment, the team must understand the facility's business environment along two axes. First, the contract type and information handled: classified information triggers FAR 52.204-2; CTI triggers DFARS 252.204-7012. Second, who operates the facility. A **Federal System** (operated by or on behalf of an executive agency, including embedded information systems and agency-provided cloud services) falls under FISMA, FIPS 200, and NIST SP 800-53. A **Non-Federal System** (contractor-owned and operated, internal cloud or IT processing done on the contractor's behalf) falls under NIST SP 800-171 for CUI protection. Getting this routing right determines which control set and which clauses actually apply.

**The general ICS security concepts (from 800-82).** The source lists practical controls the assessor should look for: security policies, procedures, training, and materials tailored to the manufacturing environment; addressing cybersecurity across the whole maturation arc; a layered network topology where the most critical communications live in the most secure and reliable layer; logical separation between corporate, IT, and OT networks; a DMZ architecture that blocks direct traffic between corporate and IT/OT networks; redundant networks for critical components such as a process control system (PCS); protection of manufacturing process data (recipes, configuration control information, test parameters and results); operator authentication to OT equipment where feasible; and protection of non-conformance information for critical processes, marked and disseminated as controlled technical information or company-proprietary — both categories of CUI.

**Self-audit before external audit.** For small manufacturing companies, the source recommends leaning on PTAC, MEP, and CSET guidance and training *instead of* jumping straight to external or independent audits — but only after the company has first run an internal self-audit.

## Mental Models

**The shop floor is an attack surface, not just a workspace.** Treat NC machines, inspection rigs, and sensors as networked, programmable assets that an adversary can reach and subvert. A successful OT attack does not announce itself; it may simply make the product worse while the line keeps running.

**Two questions before the checklist: what information, and who operates the system.** These two axes — the sensitivity of the information (classified / CTI / CUI) and the operator's status (Federal vs Non-Federal) — deterministically select which standards and clauses govern the facility. Resolve them first; everything downstream follows.

**Common sense over forensic depth.** The assessment is a screen, not an audit. The mental posture is "has this been thought about, and are basic controls present," with the goal of catching major gaps — not certifying full compliance. Save the deep technical interrogation for an actual cyber expert.

**Defense in layers and separation.** Picture concentric network zones: corporate on the outside, IT and OT progressively more protected, with the most critical communications in the innermost, most reliable layer. A DMZ stands between corporate and IT/OT so no traffic flows directly across; critical control components sit on redundant networks.

**Certification is a wrapper, not the source.** CMMC is the process that checks for the requirements; NIST SP 800-171 is where the requirements to protect CUI actually live. Don't confuse the audit mechanism with the control set it inspects.

## Anti-patterns

The source does not explicitly label any practice as an "anti-pattern," so none are asserted here. The closest cautions it raises — leaving OT outside the IT department's normal review scope, mistaking CMMC for the source of CUI requirements, and small firms reaching for external audits before doing an internal self-audit — are framed as considerations and notes rather than named anti-patterns.

## Key Takeaways

- Manufacturing readiness now includes protecting shop-floor networks and equipment; the MRL Working Group embedded OT cybersecurity criteria across multiple MRL threads.
- "Operational Technology" is defined by NIST SP 800-37: programmable systems/devices that interact with the physical environment by monitoring or controlling devices, processes, and events.
- OT is deliberately distinguished from IT, PIT/mission data, and MIS because it is often less closely governed and less thoroughly audited — which is exactly why it needs attention.
- The criteria are a top-level screen, not a detailed audit: ask fundamental questions, confirm basic controls, and flag major gaps. SMEs need not be cyber experts.
- Resolve two things first: what information the facility handles (classified → FAR 52.204-2; CTI → DFARS 252.204-7012) and whether it is a Federal System (FISMA / FIPS 200 / NIST SP 800-53) or a Non-Federal System (NIST SP 800-171 for CUI).
- DFARS 252.204-7019/7020 drive an assessment of NIST SP 800-171 implementation, with results in SPRS.
- General ICS security concepts come from NIST SP 800-82: layered networks, corporate/IT/OT separation, DMZ architecture, redundant networks for the PCS, protection of process data and non-conformance information, and operator authentication.
- CMMC leverages NIST SP 800-171 but is not the source of the CUI-protection requirements; 800-171 is.
- Small manufacturers should use PTAC, MEP, and CSET support — and run an internal self-audit before turning to external audits.

## Connects To

- **gao-tra (MRL 1-10):** This chapter deepens the MRL maturation framework that the GAO Technology Readiness Assessment material treats. OT cybersecurity is to be addressed throughout maturation — from manufacturing concept development to FRP capability — so it threads through the same MRL 1-10 progression rather than sitting at a single milestone.
- **NIST standards family:** SP 800-37 (OT definition and Risk Management Framework), SP 800-53 (Federal System controls), SP 800-171 (Non-Federal System CUI protection), and SP 800-82 (ICS security concepts) form the technical backbone referenced throughout.
- **Contractual / regulatory layer:** FAR 52.204-2, FAR 52.204-21, DFARS 252.204-7012, and DFARS 252.204-7019/7020, plus DoD Instruction 5200.48, govern how the requirements reach the facility and how implementation is assessed (SPRS).
- **CMMC and small-business support:** CMMC as the certification process over 800-171, and PTAC / MEP / CSET as the on-ramp for small manufacturers, connect the formal standards to the practical readiness path.
