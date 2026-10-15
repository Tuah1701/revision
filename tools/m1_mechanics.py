"""9709 Paper 4 · Mechanics: whole-paper deck built from Puan Syazwani's KYUEM notes, tutorials and quizzes
(Forces & equilibrium, Kinematics, Newton's laws, Momentum, Work-energy-power). g = 10, answers to 3 s.f."""
import math, pathlib
import engine
from engine import card
from diagrams import Fig, fig

HERE = pathlib.Path(__file__).parent

# ---------------------------------------------------------------- force-diagram helpers (hand SVG, theme classes)
DEFS = ('<defs><marker id="fh" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
        '<path class="arh" d="M0,0 L10,5 L0,10 z"/></marker></defs>')


def arr(x1, y1, x2, y2, cls="ar"):
    return f'<line class="{cls}" x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" marker-end="url(#fh)"/>'


def txt(x, y, s, cls="t-pt", anchor="middle"):
    return f'<text class="{cls}" x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}">{s}</text>'


def svg(parts, aria, w=320, h=230):
    return f'<svg viewBox="0 0 {w} {h}" role="img" aria-label="{aria}">{DEFS}{"".join(parts)}</svg>'


def slope_svg():
    """Block on a rough slope: W down, R normal, P up the slope, F (friction) down the slope (block about to move up)."""
    th = math.radians(28)
    x0, y0, L = 20, 205, 290
    x1, y1 = x0 + L * math.cos(th), y0 - L * math.sin(th)
    p = [f'<path class="ax" d="M{x0},{y0} L{x1:.1f},{y0} L{x1:.1f},{y1:.1f} Z"/>']
    # block centre on the slope
    d = 150
    bx, by = x0 + d * math.cos(th), y0 - d * math.sin(th)
    ux, uy = math.cos(th), -math.sin(th)          # up-slope unit
    nx, ny = -math.sin(th), -math.cos(th)         # outward normal
    s = 20
    cx, cy = bx + nx * s, by + ny * s             # block centre
    corners = [(bx - ux * s, by - uy * s), (bx + ux * s, by + uy * s),
               (bx + ux * s + nx * 2 * s, by + uy * s + ny * 2 * s), (bx - ux * s + nx * 2 * s, by - uy * s + ny * 2 * s)]
    p.append('<polygon class="fb" points="' + " ".join(f"{a:.1f},{b:.1f}" for a, b in corners) + '"/>')
    p.append(arr(cx, cy, cx, cy + 70, "ar"))
    p.append(txt(cx + 14, cy + 72, "W = mg", "t-b", "start"))
    p.append(arr(cx, cy, cx + nx * 62, cy + ny * 62))
    p.append(txt(cx + nx * 70, cy + ny * 70, "R", "t-s"))
    p.append(arr(cx + ux * 22, cy + uy * 22, cx + ux * 80, cy + uy * 80))
    p.append(txt(cx + ux * 90, cy + uy * 90 - 2, "P", "t-d"))
    p.append(arr(cx - ux * 22, cy - uy * 22, cx - ux * 70, cy - uy * 70))
    p.append(txt(cx - ux * 80 - 6, cy - uy * 80 + 4, "F ≤ μR", "t-gr", "end"))
    p.append(f'<path class="g" d="M{x0 + 46},{y0} A46,46 0 0 0 {x0 + 46 * math.cos(th):.1f},{y0 - 46 * math.sin(th):.1f}"/>')
    p.append(txt(x0 + 56, y0 - 8, "θ", "t-sm", "start"))
    p.append(txt(cx + 16, cy + 98, "mg sinθ down the slope · mg cosθ into it", "t-sm"))
    return svg(p, "Block on a rough slope with weight, normal reaction, applied force P up the slope and friction down the slope", 320, 240)


def pulley_svg():
    p = []
    px, py, r = 160, 40, 18
    p.append(f'<circle class="pto" cx="{px}" cy="{py}" r="{r}"/>')
    p.append(f'<line class="ax" x1="{px}" y1="{py - r - 14}" x2="{px}" y2="{py}"/>')
    p.append(f'<line class="ax" x1="{px - 70}" y1="{py - r - 14}" x2="{px + 70}" y2="{py - r - 14}"/>')
    for sx, by, name, m, cls in ((px - r, 150, "A", "3 kg", "fa"), (px + r, 110, "B", "5 kg", "fc")):
        p.append(f'<line class="ax" x1="{sx}" y1="{py}" x2="{sx}" y2="{by}"/>')
        p.append(f'<rect class="{cls}" x="{sx - 18}" y="{by}" width="36" height="30" rx="4"/>')
        p.append(txt(sx, by + 20, name))
        p.append(arr(sx, by - 4, sx, by - 40))
        p.append(txt(sx + (-12 if name == "A" else 12), by - 22, "T", "t-s", "end" if name == "A" else "start"))
        p.append(arr(sx, by + 30, sx, by + 70))
        p.append(txt(sx + (-12 if name == "A" else 12), by + 62, "30 N" if name == "A" else "50 N", "t-b", "end" if name == "A" else "start"))
        p.append(txt(sx + (-26 if name == "A" else 26), by + 18, m, "t-sm", "end" if name == "A" else "start"))
    p.append(arr(px - r - 50, 160, px - r - 50, 130, "ar"))
    p.append(txt(px - r - 56, 150, "a", "t-d", "end"))
    p.append(arr(px + r + 50, 110, px + r + 50, 140, "ar"))
    p.append(txt(px + r + 56, 130, "a", "t-d", "start"))
    p.append(f'<line class="ax" x1="20" y1="222" x2="300" y2="222"/>')
    return svg(p, "Two particles over a smooth pulley: same tension T on both sides, A accelerates up, B down", 320, 230)


def vt_fig():
    f = Fig(xl="t (s)", yl="v (m s⁻¹)", aria="Velocity-time graph: accelerate, constant speed, decelerate", xsym="t", ysym="v")
    pts = [(0, 0), (2.5, 6), (7.5, 6), (9.5, 0)]
    f.poly(pts, "fb")
    f.path(pts, "d")
    f.guide((2.5, 6), "12", "6").guide((7.5, 6), "37")
    f.text((9.5, 0), "45", "t-ax", off=(0, 15), anchor="middle")
    f.text((0.3, 7.3), "gradient = a", "t-sm", anchor="start")
    f.text((5, 3), "area = distance", "t-pt", anchor="middle")
    return fig(f, caption="Assignment 1 Q1, the cyclist: gradient gives acceleration, area gives displacement. 36 + 150 + 24 = 210 m.")


# ---------------------------------------------------------------- cards
def tg(*marks):
    return "".join(f'<span class="tag">{m}</span>' for m in marks)


