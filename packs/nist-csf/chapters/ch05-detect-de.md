# Chapter 5: DETECT (DE) Function

## Core Idea
DETECT enables the timely discovery and analysis of anomalies, indicators of compromise, and other potentially adverse events through continuous monitoring across all asset types and correlated analysis from multiple sources that culminates in incident declaration when defined criteria are met.

## Frameworks Introduced
- **DETECT (DE)**: The Function that finds and characterizes cybersecurity attacks and compromises in progress; it depends on PROTECT for the monitoring substrate and directly enables RESPOND and RECOVER.
  - When to use: continuously; monitoring cannot be paused without creating detection blind spots.

## Key Concepts
- **Continuous Monitoring (DE.CM)**: Ongoing monitoring of networks and services (DE.CM-01), the physical environment (DE.CM-02), personnel activity and technology usage (DE.CM-03), external service provider activities (DE.CM-06), and computing hardware/software/runtime environments and their data (DE.CM-09) to find potentially adverse events.
- **Adverse Event Analysis (DE.AE)**: The analysis phase following detection: characterizing potentially adverse events (DE.AE-02), correlating information from multiple sources (DE.AE-03), estimating impact and scope (DE.AE-04), disseminating findings to authorized staff and tools (DE.AE-06), integrating threat intelligence into analysis (DE.AE-07), and declaring incidents when events meet defined criteria (DE.AE-08).
- **Anomaly**: An observable deviation from expected baseline behavior of assets, networks, or personnel that may indicate an adverse event is occurring.
- **Indicator of Compromise (IoC)**: Observable evidence — in log data, network traffic, or endpoint behavior — that a system may have been attacked or compromised; detected under DE.CM Categories and analyzed under DE.AE.
- **Incident Declaration Criteria (DE.AE-08)**: Defined thresholds or conditions against which adverse events are evaluated to determine whether a formal incident should be declared, triggering the RESPOND Function.
- **External Service Provider Monitoring (DE.CM-06)**: Monitoring of activities and services from external providers — recognizing that supply chain components are a potential vector for adverse events.
- **Threat Intelligence Integration (DE.AE-07)**: Incorporating cyber threat intelligence and contextual information into adverse event analysis to improve the accuracy and speed of characterization.

## Mental Models
- Use DE.CM-09 (computing hardware/software/runtime monitoring) in conjunction with PR.PS-04 (log generation): platforms must generate logs before those logs can be monitored.
- Use DE.AE-03 (correlation from multiple sources) before DE.AE-08 (incident declaration): single-source signals produce false positives; correlation across network, endpoint, and threat intelligence data improves fidelity.
- Use DE.CM-06 to extend detection perimeter to third parties: an unmonitored external service provider is an invisible segment of your attack surface.

## Anti-patterns
- **Monitoring only the network perimeter**: DE.CM covers networks (DE.CM-01), physical environments (DE.CM-02), personnel (DE.CM-03), external providers (DE.CM-06), and computing environments (DE.CM-09) — perimeter-only monitoring misses lateral movement and insider threats.
- **Declaring incidents without defined criteria**: Without DE.AE-08 incident declaration criteria, the boundary between an adverse event and a formal incident is ambiguous, causing delayed or inconsistent activation of RESPOND.

## Key Takeaways
1. DETECT has two distinct phases: Continuous Monitoring (DE.CM) — finding events — and Adverse Event Analysis (DE.AE) — characterizing and classifying them through to incident declaration.
2. Monitoring coverage must extend across all five asset environments: network services, physical environment, personnel/technology usage, external service providers, and computing hardware/software/runtime.
3. Incident declaration (DE.AE-08) is the explicit handoff point from DETECT to RESPOND; clear criteria prevent both under-reaction and alert fatigue.
4. Threat intelligence (DE.AE-07) is an analytic input, not just a feed: it must be actively integrated into adverse event analysis to improve signal quality.
5. Correlation across sources (DE.AE-03) is the analytical method that turns individual anomalies into confident incident signals.
6. DETECT supports RESPOND and RECOVER: timely, accurate detection is a prerequisite for effective incident response and recovery.

## Connects To
- **PROTECT (PR)**: Log generation (PR.PS-04) and network architecture (PR.IR-01) are the monitoring substrate that DETECT's continuous monitoring depends on.
- **RESPOND (RS)**: Incident declaration (DE.AE-08) triggers RESPOND; the accuracy of DE.AE analysis directly affects the speed and quality of RS.MA triage.
- **IDENTIFY (ID)**: Asset inventories (ID.AM) and threat intelligence from ID.RA-02 provide context for what to monitor and what anomalies mean.
- **SP 800-137 (Information Security Continuous Monitoring)**: The detailed NIST guidance for implementing the continuous monitoring outcomes in DE.CM.
