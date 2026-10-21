// Pages (HTML): network first, so new decks show as soon as you're online; cached copy when offline.
// Everything else (maths renderer, icons, fonts): cache first.
const CACHE = 'revision-ebe0199d95';
const FILES = ["./", "econ-ch1.html", "econ-ch2.html", "econ-essay-bank.html", "econ-essays.html", "icon-180.png", "icon-192.png", "icon-512.png", "index.html", "manifest.webmanifest", "mathjax/tex-svg.js", "maths-p4.html", "phys-defs.html", "phys-graphs.html", "timer.html"];
self.addEventListener('install', e => { e.waitUntil(caches.open(CACHE).then(c => c.addAll(FILES.map(f => new Request(f, {cache: 'reload'})))).then(() => self.skipWaiting())); });
self.addEventListener('activate', e => { e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== CACHE).map(k => caches.delete(k)))).then(() => self.clients.claim())); });
const keep = (req, res) => { if (res.ok || res.type === 'opaque') { const copy = res.clone(); caches.open(CACHE).then(c => c.put(req, copy)); } return res; };
self.addEventListener('fetch', e => {
  const req = e.request; if (req.method !== 'GET') return;
  const u = new URL(req.url), same = u.origin === location.origin;
  const page = req.mode === 'navigate' || (same && (u.pathname.endsWith('.html') || u.pathname.endsWith('/')));
  if (page) {
    e.respondWith(fetch(req, {cache: 'no-cache'}).then(res => keep(req, res))
      .catch(() => caches.match(req, {ignoreSearch: true}).then(hit => hit || caches.match('./index.html'))));
    return;
  }
  if (!same && !/fonts\.(googleapis|gstatic)\.com$/.test(u.hostname)) return;
  e.respondWith(caches.match(req, {ignoreSearch: true}).then(hit => hit || fetch(req).then(res => keep(req, res))));
});
