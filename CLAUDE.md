# 10 Springs

**Repo:** github.com/JoelColeman/10-springs
**Live:** joelcoleman.github.io/10-springs
**Stack:** Single-file index.html · Vanilla HTML/CSS/JS · GitHub Pages hosting
**Drive location:** My Drive > NetTerminalGene - Drive > GitHub > 10-springs
**Last updated:** April 26, 2026

---

## Section A — Project Spec
*Owner: Chat. Code reads, never edits. If reality departs from this spec, Code logs the deviation in Section B.*

10 Springs is a single-page collection dashboard for a 10-watch mechanical watch collection built one watch per spring, ages 35–45. The live site is a single `index.html` file hosted on GitHub Pages.

### Layout (top to bottom)
- **Bezel frame** — dark `#0d0d0d` outer shell, tachymeter bar with copper Bebas Neue labels, lume dots at bottom
- **Dial header** — "10 Springs · Ages 35–45"
- **Three Daytona subdials** — Spent (~$500) / Total Planned (~$91K) / Next Spring
- **Heritage cards section** — H1 Caravelle + H2 Accutron Spaceview
- **Collection timeline**
- **Watch slot sections** — NOW through S10, each with primary + alternates
- **10 Summers section** — placeholder list of future watches
- **Collection Philosophy accordion**
- **Watch Intel RSS section** — placed outside bezel above footer

### Card anatomy
Every watch card (primary or alternate) contains:
```
Reference number (e.g. "816" or "165.003" or "–" if none)
Watch name (e.g. "Longines Flagship 18k")
Era / date range (e.g. "1958–1968")
Movement / key detail line (e.g. "18k solid gold case" or "Cal. 552 automatic")
Role descriptor (e.g. "Formal gold dress watch")
Budget (e.g. "$2–4K")
Listings link — Chrono24 search URL
Research link — Google Search URL
Status tags / pills (e.g. VINTAGE · DRESS)
Watch image — imgur-hosted static <img> tag, or placeholder oval if no image yet
```

### Card layout rules (locked)
- **Desktop:** All cards same size. Flat horizontal row, scrollable on overflow. No fan/rotation/overlap.
- **Mobile:** Always-visible horizontal scroll carousel. No expand/collapse toggle. All cards same proportions (taller, not squatty). Primary retains bolder border.
- **Primary card:** 2px solid warm gold border (`#8a7b6a`), bolder visual weight
- **Alternate card:** 1px dashed border, same proportions as primary
- **Status badges:** Removed from all collection cards (NOW–S10). Status communicated via timeline only. Heritage cards retain HEIRLOOM · NOT FOR SALE tag.
- **Placeholder oval:** Hidden via CSS `:has()` selector when real image is present
- **Image rendering:** `image-rendering: high-quality` on all card images
- **Responsive scaling:** `clamp(20px, 3.5vw, 44px)` for thumbnails. `overflow-x: auto` below 360px.
- **Image URLs:** Always use direct imgur format: `https://i.imgur.com/XXXXXXX.jpg`

### Watch Intel RSS section
- 4 feeds: Hodinkee, A Blog to Watch, Fratello Watches, Teddy Baldassarre
- Fetched via rss2json.com as CORS proxy
- 16 most-recent articles sorted by date
- In-collection keyword tagging
- Light card panel (`#f8f6f1` bg, warm border, 8px radius)
- Distinct pill badge colors per source
- Row hover tint; date/status text warm muted; title underline on hover

---

## Section B — Build Log
*Owner: Code. Updated as part of every commit.*

### Spec Deviations

