# Chapter 3: Roles, Responsibilities, Policies, and Playbooks

## Core Idea
Successful incident response depends on a wide cast — leadership, handlers (internal/contracted/on-demand), technology professionals, legal, public affairs, HR, physical security, asset owners, and third parties — governed by policy and made executable through processes, procedures, and playbooks.

## Frameworks Introduced
- **Distributed IR responsibility model**: Many internal and external roles beyond a single IR team.
- **Policy → process → procedure → playbook stack**: Governance statements cascade into testable, trainable actions.
- **Federated multi-team coordination**: Large orgs with multiple IR teams still need one coordinated entity for consistency and information sharing.

## Key Concepts
- **Leadership**: Oversight, funding, and authority for high-impact actions (e.g., shutting down critical services).
- **Incident handlers**: Verify incidents, collect/analyze evidence, prioritize actions, limit damage, find root causes, restore operations; may be staff, MSSP/CSP teams, parent org, partners, or law enforcement surge support. Hybrid models are common.
- **Technology professionals**: Security, privacy, system, network, cloud engineers, admins, and developers engaged in response/recovery.
- **Legal**: Review plans/policies for legal compliance and privacy; advise on supplier contracts, prosecution, lawsuits, MOUs.
- **Public affairs / media relations**: Media and public notification strategy; prepare for leaks via alternate sources.
- **Human resources**: Screening/onboarding/offboarding linkages; involvement when insider causation is suspected.
- **Physical security and facilities**: Physical breach paths, coordinated physical/logical attacks, facility access for handlers.
- **Asset owners**: Prioritization insight and status consumers for affected systems/data/processes.
- **Third parties**: Primary operators (e.g., MSSP) or supporting providers (CSP IR teams, telecom, vendors) with contractual IR obligations.
- **Policy key elements**: Management commitment; purpose/objectives; scope; definitions; roles/authorities (including who may confiscate/disconnect/shut down); prioritization and severity guidelines; recovery initiation guidance; performance measures.
- **Procedures**: Document how technical and operational steps run; exercise them; prioritize common incident types and emergency-critical processes (e.g., rebuilding primary authentication).
- **Playbooks**: Actionable task lists for scenarios; improve usability versus prose procedures; CISA IR/vulnerability playbooks cited as examples of the form.

## Mental Models
- Build an IR RACI across Functions before writing tools wish-lists.
- Authority to take disruptive actions must be pre-decided in policy — not improvised at 2 a.m.
- Playbooks are for humans under stress: short steps, clear owners, explicit decision forks.
- Third-party IR capacity is part of your capability model only if contracts, contacts, and data-sharing paths are real.

## Anti-patterns
- **Hero-handler culture**: One brilliant analyst with no legal/comms/owner hooks.
- **Policy without authorities**: Beautiful principles, no one allowed to isolate a segment.
- **Unexercised procedures**: Documents that fail on first use during authentication outages or ransomware.
- **Multiple IR teams without federation**: Inconsistent severity scoring and missed lateral movement.

## Key Takeaways
1. IR is a multi-role enterprise capability, not solely an IR team specialty.
2. Handler capacity can be staffed, contracted, on-demand, or combined — design deliberately.
3. Legal, HR, facilities, and communications are first-class IR participants.
4. Policies must define terms, authorities, prioritization, and measures.
5. Procedures and playbooks translate policy into trainable, testable action.
6. Large organizations should federate multiple teams under consistent process and sharing norms.

## Connects To
- **ch02**: Life-cycle Functions these roles populate.
- **ch04**: Governance and training preparation outcomes.
- **ch05**: Response communications and recovery coordination outcomes.
- **ch06**: Coordination patterns with external parties and information sharing.
