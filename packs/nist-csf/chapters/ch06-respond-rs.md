# Chapter 6: RESPOND (RS) Function

## Core Idea
RESPOND covers the actions taken once a cybersecurity incident is declared — managing the response, conducting analysis to establish root cause and magnitude, containing and eradicating the incident, and coordinating communications with internal and external stakeholders as required by law, regulation, or policy.

## Frameworks Introduced
- **RESPOND (RS)**: The Function that activates when DETECT declares an incident; it contains the effects of cybersecurity incidents through managed, analyzed, communicated, and mitigated responses.
  - When to use: when DE.AE-08 incident declaration criteria are met; response plans (ID.IM-04) must be ready before incidents occur.

## Key Concepts
- **Incident Management (RS.MA)**: Executing the incident response plan in coordination with relevant third parties (RS.MA-01), triaging and validating incident reports (RS.MA-02), categorizing and prioritizing incidents (RS.MA-03), escalating as needed (RS.MA-04), and applying recovery initiation criteria (RS.MA-05).
- **Incident Analysis (RS.AN)**: Conducting investigations to establish what occurred and the root cause (RS.AN-03), preserving the integrity and provenance of investigation records (RS.AN-06) and collected incident data and metadata (RS.AN-07), and validating the estimated magnitude of the incident (RS.AN-08).
- **Incident Response Reporting and Communication (RS.CO)**: Notifying internal and external stakeholders of incidents (RS.CO-02) and sharing information with designated parties (RS.CO-03), in accordance with legal, regulatory, and policy obligations.
- **Incident Mitigation (RS.MI)**: Activities to prevent expansion of the incident (RS.MI-01, containment) and eradicate the threat from affected systems (RS.MI-02, eradication).
- **Incident Triage (RS.MA-02)**: The validation and preliminary classification of incident reports to distinguish genuine incidents from false positives and to determine initial priority.
- **Root Cause Analysis (RS.AN-03)**: Investigation to establish the sequence of events, attack vector, and underlying conditions that allowed the incident to occur — critical for preventing recurrence.
- **Record Integrity and Provenance (RS.AN-06, RS.AN-07)**: The requirement that investigation records and collected incident data be preserved with integrity and documented provenance to support forensics, legal proceedings, and post-incident learning.
- **Recovery Initiation Criteria (RS.MA-05)**: Defined conditions that, when met, authorize the transition from active incident response to the RECOVER Function.

## Mental Models
- Use RS.MA before RS.AN: triage and prioritization (RS.MA-02, RS.MA-03) determine where to focus analytic resources; undirected forensic analysis wastes critical response time.
- Use RS.AN-06 and RS.AN-07 from the first action: preserving record integrity and provenance cannot be retrofitted after investigation actions have been taken.
- Use RS.CO-02 proactively: notification obligations under laws and regulations (e.g., breach notification requirements) often have fixed deadlines that begin at incident discovery, not at containment.

## Anti-patterns
- **Skipping categorization and prioritization (RS.MA-03)**: Treating all incidents as equal severity prevents resource concentration on high-impact events and delays containment of the most damaging incidents.
- **Containment before analysis completion**: Moving directly to RS.MI-01 without sufficient RS.AN-03 investigation risks containing the visible symptom while leaving the root cause active in the environment.

## Key Takeaways
1. RESPOND is structured as a sequential-but-overlapping flow: manage → analyze → communicate → mitigate; all four happen during active incident response, not in strict linear sequence.
2. The incident response plan (ID.IM-04) must be established, tested, and maintained under IDENTIFY before an incident occurs — RESPOND executes a plan, it does not create one.
3. Third-party coordination is explicit: RS.MA-01 requires execution with relevant third parties, and RS.CO-03 requires information sharing with designated stakeholders.
4. Record preservation (RS.AN-06, RS.AN-07) is a formal outcome, not an afterthought — forensic integrity and legal defensibility depend on it.
5. Recovery initiation criteria (RS.MA-05) form the formal handoff from RESPOND to RECOVER, preventing premature recovery that leaves threats in place.
6. Communication obligations (RS.CO) are driven by laws, regulations, and policies — organizations must understand their notification timelines before an incident occurs.

## Connects To
- **DETECT (DE)**: Incident declaration (DE.AE-08) is the trigger for RESPOND; detection quality directly affects the speed and accuracy of initial triage (RS.MA-02).
- **RECOVER (RC)**: RS.MA-05 (recovery initiation criteria) is the formal gate between RESPOND and RECOVER; root cause analysis (RS.AN-03) informs recovery planning.
- **IDENTIFY (ID)**: Incident response plans (ID.IM-04) established under IDENTIFY are executed here; improvements identified during response feed back into ID.IM.
- **SP 800-61r2 (Computer Security Incident Handling Guide)**: Detailed NIST methodology for implementing incident management, analysis, communication, and mitigation outcomes.
