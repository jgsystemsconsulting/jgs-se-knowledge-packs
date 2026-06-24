# Chapter — Reference: Acronyms, V&V Checklists, and Definitions

## Core Idea

The closing appendices of the FAA AMS Lifecycle V&V Guidelines turn the
preceding narrative into a working reference kit. Three artifacts do this job:
a glossary of acquisition acronyms (Appendix A), a set of document-specific
verification and validation checklists (Appendix B), and a dictionary of the
verification and validation methods themselves (Appendix C). Together they let
a practitioner who is mid-review answer three concrete questions without
re-reading the body of the guideline: what does this abbreviation stand for,
what exactly must I confirm on this particular program document, and what does
it mean to verify something by (say) demonstration rather than inspection. The
reference is deliberately operational — each checklist column asks the reviewer
to name the method used and to point at the artifact that records the outcome.

## Frameworks Introduced (exact source names, when/how)

The slice introduces or formalizes the following named structures:

- **Appendix A — Acronyms.** A flat lookup table covering the acquisition
  vocabulary used throughout the guideline, from ACAT (Acquisition Categories)
  through V&V (Verification and Validation). It anchors the AMS-specific terms a
  reviewer will hit: AMS (Acquisition Management System), APB (Acquisition
  Program Baseline), PRD (Program Requirements Document), and the decision
  milestones such as IID (Initial Investment Decision), FID (Final Investment
  Decision), and ISD (In-Service Decision).

- **Appendix B — Verification and Validation Checklists.** Four document-keyed
  checklists, one per major program artifact: the Program Requirements Document
  (PRD), the Acquisition Program Baseline (APB), the Implementation Strategy and
  Planning Document (ISPD), and the Program Management Plan (PMP). Each checklist
  carries the same header fields — document title, revision, and date — and the
  same three working columns: the method(s) used, the artifact(s) that evidence
  the check, and free-text comments.

- **The Method-code legend.** A footnote shared across all four checklists
  assigns each permitted method a single-letter or short code. The codes are:
  `I` for Inspection, `P` for Peer Review, `A` for Audit, `C` for Checklist,
  `D` for Discussion, `U` for User Survey, `F` for Functional Presentation,
  `W` for Walk-through/dry run, `An` for Analysis, `T` for Testing, `Dem` for
  Demonstration, and `M` for Modeling. This legend is the bridge between the
  checklists in Appendix B and the definitions in Appendix C.

- **The Artifact definition.** Also footnoted on every checklist: an artifact is
  defined as an objective, authenticated record evidencing a V&V action or its
  outcome — examples given include a validation table, a report, a traceability
  matrix, meeting minutes, the completed checklist itself, survey results, or an
  email.

- **Appendix C — Definitions.** A glossary that defines each verification method
  named in the legend (and a few adjacent terms), giving the chapter its
  shared vocabulary for what a method actually entails in practice.

## Key Concepts

**Document-specific checklists, common skeleton.** Although the four checklists
target different documents, they share a deliberate structure. Each opens by
confirming the document conforms to the relevant FAA template (and, for the PRD,
to the standards in the System Engineering Manual). Each then walks the
document's substantive content, and each closes by asking that the content be
validated by the appropriate stakeholders. This template-then-content-then-
stakeholder pattern repeats across all four.

**Critical Performance Requirements as the through-line.** CPRs surface in three
of the four checklists and tie them together. The PRD checklist asks that CPRs be
identified and meet CPR criteria. The APB checklist asks that the CPRs be
identified and consistent with those already in the PRD, and that the approved
CPRs were obtained from the PRD with each requirement clearly stated and each
carrying its associated value. The ISPD checklist asks that program management
controls cover the tracking and management of CPRs. Consistency of CPRs across
documents is treated as a first-class review target, not an afterthought.

**The requirement-quality criteria.** The PRD checklist spells out what a good
requirement looks like, asking that each one be clearly stated, unambiguous,
complete, necessary and traceable, verifiable/measurable/testable, and solution
independent — with achievability against current or emerging technology checked
for the final PRD (fPRD) specifically. It also asks that requirements be complete
against named upstream sources: the Enterprise Architecture, the Solution Concept
of Operations, the Functional Analysis Report, the Enterprise Architecture
Shortfall Analysis, the Investment Analysis Assessments (fPRD only), and other
applicable specifications such as the NAS-RD-2010 and NAS-RD-2025 standards.

**Stakeholder validation across engineering domains.** Each checklist names the
domains that must sign off. For the PRD, stakeholders validate performance,
supportability, safety, security, interfaces, human factors, transition, and
reliability/maintainability/availability. The ISPD and PMP carry parallel lists
for engineering approaches and work breakdown structure respectively —
hardware, software, RMA, configuration management, interfaces, human factors,
maintenance, safety, security, test and evaluation, and production. The recurring
appearance of safety, security, and human factors across documents signals these
are non-negotiable review dimensions throughout the lifecycle.

**Method then evidence.** The two mandatory columns — method used and artifact
identified — encode a discipline: it is not enough to assert a check passed; the
reviewer must state how it was verified and where the proof lives. The artifact
definition closes the loop by insisting that proof be an authenticated, objective
record.