def build():
    C = []
    C.append(card("cover", "Start", "Paper 4 · Mechanics", "Cover", r"""
<p class="sec" style="margin:0">CAIE 9709 · AS Level · Paper 4</p>
<p class="cover-k">P4</p>
<h1>Mechanics: the whole paper</h1>
<p class="lede">Built from Puan Syazwani's KYUEM notes, tutorials, quizzes and Assignment 1 across all five chapters. \(g = 10\ \text{m s}^{-2}\), answers to 3 s.f.</p>
<div class="stat"><div><b>5</b>chapters</div><div><b>12</b>worked examples</div><div><b>12</b>practice Qs</div></div>
<p><a href="index.html">Open Revision Hub</a></p>
<div class="swipehint">Swipe or use the arrows · tap ☰ for contents</div>""", sec="Start"))

    C.append(card("big", "Start", "The big picture", "Overview", r"""
<h2>One method answers every question</h2>
<p class="lede">50 marks, 1 hr 15 min: about 1.5 minutes per mark. Every question is one of five ideas.</p>
<div class="tw"><table>
<tr><th>Chapter</th><th>The one equation</th><th>Use when</th></tr>
<tr><td class="k">Forces &amp; equilibrium</td><td>\(\sum F_x = 0,\ \sum F_y = 0\)</td><td>At rest, constant velocity, "about to slip"</td></tr>
<tr><td class="k">Kinematics</td><td>SUVAT, or \(v = \frac{ds}{dt},\ a = \frac{dv}{dt}\)</td><td>Motion described, no forces</td></tr>
<tr><td class="k">Newton's laws</td><td>\(F_{\text{res}} = ma\)</td><td>Forces <i>and</i> acceleration</td></tr>
<tr><td class="k">Momentum</td><td>\(m_1u_1 + m_2u_2 = m_1v_1 + m_2v_2\)</td><td>Collisions, coalescing</td></tr>
<tr><td class="k">Energy &amp; power</td><td>\(\text{WD} = \Delta KE + \Delta PE\), \(P = Fv\)</td><td>Distances/heights, no time; engines</td></tr>
</table></div>
<h3>The routine (marks are lost here, not in algebra)</h3>
<div class="chain"><span>1 · Force diagram</span><i>→</i><span>2 · Positive direction</span><i>→</i><span>3 · Name the equation</span><i>→</i><span>4 · Substitute</span><i>→</i><span>5 · 3 s.f. + units</span></div>
<div class="note tip"><b>Method marks</b>An M1 needs every relevant term present with the correct component (sin/cos). Write the unsimplified equation first: an examiner can award M1 even if your arithmetic later slips.</div>""", sec="Start"))

    C.append(card("words", "Start", "Modelling words", "Concept", r"""
<h2>What the modelling words mean in your equations</h2>
<div class="tw"><table>
<tr><th>Word</th><th>So in the equations…</th></tr>
<tr><td class="k">Particle</td><td>All mass at a point: no rotation, no size, forces all act at one point.</td></tr>
<tr><td class="k">Smooth</td><td>No friction: \(F = 0\). Only \(R\) acts at the contact.</td></tr>
<tr><td class="k">Rough</td><td>Friction acts, \(F \le \mu R\).</td></tr>
<tr><td class="k">Limiting equilibrium / about to slip</td><td>\(F = \mu R\) <b>exactly</b>, and acceleration is still 0.</td></tr>
<tr><td class="k">Light (string, rod, pulley)</td><td>Mass ignored, so tension is the <b>same all the way along</b>.</td></tr>
<tr><td class="k">Inextensible</td><td>Doesn't stretch: connected particles share the <b>same magnitude of acceleration and speed</b>.</td></tr>
<tr><td class="k">Smooth pulley</td><td>Tension the same on both sides; only the direction changes.</td></tr>
<tr><td class="k">Rigid rod / tow-bar</td><td>Can be in tension (pulling) <b>or thrust</b> (pushing). A string can only be in tension.</td></tr>
<tr><td class="k">Coalesce</td><td>The two bodies stick together and move with one common velocity.</td></tr>
<tr><td class="k">Line of greatest slope</td><td>Force/motion is straight up or down the slope, so resolve parallel and perpendicular to it.</td></tr>
</table></div>
<div class="note trap"><b>Trap</b>"Limiting" doesn't mean moving. It means on the point of moving, so \(a = 0\) and \(F = \mu R\).</div>""", sec="Start"))

    # ------------------------------------------------------------ 1. Forces & equilibrium
    S1 = "1 · Forces &amp; equilibrium"
    C.append(card("f-res", "1 Forces & equilibrium", "Components and resultants", "Concept", r"""
<h2>Resolve everything into two perpendicular directions</h2>
<div class="def"><div class="lab">Components <i>θ from the x-axis</i></div>
<p>\(F_x = F\cos\theta, \qquad F_y = F\sin\theta\)</p></div>
<div class="def"><div class="lab">Resultant of several forces</div>
<p>\(X = \sum F_x,\ \ Y = \sum F_y\), then \(R = \sqrt{X^2 + Y^2}\), \(\tan\alpha = \dfrac{Y}{X}\)</p></div>
<ul>
<li><b>cos goes with the angle you're touching</b>: the component <i>adjacent</i> to the marked angle uses cos.</li>
<li>Give the direction of a resultant as an angle <i>from a stated line</i> ("8.66° below the horizontal").</li>
<li>Two forces in equilibrium are equal and opposite. Three forces in equilibrium form a closed <b>triangle of forces</b> (sine/cosine rule works).</li>
</ul>
<div class="note tip"><b>Quick check</b>Draw a rough sketch of \(X\) and \(Y\) with their signs before you take \(\tan^{-1}\). The calculator only gives \(-90°\) to \(90°\).</div>""", sec=S1))

    C.append(card("f-eq", "1 Forces & equilibrium", "Equilibrium", "Concept", r"""
<h2>Equilibrium: resultant force is zero</h2>
<p class="lede">At rest <b>or</b> moving with constant velocity (Newton's first law).</p>
<div class="formula">Σ(components in any direction) = 0</div>
<h3>Choosing directions</h3>
<div class="two">
<div><h4>Flat ground</h4><p>Resolve horizontally and vertically.</p></div>
<div><h4 class="t">Slope</h4><p>Resolve <b>parallel</b> and <b>perpendicular</b> to the slope. Only the weight (and any horizontal force) needs splitting.</p></div>
<div><h4 class="g">Unknown you don't want</h4><p>Resolve <b>perpendicular to it</b> and it disappears from that equation (the note's tugboat example: resolve perpendicular to \(T\)).</p></div>
</div>
<div class="note link"><b>Newton's third law</b>If A pushes on B, B pushes back on A with an equal and opposite force. That's why the floor pushes up on you (\(R\)) and why tension acts towards the centre of the string on both connected bodies.</div>
<div class="note trap"><b>Trap</b>\(R\) is <b>not</b> always \(mg\). Any force with a vertical component (a pull at an angle, a boy pushing down on a chair) changes \(R\), and therefore changes \(\mu R\).</div>""", sec=S1))

    C.append(card("f-fric", "1 Forces & equilibrium", "Friction", "Concept", r"""
<h2>Friction: a force that grows until it can't</h2>
<div class="def"><div class="lab">Friction law</div>
<p>\(0 \le F \le \mu R\). At limiting equilibrium or when sliding, \(F = \mu R\).</p></div>
<ul>
<li>Friction only takes the value it needs to stop motion, up to the maximum \(\mu R\).</li>
<li>Friction opposes the motion <b>or the motion that would happen</b> (the tendency). Decide which way it would slide before you draw \(F\).</li>
<li>Smooth means \(\mu = 0\). Usually \(0 \le \mu \le 1\), but \(\mu\) can exceed 1 (tutorial Q7 uses \(\mu = 1.125\)).</li>
<li>Angle of friction: \(\tan\lambda = \mu\). On a slope with no other force, the particle is on the point of slipping when \(\tan\theta = \mu\).</li>
</ul>
<div class="tw"><table>
<tr><th>Applied push</th><th>Result</th></tr>
<tr><td>Less than \(\mu R\)</td><td>Stays at rest, \(F\) = push</td></tr>
<tr><td>Equal to \(\mu R\)</td><td>Limiting equilibrium, about to slip</td></tr>
<tr><td>Greater than \(\mu R\)</td><td>Moves; \(F = \mu R\) and use \(F_{\text{res}} = ma\)</td></tr>
</table></div>""", sec=S1))

    C.append(card("f-slope", "1 Forces & equilibrium", "Rough slopes and ranges", "Concept", r"""
<h2>Rough slopes: two critical cases</h2>
<figure class="dg">""" + slope_svg() + r"""<figcaption>Perpendicular: R = mg cos θ (plus any perpendicular component of P). Parallel: mg sin θ down the slope.</figcaption></figure>
<div class="two">
<div><h4 class="r">About to slip DOWN</h4><p>Friction acts <b>up</b> the slope. Gives the <b>least</b> \(P\):<br>\(P + \mu R = mg\sin\theta\)</p></div>
<div><h4 class="g">About to move UP</h4><p>Friction acts <b>down</b> the slope. Gives the <b>greatest</b> \(P\):<br>\(P = mg\sin\theta + \mu R\)</p></div>
</div>
<p>For any \(P\) between these two values, the particle stays at rest. Answer "range of values" as \(P_{\min} \le P \le P_{\max}\).</p>
<div class="note trap"><b>Trap</b>If \(P\) acts at an angle to the slope, \(R\) is different in the two cases' equations only if you forget it. \(R = mg\cos\theta - P\sin\alpha\) depends on \(P\), so substitute it in <b>before</b> solving for \(P\).</div>""", sec=S1))

    C.append(card("we-f1", "1 Forces & equilibrium", "Resultant of two pushes", "Worked example", r"""
<h2>The tractor: resultant of two forces</h2>
<p><b>Q (Forces note):</b> Two people push a tractor with forces 210 N at 15° above the horizontal and 190 N at 35° below the horizontal, in the same vertical plane. Find the resultant.</p>
<ol class="steps">
<li><b>Diagram, directions:</b> both forces point forward; take right (forward) and up as positive.</li>
<li>""" + tg("M1") + r""" Resolve horizontally: \(X = 210\cos15° + 190\cos35° = 202.84 + 155.64 = 358.48\ \text{N}\)</li>
<li>""" + tg("M1") + r""" Resolve vertically: \(Y = 210\sin15° - 190\sin35° = 54.35 - 108.98 = -54.63\ \text{N}\) (downward)</li>
<li>""" + tg("M1") + r""" \(R = \sqrt{358.48^2 + 54.63^2} = 363\ \text{N}\) """ + tg("A1") + r"""</li>
<li>\(\tan\alpha = \dfrac{54.63}{358.48}\Rightarrow \alpha = 8.66°\) <b>below the horizontal</b> """ + tg("A1") + r"""</li>
</ol>
<div class="note tip"><b>Why it works</b>Keep 5 s.f. in the working and round only at the end, or the angle drifts to 8.7°.</div>""", sec="Worked example · " + S1))

    C.append(card("we-f2", "1 Forces & equilibrium", "Range of P on a rough slope", "Worked example", r"""
<h2>Least P to stop slipping, least P to move it up</h2>
<p><b>Q (Forces note):</b> A block of weight 30 N is on a rough plane inclined at \(\theta\), \(\tan\theta = \frac34\). A force \(P\) N acts up the slope, parallel to it. \(\mu = \frac13\). Find the least \(P\) that (a) prevents slipping down, (b) makes it move up.</p>
<ol class="steps">
<li>\(\tan\theta = \frac34 \Rightarrow \sin\theta = 0.6,\ \cos\theta = 0.8\) (3-4-5 triangle).</li>
<li>""" + tg("M1") + r""" Perpendicular to slope: \(R = 30\cos\theta = 24\ \text{N}\), so \(F_{\max} = \frac13(24) = 8\ \text{N}\). Weight component down slope: \(30\sin\theta = 18\ \text{N}\).</li>
<li>""" + tg("M1") + r""" (a) About to slip <b>down</b>: friction acts <b>up</b>. Parallel: \(P + 8 = 18\), so \(P = 10\ \text{N}\) """ + tg("A1") + r"""</li>
<li>""" + tg("M1") + r""" (b) About to move <b>up</b>: friction acts <b>down</b>. Parallel: \(P = 18 + 8 = 26\ \text{N}\) """ + tg("A1") + r"""</li>
<li>So the block stays at rest for \(10 \le P \le 26\).</li>
</ol>
<div class="note trap"><b>Where marks go</b>Friction flips direction between parts. Same magnitude, opposite sign.</div>""", sec="Worked example · " + S1))

    # ------------------------------------------------------------ 2. Kinematics
    S2 = "2 · Kinematics"
    C.append(card("k-suvat", "2 Kinematics", "SUVAT", "Concept", r"""
<h2>Constant acceleration: SUVAT</h2>
<div class="tw"><table>
<tr><th>Equation</th><th>Missing</th></tr>
<tr><td>\(v = u + at\)</td><td>\(s\)</td></tr>
<tr><td>\(s = \frac12(u+v)t\)</td><td>\(a\)</td></tr>
<tr><td>\(s = ut + \frac12at^2\)</td><td>\(v\)</td></tr>
<tr><td>\(s = vt - \frac12at^2\)</td><td>\(u\)</td></tr>
<tr><td>\(v^2 = u^2 + 2as\)</td><td>\(t\)</td></tr>
</table></div>
<ul>
<li>List \(s, u, v, a, t\); circle the 3 you know and the 1 you want; pick the equation <b>missing</b> the 5th.</li>
<li>Displacement, velocity, acceleration are <b>vectors</b> (sign matters). Distance and speed are <b>scalars</b>.</li>
<li>Average velocity = net displacement ÷ total time. Average speed = total distance ÷ total time.</li>
</ul>
<div class="note trap"><b>Only for constant a</b>If \(a\) depends on \(t\) (e.g. \(v = 0.6t^2 - 0.12t^3\)), SUVAT is <b>wrong</b>. Use calculus.</div>
<div class="note tip"><b>Two unknowns?</b>Write two SUVAT equations for two stages from the <b>same start point</b> (e.g. A→B and A→C) and solve simultaneously. Quiz 1 Q1 and Assignment Q4 both do this.</div>""", sec=S2))

    C.append(card("k-vert", "2 Kinematics", "Vertical motion", "Concept", r"""
<h2>Vertical motion under gravity</h2>
<p>Ignoring air resistance, everything moves with \(a = g = 10\ \text{m s}^{-2}\) downward, whatever its mass.</p>
<ul>
<li>Choose <b>up positive</b> for a thrown-up object: \(u > 0\), \(a = -10\).</li>
<li>At the greatest height, \(v = 0\). Back at the start, \(s = 0\).</li>
<li>\(s = 25\) on the way up and on the way down gives <b>two</b> values of \(t\): the quadratic's two roots.</li>
<li>Two balls colliding: write \(s\) for each with its own start time (ball thrown 1 s later uses \(t - 1\)), then set positions equal.</li>
</ul>
<div class="note link"><b>From the note</b>Ball up at 30 m s⁻¹: greatest height \(0 = 900 - 20s \Rightarrow s = 45\) m; returns after \(0 = 30t - 5t^2 \Rightarrow t = 6\) s; at 25 m when \(5t^2 - 30t + 25 = 0\), so \(t = 1\) or \(5\) s.</div>
<div class="note trap"><b>Trap</b>Mixing signs: if up is positive, a ball dropped from 30 m ends at \(s = -30\), not \(+30\).</div>""", sec=S2))

    C.append(card("k-graph", "2 Kinematics", "Motion graphs", "Concept", r"""
<h2>Reading s–t and v–t graphs</h2>
<div class="two">
<div><h4>Displacement–time</h4><ul><li>Gradient = <b>velocity</b></li><li>Horizontal line = at rest</li><li>Curve = changing velocity</li></ul></div>
<div><h4 class="t">Velocity–time</h4><ul><li>Gradient = <b>acceleration</b></li><li>Area under = <b>displacement</b></li><li>Below the axis = moving backwards</li></ul></div>
</div>
""" + vt_fig() + r"""
<div class="note trap"><b>Distance vs displacement</b>If the v–t graph goes below the axis, <b>distance</b> = sum of the areas (all positive), <b>displacement</b> = area above − area below.</div>
<div class="note tip"><b>Trapezium shortcut</b>For accelerate–cruise–decelerate, area = \(\frac12(\text{top} + \text{bottom}) \times v\). With total distance given, this is often one equation in one unknown.</div>""", sec=S2))

    C.append(card("k-calc", "2 Kinematics", "Variable acceleration", "Concept", r"""
<h2>Variable acceleration: use calculus</h2>
<div class="chain"><span>\(s\)</span><i>→ d/dt →</i><span>\(v\)</span><i>→ d/dt →</i><span>\(a\)</span></div>
<div class="chain"><span>\(a\)</span><i>→ ∫ dt →</i><span>\(v\)</span><i>→ ∫ dt →</i><span>\(s\)</span></div>
<ul>
<li>Every indefinite integral needs \(+c\). Find it from the given condition ("starts from rest" ⇒ \(v = 0\) at \(t = 0\); "from O" ⇒ \(s = 0\) at \(t = 0\)).</li>
<li><b>Instantaneous rest</b>: solve \(v = 0\).</li>
<li><b>Maximum velocity</b>: solve \(a = \frac{dv}{dt} = 0\); justify with \(\frac{d^2v}{dt^2} < 0\).</li>
<li><b>Distance</b> between times: \(\int_{t_1}^{t_2} v\,dt\) — but split the integral wherever \(v\) changes sign and add the magnitudes.</li>
</ul>
<div class="note link"><b>From the note</b>Go-kart \(v = \frac1{10}t(36 - t)\): \(\frac{dv}{dt} = \frac{36 - 2t}{10} = 0 \Rightarrow t = 18\) s, \(v_{\max} = 32.4\ \text{m s}^{-1}\); \(\frac{d^2v}{dt^2} = -\frac15 < 0\), so a maximum.</div>""", sec=S2))

    C.append(card("we-k1", "2 Kinematics", "Two stages, same acceleration", "Worked example", r"""
<h2>Find a and u from two equal-time stages</h2>
<p><b>Q (Kinematics Quiz 1 Q1):</b> P moves along ABCD with constant acceleration. AB = 100 m, BC = 148 m; each takes 4 s. (a) Show \(a = 3\ \text{m s}^{-2}\) and find the speed at A. [6] (b) P reaches D at 61 m s⁻¹. Find CD. [3]</p>
<ol class="steps">
<li>Let \(u\) = speed at A. Use \(s = ut + \frac12at^2\) from A both times so \(u\) is the same unknown.</li>
<li>""" + tg("M1", "A1") + r""" A→B (\(t = 4\)): \(100 = 4u + 8a\)</li>
<li>""" + tg("M1", "A1") + r""" A→C (\(t = 8\), \(s = 248\)): \(248 = 8u + 32a\)</li>
<li>""" + tg("M1") + r""" Double the first: \(200 = 8u + 16a\). Subtract: \(48 = 16a\), so \(a = 3\) """ + tg("A1") + r""" (shown), then \(u = 19\ \text{m s}^{-1}\) """ + tg("A1") + r"""</li>
<li>""" + tg("B1") + r""" (b) Speed at C: \(v = 19 + 3(8) = 43\ \text{m s}^{-1}\).</li>
<li>""" + tg("M1") + r""" \(v^2 = u^2 + 2as\): \(61^2 = 43^2 + 6s \Rightarrow s = \dfrac{3721 - 1849}{6} = 312\ \text{m}\) """ + tg("A1") + r"""</li>
</ol>
<div class="note trap"><b>Common slip</b>Using B→C with \(u = 0\). The particle is still moving at B.</div>""", sec="Worked example · " + S2))

    C.append(card("we-k2", "2 Kinematics", "Variable velocity: distance to rest", "Worked example", r"""
<h2>"Show that OP = 6.25 m"</h2>
<p><b>Q (Kinematics Quiz 1 Q2a):</b> A particle starts from rest at O and comes to instantaneous rest at P. \(v = 0.6t^2 - 0.12t^3\). Show that OP = 6.25 m. [5]</p>
<ol class="steps">
<li>\(v\) is a function of \(t\) ⇒ acceleration not constant ⇒ <b>calculus, not SUVAT</b>.</li>
<li>""" + tg("M1") + r""" Rest at P: \(0.6t^2 - 0.12t^3 = t^2(0.6 - 0.12t) = 0 \Rightarrow t = 5\) (t = 0 is O) """ + tg("A1") + r"""</li>
<li>""" + tg("M1") + r""" Integrate: \(s = \int_0^5 (0.6t^2 - 0.12t^3)\,dt = \left[0.2t^3 - 0.03t^4\right]_0^5\) """ + tg("A1") + r"""</li>
<li>\(= 0.2(125) - 0.03(625) = 25 - 18.75 = 6.25\ \text{m}\) """ + tg("A1") + r""" (AG: answer given, so show every line)</li>
</ol>
<div class="note tip"><b>"Show that"</b>The answer is given, so the marks are for the working. Show the limits, the substituted values and the subtraction.</div>""", sec="Worked example · " + S2))

    C.append(card("we-k3", "2 Kinematics", "Overtaking problem", "Worked example", r"""
<h2>Cyclist and car: total time, then overtaking</h2>
<p><b>Q (Assignment 1 Q1):</b> A cyclist starts from rest at A, accelerates at 0.5 m s⁻² for 36 m, travels at constant speed for 25 s, then decelerates uniformly to rest at B. AB = 210 m. (a) Find the total time. [5] (b) 24 s after the cyclist leaves A, a car starts from rest at A with acceleration 4 m s⁻². It overtakes the cyclist during her constant-speed stage. Find the time from the cyclist's start until the car overtakes. [5]</p>
<ol class="steps">
<li>""" + tg("M1") + r""" Stage 1: \(v^2 = 0 + 2(0.5)(36) \Rightarrow v = 6\); \(t = 6 / 0.5 = 12\) s.</li>
<li>""" + tg("B1") + r""" Stage 2: \(6 \times 25 = 150\) m. Stage 3 distance: \(210 - 36 - 150 = 24\) m.</li>
<li>""" + tg("M1") + r""" Stage 3: \(24 = \frac12(6 + 0)t \Rightarrow t = 8\) s. Total \(= 12 + 25 + 8 = 45\) s """ + tg("A1") + r"""</li>
<li>""" + tg("M1") + r""" (b) Let \(T\) = time since the cyclist started. Cyclist (cruising): \(s = 36 + 6(T - 12)\). Car: \(s = \frac12(4)(T - 24)^2 = 2(T - 24)^2\).</li>
<li>""" + tg("M1") + r""" Equal: \(2(T - 24)^2 = 6T - 36 \Rightarrow T^2 - 51T + 594 = 0\) """ + tg("A1") + r"""</li>
<li>""" + tg("A1") + r""" \(T = 18\) or \(33\). \(T = 18\) is before the car starts, so \(T = 33\) s (and 33 is inside the cruise window 12–37 s ✓).</li>
</ol>
<div class="note trap"><b>Trap</b>Using the car's own clock for both. Put both on <b>one</b> time variable and shift the later starter by its delay.</div>""", sec="Worked example · " + S2))

    # ------------------------------------------------------------ 3. Newton's laws
    S3 = "3 · Newton's laws"
    C.append(card("n-laws", "3 Newton's laws", "F = ma and the forces", "Concept", r"""
<h2>Newton's second law: \(F_{\text{res}} = ma\)</h2>
<ol>
<li><b>First law:</b> no resultant force ⇒ rest or constant velocity.</li>
<li><b>Second law:</b> resultant force = rate of change of momentum = \(ma\) (constant mass).</li>
<li><b>Third law:</b> A on B is equal and opposite to B on A.</li>
</ol>
<div class="tw"><table>
<tr><th>Force</th><th>Direction / size</th></tr>
<tr><td class="k">Weight \(W = mg\)</td><td>Vertically down. Mass in kg, weight in N.</td></tr>
<tr><td class="k">Normal reaction \(R\)</td><td>Perpendicular to the surface, away from it.</td></tr>
<tr><td class="k">Friction \(F\)</td><td>Along the surface, against (attempted) motion; \(\le \mu R\).</td></tr>
<tr><td class="k">Tension \(T\)</td><td>Along the string, away from the body.</td></tr>
<tr><td class="k">Thrust</td><td>Along a rod, towards the body (pushing).</td></tr>
<tr><td class="k">Driving force \(D\)</td><td>Forward; from an engine (\(D = P/v\)).</td></tr>
<tr><td class="k">Resistance</td><td>Opposes motion. "0.5 N per kg" ⇒ \(0.5m\).</td></tr>
</table></div>
<div class="note tip"><b>Write it in this order</b>(forces in direction of \(a\)) − (forces against) \(= ma\). Then the sign of \(a\) is automatic.</div>""", sec=S3))

    C.append(card("n-slope", "3 Newton's laws", "Moving on a slope", "Concept", r"""
<h2>Moving on a slope</h2>
<ul>
<li>Perpendicular: no acceleration, so \(R = mg\cos\theta\) (± components of any angled force).</li>
<li>Parallel: \(F_{\text{res}} = ma\). Friction is now <b>exactly</b> \(\mu R\) because it's sliding.</li>
</ul>
<div class="formula">Sliding down: ma = mg sinθ − μ mg cosθ<br>Pushed up:   ma = P − mg sinθ − μ mg cosθ</div>
<div class="note link"><b>Exact trig</b>\(\sin\theta = 0.6 \Rightarrow \cos\theta = 0.8\); \(\sin\theta = \frac{7}{25} \Rightarrow \cos\theta = \frac{24}{25}\); \(\sin\theta = 0.05 \Rightarrow\) usually only \(\sin\theta\) is needed (no friction). Use exact values, not rounded angles.</div>
<div class="note trap"><b>Trap</b>When a particle slides up, stops, then slides back, friction <b>changes direction</b> and so does the acceleration. New stage, new equation.</div>
<h3>Lifts</h3>
<p>Person in a lift: \(R - mg = ma\) (up positive). Accelerating up or decelerating while moving down ⇒ \(R > mg\). Note: man of 70 kg, lift from rest to 10 m s⁻¹ in 2 s: \(a = 5\), \(R = 70(10 + 5) = 1050\) N.</p>""", sec=S3))

    C.append(card("n-conn", "3 Newton's laws", "Connected particles", "Concept", r"""
<h2>Connected particles: two equations, or one plus one</h2>
<div class="two">
<div><h4>Whole system</h4><p>Treat car + trailer as one body. Internal tension cancels. Gives \(a\) quickly.<br>\(D - R_1 - R_2 = (m_1 + m_2)a\)</p></div>
<div><h4 class="t">Separate body</h4><p>One particle on its own. Tension appears. Gives \(T\).<br>Trailer: \(T - R_2 = m_2a\)</p></div>
</div>
<p>Use the system equation to find \(a\), then the <b>simpler</b> single body (usually the one with fewer forces) to find \(T\).</p>
<h3>Strings over pulleys</h3>
<figure class="dg">""" + pulley_svg() + r"""<figcaption>Smooth light pulley, light inextensible string: same T on both sides, same size of acceleration. Each particle's positive direction is the way it moves.</figcaption></figure>
<div class="note trap"><b>Trap</b>You can't use a "whole system" equation for a string that changes direction unless you take "along the string" as the direction for each particle. Safer: write \(F = ma\) for each particle separately and add.</div>
<div class="note tip"><b>After the string goes slack</b>When the falling particle hits the floor, \(T = 0\). The other particle continues with its current speed and moves freely (\(a = -g\) if vertical, \(a = -g\sin\theta\) on a smooth slope).</div>""", sec=S3))

    C.append(card("we-n1", "3 Newton's laws", "Car and trailer", "Worked example", r"""
<h2>Car towing a trailer</h2>
<p><b>Q (Newton note):</b> Car 700 kg tows a trailer 200 kg on a horizontal road. Driving force 1220 N. Resistances: car 200 N, trailer 300 N. Find the acceleration and the tension in the tow-bar.</p>
<ol class="steps">
<li><b>Diagram:</b> car: \(1220\) forward, \(200\) back, \(T\) back. Trailer: \(T\) forward, \(300\) back. Positive = direction of motion.</li>
<li>""" + tg("M1") + r""" Whole system, \(F = ma\): \(1220 - 200 - 300 = 900a\)</li>
<li>\(a = \dfrac{720}{900} = 0.8\ \text{m s}^{-2}\) """ + tg("A1") + r"""</li>
<li>""" + tg("M1") + r""" Trailer alone: \(T - 300 = 200(0.8)\)</li>
<li>\(T = 460\ \text{N}\) """ + tg("A1") + r""". Check with the car: \(1220 - 200 - 460 = 560 = 700(0.8)\) ✓</li>
</ol>
<div class="note link"><b>Tension or thrust?</b>If your \(T\) comes out negative, the tow-bar is in <b>thrust</b> (pushing). That's the point of the note's caravan-uphill example: say which it is.</div>""", sec="Worked example · " + S3))

    C.append(card("we-n2", "3 Newton's laws", "Pulley: after B lands", "Worked example", r"""
<h2>Pulley system, then free motion</h2>
<p><b>Q (Newton's 2nd law sheet Q6):</b> A (3 kg) and B (5 kg) hang over a smooth pulley, string taut. A is 1 m above a horizontal plane, B is 2 m above it. Released from rest; B stays on the plane once it lands; A doesn't reach the pulley. (a) Find \(T\) and the time for B to reach the plane. (b) Find the time for which A is at least 3.25 m above the plane.</p>
<ol class="steps">
<li>""" + tg("M1") + r""" B (down +): \(50 - T = 5a\). A (up +): \(T - 30 = 3a\).</li>
<li>""" + tg("M1") + r""" Add: \(20 = 8a \Rightarrow a = 2.5\ \text{m s}^{-2}\); \(T = 30 + 7.5 = 37.5\ \text{N}\) """ + tg("A1") + r"""</li>
<li>""" + tg("M1") + r""" B falls 2 m: \(2 = \frac12(2.5)t^2 \Rightarrow t = \sqrt{1.6} = 1.26\ \text{s}\) """ + tg("A1") + r"""</li>
<li>""" + tg("B1") + r""" (b) When B lands, A has risen 2 m to 3 m, with \(v^2 = 2(2.5)(2) = 10\), \(v = \sqrt{10}\).</li>
<li>""" + tg("M1") + r""" String slack ⇒ A moves freely, \(a = -10\). Height above plane: \(3 + \sqrt{10}\,t - 5t^2 \ge 3.25\)</li>
<li>""" + tg("M1") + r""" \(5t^2 - \sqrt{10}\,t + 0.25 = 0\): roots differ by \(\dfrac{\sqrt{10 - 5}}{5} = 0.447\ \text{s}\) """ + tg("A1") + r"""</li>
</ol>
<div class="note tip"><b>Shortcut</b>The time between the two roots of \(at^2 + bt + c = 0\) is \(\dfrac{\sqrt{b^2 - 4ac}}{a}\).</div>""", sec="Worked example · " + S3))

    C.append(card("we-n3", "3 Newton's laws", "Rough slope and hanging particle", "Worked example", r"""
<h2>Pulley at the bottom of a rough slope</h2>
<p><b>Q (Newton's 2nd law sheet Q7):</b> A (0.2 kg) on a rough plane, \(\sin\theta = 0.6\), \(\mu = 1.125\), is joined over a smooth pulley at the bottom of the plane to B (0.3 kg) hanging 0.25 m above the ground. Released from rest. (a) Find \(T\) and \(a\). (b) B lands and stops. Find the total distance A travels down the plane.</p>
<ol class="steps">
<li>""" + tg("B1") + r""" A: \(R = 0.2(10)(0.8) = 1.6\ \text{N}\), so \(F = 1.125(1.6) = 1.8\ \text{N}\), acting <b>up</b> the slope (A moves down).</li>
<li>""" + tg("M1") + r""" A (down slope +): \(T + 0.2(10)(0.6) - 1.8 = 0.2a \Rightarrow T + 1.2 - 1.8 = 0.2a\)</li>
<li>""" + tg("M1") + r""" B (down +): \(3 - T = 0.3a\). Add: \(2.4 = 0.5a \Rightarrow a = 4.8\ \text{m s}^{-2}\), \(T = 3 - 1.44 = 1.56\ \text{N}\) """ + tg("A1", "A1") + r"""</li>
<li>""" + tg("M1") + r""" After 0.25 m: \(v^2 = 2(4.8)(0.25) = 2.4\).</li>
<li>""" + tg("M1") + r""" String slack: A has \(1.2\) N down slope, \(1.8\) N friction up slope ⇒ deceleration \(= \dfrac{0.6}{0.2} = 3\ \text{m s}^{-2}\).</li>
<li>""" + tg("A1") + r""" \(0 = 2.4 - 2(3)s \Rightarrow s = 0.4\) m. Total \(= 0.25 + 0.4 = 0.65\ \text{m}\).</li>
</ol>
<div class="note trap"><b>Trap</b>Keeping \(T\) in the second stage. Once B lands, the string is slack: \(T = 0\).</div>""", sec="Worked example · " + S3))

    # ------------------------------------------------------------ 4. Momentum
    S4 = "4 · Momentum"
    C.append(card("m-con", "4 Momentum", "Conservation of momentum", "Concept", r"""
<h2>Momentum is conserved in a collision</h2>
<div class="def"><div class="lab">Momentum <i>vector, N s or kg m s⁻¹</i></div><p>\(p = mv\)</p></div>
<div class="def"><div class="lab">Conservation of linear momentum</div>
<p>\(m_Au_A + m_Bu_B = m_Av_A + m_Bv_B\)</p>
<p>Coalesce: \(m_Au_A + m_Bu_B = (m_A + m_B)v\)</p></div>
<ul>
<li><b>Pick one positive direction</b> and keep it for every velocity, before and after. Anything moving the other way is negative.</li>
<li>Unknown velocity? Leave it as \(+v\); a negative answer just means it moves the other way.</li>
<li>Change in momentum of one body = \(m(v - u)\), with signs. Rebounding ball: \(u = -3,\ v = +6\) gives \(\Delta p = 9m\), not \(3m\).</li>
<li>Kinetic energy is <b>not</b> usually conserved: loss of KE = KE before − KE after (common follow-up).</li>
<li>Chain collisions (A hits B, B hits C): apply conservation to <b>each</b> collision separately.</li>
</ul>
<div class="note tip"><b>Combine with kinematics</b>Momentum questions often need SUVAT first (speed just before impact) and after (where the coalesced object lands). The note's balls X and Y do both.</div>""", sec=S4))

    C.append(card("we-m1", "4 Momentum", "Head-on collision", "Worked example", r"""
<h2>Opposite directions before impact</h2>
<p><b>Q (Momentum note):</b> P (0.5 kg) and Q (0.2 kg) move towards each other at 8 m s⁻¹ and 2 m s⁻¹. After the collision P's direction is unchanged and Q's speed is double P's. Find (a) P's speed after, (b) the change in Q's momentum.</p>
<ol class="steps">
<li><b>Direction:</b> P's original direction positive. Before: \(u_P = 8,\ u_Q = -2\). After: \(v_P = v,\ v_Q = 2v\) (Q must now move in P's direction, ahead of it).</li>
<li>""" + tg("M1") + r""" CoM: \(0.5(8) + 0.2(-2) = 0.5v + 0.2(2v)\) """ + tg("A1") + r"""</li>
<li>\(3.6 = 0.9v \Rightarrow v = 4\ \text{m s}^{-1}\) """ + tg("A1") + r"""</li>
<li>""" + tg("M1") + r""" (b) \(\Delta p_Q = 0.2(8 - (-2)) = 2\ \text{N s}\) in P's original direction """ + tg("A1") + r"""</li>
</ol>
<div class="note trap"><b>Biggest momentum error</b>Writing \(0.2(2)\) instead of \(0.2(-2)\) for Q before impact. Signs come from your chosen direction, not from the word "speed".</div>""", sec="Worked example · " + S4))

    C.append(card("we-m2", "4 Momentum", "Coalescing particles", "Worked example", r"""
<h2>Find u when the particles coalesce</h2>
<p><b>Q (Momentum note):</b> A (2 kg) and B (3 kg) move towards each other with speeds \(u\) and \(2u\) m s⁻¹. They coalesce and move in B's original direction at 4 m s⁻¹. Find \(u\).</p>
<ol class="steps">
<li><b>Direction:</b> B's original direction positive, so A's velocity is \(-u\).</li>
<li>""" + tg("M1") + r""" \(3(2u) + 2(-u) = (2 + 3)(4)\) """ + tg("A1") + r"""</li>
<li>\(4u = 20 \Rightarrow u = 5\) """ + tg("A1") + r"""</li>
<li>Follow-up you might get: KE lost \(= \frac12(2)(5^2) + \frac12(3)(10^2) - \frac12(5)(4^2) = 25 + 150 - 40 = 135\ \text{J}\).</li>
</ol>""", sec="Worked example · " + S4))

    # ------------------------------------------------------------ 5. Energy, work, power
    S5 = "5 · Work, energy &amp; power"
    C.append(card("e-work", "5 Work, energy & power", "Work, KE, PE", "Concept", r"""
<h2>Work and energy</h2>
<div class="tw"><table>
<tr><th>Quantity</th><th>Formula</th><th>Note</th></tr>
<tr><td class="k">Work done by a force</td><td>\(W = Fs\cos\theta\)</td><td>\(\theta\) between force and displacement. J.</td></tr>
<tr><td class="k">Kinetic energy</td><td>\(\frac12mv^2\)</td><td>Scalar: direction doesn't matter.</td></tr>
<tr><td class="k">Gravitational PE</td><td>\(mgh\)</td><td>\(h\) is <b>vertical</b> height; state the zero level.</td></tr>
<tr><td class="k">WD against gravity on a slope</td><td>\(mg \times (d\sin\theta)\)</td><td>Only the vertical rise counts.</td></tr>
<tr><td class="k">WD against friction</td><td>\(\mu R \times d\)</td><td>Distance along the surface.</td></tr>
</table></div>
<div class="def"><div class="lab">Work–energy principle</div>
<p>WD by driving force − WD against resistance<br>\(= \Delta KE + \Delta PE\)</p>
<p>No resistances and no driving force ⇒ \(KE + PE\) is conserved.</p></div>
<div class="note tip"><b>When to use energy</b>When the question gives distances or heights but no time, or the resistance isn't constant (only its work is given). Energy can't give you time directly.</div>
<div class="note trap"><b>Trap</b>Using the slope length \(d\) for \(h\) in \(mgh\). Height gained = \(d\sin\theta\).</div>""", sec=S5))

    C.append(card("e-power", "5 Work, energy & power", "Power", "Concept", r"""
<h2>Power: the rate of doing work</h2>
<div class="def"><div class="lab">Power <i>W = J s⁻¹</i></div>
<p>\(P = \dfrac{\text{work done}}{\text{time}}\), and for a driving force at speed \(v\): \(P = Dv\)</p></div>
<div class="chain"><span>Given \(P\) and \(v\)</span><i>→</i><span>\(D = \dfrac{P}{v}\)</span><i>→</i><span>\(D - R - mg\sin\theta = ma\)</span></div>
<ul>
<li><b>Maximum / steady speed</b>: \(a = 0\), so \(D = R\) (+ \(mg\sin\theta\) uphill, − downhill). Then \(v_{\max} = P / D\).</li>
<li>kW ⇒ ×1000. "Working at 4 kW" means \(P = 4000\).</li>
<li>Power constant over a time \(t\) ⇒ work done by the engine \(= Pt\) (use it in the work–energy equation).</li>
</ul>
<div class="note trap"><b>Trap</b>\(P = Fv\) uses the <b>driving force</b>, not the resultant force. Find \(D\) first, then put it into \(F = ma\).</div>""", sec=S5))

    C.append(card("we-e1", "5 Work, energy & power", "μ from energy", "Worked example", r"""
<h2>Coefficient of friction by energy</h2>
<p><b>Q (Energy note):</b> A 10 kg box slides 3 m down a rough slope at 30°. Its speed rises from 3.25 m s⁻¹ to 5 m s⁻¹. Find \(\mu\).</p>
<ol class="steps">
<li>""" + tg("B1") + r""" PE lost \(= 10(10)(3\sin30°) = 150\ \text{J}\).</li>
<li>""" + tg("B1") + r""" KE gained \(= \frac12(10)(5^2 - 3.25^2) = 72.19\ \text{J}\).</li>
<li>""" + tg("M1") + r""" Work–energy: WD against friction = PE lost − KE gained \(= 77.81\ \text{J}\).</li>
<li>""" + tg("M1") + r""" \(R = 10(10)\cos30° = 86.60\ \text{N}\), so WD \(= \mu(86.60)(3)\).</li>
<li>\(\mu = \dfrac{77.81}{259.8} = 0.300\) """ + tg("A1") + r"""</li>
</ol>
<div class="note link"><b>Same answer by Newton</b>\(a = \frac{25 - 10.5625}{6} = 2.406\); \(10a = 50 - \mu(86.6)\) ⇒ \(\mu = 0.300\). Pick whichever is fewer lines.</div>""", sec="Worked example · " + S5))

    C.append(card("we-e2", "5 Work, energy & power", "Car with constant power", "Worked example", r"""
<h2>Acceleration and top speed at constant power</h2>
<p><b>Q (MJ2023/41/Q7 a–b):</b> A car of mass 1200 kg on a horizontal road. Engine power constant at 16 kW. Resistance 500 N. (a) Find the acceleration when the speed is 20 m s⁻¹. [3] (b) Find the steady speed. [2]</p>
<ol class="steps">
<li>""" + tg("M1") + r""" \(D = \dfrac{P}{v} = \dfrac{16\,000}{20} = 800\ \text{N}\)</li>
<li>""" + tg("M1") + r""" \(F = ma\): \(800 - 500 = 1200a\)</li>
<li>\(a = 0.25\ \text{m s}^{-2}\) """ + tg("A1") + r"""</li>
<li>""" + tg("M1") + r""" (b) Steady ⇒ \(a = 0\) ⇒ \(D = 500\): \(\dfrac{16\,000}{v} = 500\)</li>
<li>\(v = 32\ \text{m s}^{-1}\) """ + tg("A1") + r"""</li>
</ol>
<div class="note tip"><b>Part (c) style</b>On the hill the resistance varies, so only its work is given. Use work–energy: \(Pt - \text{WD}_{\text{res}} = \Delta KE + mg(d\sin\theta)\).</div>""", sec="Worked example · " + S5))

    # ------------------------------------------------------------ exam
    C.append(card("traps", "Exam", "Common mistakes", "Traps", r"""
<h2>Where Paper 4 marks disappear</h2>
<div class="tw"><table>
<tr><th>Mistake</th><th>Fix</th></tr>
<tr><td>\(R = mg\) when a force pulls at an angle</td><td>Resolve vertically every time; \(R = mg - P\sin\alpha\).</td></tr>
<tr><td>Friction in the wrong direction</td><td>Ask "which way would it slide?" Friction points the other way.</td></tr>
<tr><td>\(\sin\) / \(\cos\) swapped on a slope</td><td>Down the slope: \(mg\sin\theta\). Into the slope: \(mg\cos\theta\).</td></tr>
<tr><td>Mass for weight (\(m\) instead of \(mg\))</td><td>Forces in N; \(W = 10m\). Check units of each term.</td></tr>
<tr><td>Different tensions either side of a smooth pulley</td><td>Light string, smooth pulley ⇒ one \(T\).</td></tr>
<tr><td>Sign error in momentum</td><td>One positive direction, every velocity signed.</td></tr>
<tr><td>SUVAT with variable acceleration</td><td>If \(a\) or \(v\) is given as a function of \(t\), use calculus.</td></tr>
<tr><td>Forgetting \(+c\)</td><td>Use the initial condition to find it.</td></tr>
<tr><td>\(P = Fv\) with the resultant force</td><td>\(F\) here is the <b>driving</b> force.</td></tr>
<tr><td>Slope length used as height</td><td>\(h = d\sin\theta\).</td></tr>
<tr><td>Tension kept after string goes slack</td><td>Particle lands ⇒ \(T = 0\); new stage.</td></tr>
<tr><td>Rounding early</td><td>Carry 4–5 s.f.; give 3 s.f. (angles to 1 d.p.).</td></tr>
</table></div>""", sec="Exam technique"))

    C.append(card("tech", "Exam", "Exam technique", "Strategy", r"""
<h2>How to sit Paper 4</h2>
<ul>
<li><b>Timing:</b> 50 marks in 75 min ⇒ 1.5 min per mark. Leave 8 minutes to check signs and units.</li>
<li><b>Diagram first</b>, even when one is printed: add every force, the direction of \(a\), and your positive direction.</li>
<li><b>Name the principle</b> on the line: "N2L for A:", "Resolving ⊥ to the plane:", "CoM:", "Work–energy:". Examiners look for it before awarding M1.</li>
<li><b>One equation per particle</b> in connected systems. Add them to eliminate \(T\).</li>
<li><b>"Show that"</b>: answer given, so every step must appear; don't work backwards from it.</li>
<li><b>g = 10</b> and 3 s.f. unless told otherwise. Exact answers (fractions, surds) are fine if exact.</li>
<li><b>Multi-stage questions</b> (slack strings, braking, bounce): the end speed of one stage is the start speed of the next. Write it down clearly so follow-through marks apply.</li>
</ul>
<div class="note tip"><b>Which tool?</b>Time involved ⇒ SUVAT / \(F = ma\). Heights and distances only ⇒ energy. Impact ⇒ momentum. At rest ⇒ resolve.</div>""", sec="Exam technique"))

    C.append(card("pr1", "Practice", "Practice: forces and kinematics", "Practice", r"""
<h2>Practice · Forces and kinematics</h2>
<p class="lede">Do these on paper or in "Write your working", then reveal.</p>
<div class="pq"><div class="qh"><span>Q1 · Forces note</span><span class="mk">[5]</span></div>
<p class="qt">A book of mass 8 kg is at rest on a rough slope at 20° to the horizontal, held in limiting equilibrium by a force of 10 N up the line of greatest slope. (a) Find \(\mu\). (b) Find the largest force up the slope for which the book stays at rest.</p>
<div class="ans"><b>Answer</b>(a) Friction acts up the slope: \(10 + \mu(80\cos20°) = 80\sin20°\), so \(\mu = 0.231\). (b) Friction now acts down the slope: \(P = 80\sin20° + 0.231(80\cos20°) = 44.7\ \text{N}\).</div></div>
<div class="pq"><div class="qh"><span>Q2 · Newton sheet Q2</span><span class="mk">[6]</span></div>
<p class="qt">A particle of mass 0.8 kg on a rough plane inclined at 28° is held in equilibrium by a force \(T\) N acting at 35° above a line of greatest slope. \(\mu = 0.2\). Find the least and greatest possible values of \(T\).</p>
<div class="ans"><b>Answer</b>\(R = 8\cos28° - T\sin35°\). Least (friction up): \(T\cos35° + 0.2R = 8\sin28°\) ⇒ \(T = 3.33\) N. Greatest (friction down): \(T\cos35° = 8\sin28° + 0.2R\) ⇒ \(T = 5.53\) N.</div></div>
<div class="pq"><div class="qh"><span>Q3 · Assignment 1 Q4</span><span class="mk">[6]</span></div>
<p class="qt">A car with initial speed \(u\) and constant acceleration \(a\) takes 5 s for the first 80 m and 8 s for the first 160 m. Find \(a\) and \(u\).</p>
<div class="ans"><b>Answer</b>\(80 = 5u + 12.5a\), \(160 = 8u + 32a\). Solving: \(a = \frac83 = 2.67\ \text{m s}^{-2}\), \(u = \frac{28}{3} = 9.33\ \text{m s}^{-1}\).</div></div>
<div class="pq"><div class="qh"><span>Q4 · Kinematics Quiz 1 Q2(b)(c)</span><span class="mk">[7]</span></div>
<p class="qt">Now \(s = kt^3 + ct^5\). The particle passes P (\(s = 6.25\)) with velocity 1.25 m s⁻¹ at \(t = 5\). Find \(k\) and \(c\), then the acceleration at \(t = 5\).</p>
<div class="ans"><b>Answer</b>\(125k + 3125c = 6.25\); \(v = 3kt^2 + 5ct^4\) ⇒ \(75k + 3125c = 1.25\). Subtract: \(k = 0.1\), \(c = -0.002\). \(a = 6kt + 20ct^3 = 3 - 5 = -2\ \text{m s}^{-2}\).</div></div>""", sec="Practice · 1–2"))

    C.append(card("pr2", "Practice", "Practice: Newton's laws", "Practice", r"""
<h2>Practice · Newton's laws</h2>
<div class="pq"><div class="qh"><span>Q5 · Newton sheet Q1</span><span class="mk">[6]</span></div>
<p class="qt">A bobsled starts at the top of a 60 m slope inclined at 12°, speed 5 m s⁻¹, and slides straight down. (a) With no resistance, find its speed at the bottom. (b) If instead \(\mu = 0.03\), find the time to reach the bottom.</p>
<div class="ans"><b>Answer</b>(a) \(a = 10\sin12° = 2.079\); \(v^2 = 25 + 2(2.079)(60)\) ⇒ \(v = 16.6\ \text{m s}^{-1}\). (b) \(a = 10(\sin12° - 0.03\cos12°) = 1.786\); \(60 = 5t + 0.893t^2\) ⇒ \(t = 5.86\) s.</div></div>
<div class="pq"><div class="qh"><span>Q6 · Newton sheet Q3</span><span class="mk">[9]</span></div>
<p class="qt">A van (4500 kg) tows a trailer (750 kg) down a hill, \(\sin\theta = 0.05\), by a light rigid tow-bar. Resistances: van 2500 N, trailer 300 N. (a) Tension is 450 N: find the trailer's acceleration and the van's driving force. (b) Uphill, \(\sin\alpha = 0.09\), driving force 9100 N, speed 20 m s⁻¹ at the bottom: find \(a\), the tension, and the speed after 375 m.</p>
<div class="ans"><b>Answer</b>(a) Trailer: \(450 + 375 - 300 = 750a\) ⇒ \(a = 0.7\); van: \(D + 2250 - 2500 - 450 = 4500(0.7)\) ⇒ \(D = 3850\) N. (b) System: \(9100 - 4725 - 2800 = 5250a\) ⇒ \(a = 0.3\); trailer: \(T - 675 - 300 = 225\) ⇒ \(T = 1200\) N; \(v^2 = 400 + 2(0.3)(375)\) ⇒ \(v = 25\ \text{m s}^{-1}\).</div></div>""", sec="Practice · 3"))

    C.append(card("pr3", "Practice", "Practice: momentum and energy", "Practice", r"""
<h2>Practice · Momentum, energy, power</h2>
<div class="pq"><div class="qh"><span>Q7 · Momentum note</span><span class="mk">[3]</span></div>
<p class="qt">A 2 kg particle at 5 m s⁻¹ hits a stationary 8 kg particle. Afterwards the 2 kg particle moves at 3 m s⁻¹ in the reverse direction. Find the speed of the 8 kg particle.</p>
<div class="ans"><b>Answer</b>\(2(5) + 0 = 2(-3) + 8v\) ⇒ \(v = 2\ \text{m s}^{-1}\).</div></div>
<div class="pq"><div class="qh"><span>Q8 · Momentum note</span><span class="mk">[4]</span></div>
<p class="qt">A (0.01 kg), B (0.06 kg), C (0.12 kg) are at rest in a line on a smooth surface, B between. A is given 4 m s⁻¹ towards B, rebounds at 2 m s⁻¹; B then hits C and comes to rest. Find C's speed.</p>
<div class="ans"><b>Answer</b>First: \(0.04 = -0.02 + 0.06v_B\) ⇒ \(v_B = 1\). Second: \(0.06(1) = 0.12v_C\) ⇒ \(v_C = 0.5\ \text{m s}^{-1}\).</div></div>
<div class="pq"><div class="qh"><span>Q9 · MJ2023/41/Q2</span><span class="mk">[6]</span></div>
<p class="qt">P (0.4 kg) is projected vertically upwards from the ground at 10 m s⁻¹. (a) Find the greatest height. (b) On first hitting the ground it loses 7.2 J and bounces vertically. Find the time between the first and second impacts.</p>
<div class="ans"><b>Answer</b>(a) \(0 = 100 - 20h\) ⇒ \(h = 5\) m. (b) KE at impact \(= 20\) J, after \(= 12.8\) J ⇒ \(v = 8\); time up and down \(= 2(8)/10 = 1.6\) s.</div></div>
<div class="pq"><div class="qh"><span>Q10 · Energy note</span><span class="mk">[3]</span></div>
<p class="qt">A crate of mass 50 kg slides across a rough horizontal floor from 3 m s⁻¹ to rest in 4 m. Find \(\mu\).</p>
<div class="ans"><b>Answer</b>KE lost \(= 225\) J \(= \mu(500)(4)\) ⇒ \(\mu = 0.1125 = 0.113\).</div></div>
<div class="pq"><div class="qh"><span>Q11 · Energy note</span><span class="mk">[4]</span></div>
<p class="qt">A car of mass 800 kg on a level road, resistance 0.5 N per kg, engine at 4 kW. Find (a) the acceleration at 8 m s⁻¹, (b) the maximum speed.</p>
<div class="ans"><b>Answer</b>Resistance \(= 400\) N. (a) \(D = 500\); \(500 - 400 = 800a\) ⇒ \(a = 0.125\ \text{m s}^{-2}\). (b) \(4000/v = 400\) ⇒ \(v = 10\ \text{m s}^{-1}\).</div></div>
<div class="pq"><div class="qh"><span>Q12 · Momentum note</span><span class="mk">[4]</span></div>
<p class="qt">Carts A (1.2 kg) and B (2.4 kg) move the same way at 9 and 3 m s⁻¹. A collides with B and slows to 1 m s⁻¹. Find B's new velocity and the KE lost.</p>
<div class="ans"><b>Answer</b>\(10.8 + 7.2 = 1.2 + 2.4v\) ⇒ \(v = 7\ \text{m s}^{-1}\). KE before \(= 48.6 + 10.8 = 59.4\) J; after \(= 0.6 + 58.8 = 59.4\) J ⇒ no KE lost (a perfectly elastic collision).</div></div>""", sec="Practice · 4–5"))

    C.append(card("sheet", "Summary", "Formula sheet", "Summary", r"""
<h2>Everything to remember</h2>
<div class="tw"><table>
<tr><th>Topic</th><th>Formulae</th></tr>
<tr><td class="k">Resolving</td><td>\(F\cos\theta,\ F\sin\theta\); \(R = \sqrt{X^2 + Y^2}\), \(\tan\alpha = Y/X\)</td></tr>
<tr><td class="k">Equilibrium</td><td>\(\sum F_x = 0,\ \sum F_y = 0\)</td></tr>
<tr><td class="k">Friction</td><td>\(F \le \mu R\); limiting/sliding \(F = \mu R\)</td></tr>
<tr><td class="k">Slope</td><td>\(R = mg\cos\theta\); down-slope \(mg\sin\theta\)</td></tr>
<tr><td class="k">SUVAT</td><td>\(v = u + at\); \(s = \frac12(u+v)t\); \(s = ut + \frac12at^2\); \(s = vt - \frac12at^2\); \(v^2 = u^2 + 2as\)</td></tr>
<tr><td class="k">Calculus</td><td>\(v = \frac{ds}{dt}\), \(a = \frac{dv}{dt}\); \(s = \int v\,dt\), \(v = \int a\,dt\)</td></tr>
<tr><td class="k">Newton II</td><td>\(F_{\text{res}} = ma\); \(W = mg\)</td></tr>
<tr><td class="k">Momentum</td><td>\(p = mv\); \(m_1u_1 + m_2u_2 = m_1v_1 + m_2v_2\)</td></tr>
<tr><td class="k">Work</td><td>\(W = Fs\cos\theta\)</td></tr>
<tr><td class="k">Energy</td><td>\(KE = \frac12mv^2\), \(PE = mgh\); WD = \(\Delta KE + \Delta PE\)</td></tr>
<tr><td class="k">Power</td><td>\(P = \frac{W}{t} = Dv\); max speed when \(a = 0\)</td></tr>
</table></div>
<div class="note tip"><b>Last check before you write the answer</b>Units? 3 s.f.? Direction stated for vectors? Tension or thrust stated?</div>""", sec="Summary"))
    return C


