# NIST CSF 2.0 Patterns & Techniques

## Pattern: Current-to-Target Profile Gap Cycle
**When to use**: When an organization wants to drive measurable cybersecurity improvement over time rather than responding reactively to incidents or audits.
**How**: (1) Scope the Profile (whole org, a system, a threat scenario). (2) Gather data on current practices against Core outcomes. (3) Document the Current Profile. (4) Select and prioritize Target Profile outcomes based on mission, risk appetite, and threat landscape. (5) Conduct gap analysis and produce a prioritized action plan (risk register, POA&M). (6) Implement, update the Profile, and repeat.
**Trade-offs**: Profiles require organizational consensus and honest self-assessment; if Current Profile documentation is inflated, gaps go unaddressed. Multiple scoped Profiles cost more to maintain but are more actionable than a single enterprise-wide Profile.

## Pattern: GOVERN-First Program Build
**When to use**: When starting or restructuring a cybersecurity program; also when an existing program lacks executive sponsorship or consistent policy.
**How**: Establish Organizational Context (GV.OC) before setting risk appetite (GV.RM). Define roles and authorities (GV.RR) and enforce policy (GV.PO). Only then prioritize IDENTIFY and PROTECT investments.
**Trade-offs**: GOVERN-first takes time before visible technical controls appear; executives may push for immediate technical fixes. Without GOVERN, technical controls are deployed without strategic alignment and risk wasted investment.

## Pattern: Tiered Maturity Progression
**When to use**: When communicating cybersecurity maturity goals to executives or benchmarking against peers; when justifying investment in governance process improvements.
**How**: Assess current practices against Tier descriptors (Partial/Risk Informed/Repeatable/Adaptive) for governance and management separately. Identify one Tier step up as the target, conduct a cost-benefit analysis, and define the policy and process changes needed to achieve it. Document progression in Organizational Profiles.
**Trade-offs**: Tiers describe practice rigor, not outcome achievement; an organization at Tier 3 may still have unmet outcomes in specific Categories. Higher Tiers require genuine governance change — not just more tools — and may be unnecessary where risks and mandates are low.

## Pattern: Supply Chain Risk Integration (GV.SC Full Cycle)
**When to use**: Whenever the organization acquires technology products or relies on external service providers; especially in regulated sectors where third-party risk is audited.
**How**: (1) Establish a C-SCRM program with objectives and policies (GV.SC-01). (2) Define supplier roles and responsibilities (GV.SC-02). (3) Prioritize suppliers by criticality (GV.SC-04). (4) Conduct pre-engagement due diligence (GV.SC-06). (5) Embed cybersecurity requirements in contracts (GV.SC-05). (6) Monitor throughout the relationship (GV.SC-07). (7) Include suppliers in incident planning (GV.SC-08). (8) Plan for post-relationship obligations (GV.SC-10).
**Trade-offs**: Comprehensive C-SCRM requires contractual leverage with suppliers and dedicated monitoring resources. Small organizations may need to prioritize highest-criticality suppliers rather than implementing the full cycle across all vendors.

## Pattern: Bidirectional Risk Communication
**When to use**: When executives and practitioners lack a shared language for cybersecurity risk; when cybersecurity reporting does not influence strategic decisions.
**How**: Executives communicate risk appetite and strategic priorities downward via GOVERN outcomes. Managers translate these into Target Profiles and action plans. Practitioners implement controls and report KPIs/KRIs upward. Updated Organizational Profiles close the loop, informing executive decisions on risk strategy adjustments.
**Trade-offs**: Bidirectional communication requires consistent reporting cadence and agreed metrics; without it, practitioners optimize for technical metrics that do not translate to business risk conversations.

## Pattern: Asset-Driven Safeguard Targeting
**When to use**: When an organization has limited resources and needs to prioritize where to invest in PROTECT controls.
**How**: Complete ID.AM inventories and apply ID.AM-05 criticality classification. Map the highest-criticality assets to the PROTECT Categories most relevant to their exposure (PR.AA for access, PR.DS for data, PR.PS for platform, PR.IR for resilience). Allocate controls proportionate to criticality and assessed risk (ID.RA).
**Trade-offs**: Criticality classification requires ongoing maintenance; assets change life-cycle status (ID.AM-08) and criticality can shift with mission changes. Under-classified assets become unprotected attack vectors.

