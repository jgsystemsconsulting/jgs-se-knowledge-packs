# Chapter 4: Community Profile — Preparation and Lessons Learned

## Core Idea
Table 2 of the CSF 2.0 Community Profile covers Govern, Identify, and Protect preparation plus Identify-Improvement (lessons learned). Most rows are lower IR-relative priority because they are not unique to executing incidents — yet they determine whether DE/RS/RC can succeed.

## Frameworks Introduced
- **Preparation band (GV / ID / PR)**: Strategy, asset/risk understanding, and safeguards that prevent and pre-position response.
- **Lessons learned band (ID.IM)**: Continuous improvement Category that absorbs lessons from all Functions and feeds changes back.
- **Priority + R/C/N annotation scheme**: High/Medium/Low IR relevance with recommendations, considerations, and notes.

## Key Concepts
- **Govern highlights for IR**: Understand mission, stakeholders, and legal/regulatory/contractual duties including breach notification; know critical services external parties depend on and critical external dependencies you rely on; include cyber risk in ERM; establish risk appetite/tolerance and standardized risk calculation methods that later drive incident prioritization; set communication lines for supplier/third-party risk.
- **Identify highlights**: Asset inventories and risk assessments that tell responders what matters; vulnerability and threat awareness; improvement processes that capture exercise and incident lessons quickly.
- **Protect highlights**: Safeguards (identity, data security, platform hardening, awareness, resilience) that reduce incident frequency and impact and preserve forensic/recovery options (e.g., logging, backups).
- **Improvement (ID.IM)**: Evaluate lessons from operations, exercises, and incidents; update response plans and broader CRM practices without waiting for a single end-of-incident gate.
- **Priority interpretation**: Low/Medium on prep rows does not mean “skip” — it means “not unique to active response.” Mission context may raise them.
- **Inheritance rule**: R/C/N at Function or Category level apply downward to component Subcategories.
- **Non-comprehensiveness**: Annotations supplement CSF resources; not all apply to every organization; technology examples age.

## Mental Models
- Preparation debt becomes response latency: weak asset inventories and unclear authorities show up as slow triage.
- Use standardized risk methods (GV.RM) so incident severity scoring matches how the enterprise already ranks risk.
- Map notification duties (GV.OC legal/regulatory) before the first reportable incident.
- Treat ID.IM as a product backlog fed by detections, near-misses, and recovery friction — not only catastrophic breaches.

## Anti-patterns
- **Starving prep because Table 2 priorities look lower**: The Profile’s IR-relative ranking is not an enterprise risk ranking.
- **Lessons learned wiki that never changes controls or playbooks**: Improvement without change control is theater.
- **Ignoring external dependency mapping**: Cloud/MSSP failures become unprioritizable surprises during response.

## Key Takeaways
1. Table 2 is the preparation and continuous-improvement half of the IR Community Profile.
2. Legal/notification context and dependency mapping are governance prerequisites for sane response prioritization.
3. Risk appetite and standardized risk methods connect CRM to incident severity decisions.
4. Protect safeguards are IR controls in slow motion — they shape blast radius and recoverability.
5. ID.IM must run continuously, not only after recovery.
6. Customize priorities upward when sector rules or mission criticality demand it.

## Connects To
- **ch02**: Where GV/ID/PR and ID.IM sit in the life-cycle figure.
- **ch03**: Policies and roles that implement Govern outcomes.
- **ch05**: Active response half of the Profile (Table 3).
- **nist-csf**: Full Category/Subcategory definitions.
