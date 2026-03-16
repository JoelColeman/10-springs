# Implementation Plan — Timeline Changes

**Only file touched:** `index.html`

---

## Change 1 — Move timeline after Heritage Pieces

**Current state:**
The `<div class="tl">` is `position: fixed; top: 0; z-index: 150` — it is always pinned to the top of the viewport regardless of scroll position. It lives in the DOM before the API key modal. `body` has `padding-top: 130px` to compensate, and JS toggles that padding between 130 px (tall) and 64 px (compact) on scroll.

**Proposed change:**
1. Remove the `<div class="tl">` from its current location (before the modal).
2. Re-insert it in the document flow directly after `</div>` that closes `.heritage-wrap` and before the `.accord` accordion element.
3. Change the CSS to `position: sticky; top: 0` (removing `position: fixed; z-index: 150; height: 120px`). A sticky element sits in flow until its containing scroll context scrolls it to `top: 0`, at which point it sticks — exactly the right behaviour here: the user sees heritage first, then the timeline snaps to the top as they scroll into the main watch list.
4. Remove `body { padding-top: 130px }` and the JS lines that toggle it between 130 px and 64 px (those were workarounds for `fixed` positioning).
5. Keep the compact scroll logic, but update the trigger: instead of `scrollY > 80`, observe an element that is above the timeline in the DOM (e.g. a sentinel `<div>` at the top of `.heritage-wrap`) using IntersectionObserver — when the sentinel leaves the viewport, add `.compact`; when it re-enters, remove it.

**Tradeoff:**
`sticky` requires the timeline to be inside a scroll container that is tall enough to scroll. Since `.db` contains everything, this works out of the box. One edge case: if a user's browser has `position: sticky` quirks inside a flex/grid parent, we may need to set `align-self: flex-start` on `.db` or wrap the timeline differently. This is unlikely with the current markup but worth a quick check.

---

## Change 2 — Heritage watches leftmost

**Current state:**
H1 and H2 are the rightmost slots, separated from the main sequence by a `.tl-heritage-sep` spacer.

**Proposed change:**
1. Move the heritage `.tl-era-group` and its separator to the **left** end of `.tl-track` — it becomes the first group.
2. Move the `tl-heritage-sep` so it sits between the heritage group and the first main-sequence group (DRESS), giving a small visual gap that says "these are different in kind."
3. Keep `ring-heritage` (1 px solid rgba(0,0,0,.1)) as the border style — already faint.
4. Add `opacity: 0.65` to `.tl-era-group[data-era="heritage"]` to visually step it back relative to the purchased/planned watches. This makes the inherited watches legible but subordinate.
5. The heritage era label text changes to **HERITAGE** (already correct). No IntersectionObserver needed for heritage since there is no `#sec-heritage` page section — leave observer as-is.

**Tradeoff:**
Opacity 0.65 is a soft approach. A dashed ring is also an option, but `ring-heritage` already has a very faint solid ring; making it dashed as well might look noisy. Opacity is cleaner and communicates "not purchased" clearly.

---

## Change 3 — Bracket labels based on watch character

**Proposed 5 brackets** (keeping slots in chronological age order H1/H2, then ages 35–45):

| Bracket | Slots | Watches | Rationale |
|---|---|---|---|
| **HERITAGE** | H1, H2 | Caravelle manual wind · Bulova Accutron Spaceview | Inherited heirlooms; set the emotional baseline |
| **DRESS** | NOW, S2, S5 | Longines Sport Chief 7042 · Longines Flagship 18k 3410 · Rolex Datejust 1601 | All share a formal/dressy character — the wearable everyday and occasion watches |
| **FIELD** | S1, S3, S4, S6 | Omega Seamaster 166.010 · UG Polerouter · Zenith El Primero A386 · Omega Speedmaster 3570.50 | Golden-age Swiss instrument and tool watches — worn by scientists, pilots, and collectors |
| **SPORT** | S7 | TBD modern sport (Hulk Sub, Batman/Root Beer GMT, or Seamaster 300M) | The one modern sport anchor; "DIVE" is a more precise label if the Hulk Sub wins |
| **GRAIL** | S8, S9, S10 | JLC Master Ultra Thin Moon · Rolex Day-Date · Rolex GMT-Master 1675 Pepsi | All declared aspirational top-tier pieces; $7 K–$18 K; the collection's endgame |

**Why 5 not 6:**
The actual watch list has only one slot (S7) that is naturally DIVE/SPORT, and only one GMT watch (S10, which the collector already calls the "Grail"). Forcing both DIVE and GMT as separate brackets would give each just one slot — that's visually thin and doesn't add information. Grouping them makes the brackets feel balanced: 2 / 3 / 4 / 1 / 3.

