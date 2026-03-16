#!/usr/bin/env python3
"""
embed_images.py — Downloads one watch photo per slot, compresses it,
base64-encodes it, and patches it into index.html in-place.
"""

import subprocess, sys

print("Installing deps…")
for pkg in ["Pillow", "duckduckgo-search", "requests"]:
    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", "-q", pkg],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )

import base64, re, time
from io import BytesIO
from pathlib import Path

import requests
from PIL import Image, UnidentifiedImageError

try:
    from duckduckgo_search import DDGS
    HAS_DDG = True
except Exception:
    HAS_DDG = False
    print("  duckduckgo_search unavailable — will use Wikimedia only")

# ── watch table ─────────────────────────────────────────────────────────────
# (slot, display_name in onclick, ddg query, wikimedia query)
WATCHES = [
    ("H1",
     "Caravelle manual wind",
     "Caravelle Bulova manual wind 1950s vintage watch dial",
     "Caravelle watch 1950s manual wind"),
    ("H2",
     "Bulova Accutron Spaceview",
     "Bulova Accutron Spaceview 214 tuning fork vintage watch",
     "Bulova Accutron Spaceview"),
    ("Now",
     "Longines Sport Chief ref 7042",
     "Longines Sport Chief 7042 vintage cream dial 1950s watch",
     "Longines Sport Chief 7042"),
    ("S1",
     "Omega Seamaster ref 166.010",
     "Omega Seamaster 166.010 crosshair dial vintage 1964",
     "Omega Seamaster 166.010"),
    ("S2",
     "Longines Flagship 18k ref 3410",
     "Longines Flagship 3410 18k gold case vintage 1960s watch",
     "Longines Flagship gold 3410"),
    ("S3",
     "Universal Genève Polerouter ref 20217",
     "Universal Geneve Polerouter 20217 tropical brown dial vintage",
     "Universal Geneve Polerouter"),
    ("S4",
     "Zenith El Primero ref A386",
     "Zenith El Primero A386 black dial chronograph 1969",
     "Zenith El Primero A386"),
    ("S5",
     "Rolex Datejust ref 1601",
     "Rolex Datejust 1601 black pie pan dial fluted bezel vintage",
     "Rolex Datejust 1601"),
    ("S6",
     "Omega Speedmaster Professional ref 3570.50",
     "Omega Speedmaster Professional 3570.50 moonwatch black dial",
     "Omega Speedmaster Professional"),
    ("S7",
     "Rolex Submariner Hulk 116610LV",
     "Rolex Submariner Hulk 116610LV green ceramic bezel dial",
     "Rolex Submariner green Hulk"),
    ("S8",
     "JLC Master Ultra Thin Moon Q1368430",
     "Jaeger-LeCoultre Master Ultra Thin Moon silver dial moonphase",
     "Jaeger LeCoultre Master Ultra Thin Moon"),
    ("S9",
     "Rolex Day-Date 18038 yellow gold",
     "Rolex Day-Date 18038 yellow gold champagne dial president bracelet",
     "Rolex Day-Date yellow gold president"),
    ("S10",
     "Rolex GMT-Master ref 1675 Pepsi",
     "Rolex GMT-Master 1675 Pepsi red blue bezel vintage black dial",
     "Rolex GMT-Master 1675 Pepsi"),
]

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/123.0.0.0 Safari/537.36"
    ),
    "Accept": "image/webp,image/apng,image/*,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.google.com/",
}


# ── search helpers ───────────────────────────────────────────────────────────

def search_ddg(query, n=8):
    if not HAS_DDG:
        return []
    urls = []
    try:
        with DDGS() as d:
            for r in d.images(keywords=query, max_results=n, safesearch="moderate"):
                u = r.get("image", "")
                if u:
                    urls.append(u)
    except Exception as e:
        print(f"    DDG error: {e}")
    return urls


def search_wikimedia(query, thumb_w=400):
    params = {
        "action": "query", "generator": "search", "gsrnamespace": 6,
        "gsrsearch": query, "gsrlimit": 10,
        "prop": "imageinfo", "iiprop": "url|mime|size",
        "iiurlwidth": thumb_w, "format": "json",
    }
    urls = []
    try:
        r = requests.get(
            "https://commons.wikimedia.org/w/api.php",
            params=params, timeout=12,
            headers={"User-Agent": "WatchDashboard/1.0 (personal project)"},
        )
        pages = r.json().get("query", {}).get("pages", {})
        for page in pages.values():
            info = page.get("imageinfo", [])
            if not info:
                continue
            mime = info[0].get("mime", "")
            if mime in ("image/jpeg", "image/png", "image/webp"):
                u = info[0].get("thumburl") or info[0].get("url")
                if u:
                    urls.append(u)
    except Exception as e:
        print(f"    Wikimedia error: {e}")
    return urls


