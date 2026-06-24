# Chapter — Roles, Responsibilities, and Principles of Tailoring

> Source caveat: This chapter is drawn from NPR 7150.2D, a NASA Procedural Requirement published in the NASA Online Directives Information System (NODIS) and rendered here from the NODIS HTML. It governs software-engineering requirements that complement the broader software-for-systems area, and it places no obligation on members of the public other than where law allows or where its terms have been written into a contract. Always confirm the current version in the NODIS Library before relying on any requirement.

## Core Idea

This chapter answers two coupled questions: *who is accountable* for software-engineering requirements across NASA, and *how may a project be relieved* from a requirement it cannot fully meet. The directive assigns named responsibilities from the Agency headquarters level down to individual project managers, and then defines tailoring as the disciplined, evidence-backed, authority-approved path for adjusting which requirements apply to a given software effort. The unifying mechanism is governance: every requirement carries a designated authority, and every deviation must be justified, risk-assessed, formally accepted by the responsible manager, and recorded. Roles exist so that tailoring decisions land with someone who is competent and accountable to make them.

## Frameworks Introduced (exact source names, when/how)

The chapter introduces or invokes the following named instruments and constructs:

- **Requirements Mapping Matrix** — the central artifact. It documents which requirements a project commits to meet, which are marked "Not-Applicable," and any approved tailoring with its justification. It can also serve as the streamlined form for submitting a relief request, carrying the signatures that record authority approval.
- **Technical Authority (TA) governance** — the structure NASA established to keep control over how requirements are applied and to ensure proposed deviations are properly mitigated. Each requirement's responsible technical or institutional authority is listed in the directive's Appendix C "Authority" column.
- **Appendix C** — defines the default applicability of requirements by software classification, marking an invoked requirement with "X" and leaving optional/not-invoked requirements blank. It also flags requirements (the "X" markings) whose tailoring needs designated-authority approval.
- **Appendix D** — holds the software classification definitions used to check whether a project has categorized its components correctly and to recognize when an effort migrates to a higher or lower class.
- **CMMI-DEV (Capability Maturity Model Integration for Development)** — cited as the preferred benchmark for objectively gauging a Center's progress in software process improvement; ratings are measured by a CMMI Institute Certified Lead Appraiser.
- **NASA-STD-8739.8 (NASA Software Assurance and Software Safety Standard)** — the benchmark against which the Chief of Safety and Mission Assurance assesses each Center's assurance and safety capability, and the source of the criteria for Independent Verification and Validation (IV&V) — the practice of having an organization independent of the developer perform the verification and validation work.
- **NASA-HDBK-2203 (NASA Software Engineering Handbook)** — the recommended-practice companion holding guidance on document content, per-requirement detail, links to NASA Lessons Learned, and tailoring guidance; it also informs each Center's Software Engineering Improvement Plan.
- **Referenced governing directives** — tailoring is also bound by a set of higher directives: NPD 1000.3 and NPD 2800.1; the IT-security NPR 2810.1; the program/project-management family (NPR 7120.5, 7120.7, 7120.8, and the health/medical 7120.11); and the general-safety NPR 8715.3. Software sharing and release invokes NPR 2210.1, and the IV&V tailoring decision (SWE-141) is reserved to the Chief of SMA.

## Key Concepts

**Tailoring defined.** Tailoring is the process of seeking relief from a directive requirement in a way that stays consistent with program or project objectives, an acceptable level of risk, and real constraints. Because software systems vary so widely, the directive permits the requirement set to be adjusted for a specific effort where the change is both justified and approved.

**A baseline you tailor *from*.** The directive sets a baseline meant to reduce software-engineering risk; Appendix C then assigns default applicability by class. Tailoring modifies that default based on characteristics of the effort — the acceptable technical and programmatic risk posture, Agency priorities, size, and complexity. Tailoring can also be applied across a family of similar projects, a program, or an organization, not just one project at a time.

**The "X" gate.** Where a requirement is marked "X" for a given class, any tailoring of it requires approval from the authority named in Appendix C. A blank means the requirement is optional or not invoked. Even when an "X" requirement is implemented, the *how* of meeting it is normally left to software-engineering management working with the project.

**A relief request is an evidence package.** A request for relief is not a request to skip work; it carries the rationale, a risk evaluation, and the supporting material that justifies acceptance. The submitting organization must promptly inform the next higher level of management, and the dispositioning organization must coordinate with any other organization that could be affected — safety, quality, cybersecurity, health — and obtain their concurrence.

**Who signs.** Relief at either the Center or HQ level may be submitted as a Requirements Mapping Matrix, and it must collect the required signatures: engineering, the NASA CIO, and SMA authorities, with the designated SAISO signature additionally required to relieve a Section 3.11 cybersecurity requirement. The responsible program, project, or operations manager must formally accept the tailoring risk. For tailoring that involves human-safety risk, the actual risk takers (or their official spokesperson and supervisory chain) must formally agree to assume that risk.

**Layered co-approval.** Tailoring decided at the Center level consults four parties: the Center's Engineering TA and its SMA TA, the Center Health and Medical TA, plus the designee who carries the NASA CIO's Center-level IT authority. At the HQ level, the Office of Safety and Mission Assurance co-approves any software tailoring; the Office of the Chief Health and Medical Officer co-approves tailoring touching health and medical implications; and the SAISO co-approves any tailoring of the cybersecurity requirements.

**The role roster.** The chapter walks the responsibility chain:

