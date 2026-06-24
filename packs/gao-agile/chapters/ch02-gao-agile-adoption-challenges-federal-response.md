# Chapter 2 — Federal Agile Adoption: The Challenges Agencies Hit and How Government Responded

## Core Idea
Federal IT has historically been built in long, sequential phases, but many agencies have shifted toward an Agile approach that produces software in small, short increments. That transition is hard. Drawing on a 2012 GAO study, this chapter catalogs **14 specific challenges** federal agencies hit when applying Agile to software programs, organized into **four program-management activity areas** — organizational commitment and collaboration, preparation, execution, and evaluation. Most of the difficulty is cultural and structural rather than technical: a workforce and oversight regime built for Waterfall does not naturally accommodate iterative work. The chapter then surveys the laws, policies, guidance, reports, and entities created since 2012 to address those challenges — and concludes that, despite real progress, federal agencies still struggle, so they should supplement Agile practice with their own internal controls.

## Frameworks Introduced
- **The four-area challenge taxonomy** (from GAO-12-681, *Software Development: Effective Practices and Federal Challenges in Applying Agile Methods*, Jul. 27, 2012) — the 14 reported challenges are grouped under four program-management activities. Use it as a diagnostic map when assessing why an organization's Agile transition is stalling.
  - **Organizational commitment and collaboration** — management actions needed so a process takes hold and endures.
  - **Preparation** — standing up teams and processes before Agile is run on a program.
  - **Execution** — defining the concrete steps to carry out the chosen Agile approach.
  - **Evaluation** — assessing the process so the Agile approach can be improved.
- **Table 2, "Iterative Software Challenges, as Reported by Federal Agencies"** — the source's enumeration mapping each of the 14 challenges to its activity area (summarized in Key Concepts below). Use it as a checklist of known failure modes.
- **Table 3** — the source's catalog of the laws, policies, guidance documents, reports, and organizations stood up since 2012 to tackle these Agile difficulties. It is a non-exhaustive timeline of federal responses from 2012 onward (GAO analysis of OMB, GSA, and DOD documentation). Use it to locate the authoritative artifact relevant to a given problem (contracting, acquisition pathway, digital-services delivery).
- **Case study 1: Space Command and Control (Space C2), from GAO-20-146** (Oct. 30, 2019) — a worked example of one of the first DOD software-intensive programs to move from Waterfall into an Agile framework while the governing acquisition guidance did not yet cover Agile. Use it to see the "guidance lag" challenge in a real program.

## Key Concepts

### The 14 reported challenges, by activity area
- **Organizational commitment and collaboration**: teams struggled to collaborate closely; teams struggled to move to self-directed work; staff struggled to commit to more frequent, timely input; organizations had trouble committing staff.
- **Preparation**: timely adoption of new tools was hard; technical environments were hard to set up and keep running; Agile guidance was unclear.
- **Execution**: procurement practices did not always support Agile programs; customers did not trust iterative solutions; teams had trouble managing iterative requirements.
- **Evaluation**: compliance reviews were hard to fit inside an iteration's time frame; federal reporting practices, traditional artifact reviews, and traditional status tracking each failed to align with Agile methods.

### Why collaboration broke down
Agile depends on the continuous involvement of a wide set of stakeholders — business owners, sponsors, users, developers, and cybersecurity specialists — and promotes commitment by co-locating teams where possible. Federal staff accustomed to working alone in individual workspaces found this difficult: some preferred solo work, saw open status-posting (like a team-room wall chart) as intrusive, or were reluctant to show work in progress to the customer. Moving to **self-directed teams** was equally hard for people used to taking direction from a program manager, who now had to own their work and escalate only unresolved issues. **Cross-functional teams** were hard to assemble because federal employees tended to be narrow specialists; a member representing one customer set did not necessarily understand all customers' needs.

### Why preparation was difficult
Keeping artifacts such as schedules current for every iteration clashed with a workforce unused to the rapid cadence. Teams initially had trouble holding an iteration's pace because their habit was to halt work to resolve an issue rather than decide and move on, and federal customers were not always available to review deliverables as they completed. Staffing was a recurring constraint: organizations lacked enough people to dedicate to multiple Agile teams, staff with concurrent duties could not commit the large time block an Agile team needs, and frequent rotation of assignments meant new staff constantly had to learn departing colleagues' roles. New **tools and technical environments** were needed when migrating off Waterfall, and buying, installing, and training on them caused delays. Because Agile runs development, testing, and operations concurrently, keeping synchronized hardware/software environments for frequent releases was expensive and logistically hard — especially across multiple concurrent iterations. Finally, **guidance was unclear**: where existing agency guidance was written for Waterfall, new policies and procedures had to be authored (a daunting task), and teams found a mix of iterative and Waterfall life-cycle guidance confusing.

