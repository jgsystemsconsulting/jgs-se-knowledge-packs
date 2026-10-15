# Chapter 3: Software Validation Principles

Sources: S2 General Principles of Software Validation (2002-01-11), §§ 1–5 and 3.1.2 (purpose, scope, verification vs validation, ten principles, life-cycle activities and tasks). **Authority note:** S2 Section 6 (Validation of Automated Process Equipment and Quality System Software) is superseded by S3 Computer Software Assurance (see ch04); remaining S2 sections continue as FDA current thinking on device software validation (confirmed in S2 front matter and S3 Scope).

## Core Idea

Software validation is not a final test event and not a stack of scripts produced after coding. Under the Quality System regulation (and the QMSR frame that incorporates ISO 13485), design validation includes software validation and risk analysis where appropriate. S2 defines software validation as confirmation, by examination and objective evidence, that software specifications conform to user needs and intended uses, and that requirements implemented through software can be consistently fulfilled. Verification is the phase-by-phase cousin: objective evidence that design outputs of a life-cycle phase meet that phase's specified requirements. Together they run through an established software life cycle, scaled to complexity and safety risk, with plans, procedures, independent review, and re-validation after change. Read S2 for **device software** (software that is a device, or a component/part/accessory of a device) and for the engineering principles that still inform development. For **production and quality-management system software**, stop at the edge of Section 6 and switch to CSA (ch04).

## Frameworks Introduced

- **Verification vs validation (3.1.2)**: verification checks phase outputs against phase requirements (inspections, walkthroughs, static/dynamic analysis, testing, and similar). Validation checks the software against user needs and intended use, as part of finished-device design validation, with evidence built throughout the life cycle rather than only at the end.
- **Ten principles (Section 4)**: requirements baseline; defect prevention over "test quality in"; time and effort from planning onward; life-cycle context; plans define *what*; procedures define *how*; re-validation and regression after change; coverage scaled to complexity and safety risk; independence of review; flexibility with retained manufacturer responsibility.
- **Life-cycle activities and tasks (Section 5)**: quality planning; requirements; design; construction/coding; developer testing; user site testing; maintenance and software changes. S2 does not mandate a single life-cycle model; it requires that a model be chosen and used.
- **Scope split with CSA**: S2 still speaks to medical device software and to software used to design, develop, or manufacture devices at the level of general principles. **Section 6 only** (automated process equipment and quality system software validation detail) is superseded by S3 CSA. ch04 owns that replacement framework.

## Key Concepts

- **Regulatory hook.** Software validation is a Quality System requirement. Premarket review often needs software-related design-control evidence to evaluate safety and effectiveness, but the standing duty is the quality system, not the marketing file alone. QMSR (effective 2026-02-02) keeps software validation obligations in the ISO 13485-based part 820 structure; see ch05 for QMSR mechanics.
- **Applicability spectrum (4.10).** FDA-regulated applications include software that is a component/part/accessory of a device, software that is itself a device, and software used in manufacturing, design and development, or other quality-system roles. Principles apply across that spectrum; intensity follows risk. Production/QMS *how-to* now follows CSA.
- **Requirements are the baseline (4.1).** A documented software requirements specification is necessary for both verification and validation. Without established requirements, validation cannot be completed. Requirements work is design-input work, not an optional binder section.
- **Defect prevention (4.2).** Quality focus belongs on keeping defects out of the process. Testing is necessary and limited; most software cannot be exhaustively tested. Use a mix of prevention and detection methods matched to environment, language, size, and risk.
- **Start early (4.3).** Preparation begins in design and development planning and design input. The conclusion that software is validated rests on evidence collected from planned efforts across the life cycle, not on a single end-stage protocol.
- **Life cycle is the environment (4.4).** Validation sits inside chosen software engineering tasks and documentation. Specific V&V tasks should match intended use. Waterfall, iterative, or other models are sponsor choices; absence of any model is not.
- **Plans and procedures (4.5–4.6).** Plans set scope, approach, resources, schedule, and extent of activities. Procedures set the sequence of actions to finish those activities. Plans without procedures, or procedures without a plan, both fail the quality-system tool test.
- **Validation after change (4.7).** Small local edits can have global impact. Any software change requires analysis not only of the change itself but of extent and impact on the whole system, then appropriate regression testing of unchanged but vulnerable portions. Design controls plus regression rebuild confidence after change.
- **Coverage follows risk, not headcount (4.8).** Choose activities commensurate with design complexity and safety risk of the intended use. Lower risk may justify baseline activities; higher risk adds activities. Documentation must show plans and procedures completed successfully. Firm size and budget are not coverage drivers.
- **Independence of review (4.9).** Self-validation is weak. Prefer evaluators not invested in the particular design implementation. Third parties or internal staff with knowledge but without implementation ownership both work. Small manufacturers still need creative separation of build and check roles for higher-risk work.
- **Flexibility and responsibility (4.10).** Implementation differs by application; the manufacturer or specification developer remains responsible for demonstrating validation even when tasks are distributed across vendors, OTS components, or multiple sites.
- **What verification looks like in practice.** Reviews, traceability analyses, architecture and detailed-design evaluations, code inspection, and testing that confirms outputs meet inputs for that phase. Testing is one verification technique among several.
- **What validation looks like in practice.** Evidence that all software requirements are implemented correctly and completely and trace to system requirements; simulated-use testing; user site testing as part of overall design validation for a software-automated device. The validated conclusion depends on the cumulative verification record plus these confirmation activities.
- **Developer testing vs user site testing (5.2.5–5.2.6).** Developer testing (unit through system as appropriate) builds the technical case. User site testing challenges the product in the environment of use as part of design validation. Neither fully replaces the other for device software with real users and environments.
- **Maintenance is still validation (5.2.7).** Post-release changes re-enter analysis, regression, and documentation. Pair with ch10 when the device is 510(k)-subject and the question is whether a new premarket file is needed; validation duty exists either way.
- **OTS and supplied software.** Principles still apply when components come from outside. Manufacturer responsibility does not transfer to the vendor invoice. Deeper OTS submission expectations sit in ch08; production-software supplier evidence also appears in CSA (ch04).
- **IQ/OQ/PQ vocabulary.** S2 discusses installation/operational/performance qualification language used in process validation contexts. For automated production equipment and quality-system software, do not stretch S2 Section 6; use CSA's assurance framework instead.
- **Least burdensome reading.** S2 endorses least-burdensome compliance paths. Least burdensome still means objective evidence matched to risk, not empty templates.

