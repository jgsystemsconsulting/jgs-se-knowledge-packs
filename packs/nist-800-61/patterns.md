# Patterns — NIST SP 800-61 Rev. 3

## 1. CSF-Aligned IR Operating Model
- **When:** Migrating from r2-style circular IR or standing up IR in a CSF shop.
- **How:** Map existing phases to GV/ID/PR vs DE/RS/RC; put ID.IM on a continuous cadence; reuse CPRT mappings.
- **Trade-offs:** Taxonomy onboarding cost vs shared language with enterprise risk and vendors.

## 2. Community Profile Tailoring Workshop
- **When:** Adopting Table 2/3 priorities.
- **How:** Score each row against mission/regulators/threats; raise/lower H/M/L; select applicable R/C items; record owners.
- **Trade-offs:** Facilitation time vs blind copy of NIST starting priorities.

## 3. Authority Matrix Before Tools
- **When:** Policy rewrite or post-incident blame cycles about who can isolate systems.
- **How:** Define confiscate/disconnect/shutdown authorities, severity tiers, and executive triggers in policy; exercise them.
- **Trade-offs:** Political negotiation upfront vs frozen response during impact events.

## 4. Hybrid Handler Capacity Model
- **When:** Org cannot staff 24/7 elite IR alone.
- **How:** Combine internal tier-1, MSSP/CSP surge, and specialist retainers; federate process and data sharing.
- **Trade-offs:** Vendor management overhead vs depth on rare high-impact incidents.

## 5. Playbook Minimum Set
- **When:** Procedures exist only as prose.
- **How:** Author playbooks for top incident types plus emergency rebuilds (identity, core network, backup restore).
- **Trade-offs:** Authoring/maintenance load vs speed and consistency under stress.

## 6. Threat-Informed Detection Tuning
- **When:** High false positives or missed activity.
- **How:** Feed cyber threat information into DE.CM; tune; cover networks, hosts, physical, personnel, and providers.
- **Trade-offs:** Analyst/content engineering time vs alert fatigue and blind spots.

## 7. Declaration Criteria Catalog
- **When:** Ambiguous handoff from monitoring to IR.
- **How:** Write DE.AE declaration criteria by scenario; link to severity and RS.MA entry points.
- **Trade-offs:** Rigid criteria vs chaotic ad hoc declarations — revisit after exercises.

## 8. Evidence-Preserving Containment
- **When:** Live response actions may destroy forensics.
- **How:** Playbooks state order of operations: snapshot/collect → contain → eradicate; legal hold hooks.
- **Trade-offs:** Slightly slower mitigation vs lost root-cause and legal options.

## 9. Recovery Integrity Gate
- **When:** Pressure to “just restore.”
- **How:** Enforce backup integrity verification and formal recovery declaration criteria (RC.RP).
- **Trade-offs:** Longer restore clocks vs reinfection and silent integrity failures.

## 10. Lessons-Within-24-Hours Rule
- **When:** Culture delays learning until after full recovery.
- **How:** Require interim lessons tickets into ID.IM during DE/RS as well as post-incident reviews.
- **Trade-offs:** Noise management vs faster detection/protect updates on active campaigns.

## 11. External Coordination Pack
- **When:** Third parties touch detection, hosting, or notifications.
- **How:** Pre-stage contacts, SLAs, data-sharing templates, and joint exercise invitations.
- **Trade-offs:** Relationship maintenance vs first-contact-during-breach failure mode.

## 12. Executive Decision Drills
- **When:** Leadership only sees tabletop slides.
- **How:** Exercise shutdown, disclose, engage law enforcement, and third-party escalation decisions with timers.
- **Trade-offs:** Executive time vs high-impact hesitation during real incidents.
