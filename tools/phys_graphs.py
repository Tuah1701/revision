"""9702 Physics · Graphs deck: every AS graph from Kinematics to Work, energy & power
(kinematics, free fall, projectiles, air resistance & motion in fluids, dynamics/momentum,
pressure & upthrust, work-energy-power). Cambridge notation, g = 9.81 m s⁻², answers to 2-3 s.f."""
import math, pathlib
import engine
from engine import card
from diagrams import fig

HERE = pathlib.Path(__file__).parent
G = 9.81

DEFS = ('<defs><marker id="gh" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
        '<path class="arh" d="M0,0 L10,5 L0,10 z"/></marker></defs>')


class Plot:
    """Small graph panel. Axes cross at (0, 0); y range may go negative (axis then sits mid-panel)."""

    def __init__(self, xr=(0, 10), yr=(0, 10), xl="t", yl="v", aria="graph", w=300, h=200, L=34, R=16, T=24, B=24, dn=None):
        self.dn = dn
        self.x0, self.x1 = xr
        self.y0, self.y1 = yr
        self.xl, self.yl, self.aria = xl, yl, aria
        self.w, self.h, self.L, self.R, self.T, self.B = w, h, L, R, T, B
        self.parts = []

    def X(self, x):
        return self.L + (x - self.x0) / (self.x1 - self.x0) * (self.w - self.L - self.R)

    def Y(self, y):
        return self.T + (self.y1 - y) / (self.y1 - self.y0) * (self.h - self.T - self.B)

    def _d(self, pts):
        return "M" + " L".join(f"{self.X(x):.1f},{self.Y(y):.1f}" for x, y in pts)

    def path(self, pts, cls="d"):
        self.parts.append(f'<path class="k {cls}" d="{self._d(pts)}"/>')
        return self

    def curve(self, f, a, b, cls="d", n=60):
        return self.path([(a + (b - a) * i / n, f(a + (b - a) * i / n)) for i in range(n + 1)], cls)

    def fill(self, pts, cls="fb"):
        self.parts.append(f'<polygon class="{cls}" points="' + " ".join(f"{self.X(x):.1f},{self.Y(y):.1f}" for x, y in pts) + '"/>')
        return self

    def area(self, f, a, b, cls="fb", n=60):
        pts = [(a, 0)] + [(a + (b - a) * i / n, f(a + (b - a) * i / n)) for i in range(n + 1)] + [(b, 0)]
        return self.fill(pts, cls)

    def guide(self, pts):
        self.parts.append(f'<path class="g" d="{self._d(pts)}"/>')
        return self

    def vg(self, x, y, lab=None):
        self.guide([(x, y), (x, 0)])
        if lab:
            self.t(x, 0, lab, "t-ax", 0, 14 if y >= 0 else -6, "middle")
        return self

    def hg(self, x, y, lab=None):
        self.guide([(x, y), (0, y)])
        if lab:
            self.t(0, y, lab, "t-ax", -5, 4, "end")
        return self

    def t(self, x, y, s, cls="t-sm", dx=0, dy=0, anchor="start"):
        self.parts.append(f'<text class="{cls}" x="{self.X(x) + dx:.1f}" y="{self.Y(y) + dy:.1f}" text-anchor="{anchor}">{s}</text>')
        return self

    def pt(self, x, y, hollow=False):
        self.parts.append(f'<circle class="{"pto" if hollow else "pt"}" cx="{self.X(x):.1f}" cy="{self.Y(y):.1f}" r="3.4"/>')
        return self

    def arrow(self, a, b):
        self.parts.append(f'<line class="ar" x1="{self.X(a[0]):.1f}" y1="{self.Y(a[1]):.1f}" x2="{self.X(b[0]):.1f}" y2="{self.Y(b[1]):.1f}" marker-end="url(#gh)"/>')
        return self

    def svg(self):
        ax0, ay0 = self.X(0), self.Y(0)
        ax = (f'<path class="ax" d="M{ax0:.1f},{self.T - 8} L{ax0:.1f},{self.h - self.B + (6 if self.y0 < 0 else 0):.1f}"/>'
              f'<path class="ax" d="M{ax0:.1f},{ay0:.1f} L{self.w - self.R + 8:.1f},{ay0:.1f}"/>'
              f'<text class="t-axl" x="{ax0 + 5:.1f}" y="{self.T - 10}" text-anchor="start">{self.yl}</text>'
              f'<text class="t-axl" x="{self.w - 4:.1f}" y="{ay0 + (16 if self.y0 >= 0 else -6):.1f}" text-anchor="end">{self.xl}</text>'
              f'<text class="t-ax" x="{ax0 - 5:.1f}" y="{ay0 + 14:.1f}" text-anchor="end">0</text>')
        if self.dn:
            ax += f'<text class="t-dn" x="{self.w - 6}" y="15" text-anchor="end" style="font-size:10.5px;font-weight:700;fill:var(--teal)">{self.dn}</text>'
        return (f'<svg viewBox="0 0 {self.w} {self.h}" role="img" aria-label="{self.aria}">{DEFS}'
                + "".join(self.parts) + ax + "</svg>")


def tg(*marks):
    return "".join(f'<span class="tag">{m}</span>' for m in marks)


def rule(grad, area):
    return f'<div class="chain"><span>gradient = {grad}</span><span>area = {area}</span></div>'


# ---------------------------------------------------------------- diagrams
def st_shapes():
    a = Plot(dn="+ve → forward", yl="s", xl="t", aria="s-t at rest: horizontal line").path([(0, 5), (10, 5)]).t(5, 5, "at rest", "t-d", 0, -8, "middle")
    b = Plot(dn="+ve → forward", yl="s", xl="t", aria="s-t constant velocity: straight line").path([(0, 0), (10, 9)]).t(6, 4, "constant v", "t-d")
    c = Plot(dn="+ve → forward", yl="s", xl="t", aria="s-t accelerating: curve getting steeper").curve(lambda t: 0.09 * t * t, 0, 10).t(3.5, 6, "speeding up", "t-d")
    d = Plot(dn="+ve → forward", yl="s", xl="t", aria="s-t decelerating to rest: curve flattening").curve(lambda t: 9 - 0.09 * (10 - t) ** 2, 0, 10).t(5.5, 4, "slowing down", "t-d")
    return fig(("At rest", a), ("Constant velocity", b), ("Accelerating", c), ("Decelerating", d),
               caption="Steepness = speed. Straight = constant velocity; curving up = accelerating; flattening = decelerating.")


def st_tangent():
    p = Plot(dn="+ve → forward", yl="s / m", xl="t / s", aria="tangent drawn on a curved s-t graph")
    f = lambda t: 0.08 * t * t
    p.curve(f, 0, 10)
    t0 = 6
    m = 0.16 * t0
    p.path([(3, f(t0) + m * (3 - t0)), (9.5, f(t0) + m * (9.5 - t0))], "s")
    p.pt(t0, f(t0))
    p.guide([(4, f(t0) + m * (4 - t0)), (9, f(t0) + m * (4 - t0)), (9, f(t0) + m * (9 - t0))])
    p.t(6.5, f(t0) + m * (4 - t0) - 0.6, "Δt", "t-sm", 0, 0, "middle").t(9, 2.6, "Δs", "t-sm", 6, 0)
    p.t(3.2, 7.5, "tangent at t", "t-s")
    return fig(p, caption="Instantaneous velocity = gradient of the TANGENT. Draw a big triangle (over half the line) to cut reading error.")


def vt_shapes():
    a = Plot(dn="+ve → forward", aria="v-t constant velocity: horizontal line").path([(0, 6), (10, 6)]).t(5, 6, "a = 0", "t-d", 0, -8, "middle")
    b = Plot(dn="+ve → forward", aria="v-t uniform acceleration: straight line up").path([(0, 1), (10, 9)]).t(4, 6, "a constant", "t-d", 0, 0, "end")
    c = Plot(dn="+ve → forward", aria="v-t uniform deceleration: straight line down").path([(0, 9), (9, 0)]).t(5, 6.5, "a negative", "t-d")
    d = Plot(dn="+ve → forward", aria="v-t increasing acceleration: curve getting steeper").curve(lambda t: 0.09 * t * t, 0, 10).t(3, 6, "a increasing", "t-d")
    return fig(("Constant velocity", a), ("Uniform acceleration", b), ("Uniform deceleration", c), ("Increasing acceleration", d),
               caption="On v–t the slope is acceleration. Don't confuse a flat v–t (moving steadily) with a flat s–t (at rest).")


def vt_area():
    p = Plot(dn="+ve → initial direction", yr=(-5, 7), yl="v", xl="t", aria="v-t graph crossing the time axis, areas above and below")
    pts = [(0, 6), (5, 0), (8, -3.6), (10, -3.6)]
    p.fill([(0, 0), (0, 6), (5, 0)], "fb").fill([(5, 0), (8, -3.6), (10, -3.6), (10, 0)], "fc")
    p.path(pts)
    p.t(1.6, 2, "A₁ (+)", "t-pt").t(7.6, -1.6, "A₂ (−)", "t-pt", 0, 0, "middle")
    p.t(5, 0, "turns back", "t-sm", 4, -8)
    return fig(p, caption="Displacement = A₁ − A₂.  Distance = A₁ + A₂.  Velocity crosses zero = object momentarily at rest and reverses.")


def at_graph():
    p = Plot(dn="+ve → forward", yr=(-5, 5), yl="a", xl="t", aria="a-t graph: area equals change in velocity")
    p.fill([(0, 0), (0, 3), (4, 3), (4, 0)], "fb").fill([(7, 0), (7, -2.5), (10, -2.5), (10, 0)], "fc")
    p.path([(0, 3), (4, 3)]).path([(4, 0), (7, 0)]).path([(7, -2.5), (10, -2.5)])
    p.guide([(4, 3), (4, 0)]).guide([(7, 0), (7, -2.5)])
    p.t(2, 1.3, "Δv gained", "t-pt", 0, 0, "middle").t(8.5, -1.3, "Δv lost", "t-pt", 0, 0, "middle")
    p.t(5.5, 0, "steady v", "t-sm", 0, -6, "middle")
    return fig(p, caption="Area under a–t = change in velocity, not velocity itself. Add the initial velocity u.")


def changing_accel():
    F = "+ve → forward"
    a = Plot(dn=F, aria="v-t concave down rising curve: decreasing acceleration").curve(lambda t: 9 * (1 - (1 - t / 10) ** 2), 0, 10).t(5.5, 4, "slope falls", "t-d")
    b = Plot(dn=F, aria="v-t concave up rising curve: increasing acceleration").curve(lambda t: 0.09 * t * t, 0, 10).t(3, 6, "slope grows", "t-d")
    c = Plot(dn=F, aria="v-t falling curve getting steeper: increasing deceleration").curve(lambda t: 9 - 0.09 * t * t, 0, 10).t(1.5, 4, "slope more −ve", "t-d")
    d = Plot(dn=F, aria="v-t falling curve flattening: decreasing deceleration").curve(lambda t: 9 * (1 - t / 10) ** 2, 0, 10).t(4.5, 5, "slope less −ve", "t-d")
    return fig(("decreasing acceleration", a), ("increasing acceleration", b), ("increasing deceleration", c), ("decreasing deceleration", d),
               caption="Speeding up: v rises. Slowing down: v falls. Whether it's getting MORE or LESS so is read from how the gradient changes (steeper or flatter).")


