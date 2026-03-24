DASHBOARD BUILD CONTEXT (10springs-build.md)
════════════════════════════════════════════
# 10 Springs — Dashboard Build Reference
*For Claude Code agents and dashboard build sessions*
*Last updated: March 2026*

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

Every watch card — primary or alternate — contains the following fields. Use this as the template when building any new card from scratch.

```
Reference number (e.g. "3410" or "166.010" or "–" if none)
Watch name (e.g. "Longines Flagship 18k")
Era / date range (e.g. "1958–1968")
Movement / key detail line (e.g. "18k solid gold case" or "Cal. 565 automatic")
Role descriptor (e.g. "Formal gold dress watch")
Budget (e.g. "~$1K" or "$2–4K")
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

## What Is Currently Built and Live

✅ Bezel frame — dark outer shell, tachymeter bar, lume dots
✅ Dial header — "10 Springs · Ages 35–45"
✅ Three Daytona subdials — Spent (~$500) / Total Planned ($84K) / Next Spring ($1K)
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
✅ S7 primary — Hulk (116610LV) with note "or another colorful sport watch"
✅ Empty placeholder oval hidden when real image present
✅ Mobile layout — always-visible carousel, no toggle
✅ image-rendering: high-quality on card images
✅ S1 — Breitling Navitimer 816 primary + 3 alts (7806, Chrono-Matic 1806, Heuer Carrera 3147S)
✅ S2 — Longines Flagship 18k ref. 2404 primary + 4 alts (Conquest 18k, Constellation pie pan, UG gold dress, Seamaster 18k gold)
✅ S4 — Sinn 103 added as Alt 4 · Zenith El Primero Shark Tooth A3817 added as Alt 1
✅ S6 — Heuer Autavia (vintage, pre-1985) added as Alt 1 · Tudor Black Bay Chrono as Alt 2
✅ S8 — GO PanoMaticLunar as primary · JLC as Alt 1 · GO silver dial as Alt 2
✅ Full image URL sweep — all slots H1 through S8 have imgur images loaded (i.imgur.com direct format)
✅ Section headers audited — no duplicates or orphans found

---

## Pending Build Tasks

- [ ] **S9 alternates** — content needs strategic review. Placeholders currently in dashboard.

- [ ] **S10 alternates** — content needs strategic review. Placeholders currently in dashboard.

- [ ] **Sparse card content** — some alternate cards missing role/notes line (Heuer Carrera 2447, Omega Speedmaster Reduced, a few others). Cards render shorter than neighbors as a result. Fill in during a future content pass.

- [ ] **S10 Omega Planet Ocean / AP Royal Oak** — confirm whether these are intentional alternates or leftover placeholders. Needs strategic review alongside S10 alternates.

- [ ] **Add imgur URLs** for S9 and S10 alternates — defer until after strategic review and alternate decisions made.

---

## Deferred (Longer Term)

- [ ] Skin toggle system — dashboard switches between visual themes (Daytona / Pepsi GMT / Hulk / Day-Date)
- [ ] Public collection builder tool — separate repo
- [ ] Tablet layout (600–899px)
- [ ] Mobile carousel final polish

---

## Collection Data — All Slots

*Source of truth for card content. Use reference numbers, eras, and alternates exactly as listed.*

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

### S1 (Age 36) — Breitling Navitimer ✅ LOCKED
Primary ref: 816 · Era: 1960s–early 1970s · Valjoux 72 movement
Dial: Black, circular slide rule bezel, sector subdials · Budget: ~$2–3K
Role: Vintage aviation chronograph — sector dial, AOPA heritage, exploration age instrument
Tags: VINTAGE · CHRONO
Image: https://i.imgur.com/ntyvdp2.jpg
Alternates:
- Alt 1: Breitling Navitimer 7806 · https://i.imgur.com/A7ZOpLZ.jpg
- Alt 2: Breitling Chrono-Matic 1806 (automatic Cal. 11, left crown at 9 o'clock, ~1969–1973) · https://i.imgur.com/LXPtsUr.jpg
- Alt 3: Heuer Carrera 3147S · https://i.imgur.com/T7KDcpi.jpg

---

### S2 (Age 37) — Longines Flagship 18k ✅ LOCKED
Primary ref: 2404 · Era: 1958–1968 · 18k solid gold · Cal. 30L family
Dial: Cream or champagne · Budget: ~$2K
Role: Solid gold vintage dress watch — formal/important occasion piece
Tags: VINTAGE · DRESS
Image: https://i.imgur.com/9fRcxvp.jpg
Alternates:
- Alt 1: Longines Conquest 18k solid gold · https://i.imgur.com/CowmIVN.jpg
- Alt 2: Omega Constellation pie pan 18k solid gold (Cal. 505/561, observatory caseback) · https://i.imgur.com/d041da6.jpg
- Alt 3: Universal Genève solid gold dress 1960s · https://i.imgur.com/51bCgrN.jpg
- Alt 4: Omega Seamaster 18k solid gold 1960s · https://i.imgur.com/tszQWDU.jpg

---

### S3 (Age 38) — Universal Genève Polerouter
Ref: 20217 · Era: 1956–1964 · Micro-rotor Cal. 215/218 · Designer: Gerald Genta
Dial preference: Tropical brown (primary) · crosshair silver and blue dial (alternates within ref)
Budget: $2–4K
Tags: VINTAGE · INSTRUMENT
Image: https://i.imgur.com/adAggDf.jpg
Alternates:
- Girard-Perregaux Gyromatic 1965–72 · https://i.imgur.com/y4Jlu1i.jpg
- Omega Dynamic (166.039) · https://i.imgur.com/GldPRzF.jpg
- Zenith Defy (A3642) · https://i.imgur.com/WV71kEh.jpg

---

### S4 (Age 39) — Zenith El Primero
Ref: A386 (primary) · Era: 1969–1972 · El Primero 3019PHC · 36,000 vph
Dial: Black, instrument style · Budget: $2–3K
Tags: VINTAGE · CHRONO
Image: https://i.imgur.com/lJQ6Cxf.jpg
Alternates:
- Alt 1: Zenith El Primero "Shark Tooth" A3817 (strong alternate, darker instrument aesthetic) · https://i.imgur.com/fKC4eKx.jpg
- Alt 2: Heuer Carrera (2447) · https://i.imgur.com/rkruIxa.jpg
- Alt 3: Omega Speedmaster Reduced (3510.50) · https://i.imgur.com/WFqzMgH.jpg
- Alt 4: Sinn 103 (current production, ~$2K) · https://i.imgur.com/gijyQWI.jpg

---

### S5 (Age 40) — Rolex Datejust
Ref: 1601 · Era: 1965–1977 · Fluted bezel, pie-pan dial
Dial preference: Black or blue sunburst · Budget: $4–6K
Tags: VINTAGE · DRESS
Image: https://i.imgur.com/hDaZahC.jpg
Alternates:
- Rolex Explorer (14270) · https://i.imgur.com/tfTCQxF.jpg
- Rolex Air-King (5500) · https://i.imgur.com/QNGqXGx.jpg
- Rolex Turn-O-Graph (1625) · https://i.imgur.com/scbvgTc.jpg

---

### S6 (Age 41) — Omega Speedmaster Professional
Ref: 3570.50 · Era: 1996–2014 · Cal. 1861 · Moonwatch, hesalite, no date
Budget: $4–6K · Status: DECIDED
Tags: MODERN · CHRONO
Image: https://i.imgur.com/iIzRToh.jpg
Alternates:
- Alt 1: Heuer Autavia vintage pre-1985 (~$3–5K) · https://i.imgur.com/ZHcDHX0.jpg
- Alt 2: Tudor Black Bay Chrono (79360N) · https://i.imgur.com/4LsfhSl.jpg

---

### S7 (Age 42) — Rolex Submariner "Hulk"
Ref: 116610LV · Era: 2010–2020 · Green ceramic bezel · Discontinued 2020
Budget: $12–20K · Note on card: "or another colorful sport watch"
Tags: MODERN · SPORT
Image: https://i.imgur.com/bLQLOff.jpg
Alternates:
- Alt 1: Rolex GMT-Master II "Batman" (116710BLNR) · https://i.imgur.com/zUWUKzm.jpg
- Alt 2: Rolex GMT-Master II "Root Beer" (126711CHNR) · https://i.imgur.com/dVopQSA.jpg
- Alt 3: Omega Seamaster Diver 300M · https://i.imgur.com/P8gfdc5.jpg
- Alt 4: Tudor Black Bay 58 Blue (79030B) · https://i.imgur.com/Xu1yIW5.jpg

---

### S8 (Age 43) — Glashütte Original PanoMaticLunar ✅ UPDATED
Ref: 1-90-02-46-32-50 · Current production · ~40mm steel
Dial: Deep sunburst blue · Budget: $7–9K
Tags: MODERN · DRESS
Image: https://i.imgur.com/w443h5L.jpg
Alternates:
- Alt 1: JLC Master Ultra Thin Moon (Q1368430) · https://i.imgur.com/7PZY1nI.jpg
- Alt 2: Glashütte Original PanoMaticLunar silver/white dial · https://i.imgur.com/V4kj0SS.jpg

---

### S9 (Age 44) — Rolex Day-Date
Ref: 18038 (vintage 36mm preferred) or 228238 (modern 40mm)
Era: 1978–1988 (vintage ref) · Full yellow gold · Presidential bracelet
Dial: Champagne (default) · Black (strongly preferred alternate)
Budget: $14–18K
Tags: VINTAGE · DRESS
Alternates: ⚠️ NEEDS STRATEGIC REVIEW — placeholders currently in dashboard

---

### S10 (Age 45) — Rolex GMT-Master "Pepsi"
Ref: 1675 · Era: 1965–1979 · Budget: $14–18K
Tags: VINTAGE · SPORT
Alternates: ⚠️ NEEDS STRATEGIC REVIEW — placeholders currently in dashboard
Note: Omega Planet Ocean and AP Royal Oak currently showing as placeholder alts — confirm whether intentional or remove.

---

## Claude Code Prompt Conventions

### Every prompt must:
1. Start with a planning step — describe what will change and wait for confirmation before executing
2. End with: *"After committing, provide the direct PR merge link to merge your branch into main so I can merge with one click."*
3. Include: *"If you find yourself retrying the same approach more than twice, stop and tell me what's blocking rather than continuing to loop."*

### Technical conventions:
- **Large file writes:** Always use bash heredoc (`cat > index.html << 'PYEOF'`) — never sub-agents or the Write tool for files over ~400 lines. The Write tool silently drops the `content` parameter on large writes.
- **Prototype files:** Reference `_prototypes/dashboard-mockup.html` and `_prototypes/card-fan-v2.html` for design system and animation specs — don't rebuild from scratch.
- **Python script writes:** Always verify the file was actually written to disk after a Python script runs.
- **After any commit:** Verify the git diff matches expected changes before moving to the next task.
- **Image URLs:** Always use direct imgur format `https://i.imgur.com/XXXXXXX.jpg` — never the page URL format `https://imgur.com/XXXXXXX`.

### Agent hygiene:
- Start a fresh agent for each distinct build phase
- When layout or CSS prompts loop more than twice, stop and re-spec before continuing
- Claude Code cannot push directly to main — manual PR merge always required
