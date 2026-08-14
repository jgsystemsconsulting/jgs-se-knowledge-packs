# Chapter 2: Incident Response Life Cycle Model (CSF 2.0)

## Core Idea
Rev. 3 replaces the classic four-phase circular IR life cycle (Preparation → Detection & Analysis → Containment/Eradication/Recovery → Post-Incident) with a CSF 2.0 Function model that separates continuous preparation from active incident handling and routes lessons learned continuously through Identify-Improvement (ID.IM).

## Frameworks Introduced
- **Legacy life cycle (Fig. 1 / r2)**: Circular, intermittent IR by a dedicated team when incidents were rarer and shorter.
- **CSF-based life cycle (Fig. 2)**: Bottom layer GV/ID/PR preparation; top layer DE/RS/RC incident handling; middle continuous improvement via ID.IM feeding all Functions.
- **Phase-to-Function mapping (Table 1)**: Crosswalk from r2 phases to CSF Functions (with ID.IM appearing across post-incident and continuous learning).

## Key Concepts
- **Why the model changed**: Modern incidents are frequent, broad, complex, and often take weeks or months; IR must be continuous and enterprise-wide, not a short special-ops loop.
- **Govern (GV)**: Strategy, expectations, and policy established, communicated, monitored — IR authorities and risk appetite live here.
- **Identify (ID)**: Current cybersecurity risks understood — assets, vulnerabilities, threats, and improvement opportunities.
- **Protect (PR)**: Safeguards that prevent some incidents and reduce blast radius when they occur.
- **Detect (DE)**: Find and analyze possible attacks and compromises.
- **Respond (RS)**: Take action on declared incidents (manage, contain, eradicate, communicate).
- **Recover (RC)**: Restore assets and operations; coordinate recovery communications.
- **Preparation vs response**: GV/ID/PR are broader CRM activities that support IR; DE/RS/RC are the incident response execution layer in the figure.
- **Continuous improvement**: Lessons can surface at any time (e.g., characterizing a new threat mid-detection) and should not wait for a formal post-incident meeting before informing policy and practice.
- **Model choice**: Organizations may use another IR life-cycle framework if it fits better; larger/tech-dependent orgs often benefit more from continuous-improvement emphasis. Regardless of model, IR considerations must permeate CRM activities.

## Mental Models
- Preparation is the foundation slab; DE/RS/RC is the active firefight floor; ID.IM is the elevator moving lessons between floors in real time.
- Map your existing playbooks onto CSF Functions so you can reuse CSF tooling and CPRT mappings.
- “Post-incident activity” is no longer a single trailing phase — improvement is always on.

## Anti-patterns
- **Waiting until recovery completes to share lessons**: r3 explicitly rejects delayed learning as the default.
- **IR team as the only actors in the life cycle**: The model assumes enterprise participation.
- **Forcing every org into maximum continuous-improvement ceremony**: Choose intensity appropriate to size and dependency on technology.

## Key Takeaways
1. The r2 circular model assumed rare, short, narrow incidents; that world largely ended.
2. CSF Functions provide the organizing spine for modern IR life cycles in this publication.
3. GV/ID/PR prepare and harden; DE/RS/RC execute response and recovery.
4. ID.IM is the continuous improvement hub linking lessons into every Function.
5. Table 1 is the migration aid for teams steeped in preparation/detection/containment/post-incident vocabulary.
6. Using a coherent life-cycle model matters more than using this one — but IR must still be woven through CRM.

## Connects To
- **ch01**: Why r3 abandoned static tactical depth.
- **ch03**: Roles that populate each Function during incidents.
- **ch04**: Preparation and lessons-learned Profile rows.
- **ch05**: Detect/Respond/Recover Profile rows.
