# Chapter 3: IDENTIFY (ID) Function

## Core Idea
IDENTIFY establishes a clear understanding of the organization's current cybersecurity risks by inventorying assets, conducting risk assessments, and identifying improvement opportunities — providing the situational awareness that enables all other Functions to be prioritized effectively.

## Frameworks Introduced
- **IDENTIFY (ID)**: The Function that generates the risk understanding — asset inventory, threat and vulnerability analysis, and continuous improvement identification — needed to make informed decisions across the CSF.
  - When to use: as an ongoing activity that precedes and informs PROTECT, DETECT, RESPOND, and RECOVER prioritization.

## Key Concepts
- **Asset Management (ID.AM)**: Identifying and managing assets (data, hardware, software, systems, facilities, services, people, and supplier-provided services) consistent with their relative importance to organizational objectives and risk strategy; includes life-cycle management (ID.AM-08) and data/metadata inventories (ID.AM-07).
- **Risk Assessment (ID.RA)**: The process of identifying vulnerabilities (ID.RA-01), receiving threat intelligence (ID.RA-02), characterizing internal and external threats (ID.RA-03), estimating likelihood and impact (ID.RA-04), and prioritizing risk responses (ID.RA-05 through ID.RA-06).
- **Improvement (ID.IM)**: Identifying opportunities to enhance cybersecurity risk management processes across all CSF Functions through evaluations (ID.IM-01), tests and exercises (ID.IM-02), operational execution (ID.IM-03), and maintenance of incident response and operational plans (ID.IM-04).
- **Cyber Threat Intelligence**: Threat information received from information sharing forums and sources (ID.RA-02) and used to contextualize vulnerabilities and inform risk prioritization.
- **Asset Prioritization (ID.AM-05)**: Assets are classified and prioritized based on criticality, resource requirements, and mission impact — not treated as a flat inventory.
- **Vulnerability Disclosure Process (ID.RA-08)**: Established processes for receiving, analyzing, and responding to externally-reported vulnerabilities, covering both acquisition-time (ID.RA-09, ID.RA-10) and operational assessments.
- **Inherent Risk**: The level of risk to the organization before any risk responses are applied; understood by combining threats, vulnerabilities, likelihoods, and impacts (ID.RA-05).
- **Network Communication Representations (ID.AM-03)**: Maintained diagrams or records of authorized network communication and internal/external data flows, enabling both asset management and anomaly detection.

## Mental Models
- Use IDENTIFY before PROTECT: without knowing what assets exist and how they are prioritized, safeguards cannot be targeted at what matters most.
- Use ID.IM as the improvement engine: every evaluation, test, and operational execution is an input to refining the program — treat IDENTIFY as a learning system, not a one-time assessment.
- Use ID.RA-09 and ID.RA-10 as supply chain gates: assess hardware/software authenticity and critical supplier posture before acquisition, not after deployment.

## Anti-patterns
- **Static asset inventories**: ID.AM-08 requires life-cycle management; inventories that are not updated as assets are acquired, modified, or decommissioned create blind spots in risk assessments.
- **Risk assessment without threat intelligence integration**: ID.RA-02 and ID.RA-07 require active intake of external threat intelligence and change/exception tracking; internally-only-scoped assessments miss emerging risks.

## Key Takeaways
1. Asset management (ID.AM) is the foundation: you cannot assess, protect, detect, or respond to risks involving assets you do not know exist.
2. Risk assessment (ID.RA) is a complete loop — from identifying vulnerabilities through prioritizing responses — not merely a vulnerability scan.
3. Supply chain risk enters IDENTIFY at acquisition time: assess hardware/software integrity (ID.RA-09) and critical suppliers (ID.RA-10) before onboarding.
4. Improvement (ID.IM) makes IDENTIFY self-correcting: lessons from incidents, exercises, and operational execution feed back into better risk management processes.
5. Data and metadata inventories (ID.AM-07) are an explicit outcome, reflecting the increasing importance of data as a critical organizational asset.
6. Network flow representations (ID.AM-03) serve double duty: asset management visibility and a reference baseline for anomaly detection in DETECT.

## Connects To
- **GOVERN (GV)**: Risk strategy and priorities from GOVERN determine which assets and risks IDENTIFY focuses on; improvements identified in ID.IM may trigger GOVERN policy updates.
- **PROTECT (PR)**: Asset classification and risk prioritization from IDENTIFY directly guide which safeguards are applied and where.
- **DETECT (DE)**: Network flow baselines and threat intelligence from IDENTIFY inform what DETECT monitors for.
- **SP 800-30 (Guide for Conducting Risk Assessments)**: Detailed methodology for the risk assessment activities covered by ID.RA.
- **SP 800-161r1**: Supply chain risk management practices that operationalize ID.RA-09 and ID.RA-10 supplier assessment requirements.
