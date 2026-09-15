# Labelled Site Stills (P11) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add two labelled self-hosted stills under `docs/assets/`, wire them into `docs/index.html` body sections §03 and §06 with drafting-sheet captions, leave hero and OG meta alone, preserve BRAND-TOKENS, and keep html-assets / CI / release gates green.

**Architecture:** PNG stills match the P9 dark drafting kit (ink ground, paper spine, mono labels). Body uses relative `assets/` paths. CSS class `still` is separate from any future hero media. Packs.html is not touched.

**Tech Stack:** Python 3 + Pillow (local generation only; PNGs committed), plain HTML/CSS in `docs/index.html`. No CDN. No new repo runtime dependency.

**Spec:** docs/superpowers/specs/2026-09-15-labelled-site-stills.md

**Research:** research: skipped (in-repo static stills and HTML wiring; no external API)

## Global Constraints

- No CDN. Self-hosted assets under `docs/assets/` only; body `img src` relative.
- Do not change OG/Twitter meta (P9).
- Do not touch hero markup or claim hero layout (P10 may land later).
- Do not hand-edit or redesign `docs/packs.html`.
- Preserve `/* BRAND-TOKENS:BEGIN` / `/* BRAND-TOKENS:END` markers and token contents.
- Captions: drafting-sheet voice (mono, short, FIG.xx labels).
- Gates: `python tooling/test_html_assets.py`, `python tooling/test_ci_gate.py`, `python tooling/check_release.py`.
- Em-dash-free durable prose (RR-B-28).

## Codebase context

- `docs/index.html` hero is text-only today (P10 not done).
- §03 ends with a pre block + progressive-disclosure paragraph.
- §06 has packs chips + packs.html link paragraph.
- `docs/assets/og-default.png` already exists from P9.
- P12 `[html-assets]` allows relative `assets/...` body images.

---

### Task 1: Generate branded still PNGs (and optional SVGs)

**Files:**
- Create: `docs/assets/still-using-a-pack.png`
- Create: `docs/assets/still-catalogue.png`
- Create (optional): matching `.svg` companions

**Model:** standard

- [ ] **Step 1: Ensure assets dir**

```bash
mkdir -p docs/assets
```

- [ ] **Step 2: Generate still-using-a-pack.png**

Pillow one-shot, ~1200x675 RGB:

- ink `#0a0a0b` ground, frame `#2a2d33`, paper spine `#f4f2ec`
- mast `DOC-ID  JGS-SE-KP/STILL-03` / `PUBLIC`
- title `§03 · Using a pack`
- terminal panel with invoke lines:
  - `/sebok systems of systems`
  - `/nasa-se-handbook ch06`
- footer `INVOKE · PROGRESSIVE DISCLOSURE`

- [ ] **Step 3: Generate still-catalogue.png**

Same kit, mast `STILL-06`, title `§06 · The catalogue`, family chip rows with counts (NASA 15, DoD 13, NIST 9, FAA 6, GAO 4), footer `54 PACKS · 2 SIGNPOSTS · FILTER ON packs.html`.

- [ ] **Step 4: Verify files open**

```bash
python -c "from PIL import Image; 
for p in ('docs/assets/still-using-a-pack.png','docs/assets/still-catalogue.png'):
 im=Image.open(p); print(p, im.size, im.mode); assert im.size[0]>=1000"
```

Optional: write matching SVGs for editability (meta/pages do not require them).

---

### Task 2: Wire figures + CSS on docs/index.html body

**Files:**
- Modify: `docs/index.html` (style block outside BRAND-TOKENS; §03 and §06 body only)

**Model:** flash

- [ ] **Step 1: Add `.still` CSS after existing section styles (after packs rules, before sheet or media queries)**

```css
/* Labelled body stills (P11) */
.still{margin:1.6rem 0 0;border:1px solid var(--line);background:var(--ink-2);padding:0}
.still img{display:block;width:100%;height:auto;border-bottom:1px solid var(--line)}
.still figcaption{font-family:var(--mono);font-size:0.75rem;letter-spacing:0.06em;text-transform:uppercase;color:var(--mute);padding:12px 16px;margin:0}
```

Do not insert inside BRAND-TOKENS markers.

- [ ] **Step 2: Insert figure in §03 after the `<pre>` block (before the progressive-disclosure paragraph)**

```html
  <figure class="still">
    <img src="assets/still-using-a-pack.png" width="1200" height="675"
         alt="Drafting-sheet still of slash-invoking a pack topic so the agent loads one chapter.">
    <figcaption>FIG.03 · Slash-invoke a topic; the pack index routes one chapter into context.</figcaption>
  </figure>
```

- [ ] **Step 3: Insert figure in §06 after the packs chips grid (before the browse paragraph)**

```html
  <figure class="still">
    <img src="assets/still-catalogue.png" width="1200" height="675"
         alt="Drafting-sheet still of the catalogue families and pack counts.">
    <figcaption>FIG.06 · Fifty-four packs across open sources; filter the full list on packs.html.</figcaption>
  </figure>
```

- [ ] **Step 4: Confirm hero and OG untouched; brand markers intact**

```bash
rg -n "BRAND-TOKENS|og:image|class=\"hero\"|class=\"still\"|still-using|still-catalogue" docs/index.html
```

Hero block must still be text+CTA only. OG meta lines unchanged.

---

### Task 3: Mark P11 done and run gates

**Files:**
- Modify: `docs/superpowers/packages/2026-09-15-jgs-se-knowledge-packs-packages.md` (P11 status → done)

**Model:** flash

- [ ] **Step 1: Set P11 status to done**

In the packages document, change P11 `- **status**: ready` to `- **status**: done`.

- [ ] **Step 2: Run gates**

```bash
python tooling/test_html_assets.py
python tooling/test_ci_gate.py
python tooling/check_release.py
```

All must exit 0 / PASS.

- [ ] **Step 3: Commit in logical slices**

1. assets (stills)
2. index.html wire
3. packages status + superpowers closeout docs

Use HEREDOC commit messages. Do not push unless asked.

---

## Acceptance checklist

- [ ] Two PNGs under `docs/assets/`
- [ ] Two `<figure class="still">` on index body (§03, §06)
- [ ] Relative img paths; no CDN
- [ ] Hero unchanged; OG meta unchanged; BRAND-TOKENS intact
- [ ] packs.html not redesigned
- [ ] P11 status done
- [ ] Gate trio green
