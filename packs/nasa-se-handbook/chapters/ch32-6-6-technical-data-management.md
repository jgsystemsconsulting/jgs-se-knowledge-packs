# Chapter 32: 6.6 Technical Data Management

## Core Idea
Technical Data Management ensures that engineering work products—requirements, analyses, decisions, test results, lessons learned—are systematically collected, stored, maintained, and securely distributed to authorized stakeholders throughout the project lifecycle, becoming a persistent knowledge asset for current and future NASA missions.

## Frameworks Introduced
- **Technical Data Management Process**: Systematic capture, maintenance, distribution, and protection of engineering data from conception through disposal.
  - When to use: Every NASA program and project must implement this process to ensure traceability, continuity, and compliance with retention and security regulations (NPR 1441.1, NPR 1600.1).
  - **Inputs**: Project scope, data types to be generated, stakeholder access requirements, security classifications, retention policies, technical plans.
  - **Key Activities**: Plan data infrastructure; collect and store technical work products; perform data integrity checks; maintain databases; distribute data to authorized parties; protect sensitive data (CPI, SBU, ITAR); review system performance periodically.
  - **Outputs**: Secure, accessible technical data in multiple formats; an information library/reference index; proof of data integrity; backups and hazard protection; audit records of access and maintenance.

## Key Concepts
- **Technical Data**: Any information produced during systems engineering and technical management activities—requirements, design descriptions, test results, analyses, recommendations, decisions, assumptions, lessons learned, anomalies, deviations from plan, and traceability records.
- **Critical Program Information (CPI)**: Sensitive data that reveals a system's distinctive operational capability, including components, design/manufacturing processes, technologies, system capabilities, and vulnerabilities; requires special protection procedures.
- **Sensitive But Unclassified (SBU)**: Data marked per NID 1600.55 that requires controlled dissemination but is not classified; examples include design models, limited-rights data, bid/proposal information, financial data, and emergency contingency plans.
- **International Traffic in Arms Regulation (ITAR)**: U.S. export control framework administered by the Department of State; designates defense articles and technical data on the United States Munitions List (USML) requiring controlled access and licensing.
- **Data Integrity**: Assurance that collected data comply with content/format standards, contain no errors in specification/recording, and remain valid, complete, accurate, current, and traceable throughout storage and distribution.
- **Access Control**: Restrictions limiting data availability to authorized personnel on a need-to-know basis, enforced at the file level in the data management system.
- **Data Maintenance**: Periodic review and update of data collection procedures, quality checks, version control, and system performance; includes correcting errors, mitigating impacts, and handling anomalies.

## Mental Models
- **Think of technical data as organizational memory.** Data captured during design reviews, testing, anomaly resolution, and decision-making become the institutional record that explains *why* the system was built the way it was. This record is essential for troubleshooting, modification, and knowledge transfer to future projects.
- **View data management infrastructure as a dual-priority stack.** Primary priority is accessibility and ease of input (so engineers *will* capture data); secondary priority is assessing the long-term value of data to current and future programs and to NASA's engineering knowledge base.
- **Use the four questions about data value as a gate.** Before deciding to retain or archive data, ask: (1) Does it describe the product being built? (2) Is it required to produce that product? (3) Does it offer insight for future programs? (4) Does it hold key learning for NASA's knowledge base? Data that answer "no" to all four should be explicitly disposed of; data answering "yes" to any require long-term stewardship.

## Anti-patterns
- **Choosing tools for technical sophistication over usability.** A data management tool with powerful features but poor search, cumbersome input workflows, or unclear permission models will result in incomplete data capture and low adoption.
- **Conflating temporary project data with permanent engineering records.** Not all data generated during a project need the same retention, security, and access controls; applying SBU or CPI protections to routine project artifacts creates overhead that diverts resources from protecting genuinely sensitive information.
- **Relying on passive access control.** Marking documents SBU or storing them in locked filing cabinets is necessary but insufficient; active safeguards include copy control, attended use, secure transmission (PKI/encrypted email, not standard email or WebEx), and approved destruction (shredding, incineration).

## Key Takeaways
1. **Plan data management infrastructure at project start.** Do not defer decisions about data storage, access, retention, and security tools until the project is underway; unplanned data sprawl becomes difficult and expensive to remediate.
2. **Implement data integrity checks as a continuous activity.** Periodic validation of collected data for completeness, validity, accuracy, and currency prevents silent data corruption and ensures that downstream decision-making rests on reliable artifacts.
3. **Link data capture to the technical and technical management processes.** Specify *when* (in which process steps), *what* (which data types), *by whom*, and *in what format* data will be collected; without this orchestration, critical work products are lost or duplicated.
4. **Balance security classification with usability.** SBU, CPI, and ITAR data require special handling (encrypted transmission, air-gapped storage, role-based access), but overly restrictive controls can stall collaboration; establish clear criteria for who has access and through what channels.
5. **Establish proof of data correctness and system reliability.** Provide evidence (audit logs, hash checks, backup schedules, hazard-resilience plans) that technical data are secure, backed up, and resilient against foreseeable threats (fire, flood, earthquakes, unauthorized intrusion).
6. **Maintain traceability from data source to storage to distribution.** Track who created each data artifact, when it entered the system, who accessed it, and to whom it was delivered; this chain of custody is essential for compliance with NPR 1441.1 (Records Management) and for forensic analysis if disputes arise.

## Connects To
- **NASA Policy Requirement (NPR) 1441.1, Records Management Program Requirements**: Specifies retention and disposal requirements for NASA records; Technical Data Management Process must classify data items against these rules to determine mandatory hold periods.
- **NASA Policy Requirement (NPR) 1600.1, Security Program Procedural Requirements**: Establishes procedures for handling SBU data, CPI, and other sensitive information; Technical Data Management must implement and enforce these safeguards.
- **NASA Policy Requirement (NPR) 1600.55, Sensitive But Unclassified (SBU) Controlled Information**: Provides marking standards, transmission rules (PKI for email, no WebEx), storage controls (locked containers, secure servers), and approved destruction methods for SBU documents and data.
- **International Traffic in Arms Regulation (ITAR), 22 CFR 120–121**: U.S. export control framework; any technical data or software defined as USML defense articles or defense services requires explicit compliance and may trigger licensing requirements for foreign access.
- **ISO/IEC/IEEE 15288, Systems and Software Engineering—System and Software Engineering Life Cycle Processes**: Aligns with the broader SE lifecycle; Technical Data Management supports traceability, configuration management, and knowledge continuity across process areas.
- **Configuration Management Process (Section 6.5)**: Overlaps with Technical Data Management in version control, access control, and change tracking; CM tools often provide the primary infrastructure for data storage and retrieval.
