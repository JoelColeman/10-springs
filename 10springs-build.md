DASHBOARD BUILD CONTEXT (10springs-build.md)
════════════════════════════════════════════
# 10 Springs — Dashboard Build Reference
*For Claude Code agents and dashboard build sessions*
*Last updated: April 1, 2026*

---

## Project Overview

**10 Springs** — a 10-watch mechanical watch collection dashboard.
**Live at:** joelcoleman.github.io/10-springs
**Repo:** github.com/JoelColeman/10-springs
**Stack:** Single-file index.html · Vanilla HTML/CSS/JS · GitHub Pages hosting

Claude Code handles all building and commits. Strategic conversations are handled separately and produce updated versions of this document.

---

## Repo Structure

- `index.html` — the live dashboard (single file, all HTML/CSS/JS)
- `10springs-build.md` — this document
- `10springs-strategy.md` — strategic/advisory context (NOT for Claude Code)
- `_prototypes/dashboard-mockup.html` — Daytona bezel/subdial/card design reference
- `_prototypes/card-fan-v2.html` — fan-out alternates interaction reference
- `_prototypes/chatbar.html` — archived Claude API chat bar (removed from main dashboard)
- `CLAUDE.md` — project instructions for Claude Code agents
- `embed_images.py` — image embedding utility script

---

## File Ownership

Every file has a declared owner. Only the declared owner writes to that file.
Other roles read it, never edit it.

**`10springs-build.md`** — Split ownership
Sections A (Design System, Card Anatomy, Card Layout Rules) and C (Collection Data): Chat-owned.
Chat drafts updates; Joel commits directly to main.
Section B (Spec Deviations, Discovered Conventions, Build Log): Code-owned.
Code updates every commit. Chat reads after sync. Joel never rewrites any section directly.

**`index.html`** — Owner: Code
Code writes all HTML/CSS/JS. Chat reads via project sync.

**`CLAUDE.md`** — Owner: Joel
Updated manually when branch or PR URL changes.

**`_prototypes/*`** — Owner: Code
Reference files. Code may update; Chat reads.

**`embed_images.py`** — Owner: Code
Utility script. Code owns.

**`10springs-strategy.md`** — Owner: Chat
Claude project only — NOT in repo. Code never sees it.
Chat produces the complete file when updates are needed; Joel replaces it in the project knowledge panel.

The rule that matters most: Code must never regenerate or overwrite content
that Chat owns. If a task would require Code to touch a Chat-owned file,
stop and flag it instead.

---

## Design System

### Color Palette
- `#f4f1eb` — linen background
- `#f8f6f1` — card surfaces
- `#8a7b6a` — accent/warm gold
- `#1a1a1a` — near-black text
- `#cc2200` — status red
- `#0d0d0d` — bezel outer shell

### Typography
- **Bebas Neue** — bezel labels, tachymeter bar
- **Playfair Display** — watch names, headings
- **DM Sans** — body text, metadata
- **DM Mono** — reference numbers, codes

### Layout Components
- Bezel frame — dark #0d0d0d outer shell, tachymeter bar with copper Bebas Neue labels, lume dots at bottom
- Dial header — "10 Springs · Ages 35–45"
- Three Daytona subdials — Spent / Total Planned / Next Spring
- Heritage cards section — H1 + H2
- Collection timeline
- Watch slot sections — NOW through S10
- 10 Summers section
- Collection Philosophy accordion

---

## Card Anatomy

Every watch card — primary or alternate — contains the following fields.
Use this as the template when building any new card from scratch.

```
Reference number (e.g. "3410" or "166.010" or "–" if none)
Watch name (e.g. "Longines Flagship 18k")
Era / date range (e.g. "1958–1968")
Movement / key detail line (e.g. "18k solid gold case" or "Cal. 565 automatic")
Role descriptor (e.g. "Formal gold dress watch")
Budget (e.g. "$2–4K" or "$11–15K")
Listings link — Chrono24 search URL with watch-specific search terms
Research link — Google Search URL with watch-specific search terms
Status tags / pills (e.g. VINTAGE · DRESS or VINTAGE · CHRONO)
Watch image — imgur-hosted static <img src="..."> tag, or placeholder oval if no image yet
```

### Primary card distinguishers
- 2px solid warm gold border (`#8a7b6a`)
- Bolder visual weight than alternates

### Alternate card distinguishers
- 1px dashed border
- Same proportions as primary on mobile

