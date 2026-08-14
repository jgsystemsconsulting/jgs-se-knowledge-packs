# Chapter 3: Awareness & Training, Personnel Security, and Physical Protection

## Core Idea
Human and facility controls keep CUI from walking out through people or doors. Family 3.2 builds literacy and role-based skill; 3.9 screens and manages personnel transitions; 3.10 authorizes, controls, and monitors physical access — including alternate work sites and transmission lines carrying CUI.

## Frameworks Introduced
- **Literacy plus role-based training**: Organization-wide CUI awareness paired with deeper training for roles that design, operate, or assess protections.
- **Personnel trust lifecycle**: Screening before access, and controlled termination/transfer that revokes access and recovers assets.
- **Physical access control system**: Authorizations, badges/keys, visitor control, monitoring, and protection of transmission and display paths.

## Key Concepts
- **Literacy training and awareness (03.02.01)**: Provide training to system users on CUI security risks and practical practices; refresh on a defined cadence and when the environment changes.
- **Role-based training (03.02.02)**: Ensure personnel with assigned security roles receive training before authorizing access to CUI systems or performing those roles, with periodic refreshers.
- **Personnel screening (03.09.01)**: Screen individuals prior to authorizing access to CUI organizational systems, consistent with applicable policies and risk.
- **Termination and transfer (03.09.02)**: Disable access promptly; recover authenticators, devices, and CUI media; conduct exit interviews as appropriate; and update authorizations when people change roles.
- **Physical access authorizations (03.10.01)**: Maintain lists of individuals and inventory of physical access devices; authorize access to facilities where CUI systems reside.
- **Monitoring physical access (03.10.02)**: Review physical access logs and investigate anomalies.
- **Alternate work site (03.10.06)**: Employ security controls at alternate sites commensurate with organizational assessments of risk for CUI.
- **Physical access control (03.10.07)**: Enforce physical access authorizations at entry/exit points; control visitor access; secure keys, combinations, and other physical access devices.
- **Access control for transmission (03.10.08)**: Control physical access to CUI distribution and transmission lines within organizational facilities.

## Mental Models
- Training is a control, not a once-a-year HR event: literacy for everyone, depth for custodians of CUI safeguards.
- Joiner–mover–leaver is a security workflow: HR events must trigger technical and physical revocation on the same timeline as employment changes.
- “Facility” includes the home office and other alternate sites when CUI is processed there — risk-based, not identical to the SCIF model, but not zero either.
- Physical and logical access should tell one story: the same person should not retain badge rights after account disablement.

## Anti-patterns
- **Checkbox annual training with no role differentiation**: Admins, developers, and assessors need different depth than general users.
- **Delayed offboarding**: Terminated staff retaining VPN, badge, or laptop access is a classic CUI incident precursor.
- **Ignoring visitors and shared spaces**: Tailgating and unescorted visitors bypass expensive logical controls.
- **Unprotected network closets and cabling**: Transmission-line physical access is explicitly in scope for CUI environments.

## Key Takeaways
1. Awareness builds a baseline culture; role-based training qualifies people who operate or judge the controls.
2. Screening is a precondition to CUI access, not a paperwork afterthought.
3. Termination/transfer procedures must revoke logical and physical access and recover CUI-bearing assets quickly.
4. Physical access authorizations, enforcement, and monitoring form a closed loop.
5. Alternate work sites need deliberate control selection based on risk to CUI.
6. Protecting distribution and transmission lines prevents physical taps and casual interception inside facilities.

## Connects To
- **ch02**: Logical access and authentication depend on trustworthy, trained people.
- **ch05**: Media leaving the facility intersects with physical and personnel controls.
- **ch06**: Incident and assessment programs should test physical and human control effectiveness.
- **ch01**: Scope isolation choices affect which facilities and alternate sites fall in the CUI boundary.