## Pattern: Detection Substrate Build
**When to use**: Before deploying DETECT tooling; when monitoring programs generate alerts that cannot be analyzed because log sources are insufficient.
**How**: Establish log generation (PR.PS-04) for all platforms before deploying monitoring. Build network flow representations (ID.AM-03) to define normal baselines. Deploy monitoring across DE.CM asset environments (network, physical, personnel, external providers, computing). Define incident declaration criteria (DE.AE-08) before activating alerting.
**Trade-offs**: Comprehensive logging increases storage and processing costs. Poorly tuned monitoring produces alert fatigue, which undermines DE.AE analysis quality.

## Pattern: Incident Life-Cycle Gate Management
**When to use**: When incident response produces inconsistent outcomes due to unclear boundaries between DETECT, RESPOND, and RECOVER phases.
**How**: Define DE.AE-08 incident declaration criteria as the DETECT-to-RESPOND gate. Define RS.MA-05 recovery initiation criteria as the RESPOND-to-RECOVER gate. Define RC.RP-06 recovery declaration criteria as the end-of-incident gate. Treat each gate as a formal decision requiring documented authorization.
**Trade-offs**: Strict gates slow the response if criteria are overly conservative; too-loose criteria create premature transitions (e.g., recovering before eradication is complete, per RS.MI-02).

## Pattern: Backup-Integrity Recovery Chain
**When to use**: When planning recovery capabilities; when validating that the organization can actually recover from ransomware or destructive attacks.
**How**: Create and test backups under PR.DS-11. Verify backup integrity before restoration (RC.RP-03). Select recovery actions based on scope and priority (RC.RP-02). Verify restored asset integrity before confirming normal operations (RC.RP-05). Formally declare recovery end with completed documentation (RC.RP-06).
**Trade-offs**: Backup testing (PR.DS-11) consumes production-like resources and time. Skipping RC.RP-03 pre-use integrity verification risks recovering from a compromised or incomplete backup.

## Pattern: Continuous Improvement Integration (ID.IM Loop)
**When to use**: To prevent cybersecurity programs from becoming static; to institutionalize lessons learned from incidents, exercises, and operations.
**How**: After any evaluation (ID.IM-01), exercise (ID.IM-02), operational execution (ID.IM-03), or incident recovery (links to RC.RP-06), capture improvement opportunities and feed them into updated incident response plans (ID.IM-04) and Organizational Profiles. Escalate systemic findings to GOVERN for policy or strategy updates (GV.PO-02, GV.OV-01).
**Trade-offs**: Without dedicated time and process for improvement capture, operational tempo crowds out learning. Improvements not escalated to governance remain tactical fixes rather than program-level changes.

## Pattern: ERM Integration via CSF Language Translation
**When to use**: When cybersecurity risk is managed in isolation from other enterprise risks; when boards and executives do not engage with cybersecurity risk in the same terms as financial or operational risk.
**How**: Map cybersecurity risk management outputs (from GOVERN and IDENTIFY) to ERM language using NIST IR 8286-series guidance. Include cybersecurity risk in enterprise risk registers alongside financial, privacy, and operational risks. Present cybersecurity posture to executives using business-impact terms rather than technical vulnerability counts.
**Trade-offs**: Translation requires cybersecurity practitioners to understand business context and risk quantification methods; this capability gap is common and must itself be addressed (often via GV.RR-04 and PR.AT-02).

## Pattern: Emerging Technology Risk Assimilation
**When to use**: When the organization adopts new technologies (AI, IoT, cloud) that introduce novel cybersecurity risks not covered by existing controls.
**How**: Assess the new technology against all six CSF Functions to identify new risks. Integrate with relevant frameworks (e.g., NIST AI RMF for AI systems). Update Organizational Profiles to reflect changed Current and Target states. Treat the technology adoption as a change event triggering GV.RM strategy review and ID.RA risk assessment.
**Trade-offs**: Integrating novel technology risks into existing programs requires cross-functional coordination. Waiting until after deployment to assess risks allows threats to materialize before controls are in place.
