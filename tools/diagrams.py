"""Tiny SVG diagram kit for economics decks.
Data space is 0..10 on both axes; colours come from CSS classes so diagrams follow the theme."""

W, H = 320, 250
OX, OY = 46, 214          # origin in px
PW, PH = 256, 190         # plot width/height in px


def px(x):
    return OX + x / 10 * PW


def py(y):
    return OY - y / 10 * PH


class Fig:
    def __init__(self, xl="Quantity", yl="Price", aria="diagram", xsym="Q", ysym="P", origin=True):
        self.parts = []
        self.aria = aria
        self.xl, self.yl, self.xsym, self.ysym = xl, yl, xsym, ysym
        self.origin = origin

    # ---- primitives -------------------------------------------------
    def line(self, a, b, cls="d", label=None, at="b", off=(5, -4), anchor="start"):
        self.parts.append(f'<line class="k {cls}" x1="{px(a[0]):.1f}" y1="{py(a[1]):.1f}" x2="{px(b[0]):.1f}" y2="{py(b[1]):.1f}"/>')
        if label:
            p = b if at == "b" else a
            self.text(p, label, cls="t-" + cls.split()[0], off=off, anchor=anchor)
        return self

    def path(self, pts, cls="d", label=None, off=(5, -4), anchor="start"):
        d = "M" + " L".join(f"{px(x):.1f},{py(y):.1f}" for x, y in pts)
        self.parts.append(f'<path class="k {cls}" d="{d}"/>')
        if label:
            self.text(pts[-1], label, cls="t-" + cls.split()[0], off=off, anchor=anchor)
        return self

    def curve(self, f, x0, x1, cls="d", label=None, n=40, off=(5, -4), anchor="start", lab_at="end"):
        pts = [(x0 + (x1 - x0) * i / n, f(x0 + (x1 - x0) * i / n)) for i in range(n + 1)]
        d = "M" + " L".join(f"{px(x):.1f},{py(y):.1f}" for x, y in pts)
        self.parts.append(f'<path class="k {cls}" d="{d}"/>')
        if label:
            p = pts[-1] if lab_at == "end" else pts[0]
            self.text(p, label, cls="t-" + cls.split()[0], off=off, anchor=anchor)
        return self

    def poly(self, pts, cls="fa"):
        d = " ".join(f"{px(x):.1f},{py(y):.1f}" for x, y in pts)
        self.parts.append(f'<polygon class="{cls}" points="{d}"/>')
        return self

    def guide(self, p, xt=None, yt=None):
        x, y = p
        self.parts.append(f'<path class="g" d="M{px(x):.1f},{py(y):.1f} L{px(x):.1f},{OY} M{px(x):.1f},{py(y):.1f} L{OX},{py(y):.1f}"/>')
        if xt:
            self.parts.append(f'<text class="t-ax" x="{px(x):.1f}" y="{OY + 15}" text-anchor="middle">{xt}</text>')
        if yt:
            self.parts.append(f'<text class="t-ax" x="{OX - 6}" y="{py(y) + 4:.1f}" text-anchor="end">{yt}</text>')
        return self

    def pt(self, p, label=None, off=(6, -6), anchor="start", hollow=False):
        cls = "pto" if hollow else "pt"
        self.parts.append(f'<circle class="{cls}" cx="{px(p[0]):.1f}" cy="{py(p[1]):.1f}" r="3.6"/>')
        if label:
            self.text(p, label, cls="t-pt", off=off, anchor=anchor)
        return self

    def text(self, p, s, cls="t-sm", off=(0, 0), anchor="start"):
        self.parts.append(f'<text class="{cls}" x="{px(p[0]) + off[0]:.1f}" y="{py(p[1]) + off[1]:.1f}" text-anchor="{anchor}">{s}</text>')
        return self

    def arrow(self, a, b, cls="ar"):
        self.parts.append(f'<line class="{cls}" x1="{px(a[0]):.1f}" y1="{py(a[1]):.1f}" x2="{px(b[0]):.1f}" y2="{py(b[1]):.1f}" marker-end="url(#ah)"/>')
        return self

    # ---- output -----------------------------------------------------
    def svg(self):
        ax = (f'<path class="ax" d="M{OX},{OY - PH - 12} L{OX},{OY} L{OX + PW + 12},{OY}"/>'
              f'<text class="t-axl" x="{OX - 6}" y="{OY - PH - 16}" text-anchor="start">{self.yl}</text>'
              f'<text class="t-axl" x="{OX + PW + 12}" y="{OY + 30}" text-anchor="end">{self.xl}</text>')
        if self.origin:
            ax += f'<text class="t-ax" x="{OX - 6}" y="{OY + 15}" text-anchor="end">O</text>'
        defs = ('<defs><marker id="ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
                '<path class="arh" d="M0,0 L10,5 L0,10 z"/></marker></defs>')
        return (f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="{self.aria}">{defs}'
                + "".join(self.parts) + ax + "</svg>")


def fig(*figs, caption=None):
    """Wrap one or more Fig objects (or (title, Fig) tuples) into a figure block."""
    panels = []
    for f in figs:
        if isinstance(f, tuple):
            t, f = f
            panels.append(f'<div class="pnl"><p class="ptitle">{t}</p>{f.svg()}</div>')
        else:
            panels.append(f'<div class="pnl">{f.svg()}</div>')
    cap = f"<figcaption>{caption}</figcaption>" if caption else ""
    return f'<figure class="dg{" multi" if len(figs) > 1 else ""}">{"".join(panels)}{cap}</figure>'


def line_xy(a, b):
    """Return f(x) for the straight line through a and b."""
    m = (b[1] - a[1]) / (b[0] - a[0])
    return lambda x: a[1] + m * (x - a[0])


def inter(a1, b1, a2, b2):
    (x1, y1), (x2, y2), (x3, y3), (x4, y4) = a1, b1, a2, b2
    d = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / d
    return (x1 + t * (x2 - x1), y1 + t * (y2 - y1))
