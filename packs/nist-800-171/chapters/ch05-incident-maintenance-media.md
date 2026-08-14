# Chapter 5: Incident Response, Maintenance, and Media Protection

## Core Idea
Families 3.6, 3.7, and 3.8 cover what happens when things go wrong, when systems are serviced, and when CUI rides on removable or backup media. Together they ensure incidents are handled under a plan, maintenance does not become a back door, and media is stored, marked, transported, sanitized, and cryptographically protected as needed.

## Frameworks Introduced
- **Incident response capability**: Handling capability + monitoring/reporting + testing + training + documented plan.
- **Controlled maintenance**: Tools, nonlocal maintenance sessions, and vetted maintenance personnel.
- **Media protection chain**: Storage, access, sanitization, marking, transport, use restrictions, and cryptographic protection of backups.

## Key Concepts
- **Incident handling (03.06.01)**: Implement an operational capability covering preparation, detection/analysis, containment, eradication, and recovery for CUI systems.
- **Monitoring, reporting, assistance (03.06.02)**: Track incidents; report organizationally defined details to designated authorities on defined timelines; provide support to users.
- **Testing and training (03.06.03–04)**: Test the IR capability; train personnel with IR roles before they take those roles and refresh periodically.
- **Incident response plan (03.06.05)**: Maintain a plan that defines structure, roles, reporting, requirements to external bodies, and metrics; review and update it.
- **Maintenance tools (03.07.04)**: Approve, control, and monitor tools; check media containing diagnostic programs for malicious code; prevent unauthorized removal of maintenance equipment.
- **Nonlocal maintenance (03.07.05)**: Authorize, monitor, and control nonlocal maintenance and diagnostic activities; use strong authentication; terminate sessions and network connections after completion.
- **Maintenance personnel (03.07.06)**: Maintain a list of authorized maintenance organizations/personnel; ensure non-escorted personnel have required access authorizations; supervise those without sufficient clearance/access.
- **Media storage and access (03.08.01–02)**: Physically control and securely store CUI media; restrict access to authorized users.
- **Sanitization (03.08.03)**: Sanitize media before disposal, release, or reuse using approved techniques.
- **Marking (03.08.04)**: Mark media indicating distribution limitations, handling caveats, and applicable CUI markings.
- **Transport (03.08.05)**: Protect and control media during transport; maintain accountability; use authorized custodians.
- **Media use (03.08.07)**: Restrict use of certain media types on CUI systems using organizational policy and technical controls.
- **Backup cryptographic protection (03.08.09)**: Protect the confidentiality of backup CUI with cryptography.

## Mental Models
- IR is a practiced capability (plan + trained people + tested procedures), not a binder on a shelf.
- Maintenance is privileged access in disguise — remote vendor sessions need the same rigor as admin remote access.
- Media is a portable CUI system: mark it, lock it, track it, wipe it, encrypt backups.
- Sanitization standards matter more at disposal time than any label on the shelf.

## Anti-patterns
- **IR plan that only lists phone numbers**: Missing containment/eradication/recovery playbooks and external reporting triggers.
- **Unmonitored vendor remote desktops**: Nonlocal maintenance without session control is a common breach path.
- **Tossing disks without sanitization**: Residual CUI on retired media is a classic compliance and incident finding.
- **Unmarked USB drives with CUI**: Breaks handling rules and multiplies loss impact.

## Key Takeaways
1. Incident handling spans the full lifecycle and must be tested and staffed with trained personnel.
2. Reporting timelines and authorities are ODP-driven — contracts often tighten them further.
3. Maintenance tools and personnel are in-scope attack surfaces; authorize and supervise them.
4. Nonlocal maintenance requires strong authentication and clean session teardown.
5. Media controls cover the physical lifecycle from creation through sanitization.
6. Backup confidentiality (crypto) is called out even though broad contingency planning was tailored out.

## Connects To
- **ch04**: Audit logs fuel detection and post-incident analysis.
- **ch02**: Remote access and authentication requirements bind nonlocal maintenance.
- **ch07**: Cryptographic protection requirements align with backup and media encryption.
- **ch06**: POA&Ms and assessments often track IR exercise findings and media-control gaps.
