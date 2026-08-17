# Phase 10: Source Vetting - Research

**Researched:** 2026-08-17
**Domain:** Licence-vetting / US-government public-domain source clearance (not pack construction)
**Confidence:** MEDIUM — three of six named candidates have in-source or official-metadata licence evidence this session; Army CBA, DoDM 5000.102, and AAF guidebook PDFs remain unreachable

<user_constraints>
## User Constraints (from STATE / REQUIREMENTS; no CONTEXT.md)

**CRITICAL:** Discuss was skipped. There is no CONTEXT.md. Locked decisions below are taken from STATE.md, REQUIREMENTS.md, ROADMAP.md, and SEED-001 — these MUST be honored by the planner.

### Locked Decisions

- This is a **documentation / vetting phase, NOT a pack-build phase**. Phase 11 builds packs from what this phase **clears**. [VERIFIED: `.planning/ROADMAP.md:31-39` — "Every v1.19 candidate has a definitive tier decision; AAF stays unused until cleared"]
- Requirements in scope: **VET-19-01, VET-19-02, VET-19-03, VET-19-04 only**. IO-01..07, MAP-19, HYG, REL-19 are Phase 11–13. [VERIFIED: `.planning/REQUIREMENTS.md:12-17`]
- **AAF stays unused until cleared.** Phase 6 deferral is still in force. [VERIFIED: `.planning/REQUIREMENTS.md:16` — "licence spot-check BEFORE any use (Phase 6 deferral still in force); record Tier or keep Excluded-pending"]
- **Honest deferral is a valid outcome.** ROADMAP SC-1 explicitly allows "or FUT-04 remains deferred with fresh evidence". [VERIFIED: `.planning/ROADMAP.md:36`]
- STATE already expects AAF not to clear: "IO-05/IO-06 are conditional on AAF clearing VET-19-03 — expect honest deferral". [VERIFIED: `.planning/STATE.md:56`]
- **Do not invent a pack** (IO-07 pattern; applies to any candidate that does not clear). [VERIFIED: `.planning/REQUIREMENTS.md:27`]
- **No source URLs in `docs/SOURCE-VETTING.md`** (or packs). URLs live only in this research store. [VERIFIED: `.planning/ROADMAP.md:39` — "New exclusions in docs/SOURCE-VETTING.md; no source URLs in that doc"]
- **Do not treat "unreachable" as Tier 1.** In-source licence evidence is required before a build-clear. [VERIFIED: `docs/SOURCE-VETTING.md:182` — "Found the **licence statement** in the source itself (not a third-party claim)."]
- Stay on `main`. No branches / worktrees. No pack directories created this phase.

### Claude's Discretion

- Whether FUT-04 / DoDM 5000.102 land as **deferred-with-fresh-evidence** vs **Excluded** (both are valid under ROADMAP SC-1 / the Def Stan 00-051 pending pattern). Prefer deferral when the only defect is reachability, not a negative licence finding.
- Whether GPS clearance is **IS-GPS-200N only** or **IS-GPS-200N + IS-GPS-705J / IS-GPS-800J** as the "select" set (there is no IS-300 — see candidates).
- Whether SP-7084 is restated as a v1.19 Vetted row or only reconfirmed by pointer to the existing v1.18 row (it is already Tier 1).
- How to word the AAF Excluded-pending row without putting URLs in SOURCE-VETTING.

### Deferred Ideas (OUT OF SCOPE)

- Pack builds, chapter generation, catalog registration (Phase 11 / 13)
- Capability-map regen, HYG-01..04, vet_source EXCLUDED sync (Phase 12)
- NASA-HDBK-2203 / NPR 7150.2 (REQUIREMENTS Out of Scope) [VERIFIED: `.planning/REQUIREMENTS.md:57`]
- Per-role packs; se-agents consumer refresh; FUT-05; committed overlap checker
- Inventing a Stakeholder Engagement pack (IO-07)
</user_constraints>

<architectural_responsibility_map>
## Architectural Responsibility Map

Single-tier compliance documentation — all Phase 10 capabilities reside in the **repo integrity / planning store** (docs + `.planning`). No Browser/Client, API, or Database tier.

| Capability | Primary Tier | Secondary Tier | Rationale |
|------------|-------------|----------------|-----------|
| Live fetch + in-source licence read | Planning store (`10-RESEARCH.md`) | — | Link Policy: URLs and quotes live only in research |
| Tier decision (1 / 2 / Excluded / deferred) | Published integrity doc (`docs/SOURCE-VETTING.md`) | REQUIREMENTS / STATE annotations | Human judgement; CI only greps URL-absence and later pack fields |
| Phase 11 handoff (cleared / deferred / excluded) | This RESEARCH + SOURCE-VETTING v1.19 section | ROADMAP SC text | Planner/executor of Phase 11 must not re-guess |
</architectural_responsibility_map>

<research_summary>
## Summary

Phase 10 must give every v1.19 candidate a **dated tier decision** and leave AAF unused unless an in-source grant is found. The established process is the Phase 6 pattern: live HTTP + in-PDF/metadata inspection; verdicts written to `docs/SOURCE-VETTING.md` with **zero http/https**; URLs and quotes stored only in `{phase}-RESEARCH.md`; honest deferral when a PDF cannot be opened.

This session re-fetched every named candidate. **Cleared (Tier 1 leaning, build-time in-source still required):** NASA-STD-8719.14C (official PDF + "Internet Public"), GPS **IS-GPS-200N** (in-PDF DIST-A; there is **no IS-300**), NASA SP-7084 (NTRS metadata reconfirmed). **Not cleared:** FUT-04 Army CBA (live 403, Wayback 503 — same class as Phase 7), DoDM 5000.102 (WHS/media.defense.gov 403 — never ingested in `dod-vva-rpg`), AAF Product Support + Software pathway (Cloudflare 403 on aaf.dau.edu; DAU→WarU 404 on the 2022 PSM PDF path; landing-page `Copyright © 2022 … DAU` is not a redistribution grant).