FLASH = [
    ["Modelling", "What does 'light' imply for a string?", "Its mass is ignored, so the tension is the same throughout the string."],
    ["Modelling", "What does 'inextensible' imply for connected particles?", "They have the same magnitude of acceleration (and speed)."],
    ["Modelling", "What does 'smooth' mean?", "No friction acts at that contact (μ = 0)."],
    ["Modelling", "What does 'limiting equilibrium' mean?", "On the point of moving: a = 0 and friction is at its maximum, F = μR."],
    ["Modelling", "What does 'modelled as a particle' let you ignore?", "Size and rotation: all forces act at a single point."],
    ["Modelling", "Rod vs string: what can a rod do that a string can't?", "Be in thrust (push). A string can only be in tension."],
    ["Forces", "Components of force F at angle θ to the x-axis?", "F cos θ along x, F sin θ along y."],
    ["Forces", "Condition for equilibrium?", "Resultant force zero: sum of components in each of two perpendicular directions is zero."],
    ["Forces", "On a slope at θ, the weight's components?", "mg sin θ down the slope, mg cos θ into the slope."],
    ["Forces", "Friction law?", "0 ≤ F ≤ μR, with F = μR when limiting or sliding."],
    ["Forces", "On a rough slope, which case gives the least P (up the slope)?", "About to slip down: friction acts up the slope, P + μR = mg sin θ."],
    ["Forces", "A particle on a slope with only W, R, F is about to slip. Link θ and μ?", "μ = tan θ."],
    ["Forces", "Why isn't R always mg?", "Any other force with a perpendicular component (pull at an angle, push down) changes R."],
    ["Kinematics", "Gradient of a displacement–time graph?", "Velocity."],
    ["Kinematics", "Gradient and area of a velocity–time graph?", "Gradient = acceleration; area = displacement."],
    ["Kinematics", "When is SUVAT not allowed?", "When acceleration isn't constant, e.g. v or a given as a function of t."],
    ["Kinematics", "How to find maximum velocity from v(t)?", "Solve dv/dt = 0; confirm with d²v/dt² < 0."],
    ["Kinematics", "Ball thrown up at 30 m/s: greatest height?", "0 = 900 − 20s ⇒ 45 m."],
    ["Kinematics", "Distance vs displacement on a v–t graph crossing the axis?", "Distance adds all areas as positive; displacement subtracts areas below the axis."],
    ["Newton", "Newton's second law?", "Resultant force = rate of change of momentum = ma (constant mass)."],
    ["Newton", "Connected particles: fastest way to a, then T?", "Whole-system equation for a, then one particle on its own for T."],
    ["Newton", "Person in a lift accelerating upwards: R vs mg?", "R − mg = ma, so R > mg."],
    ["Newton", "Particle lands and string goes slack: what changes?", "T = 0; the other particle moves freely with its current speed."],
    ["Newton", "Tow-bar force comes out negative. Meaning?", "It's a thrust, not a tension."],
    ["Momentum", "Principle of conservation of momentum?", "Total momentum before = total after, for a collision with no external impulse."],
    ["Momentum", "Formula when particles coalesce?", "m₁u₁ + m₂u₂ = (m₁ + m₂)v."],
    ["Momentum", "Ball of 0.2 kg hits a wall at 3 m/s, rebounds at 2 m/s. Change in momentum?", "0.2(2 − (−3)) = 1 N s, away from the wall."],
    ["Momentum", "Is KE conserved in collisions?", "Not usually. KE lost = KE before − KE after."],
    ["Energy", "Work done by force F through s at angle θ?", "Fs cos θ."],
    ["Energy", "Work–energy principle?", "WD by driving − WD against resistance = ΔKE + ΔPE."],
    ["Energy", "Particle moves d up a slope at θ: gain in PE?", "mg d sin θ."],
    ["Power", "Power of an engine at speed v with driving force D?", "P = Dv."],
    ["Power", "Condition for maximum (steady) speed?", "a = 0, so driving force = resistance (+ mg sin θ uphill)."],
    ["Exam", "Default g and accuracy in 9709 Paper 4?", "g = 10 m s⁻², answers to 3 s.f. (angles 1 d.p.)."],
]

