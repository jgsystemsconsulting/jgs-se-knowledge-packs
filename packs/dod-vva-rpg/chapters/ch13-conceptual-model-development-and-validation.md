# Chapter 13: Conceptual Model Development and Validation

## Core Idea
The **simulation conceptual model** is the Developer’s translation of intended-use requirements into a design framework — the communication bridge among User, Developer, V&V Agent, Accreditation Agent, and SMEs. Validating that conceptual model (against the referent, and then using it to verify the implementation) is how validation starts before code exists.

## Frameworks Introduced
- **Two varieties**: a standalone **simulation conceptual model** and a **federation conceptual model** (HLA federations and, more generally, any cooperating set of simulations). Management and assessment practices largely overlap; federations may also owe FEDEP / HLA process artifacts.
- **Three information categories**: *simulation context* (authoritative domain sources, coordinate systems, algorithms, equipment modes, org/info flows, and usually the validation-referent pointers); *simulation concept* (how the problem will be represented given those constraints); *simulation elements* (the entities, processes, and interactions that will actually be built).
- **Life-cycle placement**: conceptual modeling sits in definition/concept development and is maintained through design, implementation, test, and revision — not a one-page kickoff sketch.
- **Implementation independence (reasonable)**: early conceptual models should not lock software paradigm or hardware unless requirements, User/sponsor decisions, or reuse of legacy pieces force a dependency. Record forced dependencies; avoid accidental ones.

## Key Concepts
- **Not every “conceptual” artifact is this model**: problem-formulation notes, database conceptual schemas, and mission-space knowledge models (CMMS / FDMS / DCMF-style referent descriptions) are related but distinct. This chapter is the *simulation* conceptual model — what will be built and why it is enough for the use.
- **Bounds inclusion, exclusion, and fidelity**: the conceptual model is the receptacle for intended-use information; it states what is in, what is out, and how much fidelity each included behavior needs.
- **Referent hooks**: specify which authoritative information is the development referent and which is the validation referent. Representation in the M&S may aggregate or approximate the referent (team → one delay distribution; hydrocode → semi-empirical real-time algorithm). When data/theory are thin, name the SMEs or SME class and the process they will use.
- **Uses of the artifact**: judge appropriateness for a use; give context for results validation (interpolation/extrapolation vs referent data); drive design; communicate capabilities/limits; support implementation verification; enable reuse.
- **Why the cost is justified**: early discovery of requirements faults (a major source of simulation defects) and safer use of results in planning, analysis, design, operations, or training.
- **Where it lives**: a CM-controlled development deliverable. If a legacy M&S has none, the V&V Agent builds a *surrogate* from manuals, diagrams, algorithms, limitations, and scenarios — then Developers should produce a real one at the next modification.
- **Form is not prescribed**: use cases, knowledge-engineering structures, scientific-paper style, DoDAF views, UML/SysML, or enriched user manuals can all work. Whatever the shape, it must be coherent, understandable to User/Developer/V&V/SMEs, and traced to requirements. Use-case-only models often miss assumption and algorithm pedigree.
- **Federation extras**: a federation conceptual model composes member representations and interactions; if a VV&A overlay already assembled acceptability criteria and the federation referent, ingest those rather than reinventing them.

## Mental Models
- **Bridge, not brochure**: if Users and Developers cannot argue scope from the same artifact, the conceptual model is missing.
- **Validate the idea before the build**: conceptual-model V&V asks whether the planned representation matches the referent at the needed fidelity — implementation verification comes after.
- **Surrogate is debt**: reconstructing a conceptual model from a running legacy code is V&V tax for skipping the artifact the first time.

## Anti-patterns
- Treating “conceptual model” as whatever whiteboard existed in problem formulation, then skipping a maintained product.
- Encoding an accidental language/hardware choice as if it were a domain law.
- Pointing at CMMS/mission-space descriptions and calling the simulation conceptual model done.
- Leaving SME-as-referent unnamed and process-free, then claiming repeatable validation.
- Skipping a distinct conceptual-model document and discovering the gap only when V&V cost spikes.

## Key Takeaways
1. Own a maintained simulation (or federation) conceptual model that traces requirements to context, concept, and elements.
2. Hook development and validation referents — including SME processes when data are thin.
3. Keep implementation independence unless a recorded constraint forces otherwise.
4. Validate the conceptual model against the referent; use it to verify the implementation and to bound how far results may be extrapolated.

## Connects To
- **ch03**: Developer design/build evidence should trace to this model.
- **ch05**: V&V Agent assesses the conceptual model and later the implementation against it.
- **ch07**: fidelity needed for intended use is declared here.
- **ch08**: validation fundamentals assume a stated representation and referent.
- **ch12**: developing the referent that the conceptual model must cite.