**Primary recommendation:** Plan a single documentation wave (Phase 6 analogue). Write a `Vetted candidates (v1.19.0)` section for the three cleared sources; keep Army CBA as FUT-04 deferred-with-fresh-evidence; record DoDM 5000.102 as unverified / deferred-excluded this milestone; keep AAF as **"NOT yet vetted — do not use"**. Do not start Phase 11 packs from uncleared names. Phase 11 IO-01/IO-02 fallbacks (A-94 / VV&A remap; more VV&A chapters) are already specified and do not need a new source.
</research_summary>

<standard_stack>
## Standard Stack / existing process

This repo does not add a library for vetting. The stack is the integrity rubric + sibling tooling + the Phase 6 write-up pattern.

### Core

| Artifact | Version / location | Purpose | Why standard |
|---------|--------------------|---------|--------------|
| `docs/SOURCE-VETTING.md` | living; last v1.18 rows 2026-08-14/16 | Published tier register + Excluded table | "No pack is accepted unless its source clears this rubric." [VERIFIED: `docs/SOURCE-VETTING.md:8-9`] |
| `docs/LICENSING.md` §4 | living | Link Policy rationale | Attribution is title+publisher+version, never a source URL [VERIFIED: `docs/LICENSING.md:72-73`] |
| Phase RESEARCH.md | `2-RESEARCH.md`, `6-RESEARCH.md`, this file | Private URL + quote store | "Link Policy: source URLs live only in this research store, never in docs/ or packs." [VERIFIED: `.planning/phases/6-source-vetting-unverified-resolution/6-RESEARCH.md:8-9`] |
| `jgs-reference-skill/tools/vet_source.py` | sibling repo (not in this tree) | Mechanical gate at **build** (Phase 11) | Encodes SOURCE-VETTING as code; exit 2 = Excluded. Phase 10 does not run it to invent a tier. |

### Supporting

| Artifact | Purpose | When to use |
|---------|---------|-------------|
| `docs/SOURCE-VETTING.md` checklist (8 boxes) | Human pre-PR rubric | Every candidate before a pack PR; Phase 10 completes boxes 1–4 only [VERIFIED: `docs/SOURCE-VETTING.md:180-189`] |
| `tooling/validate_pack.py` | Enforces PACK.yaml fields + `license_tier ∈ {1,2,3}` | Phase 11+, not Phase 10 |
| Statute string | `Public Domain (US Government work, 17 U.S.C. § 105)` | PACK.yaml `license` for cleared US-gov works (Phase 7 convention) |
| DIST-A variant | `… Distribution Statement A — Approved for public release; distribution is unlimited` | DoD / GPS copies that carry DIST-A in-source |

### Alternatives Considered

| Instead of | Could Use | Tradeoff |
|------------|-----------|----------|
| Live in-source read | Statute-only Tier 1 (17 U.S.C. § 105) | Phase 6 GP-06 did this and Phase 7 then **dropped** Army CBA when fetch failed. Do not repeat the over-claim. |
| Excluded table for every miss | Deferred / Excluded-pending prose | Excluded is a hard stop that blocks revisit. Deferral is the Phase 6 AAF / Def Stan pattern when the defect is reachability. |
| Building from Wayback / FAS / everyspec as canonical | Mirror as fetch locator only | Gap report: mirrors are "fallback download locators — canonical copies must come from" official hosts. [VERIFIED: `.planning/research/capability-gap-report.md:175`] |

**Installation:** none. Phase 10 is Edit-only on docs/planning files.

### How vetting is done in this repo (planner must copy)

1. Identify exact title, version, publisher.
2. Fetch the **official** landing page / PDF (browser UA; expect Akamai/Cloudflare 403).
3. Read the **licence statement in the source itself** (PDF cover, NTRS metadata, DIST-A block). "Free to download" is not a grant. [VERIFIED: `docs/SOURCE-VETTING.md:15-19`]
4. Assign Tier 1 / 2 / 3 / Excluded with a dated stamp.
5. Write the published row **without URLs**; point at this `10-RESEARCH.md` as the URL store (v1.17 pointed at `2-RESEARCH.md`; v1.18 at `6-RESEARCH.md`). [VERIFIED: `docs/SOURCE-VETTING.md:95-97`]
6. If unreachable: **do not** write Tier 1. Defer with fresh HTTP evidence, or Excluded if stale/unusable (AFOTEC pattern).
7. Stop. Do not extract, outline, or scaffold.
</standard_stack>

<architecture_patterns>
## Architecture Patterns

### System Architecture Diagram

```text
  official host (nasa.gov / gps.gov / army.mil / esd.whs.mil / aaf.dau.edu / waru.edu)
           |  HTTP 200 PDF or HTML
           |  or 403 / 404 / CF challenge / 503
           v
  Phase RESEARCH store  ----------------->  quotes, URLs, HTTP codes, edition
           |                                         (never published)
           | verdict + dated rationale
           v
  docs/SOURCE-VETTING.md  ---- Link Policy grep (zero http) ---->  published register
           |  Vetted (v1.19.0)  |  Excluded table  |  Excluded-pending / FUT
           v
  Phase 11 planner
           |-- CLEARED Tier 1/2 --> pack build (vet_source + extract + PACK.yaml)
           |-- DEFERRED           --> IO fallback already in REQUIREMENTS (remap / more VV&A / record deferred)
           +-- EXCLUDED           --> never package; VET-19-04 row only
```

### Recommended Project Structure (Phase 10 outputs only)

```
.planning/phases/10-source-vetting/
├── 10-RESEARCH.md          # this file — URL + quote store
├── 10-01-PLAN.md           # planner writes; docs-only tasks
└── 10-01-SUMMARY.md        # executor
docs/SOURCE-VETTING.md      # Vetted (v1.19.0) + any new Excluded / pending rows
.planning/REQUIREMENTS.md   # VET-19 checkboxes stay open until verify
.planning/STATE.md          # Phase 10 deviation note (verdicts)
```

Do **not** create `packs/`, `sources/`, or catalog rows.

### Pattern 1: Phase 6 write-up (copy this)

**What:** One execute plan that only edits integrity surfaces. Eight dated Vetted rows + Excluded rows; pointer paragraph names the RESEARCH file; Task 5 greps `http` = 0.
**When to use:** Every vetting phase.
**Example (pointer paragraph, no URL):**

```markdown
Source URLs for all vetted/excluded/UNVERIFIED candidates are recorded in
`.planning/phases/10-source-vetting/10-RESEARCH.md` (Link Policy: never
published in docs or packs).
```