def changing_accel_at():
    F = "+ve → forward"
    a = Plot(dn=F, yr=(-5, 5), yl="a", aria="a-t positive line falling to zero").path([(0, 4), (10, 0)]).t(1, 1.2, "a > 0, falling", "t-d")
    b = Plot(dn=F, yr=(-5, 5), yl="a", aria="a-t positive line rising").path([(0, 0), (10, 4)]).t(5, 3.2, "a > 0, rising", "t-d", 0, 0, "end")
    c = Plot(dn=F, yr=(-5, 5), yl="a", aria="a-t negative line becoming more negative").path([(0, 0), (10, -4)]).t(5, -3.2, "a < 0, more −ve", "t-d", 0, 0, "end")
    d = Plot(dn=F, yr=(-5, 5), yl="a", aria="a-t negative line rising towards zero").path([(0, -4), (10, 0)]).t(1, -1.2, "a < 0, → 0", "t-d")
    return fig(("decreasing acceleration", a), ("increasing acceleration", b), ("increasing deceleration", c), ("decreasing deceleration", d),
               caption="The matching a–t graphs (straight lines shown for simplicity). Deceleration = negative acceleration when forward is positive.")


def bounce_up():
    t1, t2 = 0.606, 0.404
    t3 = 2.6 / G
    v = Plot(dn="+ve ↑ up", xr=(0, 2.1), yr=(-7, 5), yl="v", xl="t", aria="bouncing ball velocity-time with up positive: lines slope downwards, jumps upward at each bounce")
    v.path([(0, 0), (t1, -5.94)]).guide([(t1, -5.94), (t1, 3.96)]).path([(t1, 3.96), (t1 + 2 * t2, -3.96)])
    v.guide([(t1 + 2 * t2, -3.96), (t1 + 2 * t2, 2.6)]).path([(t1 + 2 * t2, 2.6), (min(2.07, t1 + 2 * t2 + 2 * t3), -2.6 * (min(2.07, t1 + 2 * t2 + 2 * t3) - t1 - 2 * t2) / t3 + 2.6)])
    v.t(t1, 3.96, "bounce", "t-sm", 4, -4).t(0.06, -4.2, "falling: v < 0", "t-sm", 10)
    a = Plot(dn="+ve ↑ up", xr=(0, 2.1), yr=(-4, 9), yl="a", xl="t", aria="bouncing ball acceleration-time with up positive: constant minus g with large upward spikes at each bounce")
    a.path([(0, -2.6), (t1 - 0.02, -2.6), (t1, 8.4), (t1 + 0.02, -2.6), (t1 + 2 * t2 - 0.02, -2.6), (t1 + 2 * t2, 6.5), (t1 + 2 * t2 + 0.02, -2.6), (2.07, -2.6)])
    a.t(0, -2.6, "−g", "t-ax", -5, 4, "end").t(t1, 8.4, "huge upward a during contact", "t-sm", 6, 10)
    return fig(("velocity–time (up +)", v), ("acceleration–time (up +)", a),
               caption="Same motion, up positive: every free-flight line now slopes DOWN (gradient −g); each bounce is an upward jump from −v to a smaller +v.")


def air_liquid():
    D = "+ve ↓ down"
    a = Plot(dn=D, yr=(0, 10), yl="v", xl="t", aria="dropped through air then into liquid faster than terminal velocity: rises at g then decreases to v_T")
    a.path([(0, 0), (3, 7.5)]).curve(lambda t: 3 + 4.5 * math.exp(-(t - 3) / 0.9), 3, 10)
    a.guide([(3, 7.5), (3, 0)]).guide([(0, 3), (10, 3)]).hg(0, 3, "v_T").t(3, 0, "enters", "t-ax", 0, 14, "middle").t(0.2, 8.6, "air: slope g", "t-sm")
    b = Plot(dn=D, yr=(0, 10), yl="v", xl="t", aria="dropped from a small height: enters liquid slower than terminal velocity, then rises slowly to v_T")
    b.path([(0, 0), (1.2, 3)]).curve(lambda t: 5 - 2 * math.exp(-(t - 1.2) / 1.6), 1.2, 10)
    b.guide([(1.2, 3), (1.2, 0)]).guide([(0, 5), (10, 5)]).hg(0, 5, "v_T").t(1.2, 0, "enters", "t-ax", 0, 14, "middle").t(4, 3, "slope < g, falls to 0", "t-sm")
    c = Plot(dn=D, yr=(-8, 6), yl="a", xl="t", aria="acceleration: g in air, sudden negative on entry, decaying to zero")
    c.path([(0, 4), (3, 4)]).guide([(3, 4), (3, -6)]).curve(lambda t: -6 * math.exp(-(t - 3) / 0.9), 3, 10)
    c.hg(0, 4, "g").t(3.3, -6, "D + U > W: a upward", "t-sm", 4, 4)
    e = Plot(dn=D, yr=(-8, 6), yl="a", xl="t", aria="low drop acceleration: g in air, sudden fall to smaller positive value, decaying to zero")
    e.path([(0, 4), (1.2, 4)]).guide([(1.2, 4), (1.2, 2.2)]).curve(lambda t: 2.2 * math.exp(-(t - 1.2) / 1.6), 1.2, 10).hg(0, 4, "g")
    e.t(2.4, 2.2, "W > U + D: a down, < g", "t-sm")
    return fig(("enters faster than v_T (high drop)", a), ("enters slower than v_T (low drop)", b), ("a–t for the high drop", c), ("a–t for the low drop", e),
               caption="Air resistance in air neglected. In the liquid, upthrust and viscous drag act up; terminal when W = U + D. If it enters at exactly v_T the line just stays flat.")


def journey_trio():
    s = Plot(dn="+ve → forward", yl="s", xl="t", aria="journey s-t", h=170)
    def sf(t):
        if t <= 3: return 0.25 * t * t
        if t <= 7: return 2.25 + 1.5 * (t - 3)
        return 8.25 + 1.5 * (t - 7) - 0.25 * (t - 7) ** 2
    s.curve(sf, 0, 10).vg(3, sf(3)).vg(7, sf(7))
    v = Plot(dn="+ve → forward", yl="v", xl="t", aria="journey v-t", h=170).path([(0, 0), (3, 1.5 * 5), (7, 7.5), (10, 0)])
    v.vg(3, 7.5).vg(7, 7.5)
    a = Plot(dn="+ve → forward", yr=(-6, 6), yl="a", xl="t", aria="journey a-t", h=170)
    a.path([(0, 3), (3, 3)]).path([(3, 0), (7, 0)]).path([(7, -4), (10, -4)]).guide([(3, 3), (3, 0)]).guide([(7, 0), (7, -4)])
    return fig(("s–t", s), ("v–t", v), ("a–t", a),
               caption="One journey, three graphs: speed up, cruise, brake. Each graph is the gradient of the one above.")


def freefall():
    v = Plot(dn="+ve ↓ down", yl="v", xl="t", aria="free fall v-t straight line gradient g").path([(0, 0), (9, 9)]).t(6, 3.5, "gradient = g", "t-d")
    s = Plot(dn="+ve ↓ down", yl="s", xl="t", aria="free fall s-t parabola").curve(lambda t: 0.1 * t * t, 0, 9.5).t(2, 6, "s = ½gt²", "t-d")
    a = Plot(dn="+ve ↓ down", yl="a", xl="t", aria="free fall a-t horizontal line at g").path([(0, 7), (10, 7)]).hg(0, 7, "g").t(5, 7, "constant", "t-d", 0, -8, "middle")
    return fig(("v–t", v), ("s–t (distance fallen)", s), ("a–t", a),
               caption="Dropped from rest, no air resistance, down taken as positive.")


def thrown_up():
    v = Plot(dn="+ve ↑ up", yr=(-6, 6), yl="v", xl="t", aria="ball thrown up: v-t straight line from +u to -u").path([(0, 5), (10, -5)])
    v.hg(0, 5, "+u").t(0, -5, "−u", "t-ax", -5, 4, "end").guide([(10, -5), (0, -5)]).t(5, 0, "top", "t-sm", 3, -7)
    s = Plot(dn="+ve ↑ up", yl="s", xl="t", aria="ball thrown up: displacement-time inverted parabola").curve(lambda t: 0.36 * t * (10 - t), 0, 10)
    s.vg(5, 9, "top").t(5, 9, "gradient 0 at top", "t-sm", 0, -7, "middle")
    sp = Plot(dn="speed: scalar (no direction)", yl="speed", xl="t", aria="ball thrown up: speed-time V shape").path([(0, 9), (5, 0), (10, 9)]).t(5, 0, "speed 0", "t-sm", 0, 14, "middle")
    a = Plot(dn="+ve ↑ up", yr=(-6, 6), yl="a", xl="t", aria="ball thrown up: acceleration constant at -g").path([(0, -4), (10, -4)]).t(0, -4, "−g", "t-ax", -5, 4, "end")
    return fig(("velocity–time (up +)", v), ("displacement–time", s), ("speed–time", sp), ("acceleration–time", a),
               caption="Thrown up, caught at the same level. One straight v–t line through zero: the acceleration is −g the WHOLE time, including at the top.")


def bounce():
    t1, t2 = 0.606, 0.404
    v = Plot(dn="+ve ↓ down", xr=(0, 2.1), yr=(-5, 7), yl="v", xl="t", aria="bouncing ball velocity-time sawtooth, down positive")
    v.path([(0, 0), (t1, 5.94)]).guide([(t1, 5.94), (t1, -3.96)]).path([(t1, -3.96), (t1 + 2 * t2, 3.96)])
    v.guide([(t1 + 2 * t2, 3.96), (t1 + 2 * t2, -2.6)]).path([(t1 + 2 * t2, -2.6), (2.07, 2.6)])
    v.t(t1, -3.96, "bounce", "t-sm", 4, 12)
    h = Plot(dn="h measured up", xr=(0, 2.1), yr=(0, 2), yl="h", xl="t", aria="bouncing ball height-time series of parabolas")
    h.curve(lambda t: 1.8 - 0.5 * G * t * t, 0, t1)
    h.curve(lambda t: 3.96 * (t - t1) - 0.5 * G * (t - t1) ** 2, t1, t1 + 2 * t2)
    t3 = 2.6 / G
    h.curve(lambda t: 2.6 * (t - t1 - 2 * t2) - 0.5 * G * (t - t1 - 2 * t2) ** 2, t1 + 2 * t2, min(2.07, t1 + 2 * t2 + 2 * t3))
    return fig(("velocity–time", v), ("height–time", h),
               caption="Straight v–t lines all have gradient g (parallel). Each bounce: velocity flips sign and shrinks (KE lost), so peaks get lower.")