| Date | What Changed | Why | Spec Update Needed |
|---|---|---|---|
| April 3, 2026 | S5 Chrono24 URL refs corrected | Task spec's corrected URL table showed Summer Blue primary as 234.30.41.21.03.001 and Standard Blue as 234.30.41.21.03.002 — reverse of what was in file. Applied corrected table as authoritative. | Note: Listing URL refs may differ from card-ref display refs |
| April 3, 2026 | S1 Alt 2 URL trimmed | Task spec showed Seamaster Cosmic without "+vintage" suffix. Removed "+vintage" from query string. No card content change. | — |
| April 3, 2026 | S3 primary URL trimmed | Task spec shows query=Universal+Geneve+Polerouter (no +20217 ref). Removed +20217 from query string. | — |
| April 3, 2026 | S6 primary URL trimmed | Task spec shows query=Omega+Speedmaster+3570.50 (no "Professional"). Removed "Professional" from query string. | — |
| April 9, 2026 | 10 Summers list corrected | Removed: AP Royal Oak 14790, Patek Calatrava 5119, Patek Annual Calendar 5146, FP Journe, Vintage Patek. Added: UG Tri-Compax, Zenith A386, Lange 1, Lange 1 Moon, Rolex 1675 Tropical. List reordered by price ascending. | 10 Summers list order is price-ascending; all entries include price range in meta line |

### Discovered Conventions

| Date | Convention | Context |
|---|---|---|
| Pre-March 2026 | Large file writes: always use bash heredoc (`cat > file << 'PYEOF'`). Never use Write tool on files >~400 lines — silently drops content. | index.html |
| Pre-March 2026 | Image URLs: always direct imgur format `https://i.imgur.com/XXXXXXX.jpg`. Never the page URL format. | All card images |
| Pre-March 2026 | Python script writes: always verify file landed on disk after script runs. Silent failure possible. | embed_images.py |
| Pre-March 2026 | Git diff verification: after any commit, verify git diff matches expected changes before next task. | All commits |
| Pre-March 2026 | CSSimage-rendering: `image-rendering: high-quality` required on all card images. GPU compositing from border-radius + overflow:hidden + transition:transform causes pixelation without it. | Card images |
| Pre-March 2026 | Lightbox DOM order: lightbox HTML must appear in DOM before the script that references it. Placing script first causes silent failure — by no error thrown. | index.html |
| Pre-March 2026 | CSS`:has(>img)` selector auto-hides placeholder ovals when real image tag is present. | Card placeholders |

### Completed Tasks

✅ Bezel frame — dark outer shell, tachymeter bar, lume dots
✅ Dial header — "10 Springs · Ages 35–45"
✅ Three Daytona subdials — Spent (~$500) / Total Planned (~$91K) / Next Spring
✅ Heritage cards — H1 Caravelle + H2 Accutron. HEIRLOOM · NOT FOR SALE tag. Listings + Research links.
✅ Listings + Research links — on ALL cards, primary and alternate
✅ Collection Philosophy accordion — pills wrap horizontally on mobile
✅ 10 Summers section
✅ Font system — Bebas Neue + Playfair Display + DM Sans + DM Mono
✅ Color palette as specified
✅ Claude API chat bar — removed. Archived to `_prototypes/chatbar.html`.
✅ Tap-for-photo behavior — removed entirely. Static imgur images only.
✅ Photo search JS — removed entirely
✅ Lightbox z«� click any watch image for fullscreen overlay. Dismiss via click outside, X, or Escape.
✅ Empty placeholder oval hidden when real image present
✅ Mobile layout — always-visible carousel, no toggle
✅ image-rendering: high-quality on card images
✅ S1 — Omega Seamaster 165.003 primary + 2 alts (166.010, Seamaster Cosmic) · All imgur images loaded · Row label VINTAGE SPORT
✅ S2 — Longines Flagship 18k ref. 2404 primary + 4 alts
✅ S4 — Breitling Navitimer 816 primary + 2 alts · All imgur images loaded · Row label AVIATION CHRONOGRAPH · Old El Primero/Sinn/Heuer/Speedmaster Reduced slate removed
✅ S5 — Omega Seamaster 300 Summer Blue primary + Black dial alt + Standard Blue alt · All imgur images loaded
✅ S6 — Speedmaster 3570.50 primary + Heuer Autavia Alt 1 · Tudor Alt 2 removed
✅ Full image URL sweep — all slots H1 through S10 have imgur images loaded (i.imgur.com direct format)
✅ Section headers audited —"no duplicates or orphans
✅ Chrono24 URL sweep — all cards updated to clean ?query= format; &redirectToSearchIndex=true stripped globally; S2/S4/S6-alt1 custom paths converted; S3 query trimmed; S5 refs corrected; S6 "Professional" dropped
✅ Watch Intel RSS section — 4 feeds via rss2json.com; 16 articles sorted by date; keyword tagging; outside bezel above footer
✅ Watch Intel readability fix — light card panel; WATCH INTEL header near-black; dark pill badges per source; row hover tint
✅ S7 — Glashütte Original PanoMaticLunar primary + Alt 1 JLC Master Ultra Thin Moon + Alt 2 GO PanoMaticLunar Silver/White · All imgur images loaded
✅ S8 — Blancpain Fifty Fathoms Automatique primary + Alt 1 Bathyscaphe + Alt 2 Rolex Submariner Hulk 116610LV · All imgur images loaded
✅ S9 — Rolex Day-Date 18038 champagne primary + Alt 1 black dial + Alt 2 blue dial (originality warning rendered) · All imgur images loaded
✅ S10 — Rolex GMT-Master 1675 primary + Alt 1 IWC Portugieser Perpetual Calendar + Alt 2 Breitling Navitimer 806 AOPA · All imgur images loaded
✅ 10 Summers list corrected and reordered by price ascending

