# Chapter 13 — Process Concepts

## Core Idea
Systems engineering rests on a well-defined set of processes that guide complex systems across the whole life cycle. These processes are the backbone of systematic practice and are what separate disciplined engineering from ad-hoc approaches. The **Process Concepts** knowledge area makes two points that hang together: (1) processes must be *described* in a uniform way so they are clear, consistent, and comparable — this is the job of **ISO/IEC/IEEE 24774**; and (2) processes are *not* meant to run serially in a fixed sequence — **concurrency, iteration, and recursion** make life cycle management dynamic and non-linear. Together these two ideas — consistent description plus non-linear application — define how the SEBoK treats life cycle processes.

## Frameworks Introduced
- **ISO/IEC/IEEE 24774 (Specification for process description)** — the standard whose stated aim is to encourage uniformity in how processes are described. It specifies how process descriptions are established and builds on lessons learned from earlier international, national, and industry process standards.
  - When/how: use it whenever you write or evaluate a process description, so that processes are understandable, comparable, and manageable across an organization.
- **Process Elements (per ISO/IEC/IEEE 24774)** — the building blocks of any process description, split into **Required**, **Optional**, and **For Any Other Element**.
  - Required: **Process Name, Purpose, Outcomes**.
  - Optional: **Inputs, Activities, Tasks, Outputs**.
  - For any other element: **Notes, Controls, Constraints**.
  - When/how: at minimum a description carries Name, Purpose, and Outcomes; the rest is added only if deeper analysis or refinement requires it.
- **Input-Process-Output (IPO) diagram** — the representation used in **INCOSE SEHv5** to show typical inputs, activities, and typical outputs of each life cycle process.
  - When/how: to illustrate one possible way to perform a process — explicitly not a mandatory approach.
- **Concurrency, iteration, and recursion** — the three mechanisms that make life cycle processes non-linear, also discussed in **ISO/IEC/IEEE 15288** and the SEBoK Part 2 article *Applying the Systems Approach*.
  - When/how: applied continuously across system definition and realization to support communication, ongoing learning, and informed decision-making.

## Key Concepts

### Why describe processes consistently
A **life cycle model** is a framework of processes and activities for the life cycle; processes integrated into that framework are called **life cycle processes** (per the *Life Cycle Models* article). Describing those processes in a consistent manner makes them understandable, comparable, and manageable. Consistency gives a common language for how work is done, which reduces ambiguity, simplifies collaboration, and enables alignment with standards, regulations, and good practices. A consistent structure also makes processes easier to document, analyze, and improve systematically, and supports training and knowledge transfer.

### The required elements
- **Process Name (required)** — a concise noun phrase that identifies the process's main focus and distinguishes it from others. Verbs are avoided so the name does not resemble an activity or a purpose.
- **Process Purpose (required)** — one or more high-level goals stating *why* the process is performed; it clarifies scope and boundaries where processes appear to overlap. Ideally one concise sentence beginning "The purpose of the xxx process is…", avoiding "and" so unrelated goals are not bundled together. It does not summarize activities or outcomes.
- **Process Outcomes (required)** — measurable, observable results or changes of state achieved by executing the process. Unlike outputs, outcomes are *not* documents or information items — they are tangible technical or business achievements. Each is a single, present-tense declarative sentence (deliver a service, achieve a change of state, maintain a condition, meet requirements), avoiding "and"/"and/or". A process typically has **three to seven** concise outcomes, each supporting the purpose. Outcomes differ from **benefits**, a term reserved for broader organizational gains and are recorded as informative notes.

### The optional elements
- **Process Activities (optional)** — a "set of cohesive tasks of a process". Activities describe the broad actions to execute a process and group related tasks; if cohesive they can act as lower-level processes with their own purposes and outcomes. They should be strongly cohesive internally but loosely coupled to other activities, and are ongoing responsibilities rather than sequential steps — no timing or order is imposed unless explicitly required. All activities together must achieve the process outcomes and purpose.
- **Process Tasks (optional)** — a "required, recommended, or permissible action meant to help achieve one or more of a process's outcomes". Tasks are discrete points within the broader space of processes and activities; they support outcomes but need not fully cover an activity's scope. Sequencing is not assumed unless stated, preserving flexibility across life cycle models.
- **Process Inputs (optional)** — items transformed into outputs by the process, excluding the human or automated resources that do the work. Inputs may come from other processes, organizational resources, suppliers, or external sources; specifying them is optional in general but essential in closed-loop life cycles.
- **Process Outputs (optional)** — optional if outcomes can be demonstrated. Some are essential deliverables, others exist only for validation or audit. They are categorized as **artefacts** (prototypes, models, components, services) or **information items**, with artifacts further covering four generic work product types: **services, software, hardware, and processed materials**.

### Notes, controls, and constraints
- **Process Notes** add further detail on the what, how, and why — often explaining interrelationships with other processes and giving brief examples.
- **Process Controls and Constraints** guide or restrict how (and to some extent when) a process is performed. Controls can come from laws, regulations, organizational policies, voluntary standards, or supplier/customer agreements; constraints often stem from external environmental or business conditions.

