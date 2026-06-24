# Chapter 27 — Enabling Teams

> Synthesized reference notes from SEBoK v2.14, Knowledge Area **Enabling Teams** (Part 5, Enabling Systems Engineering). Content is transformed for study use under CC BY-NC-SA 3.0; attribution to the BKCASE Project. No long verbatim passages are reproduced.

## Core Idea

This Knowledge Area is about getting a *team* into a state where it can actually do systems engineering — before any of the "how to do SE" material in Part 3 becomes useful. SEBoK situates it deliberately: **Enabling Systems Engineering** (Part 5) treats SE as enabled at three organizational levels — the business or enterprise, the team, and the individual — and this KA owns the *team* level (with **Enabling Businesses and Enterprises** above it and **Enabling Individuals** below). Throughout the KA "business" is shorthand for "business or enterprise."

The framing distinction is sharp: not every group working together is a team. A team is a set of individuals cooperating toward shared objectives under a common vision, with capabilities and dynamics specifically attuned to SE. The KA also widens who counts as a systems engineer — electrical, mechanical, or software engineers; service providers; or IT enterprise architects shops may lead or sit on teams performing SE tasks, and the KA calls all of them "systems engineers" regardless of job title.

Two questions organize the core topics. **Team Capability** answers *how a business determines the value SE teams add* and *how it judges their efficiency and effectiveness*. **Team Dynamics** answers *how group dynamics let systems engineers get work done and hit their goals*. Two further topics round out the KA: **Diversity, Equity, and Inclusion** (both inside the team and in the systems the team designs) and **Technical Leadership in Systems Engineering**. The KA is explicit that it covers *enabling* teams, not *managing* them — questions about managing systems engineers and SE teams are pushed to the Part 6 relationship topics between SE and project management.

## Frameworks Introduced

(Exact SEBoK terms; what each is and when/how it is used.)

- **Team Capability (organize / staff / develop / assess)** — the four-part lifecycle of building a capable SE team. Capability rests on capable staff; enough time; adequate resources and equipment; and fitting policies and procedures (Torres and Fairbanks). The team should have a **charter**, the right attitude, organization, tools, training, and processes such as configuration management and peer review.

- **Integrated Product Team (IPT)** and **system breakdown structure (SBS)** — in **Product Centered Organizations**, an IPT is assigned to each element of the SBS, staffed with the technical disciplines that element needs. Use IPTs when the organizational strategy is product-centered (cross-reference: Systems Engineering Organizational Strategy).

- **SE and Integration Team (SEIT)** and **Analysis and Integration Teams (AITs)** — at the program level a top-level IPT (the SEIT) oversees all lower-level IPTs. Specialists who must span a whole SBS level (reliability, safety) are grouped into AITs, created at whatever SBS levels need them.

- **The 7 ± 2 rule / communication-path arithmetic** — organize communication among engineers knowing the number of paths in a fully connected group of N engineers is N(N−1)/2 (Brooks). 5 engineers → 10 paths; 7 → 21; 9 → 36; a team past ~10 people (45 communication paths) ought to be arranged hierarchically under a top-level leader, partitioned by subsystem or by process activity (analysis, design, integration).

- **The nine-step competency-determination procedure** — to find the *collective* competencies a team needs: identify context (domain, stakeholders, organizational culture, scope, criticality, new-vs-sustainment); clarify responsibilities/authority/communication channels; establish roles; determine required competencies and levels per role; size the headcount; check availability; adjust for shortfalls; organize for communication and coordination; then ask stakeholders "What are we missing?"

- **Competency models as checklists** — INCOSE Systems Engineering Competencies Framework (2010) and the **People Capability Maturity Model (P-CMM)** (Curtis et al.) used as checklists to set needed competencies and levels for a product, enterprise, or service (cross-reference: Roles and Competencies). Competencies are typically *distributed* across a team; one person rarely holds the full list.

- **Tuckman's stages of group development** — **Forming, Storming, Norming, Performing** (Tuckman 1965), with **Adjourning** added later (Tuckman and Jensen 1977). A team needs time to move through these; the original sequence is linear, but groups may move through stages recursively and iteratively (Forsyth).

