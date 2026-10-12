# Chapter 10: Software Changes and the 510(k) Trigger

Sources: S9 Deciding When to Submit a 510(k) for a Software Change to an Existing Device (2017-10-25), §§ I–VI and Figure 1 (guiding principles, flowchart questions, documentation, common change types).

## Core Idea

A software or firmware change to an existing 510(k)-subject device is not a gut call and not a pure engineering preference. 21 CFR 807.81(a)(3) requires a new premarket notification when a change could significantly affect safety or effectiveness (including significant design or manufacturing changes) or is a major change in intended use. S9 turns that threshold into a least-burdensome decision sequence: run a risk-based assessment, walk the flowchart questions in order, confirm the answer with verification and validation results, and document either a new 510(k) or a reasoned decision to stay put. Both outcomes are records. The quality system still owns every change whether or not FDA sees a new file.

## Frameworks Introduced

- **When-to-submit decision sequence (Figure 1)**: ordered questions that route each software change to "new 510(k)" or "document" (meaning a new 510(k) is likely not required, so record the analysis for later reference).
- **Guiding Principles (ten)**: standing rules that sit beside the flowchart: intent to affect safety or effectiveness, initial risk-based assessment, unintended consequences, use of risk management concepts, role of testing, simultaneous and cumulative changes, the correct comparative device, documentation, what to put in a new 510(k) for a modified device, and the reminder that filing does not guarantee substantial equivalence.
- **Risk-based assessment (S9 term)**: analysis of whether the change could significantly affect safety or effectiveness, positively or negatively. It borrows hazard and harm language from recognized risk-management practice, but it deliberately also covers effectiveness, not safety alone.
- **Original device baseline**: compare the changed device to the manufacturer's own most recently cleared 510(k) configuration, preamendments device (if never subsequently cleared), or De Novo-authorized device (if never subsequently cleared). That baseline is not the same as choosing a new predicate for substantial equivalence.
- **QS documentation duty**: every device change still runs through 21 CFR part 820 design and production change controls and record-keeping, including when the flowchart ends at "document."

## Key Concepts

- **Scope of S9.** The guidance covers software (including firmware) changes to 510(k)-cleared devices, other devices subject to 510(k) requirements (preamendments devices), and devices that received De Novo classification when later changes are judged under 510(k) rules. It is not a new policy rewrite; it makes the existing "when to submit" logic more predictable for software.
- **Regulation threshold.** A new 510(k) is required when the change could significantly affect safety or effectiveness, or is a major change or modification in intended use. "Could" is the operative word: successful routine testing does not erase a risk-based conclusion that the change could matter.
- **Principle 1, intent.** If the manufacturer modifies the device with the intent to significantly affect safety or effectiveness (for example to improve clinical outcomes, mitigate a known risk, or respond to adverse events), a new 510(k) is likely required, regardless of later flowchart branches. Changes not intended to have that effect still need evaluation for what they could do.
- **Principle 2, initial risk-based assessment.** Identify and analyze new risks and changes to existing risks from the modification, and reach an initial submit-or-not decision before leaning on slogans about "minor release."
- **Principle 3, unintended consequences.** Software changes often pull secondary effects (an OS upgrade that forces driver and embedded-code changes). Assess the whole consequence set, not only the ticket title.
- **Principle 4, risk concepts for software.** Use hazard, hazardous situation, risk estimation, risk control, and related ideas. Software failures are often systematic; when probability of software failure cannot be estimated usefully, estimate risk from severity of harm alone.
- **Principle 5, testing confirms, it does not override.** If the initial assessment says no new 510(k), successful routine verification and validation should confirm that. Unexpected V&V results send the manufacturer back through the flowchart. If the risk-based assessment already says the change could significantly affect safety or effectiveness, a clean test report does not remove the 510(k) duty. Design control V&V still applies either way.
- **Principle 6, simultaneous changes.** Evaluate each change separately and in aggregate. Individual source lines are not automatically each a separate "change."
- **Principle 7, cumulative effect.** Many small changes can stay inside QS until their combined effect against the original device crosses the regulatory threshold. Each new change is still judged against the original device, not against the last undocumented tweak.
- **Principle 8, documentation.** Establish the decision process inside the manufacturer's quality system. Scope of records varies, but the submit-or-document reasoning is part of design control evidence and must be available to FDA on inspection.
- **Principle 9, contents of a new 510(k) for a modified device.** Describe every change that triggers the new submission, and also describe other changes since the last cleared 510(k) that would have appeared in a first 510(k) for that device (for example labeling warnings). Independent non-triggering changes may ship immediately if they do not depend on the triggering change; they still get QS documentation and should appear in the new 510(k) narrative.
- **Principle 10, SE not guaranteed.** Following S9 and filing does not assure a substantial equivalence determination.
- **Flowchart Question 1, cybersecurity-only strengthen.** Is the change made solely to strengthen cybersecurity with no other impact on the software or device? Often no new 510(k). Still perform analysis, verification, and/or validation so the change does not harm safety or effectiveness. Any incidental impact forces the remaining questions. Pair with the separate cybersecurity guidances for content expectations.
- **Flowchart Question 2, restore to cleared specification.** Is the change solely to return the system to the specification of the most recently cleared device? Often no new 510(k), but still evaluate risk and performance impact. If the work updates missing, incomplete, ambiguous, or conflicting requirements in a way that drives new code beyond pure restoration, answer is likely "no" and continue. Clarifying specification text without code or performance-specification changes generally stays out of a new 510(k), with design-control impact still assessed.
- **Flowchart Question 3a, new or modified risk of significant harm.** Does the change introduce a new risk or modify an existing risk that could result in significant harm and that is not effectively mitigated in the most recently cleared device? "Risk" here covers hazard, hazardous situation, or cause. Significant harm means serious or worse (injury needing professional intervention, permanent impairment, or death), judged pre-mitigation. All three criteria must hold for a likely new 510(k): (1) new or modified hazard/hazardous situation/cause in the risk file, (2) serious-or-worse harm level, (3) not already effectively mitigated on the cleared device. Existing controls can cover new causes; absence of effective controls meets criterion 3.
- **Flowchart Question 3b, risk control changes.** Does the change create or require a new risk control, or modify an existing risk control, for a hazardous situation that could result in significant harm? New or changed controls needed to prevent significant harm likely need a new 510(k). Redundant or enhanced controls on top of controls that already mitigated the situation on the cleared device often do not.
- **Flowchart Question 4, clinical functionality or performance specifications.** Could the change significantly affect clinical functionality or performance specifications tied directly to intended use (speed, strength, response time, throughput, limits, reliability, delivery rate, assay performance, and similar)? If yes, a new 510(k) is likely required. For IVDs, include clinically significant impact on clinical decision-making, and judge analytical and clinical performance against the cleared claims. Pure indications-for-use or intended-use changes belong in the companion general device-change guidance, not this software flowchart alone.
- **Common change types that still need careful judgment (Section VI).** Infrastructure changes (compiler, language, drivers, libraries), architecture changes (new OS, new hardware platform support, middleware), core algorithm changes (including full rewrites that keep nominal claims), clarification of requirements with no functionality change, cosmetic changes with no clinical-use impact, reengineering, and refactoring. Modular architecture lowers the chance of unintended cross-impact; loose architecture raises it. Significant V&V script rewrites can signal infrastructure shifts worth examining. Minor maintainability refactoring inside specification often stays off a new 510(k); broad rewrites that touch performance or risk controls often do not.
- **How to read flowchart endpoints.** "New 510(k)" means submission is likely required. "Document" means a new 510(k) is likely not required: write the analysis down and keep it. Uncertainty should be rare if principles, questions, and examples are used together; gray areas can be taken to the reviewing division.

