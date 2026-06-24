# Chapter 2 — Model Planning and Setting Up the Model

## Core Idea

Before any modeling element gets drawn, two preparatory activities have to happen, and this chapter is about both. The first, **Model Planning**, answers the governance question: how will modeling actually support the systems engineering work the program is obligated to do? The second, **Setting Up the Model**, answers the housekeeping question: what conventions, standards, and organizational structure will the model itself follow so that everything built later is consistent and navigable? These are the two model-specific steps the NASA SE Engine does not natively contain (introduced in Chapter 1 as borrowed from OOSEM), and here the handbook spells out what each one produces.

The unifying thread is the **Modeling Plan**. Model planning is the activity that creates this plan; setting up the model produces decisions (conventions, metamodel, standards, organization) that get recorded *into* that same plan. So the chapter is really describing one document — the Modeling Plan — assembled from two different angles, plus the technical setup work that feeds it. The plan is not a stand-alone artifact either: it is a subset of the program's Systems Engineering Management Plan (SEMP), which is the larger document that explains how the NPR 7123.1 requirements and practices get satisfied across the life cycle. The Modeling Plan narrows that to the modeling dimension specifically.

Keep the Chapter 1 caveat in view throughout: the method here is tool-agnostic SysML tied to NPR 7123.1, and this is the current Revision A (2025) baseline. Nothing in model planning or model setup is locked to a particular tool — the conventions and organizational choices are framed as decisions the project makes for itself, illustrated against the NASA SE Engine rather than mandated by a product.

## Frameworks Introduced (exact source names, when/how)

The slice is light on new named frameworks — most of the heavy machinery (SE Engine, OOSEM, MBSE Grid) was established in Chapter 1 — but it anchors the two activities to specific, named reference points:

- **The Modeling Plan.** The central artifact of the chapter. It is defined as a *technical* plan and explicitly as a subset of the SEMP. Its job is to document how modeling will support NASA's SE requirements and practices across the project/program life cycle. The handbook enumerates what it contains (see Key Concepts) and states that the outputs of model setup are documented back into it.
- **The Systems Engineering Management Plan (SEMP).** The parent document. The handbook describes the SEMP as documenting how the SE requirements and practices of NPR 7123.1 are addressed throughout the life cycle; the Modeling Plan is positioned as the modeling-focused subset of it.
- **NPR 7123.1.** Continues as the governing reference. Both the SEMP and, through it, the Modeling Plan exist to address its requirements and practices.
- **The NASA SE Engine — Technical Process 10 (Technical Planning).** Model planning is located inside this process. The handbook points to Figure 4.1-1 (the SE Engine) and places the activity within its Technical Process 10.
- **The System Design Processes / "NASA SE Engine with Modeling Specific Steps."** Setting up the model is located at the start of the System Design Processes, referencing the discussion in section 4.3.2 and Figure 4.3-3 (NASA SE Engine with Modeling Specific Steps).
- **Figure 6-1, Sample Model Organization.** A worked example of a package structure that maps onto the NASA SE Engine, offered as an illustration projects can adopt or adapt.
- **NASA MBSE Community of Practice website.** Cited as the place to find sample modeling plans (the handbook points to a Modeling Plan Template searchable on the NEN MBSE site).
- **Friedenthal, Moore, and Steiner — *A Practical Guide to SysML*, 3rd ed. (2014).** The external reference (footnote 8) backing the guidance on modeling standards/profiles and on model organization reflecting the system hierarchy.

## Key Concepts

**What the Modeling Plan contains.** The handbook gives a concrete inventory of what goes in the plan. It lists the project products that the system models can support, the modeling resources available to the project, roles and responsibilities, the modeling tools, the modeling conventions, model accessibility, and model management. Read that list as the scope of model planning: it spans people (roles), means (tools, resources), rules (conventions), reach (accessibility), and stewardship (management), all tied back to the products the models are meant to support.

**The plan is living, not one-and-done.** Model planning happens early in the life cycle, but the handbook is explicit that the plan should be revisited and updated as the system matures and moves through the life cycle, so it keeps reflecting the current environment and resources. A modeling plan written at the concept stage and never touched again is, by this guidance, a stale plan.

**Setting up the model = three setup decisions.** The second activity decomposes into three concrete pieces of work:

1. *Modeling conventions* — establishing the naming conventions for model elements and for package names. This is the consistency layer: how things get named so the model reads coherently.
2. *Modeling standards* — establishing standard profiles and other modeling standards, chosen according to the needs of the specific project or program. This is the rigor layer, and the handbook ties it to the Friedenthal/Moore/Steiner SysML guidance.
3. *Model organization* — the package structure and hierarchy used to capture the system model. Organizing the model gives a standard package structure that best reflects the system hierarchy.

