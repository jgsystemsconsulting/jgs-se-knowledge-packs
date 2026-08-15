# Chapter 3: PROTECT Goals

## Core Idea
PROTECT is the largest CPG cluster: credential hygiene, MFA, privileged account separation, segmentation, training, encryption, secure defaults, change management, backups, software/hardware approval, logging, device control, and hardening of internet-facing systems. These goals target the TTPs CISA most often sees succeeding against critical infrastructure.

## Frameworks Introduced
- **Identity and access hygiene set (3.A–3.H)**: Passwords, unique credentials, login monitoring, MFA, separate admin accounts.
- **Architecture and people set (3.I–3.J)**: Segmentation and cybersecurity training.
- **Data/platform resilience set (3.K–3.S)**: Encryption, autorun/macros off, change management, backups, approval processes, logging, unauthorized device prohibition, internet-facing device security.

## Key Concepts
- **3.A Change default passwords**: Remove vendor defaults that attackers spray first.
- **3.B Establish minimum password strength**: Enforce password quality policies commensurate with risk.
- **3.C / 3.D Create unique credentials**: Prevent credential reuse so one compromise does not unlock many systems.
- **3.E Monitor unsuccessful (automated) login attempts**: Detect password spraying and brute force early.
- **3.F Implement multifactor authentication (MFA)**: Strongly reduce account-takeover success on remote and privileged paths.
- **3.G / 3.H Administrators maintain separate user and privileged accounts**: Stop daily-driver admin use; limit privilege dwell time.
- **3.I Implement logical/physical network segmentation**: Contain OT/IT blast radius and limit lateral movement.
- **3.J Implement cybersecurity training**: Build human capacity aligned to threats the org actually faces.
- **3.K / 3.L Utilize strong encryption**: Protect confidentiality of sensitive data in transit/at rest as applicable.
- **3.M Disable autorun and macros by default**: Cut common malware initial-access paths.
- **3.N Establish change management processes**: Controlled changes reduce accidental outages and malicious persistence.
- **3.O Maintain system backups and restoration ability**: Ensure recoverable state against ransomware and destructive attacks.
- **3.P Maintain hardware and software approval process**: Know and control what is allowed to run/connect.
- **3.Q Maintain log collection and storage**: Retain security-relevant logs long enough to investigate and learn.
- **3.R Prohibit connection of unauthorized devices**: Stop rogue media and shadow endpoints.
- **3.S Secure internet-facing devices**: Reduce exposure of remote access and edge systems frequently targeted by adversaries.

## Mental Models
- Most CPG protect value is “boring excellence”: defaults, MFA, segmentation, backups, logging.
- Privileged access is a product: separate accounts + MFA + monitoring beat one strong password.
- Segmentation is both IT and OT: treat control networks as high-impact zones, not flat extensions of the enterprise LAN.
- Backups without tested restore are not a protect control — they are a hope.

## Anti-patterns
- **MFA everywhere except the VPN/admin path that matters**: Mis-prioritized MFA rollout.
- **Shared OT service accounts with default passwords**: Combines 3.A/3.C/3.G failures.
- **Flat plant networks with internet-exposed HMIs**: Fails 3.I and 3.S together.
- **Logs kept three days**: Investigation and hunting become impossible (3.Q).
- **Backup targets reachable by the same ransomware identity**: Weakens 3.O.

## Key Takeaways
1. PROTECT goals concentrate on identity, privilege, segmentation, secure defaults, and recoverability.
2. Default passwords and credential reuse remain high-yield attacker paths CPGs explicitly target.
3. MFA and separate admin accounts are foundational for remote and privileged access.
4. Segmentation and internet-facing hardening bound OT/IT blast radius.
5. Training, change control, and approval processes reduce both human and supply-path risk.
6. Logging and backups convert preventative misses into survivable events.

## Connects To
- **ch02**: Assets and topology that PROTECT controls apply to.
- **ch04**: Detection and response that consume logs and IR readiness.
- **ch05**: IT vs OT nuances for passwords, segmentation, and remote access.
- **nist-800-171 / nist-csf**: Related control and outcome taxonomies for deeper programs.
