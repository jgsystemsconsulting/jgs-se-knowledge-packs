# Chapter 3: Software requirements specifications

Sources: S5 Regulatory Guide 1.172, "Software Requirement Specifications for Digital Computer Software and Complex Electronics Used in Safety Systems of Nuclear Power Plants" (Rev. 1, July 2013, ML13007A173), C. STAFF REGULATORY GUIDANCE §§1-7, lines 288-536 of `sources/text/S5.txt` (printed pp. 6-9). Exclusions per pin: cover, Purpose-of-RGs/Paperwork plates, D. IMPLEMENTATION, and REFERENCES. Name-only standards cited with edition as printed: IEEE Std. 830-1998 (endorsed by RG 1.172 with the clarifications in C); IEEE Std. 610.12-1990 (definitions source named by IEEE Std. 830-1998 Clause 3); IEEE Std 603-1991 (design-basis trace target named in C.2.g); IEEE Std 7-4.3.2-2003 (abnormal conditions and events path named via RG 1.152 in C.6.a); IEEE Std. 828-2005 (configuration item path via RG 1.169 in C.3); IEEE/EIA Std. 12207.1-1997 (named only as not endorsed, Annex B). Adjacent RG 1.152 and RG 1.169 named only where the source points to them for SDOE attributes and change control.

## Core Idea

RG 1.172 states the staff method for preparing software requirements specifications (SRSs) for digital computer software used in nuclear power plant safety systems, including complex electronics covered by the guide's title. IEEE Std. 830-1998 is the endorsed approach for meeting 10 CFR Part 50 SRS expectations, subject to the exceptions and additions in the regulatory positions. The chapter is the qualities and control rules an SRS must satisfy, not a template dump of clause text from the standard.

The staff positions walk definitions, the characteristic set of an acceptable SRS, change control, incomplete entries, when design-specific material belongs in the SRS, software attributes of special interest for safety systems, and which annexes are or are not endorsed. Traceability, completeness (including timing), internal and external consistency, verifiability, and forward links into design and V&V materials are the recurring tests.

## Frameworks Introduced

