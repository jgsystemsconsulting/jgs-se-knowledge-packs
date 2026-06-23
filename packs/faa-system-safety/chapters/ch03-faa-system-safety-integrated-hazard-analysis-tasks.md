# Chapter — Integrated System Hazard Analysis and Safety Analysis Tasks

## Core Idea

System safety exists to push a system toward an optimum degree of safety by finding the risks built into it and then eliminating or controlling them through design or procedure, working down the order of precedence. The two FAA System Safety Handbook chapters synthesized here — Chapter 7 (Integrated System Hazard Analysis) and Chapter 8 (Safety Analysis: Hazard Analysis Tasks) — make one combined argument: an accident in a complex system is almost never a single failure, so neither a single technique nor a single analysis can capture the risk. You must *logically combine* several hazard analyses into an integrated picture (Chapter 7), and you must execute that picture through a disciplined sequence of design-phase analysis tasks tied to the acquisition lifecycle (Chapter 8).

The handbook is emphatic that this is not a matter of stapling many techniques into one report and hoping a coherent risk evaluation emerges. Integration is a deliberate act of reasoning about how the human (with procedures), the machine (hardware, firmware, software), and the environment interact under change and deviation. A risk is built from a chain of hazards, each with its own likelihood; the analyst's job is to hypothesize the accident scenario, identify the contributory hazards along it, estimate the credible worst-case harm, and estimate the likelihood of reaching that harm — then design controls that drive the risk to an acceptable level and verify that those controls actually work.

## Frameworks Introduced (exact source names, when/how)

The slice names and uses the following frameworks, models, and analysis tasks:

- **Integrated System Hazard Analysis** — the handbook's term for the logical combining of separate hazard analyses into one coherent risk evaluation. Used as the organizing concept for all of Chapter 7; conducted by the Integrated System Safety Working Group (ISSWG) during safety reviews and integrated risk/hazard tracking and resolution.
- **5M model** — the interaction model the handbook points to (with a cross-reference to Chapter 3) for evaluating the relationships among the human, the machine, and the environment as the elements of a system.
- **Order of Precedence (system safety precedence)** — invoked from the opening as the basis for choosing how to eliminate or control risk (cross-referenced to a table in Chapter 3, and to Chapter 4). Chapter 8 illustrates it concretely with the landing-gear resolution example: change the design to remove the hazard, then safety devices, then warning devices, then special training and procedures.
- **Specific integrated analyses keyed to interactions** — the handbook lists, at minimum, Human–Human Interface Analysis; for the machine, Abnormal Energy Exchange, Software Hazard Analysis, and Fault Hazard Analysis; for the environment, Abnormal Energy Exchange and Fault Hazard Analysis. Hazard Control Analysis is added across all interfaces to test whether control of the system is sufficient.
- **Common Cause Analysis** — named as a technique (referencing the *System Safety Analysis Handbook*) for finding accident sequences where shared physical relationships let one event defeat multiple redundant legs. Companion location-based techniques named: vicinity analysis and zonal analysis.
- **Event Flow / "point of no return" model** — a model of how a balanced system becomes unbalanced after an initiator, passing through detection, recovery, and loss-control onset toward harm; used to frame why monitoring must reliably reveal the system state.
- **Failure Modes and Effects Analysis (FMEA)** and **Failure Modes, Effects, and Criticality Analysis (FMECA)** — reliability analyses the handbook contrasts with hazard analysis; FMECA is built from an FMEA by adding a criticality figure of merit, considers only hardware failures, and runs typically bottom-up.
- **The seven design and pre-design safety activities (Chapter 8.4)** — Preliminary Hazard List (PHL), Preliminary Hazard Analysis (PHA), Requirements Hazard Analysis (RHA), Subsystem Hazard Analysis (SSHA), System Hazard Analysis (SHA), Operating and Support Hazard Analysis (O&SHA), and Health Hazard Assessment (HHA). Each is defined with purpose, timing, inputs, content, and the Statement of Work (SOW) details to specify when the work is under contract.
- **Fault Tree Analysis (FTA)** and **Success Trees** — FTA is the dominant deductive logic-model technique, starting from a defined top undesired event and branching down through AND/OR/INHIBIT gates and transfers to cut sets; Success Trees are its inverse, modeling the success state with path sets. Boolean algebra underlies the quantification of both.
- **Hazard Tracking / Risk Resolution system** — referenced (Chapter 4) as the mechanism for carrying medium- and high-risk hazards to documented closure.
- **Operational Safety Assessment (OSA)** — named as the source of safety goals and parameters that qualitative analysis must verify the design operates within.
- **Proactive vs. reactive System Safety Program (SSP)** — the framing distinction that opens Chapter 8: a proactive program shapes the design before it begins, via a PHL carried into the RFP, contract, and specifications; a reactive program is stuck justifying redesign after milestones.