### Open Tasks

- [ ] **S6 Alt 2** — needs a replacement watch. Content TBD pending strategy session. Currently no Alt 2 card in S6.
- [ ] **Watch Intel — HTML entity decoding** — article titles with &amp; and other entities render as raw text. Fix esc() function to decode before display.
- [ ] **Watch Intel — keyword tightening** — Longines and Omega match too broadly. Tighten to specific references only (Sport Chief, Flagship, Conquest; Seamaster 300, Speedmaster, Seamaster 165.003).
- [ ] **Sparse card content** — some alternate cards missing role/notes line. Cards render shorter than neighbors. Fill in during a future content pass.

### Deferred

- [ ] Skin toggle system — dashboard switches between visual themes (Daytona / Pepsi GMT / Hulk / Day-Date)
- [ ] Public collection builder tool — separate repo
- [ ] Tablet layout (600–899px)
- [ ] Mobile carousel final polish

---

## Section C — Content Data
*Owner: Chat. Code reads, never regenerates.*

*Budgets reflect current market ranges (Chrono24, March–April 2026) — not original planning estimates.*

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
Dial: Cream/ivory �� Case: ~37⟓38mm stainless · Price paid: ~$500
Status: IN HAND
Image: https://i.imgur.com/Qniu7LS.jpg
Alternates:
- Omega Seamaster small seconds (2757) · https://i.imgur.com/RvJLLqJ.jpg
- Omega Genève manual (131.019) · https://i.imgur.com/30AVqnM.jpg
- Tissot Antimagnetique · https://i.imgur.com/1BHjSfR.jpg

---

### S1 (Age 36) — Omega Seamaster 165.003
Primary ref: 165.003 · Era: 1962–1969 · Cal. 552 automatic
Dial: Black lacquered · No date · Budget: $1.5–2.5K
Role: Opens collection — high-contrast vintage Omega, exploration age object, entry into the market
Tags: VINTAGE · SPORT
Note: Dial authenticity flag — avoid black crosshair dial variants (frequently redials). Stick to standard 165.003.
Image: [PLACEHOLDER — imgur URL pending]
Alternates:
- Alt 1: Omega Seamaster 166.010 (date version, Cal. 562/565, same era) · $1.2–2K · [PLACEHOLDER]
- Alt 2: Omega Seamaster Cosmic (cushion case, black dial, late 1960s) · $1.5–2.5K · [PLACEHOLDER]

---

### S2 (Age 37) — Longines Flagship 18k ✅ LOCKED
Primary ref: 2404 · Era: 1958–1968 · 18k solid gold · Cal. 30L family
Dial: Cream or champagne · Budget: $2–4K
Role: Solid gold vintage dress watch — formal/important occasion piece
Tags: VINTAGE · DRESS	mage: https://i.imgur.com/9fRcxvp.jpg
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
image: https://i.imgur.com/adAggDf.jpg
Alternates:
- Girard-Perregaux Gyromatic 1965–72 · $2–4K · https://i.imgur.com/y4Jlu1i.jpg
- Omega Dynamic (166.039) · $2–4K · https://i.imgur.com/GldPRzF.jpg
- Zenith Defy (A3642) · $2–4K · https://i.imgur.com/WV71kEh.jpg