QUIZ = [
    {"s": "Forces", "q": "A 5 kg block rests on a horizontal floor. A force of 20 N pulls it at 30° above the horizontal. What is R?",
     "o": ["50 N", "40 N", "60 N", "32.7 N"], "c": 1,
     "e": "Vertically: R + 20 sin30° = 50, so R = 40 N. A forgets the pull's vertical component; C adds it the wrong way."},
    {"s": "Forces", "q": "A particle is in limiting equilibrium on a rough slope at 30° with no other applied force. What is μ?",
     "o": ["0.5", "0.577", "0.866", "1.73"], "c": 1,
     "e": "mg sinθ = μ mg cosθ ⇒ μ = tan 30° = 0.577."},
    {"s": "Forces", "q": "A 30 N block on a slope with sinθ = 0.6, μ = ⅓. A force P acts up the slope. The block is about to move UP. P = ?",
     "o": ["10 N", "18 N", "26 N", "8 N"], "c": 2,
     "e": "R = 24, μR = 8. About to move up ⇒ friction down: P = 18 + 8 = 26 N. A is the 'about to slip down' case."},
    {"s": "Kinematics", "q": "A car accelerates uniformly from 4 to 12 m s⁻¹ in 4 s. Distance covered?",
     "o": ["32 m", "48 m", "16 m", "64 m"], "c": 0,
     "e": "s = ½(u + v)t = ½(16)(4) = 32 m."},
    {"s": "Kinematics", "q": "v = 0.6t² − 0.12t³ for t ≥ 0. When is the particle next at instantaneous rest?",
     "o": ["t = 2.5 s", "t = 5 s", "t = 0.2 s", "t = 3.33 s"], "c": 1,
     "e": "t²(0.6 − 0.12t) = 0 ⇒ t = 5. D (t = 3.33) is where acceleration is zero (maximum v)."},
    {"s": "Kinematics", "q": "Which is TRUE for a velocity–time graph?",
     "o": ["Area = acceleration", "Gradient = displacement", "Area = displacement", "Gradient = velocity"], "c": 2,
     "e": "v–t: gradient is acceleration, area is displacement. Gradient = velocity is the s–t graph."},
    {"s": "Newton", "q": "Car 700 kg tows trailer 200 kg. D = 1220 N, resistances 200 N (car) and 300 N (trailer). Tension?",
     "o": ["300 N", "460 N", "560 N", "720 N"], "c": 1,
     "e": "System: a = 720/900 = 0.8. Trailer: T − 300 = 160 ⇒ T = 460 N."},
    {"s": "Newton", "q": "A 3 kg and a 5 kg particle hang over a smooth pulley. Acceleration?",
     "o": ["2 m s⁻²", "2.5 m s⁻²", "4 m s⁻²", "6.25 m s⁻²"], "c": 1,
     "e": "(50 − 30) = 8a ⇒ a = 2.5 m s⁻²."},
    {"s": "Newton", "q": "A 60 kg person is in a lift moving DOWN and slowing at 2 m s⁻². Normal reaction?",
     "o": ["480 N", "600 N", "720 N", "120 N"], "c": 2,
     "e": "Slowing while moving down ⇒ acceleration is upward. R − 600 = 60(2) ⇒ R = 720 N."},
    {"s": "Momentum", "q": "A 6 kg hammer at 24 m s⁻¹ strikes a 2 kg post and doesn't rebound. Common speed?",
     "o": ["18 m s⁻¹", "24 m s⁻¹", "16 m s⁻¹", "12 m s⁻¹"], "c": 0,
     "e": "Coalesce: 6(24) = 8v ⇒ v = 18 m s⁻¹."},
    {"s": "Momentum", "q": "A (2 kg) at u and B (3 kg) at 2u move towards each other, coalesce and move in B's direction at 4 m s⁻¹. u = ?",
     "o": ["2.5", "4", "5", "10"], "c": 2,
     "e": "B's direction positive: 6u − 2u = 5(4) ⇒ u = 5. Forgetting A's minus sign gives 8u = 20, u = 2.5 (A)."},
    {"s": "Energy", "q": "A 3.5 kg case is lifted vertically 1.8 m. Work done against gravity?",
     "o": ["6.3 J", "63 J", "35 J", "31.5 J"], "c": 1,
     "e": "mgh = 3.5 × 10 × 1.8 = 63 J."},
    {"s": "Power", "q": "A car engine works at 16 kW against 500 N resistance on level ground. Maximum speed?",
     "o": ["20 m s⁻¹", "32 m s⁻¹", "8 m s⁻¹", "40 m s⁻¹"], "c": 1,
     "e": "At max speed a = 0 ⇒ D = 500 ⇒ v = 16 000/500 = 32 m s⁻¹."},
    {"s": "Energy", "q": "A particle moves 5 m up a smooth slope inclined at 30°. Its mass is 2 kg. Gain in PE?",
     "o": ["100 J", "50 J", "86.6 J", "10 J"], "c": 1,
     "e": "Height = 5 sin 30° = 2.5 m; PE = 2 × 10 × 2.5 = 50 J. A uses the slope length as height."},
]


def write():
    meta = {"title": "Mechanics Paper 4 Deck", "short": "Mechanics P4", "bar": "Mechanics · Paper 4",
            "code": "9709 · Paper 4 · all chapters", "key": "deck-9709-p4"}
    cards = build()
    out = engine.render(meta, cards, FLASH, QUIZ, math=True)
    out = out.replace("<b>Paper 1 quiz</b>", "<b>Paper 4 quiz</b>")
    (HERE / "deck-maths-p4.html").write_text(out, encoding="utf8")
    print("p4 mechanics", len(out), "bytes,", len(cards), "cards,", len(FLASH), "flashcards,", len(QUIZ), "quiz")
    return cards


if __name__ == "__main__":
    write()
