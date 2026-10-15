"""Package the Revision Hub and decks as an installable, offline web app (PWA).
Usage: python3 app_build.py <mathjax tex-svg.js path>
Output: ./revision-app/ and ./revision-app.zip"""
import re, sys, shutil, pathlib, json, zipfile, hashlib
from PIL import Image, ImageDraw

SRC = pathlib.Path(__file__).parent
OUT = SRC / "revision-app"
HUB_URL = "https://claude.ai/artifact/3MqyaRKgJG7ufb65fwrnoF"
DECKS = {  # published artifact URL -> local file in the app
    "https://claude.ai/artifact/AC3snqSYwMhtcpnhAYTv98": ("deck-econ-ch1.html", "econ-ch1.html"),
    "https://claude.ai/artifact/HdT6C7aKQLs4S4wVd3Pp4f": ("deck-econ-ch2.html", "econ-ch2.html"),
    "https://claude.ai/code/artifact/31acac57-ce47-4e2f-9fb6-be4a409e475c": ("deck-econ-essays.html", "econ-essays.html"),
}
# decks that live only in the app (no separate artifact): built file -> local file; the hub links to the local file directly
APP_DECKS = {
    "deck-econ-essaybank.html": "econ-essay-bank.html",
    "deck-maths-p4.html": "maths-p4.html",
}

TIMER = SRC / "data/timer-source.html"
TIMER_URL = "https://claude.ai/code/artifact/f3cef93e-1ff7-49d0-8358-6c072def1db6"

REG_SNIPPET = "<script>if('serviceWorker' in navigator){navigator.serviceWorker.register('sw.js',{updateViaCache:'none'}).then(function(r){document.addEventListener('visibilitychange',function(){if(document.visibilityState==='visible')r.update().catch(function(){});});}).catch(function(){});var had=!!navigator.serviceWorker.controller,done=false;navigator.serviceWorker.addEventListener('controllerchange',function(){if(had&&!done){done=true;location.reload();}});}</script>"

HEAD = """<!doctype html>
<html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<link rel="manifest" href="manifest.webmanifest">
<link rel="apple-touch-icon" href="icon-180.png">
<link rel="icon" type="image/png" href="icon-192.png">
<style>:root{box-sizing:border-box;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}</style>
</head><body>
"""
TAIL = """
<script>if('serviceWorker' in navigator){navigator.serviceWorker.register('sw.js',{updateViaCache:'none'}).then(function(r){document.addEventListener('visibilitychange',function(){if(document.visibilityState==='visible')r.update().catch(function(){});});}).catch(function(){});var had=!!navigator.serviceWorker.controller,done=false;navigator.serviceWorker.addEventListener('controllerchange',function(){if(had&&!done){done=true;location.reload();}});}</script>
</body></html>
"""


def page(html):
    return HEAD + html + TAIL


def make_icon(size, path):
    """Three stacked revision cards in the subject colours on the app's dark ground."""
    s = size / 512
    im = Image.new("RGB", (size, size), "#11151C")
    d = ImageDraw.Draw(im)
    cards = [("#7FA8F5", 150, 92), ("#5CC6BF", 120, 132), ("#F0B44A", 90, 172)]
    for col, x, y in cards:
        d.rounded_rectangle([x * s, y * s, (x + 270) * s, (y + 220) * s], radius=34 * s, fill=col)
        d.rounded_rectangle([(x + 34) * s, (y + 46) * s, (x + 200) * s, (y + 66) * s], radius=10 * s, fill="#11151C")
    x, y = 90, 172
    for i, w in enumerate((150, 120, 170)):
        d.rounded_rectangle([(x + 34) * s, (y + 100 + i * 34) * s, (x + 34 + w) * s, (y + 116 + i * 34) * s], radius=8 * s, fill="#3A2D12")
    im.save(path)