### Status badges
- Removed from all collection cards (NOW–S10)
- Status communicated via timeline only
- Heritage cards retain HEIRLOOM · NOT FOR SALE tag

---

## Card Layout Rules (Locked)

- **Desktop:** All cards same size. Flat horizontal row, scrollable on overflow. No fan/rotation/overlap.
- **Mobile:** Always-visible horizontal scroll carousel. No expand/collapse toggle. All cards same proportions (taller, not squatty). Primary retains bolder border.
- **Placeholder oval:** Hidden via CSS `:has()` selector when real image is present.
- **Image rendering:** `image-rendering: high-quality` on all card images.
- **Responsive scaling:** `clamp(20px, 3.5vw, 44px)` for thumbnails. `flex: <slot-count>` proportional sizing. `overflow-x: auto` below 360px.
- **Image URLs:** Always use direct imgur format: `https://i.imgur.com/XXXXXXX.jpg`

---

## Spec Deviations

Code logs here whenever it departs from the spec in the Collection Data
or Card Layout Rules sections above. Chat reads this after sync and updates
the spec to match reality.

Format per entry: **Date · What changed · Why · What the spec should say instead.**

*(none yet)*

---

## Discovered Conventions

Code adds here whenever it encounters a new technical rule, tool behavior,
or failure mode not already listed in the Prompt Conventions section.
These accumulate across sessions. Chat reads them after sync and includes
them in the next prompt.

Format per entry: **Date · Convention · Files affected.**

---

**Pre-March 2026 · Large file writes**
Always use bash heredoc: `cat > file << 'PYEOF'`
Never use the Write tool for files over ~400 lines — it silently drops content.
Affects: index.html

**Pre-March 2026 · Image URLs**
Always use direct imgur format: `https://i.imgur.com/XXXXXXX.jpg`
Never use the page URL format: `https://imgur.com/XXXXXXX`
Affects: all card images

**Pre-March 2026 · Python script writes**
Always verify the file actually landed on disk after a Python script runs.
Silent failure is possible — the script appears to complete but the file may be missing or empty.
Affects: embed_images.py

**Pre-March 2026 · Git diff verification**
After any commit, verify git diff matches expected changes before moving to the next task.
Affects: all commits

**Pre-March 2026 · CSS image-rendering**
`image-rendering: high-quality` required on all card images.
GPU compositing from border-radius + overflow:hidden + transition:transform causes pixelation without it.
Affects: card images

**Pre-March 2026 · Lightbox DOM order**
The lightbox HTML element must appear in the DOM before the script that references it.
Placing the script first causes silent failure — no error thrown.
Affects: index.html

**Pre-March 2026 · CSS :has(>img) selector**
`:has(>img)` auto-hides placeholder ovals when a real image tag is present.
Affects: card placeholders

---

## What Is Currently Built and Live

✅ Bezel frame — dark outer shell, tachymeter bar, lume dots
✅ Dial header — "10 Springs · Ages 35–45"
✅ Three Daytona subdials — Spent (~$500) / Total Planned (~$91K) / Next Spring
✅ Heritage cards — H1 Caravelle + H2 Accutron. HEIRLOOM · NOT FOR SALE tag. Listings + Research links.
✅ Listings + Research links — on ALL cards, primary and alternate
✅ Collection Philosophy accordion — pills wrap horizontally on mobile
✅ 10 Summers section
✅ Font system — Bebas Neue + Playfair Display + DM Sans + DM Mono
✅ Color palette as above
✅ Claude API chat bar — removed. Archived to `_prototypes/chatbar.html`.
✅ Tap-for-photo behavior — removed entirely. Static imgur images only.
✅ Photo search JS — removed entirely
✅ Lightbox — click any watch image for fullscreen overlay. Dismiss via click outside, X, or Escape.
✅ Empty placeholder oval hidden when real image present
✅ Mobile layout — always-visible carousel, no toggle
✅ image-rendering: high-quality on card images
✅ S1 — Omega Seamaster 165.003 primary + 2 alts (166.010, Seamaster Cosmic) · All imgur images loaded · Row label updated to VINTAGE SPORT
✅ S2 — Longines Flagship 18k ref. 2404 primary + 4 alts (Conquest 18k, Constellation pie pan, UG gold dress, Seamaster 18k gold)
✅ S4 — Breitling Navitimer 816 primary + 2 alts (7806, Chrono-Matic 1806) · All imgur images loaded · Row label updated to AVIATION CHRONOGRAPH · Old El Primero/Sinn/Heuer/Speedmaster Reduced slate removed
✅ S5 — Omega Seamaster 300 Summer Blue primary + Black dial alt + Standard Blue alt · All imgur images loaded
✅ S6 — Speedmaster 3570.50 primary + Heuer Autavia Alt 1 · Tudor Alt 2 removed
✅ Full image URL sweep — all slots H1 through S10 have imgur images loaded (i.imgur.com direct format)
✅ Section headers audited — no duplicates or orphans found