def projectile():
    vx = Plot(dn="+ve → forward", yr=(0, 10), yl="vₓ", xl="t", aria="projectile horizontal velocity constant").path([(0, 6), (10, 6)]).t(5, 6, "constant (no drag)", "t-d", 0, -8, "middle")
    vy = Plot(dn="+ve ↑ up", yr=(-6, 6), yl="v_y", xl="t", aria="projectile vertical velocity line gradient minus g").path([(0, 5), (10, -5)]).t(5, 0, "top: v_y = 0", "t-sm", 4, -8)
    tr = Plot(dn="x →, y ↑ up", yr=(0, 10), yl="y", xl="x", aria="projectile trajectory parabola with and without air resistance")
    tr.curve(lambda x: 0.36 * x * (10 - x), 0, 10, "d")
    tr.curve(lambda x: 13 * (x / 7) * (1 - (x / 7) ** 3), 0, 7, "o")
    tr.t(5, 9, "no drag: symmetric", "t-d", 0, -6, "middle").t(4.4, 6.3, "with drag", "t-o", 0, -4, "middle")
    return fig(("horizontal velocity–t", vx), ("vertical velocity–t (up +)", vy), ("path y–x", tr),
               caption="Treat the two directions separately; only time links them. Air resistance: lower peak, shorter range, steeper descent.")


def drag_curves():
    d = Plot(dn="drag: size", yl="drag", xl="v", aria="drag force increases with speed").curve(lambda v: 0.09 * v * v, 0, 10).t(3, 6, "D ∝ v² (air, fast)", "t-d")
    d.curve(lambda v: 0.6 * v, 0, 10, "o").t(8.5, 4.2, "D ∝ v (slow, viscous)", "t-o", 0, 0, "end")
    v = Plot(dn="+ve ↓ down", yl="v", xl="t", aria="falling with air resistance v-t curves to terminal velocity")
    v.path([(0, 0), (4.5, 9.5)], "o").curve(lambda t: 7 * (1 - math.exp(-t / 2)), 0, 10).guide([(0, 7), (10, 7)])
    v.hg(0, 7, "v_T").t(4.6, 9.4, "no drag", "t-o")
    a = Plot(dn="+ve ↓ down", yl="a", xl="t", aria="acceleration falls from g to zero").curve(lambda t: 7 * math.exp(-t / 2), 0, 10).hg(0, 7, "g").t(5, 1.5, "→ 0 at v_T", "t-d")
    return fig(("drag–speed", d), ("v–t", v), ("a–t", a),
               caption="Initial gradient of v–t = g (drag is zero at v = 0). Gradient falls to zero at terminal velocity.")


def forces_t():
    p = Plot(dn="W ↓  D ↑ (sizes)", yl="F", xl="t", aria="weight constant, drag rising to weight, resultant falling to zero")
    p.path([(0, 7), (10, 7)], "b").curve(lambda t: 7 * (1 - math.exp(-t / 1.6)), 0, 10, "s").curve(lambda t: 7 * math.exp(-t / 1.6), 0, 10, "d")
    p.t(10, 7, "weight W", "t-b", 0, -7, "end").t(5, 5.4, "drag D", "t-s").t(2.2, 2.0, "resultant W − D", "t-d")
    return fig(p, caption="Drag grows with speed until D = W: resultant force zero, acceleration zero, constant (terminal) velocity.")


def skydiver():
    p = Plot(dn="+ve ↓ down", yl="v", xl="t", aria="skydiver v-t: rises to terminal, sudden drop after parachute opens, lower terminal velocity")
    def v(t):
        if t <= 5: return 8.5 * (1 - math.exp(-t / 1.4))
        return 2.6 + (8.5 * (1 - math.exp(-5 / 1.4)) - 2.6) * math.exp(-(t - 5) / 0.45)
    p.curve(v, 0, 10, n=120).guide([(0, 8.5), (5, 8.5)]).guide([(0, 2.6), (10, 2.6)]).hg(0, 8.5, "v₁").hg(0, 2.6, "v₂")
    p.t(5.1, 7.8, "parachute opens", "t-sm").t(1.2, 4, "A", "t-pt").t(3.8, 7.6, "B", "t-pt").t(5.8, 5, "C", "t-pt").t(8, 2.6, "D", "t-pt", 0, -6)
    return fig(p, caption="A: D < W, accelerates. B: D = W, terminal v₁. C: parachute → D > W, decelerates (resultant UP). D: D = W again, lower terminal v₂.")


def fluid():
    a = Plot(dn="+ve ↓ down", yl="v", xl="t", aria="ball released from rest in oil reaches low terminal velocity quickly")
    a.curve(lambda t: 7 * (1 - math.exp(-t / 2)), 0, 10, "o").t(9.8, 7.2, "in air", "t-o", 0, -4, "end")
    a.curve(lambda t: 3 * (1 - math.exp(-t / 0.9)), 0, 10, "d").t(9.8, 3, "in oil/water", "t-d", 0, -6, "end")
    b = Plot(dn="+ve ↓ down", yl="v", xl="t", aria="ball enters water faster than terminal velocity and slows to terminal velocity")
    b.curve(lambda t: 3 + 5 * math.exp(-t / 1.2), 0, 10).guide([(0, 3), (10, 3)]).hg(0, 3, "v_T").hg(0, 8, "v₀")
    b.t(1.5, 6, "D + U > W: slows", "t-d")
    return fig(("released from rest in liquid", a), ("enters liquid faster than v_T", b),
               caption="In a liquid, upthrust U (constant) and viscous drag D act upward: terminal when W = U + D. Higher viscosity → lower v_T, reached sooner.")


def f_a():
    a = Plot(dn="+ve → along F", yl="F", xl="a", aria="force against acceleration straight line through origin gradient m").path([(0, 0), (10, 8)]).t(5, 5.5, "gradient = m", "t-d", 0, 0, "end")
    b = Plot(dn="+ve → along F", yl="a", xl="1/m", aria="acceleration against 1 over mass straight line gradient F").path([(0, 0), (10, 8)]).t(5, 5.5, "gradient = F", "t-d", 0, 0, "end")
    c = Plot(dn="+ve → along F", yl="a", xl="F", aria="acceleration against force with friction: intercept on F axis").path([(2, 0), (10, 8)]).t(2, 0, "F needed to beat friction", "t-sm", 4, 14)
    return fig(("F against a (constant m)", a), ("a against 1/m (constant F)", b), ("a against applied F, with friction", c),
               caption="F = ma: the straight line through the origin is the evidence for proportionality. An intercept means another force (friction) acts.")


def p_t():
    a = Plot(dn="+ve → along F", yl="p", xl="t", aria="momentum time straight line: constant force").path([(0, 2), (10, 9)]).t(5, 7, "gradient = F (constant)", "t-d", 0, 0, "end")
    b = Plot(dn="+ve → along F", yl="p", xl="t", aria="momentum time curve levelling off: force decreasing").curve(lambda t: 8 * (1 - math.exp(-t / 3)), 0, 10).t(5, 3, "F decreasing → 0", "t-d")
    return fig(("constant resultant force", a), ("force dies away", b),
               caption="Newton II: F = Δp/Δt. Gradient of p–t = resultant force; a horizontal p–t means F = 0 (momentum conserved).")


def f_t():
    p = Plot(dn="F on ball, sizes", yl="F", xl="t", aria="force time graph: hard impact tall narrow, soft impact low wide, equal areas")
    p.fill([(0.5, 0), (1.5, 9), (2.5, 0)], "fc").path([(0.5, 0), (1.5, 9), (2.5, 0)], "b")
    p.curve(lambda t: 3 * math.sin(math.pi * (t - 3) / 6) if 3 <= t <= 9 else 0, 3, 9, "d")
    p.t(1.6, 9, "hard (short Δt)", "t-b", 6, 4).t(6, 3, "soft / crumple zone", "t-d", 0, -6, "middle")
    p.t(1.5, 2.5, "area", "t-pt", 0, 0, "middle")
    return fig(p, caption="Area under F–t = impulse = Δp. Same Δp spread over a longer time ⇒ smaller peak force (airbags, crumple zones, bending knees).")


def collisions():
    v = Plot(dn="+ve → A's initial dirn", yr=(-2, 8), yl="v", xl="t", aria="velocities of two trolleys before and after a collision")
    v.path([(0, 6), (4, 6), (5, 4), (10, 4)], "d").path([(0, 0), (4, 0), (5, 4)], "s")
    v.t(1, 6, "A", "t-d", 0, -6).t(1, 0, "B", "t-s", 0, -6).t(7, 4, "stick together", "t-sm", 0, -8, "middle")
    p = Plot(dn="+ve → A's initial dirn", yr=(0, 10), yl="p", xl="t", aria="momentum of each trolley changes but total stays constant")
    p.path([(0, 8), (10, 8)], "gr").path([(0, 8), (4, 8), (5, 5.33), (10, 5.33)], "d").path([(0, 0), (4, 0), (5, 2.67), (10, 2.67)], "s")
    p.t(10, 8, "total", "t-gr", 0, -6, "end").t(8, 5.33, "p_A", "t-d", 0, -6).t(8, 2.67, "p_B", "t-s", 0, -6)
    k = Plot(dn="KE: scalar (no direction)", yr=(0, 10), yl="E_k", xl="t", aria="total kinetic energy: elastic returns to start, inelastic ends lower")
    k.path([(0, 8), (4, 8), (4.5, 6), (5, 8), (10, 8)], "gr").path([(4.5, 6), (5, 5.3), (10, 5.3)], "b")
    k.t(10, 8, "elastic", "t-gr", 0, -6, "end").t(10, 5.3, "inelastic", "t-b", 0, -6, "end")
    return fig(("velocity–time", v), ("momentum–time", p), ("total KE–time", k),
               caption="Momentum: total always conserved (no external force). KE: conserved only in elastic collisions; relative speed of approach = separation.")


def pressure():
    a = Plot(dn="scalar (no direction)", yl="p", xl="depth h", aria="pressure against depth: straight line, intercept atmospheric pressure")
    a.path([(0, 3), (10, 9)], "d").path([(0, 0), (10, 6)], "o").hg(0, 3, "p₀")
    a.t(6, 7.6, "total p = p₀ + ρgh", "t-d", 0, 0, "end").t(9, 4.5, "Δp = ρgh", "t-o", 0, 0, "end")
    b = Plot(dn="U ↑ (size)", yl="U", xl="depth of base", aria="upthrust grows while object is submerging then stays constant")
    b.path([(0, 0), (5, 7), (10, 7)]).vg(5, 7, "fully under").t(7.5, 7, "constant", "t-d", 0, -7, "middle")
    c = Plot(dn="scalar (no direction)", yl="m", xl="V", aria="mass against volume straight line gradient density").path([(0, 0), (10, 8)]).t(5, 5.5, "gradient = ρ", "t-d", 0, 0, "end")
    return fig(("pressure–depth", a), ("upthrust–depth", b), ("mass–volume", c),
               caption="Gradient of Δp–h = ρg. Upthrust = weight of fluid displaced = ρgV, so it stops increasing once fully submerged.")