### Why execution was difficult
Agile favors **stable teams** — at least for the duration of an iteration — because flexibility is meant to come from continuous improvement and from adjusting teams to the program's changing scope, not from churning staff. Federal procurement did not always support that flexibility: contracts demanding Waterfall-style artifacts to judge contractor performance are unnecessary when the contractor is a team member judged on delivered iterations, and contracting officers' need for structured tasks and performance checks made it hard for contractor staff to absorb changing work within iteration time frames. **Mistrust of iterative solutions** was common — customers expecting a complete solution sometimes judged a single iteration's functionality as inadequate, which fed doubt about the team's ability to deliver the rest and hindered defining "done" (the agreed set of activities that make an increment releasable). Customers also found it hard to **prioritize requirements by release**, being used to fixing all requirements up front, and reprioritizing when new work appeared was difficult. **Compliance reviews** that took months under Waterfall could not fit inside a few-week iteration, delaying the iterations awaiting assessment.

### Why evaluation was difficult
Agile values working software over heavy documentation and milestone reporting, which misaligns with traditional federal oversight. Oversight bodies request status at Waterfall milestones and had not adjusted to frequent per-increment updates, so teams grew frustrated when dashboards looked negative. Traditional oversight wants detailed artifacts (cost estimates, strategic plans) early, whereas Agile prefers a high-level estimate and road map refined each iteration. **Status tracking** also clashed: estimating effort in **story points** rather than hours was unfamiliar, and **earned value management (EVM)** felt onerous without guidance on adapting it to iteration progress — made worse when upper management treats monthly cost/schedule/scope changes as control problems rather than expected iterative revisions.

### Actions taken since 2012 (selected from Table 3)
- **OMB OFPP modular-development contracting guidance** (June 2012) — supports modular development per item 15 of the 25-Point IT Reform Plan; covers competition, statement-of-work breadth, when to use fixed-price, and delivering functional value frequently (as little as 6 months).
- **GSA 18F office** (March 2014) — collaborates with agencies to fix technical problems and ship products using basic Agile tenets (user-centered development, hypothesis testing, frequent shipping).
- **U.S. Digital Service (USDS)** (Aug. 2014) and the **Digital Services Playbook** (Aug. 2014) — USDS fosters multidisciplinary teams; the Playbook's 13 "plays" include building services using Agile and iterative practices.
- **TechFAR Handbook** (Aug. 2014; refreshed as the **TechFAR Hub**, updated Jan. 2023) — highlights FAR flexibilities for procuring digital services with Agile, without supplanting existing law or policy.
- **18F Digital Contracting Cookbook** (2014, updated Jan. 2016) — suggestions for acquiring digital services, recognizing every organization's requirements differ.
- **FITARA** (Dec. 2014) — improves acquisition and monitoring of federal IT and codified a requirement that covered-agency CIOs certify investments are adequately implementing incremental development.
- **Federal Acquisition Institute, Agile Acquisitions 101** (Apr. 2015); **OMB OFPP Pilot for Digital Acquisition Innovation Lab** (Mar. 2016).
- **Defense Science Board, Design and Acquisition of Software for Defense Systems** (Feb. 2018) and **Defense Innovation Board, Software is Never Done** (May 2019) — the latter emphasizes speed and cycle time as the most important software metrics.
- **DODI 5000.87, Operation of the Software Acquisition Pathway** (Oct. 2020); **DOD Digital DNA** (Oct. 2021); **DODI 5000.82, Requirements for the Acquisition of Digital Capabilities** (June 2023); **GSA 18F De-risking Government Technology field guide** (July 2023).