---

### S4 (Age 39) — Breitling Navitimer 816 ✅ RESTRUCTURED APRIL 2026
Primary ref: 816 · Era: 1960s–early 1970s · Valjoux 72 movement preferred
Dial: Black, circular slide rule bezel, sector subdials · Budget: $3–5K
Role: Vintage aviation chronograph — sector dial, AOPA heritage, exploration age instrument
Tags: VINTAGE · CHRONO
Image: [PLACEHOLDER — imgur URL pending]
Alternates:
- Alt 1: Breitling Navitimer 7806 · $3–5K · https://i.imgur.com/A7ZOpLZ.jpg
- Alt 2: Breitling Chrono-Matic 1806 (automatic Cal. 11, left crown at 9 o'clock, ~1969–1973) · $3–5K · https://i.imgur.com/LXPtsUr.jpg

---

### S5 (Age 40) — Omega Seamaster 300 ✅ BUILT
Primary ref: 234.30.41.21.03.002 · Era: 2021​present · Cal. 8912 Master Chronometer
Dial: Summer Blue · Bezel: Blue anodized aluminum · Case: 41mm stainless · Budget: $6–8K
Role: First diver chapter. First blue dial in collection. Sandwich dial construction.
Tags: MODERN · SPORT
image: https://i.imgur.com/AXO9P3F.jpg
Alternates:
- Alt 1: Black dial · ref. 234.30.41.21.01.001  · $6–8K · https://i.imgur.com/obC0kB2.jpg
- Alt 2: Standard Blue · ref. 234.30.41.21.03.001 · $6–8K · https://i.imgur.com/dm0mUZx.jpg

---

### S6 (Age 41) z� Omega Speedmaster Professional ✅ BUILT
Ref: 3570.50 · Era: 1996–2014 · Cal. 1861 · Moonwatch, hesalite, no date
Budget: $4–7K · Status: DECIDED
Tags: MODERN · CHRONO
Image: https://i.imgur.com/iIzRToh.jpg
Alternates:
- Alt 1: Heuer Autavia vintage pre-1985 · $3–5K · https://i.imgur.com/ZHcDHX0.jpg
- Alt 2: ⚠️ NEEDS REPLACEMENT — content TBD pending strategy session. No card currently.

---

### S7 (Age 42) — Glashütte Original PanoMaticLunar
Ref: 1-90-02-46-32-50 · Current production · ~40mm steel
Dial: Deep sunburst blue · Budget: $7–10K
Role: German moonphase as engineering object. Asymmetric off-center layout. Single non-Swiss manufacture voice.
Tags: MODERN · DRESS
Image: https://i.imgur.com/w443h5L.jpg
Alternates:
- Alt 1: JLC Master Ultra Thin Moon (Q1368430) · $7–10K · https://i.imgur.com/7PZY1nI.jpg
- Alt 2: Glashütte Original PanoMaticLunar silver/white dial · $7–10K · https://i.imgur.com/V4kj0SS.jpg

---

### S8 (Age 43) — Blancpain Fifty Fathoms Automatique
Primary: Fifty Fathoms Automatique · Black dial · 45mm · Cal. 1315 · Budget: $11–17K
Role: Second diver chapter. Serious collector diver. Blancpain invented the modern dive watch category.
Tags: MODERN · SPORT
Image: https://i.imgur.com/ytTh26h.jpg
Alternates:
- Alt 1: Blancpain Fifty Fathoms Bathyscaphe · blue or black dial · 43mm · $11–17K · https://i.imgur.com/RMJrcaf.jpg
- Alt 2: Rolex Submariner Hulk 116610LV · $11–17K · https://i.imgur.com/bLQLOff.jpg

---

### S9 (Age 44) — Rolex Day-Date
Ref: 18038 · Era: 1977–1988 · Full yellow gold · Presidential bracelet
Dial: Champagne/gold (primary) · Budget: $15–22K
Role: The statement. Full yellow gold Presidential. Cultural weight and legacy.
Tags: VINTAGE · DRESS	mage: https://i.imgur.com/2ozRGG4.jpg
Alternates:
- Alt 1: Black dial 18038 · $15–22K · https://i.imgur.com/YeJ9DOB.jpg
- Alt 2: Blue dial 18038 · $15–22K · Dial originality must be verified — aftermarket blue dials are extremely common. Do not accept any example without confirmed provenance. · https://i.imgur.com/U9HPEm4.jpg

---

### S10 (Age 45) z� Rolex GMT Master 1675
Ref: 1675 · Era: ~1968 target · Gilt dial just starting to patina · Budget: $18–28K
Role: The grail. Pan Am pilot navigation instrument. Aviation bookend to S4 Navitimer.
Tags: VINTAGE · SPORT
Note on card: "Target 1968 examples. Gilt dial, unpolished case, no bracelet sag. The patina story is just beginning."
Image: https://i.imgur.com/IvmHdl2.jpg
Alternates:
- Alt 1: IWC Portugieser Perpetual Calendar · black Arabic dial · steel · $14–22K · MODERN · DRESS · Note: "True perpetual calendar. Only needs correction February 29 every 4 years." · https://i.imgur.com/lyzMe25.jpg
- Alt 2: Breitling Navitimer 806 AOPA@· gilt dial · $5–10K · VINTAGE · CHRONO · Note: "Narrative bookend to S4 Navitimer. The watch that established the gilt dial taste signal." · https://i.imgur.com/seEZt3H.jpg

---

## Section D — File Ownership

| File | Owner | Location | Read Path |
|---|---|---|---|
| `CLAUDE.md` | Split | In repo | Code: local. Chat: Drive. |
| `index.html` | Code | In repo | Code: local. Chat: Drive. |
| `10springs-strategy-v2.md` | Chat | Drive only (Claude Stuff > 10 springs) | Chat: Drive. Code: never. |
| `10springsimagetracker.xlsx` | Chat | Drive only (Claude Stuff > 10 springs) | Chat: Drive. Code: never. |
| `_prototypes/*` | Code | In repo | Code: local. Chat: Drive. |
| `embed_images.py` | Code | In repo | Code: local. |

*Only declared owner writes. Code never regenerates Chat-owned content. If a task would require touching a Chat-owned file, stop and flag it.*

---

## Section E — Code Conventions
*Both contribute. Promoted from Section B.*

**Large file writes (index.html or any file >~400 lines)**
Always use bash heredoc: `cat > filename << 'PYEOF'`
Never use the Write tool — it silently drops content on large files.

**After any commit**
Run `git diff HEAD~1` and verify changes match what was intended before moving to the next task.

**Python script writes**
Verify the file actually landed on disk after any Python script runs. Silent failure is possible.

**Image URLs**
Always use direct imgur format: `https://i.imgur.com/XXXXXXX.jpg`
Never use the page URL format: `https://imgur.com/XXXXXXX`

**CSS image-rendering**
`image-rendering: high-quality` required on all card images to prevent GPU compositing pixelation.

**Lightbox DOM order**
Lightbox HTML must appear in the DOM before the script that references it.

**Branch and PR**
```
git checkout -b claude/your-description-here
git push -u origin claude/your-description-here
```
One branch per task. Never push to main directly. After committing, provide this PR merge link format:
```
https://github.com/JoelColeman/10-springs/compare/main...claude/YOUR-BRANCH-NAME
```

**Loop-stop rule**
If retrying the same approach more than twice: stop and report what's blocking rather than continuing to loop.

**Prototype references**
Read `_prototypes/dashboard-mockup.html` and `_prototypes/card-fan-v2.html` for design system and animation specs before building. Do not rebuild from scratch.

**Drive connector file size**
index.html is ~100KB. Drive connector returns it successfully. Note any limits encountered with larger files.