def f_s():
    a = Plot(dn="F along s", yl="F", xl="s", aria="constant force: rectangle area").fill([(0, 0), (0, 6), (8, 6), (8, 0)]).path([(0, 6), (8, 6)]).t(4, 3, "W = Fs", "t-pt", 0, 0, "middle")
    b = Plot(dn="F along s", yl="F", xl="s", aria="force increasing linearly: triangle area").fill([(0, 0), (8, 8), (8, 0)]).path([(0, 0), (8, 8)]).t(5.5, 2, "W = ½Fs", "t-pt", 0, 0, "middle")
    c = Plot(dn="F along s", yl="F", xl="s", aria="varying force: count squares under curve").area(lambda s: 2 + 6 * math.sin(s / 3), 0, 9).curve(lambda s: 2 + 6 * math.sin(s / 3), 0, 9).t(4.5, 2.5, "count squares", "t-pt", 0, 0, "middle")
    return fig(("constant force", a), ("force ∝ extension (spring)", b), ("varying force", c),
               caption="Work done = area under the force–displacement graph, using the force component ALONG the displacement.")


def e_h():
    a = Plot(dn="energy: scalar (no direction)", yl="E", xl="height h", aria="no air resistance: GPE rises with height, KE falls, total constant")
    a.path([(0, 0), (10, 8)], "s").path([(0, 8), (10, 0)], "d").path([(0, 8), (10, 8)], "gr")
    a.t(9, 5.6, "GPE", "t-s", 0, 0, "end").t(1.5, 5.6, "KE", "t-d").t(5, 8, "total", "t-gr", 0, -6, "middle")
    b = Plot(dn="energy: scalar (no direction)", yl="E", xl="distance fallen", aria="with air resistance: total energy falls, KE rises less")
    b.path([(0, 8), (10, 0)], "s").path([(0, 0), (10, 5.6)], "d").path([(0, 8), (10, 5.6)], "gr")
    b.t(1.5, 5.4, "GPE", "t-s").t(9.6, 4.0, "KE", "t-d", 0, 0, "end").t(4, 7.2, "total", "t-gr", 0, -6)
    b.guide([(10, 8), (10, 5.6)])
    return fig(("energy against height (no drag)", a), ("falling with air resistance", b),
               caption="Energy vs height is LINEAR (GPE = mgh). The gap between the total line and its starting value = work done against air resistance.")


def e_t():
    a = Plot(dn="energy: scalar (no direction)", yl="E", xl="t", aria="dropped from rest: KE rises as t squared, GPE falls as a curve, total constant")
    a.curve(lambda t: 0.08 * t * t, 0, 10, "d").curve(lambda t: 8 - 0.08 * t * t, 0, 10, "s").path([(0, 8), (10, 8)], "gr")
    a.t(3, 2.4, "KE ∝ t²", "t-d").t(1, 6.8, "GPE", "t-s")
    b = Plot(dn="energy: scalar (no direction)", yl="E", xl="t", aria="ball thrown up: KE U shaped touching zero at top, GPE inverted")
    b.curve(lambda t: 0.32 * (t - 5) ** 2, 0, 10, "d").curve(lambda t: 8 - 0.32 * (t - 5) ** 2, 0, 10, "s")
    b.t(9.4, 5.8, "KE", "t-d", -6, 0, "end").t(5, 8, "GPE max", "t-s", 0, -6, "middle")
    return fig(("dropped from rest", a), ("thrown up and caught", b),
               caption="Against TIME the energy graphs are curves (h depends on t²). KE is zero only at the top for a vertical throw.")


def ke_v():
    a = Plot(dn="energy: scalar (no direction)", yl="E_k", xl="v", aria="kinetic energy against speed parabola").curve(lambda v: 0.08 * v * v, 0, 10).t(3, 5, "E_k = ½mv²", "t-d")
    b = Plot(dn="energy: scalar (no direction)", yl="E_k", xl="v²", aria="kinetic energy against v squared straight line gradient half m").path([(0, 0), (10, 8)]).t(5, 5.5, "gradient = ½m", "t-d", 0, 0, "end")
    c = Plot(dn="energy: scalar (no direction)", yl="E_k", xl="p", aria="kinetic energy against momentum parabola").curve(lambda p: 0.08 * p * p, 0, 10).t(3, 5, "E_k = p²/2m", "t-d")
    return fig(("E_k against v", a), ("E_k against v²", b), ("E_k against p", c),
               caption="Doubling speed quadruples KE. Plot E_k against v² to get a straight line (Paper 3 linearising).")


def power():
    a = Plot(dn="magnitudes only", yl="F", xl="v", aria="driving force P over v hyperbola meets resistance at maximum speed")
    a.curve(lambda v: 18 / v, 1.9, 10, "d").path([(0, 3), (10, 3)], "b").pt(6, 3).vg(6, 3, "v_max")
    a.t(2.3, 8.6, "D = P/v (P constant)", "t-d").t(10, 3, "resistance", "t-b", 0, -6, "end")
    b = Plot(dn="magnitudes only", yl="P", xl="v", aria="power against speed for constant force straight line gradient F").path([(0, 0), (10, 8)]).t(5, 5.5, "P = Fv, gradient F", "t-d", 0, 0, "end")
    c = Plot(dn="magnitudes only", yl="E", xl="t", aria="energy against time straight line gradient power").path([(0, 0), (10, 8)]).t(5, 5.5, "gradient = P", "t-d", 0, 0, "end")
    return fig(("max speed at fixed power", a), ("constant force", b), ("work done–time", c),
               caption="P = Fv. At maximum speed acceleration is zero, so driving force = resistance: v_max = P / F_resist.")


def linearise():
    p = Plot(dn="+ve ↓ down", yl="s / m", xl="t² / s²", aria="distance fallen against t squared straight line gradient g over 2")
    for x, y in [(1, 0.9), (2.5, 2.4), (4, 3.7), (5.5, 5.3), (7, 6.6), (8.5, 8.1)]:
        p.pt(x, y)
    p.path([(0, 0), (9.6, 9.1)], "d").guide([(2, 1.9), (9, 1.9), (9, 8.53)])
    p.t(5.5, 1.9, "Δ(t²)", "t-sm", 0, 14, "middle").t(9, 5, "Δs", "t-sm", 5, 0)
    return fig(p, caption="s = ½gt² ⇒ s against t² is a straight line through the origin with gradient ½g, so g = 2 × gradient.")


def we_vt():
    p = Plot(dn="+ve → forward", xr=(0, 26), yr=(0, 24), yl="v / m s⁻¹", xl="t / s", aria="car journey v-t trapezium")
    pts = [(0, 0), (8, 20), (20, 20), (25, 0)]
    p.fill(pts, "fb").path(pts).hg(8, 20, "20").vg(8, 20, "8").vg(20, 20, "20").t(25, 0, "25", "t-ax", 0, 14, "middle")
    return fig(p)


def we_ft():
    p = Plot(dn="+ve ← away from wall", xr=(0, 10), yr=(0, 700), yl="F / N", xl="t / ms", aria="force on ball rises to 600 N and falls over 8 ms")
    p.fill([(0, 0), (4, 600), (8, 0)], "fb").path([(0, 0), (4, 600), (8, 0)]).hg(4, 600, "600").t(8, 0, "8.0", "t-ax", 0, 14, "middle")
    return fig(p)


def we_bounce():
    t1, t2 = 0.606, 0.404
    v = Plot(dn="+ve ↓ down", xr=(0, 1.55), yr=(-5, 7), yl="v / m s⁻¹", xl="t / s", aria="sketch answer: v-t for bouncing ball, down positive")
    v.path([(0, 0), (t1, 5.94)]).guide([(t1, 5.94), (t1, -3.96)]).path([(t1, -3.96), (t1 + 2 * t2, 3.96)])
    v.hg(t1, 5.94, "5.94").t(0, -3.96, "−3.96", "t-ax", -5, 4, "end").guide([(t1, -3.96), (0, -3.96)])
    v.t(t1, 0, "0.61", "t-ax", -2, 14, "end").t(t1 + t2, 0, "1.01", "t-ax", 0, -6, "middle")
    return fig(v, caption="Both straight sections have gradient +9.81 (parallel). Rebound: velocity reverses sign and is smaller.")


def we_power():
    p = Plot(dn="magnitudes only", xr=(0, 40), yr=(0, 8000), yl="F / N", xl="v / m s⁻¹", aria="driving force 60000 over v meets 2000 N resistance at 30 m/s", L=46)
    p.curve(lambda v: 60000 / v, 7.6, 40).path([(0, 2000), (40, 2000)], "b").pt(30, 2000).vg(30, 2000, "30")
    p.pt(15, 4000).hg(15, 4000, "4000").vg(15, 4000, "15").hg(0, 2000, "2000")
    return fig(p)