---

## Remaining Open Tasks

- [ ] **S6 Alt 2** — needs a replacement watch. Content TBD pending strategy session. Currently no Alt 2 card in S6.
- [ ] **S7, S8, S9, S10** — cards not yet built into index.html. Content ready in Collection Data below. Agent 2 (S7), Agent 3 (S8), Agent 4 (S9+S10) pending.
- [ ] **Sparse card content** — some alternate cards missing role/notes line. Cards render shorter than neighbors. Fill in during a future content pass.

---

## Deferred (Longer Term)

- [ ] Skin toggle system — dashboard switches between visual themes (Daytona / Pepsi GMT / Hulk / Day-Date)
- [ ] Public collection builder tool — separate repo
- [ ] Tablet layout (600–899px)
- [ ] Mobile carousel final polish

---

## Collection Data — All Slots

*Source of truth for card content. Use reference numbers, eras, budgets, and alternates exactly as listed.*
*Budgets reflect current market ranges (Chrono24, March 2026) — not original planning estimates.*
*Chat-owned. Code reads, never regenerates.*

### Heritage Pieces

**H1 — Caravelle Manual Wind**
Era: 1950s · Manual wind · Provenance: Great-grandfather's watch
Tags: HEIRLOOM · NOT FOR SALE
Image: https://i.imgur.com/eGCtW23.jpg

**H2 — Bulova Accutron Spaceview**
Ref: Cal. 214 · Era: 1960s–70s · Tuning fork 360Hz
Tags: HEIRLOOM · NOT FOR SALE
Image: https://i.imgur.com/zSdYCso.jpg

---

### NOW (Age 35) — Longines Sport Chief
Ref: 7042 · Era: Late 1950s–early 1960s · Cal. 30L manual wind
Dial: Cream/ivory · Case: ~36–38mm stainless · Price paid: ~$500
Status: IN HAND
Image: https://i.imgur.com/Qniu7LS.jpg
Alternates:
- Omega Seamaster small seconds (2757) · https://i.imgur.com/RvJLLqJ.jpg
- Omega Genève manual (131.019) · https://i.imgur.com/30AVqnM.jpg
- Tissot Antimagnetique · https://i.imgur.com/1BHjSfR.jpg

---

### S1 (Age 36) — Omega Seamaster 165.003 ✅ RESTRUCTURED APRIL 2026
Primary ref: 165.003 · Era: 1962–1969 · Cal. 552 automatic
Dial: Black lacquered · No date · Budget: $1.5–2.5K
Role: Opens collection — high-contrast vintage Omega, exploration age object, entry into the market
Tags: VINTAGE · SPORT
Note: Dial authenticity flag — avoid black crosshair dial variants (frequently redials). Stick to standard 165.003.
Image: [PLACEHOLDER — imgur URL pending]
Alternates:
- Alt 1: Omega Seamaster 166.010 (date version, Cal. 562/565, same era, more available) · $1.2–2K · [PLACEHOLDER — imgur URL pending]
- Alt 2: Omega Seamaster Cosmic (cushion case, black dial, late 1960s, more wrist character) · $1.5–2.5K · [PLACEHOLDER — imgur URL pending]

---

### S2 (Age 37) — Longines Flagship 18k ✅ LOCKED
Primary ref: 2404 · Era: 1958–1968 · 18k solid gold · Cal. 30L family
Dial: Cream or champagne · Budget: $2–4K
Role: Solid gold vintage dress watch — formal/important occasion piece
Tags: VINTAGE · DRESS
Image: https://i.imgur.com/9fRcxvp.jpg
Alternates:
- Alt 1: Longines Conquest 18k solid gold · $2–4K · https://i.imgur.com/CowmIVN.jpg
- Alt 2: Omega Constellation pie pan 18k solid gold (Cal. 505/561, observatory caseback) · $2–4K · https://i.imgur.com/d041da6.jpg
- Alt 3: Universal Genève solid gold dress 1960s · $2–4K · https://i.imgur.com/51bCgrN.jpg
- Alt 4: Omega Seamaster 18k solid gold 1960s · $2–4K · https://i.imgur.com/tszQWDU.jpg

