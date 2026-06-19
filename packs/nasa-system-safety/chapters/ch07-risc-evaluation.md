# Chapter 7: Evaluating the RISC — The Acquirer's Role

## Core Idea
The Acquirer conducts a staged, three-phase evaluation of the RISC (acceptance review → qualitative scope/methods review → quantitative auditing), with an independent Evaluation Team scoring assurance deficits and base claim importance on a 1–5 scale and producing a RISC Evaluation Report rating the RISC Acceptable or Unacceptable.

## Frameworks Introduced
- **Staged RISC Evaluation Process**: Three sequential phases — (1) Acceptance Review (completeness check, RAIs if needed); (2) Qualitative Scope/Methods Review (surveying: methods, coverage, evidentiary strength, ASARP); (3) Quantitative Evaluation (auditing: spot-check calculations, sensitivity studies, ASARP validation, flight rule validation).
  - When to use: At each KDP after the Provider submits the RISC; depth of each phase scales with mission criticality.
- **Value-of-Information (VOI) Analysis**: Decision-analytic method for evaluating whether the cost of obtaining additional information (more testing, more analysis) is justified by the expected reduction in uncertainty and associated reduction in safety risk.
  - When to use: When an Evaluator identifies a significant assurance deficit and the decision maker must choose between accepting the risk, mitigating it, or investing in uncertainty reduction.
- **Assurance Deficit × Claim Importance Matrix**: Two-dimensional scoring combining deficit rank (1–5: evidence quality/completeness) and importance rank (1–5: effect on top claim if base claim is false) to prioritise evaluation findings and focus risk acceptance attention.
  - When to use: To rank findings from the RISC evaluation and identify which deficits most urgently require remediation.

## Key Concepts
- **Evaluator**: An agent of the Acquirer tasked to evaluate the RISC and generate technical findings; must be independent from the Provider and from the Acquirer's decision-making authority to avoid conflicts of interest and political influence.
- **Acceptance Review**: First evaluation phase; checks that all required material is present, comports with analysis protocols, is generally consistent with SSMP commitments, and is complete enough for substantive review.
- **Qualitative Scope/Methods Review (Surveying)**: Second phase; compares RISC elements to standard methods and to comparable analyses; evaluators develop their own independent perspective on results; assesses Provider qualifications and experience.
- **Quantitative Evaluation (Auditing)**: Third phase; independent checking of selected technical results; ranges from peer review (high-level spot checks) through replication of key results; evaluator develops simplified analytic models to confirm Provider findings.
- **Request for Additional Information (RAI)**: Formal mechanism for seeking clarification of a specific weakness in one or more RISC claims at any phase; RAIs drive Provider updates integrated back into the RISC.
- **Assurance Deficit Rank (1–5)**: Evaluator's score of evidence quality for each base claim: Rank 1 (~95–100% confidence base claim is justified by evidence) through Rank 5 (~0–35% confidence).
- **Importance Rank (1–5)**: Evaluator's score of how much the top claim's confidence would be affected if a base claim were false: Rank 1 (<5% effect) through Rank 5 (>65% effect).
- **Overall Confidence Aggregation**: No single formula is universally correct; the handbook discusses four simplified methods (multiply independent confidences; weighted average; minimum; weighted product of logarithms) and recommends expert judgement backed by rational argument, not mechanical aggregation.
- **RISC Evaluation Report**: The formal output of the evaluation process; contains summary and detailed evaluation findings communicated to the decision maker.
- **Delphi Method / Expert Elicitation**: Structured process for reconciling divergent expert confidence assessments; outliers may be excluded before averaging; divergence without consensus should prompt identification of specific remedies.

## Mental Models
- Use the staged process to conserve evaluation resources: acceptance review is cheap and saves substantive review time; qualitative surveying surfaces scope/methods issues; quantitative auditing targets highest-impact claims for independent verification.
- Use the deficit × importance matrix to prioritise: high-deficit, high-importance findings are the critical path to RISC acceptability; low-deficit, low-importance findings can be noted but need not block approval.
- Use VOI analysis when a deficit is significant but not immediately remediable: determine whether the cost of more testing/analysis is less than the value of the uncertainty reduction, then give the decision maker a clear framing of the three choices (accept risk, mitigate, or reduce uncertainty).
- Use multiple experts with explicit numerical confidence statements: individual scores back-referenced to deficit and importance rankings provide structured rationale and enable comparison across systems and reviews.

## Anti-patterns
- **Mechanical confidence aggregation**: Multiplying all base-claim confidence levels together or taking the minimum without accounting for the claim tree's actual logical structure; produces numbers that appear precise but reflect invalid independence assumptions.
- **Single-expert evaluation**: Expert judgement that is not cross-checked by a corps of independent subject-matter experts is vulnerable to individual blind spots and cannot provide the independence assurance required by the framework.
- **Accepting the RISC unchanged when key arguments are not understood**: The Evaluator must achieve genuine understanding of every key argument, not just acknowledge receipt; gaps in understanding are RAI triggers, not acceptance items.
- **Separating RISC evaluation from CRM**: Evaluation findings that are not converted to risk statements and tracked under the CRM process after acceptance will not be managed; the evaluation is the input, CRM is the ongoing management mechanism.

## Key Takeaways
1. The Evaluator's primary obligation is critical, adversarial interrogation of the RISC — seeking flaws, not proving safety — to avoid confirmation bias that mirrors the Provider's own.
2. Independence of the Evaluation Team is structural, not optional: independence from both Provider and Acquirer decision-making authority is required to ensure technical credibility.
3. The three-phase staged evaluation matches evaluation depth to what has been submitted; it is not a pass/fail checklist but an iterative process with RAI cycles.
4. No aggregation formula is universally correct; overall RISC confidence should be a rational expert judgement backed by deficit and importance scores, not a mechanical product of numbers.
5. VOI analysis converts the binary accept/reject decision into a structured three-way choice (accept, mitigate, reduce uncertainty), enabling more informed programmatic decisions.
6. The RISC Evaluation Report — both summary and detailed findings — becomes part of the safety-specific technical basis at the KDP; it is the Acquirer's counterpart to the Provider's RISC Report.

## Connects To
- **Chapter 6 (RISC Development)**: Evaluation criteria mirror development criteria; the same claims tree, deficit scale, and evidence categories used to build the RISC are used to evaluate it.
- **NPR 7123.1B**: RISC evaluation criteria are consistent with KDP technical review success criteria.
- **NPR 8000.4A (CRM)**: Post-evaluation assurance deficits feed into the Continuous Risk Management process as risk statements with assigned owners.
- **NASA RISC Evaluation Management Tool (OSMA)**: Implements a generic RISC evaluation tree based on the Ch. 7 framework; available as a NASA software tool for Evaluators.