# ── download + encode ────────────────────────────────────────────────────────

def fetch_bytes(url, max_bytes=8_000_000):
    try:
        r = requests.get(url, headers=HEADERS, timeout=20, stream=True)
        r.raise_for_status()
        chunks, total = [], 0
        for chunk in r.iter_content(8192):
            chunks.append(chunk)
            total += len(chunk)
            if total > max_bytes:
                break
        return b"".join(chunks)
    except Exception as e:
        print(f"    fetch: {e}")
        return None


def to_b64_jpeg(data, max_dim=(240, 300), quality=72):
    try:
        img = Image.open(BytesIO(data))
        # handle animated GIF/WebP — take first frame
        if hasattr(img, "n_frames") and img.n_frames > 1:
            img.seek(0)
        img = img.convert("RGB")
        img.thumbnail(max_dim, Image.LANCZOS)
        out = BytesIO()
        img.save(out, "JPEG", quality=quality, optimize=True)
        return base64.b64encode(out.getvalue()).decode("ascii")
    except (UnidentifiedImageError, Exception) as e:
        print(f"    encode: {e}")
        return None


def get_image_b64(ddg_q, wiki_q):
    """Try DDG then Wikimedia; return first successful base64 string."""
    candidate_urls = search_ddg(ddg_q) + search_wikimedia(wiki_q)
    for url in candidate_urls:
        print(f"    trying {url[:72]}…")
        data = fetch_bytes(url)
        if not data:
            continue
        b64 = to_b64_jpeg(data)
        if b64:
            return b64
        time.sleep(0.3)
    return None


# ── HTML patching ────────────────────────────────────────────────────────────

IMG_CSS = """
/* ── embedded watch photos ───────────────────────────────────────────── */
.watch-img-btn img, .img-btn img {
  width:100%; height:100%; object-fit:cover; display:block;
  opacity:.82; transition:opacity .15s;
}
.watch-img-btn:hover img, .img-btn:hover img { opacity:1; }
.watch-img-btn, .img-btn { padding:0 !important; overflow:hidden; }
"""


def patch_button(html, display_name, b64):
    """Replace the content of the matching <button> with an <img> tag."""
    esc = re.escape(display_name)
    # Match opening tag through to </button>
    pat = (
        rf'(<button\s[^>]*onclick="searchPhoto\(\'{esc}\'[^"]*\)"[^>]*>)'
        rf'.*?'
        rf'(</button>)'
    )
    img_tag = (
        f'<img src="data:image/jpeg;base64,{b64}" '
        f'alt="{display_name}" '
        f'style="width:100%;height:100%;object-fit:cover;display:block;">'
    )
    new_html, n = re.subn(pat, rf"\1{img_tag}\2", html, count=1, flags=re.DOTALL)
    return new_html, n > 0


# ── main ─────────────────────────────────────────────────────────────────────

html_path = Path(__file__).parent / "index.html"
html = html_path.read_text(encoding="utf-8")

ok, fail = 0, 0
for slot, display_name, ddg_q, wiki_q in WATCHES:
    print(f"\n[{slot}] {display_name}")

    b64 = get_image_b64(ddg_q, wiki_q)
    if not b64:
        print(f"  ✗ no image found — keeping placeholder")
        fail += 1
        time.sleep(1)
        continue

    html, matched = patch_button(html, display_name, b64)
    if matched:
        kb = len(b64) * 3 // 4 // 1024
        print(f"  ✓ embedded ~{kb} KB")
        ok += 1
    else:
        print(f"  ✗ button pattern not matched in HTML")
        fail += 1

    time.sleep(1.0)  # be polite to sources

# Inject CSS (once, before closing </style>)
if IMG_CSS.strip() not in html:
    html = html.replace("</style>", IMG_CSS + "</style>", 1)

html_path.write_text(html, encoding="utf-8")
total_kb = len(html) // 1024
print(f"\n{'─'*60}")
print(f"Done — {ok} embedded, {fail} failed")
print(f"index.html is now {total_kb} KB")