**If you want exactly 6:**
The cleanest split would be to break FIELD into **INSTRUMENT** (S1, S3 — vintage automatic instrument watches) and **CHRONO** (S4, S6 — vintage chronographs: El Primero and Speedmaster). That gives: HERITAGE · DRESS · INSTRUMENT · CHRONO · SPORT · GRAIL.

**Slot order in the HTML** (chronological, heritage first):
H1, H2 → NOW, S2, S5 → S1, S3, S4, S6 → S7 → S8, S9, S10
*(within each bracket, slots remain in ascending age/purchase order)*

**Note on current order disruption:**
The new bracket order means the slots no longer appear as NOW, S1, S2, … S10 left-to-right. Instead they are grouped by character. This is intentional — the brackets become the primary narrative, and age/purchase sequence is captured by the "Age XX" sub-label on each thumb.

**Changes needed in HTML:**
- Reorder the `.tl-era-group` divs and their contained `.tl-slot` divs
- Update `data-era` attributes on each group
- Update the `tl-era-lbl` text
- Update IntersectionObserver's `sections` array to map the new era names to the correct `#sec-*` page section IDs
  - `#sec-foundation` → `dress`
  - `#sec-collector` → `field`
  - `#sec-rolex` → maps to multiple brackets now; use the first slot of SPORT (S7) as the anchor → observe `#sec-rolex` for `sport`
  - `#sec-grails` → `grail`
  - No observer for heritage (no page section)

---

## Change 4 — Responsive fluid scaling

**Current state:**
`--tl-slot: 56px` is fixed. All era groups have `flex-shrink: 0`. The track uses `overflow-x: auto` so it scrolls on narrow viewports instead of shrinking.

**Proposed change:**
Remove the fixed `--tl-slot` width and switch to proportional flex layout:

1. **Era groups** get `flex: <slot-count>` so their widths are always proportional to the number of slots they contain (HERITAGE: 2, DRESS: 3, FIELD: 4, SPORT: 1, GRAIL: 3 = 13 total).
2. **Each slot** gets `flex: 1; min-width: 0` so slots expand equally within their era group. The math works out: every slot gets exactly 1/13 of the available track width.
3. **Thumbnails** scale via `width: clamp(20px, 3.5vw, 44px); height: clamp(20px, 3.5vw, 44px)`. At 1260 px viewport: 3.5vw = 44 px (cap). At 768 px: 3.5vw = 27 px. At 375 px: 3.5vw = 13 px → 20 px floor. This keeps the circle visible at all reasonable viewports without horizontal scroll.
4. **Heritage separator** changes from `width: 16px; flex-shrink: 0` to `flex: 0 0 clamp(6px, 1.2vw, 16px)` so it scales with the viewport.
5. **Remove** `overflow-x: auto` from `.tl-track` since the content now always fills the viewport. Keep it only below 360 px as a last-resort fallback.
6. **Compact connecting line position** (`top:` value in `.tl-track::before`) stays the same in px since it depends on the era-header height and thumb height (which change discretely in compact mode, not continuously). The compact transition will still look correct; only the horizontal extent of the line will now fill 100% of the viewport.

**Tradeoff:**
At very small viewports (< 360 px), 1/13 of the available width (~24 px per slot) may make thumbnails and labels illegible. A `min-width` floor on each slot and the `overflow-x: auto` fallback handles this gracefully without breaking wider viewports.

---

## Summary of edits

| Edit | What changes |
|---|---|
| CSS `.tl` | `position: sticky; top: 0` · remove `z-index: 150` · remove `height` transition (height stays 120 px by default; compact shrinks it) |
| CSS `.tl-track` | Remove `overflow-x: auto` · remove fixed `--tl-slot` |
| CSS `.tl-era-group` | Add `flex: var(--tl-era-flex)` (set inline) or explicit per-group rules |
| CSS `.tl-slot` | `flex: 1; min-width: 0` (remove fixed width) |
| CSS `.tl-thumb` | `width: clamp(20px, 3.5vw, 44px); height: clamp(20px, 3.5vw, 44px)` |
| CSS `.tl-heritage-sep` | `flex: 0 0 clamp(6px, 1.2vw, 16px)` |
| CSS `body` | Remove `padding-top: 130px` |
| HTML `<div class="tl">` | Remove from before modal; re-insert after `</div><!--/.heritage-wrap-->` |
| HTML era groups | Reorder: HERITAGE → DRESS → FIELD → SPORT → GRAIL · update labels + data-era |
| HTML slot order | H1, H2, NOW, S2, S5, S1, S3, S4, S6, S7, S8, S9, S10 (within respective era groups) |
| JS compact trigger | Replace `scrollY > 80` with IntersectionObserver on a sentinel above the timeline |
| JS IntersectionObserver (era) | Update section→era mapping for new bracket names |
| JS `body.style.paddingTop` toggle | Remove entirely |