## Key Concepts

**Risk is a chain, not a point.** The handbook insists that risk equals the worst-case severity of an event multiplied by its likelihood, and that the event itself is assembled from many contributors — unsafe acts and unsafe conditions, each with its own probability. Change the hypothesized outcome and you have changed the scenario, which means a different risk. The four worked figures (engine covers, fuel-tank rupture, hydraulic brake runway run-off, unsecured cabin door causing hypoxia) all make the same point: many things had to go wrong together, in sequence, for the accident to occur.

**Initiating, contributory, and primary hazards.** An accident sequence runs from initiating hazards through contributory hazards to a primary (catastrophic or critical) event. The handbook stresses that you cannot single out one hazard as "the" important one — all three categories must be weighed to determine the risk. Initiators can occur at any point in the lifecycle. A safeguard that fails to function is itself a hazard.

**Contributory hazards and adverse events.** Adverse events are the potential accidents under study (the top event); beneath them sit contributory hazards (unsafe acts such as human errors, and unsafe conditions such as failures, faults, anomalies, malfunctions), then less-than-adequate (LTA) controls, then LTA verification of controls. Low reliability does not by itself make a system hazardous — a system can be engineered to fail into a safe state, and procedures can be written to absorb human error.

**Safety and reliability are complementary, not interchangeable.** Both disciplines use FMEA and FTA, but their objectives differ. Reliability is the probability that a system performs its intended function for a stated time under stated conditions; safety predicts a broader notion of failure that includes hazardous hardware failures, software malfunctions, mechanically correct but functionally unsafe operation, human design error, unplanned event sequences, and adverse environments. Equipment can fail with no harm (fail-safe), and equipment can function exactly as designed yet injure someone at the wrong time. A failure rate adequate for reliability (often in the .9 to .99 range) can fall far short of a safety requirement (often nearer .999999).

**The hazard analysis steps and the four key elements.** Chapter 8 gives an explicit twelve-step procedure (bound the system, perform functional analysis, build the PHL, identify contributory hazards and initiators, establish the control baseline, determine outcomes, assess severity and likelihood, rank by risk, recommend controls, inform decision-makers for trade-offs, track medium/high risks to verified closure, and demonstrate compliance). Underlying it are four key elements: hazard identification (identification, evaluation, resolution), timely solutions, and verification that requirements are met or risk is controlled to acceptable levels.

**The seven activities map to the lifecycle.** The PHL seeds the effort and feeds the RFP. The PHA is the foundational analysis that frames all others and must land before preliminary design review. The RHA translates hazards and generic standards into design requirements and is substantially complete by the allocated baseline. The SSHA examines how component operation or failure affects the whole; the SHA examines how the whole system and its interfaces affect subsystem safety, integrating the SSHAs — and SHA/SSHA are typically submitted before Critical Design Review. The O&SHA evaluates procedurally controlled operation and support across the full lifecycle and is usually the last analysis completed. The HHA identifies and quantifies hazardous materials and physical agents and recommends life-cycle-cost-aware controls.

