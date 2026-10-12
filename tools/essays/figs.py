"""Diagrams for the Essay Bank, drawn with the deck's SVG kit (data space 0..10 on both axes)."""
import math
from diagrams import Fig, fig, inter


def _x_on(a, b, y):
    """x where the line through a and b reaches height y."""
    return a[0] + (y - a[1]) * (b[0] - a[0]) / (b[1] - a[1])


def ppc():
    f = lambda x: 9 * math.sqrt(max(0.0, 1 - (x / 9) ** 2))
    g = Fig(xl="Consumer goods", yl="Capital goods", xsym="", ysym="", aria="Concave PPC with points A, B, C, an inside point U and an unattainable point X")
    g.curve(f, 0, 9, "d", "PPC", off=(-30, -8))
    A, B, C = (3, f(3)), (6, f(6)), (8, f(8))
    g.guide(A).guide(B).guide(C)
    g.pt(A, "A").pt(B, "B").pt(C, "C", off=(6, -2))
    g.pt((3.2, 3.2), "U (unemployment)", off=(6, 4))
    g.pt((7.6, 7.2), "X (unattainable)", off=(-6, -8), anchor="end", hollow=True)
    return fig(g, caption="Moving A→B→C, each extra 2–3 units of consumer goods costs more capital goods: increasing opportunity cost, so the PPC bows out. U is inside (idle or misused resources); X is outside (unattainable now).")


def ped_tr():
    e = Fig(aria="Elastic demand: a price cut gains more revenue than it loses")
    D = ((0.5, 6.5), (9.5, 3.5))
    q0, q1 = _x_on(*D, 5.5), _x_on(*D, 4.5)
    e.poly([(0, 4.5), (q0, 4.5), (q0, 5.5), (0, 5.5)], "fc")
    e.poly([(q0, 0), (q1, 0), (q1, 4.5), (q0, 4.5)], "fb")
    e.line(*D, "d", "D", off=(-4, -8), anchor="end")
    e.guide((q0, 5.5), "Q0", "P0").guide((q1, 4.5), "Q1", "P1")
    e.text((q0 / 2, 4.95), "lost", "t-b", anchor="middle", off=(0, 4)).text(((q0 + q1) / 2, 2.2), "gained", "t-s", anchor="middle")
    i = Fig(aria="Inelastic demand: a price rise gains more revenue than it loses")
    D2 = ((2, 9.5), (4.5, 0.5))
    a0, a1 = _x_on(*D2, 4), _x_on(*D2, 6)
    i.poly([(0, 4), (a1, 4), (a1, 6), (0, 6)], "fb")
    i.poly([(a1, 0), (a0, 0), (a0, 4), (a1, 4)], "fc")
    i.line(*D2, "d", "D", off=(6, 0))
    i.guide((a0, 4), "Q0", "P0").guide((a1, 6), "", "P1")
    i.text((a1 / 2, 5), "gained", "t-s", anchor="middle", off=(0, 4))
    return fig(("Mass-market car · elastic · cut price", e), ("Luxury car · inelastic · raise price", i),
               caption="Teal = revenue gained, red = revenue lost. Each brand moves price in the direction where the gain is bigger.")


def max_price():
    g = Fig(aria="Maximum price below equilibrium creates a shortage")
    S, D = ((1, 1), (9, 9)), ((1, 9), (9, 1))
    g.line(*S, "s", "S", off=(4, 4)).line(*D, "d", "D", off=(4, 12))
    g.guide((5, 5), "Qe", "Pe").pt((5, 5))
    g.line((0.2, 3), (9.4, 3), "b", "Pmax", off=(-2, -6), anchor="end")
    g.guide((3, 3), "Qs").guide((7, 3), "Qd")
    g.arrow((3.15, 2.2), (6.85, 2.2)).text((5, 2.2), "shortage", "t-b", anchor="middle", off=(0, 16))
    g.line((3, 3), (3, 7), "o").guide((3, 7), None, "Pbm").pt((3, 7))
    g.text((3, 7), "black market", "t-sm", off=(8, -6))
    return fig(g, caption="Pmax below Pe: quantity demanded rises to Qd, quantity supplied falls to Qs, so there is a shortage. With only Qs available, some buyers would pay up to the black-market price.")