## Mental Models
- **The challenge is the culture, not the method.** GAO is explicit that the difficulties stem in large part from a cultural and social environment not conducive to transition. Tooling and process can be bought; trust, self-direction, and cross-functional habits must be grown.
- **Stability is the source of Agile flexibility, not its enemy.** Flexibility comes from continuous improvement and from adjusting teams to changing scope — not from constantly swapping staff. Keep teams stable for at least an iteration.
- **"Done" is a contract, not a feeling.** A definition of "done" is an explicit commitment of the activities required for an increment to be releasable; mistrust of iterative delivery directly blocks an organization from agreeing on it.
- **Oversight friction is a misalignment of cadence and artifacts.** Waterfall oversight wants heavy artifacts up front and status at milestones; Agile produces evolving implementation and frequent small updates. The fix is aligning reviews and reporting to the Agile cadence (a theme deferred to later chapters), not abandoning oversight.
- **Guidance lag is a predictable transition risk.** Early adopters (e.g., Space C2) often run ahead of the policy that is supposed to govern them, operating against draft guidance until formal policy catches up.
- **Policy alone does not fix execution.** Despite the Table 3 body of laws and guidance, agencies kept struggling — so each organization must add its own internal controls.

## Anti-patterns
The source names these recurring failure modes:
- **Treating a single increment as proof the whole job can't be done.** Customers expecting a total solution dismissed one iteration's functionality, breeding doubt the team would deliver the remainder.
- **Mixing iterative and Waterfall life-cycle guidance.** Teams found it confusing when a program followed a blend of the two, and staff were anxious about leaving Waterfall guidance behind.
- **Running compliance/oversight on the old schedule.** Compliance reviewers prioritizing requests as they arose, with reviews taking months, stalled iterations that needed assessment within weeks.
- **Demanding heavy artifacts and hours-based estimates inside an Agile program.** Requiring detailed cost estimates and strategic plans early, or hours-based tracking instead of story points, fights the incremental model.
- **Management treating expected iterative revisions as control problems.** When leadership tracks monthly cost/schedule/scope shifts as defects rather than normal iterative adjustment, it undermines tools like EVM and the Agile mindset.

## Key Takeaways
1. GAO's 2012 study (GAO-12-681) identified **14 Agile adoption challenges**, grouped into **four areas**: organizational commitment and collaboration, preparation, execution, and evaluation.
2. The root cause is largely **cultural and structural** — a workforce and oversight model built for Waterfall, not a defect in Agile itself.
3. **Stable, co-located, self-directed, cross-functional teams** are central to Agile and are exactly where federal organizations had the most trouble.
4. **Procurement, compliance, and evaluation practices** built for Waterfall (Waterfall artifacts, months-long compliance reviews, milestone-only status, hours-based estimating, EVM without adaptation) repeatedly collided with iterative cadence.
5. Since 2012, Congress and the executive branch built a substantial body of responses — **Table 3** (OMB/OFPP guidance, 18F, USDS, the Playbook, TechFAR, FITARA, DODI 5000.87/5000.82, and more) — but the list is **not exhaustive** and did not eliminate the struggle.
6. GAO's follow-on reviews (USCIS 2016, DOD space acquisitions 2019, DHS 2020, Space C2 2022) confirm that **adoption and execution challenges persist**.
7. Organizations should **supplement** the guide's Agile practices with their own **internal controls** (policy and guidance) to drive consistent execution, learning, and reliable reporting.

## Connects To
- **Chapter 3** — virtual co-location as an option for distributed Agile teams (referenced here for the co-location challenge).
- **Chapter 6** — aligning program milestones and reviews to an Agile cadence, and contracting best practices that reconcile Agile with contract requirements (the execution and evaluation frictions named here).
- **Chapter 7** — applying performance management systems such as earned value management to Agile programs (the EVM/story-point evaluation challenge).
- **GAO-12-681** (*Software Development: Effective Practices and Federal Challenges in Applying Agile Methods*) — the original source of the four-area challenge taxonomy.
- **GAO-20-146** (*Space Command and Control*) — the case study illustrating guidance lag during early DOD Agile adoption.
- **GAO-14-704G** (*Standards for Internal Control in the Federal Government*) — the internal-controls reference the chapter points to for supplementing Agile practice.
- Related GAO findings cited here: **GAO-16-467** (USCIS Transformation), **GAO-19-136** (DOD space acquisitions / user feedback), **GAO-20-213** (DHS Agile leading practices), **GAO-23-105920** (Space C2 tracking and reporting).
