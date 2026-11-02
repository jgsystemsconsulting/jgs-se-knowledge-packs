# Chapter: Identify monitoring and surveillance

## Core Idea

Identify turns system scope into a living list of DMSMS issues: immediate, near-term, and forecast. Section 4 of SD-22, 06-JAN-2026 covers system prioritization, tools, item-data collection and preparation, availability analysis, design-risk checks, forecasting, and FMS-specific identify notes. Appendix J holds BOM acquisition and construction method. No worksheet cells are copied here.

## Frameworks Introduced

### Monitoring and surveillance flow

1. Prioritize systems and assemblies worth the monitoring load.
2. Select and field monitoring tools.
3. Collect and clean item data (hardware electronics, MaSME, and software).
4. Analyze availability with predictive tools, vendor surveys, critical-materials analysis, and product discontinuance notices (including GIDEP and DLA PDN paths).
5. Assess preliminary designs for DMSMS risk.
6. Forecast future issues.
7. Apply FMS identify considerations when partner equipment shares or diverges from DoD configurations.

### Item-data and BOM method

- **Hierarchy.** Items sit inside assemblies and units. Flat and indentured BOMs answer different questions.
- **Data preparation.** Deduplicate, normalize, and fill gaps before risk scoring.
- **Appendix J.** When a contract did not deliver a usable BOM, the appendix describes how to acquire or build one and how to close gaps. Method only; no BOM worksheet cells.

### Risk-based focus

Not every part earns equal surveillance. Criticality, availability signals, and design stage drive where proactive watch is worth the cost. The guidebook's risk views and cubes are described at concept level; grid cells stay out.

## Key Concepts

- **Predictive tools.** Forecast end-of-life and shortage risk from market and usage signals.
- **Vendor surveys.** Direct supplier input on production plans and support windows.
- **Critical materials.** Specialty materials can create DMSMS even when a finished assembly still looks healthy.
- **PDNs.** Discontinuance notices are triggers, not complete answers. Verify scope and stock before Assess.
- **Software.** Require complete software item lists and license or support terms by contract where possible.
- **FMS identify notes.** Verify whether a DoD issue hits a foreign partner, and notify partners in time for shared resolutions or separate paths.

## Mental Models

- **Watchlist, not encyclopedia.** Identify produces a managed issue list, not a static parts catalog.
- **Data quality gates resolution quality.** Garbage BOMs make elegant BCAs wrong.
- **Shared demand changes math.** Partner quantities can justify a life-of-need buy that DoD demand alone would not.

## Key Takeaways

- Prioritize systems, then instrument them with tools and clean item data.
- Combine predictive signals, vendor input, critical-materials views, and PDNs.
- Treat software and MaSME with the same seriousness as electronics.
- Use Appendix J method when BOMs are missing or thin.
- Carry FMS verify-and-notify practice inside Identify, not as an afterthought.

## Connects To

- ch03 for the DMT and contracts that enable data access
- ch05 for Assess decisions fed by Identify outputs
- ch08 for obsolescence definitions that frame what Identify is looking for
- Appendix J (BOM method described, cells omitted)