- **Capability vs. competency** — competency is acquired knowledge and skills; **capability** (Stephenson and Weil) is a holistic attribute — knowing how to learn, being creative, high self-efficacy, applying competencies in novel situations, working well with others. Hase's survey lists the human contributors to capability — capable people; working as teams; a visible vision and values; learning that is assured, managing the complexity of change, human aspects of leadership, change-agency, involving people, developing management talent, organizational-development commitment).

- **Robbins' four-point team-assessment design** — to evaluate team performance: tie team results to organizational goals; start from the team's customer and work process; measure both team and individual performance against organizational norms/benchmarks; and train the team to build its own measures. SEBoK then re-states each point in SE terms (e.g., the SE team's end product is the *delivered* product/service, not just SE work products).

- **NASA APPEL assessments** — the Academy of Program/Project and Engineering Leadership delivers targeted interventions and four assessment types: Project/Team Effectiveness, Individual Effectiveness, Project/Team Process Utilization, and Project/Team Knowledge.

- **Capability-building techniques** — **pilot projects** (skills acquisition and/or feasibility, combinable as proof-of-concept studies), **post-mortem analysis** (with named mechanisms: third-party facilitator, brainstorming, **SWOT analysis**, **fishbone / Ishikawa diagrams**, mind mapping), and **lessons learned** (positive and negative, fed forward into team formation on the next project).

- **Six descriptors of group nature (Forsyth)** — **interaction, goals, interdependence, structure, cohesion (unity), and stage** — the lens the Team Dynamics topic uses to describe any group.

- **Bales' interaction categories** — group interactions split into **socio-emotional** and **task** interactions (Bales 1950, 1999).

- **McGrath's Circumplex Model** — categorizes group tasks into four quadrants on two axes: *choose vs. execute* (X) and *generate vs. negotiate* (Y).

- **Five types of interdependence (Forsyth)** — mutual/reciprocal; unilateral; reciprocal-unequal; serial; multi-level.

- **Group roles (Benne and Sheats)** — beyond leader and follower, emergent roles include information seeker, information giver, elaborator, procedural technician, encourager, compromiser, harmonizer; roles and **norms** (formal and informal) make up group structure.

- **DEI definitions (ABET 2020)** — **Diversity** (the range of human differences), **Equity** (fair treatment/access/opportunity by intentional focus on disparate needs), **Inclusion** (proactive, continuing practices in which all members respect, support, and value others). DEI is the compound subject area.

- **Categorized Dimensions of Diversity** — 28 characteristics recognized by INCOSE (Harding and Pickard 2019), sorted into five areas — intrinsic; employment; environment; interaction; and family.

- **Inclusive Engineering** and the **Inclusive Engineering Framework** — the discipline of making engineering products/services accessible to and inclusive of all users, free of discrimination and bias; the framework (Bonfield) has eight elements that systems engineers should address even when stated requirements omit them.

- **DEI mapped to ISO/IEC/IEEE 15288:2015 Technical Processes** — a table mapping inclusive-engineering considerations onto Business or Mission Analysis, Stakeholder Needs and Requirements Definition, System Requirements Definition, Architecture Definition, Design Definition, System Analysis, Implementation, Integration, Verification, Transition, Validation, Operation, Maintenance, and Disposal — including identifying "unwilling" stakeholders and ensuring an equitable transition plan.

- **Leadership Models vs. Styles** — **Models** describe *how* leadership arises and operates (situational, charismatic); **Styles** describe the *manner* of leading (task- vs. people-focused; autocratic / democratic / laissez-faire, per Lewin et al. 1939).

- **Trait / "Great Man" theories and the Five-Factor model** — the search for born-leader traits; the current best consensus is five personality dimensions — **Extraversion, Agreeableness, Conscientiousness, Neuroticism, Openness** — valid across literate populations but not necessarily universal (Gurven et al.).

- **Transactional vs. Transformational leadership (Burns 1978)** — transactional is allied to management (defined outputs, reward/punish); **transformational** develops people, builds trust, creates shared vision, and is usually considered the most valuable form, essential for culture, safety, adaptability, and learning.

- **Contingency Model (Fiedler 1964)** — no single best style; effectiveness is the *match* between style (task- or relationship-oriented, assessed via the **Least Preferred Co-worker / LPC** measure) and situation (group support, task structure, reward/punish power).

- **Situational Theory (Hersey, Blanchard, Johnson)** — the leader adapts among four modes — **delegating, supporting, coaching, directing** — to the team's needs; leadership is a learned skill grounded in context and self-awareness.

- **Path-Goal Theory (House and Mitchell 1974)** — the leader is a facilitator who helps followers develop behaviors to reach their goals (providing resources, knowledge, support); in SE this means opening communication pathways between areas and encouraging integrated perspectives.

- **Authentic Leadership** — staying true to one's natural style, with four behaviors: **balanced processing, internalized moral perspective, relational transparency, and self-awareness** (Gardner et al.).

- **Servant Leadership** — leader as facilitator; elements such as empowerment; standing back and sharing credit; courage and risk-taking; humility; authenticity; and stewardship correlated significantly with innovation output in engineering teams (McCleave and Capella 2015).

- **Complexity Leadership** — leadership promotes emergent adaptive outcomes in organizations seen as complex adaptive systems; takes three forms — **administrative, adaptive, enabling** — that disentangle bureaucratic coordinating structures from adaptive functions (Marion & Uhl-Bien). Leadership here is a *function*, not necessarily a person.

- **Followership** — a leader needs effective followers; Uhl-Bien et al. (2014) frame it via a **role-based** and a **process** approach, supporting distributed leadership where authority flows from technical knowledge rather than a desire to lead.

- **Motivation models** — intrinsic vs. extrinsic motivation; Maslow's **Hierarchy of Needs** (flagged as lacking scientific validity and culturally narrow); **Expectancy Theory** (Vroom) built on **valence, instrumentality, expectancy**, the more actionable basis for empowerment; and **organizational energy** (Cole, Bruch, Vogel) — productive, resignative, corrosive, comfortable.

- **Goleman's five emotional competence categories** — **self-awareness, self-regulation, motivation, empathy, social skills** (first three about self-management, last two about relationships), most associated with transformational and situational leadership.

- **Wilson Social Styles** — integrates four leadership styles (**Driver, Analytical, Amiable, Expressive**) with communication styles plotted on **assertiveness** (tell- vs. ask-oriented) and **responsiveness** (task- vs. people-oriented) axes (Wilson 2004).

- **MBTI (Myers-Briggs Type Indicator)** — Jung's three continuums plus a judging–perceiving fourth, yielding 16 types; useful for self-development and insight into interaction/communication styles, but explicitly *not* a valid basis for selection (it measures preference, not ability).

- **System Engineering Plan (SEP) vs. System Engineering Management Plan (SEMP)** — in U.S. DoD acquisition, the SEP is a government-produced document directing the technical approach; the SEMP is the developer/contractor's standalone, coordinated document that aligns with it.

## Key Concepts

- **Organizing precedes staffing precedes developing precedes assessing.** Team structure depends on project nature, size, scope, organizational preference, and external constraints (a larger embedding program). SE teams may act as technical leads, consultants, or advisers, and may be matrixed from a functional unit or permanently attached to a project. A team can be organized **by job specialization** (each member/sub-team owns a function — requirements, architecture, integration, V&V, field test, install/train — coordinated by a lead) or **by subsystem** (each member/sub-team does all functions for one subsystem, with a top-level team coordinating allocation, interfaces, integration, and V&V).

- **Two reporting geometries, one requirement to synchronize.** The SE team may sit *subordinate to project management*, or project management may sit subordinate to SE (with SE as the authoritative customer interface). Either way, SE and project management must work synergistically to balance product attributes, schedule, and budget. These geometries scale up to the program level (a top-level SE team coordinating subordinate projects) and down to a single systems engineer doing the SE work.

- **Collective competency is more than the sum of individual competencies.** What a team needs depends on domain, stakeholders, scope, criticality, new-vs-enhancement, and the team's assigned responsibility and authority — the competencies to architect a small company's IT enterprise differ sharply from those to engineer a globally distributed aircraft. When budget forces a shortfall, compromises follow (e.g., the architect doubles as lead engineer; the requirements engineer also runs integration and test despite a lower competency level there).

- **Cohesion is the engine of synergy.** A cohesive SE team has a strong sense of commitment to the work and to each other, producing performance greater than the sum of individuals. Indicators (Fairley): clear understanding of roles/responsibilities, shared ownership of work products, willingness to help one another, good communication channels, and enjoyment of working together. Cost and time to cohesion shrink with good selection and management, consistent cross-business training (common language/framework), good "infostructure" for information sharing, and shared norms and values — but cross-site, inter-company, and international teams need *more* time to form.

- **Individual goals must be satisfied alongside team goals.** SE teams are more effective when each member's work also advances their individual goals, not just the team's and organization's (Fraser).

- **Assess the team, not only individuals.** Performance evaluation is historically individual (Robbins notes individuals were long seen as the core building blocks), but team capability and performance must be assessed too — and letting the team define its own measures both clarifies roles and builds cohesion.

- **Groups are inescapable and synergistic.** Humans are social animals; group dynamics exceed the sum of member interactions and create synergistic behaviors and results. A team cannot perform effectively without strong cohesion — the interpersonal forces binding members into one unit with boundaries marking insiders from outsiders (Dion).

- **DEI has two faces in SE.** Inwardly: make the team and its leadership inclusive and welcoming of diverse talent, applying equity where needed. Outwardly ("inclusive engineering"): make the realized systems accommodate the differences across the whole stakeholder community. Failing either yields sub-optimal outcomes — missed solutions, lower productivity, or a system that doesn't meet the whole community's needs. The U.S. National Academy of Engineering frames the opportunity cost of homogeneity as "designs not thought of."

- **Equity is not equality.** Equity gives more to those who need it, proportionate to their circumstances, so everyone has the same opportunities — in engineering this can mean extra support or time for a disadvantaged student or a team member with a condition such as dyslexia.

- **Leadership complements management; it is increasingly distributed.** Leadership addresses people's behaviors, thinking, motivation, and energy and creates conditions for shared understanding, innovation, problem solving, resilience, and learning — distinct from management, which directs activities to deliver outputs. In SE, leadership functions are often *distributed* across a team because technical expertise is distributed; silos of self-interest must be broken down (or at least bridged by effective communication and a balance between global system concerns and local disciplinary interests).

- **Match leadership to the situation.** The recurring through-line across the leadership models is that no single style is universally best; effectiveness comes from matching style to situation and context, drawing on social skills, and recognizing that a leader has a preferred comfort zone they revert to under stress (Jung). Good managers are not necessarily good technical leaders and vice versa — the two require different personality traits and skill sets.

## Mental Models

- **A team is a tuned instrument, not a roster.** A group becomes a team only when its capability and dynamics are specifically attuned to SE around a shared vision; assembling competent people is necessary but not sufficient.

- **Communication cost scales quadratically.** N(N−1)/2 paths means a team's coordination burden explodes with size — the practical trigger to go hierarchical sits around 10 members / 45 paths, and is the reason large efforts partition by subsystem or by process activity.

- **Competency is distributed; rarely does one person hold the whole list.** Plan staffing around a *collective* competency set spread across roles, not around finding individual polymaths — then fill gaps consciously and ask stakeholders what's missing.

- **Cohesion compounds into synergy; its absence compounds into dysfunction.** SEBoK presents the cohesion indicators and their negations as mirror images — confused roles, protective ownership, unwillingness to help, poor communication, personal dislike — so the same five dimensions diagnose both health and pathology.

- **Forming-storming-norming-performing is a cost, and it can recur.** Team formation takes real time and money; cross-site and international teams pay more, and the stages can be revisited iteratively rather than passed once.

- **Inclusive teams build inclusive systems.** The wider the range of stakeholder views inside the team, the greater the potential for inclusive products — diversity in the team is itself a source of the innovation that yields better solutions.

- **Leadership is a function before it is a person.** In a complex SE team, leadership can flow in any direction and attach to whoever holds the relevant technical knowledge at a given moment — which is why followership and distributed leadership matter as much as designated leaders.

- **Personality instruments inform, they don't select.** MBTI, Five-Factor, and similar tools aid self-development and interaction insight, but using them (especially MBTI) for selection — particularly into leadership — is not justified by the evidence.

## Anti-patterns

- **Teamicide (DeMarco and Lister).** Management techniques — sometimes unintentional — that reliably kill teams: **physical separation of team members, fragmentation of time, unrealistic schedules, and excessive overtime.**

- **The dysfunctional / non-cohesive team.** The named negations of the cohesion indicators: confusion of roles and responsibilities, protective ownership of work products, unwillingness to help one another, absence of good communication, and personal dislike among team members.

- **Inhibitors to post-mortem analysis.** Failure to allocate time, failure to capture lessons learned, failure to document results, reluctance to be candid about others' performance, and negative social/political dynamics.

- **Inhibitors to lessons learned.** Not studying past lessons during project initiation, not allocating time/resources to document them on the current project, and reluctance to discuss problems and issues.

- **Selecting leaders on the wrong signal.** Elevating the strongest technical performers, or the most ambitious people, is not an effective route to ensure good leadership; companies instead build leadership through academies, coaching, mentoring, shadowing, and managed experience.

- **Extreme leadership/communication styles.** Each Wilson style taken to an extreme becomes a weakness — Drivers micromanage or under-direct and ignore relationships; Analyticals over- or under-inform; Amiables and Expressives play favorites or talk over listening.

## Key Takeaways

- **Enable the team before applying SE process.** This KA is the prerequisite to Part 3 — it makes a group capable of *doing* SE, sitting at the team level between enabling enterprises and enabling individuals.

- **"Systems engineer" is a role, not a title.** Anyone leading or contributing to a team performing SE tasks counts, regardless of their organizational job title.

- **Build capability in four moves: organize, staff, develop, assess.** Underpin them with a charter, the right competencies, processes (CM, peer review), and deliberate cohesion-building (celebrating milestones, off-site and family-inclusive events, the right number of members and competency mix).

- **Size the team's competency collectively and consciously close gaps.** Use INCOSE and P-CMM as checklists, run the nine-step procedure, and when budget forces compromise, make the compromise explicit.

- **Assess the team itself, not just individuals** — tie results to organizational goals, start from the customer and work process, measure at both levels, and let the team build its own measures.

- **Group dynamics are a discipline, not a soft afterthought.** Interaction, goals, interdependence, structure, cohesion, and stage describe every team; strong cohesion is non-negotiable for effective performance.

- **DEI is both a workforce imperative and a design imperative.** Inclusive teams produce better outcomes; inclusive engineering, mapped across all ISO/IEC/IEEE 15288 technical processes, produces systems that serve the whole stakeholder community — including unwilling stakeholders and the natural environment.

- **Lead by matching style to situation, and treat leadership as distributed.** Transformational leadership develops culture and people; contingency, situational, path-goal, authentic, servant, and complexity models all converge on context-fit and social skill; followership and self-leadership distribute the function across the team.

## Connects To

- **Part 5 — Enabling Systems Engineering:** the parent KA; **Enabling Businesses and Enterprises** (including **Determining Needed Systems Engineering Capabilities in Businesses and Enterprises** and **Systems Engineering Organizational Strategy**) above, and **Enabling Individuals** (with **Roles and Competencies** and **Assessing Individuals**) below.
- **Part 3 — Systems Engineering and Management:** the destination — the "how to perform SE" knowledge applied once a team is enabled; includes specific process areas (requirements, design, V&V), **Project Planning** (and its Systems Engineering Planning Process Overview), and **Systems Engineering Project Assessment and Control**.
- **Part 6 — Systems Engineering and Project Management:** owns the *managing* questions this KA defers — the article on **how Systems Engineering and Project Management relate** and the one on **how project structure and governance shape that SE/PM relationship**.
- **Systems Engineering and Quality Attributes** — specialty engineering capabilities that project teams provide while performing SE.
- **ISO/IEC/IEEE 15288:2015** — the technical-process backbone onto which the DEI / inclusive-engineering considerations are mapped, and the standard governing the SE life-cycle processes the enabled team then executes.
- **INCOSE Systems Engineering Competencies Framework (2010)** and **People Capability Maturity Model (P-CMM)** — competency checklists used in staffing.
- **NASA APPEL** and **NASA SELDP (Systems Engineering Leadership Development Program)** — referenced exemplars for team assessment and for developing technical leadership as a distributed capability.
- **PMBOK® Guide** — the five project-management process groups (initiating, planning, executing, monitoring and controlling, closing) invoked where the SE team leader's management responsibilities are described.
