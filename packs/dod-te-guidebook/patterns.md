# DoD T&E Enterprise Guidebook Patterns & Techniques

Reusable T&E patterns drawn from the DoD Test & Evaluation Enterprise Guidebook (OUSD R&E, August 2022). Each has When / How / Trade-offs. These are guidance techniques the Guidebook recommends; binding requirements live in DoDI 5000.89 and the related instructions.

## Pattern 1: Decision-First Planning with the IDSK

**When to use**: building any T&E Strategy / TEMP, on any of the six pathways.

**How**: start from the acquisition, technical, and program decisions that must be made, work back to the data those decisions require, then to the data sources (contractor test, developmental test, live-fire test, operational test, M&S) that produce it. Capture that mapping in the Integrated Decision Support Key (IDSK) — required content per DoDI 5000.89 — and let it evolve as the system matures. Every planned test event should trace to a decision in the IDSK.

**Trade-offs**: decision-first planning costs upfront analysis and forces hard conversations about which decisions actually need data; the payoff is that tests exist to inform decisions rather than to fill a checklist, and redundant testing is exposed. A test that maps to no decision is a candidate for cutting under the tailoring logic.

---

## Pattern 2: One Body of Evidence, Many Evaluators

**When to use**: from program inception, across every pathway and every test community.

**How**: stand up a shared, accessible data repository at program start. Let contractor, developmental, live-fire, and operational testers all read from, contribute to, and reuse it. Use collaborative test data scoring boards to authenticate whether existing integrated data can satisfy IOT&E or LFT&E objectives. Keep the OTA as the holder of the authoritative record of data certified for operational evaluation. Capture data once; reuse it everywhere.

**Trade-offs**: building and governing a shared repository is real engineering and contracting work, and reuse only holds where data pedigree supports it — testers must map prior data to evaluation areas and name the gaps. But the alternative (each community running its own confirmatory tests) wastes schedule the program rarely has. Reuse rescopes events; it never replaces a dedicated DT&E, OT&E, or LFT&E event.

---

## Pattern 3: Get T&E into the RFP and Contract

**When to use**: during planning, before the RFP is released, on every pathway.

**How**: use the RFP and IP Strategy to secure government access to the contractor's test events, tools, M&S, data repositories, and environments; to its own test plans, procedures, reports, and data; to its support for government-run testing; and to ownership of the test data generated, so it can enter the shared body of evidence. Attach a draft T&E Strategy to the RFP so contractors know what will be tested. Put data deliverables on the CDRL.

**Trade-offs**: negotiating data rights and access raises contract complexity and may raise bid cost; omitting them is cheaper at award and catastrophic later — the Guidebook is blunt that anything not in the RFP and contract will not be delivered, raising risk to the whole T&E program and to program cost and schedule.

---

## Pattern 4: Embed OT&E Early — Visibility Without Development

**When to use**: from pre-development / Materiel Solution Analysis, on every pathway; especially on compressed-timeline pathways.

**How**: bring operational test into systems engineering and development at the start. The OTA monitors developmental tests, judges the pedigree of DT results, maps which prior data can serve operational evaluation, VV&As automated test capabilities and environments whose data will feed operational conclusions, and identifies gaps that shape future test planning. In the Software pathway, embed in the pipeline (electronically and physically) for continuous visibility — but the OTA never writes the software. Visibility is the asset; independence is the constraint.

**Trade-offs**: embedding consumes operational-test staff early and risks blurring the independence line if mismanaged; done right, it lets operational realism enter while fixes are still cheap and preserves the independent verdict that reaches the milestone decision and Congress.

---

## Pattern 5: Tailor Tests to the Decision and the Mission Context

**When to use**: on compressed pathways (Urgent Capability, Middle Tier, Software) and whenever schedule is the binding constraint.

**How**: narrow data collection to activities tied directly to the theater of employment, the mission context (operation types, threats, environments, users, tactical employment), and the technical requirements in the need — not to everything that could be tested. Stress components under operationally relevant conditions and test at system level in an environment resembling actual employment, including a cyber-contested setting with service members from the user community. Keep plans streamlined, feasible, and aligned to the timeline and Acquisition Strategy.

**Trade-offs**: aggressive tailoring narrows coverage and can leave residual unknowns; the discipline of testing to the specific theater and mission set is what makes credible evaluation possible inside a two-to-five-year window. Document what coverage is being given up so the decision authority sees the residual risk.

---

## Pattern 6: Walk the LFT&E Ladder and Use the FUSL Waiver Correctly

**When to use**: on any program subject to 10 U.S.C. §4172 (survivability/lethality), across pathways.

**How**: run live-fire testing across the whole program — component → sub-system → system, culminating in Full-Up System-Level (FUSL) testing of a combat-equipped, production-representative system — early enough to correct design deficiencies before going beyond LRIP. If FUSL is unreasonably expensive and impractical, pursue the FUSL waiver: the PEO memorializes the case, the SAE forwards it to USD(A&S) as the Defense Acquisition Executive (who must approve even when authority is delegated), and DOT&E certifies the TEMP's alternative live-fire approach. Send the congressional defense committees a two-part package — a certification of need plus an alternative LFT&E plan grounded in actual testing (not M&S alone).

**Trade-offs**: the waiver path is a multi-level, statutory process with no shortcut; treating "rapid" or "off-the-shelf" as exempt from LFT&E is a misread — there is no waiver from LFT&E itself, only from FUSL.

---

## Pattern 7: Gate Operational Events on Readiness (OTRR) and Oversight Status

**When to use**: before any operational event, on any pathway.

**How**: hold the Operational Test Readiness Review (OTRR) before entering an operational event to verify reliability, maintainability, supportability, and hazard/ESOH/software-safety manageability. Read the program's oversight status first: on the T&E Oversight List, DOT&E is the final approver of the T&E Strategy/TEMP and operational/live-fire test plans, submissions are due ahead of the decision (about 45 days for the TEMP, about 60 days before test start for operational test plans), and any deviation from an approved plan needs DOT&E concurrence before the revised events run. Off the list, approval rests at the Component/Service level.

**Trade-offs**: the readiness gate and advance-submission rules add schedule lead time; skipping them produces hollow operational events and false confidence, and on oversight programs an unapproved or deviated plan is simply not authorized to run.

---

## Pattern 8: Continuous, Automated Testing for Iterative Software

**When to use**: on the Software Acquisition pathway and other DevSecOps/Agile efforts where releases ship continuously.

**How**: make testing a continuous embedded activity, not a downstream gate. Automate functional, performance, and regression testing so test tempo keeps pace with development; split tooling into test management and test execution; have development teams lead unit tests and independent government teams lead integration and acceptance testing, all draining into the shared body of evidence. Direct government testers toward Behavior-Driven and Acceptance-Test-Driven Development (Given-When-Then), closest to mission value. VV&A any automated capability or environment whose output supports operational conclusions. Fold post-release production telemetry (uptime, error reports, help-desk data, cyber monitoring) back into the evidence base.

**Trade-offs**: standing up pipelines, software factories, and the environment ladder (Sandbox → Dev → Integration → Test/QA → Pre-Production → Production) is significant infrastructure investment; without it, continuous integration and delivery cannot happen and T&E becomes the bottleneck that breaks the release cadence.
