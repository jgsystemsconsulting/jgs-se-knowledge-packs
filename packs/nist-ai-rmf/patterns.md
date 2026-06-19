# NIST AI RMF 1.0 Patterns & Techniques

## Pattern 1: GOVERN-First Setup
**When to use**: Before starting any system-specific risk work; when establishing or auditing an AI programme's governance foundation.
**How**: Establish GOVERN 1 (policies, legal/regulatory inventory, risk tolerance), GOVERN 2 (accountability structures and training), GOVERN 3 (team diversity and human-AI configuration roles), GOVERN 4 (risk culture practices), GOVERN 5 (external feedback mechanisms), GOVERN 6 (third-party policies) before initiating MAP activities.
**Trade-offs**: Requires upfront organisational investment and senior executive commitment; delays system-specific work but prevents governance-less risk management that produces unaccountable outcomes.

## Pattern 2: MAP Before MEASURE
**When to use**: At the start of any AI system initiative, or when a system's deployment context has changed significantly.
**How**: Complete MAP 1 (context documentation), MAP 2 (system categorisation), MAP 3 (benefits and costs), MAP 4 (third-party risks), MAP 5 (impact characterisation) before selecting measurement metrics. Use MAP outputs as direct inputs to MEASURE 1.1 metric selection.
**Trade-offs**: Takes time; organisations under schedule pressure skip MAP and then lack the contextual basis for meaningful measurement.

## Pattern 3: Independent TEVV
**When to use**: For any AI system where trustworthiness claims must withstand external scrutiny; higher-risk systems require this unconditionally.
**How**: Separate the team performing TEVV tasks from the team that built and trained the model (MEASURE 1.3). Bring in domain experts and potentially external assessors for evaluations involving human subjects (MEASURE 2.2) or high-stakes decisions.
**Trade-offs**: Adds cost and coordination overhead; substantially reduces internal bias and conflicts of interest that undermine measurement validity.

## Pattern 4: Go/No-Go Gate
**When to use**: Before committing to deployment of any AI system.
**How**: After MAP and MEASURE, formally record a go/no-go determination (MANAGE 1.1) documenting whether the system achieves its intended purposes, whether residual risks are within tolerance, and whether downstream acquirers and end users have been informed of residual risks (MANAGE 1.4).
**Trade-offs**: Creates accountability and an audit trail; requires organisational willingness to halt a system if risk is unacceptable — politically difficult but essential for trustworthiness.

## Pattern 5: Four-Option Risk Response
**When to use**: For every high-priority risk identified through MAP and MEASURE.
**How**: Explicitly choose and document one of four responses for each risk: mitigate (reduce likelihood or impact), transfer (shift responsibility, e.g., insurance or contractual), avoid (discontinue the activity), accept (proceed within documented tolerance). Record rationale for each decision (MANAGE 1.3).
**Trade-offs**: Forces explicit decision-making rather than implicit acceptance; requires more documentation but creates accountability and enables future re-evaluation.

## Pattern 6: Current-to-Target Profile Gap Analysis
**When to use**: When adopting the AI RMF for the first time, or periodically to assess maturity progress.
**How**: Construct a Current Profile describing existing AI risk management activities and outcomes. Define a Target Profile specifying desired outcomes. Compare them to identify gaps; build a prioritised action plan to close gaps.
**Trade-offs**: Requires honest self-assessment; produces a roadmap but not instant improvement. Valuable for communicating risk posture to leadership and external stakeholders.

## Pattern 7: Third-Party Risk Mapping
**When to use**: Whenever an AI system incorporates third-party data, pre-trained models, software libraries, or cloud-based AI services.
**How**: In MAP 4, document all third-party components, their associated legal and IP risks, and internal risk controls. In GOVERN 6, establish contingency processes for high-risk third-party failures. In MANAGE 3, monitor third-party risks and pre-trained models continuously during operation.
**Trade-offs**: Third-party opacity complicates assessment; organisations may have limited leverage over providers. Documenting known gaps is better than assuming provider risk management is sufficient.

## Pattern 8: Continuous Production Monitoring
**When to use**: For all deployed AI systems; mandatory for systems with human-facing outputs or safety implications.
**How**: Implement MEASURE 2.4 (functionality and behaviour monitoring in production) and MANAGE 4.1 (post-deployment monitoring plan with user feedback, appeal, override, and incident response mechanisms). Feed monitoring results back into MAP and MEASURE cycles.
**Trade-offs**: Requires ongoing resource allocation; cannot be deferred. Systems without production monitoring have no mechanism for detecting performance drift or emergent harms.

## Pattern 9: Trustworthiness Tradeoff Analysis
**When to use**: When optimising for one trustworthiness characteristic threatens to degrade another (e.g., interpretability vs. accuracy; privacy-enhancing techniques vs. accuracy; fairness vs. predictive performance).
**How**: Use MEASURE outputs to quantify the tradeoff. Document the values and context at play. Make the tradeoff decision transparently with appropriate stakeholder input. Record the rationale so it can be revisited if context changes.
**Trade-offs**: Requires contextual human judgement; no algorithm resolves value conflicts. The process creates accountability even when the outcome is contested.

## Pattern 10: Diverse Team Composition
**When to use**: For all MAP activities and AI risk management functions; especially critical for high-risk or societal-impact systems.
**How**: Assemble teams with demographic, disciplinary, and experiential diversity for MAP context-setting (MAP 1.2) and GOVERN decision-making (GOVERN 3.1). Include human factors professionals, domain experts, socio-cultural analysts, and representatives from potentially affected communities.
**Trade-offs**: Takes longer to convene and coordinate; substantially improves identification of implicit assumptions, contextual risks, and potential harms that homogeneous teams consistently miss.

## Pattern 11: Residual Risk Disclosure
**When to use**: Before deploying an AI system or releasing it to downstream acquirers.
**How**: Document all unmitigated risks (MANAGE 1.4). Communicate residual risks to downstream acquirers and end users as part of system documentation. Include in post-deployment monitoring plans how residual risks will be tracked.
**Trade-offs**: Requires transparency about system limitations; may affect adoption decisions. Omitting disclosure shifts unacknowledged risk onto users and creates liability exposure.

## Pattern 12: Deactivation Mechanism Pre-Deployment
**When to use**: For any AI system before it enters production.
**How**: Before deployment, design and test a mechanism to supersede, disengage, or deactivate the AI system if it demonstrates performance or outcomes inconsistent with intended use (MANAGE 2.4). Assign clear responsibility for activating this mechanism.
**Trade-offs**: Requires engineering effort before deployment; the absence of such a mechanism is a critical governance gap that makes it impossible to respond safely to failures once the system is live.

## Pattern 13: Lifecycle-Stage Risk Re-Assessment
**When to use**: Whenever context, capabilities, stakeholders, or deployment conditions change for a deployed AI system.
**How**: Re-apply MAP (context re-documentation), feed new MAP outputs into MEASURE (re-measure relevant characteristics), update MANAGE plans accordingly. Treat risk management as iterative, not as a one-time gate.
**Trade-offs**: Requires sustained resources; the alternative is operating on stale risk assessments that no longer reflect the actual system or its deployment environment.