def tax_inelastic():
    g = Fig(aria="Indirect tax on a good with inelastic demand: price rises a lot, quantity falls a little")
    D = ((3.6, 9.6), (5.8, 1.0))
    S, St = ((1, 1), (9, 7)), ((1, 3.6), (9, 9.6))
    e0, e1 = inter(*D, *S), inter(*D, *St)
    pnet = e1[1] - 2.6
    g.poly([(0, e0[1]), (e1[0], e0[1]), (e1[0], e1[1]), (0, e1[1])], "fa")
    g.poly([(0, pnet), (e1[0], pnet), (e1[0], e0[1]), (0, e0[1])], "fb")
    g.line(*S, "s", "S", off=(4, 4)).line(*St, "b", "S + tax", off=(-4, -6), anchor="end").line(*D, "d", "D", off=(6, 0))
    g.guide(e0, "", "P0").guide(e1, "Q1", "P1").pt(e0).pt(e1)
    g.text((e0[0], 0), "Q0", "t-ax", off=(10, 15), anchor="start")
    g.guide((e1[0], pnet), None, "P1−t")
    return fig(g, caption="Amber = tax paid by consumers (price rises P0→P1); teal = tax borne by producers. With inelastic demand most of the tax falls on consumers and quantity falls only from Q0 to Q1.")


def keynes_as():
    def AS(x):
        if x <= 4:
            return 2.0
        return 2 + 0.6 * (x - 4) / (8.2 - x)
    g = Fig(xl="Real output", yl="Price level", aria="Keynesian AS curve with three AD curves")
    g.line((0.3, 2), (4, 2), "s").curve(AS, 4, 7.98, "s", "AS", off=(6, 6))
    pts = []
    for c, lab in ((4.5, "AD1"), (8.3, "AD2"), (13.0, "AD3")):
        lo, hi = 0.3, 7.98
        for _ in range(60):
            m = (lo + hi) / 2
            if AS(m) < c - m:
                lo = m
            else:
                hi = m
        x = (lo + hi) / 2
        pts.append((x, AS(x)))
        x0, x1 = max(0.2, c - 9.6), min(9.6, c - 0.6)
        g.line((x0, c - x0), (x1, c - x1), "d", lab, off=(4, 12))
    for p, (xt, yt) in zip(pts, (("Y1", "P1"), ("Y2", "P2"), ("Yfe", "P3"))):
        g.guide(p, xt, yt).pt(p)
    return fig(g, caption="AD1 → spare capacity: output rises, prices don't. AD2 → bottlenecks: both rise. AD3 → full employment (Yfe): only the price level rises.")


def j_curve():
    def f(x):
        if x <= 2:
            return 4.0
        t = x - 2
        return 4 - 4 * t * math.exp(-t) + 0.5 * t
    g = Fig(xl="Time", yl="Current account", origin=False, aria="J-curve: the current account worsens after a depreciation, then improves")
    g.line((0.1, 5), (9.7, 5), "o", "balance = 0", off=(-2, -6), anchor="end")
    g.curve(f, 0.1, 9.4, "d", "J-curve", off=(-6, -8), anchor="end")
    g.pt((2, 4), "depreciation", off=(-6, -10), anchor="end")
    g.text((2.4, 2.4), "deficit widens", "t-b", off=(14, 14))
    return fig(g, caption="In the short run import and export volumes barely react, so dearer imports widen the deficit. As buyers switch over time (Marshall–Lerner holds), the balance improves.")


