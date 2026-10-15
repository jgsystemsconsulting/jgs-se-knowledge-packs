# Chapter 2 - Software Review Process

Sources: FAA Order 8110.49A, Software Approval Guidelines (effective 2018-03-29), Chapter 2 paragraphs 1-2 (printed pages 2-1 to 2-2).

## Core Idea

Order 8110.49A Chapter 2 tells FAA certification staff how to run software reviews against a project that uses RTCA/DO-178B or DO-178C as its means of compliance. The chapter does not rewrite the standard. It operationalizes the certification liaison process in DO-178B/C Section 9 so the authority and the applicant share a common view of compliance, and so any desk or on-site review (including work delegated to authorized designees) has a defined purpose and a planned set of arrangements.

## Frameworks Introduced

- **Certification liaison as the communication vehicle.** DO-178B/C Section 9 is the agreed channel between applicant and certification authority; Sections 9.2 and 10.3 already allow the authority to review life cycle processes and data for compliance. Chapter 2 keeps that intent and explains how FAA staff carry it out.
- **Desk review versus on-site review.** Both forms are valid. On-site review adds access to software personnel, automation, and the test setup. Either form may be delegated to properly authorized designees.
- **Nine on-site practical arrangements.** Before an on-site review, the authority and the developer agree scope, dates and locations, authority personnel, designees, agendas and expectations, data available before and at the review, procedures, required resources, and how results (including corrective actions and other post-review work) will be communicated.
- **Four review-process objectives.** Reviews exist to give timely technical interpretation of the certification basis and applicable objectives; visibility into implementation compliance and data; objective evidence that the project adheres to its approved software plans and procedures; and an opportunity for the authority to monitor designee activity.
- **Early LOI sizing drives review scope.** Level of certification authority involvement is determined and documented as early as practicable; Appendix A supplies optional worksheets. Scope and number of reviews (if any) follow eight project factors listed in Chapter 2 paragraph 2.b (detailed in ch03).

## Key Concepts

- **What the review is assessing.** The authority may review software life cycle processes and associated data to gain assurance that a software product submitted with a certification application complies with the certification basis and satisfies the applicable DO-178B/C objectives.
- **Desk review.** Remote or document-based examination of life cycle data. Useful and often sufficient; it does not by itself give access to personnel, automation, or the live test setup.
- **On-site review.** Same compliance purpose, with physical access to people, tools, and test environment. The nine arrangement items above are the planning checklist the order expects the authority to settle with the developer.
- **Designee delegation.** Both desk and on-site reviews may be delegated to properly authorized designees. The fourth review objective (monitoring designee activity) exists because delegation does not remove the authority's interest in how the review is performed.
- **Data availability timing.** Arrangement item (6) explicitly covers data both before the review and at the review. Pre-positioning data is part of the agreement, not an afterthought.
- **Corrective actions as part of results.** Arrangement item (9) treats review results as including corrective actions and other post-review activities, with agreed dates and means of communication.
- **LOI link (pointer only).** Chapter 2 paragraph 2.b lists eight factors that shape how many reviews run and how deep they go; the worksheets that score those factors live in Appendix A and are covered in ch03.

## Mental Models

- Treat the review as a planned liaison event, not a surprise audit. The nine arrangements are the contract for how the event will run.
- On-site is a capability choice (people, automation, test setup), not a higher legal standard than desk review. Pick the form that can actually see the evidence the objectives need.
- Designee performance is itself in scope. If work is delegated, the authority still needs a path to observe how that work is done.
- LOI is set first; review count and depth follow. Do not invent a review calendar before the involvement level is documented.

## Anti-patterns

- **Skipping the nine arrangements and showing up unprepared.** Without agreed scope, data list, procedures, and results channel, on-site time is spent negotiating logistics instead of examining compliance evidence.
- **Treating desk review as second-class by default.** The order says desk reviews may successfully review software; on-site is preferred when access advantages matter, not because desk is invalid.
- **Delegating and forgetting.** Handing the review to a designee without a monitoring path breaks the fourth objective.
- **Leaving LOI undecided until late in the life cycle.** Paragraph 2.b says involvement should be determined and documented as soon as possible; late LOI produces unplanned review spikes or under-review of novel work.

## Key Takeaways

1. Chapter 2 implements DO-178B/C certification liaison for FAA staff; it does not change the standard's intent.
2. Desk and on-site reviews are both valid; on-site adds access to personnel, automation, and test setup; both may be delegated to authorized designees.
3. On-site reviews rest on nine practical arrangements agreed with the developer before the visit.
4. The review process has four objectives: interpretation, visibility, plan adherence evidence, and designee monitoring.
5. LOI is set and documented early; eight project factors (and optional Appendix A worksheets) drive how many reviews run and how deep they go.

## Connects To

- **ch01** - which FAA document answers which question, and how Order 8110.49A sits beside the ACs.
- **ch03** - LOI criteria and Appendix A worksheet scoring that size the review program this chapter runs.
- **ch04** - software conformity inspection, which reuses Chapter 2 desk/on-site reviews to establish the software baseline before Form 8120-10 work.
- **ch05** - AC 20-115D recognition of DO-178C and what life cycle data the applicant produces for the liaison process.