## Mental Models

- **Build the right thing, and build the thing right.** Validation targets user needs and intended use (right thing). Verification targets phase specifications (thing built right). You need both.
- **Evidence accumulation, not a gate ceremony.** Early planning, requirements, reviews, and incremental tests are the validation case. A final script pile without that history is theatre.
- **Risk sets the dial.** Complexity and safety risk turn coverage up or down. Schedule pressure does not.
- **Change breaks the seal.** Every edit reopens validation analysis; regression scope follows impact, not hope.
- **Device software reads S2; production software reads S3.** Same industry, different chapters after the Section 6 handoff.

## Anti-patterns

- **Equating "we ran the protocol" with "software is validated."** Protocols without a requirements baseline, life-cycle verifications, and intended-use challenge are incomplete.
- **Testing quality in at the end.** S2 calls this out directly: testing alone rarely establishes fitness for intended use.
- **Skipping independence on high-risk code.** Authors marking their own homework is the failure mode independence exists to prevent.
- **Ignoring global impact of a "one-line" fix.** Change analysis and regression are mandatory thought steps.
- **Using firm size to justify thin coverage on high-severity software.** Coverage tracks risk, not headcount.
- **Applying obsolete Section 6 recipes to MES, eQMS, LIMS, or spreadsheet-controlled processes.** Those paths moved to CSA (ch04).
- **Outsourcing development and outsourcing responsibility.** Vendors can perform tasks; the manufacturer still owns the validated state.
- **Life-cycle model cosplay.** Naming Agile or V-model in a procedure while skipping requirements control, change analysis, or regression is not compliance with S2 principles.

## Key Takeaways

1. Software validation confirms, with objective evidence, that specifications meet user needs and intended uses and that implemented requirements can be fulfilled consistently; it is part of design validation for finished devices.
2. Software verification confirms phase outputs against phase requirements and feeds the validation conclusion; testing is one verification activity among several.
3. The ten Section 4 principles (requirements, defect prevention, early effort, life cycle, plans, procedures, change, risk-based coverage, independence, flexibility/responsibility) are the standing mental checklist for device software.
4. Validation coverage scales with software complexity and safety risk, not with resource slogans.
5. Any software change requires impact analysis and appropriate regression before the software is again considered validated.
6. Section 5 life-cycle tasks (planning through maintenance) structure the work; no single life-cycle model is mandated.
7. **S2 Section 6 is superseded by S3 CSA** for automated process equipment and quality-system software; use ch04 for that scope. Remaining S2 sections remain current thinking for device software validation principles.
8. Premarket documentation depth for device software functions is S1 (ch02); this chapter is the validation-engineering substrate those artifacts should rest on.

## Connects To

- **ch02**: premarket software documentation elements that present verification and validation evidence.
- **ch04**: CSA risk-based assurance replacing S2 Section 6 for production and QMS software.
- **ch05**: QMSR structure that carries design-control and validation obligations after 2026-02-02.
- **ch08**: OTS software validation and maintenance evidence expectations.
- **ch10**: when a validated software change also needs a new 510(k).
- **ch01**: orientation map placing validation beside pathway and documentation choices.