**Qualitative always precedes quantitative.** A qualitative analysis reviews all factors against predetermined acceptability parameters and describes likelihood in words; a quantitative analysis takes the next step and computes probabilities (the handbook gives the unreliability relation P = 1 − e^(−λt)). Quantitative work is more precise but more expensive, and — critically — only useful if the limitations of the numbers are stated and understood.

**FTA mechanics and evaluation.** FTA is deductive: define the top event well (neither so broad it explodes the tree nor so narrow it yields nothing), branch down through gates, assign probabilities to the lowest events, and derive minimum cut sets (the smallest event combinations that produce the top event). A predominance of OR gates is a warning sign; circles at the branch bottoms (primary failures) suggest completeness while many diamonds (undeveloped or secondary failures) suggest the tree needs expansion. Transfers must be controlled so interpage references stay consistent. FTA finds the failures leading to a *predetermined* top event — it does not, by itself, enumerate which hazards deserve a top event.

## Mental Models

**"Connect the dots."** The handbook describes the analyst's core difficulty as seeing the whole system picture — following several contributors from the initiating event, through the events that follow, to the eventual outcome. Such risks can be one-of-a-kind, hard to detect, easy to overlook, and highly unusual, which is exactly why any single technique misses them.

**System balance and the point of no return.** Picture the system as balanced while it operates within design parameters. An initiator pushes it toward imbalance; monitoring exists to detect the imbalance in time to stabilize before the point of no return — the threshold beyond which damage or accident becomes inevitable. Monitors that give erroneous "ready," "satisfactory," or "input received" indications are themselves contributory hazards.

**The 5M / human-machine-environment triangle.** Treat every interaction across the three system elements as a candidate for analysis. The human parameter pulls in human factors, biomechanics, ergonomics, and performance variables; the machine pulls in hardware, firmware, and software; both sit inside an environment whose adverse effects must be studied.

**"Should we trust what the machines tell us?"** In the human-in-the-loop discussion the handbook poses automation as capable of presenting an artificial reality — when automation malfunctions and displays false indications, the human may react to a world that is not there, and the consequences can be catastrophic during an emergency. The mental model is to treat operator trust in automation as a designed property that can be defeated.

**Software does not fail — but everything around it can.** The handbook's software axioms form a mental checklist: software does not degrade or improve over time and, executing as written, does not "fail" in the hardware sense — yet humans make requirement, design, and coding errors; a single error can propagate through a coupled system; a change in part of the software (or in the application it is used for) almost always changes system risk; planned functions can themselves be contributory hazards; and you cannot cleanly segregate software from hardware, humans, and environment.

**Redundancy is not safety until proven.** The recurring caution is to distrust the assumption "it is redundant and monitored, therefore it is safe." True independence of complex load paths, microprocessors, and software is hard to prove; even independently developed designs can share a common failure mode if the requirement given to the programmers is wrong. The Titanic is invoked as the cautionary image — compartmentalization was designed in, but latent common flaws in the steel and the cold-water effects were not considered.

## Anti-patterns

The source explicitly names these traps, mostly clustered in Chapter 7's risk-control discussion and Chapter 8's review guidance:

- **"Combine techniques and call it integration."** Simply assembling many methods in one report does not produce a logical evaluation of risk; integration must be reasoned, not stapled.
- **"Eliminate failures and the product is safe."** A highly reliable product can still carry a dangerous characteristic; removing failures does not by itself make it safe.
- **"Conformance to codes and standards equals acceptable risk."** Standards can be inappropriate, inadequate for the specific design, outdated by technology, or — as the handbook quotes from the Product Safety commission — innocuous and ineffective because they were written for broad industry acceptance.
- **"It is redundant and monitored, so it must be safe."** Independence and monitoring may be unproven; common events and shared physical locations can defeat all legs at once.
- **"Probability alone controls risk."** A probability guarantees nothing and cannot say when or to whom a mishap occurs; the handbook recounts a rocket motor with a one-in-100,000 predicted failure rate whose first test article blew up, and warns that generalized probabilities fail for localized situations (the coastal bird-strike example) and that small sample sizes give low confidence.
- **"Do not change the prediction to match limited data."** Independent events keep their probability regardless of recent results — the coin-flip and the engine-failure examples warn against revising a prediction to fit a short run of outcomes.
- **Treating an FMEA/FMECA as a finished hazard analysis.** Reliability analyses consider only hardware failures, miss human and procedural errors and sneak circuits, miss sequential and multiple hazards, do not document hazard corrective action, and treat all failure modes as if equally relevant — so blindly using one wastes effort on non-safety-critical items and leaves real hazards uncovered.
- **Late, vague, or procedure-only analysis.** Reviewers should be suspicious when hazards are fixed by procedure rather than design (a sign they were caught too late), when recommendations are vague ("needs further evaluation"), when there is a lack of detail, or when controls require testing that was never planned.
- **The safety engineer working "in a vacuum."** Performing an independent analysis and formally reporting results later, instead of feeding recommendations to designers as soon as they surface, yields costlier fixes, program resistance to change, and weaker controls.
- **A top event that is too broad or too narrow.** "Aircraft crashes" explodes the tree; an over-specified top event spends time and money for little return.

