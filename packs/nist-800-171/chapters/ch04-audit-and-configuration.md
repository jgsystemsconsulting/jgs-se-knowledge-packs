# Chapter 4: Audit & Accountability and Configuration Management

## Core Idea
Families 3.3 and 3.4 make CUI environments observable and change-controlled. Audit requirements define what is logged, how records are protected and reviewed, and how time is trusted. Configuration management establishes baselines, controls changes, limits functionality, inventories components, and hardens high-risk deployments.

## Frameworks Introduced
- **Audit logging lifecycle**: Specify events → generate content-rich records → respond to logging failures → review/analyze/report → reduce/report → protect integrity of audit data.
- **Configuration baseline and change control**: Define secure baselines, manage settings, analyze impact, restrict who can change, and inventory what exists.
- **Least functionality and allow-by-exception software**: Reduce attack surface by disabling unneeded capabilities and permitting only authorized software.

## Key Concepts
- **Event logging (03.03.01)**: Determine which events to log (successful/unsuccessful logons, privileged actions, CUI object access, etc., per ODPs) and the frequency of logging.
- **Audit record content and generation (03.03.02–03)**: Ensure records include what type of event occurred, when, where, source, outcome, and identity of individuals/processes; generate records for defined events.
- **Logging failure response (03.03.04)**: Alert responsible personnel and take organizationally defined actions when audit logging fails.
- **Review, analysis, reporting (03.03.05)**: Review records on a defined schedule and after indications of inappropriate activity; report findings to designated officials.
- **Reduction and report generation (03.03.06)**: Support on-demand analysis without altering original records.
- **Time stamps (03.03.07)**: Use internal system clocks and synchronize to authoritative time sources so correlated investigations are possible.
- **Protection of audit information (03.03.08)**: Protect audit information and logging tools from unauthorized access, modification, and deletion.
- **Baseline configuration (03.04.01)**: Develop, document, and maintain under configuration control the baselines for system components that process, store, or transmit CUI.
- **Configuration settings (03.04.02)**: Establish, document, implement, and monitor settings that reflect the most restrictive mode consistent with operations.
- **Change control and impact analysis (03.04.03–04)**: Track, review, approve/disapprove, and log changes; analyze security impacts before implementing changes.
- **Access restrictions for change (03.04.05)**: Limit physical and logical access that can alter the system.
- **Least functionality (03.04.06)**: Configure systems to provide only essential capabilities; prohibit or restrict functions, ports, protocols, and services.
- **Authorized software — allow by exception (03.04.08)**: Identify software allowed to execute; deny-all, permit-by-exception where feasible.
- **Component inventory and information location (03.04.10–11)**: Inventory system components; identify and document where CUI is processed and stored.
- **High-risk area configurations (03.04.12)**: Issue specifically configured components with hardened settings for travel or high-risk locations, and apply additional scrutiny on return.

## Mental Models
- If it is not logged with trustworthy time, it did not happen for investigation purposes.
- Configuration management is continuous security hygiene: baseline → change → re-baseline, with impact analysis as the gate.
- Software allow-listing flips the default from “trust until blocked” to “blocked until trusted.”
- Knowing *where* CUI lives (information location) is a configuration-management problem, not only a data-map exercise.

## Anti-patterns
- **Logging everything forever without review**: Storage fills; nobody analyzes; alerts are ignored.
- **Unprotected log stores**: Attackers delete evidence after compromise.
- **Snowflake servers without baselines**: Drift makes both security and assessment impossible.
- **Uncontrolled admin change windows**: Emergency changes without after-the-fact documentation break the audit story.

## Key Takeaways
1. Audit requirements cover generation, content, failure handling, review, reduction, time sync, and protection of audit data.
2. Privileged and CUI-relevant events are priority logging targets defined via ODPs.
3. Configuration baselines and restrictive settings are the reference state for CUI systems.
4. Change control without impact analysis is incomplete; both are required.
5. Least functionality and allow-by-exception software shrink the attack surface.
6. Component inventory plus CUI location documentation scopes monitoring and incident response.

## Connects To
- **ch02**: Authentication and privileged access events should appear in audit logs.
- **ch05**: Incident handling depends on usable audit trails.
- **ch06**: Continuous monitoring and security assessments consume configuration and audit evidence.
- **ch07**: Integrity monitoring complements audit for detecting unauthorized changes.