# ---------------------------------------------------------------- cards
def build():
    C = []
    C.append(card("cover", "Start", "Physics graphs", "Cover", r"""
<p class="sec" style="margin:0">CAIE 9702 · AS · Chapters 2–5</p>
<p class="cover-k">Graphs</p>
<h1>Every AS graph, Kinematics → Work &amp; Energy</h1>
<p class="lede">Displacement, velocity, acceleration, free fall, bouncing, projectiles, terminal velocity in air and liquids, force &amp; momentum, collisions, pressure, energy and power. For each: the shape, what the gradient means, what the area means, and the trap.</p>
<div class="stat"><div><b>75+</b>graphs</div><div><b>4</b>worked examples</div><div><b>11</b>practice Qs</div></div>
<p><a href="index.html">Open Revision Hub</a></p>
<div class="swipehint">Swipe or use the arrows · tap ☰ for contents</div>""", sec="Start"))

    C.append(card("big", "Start", "Gradient & area rules", "Overview", r"""
<h2>The two questions to ask of ANY graph</h2>
<p class="lede">What is the gradient? What is the area? Get the units of each: that tells you the quantity.</p>
<div class="tw"><table>
<tr><th>Graph (y against x)</th><th>Gradient</th><th>Area under</th></tr>
<tr><td class="k">s–t</td><td>velocity</td><td>—</td></tr>
<tr><td class="k">v–t</td><td>acceleration</td><td>displacement</td></tr>
<tr><td class="k">a–t</td><td>—</td><td>change in velocity</td></tr>
<tr><td class="k">p–t</td><td>resultant force</td><td>—</td></tr>
<tr><td class="k">F–t</td><td>—</td><td>impulse = Δp</td></tr>
<tr><td class="k">F–s</td><td>(spring: k)</td><td>work done</td></tr>
<tr><td class="k">E–t or W–t</td><td>power</td><td>—</td></tr>
<tr><td class="k">P–t</td><td>—</td><td>energy transferred</td></tr>
<tr><td class="k">m–V</td><td>density</td><td>—</td></tr>
<tr><td class="k">p–h (liquid)</td><td>ρg</td><td>—</td></tr>
</table></div>
<div class="note link"><b>Direction tag</b>Every graph shows its sign convention in the top-right corner (e.g. "+ve ↓ down"). In an exam, state yours before you sketch: changing it flips every velocity and acceleration graph.</div>
<div class="note tip"><b>Unit check</b>Gradient units = y-unit ÷ x-unit; area units = y-unit × x-unit. E.g. F–t area: N × s = N s = kg m s⁻¹, a momentum unit.</div>""", sec="Start"))

    # ---------------------------------------------------------- Kinematics
    S = "1 · Kinematics graphs"
    C.append(card("k-st", "1 Kinematics", "s–t shapes", "Concept", r"""
<h2>Displacement–time: the shapes</h2>
""" + st_shapes() + rule("velocity", "nothing useful") + r"""
<div class="note trap"><b>Trap</b>A horizontal s–t line means at rest. A horizontal v–t line means constant velocity. Read the y-axis label first, every time.</div>""", sec=S))

    C.append(card("k-tan", "1 Kinematics", "Tangents on s–t", "Concept", r"""
<h2>Instantaneous velocity from a curve</h2>
""" + st_tangent() + r"""
<ul><li>Average velocity = chord gradient (total \(\Delta s\) / total \(\Delta t\)).</li>
<li>Instantaneous velocity = tangent gradient at that point.</li>
<li>Same idea on v–t: tangent gradient = instantaneous acceleration.</li></ul>
<div class="note tip"><b>Paper 2</b>"Determine" from a graph: show the triangle, read both coordinates, quote the gradient to 2–3 s.f. with unit.</div>""", sec=S))

    C.append(card("k-vt", "1 Kinematics", "v–t shapes", "Concept", r"""
<h2>Velocity–time: the shapes</h2>
""" + vt_shapes() + rule("acceleration", "displacement") + r"""
<p>Straight line \(\Rightarrow\) uniform acceleration \(\Rightarrow\) SUVAT is allowed. Curved \(\Rightarrow\) acceleration changing \(\Rightarrow\) no SUVAT; use the graph.</p>""", sec=S))

    C.append(card("k-chg", "1 Kinematics", "Changing acceleration", "Concept", r"""
<h2>Increasing / decreasing acceleration &amp; deceleration</h2>
""" + changing_accel() + changing_accel_at() + r"""
<div class="tw"><table>
<tr><th>Description</th><th>v–t</th><th>a–t (forward +)</th></tr>
<tr><td class="k">Decreasing acceleration</td><td>rising, getting flatter</td><td>positive, falling to 0</td></tr>
<tr><td class="k">Increasing acceleration</td><td>rising, getting steeper</td><td>positive, rising</td></tr>
<tr><td class="k">Increasing deceleration</td><td>falling, getting steeper</td><td>negative, more negative</td></tr>
<tr><td class="k">Decreasing deceleration</td><td>falling, getting flatter</td><td>negative, rising to 0</td></tr>
</table></div>
<div class="note trap"><b>Trap</b>"Decreasing acceleration" still means speeding up, just less quickly. Falling with air resistance is the classic example; a car braking harder and harder is increasing deceleration.</div>""", sec=S))

    C.append(card("k-area", "1 Kinematics", "Area below the axis", "Concept", r"""
<h2>When the v–t line crosses the time axis</h2>
""" + vt_area() + r"""
<div class="note trap"><b>Trap</b>"Distance travelled" adds the areas; "displacement" subtracts the area below the axis. Read which one is asked.</div>""", sec=S))

    C.append(card("k-at", "1 Kinematics", "a–t graphs", "Concept", r"""
<h2>Acceleration–time</h2>
""" + at_graph() + r"""
<p>\(v = u + \text{(area under a–t)}\). For free fall the a–t graph is a horizontal line at \(g\) (or \(-g\) if up is positive).</p>""", sec=S))

    C.append(card("k-trio", "1 Kinematics", "s–t, v–t, a–t together", "Concept", r"""
<h2>Converting between the three graphs</h2>
""" + journey_trio() + r"""
<div class="chain"><span>s–t</span><i>gradient →</i><span>v–t</span><i>gradient →</i><span>a–t</span></div>
<div class="chain"><span>a–t</span><i>area →</i><span>v–t</span><i>area →</i><span>s–t</span></div>
<ul><li>Where v–t has a maximum, a–t crosses zero.</li><li>Where s–t has a maximum (turning back), v–t crosses zero.</li></ul>""", sec=S))

    # ---------------------------------------------------------- Free fall & projectiles
    S = "2 · Free fall & projectiles"
    C.append(card("f-ff", "2 Free fall", "Free fall from rest", "Concept", r"""
<h2>Dropped from rest, no air resistance</h2>
""" + freefall() + r"""
<p>\(v = gt\), \(s = \tfrac12 g t^2\), \(a = g = 9.81\ \text{m s}^{-2}\) for all masses.</p>""", sec=S))

    C.append(card("f-up", "2 Free fall", "Thrown up, comes back", "Concept", r"""
<h2>Ball thrown vertically upwards</h2>
""" + thrown_up() + r"""
<div class="note trap"><b>Trap</b>At the top \(v = 0\) but \(a = -g\), not zero. The v–t line goes straight through the axis without a kink. Time up = time down (no drag).</div>""", sec=S))

    C.append(card("f-bounce", "2 Free fall", "Bouncing ball", "Concept", r"""
<h2>Ball dropped and bouncing</h2>
<h3>Taking DOWN as positive</h3>
""" + bounce() + r"""
<h3>Taking UP as positive</h3>
""" + bounce_up() + r"""
<ul><li>Contact time is tiny ⇒ the velocity jump is drawn (almost) vertical.</li>
<li>Sign convention matters: with down positive, falling sections have positive v; rising sections negative v.</li>
<li>Peak height ratio = KE ratio after/before bounce: \(h_2/h_1 = (v_2/v_1)^2\).</li></ul>
<div class="note tip"><b>P1 favourite</b>Look for the graph whose straight segments are all <b>parallel</b> (same gradient g) and whose velocity <b>changes sign</b> at each bounce.</div>""", sec=S))

    C.append(card("f-proj", "2 Free fall", "Projectile motion", "Concept", r"""
<h2>Projectiles: split into components</h2>
""" + projectile() + r"""
<div class="tw"><table>
<tr><th></th><th>Horizontal</th><th>Vertical</th></tr>
<tr><td class="k">Acceleration</td><td>0</td><td>\(-g\)</td></tr>
<tr><td class="k">Velocity</td><td>\(u\cos\theta\) constant</td><td>\(u\sin\theta - gt\)</td></tr>
<tr><td class="k">Displacement</td><td>\(x = u\cos\theta\, t\) (linear in t)</td><td>\(y = u\sin\theta\, t - \tfrac12 g t^2\)</td></tr>
</table></div>
<p>Speed–time for an angled launch: falls to a <b>minimum of \(u\cos\theta\)</b> at the top (not zero), then rises again.</p>""", sec=S))

    C.append(card("f-lin", "2 Free fall", "Measuring g: s against t²", "Concept", r"""
<h2>Linearising: getting g from a graph</h2>
""" + linearise() + r"""
<ul><li>A positive y-intercept with \(s\) measured from the release point: reaction-time / timing systematic error.</li>
<li>Other linear forms: \(v^2\) against \(s\) (gradient \(2g\)); \(v\) against \(t\) (gradient \(g\)).</li></ul>
<div class="note tip"><b>Paper 3</b>Gradient from a triangle covering more than half the line; quote the uncertainty from the worst acceptable line.</div>""", sec=S))

    # ---------------------------------------------------------- Air resistance & fluids
    S = "3 · Air resistance & fluids"
    C.append(card("r-drag", "3 Drag", "Falling with air resistance", "Concept", r"""
<h2>Drag and terminal velocity</h2>
""" + drag_curves() + r"""
<ul><li>Drag increases with speed and depends on shape/area; acts opposite to velocity.</li>
<li>v–t: starts with gradient \(g\), gradient decreases, flattens at \(v_T\).</li>
<li>s–t: curve then straight line (constant gradient = \(v_T\)).</li></ul>""", sec=S))

    C.append(card("r-explain", "3 Drag", "Explain terminal velocity", "Concept", r"""
<h2>The 3-mark "explain" chain</h2>
""" + forces_t() + r"""
<ol class="steps">
<li>As speed increases, air resistance (drag) increases. """ + tg("B1") + r"""</li>
<li>So the resultant force (\(W - D\)) decreases, so acceleration decreases. """ + tg("B1") + r"""</li>
<li>When drag = weight, resultant force is zero, acceleration is zero: constant (terminal) velocity. """ + tg("B1") + r"""</li>
</ol>
<div class="note trap"><b>Wording</b>Say "resultant force decreases", not "the force decreases" (weight doesn't change). Never "gravity decreases".</div>""", sec=S))

    C.append(card("r-sky", "3 Drag", "Skydiver & parachute", "Concept", r"""
<h2>Skydiver: two terminal velocities</h2>
""" + skydiver() + r"""
<div class="note trap"><b>Trap</b>After the parachute opens the skydiver is still moving DOWN but decelerating, so the resultant force is UP. They do not go up.</div>""", sec=S))

    C.append(card("r-fluid", "3 Drag", "Motion in water & oil", "Concept", r"""
<h2>Falling through a liquid</h2>
""" + fluid() + r"""
<div class="tw"><table>
<tr><th>Force</th><th>Direction</th><th>Changes with speed?</th></tr>
<tr><td class="k">Weight \(W = mg\)</td><td>down</td><td>no</td></tr>
<tr><td class="k">Upthrust \(U = \rho_{\text{liq}} g V\)</td><td>up</td><td>no</td></tr>
<tr><td class="k">Viscous drag \(D\)</td><td>opposite to velocity</td><td>yes, increases</td></tr>
</table></div>
<p>Terminal condition: \(W = U + D\). A ball bearing in oil reaches \(v_T\) within a few cm: why the timing marks in the practical start well below the surface.</p>""", sec=S))

    C.append(card("r-airliq", "3 Drag", "From air into liquid", "Concept", r"""
<h2>Dropped through air, then into a liquid</h2>
""" + air_liquid() + r"""
<ol>
<li><b>In air:</b> only weight acts (drag neglected), so \(a = g\): straight line, gradient \(g\).</li>
<li><b>Entering faster than \(v_T\):</b> upthrust + viscous drag exceed weight, resultant force upward, so it decelerates. Drag falls as speed falls, so the deceleration decreases: curve flattens onto \(v_T\).</li>
<li><b>Entering slower than \(v_T\):</b> \(W &gt; U + D\), still accelerates, but less than \(g\) (upthrust and drag). Acceleration decreases to zero at \(v_T\).</li>
</ol>
<div class="note trap"><b>Trap</b>On entry the velocity does NOT jump: only the gradient (acceleration) changes suddenly. The velocity curve is continuous, the a–t graph is not.</div>""", sec=S))

    # ---------------------------------------------------------- Dynamics
    S = "4 · Dynamics & momentum"
    C.append(card("d-fa", "4 Dynamics", "F = ma graphs", "Concept", r"""
<h2>Newton's second law graphs</h2>
""" + f_a() + r"""
<p>Definition to quote: the resultant force is proportional to the rate of change of momentum (and in its direction).</p>""", sec=S))

    C.append(card("d-pt", "4 Dynamics", "Momentum–time", "Concept", r"""
<h2>Momentum–time</h2>
""" + p_t() + r"""
<p>\(F = \dfrac{\Delta p}{\Delta t}\): read two points off the line, divide. A curved p–t needs a tangent.</p>""", sec=S))

    C.append(card("d-ft", "4 Dynamics", "Force–time & impulse", "Concept", r"""
<h2>Force–time: area = impulse</h2>
""" + f_t() + r"""
<p>\(\text{impulse} = \int F\,dt = \Delta p = m(v - u)\). For a triangle: \(\tfrac12 \times F_{\max} \times \Delta t\).</p>
<div class="note tip"><b>Units</b>Impulse in N s; momentum in kg m s⁻¹. They are the same unit.</div>""", sec=S))

    C.append(card("d-coll", "4 Dynamics", "Collision graphs", "Concept", r"""
<h2>Two trolleys colliding</h2>
""" + collisions() + r"""
<ul><li>During contact the forces on A and B are equal and opposite (N3), for the same time ⇒ equal and opposite changes in momentum.</li>
<li>So the p–t graphs of A and B are mirror images; their sum is flat.</li>
<li>Ball rebounding off a wall: v–t jumps from \(+u\) to \(-v\); \(\Delta p = m(v + u)\) in magnitude.</li></ul>""", sec=S))

    # ---------------------------------------------------------- Pressure
    S = "5 · Density, pressure, upthrust"
    C.append(card("p-press", "5 Pressure", "Pressure & upthrust graphs", "Concept", r"""
<h2>Pressure, upthrust and density</h2>
""" + pressure() + r"""
<p>\(\Delta p = \rho g \Delta h\) is linear in depth and independent of the container's shape. Upthrust arises because pressure on the bottom face is greater than on the top face.</p>""", sec=S))

    # ---------------------------------------------------------- Work, energy, power
    S = "6 · Work, energy & power"
    C.append(card("w-fs", "6 Energy", "Force–displacement", "Concept", r"""
<h2>Work done from F–s</h2>
""" + f_s() + r"""
<p>\(W = Fs\cos\theta\). If only part of the force acts along the motion, only that component does work.</p>""", sec=S))

    C.append(card("w-eh", "6 Energy", "Energy against height", "Concept", r"""
<h2>Energy against height / distance</h2>
""" + e_h() + r"""
<div class="note tip"><b>Shapes</b>Against height or distance: straight lines (\(mgh\), and \(E_k = mgs\) when falling freely). Against time: curves.</div>""", sec=S))

    C.append(card("w-et", "6 Energy", "Energy against time", "Concept", r"""
<h2>Energy against time</h2>
""" + e_t() + r"""
<p>Dropped: \(E_k = \tfrac12 m (gt)^2 \propto t^2\). Angled projectile: KE has a minimum of \(\tfrac12 m (u\cos\theta)^2\) at the top, never zero.</p>""", sec=S))

    C.append(card("w-kev", "6 Energy", "KE against v, v², p", "Concept", r"""
<h2>Kinetic energy graphs</h2>
""" + ke_v() + r"""
<p>\(E_k = \tfrac12 mv^2 = \dfrac{p^2}{2m}\). Same momentum, smaller mass ⇒ more KE.</p>""", sec=S))

    C.append(card("w-pow", "6 Energy", "Power graphs", "Concept", r"""
<h2>Power: P = Fv</h2>
""" + power() + r"""
<p>Efficiency \(= \dfrac{\text{useful output}}{\text{total input}} \times 100\%\): on a Sankey or energy–time graph, compare gradients (powers) or heights (energies).</p>""", sec=S))

    # ---------------------------------------------------------- Worked examples
    S = "Worked examples"
    C.append(card("we1", "Worked", "Car journey from v–t", "Worked example", r"""
<h2>Reading a v–t graph</h2>
""" + we_vt() + r"""
<p><b>Q:</b> A car's v–t graph is shown. Find (a) the acceleration in the first 8 s, (b) the deceleration at the end, (c) the total distance, (d) the average speed. [6]</p>
<ol class="steps">
<li>""" + tg("M1") + r""" (a) \(a = \dfrac{\Delta v}{\Delta t} = \dfrac{20 - 0}{8} = 2.5\ \text{m s}^{-2}\) """ + tg("A1") + r"""</li>
<li>(b) \(a = \dfrac{0 - 20}{25 - 20} = -4.0\ \text{m s}^{-2}\), so deceleration \(= 4.0\ \text{m s}^{-2}\) """ + tg("A1") + r"""</li>
<li>""" + tg("M1") + r""" (c) Area: \(\tfrac12(8)(20) + (12)(20) + \tfrac12(5)(20) = 80 + 240 + 50 = 370\ \text{m}\) """ + tg("A1") + r"""</li>
<li>(d) \(\bar v = \dfrac{370}{25} = 14.8\ \text{m s}^{-1}\) """ + tg("A1") + r"""</li>
</ol>
<div class="note trap"><b>Where marks go</b>Average speed is total distance ÷ total time, NOT \((0 + 20)/2\).</div>""", sec=S))

    C.append(card("we2", "Worked", "Bouncing ball sketch", "Worked example", r"""
<h2>Sketching a bouncing-ball v–t graph</h2>
<p><b>Q:</b> A ball is dropped from 1.80 m and rebounds to 0.80 m. Air resistance is negligible. (a) Calculate the speed just before and just after the bounce. (b) Sketch v–t from release to the top of the first rebound, taking downwards as positive. (c) Find the fraction of KE lost. [7]</p>
<ol class="steps">
<li>""" + tg("C1") + r""" \(v^2 = u^2 + 2as\): \(v = \sqrt{2(9.81)(1.80)} = 5.94\ \text{m s}^{-1}\) down """ + tg("A1") + r"""</li>
<li>Up to 0.80 m: \(v = \sqrt{2(9.81)(0.80)} = 3.96\ \text{m s}^{-1}\) up """ + tg("A1") + r"""</li>
<li>Times: fall \(t = 5.94/9.81 = 0.61\ \text{s}\); rise \(t = 3.96/9.81 = 0.40\ \text{s}\), so top at 1.01 s.</li>
<li>""" + tg("B1", "B1") + r""" Sketch: straight line 0 → +5.94 at 0.61 s; vertical drop to −3.96; straight line back to 0 at 1.01 s, <b>parallel</b> to the first.""" + we_bounce() + r"""</li>
<li>""" + tg("C1") + r""" KE ∝ h (all KE becomes GPE): fraction lost \(= 1 - \dfrac{0.80}{1.80} = 0.56\) """ + tg("A1") + r"""</li>
</ol>""", sec=S))

    C.append(card("we3", "Worked", "Impulse from F–t", "Worked example", r"""
<h2>Area under F–t gives Δp</h2>
""" + we_ft() + r"""
<p><b>Q:</b> A ball of mass 0.060 kg moving at 20 m s⁻¹ hits a wall normally. The force on it varies as shown. Find (a) the impulse, (b) the velocity after the impact, (c) whether the collision is elastic. [5]</p>
<ol class="steps">
<li>""" + tg("C1") + r""" (a) Impulse = area \(= \tfrac12 (600)(8.0\times10^{-3}) = 2.4\ \text{N s}\) """ + tg("A1") + r"""</li>
<li>Take away from the wall as positive: \(u = -20\ \text{m s}^{-1}\).</li>
<li>""" + tg("C1") + r""" (b) \(2.4 = 0.060(v - (-20))\Rightarrow v + 20 = 40 \Rightarrow v = 20\ \text{m s}^{-1}\) away from the wall """ + tg("A1") + r"""</li>
<li>(c) Speed unchanged ⇒ KE unchanged ⇒ elastic. """ + tg("B1") + r"""</li>
</ol>
<div class="note trap"><b>Trap</b>Ignoring the sign of \(u\) gives \(2.4 = 0.060(v - 20)\Rightarrow v = 60\ \text{m s}^{-1}\): impossible (more KE than it arrived with). For a rebound, \(|\Delta p| = m(v + u)\).</div>""", sec=S))

    C.append(card("we4", "Worked", "Max speed from P = Fv", "Worked example", r"""
<h2>Driving force against speed</h2>
""" + we_power() + r"""
<p><b>Q:</b> A car of mass 1200 kg has a constant output power of 60 kW. Resistive forces are a constant 2000 N. Find (a) the maximum speed, (b) the acceleration at 15 m s⁻¹. [5]</p>
<ol class="steps">
<li>""" + tg("C1") + r""" (a) Max speed: \(a = 0\) so driving force \(= 2000\ \text{N}\). \(v = \dfrac{P}{F} = \dfrac{60\,000}{2000} = 30\ \text{m s}^{-1}\) """ + tg("A1") + r"""</li>
<li>""" + tg("C1") + r""" (b) At 15 m s⁻¹: \(F = \dfrac{60\,000}{15} = 4000\ \text{N}\)</li>
<li>""" + tg("C1") + r""" \(F_{\text{res}} = 4000 - 2000 = 2000\ \text{N}\)</li>
<li>\(a = \dfrac{2000}{1200} = 1.7\ \text{m s}^{-2}\) """ + tg("A1") + r"""</li>
</ol>
<div class="note tip"><b>Graph reading</b>Max speed is where the \(P/v\) curve meets the resistance line.</div>""", sec=S))

    # ---------------------------------------------------------- Mistakes
    C.append(card("mist", "Exam", "Common mistakes", "Common mistakes", r"""
<h2>Where graph marks are lost</h2>
<ul>
<li><b>Wrong graph read:</b> treating v–t as s–t. Check the y-axis label first.</li>
<li><b>Gradient from data points not on the line:</b> use points read from the best-fit line, large triangle.</li>
<li><b>Prefixes on axes:</b> t in ms or F in kN: convert to s and N before finding the area or gradient (factor of 1000 errors).</li>
<li><b>a = 0 at the top</b> of a vertical throw: wrong, a = −g throughout.</li>
<li><b>Bounce sketch:</b> segments not parallel, or velocity doesn't change sign, or rebound speed too big.</li>
<li><b>Terminal velocity:</b> "forces balance so it stops". No: zero resultant force = constant velocity, not rest.</li>
<li><b>Parachute opening:</b> drawing v going negative. It still moves down, just more slowly.</li>
<li><b>Projectile:</b> horizontal velocity drawn changing (no drag) or speed at the top drawn as zero.</li>
<li><b>Energy vs height</b> drawn curved: it is linear. Energy vs time is curved.</li>
<li><b>Displacement vs distance</b> when v–t crosses the axis.</li>
</ul>""", sec="Exam"))

    # ---------------------------------------------------------- Practice
    C.append(card("pr1", "Practice", "Practice: kinematics graphs", "Practice", r"""
<h2>Practice · Kinematics &amp; free fall</h2>
<div class="pq"><div class="qh"><span>Q1 · sketch</span><span class="mk">[3]</span></div>
<p class="qt">A ball is thrown vertically upwards and caught at the same height. Taking upwards as positive and ignoring air resistance, sketch (a) displacement–time, (b) velocity–time, (c) acceleration–time.</p>
<div class="ans"><b>Answer</b>(a) Inverted parabola from 0, max at mid-time with zero gradient, back to 0. (b) Straight line from \(+u\) to \(-u\), crossing zero at mid-time, gradient \(-g\). (c) Horizontal line at \(-9.81\ \text{m s}^{-2}\) throughout.</div></div>
<div class="pq"><div class="qh"><span>Q2 · v–t</span><span class="mk">[4]</span></div>
<p class="qt">A cyclist accelerates uniformly from 4.0 m s⁻¹ to 10 m s⁻¹ in 3.0 s, then decelerates uniformly to rest in 2.0 s. Sketch the v–t graph and find the total distance and the deceleration.</p>
<div class="ans"><b>Answer</b>Distance \(= \tfrac12(4+10)(3) + \tfrac12(10)(2) = 21 + 10 = 31\ \text{m}\). Deceleration \(= 10/2.0 = 5.0\ \text{m s}^{-2}\).</div></div>
<div class="pq"><div class="qh"><span>Q3 · projectile</span><span class="mk">[6]</span></div>
<p class="qt">A stone is thrown horizontally at 12 m s⁻¹ from a cliff 20 m high. Sketch horizontal and vertical velocity against time. Find the time of flight, the horizontal distance and the speed on impact.</p>
<div class="ans"><b>Answer</b>\(v_x\): horizontal line at 12. \(v_y\) (down +): straight line from 0, gradient 9.81. \(t = \sqrt{2(20)/9.81} = 2.02\ \text{s}\); \(x = 12 \times 2.02 = 24\ \text{m}\); \(v_y = 19.8\), speed \(= \sqrt{12^2 + 19.8^2} = 23\ \text{m s}^{-1}\).</div></div>
<div class="pq"><div class="qh"><span>Q4 · Paper 3 style</span><span class="mk">[4]</span></div>
<p class="qt">A student plots distance fallen \(s\) against \(t^2\) and gets a straight line through the origin with gradient 4.9 m s⁻². Determine \(g\), and state what a positive \(t^2\)-intercept would suggest.</p>
<div class="ans"><b>Answer</b>\(s = \tfrac12 g t^2\), gradient \(= g/2\) ⇒ \(g = 9.8\ \text{m s}^{-2}\). A \(t^2\)-intercept means measured times are systematically too long (e.g. reaction time in starting/stopping the stopwatch, or release delay).</div></div>""", sec="Practice · 1–4"))

    C.append(card("pr2", "Practice", "Practice: drag, momentum", "Practice", r"""
<h2>Practice · Drag &amp; momentum</h2>
<div class="pq"><div class="qh"><span>Q5 · explain</span><span class="mk">[4]</span></div>
<p class="qt">A steel ball is released from rest just below the surface of oil. Sketch its v–t graph and explain its shape in terms of the forces acting.</p>
<div class="ans"><b>Answer</b>Curve from 0, initial gradient less than g (upthrust), flattening to \(v_T\). Weight and upthrust constant; viscous drag increases with speed, so resultant force \(W - U - D\) and acceleration decrease; when \(W = U + D\) resultant force is zero and velocity is constant.</div></div>
<div class="pq"><div class="qh"><span>Q6 · p–t</span><span class="mk">[3]</span></div>
<p class="qt">A trolley's momentum increases linearly from 2.0 N s to 8.0 N s in 3.0 s. Its mass is 0.50 kg. Find the resultant force and the change in velocity.</p>
<div class="ans"><b>Answer</b>\(F = \Delta p/\Delta t = 6.0/3.0 = 2.0\ \text{N}\). \(\Delta v = \Delta p/m = 6.0/0.50 = 12\ \text{m s}^{-1}\).</div></div>
<div class="pq"><div class="qh"><span>Q7 · F–t</span><span class="mk">[3]</span></div>
<p class="qt">The resultant force on a 2.0 kg trolley, initially at rest, rises linearly from 0 to 6.0 N in 2.0 s, then stays at 6.0 N for a further 3.0 s. Find its speed at 5.0 s.</p>
<div class="ans"><b>Answer</b>Impulse \(= \tfrac12(6.0)(2.0) + 6.0(3.0) = 6.0 + 18 = 24\ \text{N s}\). \(v = 24/2.0 = 12\ \text{m s}^{-1}\).</div></div>
<div class="pq"><div class="qh"><span>Q8 · collision</span><span class="mk">[5]</span></div>
<p class="qt">Trolley A (2.0 kg, 3.0 m s⁻¹) hits stationary trolley B (1.0 kg) and they stick. Sketch momentum–time for A, B and the total, and find the KE lost.</p>
<div class="ans"><b>Answer</b>\(6.0 = 3.0v\) ⇒ \(v = 2.0\ \text{m s}^{-1}\). \(p_A\): 6.0 → 4.0; \(p_B\): 0 → 2.0 (mirror image); total flat at 6.0 N s. KE: \(9.0 - \tfrac12(3.0)(2.0)^2 = 9.0 - 6.0 = 3.0\ \text{J}\) lost.</div></div>""", sec="Practice · 5–8"))

    C.append(card("pr3", "Practice", "Practice: pressure, energy", "Practice", r"""
<h2>Practice · Pressure, energy, air → liquid</h2>
<div class="pq"><div class="qh"><span>Q9 · energy</span><span class="mk">[5]</span></div>
<p class="qt">A 0.50 kg ball is dropped from 10 m. (a) Sketch KE and GPE against height with no air resistance. (b) With a constant air resistance of 1.0 N, find the KE and speed at the ground.</p>
<div class="ans"><b>Answer</b>(a) Two straight lines: GPE from 49 J at 10 m to 0; KE from 0 at 10 m to 49 J at ground; total flat at 49 J. (b) \(E_k = mgh - Fs = 49.05 - 10 = 39\ \text{J}\); \(v = \sqrt{2(39.05)/0.50} = 12.5\ \text{m s}^{-1}\).</div></div>
<div class="pq"><div class="qh"><span>Q10 · F–s and p–h</span><span class="mk">[5]</span></div>
<p class="qt">(a) A force rises linearly from 0 to 40 N over 0.20 m, then stays at 40 N for a further 0.30 m. Find the work done. (b) A total pressure–depth graph for a liquid has intercept \(1.0\times10^5\) Pa and reads \(1.49\times10^5\) Pa at 5.0 m. Find the density.</p>
<div class="ans"><b>Answer</b>(a) \(W = \tfrac12(40)(0.20) + 40(0.30) = 4.0 + 12 = 16\ \text{J}\). (b) \(\rho = \dfrac{\Delta p}{g\Delta h} = \dfrac{4.9\times10^4}{9.81 \times 5.0} = 1.0\times10^3\ \text{kg m}^{-3}\).</div></div>
<div class="pq"><div class="qh"><span>Q11 · sketch</span><span class="mk">[4]</span></div>
<p class="qt">A stone is dropped from a bridge into a deep river. It hits the water at a speed greater than its terminal velocity in water. Taking downwards as positive and ignoring air resistance, sketch v–t and a–t from release until it has fallen a long way through the water.</p>
<div class="ans"><b>Answer</b>v–t: straight line from 0, gradient \(g\), up to the entry speed; then a curve decreasing and flattening onto \(v_T\) (no jump in v at entry). a–t: horizontal at \(+g\); at entry a sudden drop to a large negative value; then a curve rising back to 0.</div></div>""", sec="Practice · 9–11"))

    # ---------------------------------------------------------- Summary
    C.append(card("sum", "Summary", "Graph cheat sheet", "Summary", r"""
<h2>One-page graph cheat sheet</h2>
<div class="tw"><table>
<tr><th>Situation</th><th>Key graph feature</th></tr>
<tr><td class="k">Free fall (no drag)</td><td>v–t straight, gradient g; s–t parabola; a–t flat</td></tr>
<tr><td class="k">Thrown up</td><td>v–t straight through zero; a = −g at the top</td></tr>
<tr><td class="k">Bouncing</td><td>parallel v–t lines; sign flips; smaller each bounce</td></tr>
<tr><td class="k">Projectile</td><td>vₓ flat; v_y straight; path parabola; min speed u cosθ</td></tr>
<tr><td class="k">Air resistance</td><td>v–t curves to v_T; a–t falls to 0</td></tr>
<tr><td class="k">Parachute</td><td>sudden drop in v, then lower v_T (still positive)</td></tr>
<tr><td class="k">In liquid</td><td>W = U + D; low v_T reached fast; enters fast → slows to v_T</td></tr>
<tr><td class="k">Collision</td><td>p_A, p_B mirror; total flat; KE flat only if elastic</td></tr>
<tr><td class="k">Impact</td><td>F–t area = Δp; longer time → lower peak</td></tr>
<tr><td class="k">Liquid pressure</td><td>p–h linear, intercept p₀, gradient ρg</td></tr>
<tr><td class="k">Energy</td><td>linear in h, curved in t; total falls with drag</td></tr>
<tr><td class="k">Power</td><td>D = P/v meets resistance at v_max</td></tr>
</table></div>
<div class="note tip"><b>Sketch checklist</b>Label axes with quantity (and unit), mark key values on the axes, correct shape (straight vs curved), correct starting gradient, correct sign.</div>""", sec="Summary"))
    return C


