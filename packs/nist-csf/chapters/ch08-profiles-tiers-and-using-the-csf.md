# Chapter 8: Organizational Profiles, Tiers, and Using the CSF

## Core Idea
Organizational Profiles and Tiers are the operationalization layer of the CSF: Profiles translate Core outcomes into documented current and target cybersecurity postures enabling gap analysis and action planning, while Tiers characterize the rigor of risk governance and management practices — together supporting bidirectional communication across executives, managers, and practitioners, and integration with enterprise risk management.

## Frameworks Introduced
- **CSF Organizational Profile (Current + Target)**: A structured documentation of where an organization is (Current Profile) and where it wants to be (Target Profile) in terms of CSF Core outcomes.
  - When to use: to drive measurable improvement cycles, communicate posture to stakeholders, and set supplier/partner expectations.
- **CSF Community Profile**: A sector- or use-case-specific baseline of Core outcomes published for shared adoption.
  - When to use: as the starting point for a Target Profile when a relevant Community Profile exists for the organization's sector or threat context.
- **CSF Tiers (Partial/Risk Informed/Repeatable/Adaptive)**: A four-level maturity characterization applied to risk governance and management practices.
  - When to use: to set organization-wide tone for risk management rigor and communicate progress benchmarks.
- **Bidirectional Risk Communication Model**: The CSF's model of information flowing from executives to managers to practitioners (strategic direction and expectations) and back (KPIs, KRIs, posture updates).
  - When to use: when structuring governance reporting and cybersecurity dashboards across organizational levels.

## Key Concepts
- **Current Profile**: Specifies Core outcomes an organization is currently achieving (or attempting to achieve), characterizing how and to what extent each outcome is met.
- **Target Profile**: Specifies desired Core outcomes selected and prioritized by the organization for its cybersecurity risk management objectives; considers anticipated changes (new requirements, technology adoption, threat trends).
- **Gap Analysis**: The comparison of Current and Target Profiles to identify differences and develop a prioritized action plan (e.g., risk register, risk detail report, Plan of Action and Milestones [POA&M]).
- **Tier 1 (Partial)**: Risk management is ad hoc; limited organizational awareness of cybersecurity risks; no formal policies or processes.
- **Tier 2 (Risk Informed)**: Prioritization is ad hoc and not formally based on objectives or threat environment; cybersecurity risk management is implemented on an irregular, case-by-case basis.
- **Tier 3 (Repeatable)**: Risk management practices are approved by management; formally expressed as policy; risk-informed policies and procedures are defined, implemented, and reviewed; practices regularly updated.
- **Tier 4 (Adaptive)**: Organization-wide approach using risk-informed policies; cybersecurity risk is understood in the same context as financial and other organizational risks; organization adapts practices based on lessons learned and predictive indicators; uses real-time or near-real-time information on supply chain risk.
- **Plan of Action and Milestones (POA&M)**: A planning artifact used to track actions required to close gaps between Current and Target Profiles.
- **Enterprise Risk Management (ERM)**: The organization-wide portfolio approach to balancing all risk types; the CSF facilitates translation of cybersecurity risk language into general risk management terms understandable by executives.
- **Key Performance Indicators (KPIs) / Key Risk Indicators (KRIs)**: Metrics provided by practitioners to managers and executives to enable informed decisions about cybersecurity posture and risk strategy.

## Mental Models
- Use Tiers to set ambition, Profiles to track progress: Tiers answer "how rigorously do we manage risk overall?", Profiles answer "which specific outcomes are we achieving and which are gaps?".
- Use the five-step Profile cycle continuously: Scope → Gather → Create → Analyze Gaps → Implement; repeat as risk environment, requirements, or mission changes.
- Use bidirectional communication explicitly: executives communicate risk appetite and direction downward; practitioners communicate KPIs and operational insights upward; both directions are necessary for adaptive risk management.

## Anti-patterns
- **Using Tiers as a compliance score**: Tiers characterize rigor of practices, not achievement of specific outcomes; an organization at Tier 3 for governance may still have significant gaps in specific PROTECT or DETECT Categories.
- **Single static Profile**: Organizational Profiles should be scoped, updated, and multiplied as needed (e.g., one for financial systems, one for OT environments); a single organization-wide Profile often obscures high-risk sub-areas.
- **Targeting the highest Tier without cost-benefit analysis**: Progression to higher Tiers is encouraged only when risks or mandates are greater or when a cost-benefit analysis indicates a feasible and cost-effective reduction; Tier 4 is not the universal target.

## Key Takeaways
1. Profiles are the CSF's primary improvement mechanism: a Current Profile establishes baseline, a Target Profile defines goals, gap analysis produces an action plan, and implementation closes gaps.
2. Community Profiles lower the barrier to entry: organizations in sectors with published Community Profiles can adopt a proven baseline rather than building a Target Profile from scratch.
3. The four Tiers (Partial → Adaptive) describe a progression from ad hoc, informal responses to agile, risk-informed, continuously improving practices — advancing Tiers requires genuine governance change, not only technical controls.
4. The CSF enables bidirectional communication: executives use it to set expectations and resource direction; practitioners use it to report posture and surface risks; managers translate between the two levels.
5. Integration with ERM is an explicit CSF design goal: the CSF helps translate cybersecurity terminology into the general risk language that executives use for financial, reputational, and other enterprise risks.
6. Supply chain risk is fully integrated at Tier 4 (Adaptive): real-time information on supplier cybersecurity risk informs organizational risk strategy — supply chain is not a separate program but a core ERM dimension.

## Connects To
- **GOVERN (GV)**: Risk strategy and oversight established in GOVERN provide the inputs (risk appetite, objectives) that shape Target Profile priorities.
- **IDENTIFY (ID)**: Improvement outcomes (ID.IM) feed directly into Profile updates and action plan revisions.
- **NIST IR 8286 series**: Detailed guidance on integrating CSF Profile and Tier information with enterprise risk management processes.
- **SP 800-37 (NIST RMF)**: Profiles and Tiers complement the RMF's system authorization and continuous monitoring workflows; a CSF Profile can inform the selection of security controls from SP 800-53.
- **NIST Privacy Framework**: Privacy risks that overlap with cybersecurity risks can be addressed in the same Organizational Profile process using both frameworks together.