def monopoly():
    g = Fig(xl="Quantity", yl="Price, cost", aria="Monopoly compared with competition: higher price, lower output, deadweight loss")
    D, MR = ((0.2, 8.84), (9.6, 1.32)), ((0.2, 8.68), (5.4, 0.36))
    g.poly([(0, 3), (3.75, 3), (3.75, 6), (0, 6)], "fa")
    g.poly([(3.75, 6), (3.75, 3), (7.5, 3)], "fc")
    g.line(*D, "d", "D = AR", off=(-4, -8), anchor="end").line(*MR, "o", "MR", off=(4, 4))
    g.line((0.2, 3), (9.6, 3), "s", "MC = AC", off=(-2, -6), anchor="end")
    g.guide((3.75, 6), "Qm", "Pm").pt((3.75, 6)).pt((3.75, 3))
    g.guide((7.5, 3), "Qc", "Pc").pt((7.5, 3))
    g.text((1.9, 4.5), "profit", "t-pt", anchor="middle").text((4.9, 3.5), "DWL", "t-b", anchor="middle")
    return fig(g, caption="Monopoly sets MR = MC: output Qm, price Pm > MC. Competition would give Qc at Pc. Amber = supernormal profit taken from consumers; red = deadweight loss.")


def min_wage():
    c = Fig(xl="Labour", yl="Wage", xsym="L", ysym="W", aria="Minimum wage above equilibrium in a competitive labour market")
    S, D = ((1, 2), (9, 9)), ((1, 9), (9, 2))
    e = inter(*S, *D)
    qd, qs = _x_on(*D, 7), _x_on(*S, 7)
    c.line(*S, "s", "S", off=(4, 4)).line(*D, "d", "D = MRP", off=(-4, 14), anchor="end")
    c.line((0.2, 7), (9.6, 7), "b", "NMW", off=(-2, -6), anchor="end")
    c.guide(e, "Le", "We").pt(e).guide((qd, 7), "Ld").guide((qs, 7), "Ls")
    c.arrow((qd + .1, 6.2), (qs - .1, 6.2)).text(((qd + qs) / 2, 6.2), "unemployed", "t-b", anchor="middle", off=(0, 16))
    m = Fig(xl="Labour", yl="Wage", xsym="L", ysym="W", aria="Monopsony: a minimum wage can raise both wages and employment")
    m.line((0.2, 1.14), (9.4, 7.58), "s", "S = ACL", off=(-4, -8), anchor="end")
    m.line((0.2, 1.28), (5.6, 8.84), "o", "MCL", off=(4, 4))
    m.line((0.2, 8.86), (9.4, 2.42), "d", "MRP", off=(-4, 14), anchor="end")
    lm = 8 / 2.1
    m.guide((lm, 1 + .7 * lm), "Lm", "Wm").pt((lm, 1 + .7 * lm)).pt((lm, 1 + 1.4 * lm))
    m.line((0.2, 5), (5.714, 5), "b", "NMW", off=(-30, -6))
    m.guide((5.714, 5), "L*").pt((5.714, 5))
    return fig(("Competitive market", c), ("Monopsony employer", m),
               caption="Left: a wage floor above We cuts jobs from Le to Ld. Right: a monopsonist pays only Wm and hires Lm. A minimum wage set at the competitive level raises the wage and employment (to L*).")


def phillips():
    f = lambda u: 6 / u - 0.2
    g = Fig(xl="Unemployment (%)", yl="Inflation (%)", aria="Short-run and long-run Phillips curves")
    g.curve(f, 0.75, 9.5, "d", "SRPC1", off=(-4, -6), anchor="end")
    g.curve(lambda u: f(u) + 2.5, 1.1, 9.5, "o", "SRPC2", off=(-4, -6), anchor="end")
    g.line((5, 0.2), (5, 9.6), "s", "LRPC", off=(6, 10))
    A, B, C = (5, f(5)), (3, f(3)), (5, f(5) + 2.5)
    g.pt(A, "A").pt(B, "B").pt(C, "C", off=(8, 4))
    g.arrow((4.7, 1.15), (3.3, 1.7)).arrow((3.3, 2.35), (4.75, 3.3))
    g.text((5, 0), "Un", "t-ax", off=(0, 15), anchor="middle")
    return fig(g, caption="A→B: higher AD cuts unemployment at the cost of inflation (short-run trade-off). B→C: workers expect the higher inflation, wages rise, unemployment returns to the natural rate Un at higher inflation. The LRPC is vertical.")
