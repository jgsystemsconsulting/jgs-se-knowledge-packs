# Chapter 5: Respond to Vulnerabilities (RV)

## Core Idea
The RV practice group closes the security loop by ensuring that vulnerabilities discovered after software release are identified quickly, assessed and remediated in accordance with risk, and analysed for root causes so that recurrences are prevented in future software.

## Frameworks Introduced
- **RV.1 — Identify and Confirm Vulnerabilities on an Ongoing Basis**: Continuously gather vulnerability information from acquirers, users, public databases, and internal analysis; investigate all credible reports and review code to confirm findings.
  - When to use: On a continuous basis for all supported software releases; when a new CVE is published against a component in use; when a security researcher or user submits a report.
- **RV.2 — Assess, Prioritize, and Remediate Vulnerabilities**: Perform risk-based analysis of each confirmed vulnerability to gather sufficient information for remediation planning; implement risk responses including patches, temporary mitigations, and security advisories.
  - When to use: As soon as a vulnerability is confirmed; before determining a response strategy; before communicating to acquirers.
- **RV.3 — Analyze Vulnerabilities to Identify Their Root Causes**: Determine the root cause of each vulnerability; identify patterns across vulnerabilities over time; proactively search for and fix similar vulnerabilities; update the SDLC to prevent recurrence.
  - When to use: After each confirmed vulnerability is remediated; periodically as a batch analysis of accumulated vulnerability data; when a vulnerability class is identified that may affect multiple software products.

## Key Concepts
- **Vulnerability Disclosure Program (RV.1.3)**: A formal programme that makes it easy for security researchers to report potential vulnerabilities, backed by a published policy and a Product Security Incident Response Team (PSIRT).
- **Product Security Incident Response Team (PSIRT) (RV.1.3)**: A dedicated team with defined processes for handling vulnerability reports, coordinating responses, and managing communications with stakeholders.
- **Security Response Playbook (RV.1.3)**: Pre-defined procedures for handling specific vulnerability scenarios: generic reports, zero-day reports, actively exploited vulnerabilities, and multi-party open-source incidents.
- **Risk-Based Vulnerability Assessment (RV.2.1)**: Analysis of each vulnerability's exploitability, potential impact, and other characteristics to produce a risk score that drives prioritisation and response planning.
- **Temporary Mitigation (RV.2.2)**: An interim workaround applied while a permanent fix is developed; must be communicated to acquirers alongside the timeline for a permanent solution.
- **Security Advisory (RV.2.2)**: A formal notification to software acquirers describing: what the vulnerability is, how to find instances of the vulnerable software, and how to address it (patches, configuration changes, workarounds).
- **Automated Delivery of Remediations (RV.2.2)**: A trusted, automated mechanism for delivering patches to acquirers; a single remediation may address multiple vulnerabilities simultaneously.
- **Root Cause Analysis (RV.3.1)**: Post-vulnerability investigation to determine the underlying development or process failure that introduced the vulnerability, recorded in a searchable wiki for developer reference.
- **Class-Level Remediation (RV.3.3)**: Proactive search for and correction of all instances of a vulnerability's root cause within the software, rather than waiting for external reports of each individual instance.
- **SDLC Process Update (RV.3.4)**: Modifying development practices, toolchain configurations, or training based on root cause findings to prevent the same class of vulnerability from appearing in future releases.

## Mental Models
- Use vulnerability disclosure programs (RV.1.3) to turn external researchers into an asset: a well-run programme captures vulnerabilities before attackers find them.
- Use root cause analysis (RV.3) as a SDLC improvement lever: every vulnerability is evidence of a gap in PO, PS, or PW practices; fix the process, not just the symptom.
- Use class-level remediation (RV.3.3) to avoid whack-a-mole patching: once a root cause is identified, sweep the entire codebase for the same pattern rather than waiting for each instance to be reported.
- Use automated remediation delivery (RV.2.2) to shrink the window of exposure: manual patch distribution delays create extended risk windows for acquirers.

## Anti-patterns
- **Reactive-only vulnerability identification**: RV.1.2 requires proactive review and testing of code for previously undetected vulnerabilities, not just waiting for external reports.
- **Risk acceptance without documentation**: RV.2.2 permits risk acceptance as a response, but the decision and rationale must be recorded; undocumented acceptance is indistinguishable from neglect.
- **Root cause analysis without SDLC feedback loop**: RV.3.4 requires updating SDLC practices based on findings; storing root causes in a wiki without closing the loop into development process improvements does not satisfy the practice.

## Key Takeaways
1. Vulnerability identification must be ongoing and multi-source: internal testing, public databases, acquirer reports, and researcher disclosures all contribute.
2. A formal vulnerability disclosure programme and PSIRT are necessary organisational structures for credible vulnerability response.
3. Every vulnerability requires risk-based analysis to prioritise response; both permanent fixes and temporary mitigations must be communicated to acquirers.
4. Security advisories must give acquirers everything they need to identify, locate, and address the vulnerability.
5. Root cause analysis converts reactive patching into proactive process improvement.
6. Class-level remediation prevents recurrence of the same vulnerability type across the codebase.
7. The SDLC itself must be updated when root causes reveal systematic gaps in earlier practice groups.

## Connects To
- **ISO/IEC 29147 (Vulnerability Disclosure)**: RV.1.3 aligns fully with ISO 29147 for vulnerability disclosure policy and practice.
- **ISO/IEC 30111 (Vulnerability Handling Processes)**: RV.2 and RV.3 tasks map directly to ISO 30111 vulnerability handling workflow stages.
- **NIST SP 800-216 (Federal Vulnerability Disclosure Guidelines)**: RV.2.1 references SP 800-216 for risk calculation guidance.
- **EO 14028 Section 4e(viii)**: RV.1, RV.2, and RV.3 practices collectively address the EO's requirements for vulnerability identification and remediation reporting.
- **National Vulnerability Database (NVD)**: Referenced in RV.1.1 as an example vulnerability database to monitor continuously.