[VERIFIED pattern: `docs/SOURCE-VETTING.md:95-97`]

### Pattern 2: Honest deferral / Excluded-pending

**What:** When the 5th gap-report item (AAF licence spot-check) was never resolved, Phase 6 **did not** silently substitute a Tier. The DAG Excluded row now says AAF guidebooks "are NOT yet vetted — licence spot-check deferred … vet before any future use". [VERIFIED: `docs/SOURCE-VETTING.md:85`]
**When to use:** Army CBA (retry failed again), DoDM 5000.102 (no PDF this session), AAF (still no in-source guidebook read).

### Pattern 3: Statute-basis is not build-clearance

**What:** GP-06 federal-bca was recorded "Confirmed-by-statute 2026-08-16; build-time check outstanding." [VERIFIED: `docs/SOURCE-VETTING.md:135`] Phase 7 then applied P7-PRE-2: A-94 PASS in-source; Army CBA **FAIL TO FETCH** 403/503 and was dropped. [VERIFIED: `packs/federal-bca/PACK.yaml:21-24`]
**When to use:** Any US-gov candidate whose PDF was not opened. Statute may *predict* Tier 1; it does not *clear* Phase 11.

### Pattern 4: Title / edition corrections belong in the Vetted row

Phase 6 corrected SP-7084's title, DAFMAN 63-119's title, and VV&A's "consolidated PDF" premise. Phase 10 must correct **"GPS ICD-IS-200/300"** → **IS-GPS-200N** (no IS-300 on the public list).

### Anti-Patterns to Avoid

- **Using AAF before clearance** — Phase 6 MA-01 was exactly this class of silent substitution. [VERIFIED: `.planning/phases/6-source-vetting-unverified-resolution/6-REVIEW-FIX.md:26-30`]
- **Inventing packs** to fatten a cluster.
- **Putting source URLs in SOURCE-VETTING.md.**
- **Treating unreachable as Tier 1.**
- **Building from a 2022 Wayback AAF HTML copyright footer** as if it were an in-PDF grant.
- **Selecting "IS-300"** — that identifier is not on gps.gov.
- **Re-opening GP-08 / NASA-HDBK-2203** — out of v1.19 scope.
</architecture_patterns>

<dont_hand_roll>
## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| Licence classifier | New Python rubric | Existing SOURCE-VETTING tiers + sibling `vet_source.py` at Phase 11 build | Rubric already encodes Excluded keywords, US-gov, CC, "free ≠ redistribute" |
| Pack from an uncleared PDF | "We'll vet during extract" | Stop at SOURCE-VETTING | P7-PRE-2 showed fetch-fail must halt **before** generation |
| Decision Analysis depth if Army CBA dies | New invented CBA framework | IO-01 remap of existing A-94 / VV&A decision chapters | Already specified [VERIFIED: `.planning/REQUIREMENTS.md:21`] |
| Validation depth if DoDM dies | Invented VV&A manual | Additional chapters in existing `dod-vva-rpg` | Already specified [VERIFIED: `.planning/REQUIREMENTS.md:22`] |
| AAF substitute from `dod-rio` AAF chapters | Treat dod-rio as Product Support / Software pathway clearance | Keep AAF unused | dod-rio chapters describe AAF pathways from a **different** vetted DoD RIO source; they do not licence AAF guidebooks |
| URL-safe SOURCE-VETTING | Manual proofreading only | `grep -c http docs/SOURCE-VETTING.md` expect `0` | Phase 6 Task 5 gate |

**Key insight:** Phase 10's deliverable is a **decision table**, not a toolchain. The expensive problems (Akamai, Cloudflare, DIST-A image covers, dual-source halt) are already solved as process, not code.
</dont_hand_roll>

<common_pitfalls>
## Common Pitfalls

### Pitfall 1: Using AAF before clearance

**What goes wrong:** Phase 11 builds `aaf-product-support` / `aaf-software` from DAU/WarU HTML or a 2022 PDF path. Takedown or copyright-footer conflict.
**Why it happens:** Gap report listed AAF as "Tier 1" on a `.mil`/`.edu` heuristic; 6-RESEARCH §3a even called AAF "the Tier 1 substitute" for DAG **before** the licence spot-check. [VERIFIED: `.planning/phases/6-source-vetting-unverified-resolution/6-RESEARCH.md:165`]
**How to avoid:** VET-19-03 binary: in-source grant → Tier 1/2 row; else keep **"NOT yet vetted — do not use"**. STATE already expects deferral.
**Warning signs:** Plan tasks that `mkdir packs/aaf-*` or that treat the AAF site copyright line as a grant.

### Pitfall 2: Inventing packs

**What goes wrong:** A "stakeholder engagement" or "generic CBA" pack is synthesized to move a cluster number.
**Why it happens:** SEED-001 pressure to fatten primaries.
**How to avoid:** No source, no pack. IO-07 is explicit. Army CBA / DoDM / AAF misses use the recorded fallbacks.
**Warning signs:** PACK.yaml with no identifiable edition.

### Pitfall 3: Putting URLs in SOURCE-VETTING.md

**What goes wrong:** Link Policy breach; LICENSING.md §4 violated; Phase 6 verify gate fails.
**Why it happens:** Wanting "evidence" in the published doc.
**How to avoid:** Pointer sentence to `10-RESEARCH.md`; `grep -c http` = 0 (note `17 U.S.C. § 105` is not a URL).
**Warning signs:** `https://` in a Vetted or Excluded cell.

### Pitfall 4: Treating "unreachable" as Tier 1

**What goes wrong:** A statute-only row is later built from a random mirror; in-source third-party notices are missed.
**Why it happens:** 17 U.S.C. § 105 is true for US-gov works **in the abstract**; contractor inserts and © footers exist in the wild (GPS lists SAIC as Interface Control Contractor; AAF HTML says `Copyright © 2022`).
**How to avoid:** Unreachable → deferred or Excluded-pending. Never "Tier 1 (assumed)".
**Warning signs:** Vetted row with no quote and no "build-time confirmation REQUIRED".

### Pitfall 5: Selecting the wrong GPS document