**The method glossary distinctions.** Appendix C draws fine distinctions between
methods that are easy to conflate. Analysis compares a design against known
scientific and technical principles, data, or established practice to confirm it
will meet the requirement. Inspection relies on visual observation, mechanical
measurement, or technical examination of supporting documentation. Demonstration
is a qualitative rather than quantitative confirmation made during a dynamic test
— and the source notes that software functional requirements are typically
validated by demonstration because functionality must be observed through a
secondary medium. Testing operates the system under specified conditions, records
results, and evaluates an aspect of the system. Audits are independent
examinations of work products for compliance, extended to independent review of
records and activities to test the adequacy of data security and integrity
procedures. Peer reviews are structured, methodical examinations of a completed
draft by unbiased SMEs who are independent of the work product's development and
approval.

**The softer methods are still methods.** The glossary legitimizes lighter-weight
techniques by defining them precisely: modeling builds programs that represent
the effects of a postulated environment; simulation is a model that behaves like
the system when given controlled inputs; storyboarding is a sequenced graphic
arrangement used to visualize a concept; functional presentations show the
hierarchical arrangement of functions and interfaces as a complete behavioral and
performance view; user surveys gather information from individuals through
questionnaires, telephone, mail, in person, or web; and walk-throughs/dry runs
rehearse a process or procedure before the real execution to mitigate a possible
failure. Accreditation is defined separately: it is the formal sign-off
certifying that a given test capability is acceptable for one specific use.

## Mental Models

**The checklist as a contract between reviewer and record.** Reading down a
checklist, every row is a claim the reviewer must back with two things: a method
and an artifact. Think of the method column as "how did you look" and the artifact
column as "where can I look too." A checklist with passing rows but empty evidence
columns is, by the source's own definition, incomplete — the artifact is the part
that survives the meeting.

**A vocabulary ladder from acronym to method.** The three appendices form a
descent: Appendix A resolves the abbreviation, Appendix B's legend maps the
single-letter code to a named method, and Appendix C tells you what that method
demands of you. When you encounter "Dem" in a filled-out checklist, you walk the
ladder — code to name (Demonstration) to definition (a dynamic, qualitative
confirmation).

**Consistency as a cross-document property.** Because the APB pulls its CPRs from
the PRD and the ISPD must support the concepts and requirements in the EA and PRD,
the reviewer's job is partly to verify each document and partly to verify
agreement between documents. The mental model is a set of nested documents that
must not contradict one another — a change in the PRD ripples into the APB and
ISPD, and the checklists exist partly to catch the ripple.

**Authoring seams are review targets.** Two of the checklists explicitly flag the
risk that arises when different individuals author different sections — they ask
the reviewer to ensure all sections are consistent and cohesive in approach and
direction, noting this matters most when authorship is split. The seam between
authors is treated as a likely defect site.

## Key Takeaways

- The appendices convert the guideline into a usable bench reference: a glossary
  (A), four document checklists (B), and a methods dictionary (C).
- Every checklist row demands two things beyond a pass/fail: the method used and
  the artifact that evidences the outcome. An artifact must be an objective,
  authenticated record.
- The four checklists target the PRD, APB, ISPD, and PMP, and all share a
  template-conformance → content → stakeholder-validation skeleton.
- Critical Performance Requirements are a deliberate through-line: identified in
  the PRD, carried consistently into the APB, and tracked through the ISPD.
- The PRD checklist encodes the requirement-quality bar — clear, unambiguous,
  complete, necessary/traceable, verifiable, solution-independent, and (for the
  fPRD) achievable with current or emerging technology.
- Appendix C makes the method choices precise: analysis vs. inspection vs.
  demonstration vs. testing are distinct acts, and the source notes software
  functional requirements lean on demonstration because behavior is observed
  through a secondary medium.
- Split authorship of a document is named as a consistency risk the reviewer must
  actively check.

## Connects To

- **The lifecycle V&V process chapters of this pack.** The acronyms and method
  legend resolve the shorthand used when the body of the guideline walks each AMS
  phase; the appendices are the back-of-book key to that narrative.
- **AMS investment decision milestones.** Acronyms such as IID, FID, ISD, IARD,
  and CRDRD tie the checklists to the gated decision points where the program
  documents (PRD, APB, ISPD, PMP) are produced and reviewed.
- **Requirements engineering practice.** The PRD requirement-quality criteria
  (unambiguous, traceable, verifiable, solution-independent) align with the
  general requirements-writing canon and with traceability-matrix discipline.
- **The broader systems-engineering V&V canon (e.g., the 15288 process family and
  SEBoK V&V material).** The Appendix C method definitions — analysis, inspection,
  demonstration, testing — are the same four classical verification methods used
  across the SE discipline, here given an FAA-specific framing.
- **CMMI.** The acronym appears in Appendix A (Capability Maturity Model
  Integration) as part of the acquisition vocabulary, signposting the
  process-maturity context in which these reviews sit, without the appendices
  themselves elaborating the model.
- **Configuration management and traceability.** The artifact examples — the
  traceability matrix, validation table, and completed checklist — connect the
  evidence discipline here to CM records kept across the program.
