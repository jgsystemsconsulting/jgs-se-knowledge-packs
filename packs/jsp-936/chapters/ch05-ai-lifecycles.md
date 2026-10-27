Sources: JSP 936 Part 1 V1.1, printed body pp. 21-28 (source Chapter 6, paragraphs 132 to 186).

# AI Lifecycles

## Core Idea

AI development most commonly aligns to the DevOps philosophy, which speeds releases through a continual, highly automated process. That continuity is also the risk: technical debt accumulates while planning and coding run ahead of testing and monitoring. The ML-flavoured variant the directive names is MLOps, depicted in its Figure 4: data trains algorithms into models, models are verified, packaged and deployed, then monitored in use with new data collected for the next cycle, making monitoring a form of continual validation in the context of use. DevSecOps is named as the security-pushing variant.

The directive does not require or advocate any one lifecycle, and a lifecycle right for a digital system may be wrong for a RAS; the adopted lifecycle should fit the context the AI will reside in. Guidance is promised for Part 2. What follows are lifecycle-agnostic requirements, stage by stage.

## Frameworks Introduced

- Planning as the confidence engine: once AI is confirmed as the right solution, planning must show how algorithm development, data, model management and supporting processes will meet system-level requirements, how transitions between phases are controlled with timely error feedback, which tools and environments will be used, which good-practice standards apply across the lifecycle, how changes, deviations and waivers are agreed, how release into wider systems stays controlled including in-situ modification such as online learning, how through-life performance monitoring and obsolescence management work, and how environmental impacts are assessed and reduced. Planning documents are version controlled and must include steps that ensure the ethical principles can be met.
- Requirements traceability that admits its own limits: the traditional System-Level, High-Level and Low-Level requirement chain, and the directive's acceptance that with ML, traceability is often lost at the Low-Level stage, which is exactly why recorded risk-balance arguments are needed for major-and-above systems.
- A data-discipline framework: training, test and verification data as separate controlled artefacts, each set correct against four properties.
- Verification and validation as distinct demonstrations: verification shows the AI meets requirements (did we build it right), validation shows it meets the user's needs (did we build the right thing).

## Key Concepts

Requirements: performance requirements sit alongside functional ones. Hazard analysis must be undertaken to identify hazards introduced by the AI, including data failure modes where ML is used, and any new hazards must be passed back up into system-level safety processes as derived mitigation requirements. Where a high-level requirement is implemented by AI, either it decomposes like traditional software, with documentation and traceability, or the training algorithm and data requirements themselves are specified and must be demonstrated to meet the intent of the high-level requirement. High-level requirements must articulate the operating context, including data distributions in training and test data. Sparse or missing data triggers lifecycle-wide mitigation guidance, set-aside data must be curated for sufficiently independent verification confidence, and every requirement should state how it will be demonstrated through verification and validation, with meaningful measures of acceptable performance in test and operational environments.

Architecture: AI architecture must be traceable to requirements and must protect against the failure modes found in hazard analysis, such as overfitting, underfitting, and sparse or missing data, with mitigations for AI failure placed in the wider system integration and architecture.

Algorithm design and implementation: design choices such as hyperparameters, and the measures used to optimise designs, should be justified and documented with traceability to requirements. Optimising against training and test data alone risks letting data limitations drive operational performance; evidence such as overfitting avoidance should be demonstrated. Traceability is maintained in implementation, and every framework or library used must be justified with its output checked as instantiating the AI requirements.

Data: training data produces the model, test data tells the development team when it is trained enough, and verification data lets a separate team independently check performance. Data should be demonstrably correct against four properties, which the source credits to Ashmore, Calinescu and Paterson: relevant to the intended behaviour in the ODD, complete across the potential input space with real-world distributions, balanced with respect to the model's purpose, and an accurate reflection of the real-world application. Separate training, test and verification sets must be produced and independently maintained; where one dataset is split, the subsets are verified to match the original's characteristics; verification data should be collected separately where possible and cover the breadth of the ODD including edge cases inside, on and beyond boundary conditions. Data provenance must be assured and recorded from collection or ingestion, and all data and metadata that influences output must sit under configuration management commensurate with the AI itself. Synthetic data is allowed with care: validate it from the AI's perspective, since an AI may cue on different features than a human would.

Models and updates: every model built for real-world use must be accompanied by information enabling risk-informed use, re-use and further development, including assumptions, dependencies, known errors and weaknesses, and ODD information; before re-using an existing model, the risk owner must be satisfied they have that information. Models should be designed for context-appropriate interpretability with different views for different stakeholders, and a model trained on classified data inherits at least that classification, with aggregation effects considered. Where AI is updated, verification and validation must cover both existing and new behaviours, including regression testing, and must confirm that unwanted emergent effects such as catastrophic forgetting and model drift have not occurred; evidence should support the sufficiency of validity claims through metrics such as ODD test coverage and internal structural coverage.

Integration, use and modification: AI always operates inside a wider system or system of systems, and its performance there, including implications for operational governance, authorities and Rules of Engagement, should be assessed. Differences between the demonstration environment and the final operational environment must be analysed and mitigated, including transfers across differing build standards. Substantive modification of the hosting system requires demonstrated continued satisfactory performance; the approved ODD must be clearly defined; Security Operating Procedures must be specific and proportionate; the operating environment must be monitored at a contextually appropriate rate; and AI performance must be monitored so the system stays within its ODD, with additional expert checks where AI supports important or risky decisions.

## Mental Models

- The lifecycle stage names are anchors for questions, not a process to install: the directive demands the planning outputs, traceability honesty, data discipline and monitoring duties whichever lifecycle a team picks.
- Lost traceability converts into a different artefact: where the LLR chain breaks, the training recipe and data requirements become the requirement statement and must be demonstrated against intent.
- Monitoring is the deployed twin of validation: watching performance in use is continual validation in context.

## Anti-patterns

Optimising a design to maximise training and test scores is named as tempting and wrong when it lets data limits drive operational behaviour. Treating verification data as a courtesy copy of training data is refused: separate sets, independently maintained, are required. Shipping a model without its assumptions, dependencies, known errors and ODD information is refused, because the next risk owner cannot manage what was never recorded.

## Key Takeaways

- Competency is a lifecycle output too: at publication there were no set AI competency profiles in MOD, so roles are analysed for appropriate competency requirements, leadership must ensure staff maintain competence, training and supervision must be provided until competence is acquired, and external organisations must be brought in where in-house competence is insufficient.
- Data provenance and configuration management are must-level duties from the moment data is collected or ingested.
- Modification, transfer and in-situ learning are all treated as renewed assurance triggers, not as free operation.

## Connects To

The hazard-analysis handoff feeds the safety machinery in ch06; monitoring and ODD enforcement connect to assurance in ch08; the ethical-principle steps in planning belong to the ch03 framework; and the safety-management-system context named here is carried by the jsp-815 pack.
