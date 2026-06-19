# DoDAF 2.02 Vol II Cheatsheet

## Eight Viewpoints — Quick Reference

| Viewpoint | Code | Primary Audience | Core Question | Models |
|-----------|------|-----------------|---------------|--------|
| All | AV | All stakeholders / DARS | What is this architecture and what terms does it use? | AV-1 (Overview), AV-2 (Dictionary) |
| Capability | CV | Portfolio managers, JCIDS | What effects are needed and how will they be achieved? | CV-1 through CV-7 |
| Data & Info | DIV | Data architects, COI leads | What information is needed, in what form, at what level? | DIV-1 (Conceptual), DIV-2 (Logical), DIV-3 (Physical) |
| Operational | OV | Operators, mission planners | Who does what with whom, independent of technology? | OV-1 through OV-6c |
| Project | PV | Acquisition managers, PPBE | Which projects deliver what, when, and for whom? | PV-1 (Projects/Orgs), PV-2 (Schedules), PV-3 (Projects/Capabilities) |
| Services | SvcV | SOA architects, net-centric planners | How are services composed, what do they do, and how do they evolve? | SvcV-1 through SvcV-10c |
| Standards | StdV | SE, acquisition, compliance | What rules govern the architecture now and in the future? | StdV-1 (Current), StdV-2 (Forecast) |
| Systems | SV | Systems engineers, PMs | How are systems composed, what do they do, and how do they perform? | SV-1 through SV-10c |

---

## DM2 Data Groups — Quick Reference

| Data Group | Type | Core Concept | Primary Viewpoints |
|------------|------|-------------|-------------------|
| Performers | Principle | Who does what | CV, OV, PV, StdV, SvcV, SV |
| Resource Flows | Principle | How resources move between activities | OV, SvcV, SV |
| Information & Data | Principle | What is known at conceptual/logical/physical levels | AV, DIV |
| Rules | Principle | What constrains activities | OV, StdV, SvcV, SV |
| Capabilities | Principle | What effects are sought and how | CV, PV, SvcV, SV |
| Services | Principle | What is offered through prescribed interfaces | CV, StdV, SvcV |
| Projects | Principle | What is being built and when | AV, CV, PV, SvcV, SV |
| Org Structures | Principle | How entities are organized | OV, StdV, SvcV, SV |
| Measures | Supporting | How much / how well | SvcV, SV |
| Locations | Supporting | Where | PV, SvcV, SV |
| Pedigrees | Supporting | Provenance | all (as needed) |

---

## DoD Core Process Mapping

| Process | Abbreviation | Primary Data Groups | Key Models |
|---------|-------------|-------------------|------------|
| Joint Capabilities Integration & Development | JCIDS | Capabilities, Performers, Rules | CV-1, CV-2, OV-5b, SV-5a |
| Defense Acquisition System | DAS | Projects, Performers, Resource Flows | PV-1, PV-2, SV-1, SV-4 |
| Planning, Programming, Budgeting & Execution | PPBE | Projects, Capabilities, Measures | PV-1, PV-2, PV-3 |
| Systems Engineering | SE | Performers, Resource Flows, Rules | SV-1 through SV-10c |
| Operations | OPS | Performers, Activities, Resource Flows | OV-1 through OV-6c |
| Portfolio Management (IT & CPM) | PfM | Capabilities, Projects | CV-1, CV-2, PV-3 |

---

## Model Derivation Rules (Critical Constraints)

| Derived Model | Must Come From | Cannot Do |
|--------------|---------------|-----------|
| OV-5a | OV-5b | Add activities or alter OV-5b data |
| OV-2 | Subset of OV-3 | Introduce resources not in OV-3 |
| SV-2 | SV-1 | Introduce systems or activities not in SV-1 |
| SV-3 | Other SV models | Introduce new system relationships |
| SV-5a | SV-4 (functions) + OV-5b (activities) | Introduce new activities or functions |
| SvcV-2 through SvcV-10c | SvcV-1 | Introduce new services or activities |
| PV-2 | PV-1 (projects only) | Introduce new projects |
| DIV-3 | DIV-2 | Introduce concepts not in DIV-2 |
| StdV-2 | StdV-1 base (adds future-state only) | Change current standards in StdV-1 |

