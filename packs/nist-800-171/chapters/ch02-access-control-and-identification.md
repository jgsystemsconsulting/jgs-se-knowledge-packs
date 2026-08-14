# Chapter 2: Access Control and Identification & Authentication

## Core Idea
Families 3.1 (Access Control) and 3.5 (Identification and Authentication) jointly decide who may touch CUI, under what conditions, and how identity is proven. Account lifecycle, least privilege, session controls, remote/wireless/mobile access, multi-factor authentication, and authenticator management form the primary technical perimeter around CUI.

## Frameworks Introduced
- **Account and privilege lifecycle**: Define account types, assign/monitor/remove access, separate duties, and constrain privileged functions.
- **Session and device controls**: Logon limits, notifications, device lock, session termination, remote access management.
- **Boundary of external and mobile use**: Wireless, mobile devices, external systems, and publicly accessible content rules when CUI is in play.
- **Identity proofing stack**: User and device identification, MFA, replay resistance, identifier and password/authenticator management, feedback protection.

## Key Concepts
- **Account management (03.01.01)**: Specify account types; create, enable, modify, disable, and remove accounts; monitor use; notify account managers of role changes and removals.
- **Access enforcement (03.01.02)**: Enforce approved authorizations for logical access to CUI and system resources.
- **Information flow enforcement (03.01.03)**: Control CUI flows within the system and between connected systems according to policy.
- **Separation of duties / least privilege (03.01.04–07)**: Split conflicting roles; grant minimum necessary access; restrict privileged accounts and the performance of privileged functions.
- **Logon and session hygiene (03.01.08–11)**: Limit consecutive failures; display system-use notification; lock devices after inactivity and on demand; terminate user sessions after defined conditions.
- **Remote, wireless, mobile, external (03.01.12, 16, 18, 20)**: Authorize, monitor, and control remote access; establish usage restrictions and implementation guidance for wireless; control mobile device connection and CUI on mobiles; restrict use of external systems holding CUI.
- **Publicly accessible content (03.01.22)**: Train posters, review content, and remove nonpublic information from public faces.
- **User/device identification (03.05.01–02)**: Uniquely identify and authenticate organizational users and, where required, devices before interactions.
- **Multi-factor and replay-resistant authentication (03.05.03–04)**: MFA for system and network access to CUI environments; mechanisms resistant to replay.
- **Identifier and password management (03.05.05, 07)**: Manage identifiers over time; enforce password complexity, lifetime, and reuse rules consistent with ODPs.
- **Authenticator management and feedback (03.05.11–12)**: Protect authenticator content, initial distribution, and lost/compromised recovery; obscure authentication feedback during entry.

## Mental Models
- Access control answers “may this subject act?”; identification/authentication answers “is this subject who it claims?” — both must succeed before CUI operations proceed.
- Privileged access is a product line of its own: separate accounts, tighter monitoring, and no day-to-day use of admin identities for ordinary work.
- Remote/wireless/mobile are not special cases of “nice to have policy” — they are first-class CUI exposure channels and need explicit authorize-monitor-control loops.
- MFA is necessary but not sufficient without authenticator lifecycle (issuance, revocation, phishing-resistant choices where risk warrants).

## Anti-patterns
- **Shared accounts for CUI workloads**: Destroys accountability and breaks audit correlation.
- **Standing privileged access**: Always-on admin rights without just-in-time or dual control.
- **Password-only remote access to CUI**: Conflicts with MFA expectations for network/system access paths.
- **Unmanaged BYOD with local CUI caches**: Mobile and external-system requirements exist specifically to stop this.

## Key Takeaways
1. AC + IA are the gatekeepers: unique identity, strong authentication, least privilege, and controlled remote/mobile paths.
2. Account lifecycle events (joiners/movers/leavers) must drive timely enablement and removal.
3. Information flow rules matter as much as login rules when CUI moves between enclaves.
4. Device lock, session termination, and unsuccessful-logon limits reduce unattended and brute-force exposure.
5. Authenticator and password management requirements extend beyond “set a complex password” into full lifecycle control.
6. Public-facing content review prevents accidental CUI disclosure outside the authorized boundary.

## Connects To
- **ch03**: Personnel screening/termination and physical access reinforce logical AC/IA.
- **ch04**: Audit events should capture authentication and privileged actions.
- **ch07**: Boundary protection and cryptography protect CUI in transit once access is granted.
- **ch06**: Continuous monitoring and assessments validate that AC/IA controls remain effective.