**What goes wrong:** Plan says "ICD-IS-200/300" and executor searches for a non-existent IS-300, or packages ICD-GPS-153 (request-form only).
**Why it happens:** Gap report / SEED-001 used "ICD-IS-200/300 series" as shorthand. [VERIFIED: `.planning/seeds/SEED-001-agent-io-pack-depth.md:61`]
**How to avoid:** Public set is IS-GPS-200 / 705 / 800 + ICD-GPS-240 / 870. **Select = IS-GPS-200N** (optionally 705J/800J). Skip ICD-GPS-153.
**Warning signs:** Filename `IS-GPS-300` or "IS-300" in a Vetted Source cell.

### Pitfall 6: Re-clearing SP-7084 as if it were new — or ignoring the edition fork

**What goes wrong:** Either a duplicate pack, or a 1998 everyspec copy packaged without recording which edition.
**Why it happens:** VET-19-02 lists SP-7084 again; v1.18 left it "evidence-only" because cluster 25 was filled by 40051.
**How to avoid:** Reconfirm Tier 1; if Phase 11 wants the diversity pack, record 1990 NTRS vs 1998 everyspec in PACK.yaml (Phase 6 preference: 1998 if text layer else 1990 canonical).
**Warning signs:** New Excluded row for SP-7084.

### Pitfall 7: DAU hostname churn (WarU)

**What goes wrong:** Executor follows 2022 `dau.edu/pdfviewer?Guidebooks/Product-Support-Manager-(PSM)-Guidebook.pdf` and treats 301→`waru.edu` 404 as "cleared because official".
**Why it happens:** DAU properties now redirect to `www.waru.edu` (official `.gov` "An official website of the United States government" — observed 2026-08-17).
**How to avoid:** 404 / Cloudflare 403 = not cleared. Need the **current** guidebook PDF + its own licence page.
**Warning signs:** Plans that say "DAU is US-gov so all guidebooks are Tier 1".
</common_pitfalls>

<code_examples>
## Code Examples (process, not application code)

### Published Vetted row (no URL)

```markdown
| **NASA-STD-8719.14C** (Process for Limiting Orbital Debris; Version C, 2021-11-05; ACTIVE) | Tier 1 | NASA-authored US Government work (17 U.S.C. § 105). Official NTSS access control: "Internet Public -- Standard is cleared for public accessibility on the internet." In-PDF title page confirms NASA TECHNICAL STANDARD, Approved 2021-11-05, 77 pp; no copyright / all-rights-reserved notice in the text layer. Confirm no third-party inserts at Phase 11 build (10-RESEARCH.md §NASA-STD-8719.14). (Verified 2026-08-17.) |
```

### Published Excluded / pending row (no URL)

```markdown
| **DAU/WarU AAF Product Support Manager Guidebook + Software pathway guidebooks** | Intended DAG substitute still NOT yet vetted — do not use. 2022 AAF guidebooks index carries "Copyright © 2022 Adaptive Acquisition Framework - Defense Acquisition University"; live guidebook PDFs were not opened this session (Cloudflare 403 / WarU 404). Keep Excluded-pending until an in-source redistribution grant is quoted (10-RESEARCH.md §AAF). (Verified 2026-08-17.) |
```

### Link Policy gate (Phase 6 Task 5)

```bash
test "$(grep -c 'http' docs/SOURCE-VETTING.md)" = "0"
# 17 U.S.C. § 105 is plain text, not a URL
```

### Phase 11-only vet_source invocation (do NOT run in Phase 10)

```bash
# sibling repo; statute string from 7-RESEARCH convention
python "$REF/tools/vet_source.py" \
  --title "Process for Limiting Orbital Debris" \
  --publisher "NASA" \
  --license "Public Domain (US Government work, 17 U.S.C. § 105)"
# Expect tier 1, exit 0
```

`vet_source.py` US-gov / PD signals (for planner awareness only):

```
US_GOV = ("nasa", "nist", "department of defense", "dod", ... "army", ...)
PD_LICENSE = ("public domain", "17 u.s.c", "us government work",
              "distribution statement a", "distribution a", "cc0", ...)
```

[VERIFIED: `C:/Users/gower/OneDrive/Documents/GitHub/jgs-reference-skill/tools/vet_source.py:58-64`]

HYG-03 (Phase 12) still needs `afotec` / `dod-dag` / `cmu-sei` added to that EXCLUDED dict — **not** a Phase 10 task.
</code_examples>

<sota_updates>
## State of the Art (this session, 2026-08-17)

| Old assumption (gap report / SEED-001) | Current observation | When observed | Impact |
|----------------------------------------|---------------------|---------------|--------|
| Army CBA PDF is a live army.mil file | asafm.army.mil still Akamai **403 Access Denied** (489-byte HTML); Wayback CDX has PDFs through 2026-05-19 but playback **503** | 2026-08-17 | FUT-04 not cleared; same failure class as Phase 7 |
| DoDM 5000.102 at esd.whs.mil is fetchable | Entire `esd.whs.mil` issuance tree 403 from this environment; GovInfo search empty; media.defense.gov 403 | 2026-08-17 | Cannot in-source; not in `dod-vva-rpg` |
| "GPS ICD-IS-200/300" | Public list has **IS-GPS-200N**, 705J, 800J, ICD-GPS-240D, 870E. **No IS-300.** ICD-GPS-153 is request-form only | 2026-08-17 | Title correction required |
| AAF guidebooks live at aaf.dau.edu | aaf.dau.edu Cloudflare challenge (403); `dau.edu` **301 → waru.edu**; 2022 PSM PDF path **404** | 2026-08-17 | Host churn + no PDF = keep unused |
| DAU is the training host name | `www.waru.edu` presents as official US .gov ("An official website of the United States government") and lists AAF as a knowledge asset | 2026-08-17 | Rename awareness only — not a licence grant |
| NASA-STD-8719.14 URL with dots | NTSS slug is `nasa-std-871914` (no dots); Version **C** 2021-11-05 ACTIVE; real PDF (not a GP-08 placeholder) | 2026-08-17 | Cleared-leaning |

**Deprecated/outdated:**

- Treating `https://aaf.dau.edu/guidebooks/` as a stable PDF library.
- Dual-source `federal-bca` as if Army CBA were already inside the pack (it is A-94-only).
- "IS-300" as a public GPS ICD name.

**Official public-domain basis (not a substitute for in-source):**