---

### S3 (Age 38) — Universal Genève Polerouter
Ref: 20217 · Era: 1956–1964 · Micro-rotor Cal. 215/218 · Designer: Gerald Genta
Dial preference: Tropical brown (primary) · crosshair silver and blue dial (alternates within ref)
Budget: $2–4K
Tags: VINTAGE · INSTRUMENT
Image: https://i.imgur.com/adAggDf.jpg
Alternates:
- Girard-Perregaux Gyromatic 1965–72 · $2–4K · https://i.imgur.com/y4Jlu1i.jpg
- Omega Dynamic (166.039) · $2–4K · https://i.imgur.com/GldPRzF.jpg
- Zenith Defy (A3642) · $2–4K · https://i.imgur.com/WV71kEh.jpg

---

### S4 (Age 39) — Breitling Navitimer 816 ✅ RESTRUCTURED APRIL 2026
Primary ref: 816 · Era: 1960s–early 1970s · Valjoux 72 movement preferred
Dial: Black, circular slide rule bezel, sector subdials · Budget: $3–5K
Role: Vintage aviation chronograph — sector dial, AOPA heritage, exploration age instrument. Moved from S1; narrative strengthens at age 39.
Tags: VINTAGE · CHRONO
Image: [PLACEHOLDER — imgur URL pending]
Alternates:
- Alt 1: Breitling Navitimer 7806 · $3–5K · https://i.imgur.com/A7ZOpLZ.jpg
- Alt 2: Breitling Chrono-Matic 1806 (automatic Cal. 11, left crown at 9 o'clock, ~1969–1973) · $3–5K · https://i.imgur.com/LXPtsUr.jpg

---

### S5 (Age 40) — Omega Seamaster 300 ✅ BUILT
Primary ref: 234.30.41.21.03.002 · Era: 2021–present · Cal. 8912 Master Chronometer
Dial: Summer Blue · Bezel: Blue anodized aluminum · Case: 41mm stainless · Budget: $6–8K
Role: First diver chapter. First blue dial in collection. Sandwich dial construction.
Tags: MODERN · SPORT
Image: https://i.imgur.com/AXO9P3F.jpg
Alternates:
- Alt 1: Black dial · ref. 234.30.41.21.01.001 · $6–8K · https://i.imgur.com/obC0kB2.jpg
- Alt 2: Standard Blue · ref. 234.30.41.21.03.001 · $6–8K · https://i.imgur.com/dm0mUZx.jpg

---

### S6 (Age 41) — Omega Speedmaster Professional ✅ BUILT
Ref: 3570.50 · Era: 1996–2014 · Cal. 1861 · Moonwatch, hesalite, no date
Budget: $4–7K · Status: DECIDED
Tags: MODERN · CHRONO
Image: https://i.imgur.com/iIzRToh.jpg
Alternates:
- Alt 1: Heuer Autavia vintage pre-1985 · $3–5K · https://i.imgur.com/ZHcDHX0.jpg
- Alt 2: ⚠️ NEEDS REPLACEMENT — content TBD pending strategy session. No card currently.

---

### S7 (Age 42) — Glashütte Original PanoMaticLunar ⚠️ AGENT 2 PENDING
Ref: 1-90-02-46-32-50 · Current production · ~40mm steel
Dial: Deep sunburst blue · Budget: $7–10K
Role: German moonphase as engineering object. Asymmetric off-center layout. Single non-Swiss manufacture voice.
Tags: MODERN · DRESS
Image: https://i.imgur.com/w443h5L.jpg
Alternates:
- Alt 1: JLC Master Ultra Thin Moon (Q1368430) · $7–10K · https://i.imgur.com/7PZY1nI.jpg
- Alt 2: Glashütte Original PanoMaticLunar silver/white dial · $7–10K · https://i.imgur.com/V4kj0SS.jpg

---

### S8 (Age 43) — Blancpain Fifty Fathoms Automatique ⚠️ AGENT 3 PENDING
Primary: Fifty Fathoms Automatique · Black dial · 45mm · Cal. 1315 · Budget: $11–17K
Role: Second diver chapter. Serious collector diver. Blancpain invented the modern dive watch category.
Tags: MODERN · SPORT
Image: https://i.imgur.com/ytTh26h.jpg
Alternates:
- Alt 1: Blancpain Fifty Fathoms Bathyscaphe · blue or black dial · 43mm · $11–17K · https://i.imgur.com/RMJrcaf.jpg
- Alt 2: Rolex Submariner Hulk 116610LV · $11–17K · https://i.imgur.com/bLQLOff.jpg

---

### S9 (Age 44) — Rolex Day-Date ⚠️ AGENT 4 PENDING
Ref: 18038 · Era: 1977–1988 · Full yellow gold · Presidential bracelet
Dial: Champagne/gold (primary) · Budget: $15–22K
Role: The statement. Full yellow gold Presidential. Cultural weight and legacy.
Tags: VINTAGE · DRESS
Image: https://i.imgur.com/2ozRGG4.jpg
Alternates:
- Alt 1: Black dial 18038 · $15–22K · https://i.imgur.com/YeJ9DOB.jpg
- Alt 2: Blue dial 18038 · $15–22K · Dial originality must be verified — aftermarket blue dials are extremely common. Do not accept any example without confirmed provenance. · https://i.imgur.com/U9HPEm4.jpg

---

### S10 (Age 45) — Rolex GMT Master 1675 ⚠️ AGENT 4 PENDING
Ref: 1675 · Era: ~1968 target · Gilt dial just starting to patina · Budget: $18–28K
Role: The grail. Pan Am pilot navigation instrument. Aviation bookend to S4 Navitimer.
Tags: VINTAGE · SPORT
Note on card: "Target 1968 examples. Gilt dial, unpolished case, no bracelet sag. The patina story is just beginning."
Image: https://i.imgur.com/IvmHdl2.jpg
Alternates:
- Alt 1: IWC Portugieser Perpetual Calendar · black Arabic dial · steel · $14–22K · MODERN · DRESS · Note: "True perpetual calendar. Only needs correction February 29 every 4 years." · https://i.imgur.com/lyzMe25.jpg
- Alt 2: Breitling Navitimer 806 AOPA · gilt dial · $5–10K · VINTAGE · CHRONO · Note: "Narrative bookend to S4 Navitimer. The watch that established the gilt dial taste signal." · https://i.imgur.com/seEZt3H.jpg

---

## Claude Code Prompt Conventions

*Chat uses this section to construct every Code prompt. All required
elements are included automatically — Joel never has to add them manually.*

### Every prompt must include:

**1. Read first**
"Before starting, read `10springs-build.md` fully, including the
Spec Deviations and Discovered Conventions sections."

**2. Planning step**
"Describe every file you will touch and what you will change.
Include a rough time estimate for the full task.
Wait for my explicit 'go ahead' before executing."

**3. Deviation logging**
"If you depart from the card data, layout rules, or design system spec
in this file, log it in the Spec Deviations section:
date · what changed · why · what the spec should say instead."

**4. Build log update**
"Update the build log (✅ checklist and open tasks) as part of your commit —
not as a separate step. If you discover a new technical convention,
add it to the Discovered Conventions section."
"Update the date stamp at the top of `10springs-build.md` to today's date as part of your commit — format: `Last updated: Month DD, YYYY`."

**5. Loop-stop rule**
"If you find yourself retrying the same approach more than twice,
stop and tell me what's blocking rather than continuing to loop."

**6. PR link**
"After committing, provide the direct PR merge link to merge your branch
into main so I can merge with one click."

### Technical conventions (include when relevant):

**Large file writes (index.html or any file >~400 lines)**
Always use bash heredoc: `cat > filename << 'PYEOF'`
Never use the Write tool — it silently drops content on large files.

**Prototype reference**
Read `_prototypes/dashboard-mockup.html` and `_prototypes/card-fan-v2.html`
for design system and animation specs before building. Do not rebuild from scratch.

**Python scripts**
Verify the file was actually written to disk after any Python script runs.

**Image URLs**
Always use direct imgur format `https://i.imgur.com/XXXXXXX.jpg` — never the page URL format.

**After any commit**
Verify git diff matches expected changes before moving to the next task.

**New conventions**
Check the Discovered Conventions section above before starting —
it may contain rules not listed here.

### Agent hygiene:

- Start a fresh agent for each distinct build phase
- Never reuse an agent across PR merges
- When layout or CSS prompts loop more than twice: stop, report, re-spec before retrying
- Claude Code must not push to main directly — all new code lands via PR, merged by Joel