**Where setup sits in the flow.** Setting up the model occurs at the beginning of the System Design Processes — consistent with Chapter 1's framing of it as the "Step 0" that precedes the rest of design. The handbook grounds this in section 4.3.2 and the modeling-specific-steps version of the SE Engine figure.

**Model organization is a choice, illustrated not dictated.** Figure 6-1 shows a sample organization whose package structure relates to the NASA SE Engine, but the handbook immediately qualifies it: projects and programs can select whatever model organization best fits their needs. The sample is a starting point, not a required template.

**Everything lands back in the Modeling Plan.** The chapter closes the loop explicitly: the results of establishing the modeling conventions, the metamodel, the modeling standards, and the model organization are all documented in the Modeling Plan. So the two activities are connected by their shared output document — planning frames the plan, setup fills in its technical decisions.

## Mental Models

**The Modeling Plan is the SEMP, zoomed in.** The cleanest way to hold the planning half of the chapter is as a nesting relationship. The SEMP is the program's full answer to "how will we satisfy NPR 7123.1 across the life cycle." The Modeling Plan is that same answer restricted to one column — the modeling column. Anything the SEMP says about SE practice, the Modeling Plan re-states for the specific case of "and here's how the models carry that load." If you can't trace a line from a modeling decision up to a SEMP/NPR 7123.1 obligation, it probably doesn't belong in the plan.

**Plan before you draw; set up before you build.** The two activities form an obvious ordering that's worth making explicit. Model planning is the management decision — who, what tools, what products, what conventions in principle. Setting up the model is the technical instantiation — the actual naming rules, the actual profiles, the actual package tree. One is the contract; the other is the scaffolding erected to honor it. Doing setup without a plan risks an internally tidy model that supports no SE product; writing a plan without setup leaves the modelers with intentions but no scaffold.

**Conventions, standards, organization = name it, govern it, file it.** A simple triad for the setup work. *Conventions* are how you name things (elements and packages). *Standards* are the profiles and rules that constrain how you model. *Organization* is where things live (the package hierarchy). Naming, governing, filing — three orthogonal decisions, each made up front so they don't have to be renegotiated mid-build. The handbook's point in deferring organization choice to the project is that filing should mirror the system's own hierarchy, and only the project knows that shape.

**The plan breathes with the life cycle.** Treat the Modeling Plan like a control surface, not a monument. The handbook's instruction to update it as resources and environment change means the plan is a snapshot of current modeling reality, periodically re-taken. The mental discipline is: every life-cycle transition is a prompt to ask whether the plan still describes the truth.

## Key Takeaways

- Model planning produces the **Modeling Plan**, a technical plan that is a subset of the SEMP; it documents how modeling will support NPR 7123.1 requirements and practices across the project/program life cycle.
- Model planning lives in the NASA SE Engine's **Technical Process 10 (Technical Planning)**; setting up the model lives at the start of the **System Design Processes**.
- The Modeling Plan inventories: supportable project products, modeling resources, roles and responsibilities, tools, conventions, model accessibility, and model management.
- The plan is established **early** and must be **updated** as the system matures so it tracks the current environment and resources; sample plans/templates are on the NASA MBSE Community of Practice site.
- Setting up the model means three decisions: **modeling conventions** (element and package naming), **modeling standards** (standard profiles and other standards per project need), and **model organization** (package structure and hierarchy reflecting the system).
- **Figure 6-1 (Sample Model Organization)** illustrates a package structure tied to the NASA SE Engine, but projects can choose whatever organization best fits their needs.
- The outputs of setup — conventions, metamodel, standards, and organization — are all **documented in the Modeling Plan**, closing the loop between the two activities.

## Connects To

- **The SEMP and NPR 7123.1** — the parent plan and the governing requirements; the Modeling Plan is the modeling-scoped subset that carries the NPR 7123.1 obligations into the modeling effort.
- **The NASA SE Engine (Figure 4.1-1) and its modeling-specific-steps variant (Figure 4.3-3)** — Technical Process 10 anchors model planning; the System Design Processes anchor model setup. Both were introduced in Chapter 1 as the two OOSEM-derived additions.
- **OOSEM (Chapter 1)** — the source of "Model Planning" and "Setting Up the Model" as distinct steps; this chapter is the detailed treatment promised there.
- **The section 7 metamodel** — named here among the setup results documented in the plan, and the tool-agnostic core that the modeling standards and organization decisions sit on top of.
- **The MBSE Grid and model building (downstream chapters)** — model organization establishes the package structure into which the Grid's diagrams and tables, built in later chapters, get filed.
- **Friedenthal, Moore & Steiner, *A Practical Guide to SysML* (2014)** — the external SysML reference behind the standards/profiles and model-organization guidance.
- **NASA MBSE Community of Practice (NEN)** — the external resource for a Modeling Plan Template to seed the planning activity.