## Key Takeaways

- An accident in a complex system is the product of many contributors in sequence; design the analysis to find chains, not points.
- Integration means *logically combining* hazard analyses around human–machine–environment interactions — not merging reports.
- Risk = worst-case severity × likelihood; control either variable (severity or likelihood) to reduce risk, and remember a failed safeguard is itself a hazard.
- Work through the order of precedence: design out the hazard first, then safety devices, then warning devices, then training and procedures.
- Reliability and safety complement each other but are not interchangeable; reliability failure rates are usually too coarse to satisfy safety requirements.
- Run the seven activities (PHL → PHA → RHA → SSHA → SHA → O&SHA → HHA) in lifecycle order so each analysis lands in time to shape the design.
- A proactive SSP that influences design before it starts is far cheaper than a reactive one that justifies redesign after milestones.
- Qualitative analysis always precedes quantitative; quantification adds precision but only helps when the limits of the numbers are explicit.
- FTA is powerful for a chosen top event but does not tell you which hazards to analyze; judge a tree by its gates, cut sets, and the balance of circles versus diamonds.
- Distrust comfortable assumptions — eliminated failures, conformance to standards, redundancy plus monitoring, and bare probability are each insufficient on their own.
- Carry medium- and high-risk hazards to documented, verified closure in a hazard tracking and risk resolution system; never let a hazard get lost between one analysis and the next.

## Connects To

- **Chapter 3 of this pack (system description, the 5M model, the order-of-precedence table, likelihood criteria):** the integrated analysis and every Chapter 8 activity depend on bounding the system and using the precedence and likelihood definitions established there.
- **Chapter 4 (Hazard Tracking and Risk Resolution):** the closure mechanism that every analysis feeds, and the basis for tracking recommendations across analyses.
- **Chapter 9 (hazard analysis approaches) and Chapter 10 (software safety process and the software hazard risk matrix):** the technique catalog and the software-specific risk assessment that the activities draw on, especially for designating safety-critical software functions.
- **Reliability engineering (FMEA/FMECA):** a major data source for SSHAs, with the caveat that reliability objectives and failure rates must be re-scoped for safety before reuse.
- **The acquisition lifecycle and contracting:** PHL into the RFP and specifications; SOW details (severity/probability reporting thresholds, technique selection, items to include or exclude) for every activity; and the design-review milestones (preliminary design review, CDR) that pace when each analysis must be delivered.
- **Standards and references invoked in the slice:** OSHA standards, MIL-STD-454 (Requirement 1), MIL-STD-882, FAA Order 1810.1F, and FAA Order 18 series milestone reviews — the external requirement sources the RHA pulls generic safety criteria from.

---

*Source: FAA System Safety Handbook, Chapters 7 (Integrated System Hazard Analysis) and 8 (Safety Analysis: Hazard Analysis Tasks), December 30, 2000. This chapter paraphrases and synthesizes the FAA original (a U.S. Government work, public domain); any third-party reprint commentary is not public domain — use the FAA original.*