## Mental Models

- **Presumption of assessment, not presumption of filing.** Every software change gets the sequence. Many legitimate outcomes are "document and file internally."
- **Intent and effect are separate gates.** Wanting a safety improvement can force a filing even before Q3/Q4. Not wanting an effect never excuses skipping the could-it-affect analysis.
- **Baseline is your last authorized device.** Drift accumulates against that baseline. Comparing only to yesterday's unofficial build hides cumulative trigger conditions.
- **V&V is a witness, not a pardon.** Clean tests support a no-file decision already reached; they do not cancel a "could significantly affect" finding.
- **Cyber patches are special-cased, not exempt from thinking.** Sole cybersecurity hardening often documents out; mixed or side-effecting patches rejoin the main questions.

## Anti-patterns

- **Shipping on "minor version" labels without the flowchart.** Version numbers are not a regulatory classification.
- **Using successful regression tests as the whole decision record.** Missing risk reasoning fails Principle 5 and Principle 8.
- **Comparing only to the immediate prior unofficial build.** Cumulative changes against the original device are what 807.81 cares about.
- **Treating each git commit as a separate 510(k) question, or treating a large rewrite as "one cosmetic diff."** Aggregate and separate views both matter; scope and architecture drive the real impact.
- **Implementing a safety-intent fix quietly under QS only.** Principle 1 pushes safety-intent modifications toward a new 510(k).
- **Leaving no-file decisions undocumented.** "Document" is an instruction to create a durable record, not a synonym for "ignore."

## Key Takeaways

1. Software and firmware changes to 510(k)-subject existing devices are judged under 21 CFR 807.81(a)(3) using S9's principles plus Figure 1.
2. Walk Q1 (cyber-only) → Q2 (restore to cleared spec) → Q3a/Q3b (risk and risk controls for significant harm) → Q4 (clinical functionality or performance specifications).
3. "New 510(k)" and "document" are both disciplined outcomes; document means record the analysis.
4. Risk-based assessment covers safety and effectiveness, positive or negative impact, and unintended consequences.
5. Routine V&V must confirm a no-file decision and can reopen it; it cannot override a "could significantly affect" conclusion.
6. Compare to the original authorized device and watch cumulative effect across multiple changes.
7. QS change control and records apply to every change, filed or not.
8. Infrastructure, architecture, core algorithm, and reengineering work need extra scrutiny even when marketed as maintenance.

## Connects To

- **ch01**: pathway context for 510(k)-subject devices and why De Novo-authorized products later meet this trigger analysis.
- **ch03**: validation of software changes once the submit-or-document decision is made.
- **ch05**: quality-system change control and records under the QMSR frame.
- **ch06–ch07**: cybersecurity change content when Q1 does not end the analysis, and when security work is part of a filed update.
- **ch12**: authoring the new 510(k) in eSTAR when the flowchart ends at submission.
