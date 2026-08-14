# Chapter 1: Scope Shift and CSF Integration

## Core Idea
NIST SP 800-61 Rev. 3 reframes incident response as an integral part of cybersecurity risk management expressed through CSF 2.0, rather than a standalone circular handling guide. It supersedes SP 800-61r2 and deliberately stops trying to freeze rapidly changing tactical how-to steps in a static publication.

## Frameworks Introduced
- **IR-as-CRM framing**: Incident response considerations span all six CSF 2.0 Functions, not only Detect/Respond/Recover.
- **CSF 2.0 Community Profile for cyber incident risk management**: Prioritized CSF outcomes with recommendations (R), considerations (C), and notes (N) for IR context.
- **Companion resource model**: Use CPRT mappings, the Incident Response project page, and CSF supplemental materials for implementation depth that the SP no longer embeds.

## Key Concepts
- **Purpose**: Help organizations weave IR recommendations into risk management and provide a common language for internal/external communication about IR plans and activities.
- **Scope change from r2**: Earlier revisions emphasized step-by-step incident handling; r3 focuses on risk-management outcomes because tactical details change too quickly across technologies and orgs.
- **Audience**: Cybersecurity leadership, practitioners, and others who prepare for, detect, respond to, or recover from cybersecurity incidents — sector- and size-agnostic.
- **Supersession**: Explicitly replaces SP 800-61 Revision 2 (Computer Security Incident Handling Guide).
- **Event vs incident**: An event is any observable occurrence involving a system, network, or service; a cybersecurity incident is an event (or set of events) that jeopardizes systems/information or violates security policies — organizations must define related terms for their environment.
- **Community Profile mechanics**: Each CSF element gets an IR-relative priority (High/Medium/Low) plus optional R/C/N items identified like `GV.OC-03.R1`.
- **Customization expectation**: Priorities are starting points; organizations tailor the Profile to mission, threat, and regulatory context.

## Mental Models
- Think “IR operating system for the whole CSF,” not “SOC runbook encyclopedia.”
- When you need control mappings or playbooks, leave the SP and follow CPRT / sector playbooks / org procedures.
- Preparation (GV/ID/PR) and lessons learned (ID.IM) continuously shape Detect/Respond/Recover rather than sitting only in a once-per-incident postmortem.

## Anti-patterns
- **Treating r3 as a drop-in replacement for r2 playbooks**: The tactical depth moved out on purpose.
- **Only staffing DE/RS/RC**: Ignoring Govern/Identify/Protect preparation guarantees brittle response.
- **Copying Community Profile priorities unchanged**: Medium/Low prep items can be mission-critical for regulated sectors.

## Key Takeaways
1. SP 800-61r3 integrates incident response into CSF 2.0-aligned cybersecurity risk management.
2. It supersedes the r2 handling guide and points outward for implementation detail.
3. All six CSF Functions matter for IR outcomes.
4. The bulk of actionable content is a two-part Community Profile (preparation/lessons + incident response).
5. R/C/N annotations and High/Medium/Low priorities guide attention without claiming universality.
6. Define org-specific terms (e.g., data breach) against law and mission when adopting the Profile.

## Connects To
- **ch02**: Life-cycle model mapping old phases to CSF Functions.
- **ch04–ch05**: Community Profile tables in depth.
- **nist-csf pack**: Full CSF 2.0 taxonomy this Profile rides on.
- **CPRT / SP 800-53**: Implementation mappings referenced by the publication.