- **IEEE Std. 830-1998 with nuclear positions (S5 C lead-in).** The standard is acceptable for 10 CFR Part 50 SRS preparation when the guide's exceptions and additions are applied. Cited criteria are Appendix A or B to 10 CFR Part 50 unless noted.
- **Definitions clarifications (S5 C.1).** Clause 3 of IEEE Std. 830-1998 points at IEEE Std. 610.12-1990 for technical terms. Baseline uses meaning (1) of that glossary, and "formal review and agreement" means responsible management has reviewed and approved the baseline. Interface uses all four glossary variations by context; meaning (1), a shared boundary across which information is passed, is read broadly under Appendix B Criterion III to include design interfaces between participating design organizations.
- **Acceptable SRS characteristics, nuclearized (S5 C.2).** Clause 4.3's characteristic set is retained with the opening sentence restated as "An SRS should be...." and with safety-system clarifications on each trait the guide addresses.
- **Traceability and accuracy of representations (C.2.a).** When specification or representation tools are used (Subclauses 4.3.2.2 and 4.3.2.3), traceability stays intact between those representations and the natural-language software requirements derived from system requirements and system safety analyses, satisfying GDC 1.
- **Completeness for safety system software (C.2.b).** Functional requirements specify how functions are initiated and terminated and the system status at termination. Each input and output variable carries accuracy requirements including units, error bounds, data type, and data size. Variables controlled or monitored in the physical environment are fully described, and expressly prohibited functions are stated. Timing is called out as particularly important: functions with timing constraints are identified with criteria for each mode; timing requirements are deterministic and cover normal and anticipated failure conditions.
- **Consistency means internal and external (C.2.c).** IEEE Std. 830-1998 Subclause 4.3.4 limits "consistency" to internal consistency and treats external inconsistency as incorrect specification. The NRC uses both senses: external consistency with associated software and system products (including safety system requirements and design), and internal consistency so no requirement conflicts with another inside the SRS.
- **Ranking for importance or stability (C.2.d).** Requirements important to safety are identified as such. IEEE Std. 830-1998's essential / conditional / optional degrees of necessity do not justify parking unnecessary requirements on safety system software; unnecessary requirements should not be imposed. Documented variations in essential requirements link to site or equipment variations or to specific plant design bases and regulatory provisions (GDC 20 among others is named for protection-system function).
- **Verifiability (C.2.e).** Where the standard recommends removing or revising unverifiable requirements, the NRC position is that all requirements should be verifiable and should be modified or restated until each one can be verified.
- **Modifiability and glossary discipline (C.2.f).** Modifiability ties to style (form, structure, modularity), readability, and understandability. Precise definitions of technical terms live in the SRS or in a glossary.
- **Bidirectional traceability (C.2.g).** Under GDC 1 and Subclause 4.3.8, each identifiable requirement is backward traceable to a higher-level requirements specification and ultimately to system licensing (regulatory requirements satisfied) and design bases (example given: IEEE Std 603-1991 Clause 4). Each requirement is written so it is also forward traceable to subsequent design outputs (SRS to software design and software design to SRS). Forward traceability extends to documents derived from the SRS, including V&V materials: each requirement traces to the inspections, analyses, or tests that confirm it.
- **Unambiguity across the document set (C.2.h).** Subclause 4.3.2's one-interpretation rule applies; because software requirements are generally derived from associated products such as safety system requirements, the SRS plus those associated documents together must be unambiguous.
- **Change control for the SRS (S5 C.3).** Subclause 4.5(b) baselining and formal change control may be met by a procedure unique to IEEE Std. 830-1998 or by placing the SRS under a general software configuration management program as a configuration item. RG 1.169 describes SCM and endorses IEEE Std. 828-2005 for that path.
- **Incomplete entries still bound (S5 C.4).** Any incomplete SRS entry (including "to be determined" or "TBD" per Subclause 4.3.3.1) must still describe the applicable design bases and the commitments to standards or regulations that govern the final determination of that entry.
- **Design-specific content when required (S5 C.5).** Subclause 4.7's preference to omit module partitioning, function allocation, and information flow yields when security or safety exceptions apply. Independence, separation, diversity, and defense in depth, when required by the safety system design bases or by regulation, belong in the SRS and should be described there.
- **Software attributes of interest (S5 C.6).** Subclause 5.3.6 attributes that matter for safety system software include safety, secure analysis, and robustness. Safety requirements important to safety are derived from system requirements and safety analyses, marked as such, and include considerations from the safety analysis report and abnormal conditions and events as in IEEE Std 7-4.3.2-2003 (RG 1.152). Subclause 5.3.6.3 "Security" is not endorsed as sufficiently detailed for SRS security attributes; a security attribute remains useful, but specific factors come from other guidance, notably the secure development and operational environment (SDOE) guidance in RG 1.152, which can supply the needed SRS attributes. Robustness requires fault-tolerance and failure-mode requirements for each operating mode, full specification of behavior under unexpected, incorrect, anomalous, or improper input, hardware behavior, or software behavior, requirements to respond to hardware and software failures including analysis of and recovery from computer system failures, and requirements for online inservice testing and diagnostics.
- **Annex endorsement map (S5 C.7).** Annex A (SRS templates) is not endorsed; licensees may use it only as an example, and outline-use directions such as those in Clause 5.3.7 are advisory only. Annex B (guidelines for compliance with IEEE/EIA 12207.1-1997) is not endorsed because the agency does not endorse that IEEE/EIA standard.

## Key Concepts

- **SRS is a controlled quality object.** Characteristics are not style tips; they are the acceptance shape of the specification for safety system software and complex electronics under this guide.
- **Natural language remains the trace spine.** Tool representations stay tied to natural-language requirements drawn from system requirements and system safety analyses.
- **Initiation, termination, and end state.** Completeness for functions includes how they start, how they stop, and system status when they stop.
- **Accuracy is per variable.** Units, error bounds, data type, and data size are part of the requirement, not optional annotation.
- **Deterministic timing across modes and failures.** Timing criteria cover each mode and anticipated failure conditions, not only the happy path.
- **External consistency is in scope.** Agreement with safety system requirements and design is required, not only freedom from internal contradiction.
- **No optional baggage on safety software.** Conditional or optional necessities from the standard do not authorize unnecessary requirements; variations of essentials are explained against plant bases.
- **Every requirement verifiable.** Unverifiable text is rewritten until verification is possible; deletion of the need is not the first move.
- **Backward to licensing and design bases; forward to design and V&V.** Traceability is a chain, not a single upward pointer.
- **Baselined under CM.** Change control is either SRS-specific or the general SCMP configuration-item path from RG 1.169 / IEEE Std. 828-2005.
- **TBD is not a blank check.** Incomplete entries still cite the design bases and regulatory or standards commitments that will close them.
- **Safety architecture features can be requirements.** Independence, separation, diversity, and defense in depth enter the SRS when the design basis or regulation requires them.
- **SDOE carries security attributes.** The guide declines to endorse the standard's thin security subclause as sufficient detail and points to RG 1.152 SDOE guidance instead.
- **Robustness includes failure behavior and online diagnostics.** Unexpected inputs and hardware/software misbehavior are specified, with recovery and inservice test requirements.
- **Templates are examples only.** Annex A is not an endorsed fill-in form.

## Mental Models

