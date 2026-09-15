# Spec: Landing hero still (P10)

- Date: 2026-09-15
- Package: P10, visual website cut
- Status: ready for implementation
- Owner: jgs-se-knowledge-packs maintainers

## Problem

The landing hero on `docs/index.html` is typography and CTAs only (label, h1, lede,
two buttons). There is no figure, still, or brand mark beyond a data-URI favicon.
First paint reads as a long drafting memo rather than a product surface, and under-uses
the dark drafting-document system the page already claims. P9 landed a self-hosted OG
card under `docs/assets/`; the on-page hero still has no equivalent body still.

## Evidence

- `docs/index.html` hero markup: text + CTA only.
- `docs/index.html` hero CSS: text layout only.
- Favicon is data-URI SVG only; body has no self-hosted figure.
- P9 assets: `docs/assets/og-default.png` (+ optional SVG) already establish the brand kit.

## Goal

Ship one primary self-hosted hero brand still on `docs/index.html` only, with meaningful
alt text, `prefers-reduced-motion` safety, minimal inline CSS, dark drafting taste
(ink `#0a0a0b`, paper `#f4f2ec`), and green gates:
`python tooling/test_html_assets.py`, `python tooling/test_ci_gate.py`,
`python tooling/check_release.py`.

## Non-goals

- OG/Twitter meta changes (P9 done).
- `docs/packs.html` body redesign (RR-B-00; packs polish is P14).
- Labelled body stills below the hero (P11).
- CDN or third-party image hosts.
- Brand token redesign; preserve `BRAND-TOKENS:BEGIN` / `END` markers.
- Light theme, §01-§07 copy rewrite, install.py / pack Markdown, P8.

## Requirements

1. Self-hosted hero still under `docs/assets/` (PNG and/or SVG). Dark drafting brand:
   ink ground, paper accent, drafting frame / sheet labels, `§` mark language matching
   the OG card aesthetic. PNG is the page `<img>` target.
2. Wire one primary figure into the `docs/index.html` hero only. Relative `src` under
   `assets/` (self-host convention from P12).
3. Meaningful `alt` text describing the brand still (not empty, not filename-only).
4. Minimal inline CSS for hero media composition (no framework, no CDN). No animation
   that fights `prefers-reduced-motion`; existing reduce rule stays intact.
5. Do not change OG/Twitter meta. Do not redesign packs.html body. Do not break
   BRAND-TOKENS markers.
6. Gates pass: `test_html_assets.py`, `test_ci_gate.py`, `check_release.py`.

## Design

### Asset

Create `docs/assets/hero-still.png` (wide brand still, e.g. 1600x720) with a local
one-shot (Pillow). Optional companion `hero-still.svg` for editability. Composition:
ink background, thin drafting frame, paper left spine, large `§`, title
"SE Knowledge Packs", short subtitle, labelled sheet callout panel, footer path strip.
Same token palette as OG (`#0a0a0b`, `#f4f2ec`, mute/line greys).

### Hero composition

Two-column hero on wide viewports: copy (label, h1, lede, CTAs) + figure. Stack on
narrow viewports with the still above or below copy as a single column. Figure uses
bordered drafting chrome already present on the page (line, ink-2). Image is static;
no CSS animation required. Existing
`@media (prefers-reduced-motion:reduce)` keeps any future transitions inert.

### Gate posture

P12 `[html-assets]` already allows relative `assets/` image paths and fails closed on
remote hosts. No new scanner. Relative `src="assets/hero-still.png"` must scan clean.

## Acceptance criteria

1. `docs/assets/hero-still.png` is tracked (optional SVG companion allowed).
2. `docs/index.html` hero contains one primary `<img>` pointing at the self-hosted still
   with meaningful alt text.
3. Hero media CSS is minimal, inline, and stacks cleanly at the existing 860px breakpoint.
4. `prefers-reduced-motion: reduce` rule remains present; no new motion that ignores it.
5. OG/Twitter meta block unchanged from P9.
6. `docs/packs.html` body not redesigned for this package.
7. `BRAND-TOKENS:BEGIN` / `END` markers intact in `docs/index.html`.
8. `python tooling/test_html_assets.py` exits 0.
9. `python tooling/test_ci_gate.py` exits 0.
10. `python tooling/check_release.py` exits 0 (PASS).

## Risks

| Risk | Mitigation |
|------|------------|
| Absolute remote img host trips `[html-assets]` | Relative `assets/` path only |
| BRAND-TOKENS broken while editing hero CSS | Edit outside the marker block |
| Accidental packs.html body edit | Out of scope; do not touch packs body |
| Decorative image with empty alt | Require descriptive alt on the figure |
| Motion-heavy treatment | Static still; keep reduce rule |

## Research

research: skipped (in-repo static hero still and HTML wire-up; reuses P9 brand kit and P12 self-host convention; no external API)
