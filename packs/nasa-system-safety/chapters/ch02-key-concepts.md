# Chapter 2: Key Concepts

## Core Idea
Chapter 2 establishes the precise terminology and conceptual architecture underlying the entire handbook: the distinction between Acquirer and Provider roles, the two-principle definition of adequate safety, and the RISC as the vehicle for structured safety argument.

## Frameworks Introduced
- **Adequate Safety Two-Principle Framework**: A system is adequately safe if and only if it (1) meets or exceeds the minimum tolerable level of safety performance AND (2) is ASARP. Both conditions must hold simultaneously throughout all life-cycle phases.
  - When to use: As the definition against which all safety objectives, requirements, and claims are ultimately evaluated.
- **Risk-Informed Safety Case (RISC)**: Structured argument + body of evidence providing a compelling, comprehensible, and valid case that a system is or will be adequately safe.
  - When to use: To replace ad hoc collections of safety deliverables with a unified, evaluable argument at KDPs.

## Key Concepts
- **System Safety**: The application of engineering and management principles, criteria, and techniques to optimize safety and reduce safety risk within constraints of operational effectiveness, time, and cost throughout all life-cycle phases.
- **Safety Performance**: The complement of the probability of harm (1 minus the probability of adverse safety consequences); probabilistic and not directly observable.
- **Safety Risk**: The potential for shortfall with respect to safety performance requirements — only exists to the extent that uncertainty exists about whether requirements will be met.
- **Acquirer**: A NASA organization that tasks another organization to produce a product or deliver a service; responsible for safety assurance (developing confidence that safety has been ensured and accepting safety risk).
- **Provider**: A NASA or contractor organization responsible for safety ensurance (reducing/eliminating hazards and achieving adequate safety through design, procurement, fabrication, construction, and/or operation); must develop a RISC to support the Acquirer.
- **Safety Threshold**: The maximum tolerable probability of harm from all sources when the system is first put into operation (initial minimum tolerable level).
- **Safety Goal**: The maximum tolerable probability of harm after the system has matured through operational experience (long-term minimum tolerable level).
- **Safety Performance Margin**: An incremental margin subtracted from the safety threshold or goal to account for the estimated total effects of UU hazards; estimated from historical experience with similar technologies considering complexity, novelty, and environment.
- **Risk Burndown**: The expectation that as a program/project evolves and mitigations are implemented and knowledge improves, uncertainty and risk decrease over time.
- **Known Risk**: A scenario correctly identified and accurately assessed for likelihood and severity.
- **Underappreciated Risk**: A correctly identified scenario whose likelihood and/or severity is underestimated.
- **Unknown Risk**: A scenario that has not been identified at all at the time of analysis.
- **ASARP (As Safe As Reasonably Practicable)**: A system is ASARP if incremental safety improvement would require intolerable or disproportionate sacrifice of performance in other domains (technical, cost, schedule); separate from and additional to meeting minimum tolerable levels.

## Mental Models
- Use the 2x2 adequate safety matrix (meets minimum tolerable level? × is ASARP?) to diagnose a system's safety state and identify the correct remediation: a system that meets minimum but is not ASARP is sub-optimally safe and must pursue further improvement within program constraints.
- Use the Acquirer/Provider split to assign accountability: Acquirers set requirements and evaluate the RISC; Providers achieve safety and build the RISC. When a Provider also tasks a sub-provider, they assume the Acquirer role for that relationship.
- Use safety threshold vs. safety goal to express time-varying safety requirements: early flights operate against the threshold; mature operations are evaluated against the more stringent goal.

## Anti-patterns
- **Treating safety risk as absence of known accidents**: Safety risk (per NPR 8000.4A) is potential for shortfall relative to requirements, not just the probability of harm; a system can have low known risk yet high safety risk due to UU uncertainty.
- **Treating ASARP as identical to meeting minimum tolerable levels**: These are distinct conditions; a system can meet the minimum threshold while still having practicable safety improvements available (sub-optimal safe state).

## Key Takeaways
1. Adequate safety requires both meeting a probabilistic floor (minimum tolerable level) and continuous ASARP effort; either alone is insufficient.
2. The Acquirer bears risk acceptance responsibility and must independently evaluate the Provider's safety case; collaboration is required but functions remain distinct.
3. UU risks are the dominant threat; safety performance margins exist specifically to preserve headroom for scenarios not yet identified.
4. The RISC is not just documentation — it is the mechanism for organizing existing safety products into a coherent, evaluable argument that counters confirmation bias.
5. Safety thresholds and goals create a dynamic requirement profile that tightens as the system accumulates operational experience and matures.

## Connects To
- **NPR 8000.4A (Risk Management)**: Risk defined consistently; safety risk is one instance of performance risk in the mission execution domain of safety.
- **NPR 8715.3C (NASA General Safety Program Requirements)**: Defines safety for NASA systems, consistent with this chapter's definition.
- **NPR 7123.1B (Systems Engineering)**: SE processes implement the means by which safety objectives are achieved; system safety is an integral part, not an adjunct.