- **Office of the Chief Engineer (OCE)** — leads the Software Engineering Initiative, benchmarks each Center's capability, periodically reviews the requirements mapping matrices, authorizes compliance appraisals, supports training, and maintains the Agency process asset library.
- **Chief, Safety and Mission Assurance (SMA)** — owns Agency software assurance and software safety policy as the Technical Authority for those requirements, benchmarks Center capability against NASA-STD-8739.8, reviews matrices, authorizes appraisals, provides assurance training, and makes the final call on tailoring of the IV&V requirement (SWE-141).
- **Chief Information Officer (OCIO) / SAISO** — conducts security assessments and appraisals on selected requirements and participates in software development reviews as needed.
- **Chief Health and Medical Officer (CHMO)** — is the Technical Authority for health- and medical-impacting requirements and holds tailoring approval authority for software with such implications (per NPR 7120.11).
- **Center Director** — a delegable role responsible for staffing and advancing the Center's software-engineering capability, monitoring contractor capability, establishing and maintaining software processes, complying with Appendix C "X" requirements, maintaining a list of programs/projects with Class A–D software, standing up measurement and cost repositories for Class A–C work, contributing process assets to the Agency library, and governing internal software sharing/reuse (rights, conformance, contributor lists, and disclaimers).
- **Center SMA Director** — a delegable role that designates SMA Technical Authorities, ensures hazard analyses include software, reviews the IV&V Project Execution Plan against NASA-STD-8739.8, supports CMMI-DEV ratings, and ensures disagreements between engineering and assurance are identified, tracked, and escalated if unresolved.
- **Contracting Officers / Agreement Managers** — ensure the appropriate FAR, NFS, and other clauses based on this directive and NASA-STD-8739.8 are placed in contracts, agreements, and grants under which software is acquired or managed.
- **Technical Authorities** — assess matrices and tailoring by checking classification accuracy against Appendix D, confirming "Not-Applicable" markings are genuinely inapplicable, judging whether requested relief and its mitigations are reasonable, approving or disapproving the relief within their scope, including the SAISO in reviews for cybersecurity coverage, and ensuring approved matrices and rationale are archived as retrievable project records. Their approval is shown by signature in the matrix itself.

**Delegation and evolution.** Several phrases — "the Center Directors shall…," "the Center SMA Director will…," "the project manager shall…" — explicitly mean the role may be further delegated to a level consistent with the system's scope and scale. And when a system or subsystem evolves into a higher or lower classification, the project manager must update plans and initiate any supplier-contract modifications to carry the now-applicable requirements with their approved tailoring (SWE-021).

## Mental Models

- **Requirement → Authority → Signature.** Read the chapter as a pipeline: every requirement points to a designated authority, and that authority's signature in the Requirements Mapping Matrix is the record that a commitment or a tailoring decision was actually made by someone empowered to make it.
- **The matrix as a contract of intent.** The Requirements Mapping Matrix is the single place that states what the project will do, what it deems inapplicable, and what it was relieved from — with justification attached. If it is completed and approved per NPR 7120.5 and this directive, it *is* the tailoring mechanism.
- **Relief is borrowed, not free.** Tailoring transfers risk to a named risk taker who must formally accept it. Cross-impact organizations (safety, quality, cybersecurity, health) must concur, so a deviation in one discipline cannot be granted in isolation.
- **Class drives default, effort drives deviation.** Appendix C fixes the starting requirement set from software class; the project's risk posture, size, and complexity justify any move away from it. Higher headquarters-reserved requirements (e.g., HQ TA items) raise the approval level required to deviate.

## Key Takeaways

- Responsibility for the directive runs from the OCE, SMA, OCIO/SAISO, and CHMO at Agency level, through Center Directors and Center SMA Directors, to Contracting Officers, Technical Authorities, and project managers — many of these roles explicitly delegable to fit system scope and scale.
- Tailoring is the governed route to relief from a requirement: it must be justified, risk-evaluated, formally accepted by the responsible manager, concurred by impacted disciplines, and recorded.
- The Requirements Mapping Matrix is the operative artifact — it captures commitments, "Not-Applicable" calls, and approved tailoring with justification, and its signatures encode authority approval.
- Appendix C marks invoked requirements with "X" by software class and names the approving authority; Appendix D supplies the classification definitions that the TAs validate.
- Cybersecurity (Section 3.11) and human-safety tailoring carry extra co-approval and risk-acceptance requirements (SAISO signature; actual risk takers agreeing to assume the risk).
- Companion standards anchor the system: NASA-STD-8739.8 for assurance/safety and IV&V criteria, NASA-HDBK-2203 for recommended practice and tailoring guidance, and CMMI-DEV as the preferred capability benchmark.

## Connects To

- **Appendix C and Appendix D** of NPR 7150.2D — the requirement-applicability matrix and the software classification definitions that this chapter's roles and tailoring rules operate on.
- **NPR 7120.5** — the project-management directive that defines Technical Authority (Section 3.3) and the basis on which the Requirements Mapping Matrix is approved.
- **NASA-STD-8739.8** and **NASA-HDBK-2203** — the assurance/safety standard and the engineering handbook that supply benchmarks, IV&V criteria, content guidance, and tailoring detail referenced throughout the chapter.
- **CMMI-DEV** — the external capability-maturity framework NASA uses to benchmark and rate software-development organizations.
- **The broader software-for-systems area** — these software-engineering requirements complement systems-level engineering and acquisition directives (e.g., the NPR 7120.x family, NPR 8715.3, NPR 2210.1, NPR 2810.1), connecting software governance to program, safety, cybersecurity, and release frameworks.
