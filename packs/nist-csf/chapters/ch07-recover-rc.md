# Chapter 7: RECOVER (RC) Function

## Core Idea
RECOVER restores assets and operations affected by a cybersecurity incident to normal operating status through structured, integrity-verified recovery plan execution and coordinated communication with internal and external stakeholders throughout the recovery period.

## Frameworks Introduced
- **RECOVER (RC)**: The Function that returns the organization to normal operations after a cybersecurity incident; it is initiated by recovery criteria from RESPOND and depends on verified backup integrity established under PROTECT.
  - When to use: once RS.MA-05 recovery initiation criteria are met; recovery actions must be planned before incidents occur (ID.IM-04).

## Key Concepts
- **Incident Recovery Plan Execution (RC.RP)**: The structured execution of recovery activities including: executing the recovery plan (RC.RP-01), selecting and scoping prioritized recovery actions (RC.RP-02), verifying backup and restoration asset integrity before use (RC.RP-03), establishing post-incident operational norms that account for mission criticality and ongoing risk (RC.RP-04), verifying restored asset integrity and confirming normal operating status (RC.RP-05), and formally declaring the end of incident recovery with completed documentation (RC.RP-06).
- **Incident Recovery Communication (RC.CO)**: Coordinating recovery activities and progress with designated internal and external stakeholders (RC.CO-03) and sharing public updates using approved methods and messaging (RC.CO-04).
- **Backup Integrity Verification (RC.RP-03)**: The explicit requirement to verify the integrity of backups and other restoration assets before using them for restoration — preventing recovery from corrupt, incomplete, or compromised backups.
- **Post-Incident Operational Norms (RC.RP-04)**: A considered re-establishment of operating conditions that accounts for critical mission functions and ongoing cybersecurity risk, rather than a blind return to the pre-incident state.
- **Recovery Declaration (RC.RP-06)**: A formal, criteria-based declaration that incident recovery is complete, accompanied by completed documentation — providing a clear end boundary to the incident life cycle.
- **Approved Communication Methods (RC.CO-04)**: Public updates on incident recovery must use pre-approved messaging and channels; ad hoc public statements risk legal, regulatory, and reputational harm.
- **Restoration Asset Integrity (RC.RP-05)**: Verification that restored assets are free of attacker presence and behaving as expected before normal operations are confirmed.

## Mental Models
- Use RC.RP-03 before RC.RP-02: verify backup integrity before selecting restoration actions — a compromised or corrupted backup used for restoration extends the incident rather than ending it.
- Use RC.RP-04 as a deliberate decision point: returning to the exact pre-incident state may re-expose the organization to the same vulnerability; consider whether post-incident norms should differ.
- Use RC.CO-04 with pre-approved messaging: recovery communications — especially public-facing ones — should be scripted and approved in advance, not improvised during a high-pressure recovery.

## Anti-patterns
- **Declaring recovery complete without RC.RP-05 verification**: Confirming normal operations before verifying restored asset integrity risks re-declaring an incident after threat actors re-activate dormant footholds.
- **Skipping RC.RP-06 formal documentation**: Without a formal end-of-recovery declaration and completed documentation, the incident life cycle remains open — impairing post-incident review and regulatory reporting.

## Key Takeaways
1. RECOVER is not simply "restore from backup" — it includes integrity verification, post-incident norm setting, formal declaration, and coordinated communication across both technical and external stakeholder dimensions.
2. Backup integrity verification (RC.RP-03) is an explicit recovery prerequisite, not an implicit assumption; backups must be tested under PROTECT (PR.DS-11) and verified again before restoration use.
3. Post-incident operational norms (RC.RP-04) require a deliberate decision about what normal operations look like after the incident, accounting for residual risk.
4. The formal end-of-recovery declaration (RC.RP-06) provides a documented close to the incident, supporting regulatory compliance, legal defensibility, and lessons-learned processes.
5. Public recovery communications (RC.CO-04) require approved methods and messaging — organizations must establish communication protocols before incidents occur.
6. RECOVER feeds back into IDENTIFY Improvement (ID.IM): lessons learned from recovery execution should update incident response plans and organizational risk management processes.

## Connects To
- **RESPOND (RS)**: RS.MA-05 (recovery initiation criteria) is the formal trigger for RECOVER; root cause findings from RS.AN-03 inform recovery scope and post-incident norms.
- **PROTECT (PR)**: Tested backups (PR.DS-11) established under PROTECT are the data assets verified under RC.RP-03; resilience mechanisms (PR.IR-03) support the ability to recover to normal operations.
- **IDENTIFY (ID)**: Incident response plans (ID.IM-04) include recovery plans; lessons from RC.RP-06 documentation feed improvement identification (ID.IM-01, ID.IM-03).
- **SP 800-34r1 (Contingency Planning Guide)**: Detailed NIST guidance for continuity and recovery planning that operationalizes RC.RP outcomes.