FLASH = [
    ["Kinematics", "Gradient of an s–t graph?", "Velocity."],
    ["Kinematics", "Gradient of a v–t graph?", "Acceleration."],
    ["Kinematics", "Area under a v–t graph?", "Displacement."],
    ["Kinematics", "Area under an a–t graph?", "Change in velocity."],
    ["Kinematics", "Horizontal line on s–t vs on v–t?", "s–t: at rest. v–t: constant velocity."],
    ["Kinematics", "How to get instantaneous velocity from a curved s–t?", "Gradient of the tangent at that time (large triangle)."],
    ["Kinematics", "v–t crosses the time axis: meaning?", "Object momentarily at rest and reverses direction."],
    ["Kinematics", "Distance vs displacement from v–t crossing the axis?", "Distance = sum of areas; displacement = area above − area below."],
    ["Free fall", "v–t for an object dropped (no drag)?", "Straight line through origin, gradient g = 9.81 m s⁻²."],
    ["Free fall", "s–t for an object dropped from rest?", "Parabola, s = ½gt²."],
    ["Free fall", "Acceleration at the top of a vertical throw?", "−g (9.81 m s⁻² downward). Velocity is zero, acceleration isn't."],
    ["Free fall", "Speed–time for a ball thrown up and caught?", "V shape: falls linearly to 0 at the top, rises linearly back."],
    ["Free fall", "Bouncing ball v–t: two key features?", "Straight segments all parallel (gradient g); velocity changes sign and decreases in magnitude at each bounce."],
    ["Free fall", "Height–time for a bouncing ball?", "Series of parabolic arcs with decreasing peak heights."],
    ["Kinematics", "v–t shape for decreasing acceleration?", "Rising curve getting flatter (gradient positive but decreasing)."],
    ["Kinematics", "v–t shape for increasing deceleration?", "Falling curve getting steeper (gradient increasingly negative)."],
    ["Kinematics", "a–t for decreasing deceleration (forward +)?", "Negative values rising towards zero."],
    ["Free fall", "Bouncing ball v–t with UP positive?", "Lines slope down (gradient −g); falling sections negative; each bounce jumps up from −v to a smaller +v."],
    ["Free fall", "Bouncing ball a–t with up positive?", "Constant −g, with large positive spikes during each contact."],
    ["Drag", "Dropped from air into liquid faster than v_T: v–t?", "Straight line gradient g in air, then curve decreasing and flattening to v_T. No jump in v at entry."],
    ["Drag", "Dropped from air into liquid slower than v_T: v–t?", "Line gradient g, then gradient suddenly smaller and decreasing; curve rises to v_T."],
    ["Projectile", "Horizontal velocity–time (no drag)?", "Horizontal line: constant."],
    ["Projectile", "Vertical velocity–time (up +)?", "Straight line, gradient −g, zero at the top."],
    ["Projectile", "Minimum speed of an angled projectile?", "u cosθ at the top (not zero)."],
    ["Projectile", "Effect of air resistance on trajectory?", "Lower peak, shorter range, steeper descent than ascent (asymmetric)."],
    ["Drag", "v–t for an object falling with air resistance?", "Curve from 0 with initial gradient g, gradient decreasing, levelling off at terminal velocity."],
    ["Drag", "Condition for terminal velocity in air?", "Drag = weight, so resultant force and acceleration are zero."],
    ["Drag", "Condition for terminal velocity in a liquid?", "Weight = upthrust + viscous drag."],
    ["Drag", "Skydiver opens parachute: what happens on v–t?", "Velocity drops sharply (still downward) then levels at a lower terminal velocity."],
    ["Drag", "Ball enters water faster than its terminal velocity: v–t?", "Decreases (curving) down to v_T: upthrust + drag > weight."],
    ["Dynamics", "Gradient of a momentum–time graph?", "Resultant force."],
    ["Dynamics", "Area under a force–time graph?", "Impulse = change in momentum."],
    ["Dynamics", "Why do crumple zones reduce injury (use F–t)?", "Same Δp (area) over longer time ⇒ smaller peak force."],
    ["Dynamics", "Momentum–time for two colliding bodies?", "Mirror images; total momentum line is horizontal."],
    ["Dynamics", "F against a for constant mass?", "Straight line through origin, gradient = m."],
    ["Pressure", "Pressure against depth in a liquid?", "Straight line; gradient ρg; total pressure has intercept p₀ (atmospheric)."],
    ["Pressure", "Upthrust against depth as an object is lowered in?", "Increases linearly until fully submerged, then constant."],
    ["Energy", "Area under force–displacement?", "Work done."],
    ["Energy", "KE and GPE against height for free fall?", "Straight lines: GPE ∝ h rising, KE falling, total constant."],
    ["Energy", "KE against time for a dropped object?", "Parabola: KE ∝ t²."],
    ["Energy", "Which plot of E_k gives a straight line through the origin?", "E_k against v² (gradient ½m)."],
    ["Power", "Gradient of energy–time (work–time)?", "Power."],
    ["Power", "Condition for maximum speed at constant power?", "Driving force (P/v) = resistive force; a = 0."],
]

