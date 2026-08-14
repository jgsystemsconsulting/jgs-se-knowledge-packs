# Chapter 6: Risk Assessment, Security Assessment & Monitoring, and Planning

## Core Idea
Families 3.11, 3.12, and 3.15 turn SP 800-171 from a static checklist into a managed program. Organizations assess risk and vulnerabilities, respond to risk, assess control effectiveness, track deficiencies in POA&Ms, monitor continuously, govern information exchanges, and document policy, system security plans, and rules of behavior.

## Frameworks Introduced
- **Risk assessment loop**: Assess → scan/monitor vulnerabilities → respond (accept, mitigate, share, transfer, avoid).
- **Assessment and continuous monitoring**: Periodic security assessments, POA&M discipline, ongoing monitoring, and controlled information exchange.
- **Planning triad**: Policies/procedures, system security plan (SSP), and rules of behavior for users.

## Key Concepts
- **Risk assessment (03.11.01)**: Assess risk (including supply chain considerations as applicable) to operations, assets, and individuals from operation of CUI systems and from information processing/storage/transmission.
- **Vulnerability monitoring and scanning (03.11.02)**: Monitor and scan for vulnerabilities; remediate per risk; share vulnerability information across the enterprise as appropriate.
- **Risk response (03.11.04)**: Respond to findings before operations are adversely affected, consistent with organizational risk tolerance.
- **Security assessment (03.12.01)**: Assess security controls on a defined frequency to determine if they are effective in their application.
- **Plan of action and milestones (03.12.02)**: Document planned remediations for deficiencies, resources required, and scheduled completion; update as status changes.
- **Continuous monitoring (03.12.03)**: Develop and implement a continuous monitoring strategy that includes ongoing assessment metrics and status reporting.
- **Information exchange (03.12.05)**: Approve and manage exchanges of CUI between the system and other systems using agreements, procedures, and monitoring as needed.
- **Policy and procedures (03.15.01)**: Develop, document, disseminate, review, and update family-level policies and procedures for implementing the 800-171 requirements.
- **System security plan (03.15.02)**: Describe system boundaries, environment, relationships, security requirements, and control implementations; update to reflect changes and deficiencies.
- **Rules of behavior (03.15.03)**: Establish and make available rules that describe user responsibilities and expected behavior regarding CUI system usage; receive acknowledgment as required.

## Mental Models
- Risk assessment decides *priority*; assessment/monitoring decides *whether controls still work*; planning documents *what you claim to do*.
- The SSP is the single narrative assessors read first — if a specialized system cannot meet a requirement, the exception lives here.
- POA&Ms are the honest residual-risk ledger; hiding open items is worse than tracking them.
- Continuous monitoring is not only vulnerability scanning — it is the ongoing program that keeps assessment evidence fresh.

## Anti-patterns
- **Point-in-time assessment with no monitoring**: Compliance cliff every audit cycle.
- **POA&M as a parking lot**: Items never funded, never closed, never escalated.
- **SSP that copies requirement text without implementation detail**: Fails both operations and assessment.
- **Unsigned or unknown rules of behavior**: Users never formally accept CUI handling expectations.

## Key Takeaways
1. Risk assessment and vulnerability monitoring drive where to spend scarce remediation effort.
2. Risk response must be intentional — including documented acceptance when appropriate.
3. Security assessments on a defined cadence verify control effectiveness, not just documentation existence.
4. POA&Ms track deficiencies with owners, resources, and dates.
5. Continuous monitoring and information-exchange governance keep the CUI boundary healthy over time.
6. Policies, SSP, and rules of behavior are the planning backbone that makes other families implementable and assessable.

## Connects To
- **ch01**: SSP is the home for enduring scoping exceptions.
- **ch04**: Monitoring consumes audit and configuration evidence.
- **ch05**: Incident lessons feed risk assessment and POA&Ms.
- **ch08**: Supply chain risk ties into 03.11 assessments and acquisition planning.