---

## Key DM2 Relationship Types

| Relationship | DM2 Name | Meaning |
|-------------|----------|---------|
| Performs | activityPerformedByPerformer | A performer carries out an activity |
| Produces | activityProducesResource | An activity produces a resource |
| Consumes | activityConsumesResource | An activity consumes a resource |
| Constrains | ruleConstrainsActivity | A rule governs how an activity is carried out |
| Condition | activityPerformableUnderCondition | An activity is performable under a condition |
| Part of | wholePart / temporalWholePart | Compositional or temporal decomposition |
| Subtype of | superSubtype | Type inheritance / generalization |
| Measures | measureOfType | A measure applies to an element type |
| In location | resourceInLocationType | A resource is located in a location type |
| Activity in capability | activityPartOfCapability | An activity is part of a capability |

---

## IDEAS Stereotype Color Code

| Stereotype | Color | Meaning |
|-----------|-------|---------|
| «Individual» | Grey (80%) | An instance with spatio-temporal extent |
| «Type» | Pale blue | Specification of a type |
| «IndividualType» | Light orange | Type whose members are Individuals |
| «TupleType» | Light green | Type whose members are tuples (n-ary relationships) |
| «Powertype» | Lavender | Set of all subsets of a given Type |
| «Name» | Tan | A name (label for a thing) |
| «NamingScheme» | Yellow | Type whose members are names |

---

## Decision Rules: Which Model to Use?

**Strategic / portfolio decisions** → Start in CV (CV-1 for effects, CV-2 for hierarchy, PV-3 for investment mapping)

**Who does what (technology-independent)** → OV (OV-5b for activities, OV-4 for org relationships, OV-3 for resource flows)

**What information is needed** → DIV (DIV-1 for concepts, DIV-2 for requirements, DIV-3 for implementation)

**System design and interface specs** → SV (SV-1 for composition, SV-4 for functions, SV-6 for measures)

**Service-oriented or net-centric design** → SvcV (SvcV-1 for composition, SvcV-4 for functions, SvcV-5 for OV mapping)

**Standards and compliance** → StdV (StdV-1 for current, StdV-2 for forecast)

**Program/acquisition integration** → PV (PV-1 for WBS, PV-2 for schedule, PV-3 for capability mapping)

**Architecture registration / vocabulary** → AV (AV-1 for DARS, AV-2 for definitions)

---

## Tells & Smells

**Smell:** "Our systems architecture has no link to the operational concept."
→ **Tell:** Missing SV-5a (system functions to OV-5b activities mapping). Add it.

**Smell:** "We have a standards list but no idea which systems must comply with which standard."
→ **Tell:** Standards are bound to performers, not activities. Rebuild StdV-1 routing standards through activities.

**Smell:** "The capability we're funding doesn't appear in any portfolio model."
→ **Tell:** PV-3 is missing or incomplete. Map program elements to CV-2 capability hierarchy via PV-3.

**Smell:** "Two organizations use different terms for the same data element."
→ **Tell:** COI harmonization not done. Run DIV-1 and AV-2 across both communities to surface overlapping concepts.

**Smell:** "We modeled a system giving data directly to another system."
→ **Tell:** Resource flows must go through activities (resource flow triple). Add the producing and consuming activities.

**Smell:** "Our OV has systems as performers."
→ **Tell:** Systems do not belong as performers in the OV. Systems are means/constraints in OV; they are primary performers in SV.

**Smell:** "Our SV-4 has system functions with no operational activity traceability."
→ **Tell:** SV-5a is missing. Every system function must trace to at least one OV-5b operational activity.

**Smell:** "The project WBS doesn't match the architecture."
→ **Tell:** PV-1 and the WBS are not synchronized. The WBS is a PV-1 artifact and must evolve with the architecture.

**Smell:** "Services are modeled only as IT web services."
→ **Tell:** DoDAF services include non-IT services. Revisit SvcV-1 scope; non-IT services (search and rescue, logistics) may be missing.