QUIZ = [
    {"s": "Kinematics", "q": "A v–t graph is a straight line sloping downwards that crosses the time axis. The object…",
     "o": ["is slowing down the whole time", "slows, stops momentarily, then speeds up in the opposite direction", "comes to rest and stays there", "has increasing deceleration"], "c": 1,
     "e": "Constant negative gradient: speed falls to zero, then velocity becomes negative (reverses) with growing speed."},
    {"s": "Kinematics", "q": "The area under an acceleration–time graph represents…",
     "o": ["displacement", "velocity", "change in velocity", "change in displacement"], "c": 2,
     "e": "Area of a–t = Δv. You need the initial velocity to get v."},
    {"s": "Kinematics", "q": "An s–t graph curves upward and gets steeper. The object is…",
     "o": ["at rest", "moving with constant velocity", "accelerating", "decelerating"], "c": 2,
     "e": "Gradient (velocity) increasing ⇒ accelerating."},
    {"s": "Free fall", "q": "A ball is thrown vertically upwards. At its highest point…",
     "o": ["v = 0 and a = 0", "v = 0 and a = g downwards", "v = max and a = 0", "v = 0 and a = g upwards"], "c": 1,
     "e": "Only gravity acts, so a = g downward throughout."},
    {"s": "Free fall", "q": "Which describes the v–t graph of a bouncing ball (no air resistance)?",
     "o": ["Curved segments, all the same sign", "Parallel straight segments, sign reversing at each bounce", "Horizontal segments", "Straight segments with increasing gradient"], "c": 1,
     "e": "Free fall between bounces ⇒ gradient g each time; velocity reverses at impact."},
    {"s": "Kinematics", "q": "A v–t graph is a rising curve that gets flatter. The object has…",
     "o": ["increasing acceleration", "decreasing acceleration", "increasing deceleration", "decreasing deceleration"], "c": 1,
     "e": "Rising ⇒ speeding up; flattening ⇒ gradient (acceleration) decreasing."},
    {"s": "Free fall", "q": "A ball is dropped and bounces. Taking UP as positive, the straight sections of its v–t graph…",
     "o": ["all slope upwards", "all slope downwards with gradient −g", "alternate up and down", "are horizontal"], "c": 1,
     "e": "Between bounces only gravity acts: a = −g (up positive). Each bounce is a jump upward."},
    {"s": "Drag", "q": "A stone enters water faster than its terminal velocity in water. Just after entry…",
     "o": ["v drops suddenly to v_T", "the resultant force is upward and it decelerates", "acceleration is still g", "it moves upward"], "c": 1,
     "e": "U + D > W ⇒ resultant upward ⇒ decelerates (still moving down). Velocity is continuous."},
    {"s": "Projectile", "q": "For a projectile with no air resistance, the horizontal component of velocity against time is…",
     "o": ["a straight line with gradient −g", "a horizontal line", "a parabola", "zero at the top"], "c": 1,
     "e": "No horizontal force ⇒ constant horizontal velocity."},
    {"s": "Projectile", "q": "A projectile is launched at 30° with speed 20 m s⁻¹. Its speed at the highest point is…",
     "o": ["0", "10 m s⁻¹", "17.3 m s⁻¹", "20 m s⁻¹"], "c": 2,
     "e": "Only the horizontal component remains: 20 cos30° = 17.3 m s⁻¹."},
    {"s": "Drag", "q": "An object falls from rest with air resistance. The initial gradient of its v–t graph is…",
     "o": ["zero", "g", "greater than g", "equal to the terminal velocity"], "c": 1,
     "e": "At v = 0 there is no drag, so a = g initially."},
    {"s": "Drag", "q": "Immediately after a skydiver opens the parachute, the resultant force is…",
     "o": ["zero", "downwards", "upwards", "equal to the weight"], "c": 2,
     "e": "Drag suddenly exceeds weight ⇒ resultant upwards ⇒ decelerating (still moving down)."},
    {"s": "Drag", "q": "A sphere falls at terminal velocity through oil. Which is correct?",
     "o": ["weight = drag", "weight = upthrust", "weight = upthrust + drag", "upthrust = drag"], "c": 2,
     "e": "In a liquid, upthrust is significant: W = U + D."},
    {"s": "Dynamics", "q": "The gradient of a momentum–time graph is…",
     "o": ["impulse", "resultant force", "kinetic energy", "power"], "c": 1,
     "e": "F = Δp/Δt (Newton's second law)."},
    {"s": "Dynamics", "q": "A force rises from 0 to 50 N and back to 0 in 0.020 s as a triangle. The impulse is…",
     "o": ["0.25 N s", "0.50 N s", "1.0 N s", "2500 N s"], "c": 1,
     "e": "½ × 50 × 0.020 = 0.50 N s."},
    {"s": "Dynamics", "q": "Two trolleys collide (no external force). Their individual momentum–time graphs are…",
     "o": ["identical", "mirror images about a horizontal line", "both constant", "both increasing"], "c": 1,
     "e": "Equal and opposite Δp, so one gains what the other loses; total constant."},
    {"s": "Pressure", "q": "A graph of total pressure against depth in a lake is…",
     "o": ["a straight line through the origin", "a straight line with a positive intercept", "a curve", "horizontal"], "c": 1,
     "e": "p = p₀ + ρgh: intercept is atmospheric pressure."},
    {"s": "Energy", "q": "For an object falling freely, a graph of KE against distance fallen is…",
     "o": ["a parabola", "a straight line through the origin", "a horizontal line", "an exponential curve"], "c": 1,
     "e": "KE gained = mgs, linear in s. (Against time it is a parabola.)"},
    {"s": "Energy", "q": "The area under a force–displacement graph is…",
     "o": ["power", "impulse", "work done", "momentum"], "c": 2,
     "e": "W = ∫F ds."},
    {"s": "Power", "q": "A car at constant power P against constant resistance R reaches maximum speed…",
     "o": ["P × R", "P / R", "R / P", "√(P/R)"], "c": 1,
     "e": "At v_max, driving force = R and P = Rv ⇒ v = P/R."},
]


def write():
    meta = {"title": "Physics Graphs Deck", "short": "Phys Graphs", "bar": "Physics · Graphs",
            "code": "9702 · AS · Ch 2–5", "key": "deck-9702-graphs"}
    cards = build()
    out = engine.render(meta, cards, FLASH, QUIZ, math=True)
    out = out.replace("<b>Paper 1 quiz</b>", "<b>Graphs quiz</b>").replace('<figure class="dg">', '<figure class="dg" style="max-width:520px">')
    (HERE / "deck-phys-graphs.html").write_text(out, encoding="utf8")
    print("phys graphs", len(out), "bytes,", len(cards), "cards,", len(FLASH), "flashcards,", len(QUIZ), "quiz")
    return cards


if __name__ == "__main__":
    write()
