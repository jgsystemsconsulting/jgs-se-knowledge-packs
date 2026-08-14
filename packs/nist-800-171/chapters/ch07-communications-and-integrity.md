# Chapter 7: System & Communications Protection and System & Information Integrity

## Core Idea
Families 3.13 and 3.14 harden the technical fabric that carries and hosts CUI. Communications protection covers boundaries, shared resources, deny-by-default networking, confidentiality of data in transit/storage, cryptography, session authenticity, and risky collaboration features. Integrity covers flaw remediation, malicious code defense, alerts/advisories, system monitoring, and information retention.

## Frameworks Introduced
- **Network and boundary defense**: Managed interfaces, deny-by-default flows, network disconnect, and protection of CUI on shared resources.
- **Cryptographic protection pattern**: Key management + approved cryptography for confidentiality of CUI at rest and in transit.
- **Integrity operations**: Patch/flaw management, malware prevention, continuous system monitoring, and disciplined retention.

## Key Concepts
- **Boundary protection (03.13.01)**: Monitor and control communications at external managed interfaces; implement subnetworks for publicly accessible components that are separated from internal networks.
- **Shared system resources (03.13.04)**: Prevent unauthorized and unintended information transfer via shared resources (object reuse / residual data concerns).
- **Deny by default — allow by exception (03.13.06)**: Deny network communications traffic by default and allow by exception at managed interfaces.
- **Transmission and storage confidentiality (03.13.08)**: Protect confidentiality of CUI at rest and in transit.
- **Network disconnect (03.13.09)**: Terminate network connections associated with communications sessions at end of session or after defined inactivity.
- **Cryptographic key management (03.13.10)**: Establish and manage cryptographic keys when cryptography is employed for CUI protection.
- **Cryptographic protection (03.13.11)**: Implement organization-defined cryptography types for CUI confidentiality; FIPS-validated cryptography is recommended.
- **Collaborative computing and mobile code (03.13.12–13)**: Control remote activation of collaborative devices; provide physical/logical disconnect; authorize, monitor, and control mobile code.
- **Session authenticity (03.13.15)**: Protect authenticity of communications sessions (anti-hijack measures).
- **Flaw remediation (03.14.01)**: Identify, report, and correct system flaws; install security-relevant updates within defined time windows.
- **Malicious code protection (03.14.02)**: Deploy malicious code protection at entry/exit points and on hosts; update signatures/mechanisms; perform periodic and real-time scans as defined.
- **Security alerts and directives (03.14.03)**: Receive external alerts/advisories; generate internal ones; take directed actions within time frames.
- **System monitoring (03.14.06)**: Monitor systems to detect attacks, indicators of potential attacks, and unauthorized connections; heighten monitoring during heightened risk.
- **Information management and retention (03.14.08)**: Manage and retain CUI within the system and information output from the system per applicable laws, regulations, and retention policies.

## Mental Models
- Boundary protection is the network expression of CUI scope isolation from Chapter 1.
- Cryptography is a supporting control: choose validated modules, manage keys, and apply it where confidentiality requirements demand — not as a substitute for access control.
- Integrity ops is a daily factory: patch SLAs, malware engines, alert intake, and monitoring detections must run continuously.
- Session authenticity and network disconnect close the loop after successful authentication (ch02).

## Anti-patterns
- **Flat networks with CUI servers adjacent to user VLANs**: Boundary and deny-by-default requirements exist to prevent this.
- **Encryption without key management**: Keys on the same host as ciphertext, never rotated, shared in tickets.
- **“We’ll patch next maintenance window” with no SLA**: Flaw remediation ODPs expect defined time bounds.
- **Signature-only malware defense with no monitoring**: Misses novel attacks that monitoring and IR must catch.

## Key Takeaways
1. Managed boundaries, deny-by-default networking, and session controls reduce lateral movement and exposure of CUI.
2. Confidentiality of CUI in transit and at rest is an explicit technical requirement, typically met with cryptography.
3. Key establishment/management is in scope whenever crypto is used for CUI.
4. Collaborative devices, mobile code, and shared resources are specialized leak paths that need explicit policy and technical limits.
5. Flaw remediation, malware protection, advisories, and system monitoring form the integrity operations stack.
6. Retention rules ensure CUI is kept no longer (and no less protectively) than policy requires.

## Connects To
- **ch02**: Access and authentication start the session that SC/SI must keep trustworthy.
- **ch04**: Monitoring and audit correlate with SI system monitoring.
- **ch05**: Backup crypto (media family) aligns with SC cryptographic protection.
- **ch06**: Vulnerability scanning results feed flaw remediation priorities.