- **Characteristics before outline.** Judge an SRS by traceability, completeness, consistency, ranking, verifiability, modifiability, and unambiguity before arguing section order.
- **Two directions of trace.** Up to regulatory and design bases; down and across to design outputs and to the inspections, analyses, or tests that prove each requirement.
- **Safety marking is explicit.** Importance to safety is labeled in the SRS, not inferred later by the reader.
- **CM is how the SRS stays true.** Baseline plus formal change control, often via the SCMP, keeps the specification synchronized with the rest of the configuration.
- **Design silence is the default; design mandate is the exception.** Partitioning and allocation stay out unless safety or security design bases force them in.
- **Security attributes ride SDOE, not a thin subclause.** When the standard's security text is too thin, RG 1.152 supplies the attribute source the SRS can cite.
- **Complex electronics share the SRS discipline.** The guide title brings complex electronics into the same specification expectations as digital computer software for safety systems.

## Anti-patterns

- **Tool diagrams or formal representations with no trace back to natural-language requirements and system safety analyses.** C.2.a rejects orphan representations.
- **Functions specified without initiation, termination, end-state status, or prohibited behavior.** C.2.b completeness fails.
- **I/O variables without units, error bounds, type, or size.** Same completeness rule.
- **Non-deterministic or mode-blind timing.** Timing must be deterministic per mode, including anticipated failures.
- **Internal-only consistency checks that ignore mismatch with safety system requirements or design.** C.2.c external consistency is required.
- **Loading conditional or optional requirements that are unnecessary for acceptability of safety system software.** C.2.d.
- **Leaving unverifiable requirements in place.** C.2.e demands restatement until verification is possible.
- **Undefined technical terms scattered through the SRS.** C.2.f wants precise definitions in-document or in a glossary.
- **Requirements that cannot be walked backward to licensing/design bases or forward to design and V&V confirmation methods.** C.2.g.
- **SRS that is clear alone but ambiguous when read with the parent safety system requirements.** C.2.h.
- **Uncontrolled SRS edits outside baseline change control or SCMP configuration-item discipline.** C.3.
- **TBD entries with no governing design basis or regulatory commitment.** C.4.
- **Omitting required independence, separation, diversity, or defense-in-depth features from the SRS when the design basis demands them.** C.5.
- **Safety-important requirements not identified as such, or security attributes invented without SDOE grounding.** C.6.a-b.
- **No fault-tolerance, failure-mode, unexpected-input, recovery, or online diagnostic requirements.** C.6.c robustness gap.
- **Treating Annex A templates or Annex B 12207 mapping as endorsed staff positions.** C.7.

## Key Takeaways

1. RG 1.172 endorses IEEE Std. 830-1998 for safety system SRSs (software and complex electronics) with nuclear-specific clarifications; standard body text is not reproduced here.
2. Baseline means management-approved; interface includes design interfaces among participating organizations under Criterion III.
3. An acceptable SRS is traceable and accurate in its representations, complete (initiation/termination/status, per-variable accuracy, physical variables, prohibited functions, deterministic multi-mode timing), consistent internally and externally, explicit about safety importance, fully verifiable, modifiable through clear style and defined terms, bidirectionally traceable to bases and to design/V&V, and unambiguous with its associated documents.
4. The SRS is baselined under formal change control, either dedicated or as an SCMP configuration item per RG 1.169 / IEEE Std. 828-2005.
5. Incomplete (TBD) entries still state the design bases and standards or regulatory commitments that will finish them.
6. Design-specific content such as independence, separation, diversity, and defense in depth belongs in the SRS when required by design bases or regulation.
7. Safety, SDOE-grounded security attributes (RG 1.152), and robustness (fault tolerance, failure behavior, recovery, online diagnostics) are the attribute set called out for safety system software; IEEE Std 7-4.3.2-2003 abnormal conditions and events feed safety requirements via RG 1.152.
8. Annex A templates and Annex B IEEE/EIA 12207.1-1997 mapping are not endorsed staff methods.
9. Forward trace from each requirement into confirming inspections, analyses, or tests is part of the traceability duty, not an optional V&V courtesy.
10. Unnecessary requirements stay out; variations of essential requirements are tied to site, equipment, design basis, or regulatory provisions.

## Connects To

- **ch01** - where RG 1.172 sits among the six life cycle guides and how SRS questions route here rather than to V&V or test guides.
- **ch02** - life cycle processes and the Software Safety Plan expectation that appropriate safety requirements appear in the SRS.
- **ch04** - configuration management that baselines the SRS and controls changes to it.
- **ch05** - V&V and reviews that consume forward traces from SRS requirements into inspections, analyses, and tests.
- **ch06** - test documentation and unit testing that carry confirmation methods linked from requirements.
- **ch07** - B.3.3.1 Software Requirements Specification design-output review against the qualities this chapter sets.
- **ch08** - name-only map for IEEE Std. 830-1998, 603-1991, 7-4.3.2-2003, 828-2005, and related excluded material.
