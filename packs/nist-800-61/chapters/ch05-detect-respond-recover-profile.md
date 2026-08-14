# Chapter 5: Community Profile — Detect, Respond, and Recover

## Core Idea
Table 3 is the incident-response execution half of the Community Profile. Detect, Respond, and Recover elements carry higher IR-relative priorities, and every element includes recommendations or considerations for active handling, analysis, containment, eradication, reporting, and restoration.

## Frameworks Introduced
- **Detect (DE)**: Continuous monitoring and adverse event analysis leading to incident declaration.
- **Respond (RS)**: Incident management, analysis, communications/reporting, and mitigation (contain/eradicate).
- **Recover (RC)**: Recovery plan execution and recovery communications, including restoration verification criteria.

## Key Concepts
- **DE.CM continuous monitoring**: Watch networks/services, computing hardware/software/runtimes/data, physical environment, personnel activity/tech usage, and external provider activity for unauthorized actions, deviations, and posture changes. Include wired and wireless, DNS/BGP-class services, and rogue networks. Tune to manage false positives/negatives. Enrich with cyber threat information so malicious activity is not dismissed as benign.
- **DE.AE adverse event analysis**: Correlate multi-source telemetry, estimate impact/scope, integrate threat intel, and declare incidents when criteria are met — declaration is the handoff into RS.
- **RS.MA incident management**: Execute the IR plan; triage, categorize, prioritize, escalate; define criteria for initiating recovery.
- **RS.AN incident analysis**: Establish root cause where feasible; preserve evidence integrity and provenance; validate magnitude estimates.
- **RS.CO reporting and communication**: Notify internal/external stakeholders per policy and law; share information with trusted partners as appropriate.
- **RS.MI mitigation**: Contain and eradicate; choose actions that limit damage without unnecessarily destroying evidence needed for analysis and legal processes.
- **RC.RP recovery plan execution**: Select recovery actions; verify backup integrity before restore; establish post-incident operational norms; verify restoration; formally declare recovery complete when criteria are met.
- **RC.CO recovery communication**: Coordinate with stakeholders; use approved public messaging when needed.
- **Higher priority band**: Unlike Table 2, Table 3 rows are specific to responding to incidents and therefore skew High/Medium with denser R/C guidance.

## Mental Models
- Detection quality is a product of monitoring coverage, tuning, and threat context.
- Declaration criteria (DE.AE) prevent both alert-fatigue non-response and panicking at every anomaly.
- Containment is a risk decision: speed vs evidence vs business disruption — pre-authorized playbooks beat improvised calls.
- Recovery is not “systems up” until integrity verification and formal recovery declaration criteria pass.

## Anti-patterns
- **Monitoring only endpoints or only perimeter**: Profile expects multi-asset continuous monitoring including providers and physical environment.
- **Response without evidence hygiene**: Eradication that destroys forensic value undermines root-cause and legal options.
- **Restoring from backups never tested**: RC backup integrity checks exist because failed restores extend incidents.
- **Communications ad lib**: Inconsistent public/partner messages create secondary legal and trust incidents.

## Key Takeaways
1. Table 3 operationalizes DE/RS/RC as the active IR layer of the CSF-aligned life cycle.
2. Continuous monitoring must cover diverse asset classes and be tuned and threat-informed.
3. Analysis leads to explicit incident declaration that triggers managed response.
4. Response balances containment/eradication with evidence preservation and prioritized recovery initiation.
5. Recovery includes technical restore, integrity checks, operational norms, and formal completion criteria.
6. Communications requirements run through both RS and RC and must be pre-planned with legal/public affairs.

## Connects To
- **ch02**: Top-layer Functions in the life-cycle model.
- **ch03**: Who executes monitoring, declaration, mitigation, and messaging.
- **ch04**: Preparation that makes these outcomes achievable.
- **ch06**: Cross-org coordination and information-sharing patterns.
