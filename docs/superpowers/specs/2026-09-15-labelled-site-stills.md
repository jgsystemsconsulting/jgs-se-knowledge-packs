# Spec: Labelled site stills (P11)

- Date: 2026-09-15
- Package: P11, visual website cut
- Status: ready for implementation
- Owner: jgs-se-knowledge-packs maintainers

## Problem

Below the landing hero, `docs/index.html` is text and code only. Section §03
(Using a pack) is a `<pre>` block; §06 (The catalogue) is text chips. User intent
asked for labelled site stills; none exist as published page-body assets under
`docs/assets/` (P9 only shipped the OG share card).

## Evidence

- `docs/index.html` §03: pre/code only (invoke examples).
- `docs/index.html` §06: pack chips grid, text only.
- P9 shipped `docs/assets/og-default.png` and absolute OG meta; body stills are out of P9 scope.
- P10 (landing hero still) is not done on this branch: hero remains label + h1 + lede + CTAs. P11 must not claim the hero and must not conflict with a later hero figure.
- Brand tokens live between `/* BRAND-TOKENS:BEGIN` and `/* BRAND-TOKENS:END` in `docs/index.html`; P13 owns that contract.
- P12 `[html-assets]` requires relative self-hosted body images under `docs/assets/` (no CDN).

## Goal

Ship 1-2 labelled self-hosted stills on `docs/index.html` body sections (§03
and/or §06), captioned in drafting-sheet voice, with assets under `docs/assets/`,
no CDN, no OG meta changes, no `packs.html` chrome redesign, and brand-token
markers preserved. Keep gates green.

## Non-goals

- Landing hero still or hero layout (P10).
- OG/Twitter meta (P9 already shipped).
- Hand-editing or redesigning `docs/packs.html` chrome (RR-B-00).
- Publishing `.playwright-mcp` dumps or `sources/*/covers` as marketing art.
- Screenshot automation / visual-regression CI.
- CDN or third-party hosts.
- Changing brand token values or markers.
- Product YAML / pack Markdown content.

## Requirements

1. Two self-hosted stills under `docs/assets/`:
   - `still-using-a-pack.png` (and optional matching SVG): §03 invoke moment
   - `still-catalogue.png` (and optional matching SVG): §06 catalogue / pack-reference surface
2. Wire both into `docs/index.html` body only (§03 after the pre block or beside the progressive-disclosure note; §06 after the chips grid or before the packs.html link paragraph). Use `<figure class="still">` with `<img>` (relative `assets/...`) and `<figcaption>` in drafting-sheet voice.
3. Meaningful `alt` text on each image. `prefers-reduced-motion` already neutralizes animation site-wide; no new motion required.
4. Tight figure + label CSS only (inline in index). Match dark drafting tokens already on the page. Do not touch the BRAND-TOKENS block contents.
5. No CDN. Relative paths only for body images so `[html-assets]` stays clean.
6. Do not modify OG/Twitter meta. Do not redesign packs.html.
7. If a hero still lands from P10 later, body figures remain independent (class `still`, not `hero`).
8. Gates pass: `python tooling/test_html_assets.py`, `python tooling/test_ci_gate.py`, `python tooling/check_release.py`.

## Design

**Design read:** public SE knowledge-pack landing for engineers, dark drafting-document language already on the page; preserve existing system; dials variance 4 / motion 2 / density 5.

### Still A: §03 Using a pack

Composition (Pillow or SVG source, committed PNG):

- Ink ground `#0a0a0b`, thin frame `#2a2d33`, paper left spine `#f4f2ec`
- Mast strip: `DOC-ID  JGS-SE-KP/STILL-03` and `PUBLIC`
- Title line: `§03 · Using a pack`
- Fake terminal panel showing slash-invoke lines matching the live pre block tone:
  `/sebok systems of systems` and `/nasa-se-handbook ch06`
- Footer label: `INVOKE · PROGRESSIVE DISCLOSURE`

Target size ~1200x675 (16:9) or 1200x630; either is fine for page body.

### Still B: §06 The catalogue

- Same drafting frame language
- Mast: `DOC-ID  JGS-SE-KP/STILL-06`
- Title: `§06 · The catalogue`
- Simplified chip/table mock: family rows (NASA, DoD, NIST, FAA, GAO) with counts, not a live packs.html screenshot
- Footer: `54 PACKS · 2 SIGNPOSTS · FILTER ON packs.html`

### HTML / CSS

```html
<figure class="still">
  <img src="assets/still-using-a-pack.png" width="1200" height="675"
       alt="Drafting-sheet still: slash-invoke a pack topic so the agent loads one chapter.">
  <figcaption>FIG.03 · Slash-invoke a topic; the pack index routes one chapter into context.</figcaption>
</figure>
```

CSS sketch (outside brand-token markers):

```css
.still{margin:1.6rem 0 0;border:1px solid var(--line);background:var(--ink-2);padding:0}
.still img{display:block;width:100%;height:auto;border-bottom:1px solid var(--line)}
.still figcaption{font-family:var(--mono);font-size:0.75rem;letter-spacing:0.06em;
  text-transform:uppercase;color:var(--mute);padding:12px 16px}
```

Captions stay short, mono, uppercase drafting voice. No stock photography language.

## Acceptance

- Both PNGs exist under `docs/assets/` and are referenced relatively from index body.
- Index body shows two labelled figures in §03 and §06.
- Hero markup unchanged (P10 untouched).
- No new absolute third-party asset URLs; OG meta unchanged.
- `BRAND-TOKENS:BEGIN` / `END` markers still present with same token set.
- Gate trio green.

## Research

research: skipped (in-repo static stills and HTML wiring; no external API or library choice beyond local Pillow already used for P9)
