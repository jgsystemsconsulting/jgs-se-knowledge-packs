# NIST SP 800-37 Rev. 2 (RMF) Patterns & Techniques

Reusable techniques drawn from the RMF, each with **when to reach for it**, **how it
works**, and the **trade-offs** the source flags. These are operating patterns for
running the framework, not a restatement of the steps (for which see the chapters).

---

## 1. Run the RMF as an SDLC overlay, not a parallel paper trail

**When** — every time you stand up RMF on a program that already has a System
Development Life Cycle.

**How** — execute the RMF tasks concurrently with the SDLC and let SDLC artifacts
(engineering plans, test/assessment results, action items) supply the evidence the RMF
asks for. Before creating any RMF-specific document, ask whether an existing SDLC
artifact already carries that information. The strongest implementations are nearly
indistinguishable from routine engineering.

**Trade-offs** — requires the RMF roles and the engineering team to coordinate up front;
done badly it produces duplicate, divergent documents. The pay-off is that risk
management stops being a late-stage compliance gate.

→ ch03, ch05

---

## 2. Push decisions up: maximize common controls and tailored baselines

**When** — at organization-level Prepare, and whenever a new system would otherwise
re-solve a control already solved centrally.

**How** — designate controls the organization can provide once and let many systems
inherit them (common controls); where only part is central, document the split as a
hybrid control. Build organizationally-tailored baselines (overlays) for recurring
contexts — cloud, industrial control systems, national security systems, high-value
assets, privacy — so individual systems start from a pre-resourced baseline instead of a
blank SP 800-53B baseline.

**Trade-offs** — concentrates risk and effort in the common-control provider; an
inherited control that is inadequate for a given system must be supplemented with
system-specific or hybrid controls, or the gap accepted as residual risk with sign-off.
Net effect is far less duplicated work per system.

→ ch03, ch04

---

## 3. Size the authorization boundary as a deliberate trade-off

**When** — system-level Prepare (Task P-11), and revisited during continuous monitoring.

**How** — group elements that share a mission/business function, similar operating
characteristics and requirements, similar information types and impact level, and the
same environment of operation; keep elements under common direct management inside one
boundary. Decide for each piece of the environment whether it is *in scope* (its
protections land in your plan) or *inherited* (the environment supplies them as common
controls).

**Trade-offs** — too wide and risk management becomes needlessly complex; too narrow and
you multiply separately managed systems and inflate cost. There is no universally right
boundary — it is context-driven and periodically re-judged.

→ ch02, ch03

---

## 4. Choose baseline (top-down) vs. organization-generated (bottom-up) per system

**When** — Select, Task S-1, once categorization has fixed the impact level.

**How** — for mainstream systems, start from the predefined SP 800-53B baseline and
tailor *down*. For highly specialized systems (a weapons system, a medical device) or
limited-scope systems (a smart meter), build the control set *up* from the requirements
using the organization's own process. Approaches can be mixed across a portfolio.

**Trade-offs** — the baseline path is fast and consistent but wastes effort when most of
a broad baseline gets deleted; the bottom-up path fits specialized systems but demands a
mature, well-defined requirements process to avoid gaps.

→ ch04

---

## 5. Shift assessment left and reuse the evidence

**When** — Assess (and continuously, in Monitor) — especially on iterative/agile programs.

**How** — assess controls during development, in parallel with the SDLC, per cycle as
each completes, rather than at a single end-of-life gate. Feed the results forward
through interim reports into the final assessment report. Establish *up front* what
evidence may be reused — prior audits, vendor/developer assessments, external
product-evaluation programs (Common Criteria, the Cryptographic Module Validation
Program), earlier SDLC testing, and reciprocity. Automate assessment procedures to widen
frequency, volume, and coverage.

**Trade-offs** — requires assessor independence to be set deliberately (the AO scales it
to law and policy), and reuse criteria must be written before the fact so reuse stays
principled rather than ad hoc. The pay-off is catching deficiencies when they are
cheapest and avoiding repeated work at authorization.

→ ch05, ch07

---

## 6. Route every deficiency to one of three destinies

**When** — Assess (A-5/A-6) and Authorize (R-3), whenever a finding is recorded.

**How** — for each deficiency, choose: **fix now** (initial remediation, then reassess —
assessors *add* findings, never overwrite the originals); **schedule it** (a POA&M entry
with tasks, resources, milestones, and dates); or **accept it** as residual risk (the AO
alone may accept; it is logged in the assessment reports for the audit trail but gets no
milestone). Prioritize by risk assessment, security categorization, and mission
criticality — not first-come-first-served.

**Trade-offs** — acceptance must be an explicit, accountable AO decision, not a silent
omission; only exploitable deficiencies are vulnerabilities, so severity routing has to
distinguish a finding from a true vulnerability.

→ ch05, ch06

---

## 7. Convert the dated authorization into ongoing authorization

**When** — once a continuous monitoring program is robust and mature (Authorize R-4,
Monitor M-6).

**How** — keep the authorization package live (plans, assessment reports, POA&M updated
on an ongoing basis), then replace the fixed termination date with a time-driven
re-judgment frequency. The AO re-confirms or withdraws acceptance on a rolling basis from
monitoring evidence; reauthorization becomes a by-product of keeping the package current.
GRC and automated reporting tools assemble, transmit, and refresh the package.

**Trade-offs** — depends entirely on monitoring maturity and timely artifact updates;
without them, ongoing authorization and reauthorization break down. Automate the
paperwork, but the source still treats risk *acceptance* as a human accountability.

→ ch06, ch07

---

## 8. Treat disposal as a risk event with inheritance impact

**When** — Monitor, Task M-7, when any system or element leaves operation.

**How** — execute the disposal strategy: sanitize media (SP 800-88), preserve component
authenticity and required records, update inventory and posture reports, and notify
affected users and application owners. Critically, review and assess every
control-inheritance relationship — disposing of a common-control provider can leave
dependent systems exposed.

**Trade-offs** — treating end-of-life as a clean-up chore rather than a managed risk
event is the failure mode the task exists to prevent; the inheritance review is the
non-obvious step that catches downstream exposure.

→ ch07
