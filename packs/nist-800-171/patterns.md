# Patterns — NIST SP 800-171 Rev. 3

## 1. CUI Enclave Isolation
- **When to use:** CUI touches only a subset of enterprise systems.
- **How:** Architect a separate security domain (VLANs/firewalls, identity boundary, dedicated admin plane); inventory CUI locations; apply 800-171 inside the enclave.
- **Trade-offs:** Up-front segmentation cost vs enterprise-wide control rollout; mis-drawn boundaries create silent scope gaps.

## 2. ODP Completion Workshop
- **When to use:** Contract arrives with unfilled assignment/selection parameters.
- **How:** Inventory all ODPs; assign agency values where provided; for blanks, set org values with risk owners; freeze values in SSP and assessment procedures.
- **Trade-offs:** Speed of “copy industry defaults” vs defensible, environment-specific choices assessors will test.

## 3. Joiner–Mover–Leaver Security Workflow
- **When to use:** Any org with staff/contractor turnover on CUI systems.
- **How:** Tie HR events to account provisioning, privilege review, badge issuance, and same-day disablement/recovery of authenticators and media.
- **Trade-offs:** Automation investment vs residual orphaned access risk.

## 4. Deny-by-Default Software and Network Posture
- **When to use:** High-value CUI hosts and managed interfaces.
- **How:** Allow-list applications (03.04.08); deny network traffic by default at boundaries (03.13.06); document exceptions with owners.
- **Trade-offs:** Operational friction and exception backlog vs reduced malware and lateral-movement surface.

## 5. Privileged Access Dual Control
- **When to use:** Admin paths to CUI systems.
- **How:** Separate privileged accounts; MFA; session logging; no daily-driver admin use; monitor privileged functions.
- **Trade-offs:** Slightly slower ops vs dramatically better accountability and incident forensics.

## 6. IR Capability Drill Cadence
- **When to use:** After the IR plan exists (03.06.05).
- **How:** Train IR roles; tabletop then technical tests on defined cadence; feed findings to POA&M and plan updates.
- **Trade-offs:** Exercise cost/time vs discovering broken call trees and tooling only during a real incident.

## 7. Media Custody Chain
- **When to use:** Removable media, tapes, field laptops, and backup sets with CUI.
- **How:** Mark → store → authorize access → track transport → sanitize before release → encrypt backups.
- **Trade-offs:** Process overhead vs catastrophic loss from an unmarked USB or unsanitized disk.

## 8. Continuous Monitoring Mini-Program
- **When to use:** After initial assessment, to avoid compliance cliffs.
- **How:** Define metrics (vuln age, config drift, log coverage, IR drill status); report on cadence; escalate via risk response.
- **Trade-offs:** Tooling and analyst time vs stale evidence and surprise assessment failures.

## 9. External Provider Oversight Pack
- **When to use:** Cloud, SaaS, or MSSP processes CUI.
- **How:** Flow down requirements; define oversight roles; require evidence; monitor compliance; reflect in SSP and SCRM plan.
- **Trade-offs:** Vendor management load vs uncontrolled third-party CUI exposure.

## 10. Unsupported Component Decision Record
- **When to use:** Vendor ends support for OS, app, or appliance in the CUI boundary.
- **How:** Prefer replace; else isolate + compensating controls + formal risk acceptance with review date (03.16.02).
- **Trade-offs:** Migration cost vs accepted exploitability and assessment findings.

## 11. SSP as Living Boundary Document
- **When to use:** Always for assessable 800-171 implementations.
- **How:** Describe components, data flows, inherited controls, ODPs, and enduring exceptions; update on architecture change.
- **Trade-offs:** Documentation discipline vs assessment chaos and incorrect scoping.

## 12. Supply Chain Flow-Down
- **When to use:** Subcontractors or integrators can touch CUI or critical components.
- **How:** Contractual SCRM requirements, authenticity checks, notification duties, right-to-assess; monitor performance (03.17.xx).
- **Trade-offs:** Procurement complexity vs sub-tier blind spots.