### Elaboration in INCOSE SEHv5
INCOSE SEHv5 (section 2.3) applies a common structure to the system life cycle processes. To stay aligned with **ISO/IEC/IEEE 15288**, the standard's **purpose statements are reproduced verbatim** for each process, and activity titles follow the standard (describing *what*, not *how*). Each process is shown as an **IPO diagram** of typical inputs, activities, and typical outputs. Notably, the **outcomes** from 15288 are *not* carried into SEHv5 — it presents typical inputs and outputs instead. Controls and enablers are usually left off IPO diagrams, though they can be noted to show how inputs are transformed into outputs under process controls.

### Concurrency, iteration, and recursion
The system life cycle processes are sometimes mistakenly seen as linear and sequential, applied at a single hierarchy level. In reality, effective management depends on exchanging information and insight across processes and accounting for learning and feedback gathered as processes are applied.
- **Concurrency** — performing two or more processes in parallel where they do not strongly depend on each other's outputs. Example: **risk management and measurement** are typically continuous and concurrent.
- **Iteration** — repeated application and interaction between processes, to accommodate stakeholder decisions, incorporate learning and feedback, and respond to evolving understanding, architectural constraints, and trade-offs (affordability, feasibility, resilience, adaptability). It frequently occurs between **system requirements definition** and **system architecture definition** — evolving requirements drive architectural changes, which prompt updates back to requirements, design, or trade-offs.
- **Recursion** — applying the life cycle processes again and again across the system structure. **Technical Management and Technical Processes** run recursively, defining the system at continually lower levels until make/buy/reuse decisions are made; outputs from one element level become inputs to another, in both system definition and system realization, preserving consistency and integrity.

## Mental Models
- **Describe-then-apply.** First nail the *description* (uniform via 24774), then accept that *application* is non-linear (concurrency/iteration/recursion). The two are not in tension — a process is defined consistently precisely so it can be applied flexibly.
- **Outcome ≠ output.** An outcome is an achieved change of state; an output is a document or artifact. You can have outputs without achieving the outcome, and you can demonstrate an outcome without a particular output — which is why outputs are optional when outcomes are demonstrable.
- **Three required, the rest on demand.** Name, Purpose, Outcomes are the irreducible core; inputs, activities, tasks, and outputs are elaboration added only when deeper analysis warrants it.
- **Cohesive inside, loose outside.** Good activities (and tasks) are tightly related internally but loosely connected to one another — and carry no implied order unless explicitly required.
- **The IPO diagram is illustrative, not prescriptive.** It shows *one* possible way to perform a process, not the mandatory route.
- **Triage the three mechanisms by their driver:** parallelism with no strong output dependency → **concurrency**; feedback/learning across the same processes → **iteration**; the same processes pushed down (or up) the system hierarchy → **recursion**.

## Anti-patterns
*(Stated as cautions in the source rather than formally named patterns.)*
- **Verbs in a process name** — naming a process with a verb so it reads like an activity or purpose, blurring the distinction the Name element exists to preserve.
- **Bundling goals with "and" in the Purpose** — listing unrelated goals in one purpose statement, obscuring the process's scope and boundaries.
- **Conjunctions in Outcomes** — using "and"/"and/or" inside an outcome instead of separate present-tense statements.
- **Treating life cycle processes as linear and sequential at a single hierarchy level** — the explicitly identified misperception that concurrency, iteration, and recursion correct.

## Key Takeaways
1. Processes are the backbone of systematic SE; **ISO/IEC/IEEE 24774** standardizes their description for clarity, consistency, and comparability.
2. Every process description has three **required elements — Name, Purpose, Outcomes** — with Inputs, Activities, Tasks, and Outputs optional, plus Notes, Controls, and Constraints.
3. **Outcomes are achievements/changes of state, not documents**; a process typically has three to seven, each a single present-tense statement, distinct from benefits.
4. **INCOSE SEHv5** elaborates the 15288 processes with a common structure, verbatim purpose statements, and **IPO diagrams** (which omit the 15288 outcomes).
5. **Concurrency, iteration, and recursion** make life cycle management dynamic and non-linear, supporting continuous communication, learning, and informed decisions across system definition and realization.

## Connects To
- **Life Cycle Models (SEBoK)** — supplies the definition of a life cycle model as a framework of processes/activities; Process Concepts describes the processes that populate that framework.
- **Applying the Systems Approach (SEBoK Part 2)** — covers concurrency, iteration, and recursion for developing complex systems; this KA applies the same concepts to *life cycle processes*.
- **Technical Management and Technical Processes (SEBoK / ISO/IEC/IEEE 15288)** — the process groups applied recursively across the system structure; the recursion example is drawn from them.
- **ISO/IEC/IEEE 15288:2023** — the system life cycle processes standard whose purpose statements SEHv5 reproduces verbatim, and which itself discusses concurrency/iteration/recursion.
- **ISO/IEC/IEEE 24774:2021** — the process-description standard that defines the process elements (Name/Purpose/Outcomes and the optional set).
- **INCOSE SE Handbook v5 (2023)** — the elaboration source applying a common structure and IPO diagrams to the life cycle processes.