def main(mathjax):
    mj = pathlib.Path(SRC / "revision-app.mathjax.tmp"); shutil.copy(mathjax, mj)
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "mathjax").mkdir(parents=True)
    shutil.move(mj, OUT / "mathjax" / "tex-svg.js")

    # hub: deck links stay inside the app; drop the "add to home screen" box (it's already installed)
    hub = (SRC / "revision-hub.html").read_text(encoding="utf8")
    for url, (_, local) in DECKS.items():
        hub = hub.replace(f'href="{url}" target="_blank" rel="noopener"', f'href="{local}"')
    hub = re.sub(r'\s*<div class="install">.*?</div>\n', "\n", hub, flags=re.S)
    hub = hub.replace('<p class="sub">A-Level · Econ · Phys · Maths · FM</p>',
                      '<p class="sub">A-Level · Econ · Phys · Maths · FM · works offline</p>')
    (OUT / "index.html").write_text(page(hub), encoding="utf8")

    for url, (src, local) in list(DECKS.items()) + [(None, v) for v in APP_DECKS.items()]:
        h = (SRC / src).read_text(encoding="utf8")
        h = h.replace(f'href="{HUB_URL}" target="_blank" rel="noopener">Open Revision Hub', 'href="index.html">← Back to Revision Hub')
        h = h.replace("https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.2/es5/tex-svg.js", "mathjax/tex-svg.js")
        (OUT / local).write_text(page(h), encoding="utf8")

    # in-app home button on every deck (standalone apps have no browser back button)
    home = ('<a class="ib" href="index.html" aria-label="Revision Hub"><svg viewBox="0 0 24 24">'
            '<path d="M4 11l8-7 8 7M6 9.5V20h12V9.5"/></svg></a>')
    for local in [l for _, l in DECKS.values()] + list(APP_DECKS.values()):
        p = OUT / local
        p.write_text(p.read_text(encoding="utf8").replace('<button class="ib" id="tocBtn"', home + '<button class="ib" id="tocBtn"', 1), encoding="utf8")

    # Exam Timer: copied from its artifact so it runs offline inside the app
    if TIMER and pathlib.Path(TIMER).exists():
        t = pathlib.Path(TIMER).read_text(encoding="utf8")
        t = t.replace("</head>", '<link rel="manifest" href="manifest.webmanifest"><link rel="apple-touch-icon" href="icon-180.png"></head>', 1)
        t = t.replace('<div><span class="eyebrow" id="subjectCode">',
                      '<div><a href="index.html" style="display:inline-block;font-weight:700;color:var(--accent);text-decoration:none;padding:6px 0;margin-bottom:4px">← Revision Hub</a><br><span class="eyebrow" id="subjectCode">', 1)
        t = t.replace("</body>", "<script>if('serviceWorker' in navigator){navigator.serviceWorker.register('sw.js',{updateViaCache:'none'}).then(function(r){document.addEventListener('visibilitychange',function(){if(document.visibilityState==='visible')r.update().catch(function(){});});}).catch(function(){});var had=!!navigator.serviceWorker.controller,done=false;navigator.serviceWorker.addEventListener('controllerchange',function(){if(had&&!done){done=true;location.reload();}});}</script></body>", 1)
        (OUT / "timer.html").write_text(t, encoding="utf8")
        h = (OUT / "index.html").read_text(encoding="utf8")
        h = h.replace(f'href="{TIMER_URL}" target="_blank" rel="noopener"', 'href="timer.html"')
        h = h.replace("Timed past-paper sessions", "Timed past-paper sessions · works offline")
        (OUT / "index.html").write_text(h, encoding="utf8")

    (OUT / ".nojekyll").write_text("", encoding="utf8")

    for n in (180, 192, 512):
        make_icon(n, OUT / f"icon-{n}.png")

    manifest = {
        "name": "Revision Hub", "short_name": "Revision", "start_url": "./index.html", "scope": "./",
        "display": "standalone", "orientation": "any", "background_color": "#11151C", "theme_color": "#11151C",
        "icons": [{"src": "icon-192.png", "sizes": "192x192", "type": "image/png"},
                  {"src": "icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any maskable"}],
    }
    (OUT / "manifest.webmanifest").write_text(json.dumps(manifest, indent=2), encoding="utf8")

    files = sorted(str(p.relative_to(OUT)) for p in OUT.rglob("*") if p.is_file() and not p.name.startswith("."))
    ver = hashlib.sha1(b"".join((OUT / f).read_bytes() for f in files)).hexdigest()[:10]
    sw = f"""// Pages (HTML): network first, so new decks show as soon as you're online; cached copy when offline.
// Everything else (maths renderer, icons, fonts): cache first.
const CACHE = 'revision-{ver}';
const FILES = {json.dumps(['./'] + files)};
self.addEventListener('install', e => {{ e.waitUntil(caches.open(CACHE).then(c => c.addAll(FILES.map(f => new Request(f, {{cache: 'reload'}})))).then(() => self.skipWaiting())); }});
self.addEventListener('activate', e => {{ e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== CACHE).map(k => caches.delete(k)))).then(() => self.clients.claim())); }});
const keep = (req, res) => {{ if (res.ok || res.type === 'opaque') {{ const copy = res.clone(); caches.open(CACHE).then(c => c.put(req, copy)); }} return res; }};
self.addEventListener('fetch', e => {{
  const req = e.request; if (req.method !== 'GET') return;
  const u = new URL(req.url), same = u.origin === location.origin;
  const page = req.mode === 'navigate' || (same && (u.pathname.endsWith('.html') || u.pathname.endsWith('/')));
  if (page) {{
    e.respondWith(fetch(req, {{cache: 'no-cache'}}).then(res => keep(req, res))
      .catch(() => caches.match(req, {{ignoreSearch: true}}).then(hit => hit || caches.match('./index.html'))));
    return;
  }}
  if (!same && !/fonts\\.(googleapis|gstatic)\\.com$/.test(u.hostname)) return;
  e.respondWith(caches.match(req, {{ignoreSearch: true}}).then(hit => hit || fetch(req).then(res => keep(req, res))));
}});
"""
    (OUT / "sw.js").write_text(sw, encoding="utf8")

    z = SRC / "revision-app.zip"
    with zipfile.ZipFile(z, "w", zipfile.ZIP_DEFLATED) as zf:
        for p in sorted(OUT.rglob("*")):
            if p.is_file():
                zf.write(p, "revision-app/" + str(p.relative_to(OUT)))
    print("built", len(files) + 1, "files;", z.stat().st_size, "bytes zipped; cache", ver)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else SRC.parent / "mathjax/tex-svg.js")