17 U.S.C. § 105: "Copyright protection under this title is not available for any work of the United States Government". [CITED: https://www.copyright.gov/title17/92chap1.html#105]
</sota_updates>

<candidate_findings>
## Candidate-by-candidate findings

Planner-consumable. Confidence is for the **Phase 10 decision**, not for a future human-browser fetch.

### Decision table (Phase 11 input)

| ID | Candidate | Phase 10 decision | Confidence | Phase 11 action |
|----|-----------|-------------------|------------|-----------------|
| VET-19-01 | FUT-04 Army CBA Guide (ASAFM) | **DEFERRED** (unreachable; no in-source). Not Tier 1. | HIGH (failure class) | Do **not** build Army CBA. IO-01 uses A-94 / VV&A remap. Keep FUT-04 open or Excluded-pending — do not invent a CBA pack. |
| VET-19-02a | DoDM 5000.102 | **UNVERIFIED / deferred-excluded this milestone** (no PDF opened). Not Tier 1. | HIGH (no in-source) | Do **not** create `dodm-5000-102`. IO-02 = additional `dod-vva-rpg` chapters. |
| VET-19-02b | NASA-STD-8719.14C | **Tier 1 leaning** — official PDF + Internet Public + NASA authorship. Build-time third-party scan still required. | HIGH | IO-03 GO (`nasa-std-8719-14`). |
| VET-19-02c | GPS ICD "IS-200/300" | **Tier 1 leaning on IS-GPS-200N** (in-PDF DIST-A). **IS-300 does not exist** on the public page. | HIGH (200N); HIGH (no 300) | IO-04 GO on **IS-GPS-200N** (optional +705J/+800J). Do not search for IS-300. |
| VET-19-02d | NASA SP-7084 | **Tier 1 RECONFIRMED** (already on v1.18 Vetted). | HIGH | Optional Training-diversity pack; not an IO-01..07 must. If built, record 1990 vs 1998 edition. |
| VET-19-03 | AAF Product Support + Software pathway | **NOT yet vetted — do not use** (Excluded-pending). | HIGH | IO-05 / IO-06 **record deferred**. No AAF pack. |
| VET-19-04 | Newly ruled-out | Only add Excluded rows for sources the planner **rules out**. Deferrals are not automatic Excluded-table rows. | HIGH | If Army CBA / DoDM / AAF stay pending, VET-19-04 may be a no-op plus the AAF pending sentence. |

---

### 1. FUT-04 — US Army Cost Benefit Analysis Guide (ASAFM)

**Prior evidence (do not weaken):** Phase 7 dual-gate failed: "asafm.army.mil returned HTTP 403 (Akamai) for all tried paths; Wayback CDX/API returned 503 from this environment; no alternate public PDF obtained." [VERIFIED: `packs/federal-bca/PACK.yaml:21-24`] SOURCE-VETTING GP-06 still claims dual-source statute-basis with build-time check outstanding — that Army half is **stale relative to the shipped pack** (A-94-only). [VERIFIED: `docs/SOURCE-VETTING.md:135`]

**This session:**

- Live PDF `https://www.asafm.army.mil/Portals/72/Documents/Offices/CE/US%20Army%20Cost%20Benefit%20Analysis.pdf` → **HTTP 403** `text/html` 489 bytes, title `Access Denied` (Akamai). Same stub class as Phase 7.
- Host home and `/Offices/Cost-Estimating/` also 403.
- Wayback CDX (filter status 200 / `application/pdf`) lists captures including `20201019234245` … `20260519133432` (length ~1.3 MB). Playback of `20221006014603id_` and `20260519133432id_` and `20201019234245` → **HTTP 503** "No server is available to handle this request."
- No in-PDF licence statement obtained.

**Licence pattern [ASSUMED until PDF opens]:** ASAFM / US Army document would normally be a US Government work under 17 U.S.C. § 105. That is **prediction**, not clearance.

**Decision:** **DEFERRED** with fresh 2026-08-17 evidence. Satisfies ROADMAP SC-1's "or FUT-04 remains deferred with fresh evidence". Does **not** satisfy a strict reading of VET-19-01 "build-or-exclude with in-source licence evidence" — planner should **annotate VET-19-01** as "retry failed; deferred, no in-source; not a build-clear" rather than tick it as built. Prefer **not** putting Army CBA on the Excluded table unless the user wants a hard stop (nothing negative was found; the PDF is historically real).

**Confidence:** HIGH that it is not cleared. LOW on eventual licence text.

---

### 2. DoDM 5000.102 (VV&A implementing manual)

**Prior:** Gap report listed `https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodm/5000102m.PDF` as Tier 1, ~30 pp, clusters 8/7. [VERIFIED: `.planning/research/capability-gap-report.md:81`] Archived v1.18 REQUIREMENTS parenthetical "(+ DoDM 5000.102)" on GP-01. Phase 7 research build sheet is **RPG chapter-wise only**; 7-PLAN_CHECK: "DoDM 5000.102 is a REQUIREMENTS parenthetical / gap-report companion, not a 7-RESEARCH build-sheet input." Shipped `dod-vva-rpg` provenance lists 10 RPG chapter PDFs — **no 5000.102**. [VERIFIED: `packs/dod-vva-rpg/PACK.yaml:25-35`]

**This session:**

- `…/dodm/5000102m.PDF` and lowercase `.pdf` → **403 Access Denied**.
- `https://www.esd.whs.mil/Directives/issuances/dodm/` and even a sample DoDI PDF → **403** (host-level bot block, not a missing-file 404).
- `https://media.defense.gov/2022/May/13/2002996697/-1/-1/1/DODM-5000.102.PDF` → 403 (URL guessed; not confirmed as the real object).
- Wayback CDX for the WHS URL: `20250919115812` 200 `application/pdf`; playback `id_` → **502**.
- GovInfo search: not found.
- DLA QuickSearch home is reachable; no 5000.102 record was retrieved (issuances are usually on WHS, not ASSIST).

**Licence pattern [ASSUMED]:** A current DoD Manual authored by OSD/WHS is a US Government work; many carry DIST-A or "unclassified / public release". **Not verified in-source.**

**Decision:** **UNVERIFIED / deferred-excluded for v1.19 build**. Dated rationale: official PDF not readable from this environment; no in-source statement; must not be labelled Tier 1. IO-02 fallback already exists.

**Confidence:** HIGH (not cleared). MEDIUM that a human browser on WHS would get the PDF (Phase 6 DAFMAN pattern: 403 to curl, 200 to rendered fetch).

---

### 3. NASA-STD-8719.14 — Process for Limiting Orbital Debris

**Official record (live):** `https://standards.nasa.gov/standard/nasa/nasa-std-871914` HTTP **200**.

Verbatim NTSS fields this session:

- Title: `Process for Limiting Orbital Debris`
- `Document Number NASA-STD-8719.14`
- `Version C` `Document Date 11/05/2021` `Is Active? ACTIVE`
- `Document Access Control` / `Document Viewable by` / `Export Control/Distribution Authorization` : **`Internet Public -- Standard is cleared for public accessibility on the internet.`**
- `PUBLIC: Upload Publicly Available Standard nasa-std-871914c.pdf (884.36 KB)`

**PDF:** `https://standards.nasa.gov/sites/default/files/standards/NASA/C/0/nasa-std-871914c.pdf` → HTTP **200** `application/pdf` 905,584 bytes. In-PDF first page (pdftotext):

```
NASA TECHNICAL STANDARD
National Aeronautics and Space Administration
NASA-STD-8719.14C
Approved: 2021-11-05
Superseding NASA-STD-8719.14B
Process for Limiting Orbital Debris
```

Document reports `5 of 77` on the Foreword page (77 pp). Text-layer scan: **0** hits for `Copyright`, `All rights`, `public release`, `17 U.S.C`; "DISTRIBUTION" hits are orbital-debris physics, not DIST-A.

**Contrast with GP-08:** NASA-HDBK-2203's standards-page PDF was a ~5.9 KB placeholder. This is a real 884 KB standard. Do not conflate.

**Decision:** **Tier 1 leaning**. Basis: NASA US-gov authorship + NTSS "Internet Public" + downloadable official PDF + no contrary notice in the text layer. Phase 11 must still scan for third-party inserts (Phase 3 NASA pattern) and quote the Internet Public / title-page lines in PACK.yaml notes.

**Confidence:** HIGH.

---

### 4. GPS ICD / IS — "IS-200/300 (select)"

**Official page (live):** `https://www.gps.gov/interface-control-documents-icds-interface-specifications-iss` HTTP **200**.

Verbatim:

> `GPS.gov only publishes ICDs approved for public release.`

Public documents named on the page (this session): **IS-GPS-200 N** (orig. 08/22/2022, rev. 01/19/2024), **IS-GPS-705 J**, **IS-GPS-800 J**, **ICD-GPS-240 D**, **ICD-GPS-870 E**. **No `IS-300` / `IS-GPS-300` string.** ICD-GPS-153 is explicitly *not* posted (request form).

**IS-GPS-200N PDF:** `https://www.gps.gov/sites/default/files/2025-07/IS-GPS-200N.pdf` → HTTP **200** `application/pdf` 3,338,120 bytes. In-PDF cover (pdftotext):

```
DISTRIBUTION STATEMENT A. Approved for public release. Distribution is unlimited.
...
PNT Technical Director, MilComm & PNT Directorate,
Space Systems Command (SSC)
...
Interface Control Contractor:
SAIC (GPS SE&I)
...
TITLE:
NAVSTAR GPS Space Segment/Navigation User Segment
Interfaces
IS-GPS-200
REV: N
```

Revision record includes `N/A Changed distribution status to Public Release`. Zero `Copyright` / `All rights` hits in the extracted text. **IS-GPS-705J** cover carries the same DIST-A sentence (sampled).

**Licence analysis:** DIST-A is this repo's textbook Tier 1 signal for defense documents. [VERIFIED: `docs/SOURCE-VETTING.md:35-36`] SSC authorship is US Space Force. SAIC is named as Interface Control Contractor — watch-item (contractor-prepared form), **not** an all-rights-reserved notice. `vet_source.py` already warns US-gov works may quote third parties.

**Decision:** **Tier 1 leaning for IS-GPS-200N** (and the same DIST-A family 705J/800J if Phase 11 wants more than one exemplar). **IS-300 is a naming error** — do not Excluded-table a phantom document; correct the identifier in the Vetted row. Do not package ICD-GPS-153.

**Confidence:** HIGH for 200N DIST-A. HIGH that IS-300 is not public. MEDIUM on whether Phase 11 should add 705/800 (scope / page-count, not licence).

---

### 5. NASA SP-7084

**Already recorded Tier 1** in SOURCE-VETTING v1.18: NTRS metadata `Work of the US Gov. Public Use Permitted`; Distribution Limits Public; prefer 1998 if text layer else NTRS 1990. [VERIFIED: `docs/SOURCE-VETTING.md:129`]

**This session reconfirm:**

- NTRS `https://ntrs.nasa.gov/citations/19900017394` HTTP **200**.
- HTML contains `Distribution Limits` → `Public` and `Copyright` → `Work of the US Gov. Public Use Permitted.`
- PDF `https://ntrs.nasa.gov/api/citations/19900017394/downloads/19900017394.pdf` HTTP **200** `application/pdf` 3,958,866 bytes.
- In-PDF title pages: `NASA SP-7084` / `Grammar, Punctuation, and Capitalization` / `A Handbook for Technical Writers and Editors` / `Mary K. McCaskill` / `Langley Research Center` / `1990`. No `Copyright` / `All rights` in the text layer (scan quality is poor: `GraIllIllar`).
- Everyspec index (mirror, not canonical) lists **03 AUG 1998** rev, 420.07 KB, status Active — still the Phase 6 edition fork.

**Decision:** **Tier 1 RECONFIRMED**. Not a new exclusion. Not a v1.18 pack (cluster 25 filled). SEED-001 still lists it for Training **diversity** (2 packs). Phase 10 should date-stamp the reconfirm; Phase 11 may skip the pack without failing IO-01..07.

**Confidence:** HIGH.

---

### 6. AAF Product Support + Software pathway (VET-19-03)

**Governing published sentence:** DAG Excluded row: `AAF guidebooks are the intended substitute but are NOT yet vetted — licence spot-check deferred (not a v1.18 build item); vet before any future use`. [VERIFIED: `docs/SOURCE-VETTING.md:85`]

**This session:**

- Live `https://aaf.dau.edu/guidebooks/` → **403** Cloudflare `Just a moment...` (not a licence page).
- Wayback `20221013134401id_` HTML **200**. Verbatim DAG line still present: `The Defense Acquisition Guidebook has been retired and replaced by a modern set of guidebooks aligned with our new acquisition policies.` Footer verbatim: `Copyright © 2022 Adaptive Acquisition Framework - Defense Acquisition University`.
- 2022 index mapped **Sustainment → Product Support Manager Guidebook** to `https://www.dau.edu/pdfviewer?Guidebooks/Product-Support-Manager-(PSM)-Guidebook.pdf` and a tools suite URL. Software Acquisition was a **pathway** (`/aaf/software/`), not a single "Software pathway guidebook" PDF on that index. Adjacent "IT & Business Systems" pointed at a DoD CIO *Digital Capabilities* guidebook (different document).
- Those `dau.edu` PDF/tool URLs now **301 to `www.waru.edu` and 404**.
- `www.waru.edu` home HTTP **200**, official US .gov banner. AAF is listed as a knowledge asset. `/aaf/about/resources` describes **courses, credentials, workshops, tools** — not a downloadable Product Support / Software guidebook with a licence block. No copyright sentence on the homepage text extract.
- DoD CIO Digital Capabilities PDF (2022 AAF-adjacent link) → 403 this session.

**Licence pattern:** A DAU/WarU compiled guidebook **might** be a US-gov work, but the 2022 site footer is an explicit **Copyright ©** line. That is the opposite of an in-source public-domain dedication. Until the **guidebook PDF itself** is opened and quoted, statute-heuristic Tier 1 is forbidden. This is why Phase 6 deferred.

**Decision:** **Keep Excluded-pending / "NOT yet vetted — do not use".** Do not build. IO-05 / IO-06 record deferred. Optional VET-19-04 row naming the two guidebook families (no URLs) so Phase 11 cannot "discover" them.

**Confidence:** HIGH that they are not cleared. LOW on the eventual in-PDF grant (could still be DIST-A / public domain once a PDF is found).

---

### Public-domain / US-gov patterns (how to read these families)

| Family | Typical in-source grant this repo accepts | Observed this session | Failure mode |
|--------|------------------------------------------|----------------------|--------------|
| NASA STD / SP | NTSS "Internet Public"; NTRS "Work of the US Gov. Public Use Permitted." | Both seen (8719.14C, SP-7084) | Placeholder PDF (HDBK-2203) |
| DoD Manual / MIL-STD | DIST-A or "no releasability restrictions" | Not seen (host 403) | Unreachable ≠ DIST-A |
| GPS IS/ICD | DIST-A on cover; "approved for public release" on gps.gov | DIST-A on IS-GPS-200N / 705J | Request-only ICDs (153); contractor name on cover |
| Army ASAFM | Expected US-gov work | **No PDF** | Akamai 403 |
| AAF / DAU / WarU | Need per-guidebook statement | Site © 2022 DAU; PDFs missing | Copyright footer + host churn |
</candidate_findings>

<validation_architecture>
## Validation Architecture (Nyquist — how a planner knows vetting is done)

Phase 10 has no runtime, no tests, and no pack gate. "Done" is a **closed decision set** plus Link Policy. Success is **not** "we found PDFs for everything."

### Signals that must be true after execute

| Signal | How to measure | Pass |
|--------|----------------|------|
| VET-19-01 decided | REQUIREMENTS annotation + SOURCE-VETTING / STATE sentence with **2026-08-17** (or execute-day) evidence | Army CBA is Tier 1 **with in-source quote**, or **deferred/excluded** with 403/503 evidence. Not silent. |
| VET-19-02 decided | Four named sources each have a dated Tier 1 / 2 / Excluded / deferred-excluded rationale | 8719.14 + IS-GPS-200N + SP-7084 may be Vetted; DoDM must not be unmarked |
| VET-19-03 decided | AAF sentence still contains **NOT yet vetted** / Excluded-pending **or** a new Tier 1/2 row with an in-source quote | Default: keep unused |
| VET-19-04 | Any **ruled-out** source is in the Excluded table; deferrals are labelled as such | No URL in the table |
| Link Policy | `grep -c http docs/SOURCE-VETTING.md` | `0` |
| No pack creep | `git diff --name-only` has no `packs/` | true |
| Phase 11 can consume | A table in SOURCE-VETTING or STATE lists cleared vs deferred vs excluded | Three GO / three NO-GO as in this RESEARCH unless execute found new PDFs |

### What is *not* a completion signal

- `vet_source.py` exit 0 on a guessed title (publisher heuristic ≠ in-source).
- Wayback CDX `200 application/pdf` without opening the bytes.
- Cluster-need pressure from SEED-001.

### Residual risk after a correct Phase 10

Phase 11 build-time still owes visual/text confirmation on 8719.14C (third-party inserts) and IS-GPS-200N (SAIC contractor line + DIST-A remains on the copy actually extracted). That is the Phase 3/7 P7-PRE pattern, not a reason to withhold the Tier 1 *leaning* decision.
</validation_architecture>

<open_questions>
## Open Questions

1. **Can a human browser open asafm.army.mil or esd.whs.mil?**
   - What we know: automated clients get 403; Phase 6 retrieved DAFMAN via "rendered fetch" despite curl 403.
   - What's unclear: whether execute-with-browser would clear Army CBA / DoDM.
   - Recommendation: planner may add an optional "browser-UA / interactive fetch" task. If it fails, keep deferral. Do not block the phase on it. Do not call a 403 host Tier 1 because DAFMAN once worked.

2. **Where did the Product Support Manager Guidebook move after WarU?**
   - What we know: 2022 path 404s; WarU AAF resources page is training-centric.
   - What's unclear: current filename / tools-catalog slug.
   - Recommendation: do not hunt indefinitely in Phase 10. Excluded-pending is the honest close.

3. **Is the AAF site copyright a claim on the guidebooks?**
   - What we know: footer `Copyright © 2022 Adaptive Acquisition Framework - Defense Acquisition University`.
   - What's unclear: whether that attaches to compiled HTML, to guidebook PDFs, or is leftover theme text.
   - Recommendation: irrelevant until a PDF is in hand. Treat as a **reason not to assume Tier 1**, not as a final Excluded hard-stop (unless the planner wants a hard-stop).

4. **Should VET-19-01 be checkable if the only outcome is deferral?**
   - What we know: wording is "build-or-exclude with in-source licence evidence"; ROADMAP allows deferral.
   - Recommendation: planner writes VET-19-01 acceptance as "retry recorded; not cleared; FUT-04 remains" so verify does not demand a pack or an Excluded row.
</open_questions>

<recommended_plan_shape>
## Recommended plan shape (do NOT write PLAN.md here)

One documentation plan (Phase 6 `6-01` analogue). Wave 1 only. No pack plans.

**Plan 10-01 — Record v1.19 verdicts (docs/planning only)**

1. Insert `### Vetted candidates (v1.19.0)` after the v1.18 section. Pointer to `10-RESEARCH.md` as the URL store. Rows:
   - NASA-STD-8719.14C — Tier 1, Internet Public quote, 77 pp, build-time third-party scan.
   - GPS IS-GPS-200N (select; **not** IS-300) — Tier 1, DIST-A quote, SAIC contractor watch-item.
   - NASA SP-7084 — Tier 1 reconfirm (or a one-line "reconfirmed 2026-08-17" under the existing v1.18 row if the planner wants less duplication).
2. FUT-04: do **not** add a Tier 1 row. Annotate REQUIREMENTS VET-19-01 + STATE + the GP-06 dual-source sentence so it no longer implies Army CBA is still a pending dual-source half of a live pack. Fresh 403/503 evidence dated.
3. DoDM 5000.102: dated **UNVERIFIED / deferred-excluded** (Def Stan 00-051 pattern or a short "v1.19 pending" subsection). Not Tier 1.
4. AAF: keep or strengthen **"NOT yet vetted — do not use"**. Optional VET-19-04 Excluded-pending row for Product Support Manager Guidebook + Software pathway (copyright-footer + no PDF). Do not mention URLs.
5. Consistency sweep: `http` = 0; no `packs/` edits; Phase 11 handoff table (GO: 8719.14C, IS-GPS-200N, SP-7084 optional; NO-GO: Army CBA, DoDM 5000.102, AAF).

**Out of this plan:** extract.py, outline, build_pack, catalog, capability map, HYG-03 vet_source sync, IO-01 remaps.

**If execute later opens a blocked PDF:** amend RESEARCH + flip that one row. Do not pre-write pack tasks.
</recommended_plan_shape>

<project_constraints>
## Project Constraints (no CLAUDE.md / AGENTS.md in repo)

From `PROJECT.md` / `docs/SOURCE-VETTING.md`:

- Pack content licences are inherited from sources (Tier 1 public domain → Tier 3 excluded); **vetting is a hard stop, not advisory**. [VERIFIED: `.planning/PROJECT.md:29`]
- Packs stay plain Markdown, progressive-disclosure.
- CI `content-integrity` / `check_release.py` must pass for release commits — Phase 10 should not touch pack trees, so the gate should stay green.
- "Free to download" is not "free to redistribute." [VERIFIED: `docs/SOURCE-VETTING.md:15`]
</project_constraints>

<sources>
## Sources

### Primary (HIGH confidence)

- `docs/SOURCE-VETTING.md` — tiers, Excluded columns (`Source` / `Why excluded`), Link Policy, v1.18 rows, AAF "NOT yet vetted" sentence
- `docs/LICENSING.md` §4 — no source-material URLs
- `.planning/REQUIREMENTS.md`, `STATE.md`, `ROADMAP.md`, `MILESTONES.md`, `seeds/SEED-001-agent-io-pack-depth.md`
- `.planning/phases/6-source-vetting-unverified-resolution/6-RESEARCH.md`, `6-01-PLAN.md`, `6-REVIEW-FIX.md`, `6-VERIFICATION.md`
- `packs/federal-bca/PACK.yaml`, `packs/dod-vva-rpg/PACK.yaml`
- `C:/Users/gower/OneDrive/Documents/GitHub/jgs-reference-skill/tools/vet_source.py`
- Live fetches 2026-08-17: NTSS 8719.14 page + PDF; NTRS 19900017394 page + PDF; gps.gov ICD page + IS-GPS-200N / 705J PDFs; asafm/esd/aaf HTTP codes; Wayback CDX + one AAF HTML capture; waru.edu home + AAF resources

### Secondary (MEDIUM confidence)

- `.planning/research/capability-gap-report.md` — candidate URLs and original Tier-1 heuristic (several hosts now 403)
- `.planning/v1.18.0-MILESTONE-AUDIT.md` — FUT-04 / AAF backlog
- 17 U.S.C. § 105 official text [CITED: https://www.copyright.gov/title17/92chap1.html#105]

### Tertiary (LOW confidence — needs validation)

- Guessed `media.defense.gov` DoDM object path (403; not confirmed as the real file)
- Whether a rendered browser session would defeat WHS/ASAFM Akamai
- Whether WarU tools catalog hides a current PSM PDF under a new slug
</sources>

<metadata>
## Metadata

**Research scope:**
- Core technology: licence vetting / 17 U.S.C. § 105 / DIST-A / NTSS Internet Public
- Ecosystem: NASA NTSS, NTRS, GPS.gov, ASAFM, WHS issuances, AAF/DAU/WarU
- Patterns: Phase 6 register write-up; honest deferral; Link Policy
- Pitfalls: AAF-before-clearance; unreachable-as-Tier-1; IS-300 misnomer; URL leak

**Confidence breakdown:**
- Standard stack: HIGH — read SOURCE-VETTING, LICENSING, Phase 6 plan, vet_source.py
- Architecture: HIGH — same as Phase 6
- Candidate reachability: HIGH for 8719.14C, SP-7084, IS-GPS-200N, AAF/Army/DoDM failures
- In-source licence for blocked PDFs: LOW — not obtained
- Code examples: HIGH — process snippets from this repo

**Research date:** 2026-08-17
**Valid until:** 2026-09-16 (30 days — host/WAF rules move; GPS/NASA editions move slower)
</metadata>

---

*Phase: 10-source-vetting*
*Research completed: 2026-08-17*
*Ready for planning: yes*
