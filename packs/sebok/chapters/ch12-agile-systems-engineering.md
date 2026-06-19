# Chapter 12: Agile Systems Engineering

## Core Idea
Organizations must systematically select, adapt, and continuously improve life cycle models and development approaches to balance regulatory requirements, organizational culture, and project-specific needs while maintaining alignment across teams.

## Frameworks Introduced
- **Life Cycle Model**: A framework of processes and activities organized into stages with decision gates based on entry/exit criteria, serving as a common reference for communication and management throughout system and service development (ISO/IEC/IEEE 24748-1:2024).
  - When to use: Always as the foundational structure for any system development; organizations should maintain multiple models with clear guidance on which to apply to each project type.

- **PMI Situation Context Framework (SCF)**: A seven-dimensional framework for selecting situation-dependent development strategies, scaling across team size, geographic distribution, organizational distribution, skill availability, compliance, domain complexity, and solution complexity.
  - When to use: To guide selection between Sequential, Incremental, Evolutionary, and Agile development approaches when context varies significantly.

- **Development Approaches** (Sequential, Incremental, Evolutionary, Agile): Candidate strategies for system development, selected and adapted based on risk, requirements clarity, technological novelty, and organizational constraints.
  - When to use: Selected based on risk analysis and contextual factors such as how well requirements are understood, system size, technology change rate, staff and budget constraints, and user preferences for phased capability delivery.

## Key Concepts
- **Life Cycle Stage**: A distinct phase within the overall life cycle model (concept, development, production, utilization, support, retirement) for which approaches and criteria must be explicitly selected and adapted.
- **Adaptation**: Modification of a life cycle model or development approach to suit project-specific needs; changes must be guided by adaptation guidelines, documented, and approved if they exceed organizational limits.
- **Entry/Exit Criteria**: Specific conditions that gate transitions between life cycle stages; adapting these criteria is a key adaptation mechanism.
- **Domain-Specific Life Cycle Model**: Distinct life cycle models appropriate for different technical domains (hardware vs. software); systems with both may require synchronized but separate models for each domain.
- **Risk-Driven Selection**: Use of risk analysis to compare candidate development approaches and guide selection toward approaches that reduce project risk most effectively.
- **Stakeholder Alignment**: Shared understanding and agreement between acquirer and supplier on selected development approaches and life cycle stages to ensure consistent execution.
- **Continuous Improvement**: Regular review and measurement of life cycle models against key performance indicators to ensure they remain relevant and effective as organizational and customer requirements evolve.

## Mental Models
- **Think of life cycle models as organization-specific templates, not universal prescriptions.** Every organization's size, industry, history, and culture shape which model works; transferring a model directly between organizations rarely succeeds.
- **Use adaptation guidelines as guardrails, not constraints.** Adaptation is expected and necessary; what matters is that changes are documented, stay within organizational limits, and don't break cross-project value propositions.
- **Match the development approach to uncertainty, not just to scale.** If requirements are unclear, technology is new, or the domain is unfamiliar, consider approaches (Evolutionary, Agile) that reduce risk through iteration rather than upfront planning.
- **Synchronize domain-specific models at the system level.** Hardware and software may follow different life cycles internally, but must hand off at defined integration points and share consistent entry/exit criteria.

## Anti-patterns
- **Ignoring organizational context when adapting life cycle models**: Adaptation must account for the broader portfolio of projects in the organization to preserve value propositions like consistent project startup, cross-project knowledge transfer, and efficient resource allocation.
- **Treating life cycle models as static**: Failure to review and refresh models as organizational and regulatory environments change leads to misalignment and inefficient project execution.
- **Selecting a development approach in isolation**: Not considering system elements, enabling systems, and domain-specific factors means some parts of the system may use inappropriate approaches, increasing risk.
- **Lack of acquirer–supplier agreement**: Misalignment between acquirer and supplier on development approach, stages, or criteria creates coordination failures and delivery risk.

## Key Takeaways
1. **Start with organization-specific life cycle models.** Define multiple models if needed (e.g., for small vs. large projects, different regulatory domains), and maintain clear decision logic for which model applies when.
2. **Develop adaptation guidelines and limits.** Document the boundaries within which projects can adapt stages, criteria, and approaches without requiring approval; this balances flexibility with organizational consistency.
3. **Select development approaches based on context and risk.** Use frameworks like the PMI Situation Context Framework to weigh candidate approaches (Sequential, Incremental, Evolutionary, Agile) against factors like requirements clarity, team distribution, technology novelty, and regulatory constraints.
4. **Treat every life cycle stage (not just development) as needing a selected and documented approach.** Production, utilization, support, and retirement each require explicit strategy selection and adaptation.
5. **Synchronize domain-specific models in multi-technology systems.** If hardware and software follow different life cycles, define clear handoff points and ensure synchronized entry/exit criteria at the system integration boundary.
6. **Measure and improve continuously.** Define key performance indicators alongside life cycle models, track them over time, and use results to evolve models as organizational maturity and market conditions change.
7. **Ensure alignment across organizational boundaries.** When acquirer and supplier are distinct entities, reach explicit agreement on development approaches and life cycle stages; ambiguity creates execution risk and delivery surprises.

## Connects To
- **ISO/IEC/IEEE 24748-1 (Life Cycle Management)**: The normative reference for life cycle model structure, decision gates, and adaptation practices; SEBoK elaborates on how to instantiate these concepts in organizational context.
- **ISO/IEC/IEEE 15288 (Systems and Software Engineering – System Life Cycle Processes)**: Defines the life cycle processes (concept, development, production, utilization, support, disposal) that life cycle models organize and govern.
- **PMI Situation Context Framework**: Complements SEBoK's development approach selection with structured guidance on scaling factors for context-dependent strategy.
- **Organizational governance and process improvement**: Life cycle model selection and continuous improvement are foundational to enterprise systems engineering capability maturity.
