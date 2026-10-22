"""9709 Paper 4 · Force exerted on a pulley (connected particle systems).
Built from Puan Syazwani's 'Connected pulley systems 2' note (Cases 1-3), extended with the wedge case,
worked examples (incl. KYUEM Trial 2023 Q4), traps and practice. g = 10, answers to 3 s.f."""
import math, pathlib
import engine
from engine import card
from m1_mechanics import arr, txt, svg, tg

HERE = pathlib.Path(__file__).parent


def u(phi):
    """Unit vector in SVG space for a direction phi (degrees, maths convention, y up)."""
    r = math.radians(phi)
    return math.cos(r), -math.sin(r)


def pulley_parts(px, py, dirs, slen=(95, 95), tlab=True, rlab="R", rlen=None):
    """Pulley at (px, py); string segments leave along dirs (deg); T arrows on each; R along the bisector."""
    p = []
    for phi, L in zip(dirs, slen):
        ux, uy = u(phi)
        p.append(f'<line class="ax" x1="{px:.1f}" y1="{py:.1f}" x2="{px + ux * L:.1f}" y2="{py + uy * L:.1f}"/>')
    p.append(f'<circle class="pto" cx="{px}" cy="{py}" r="9"/>')
    if tlab:
        for phi in dirs:
            ux, uy = u(phi)
            p.append(arr(px + ux * 12, py + uy * 12, px + ux * 52, py + uy * 52, "k s"))
            p.append(txt(px + ux * 64 + (8 if ux >= 0 else -8), py + uy * 64 + 4, "T", "t-s"))
    a, b = dirs
    while b - a > 180:
        b -= 360
    while a - b > 180:
        a -= 360
    bis = (a + b) / 2
    th = abs(a - b)
    R = rlen or 40 + 60 * math.cos(math.radians(th / 2))
    ux, uy = u(bis)
    p.append(arr(px + ux * 10, py + uy * 10, px + ux * R, py + uy * R, "k b"))
    if rlab:
        p.append(txt(px + ux * (R + 14), py + uy * (R + 14) + 4, rlab, "t-b"))
    return p, bis, th


def general_svg():
    p, bis, th = pulley_parts(160, 50, [-115, -35], slen=(120, 120), rlen=125)
    # angle arc between strings
    r = 34
    a1, a2 = -115, -35
    x1, y1 = 160 + r * u(a1)[0], 50 + r * u(a1)[1]
    x2, y2 = 160 + r * u(a2)[0], 50 + r * u(a2)[1]
    p.append(f'<path class="g" style="stroke-dasharray:none;stroke-width:1.4" d="M{x1:.1f},{y1:.1f} A{r},{r} 0 0 0 {x2:.1f},{y2:.1f}"/>')
    p.append(txt(160 + 46 * u(-75)[0] + 10, 50 + 46 * u(-75)[1] - 4, "θ", "t-pt"))
    p.append(txt(160, 222, "R = 2T cos(θ/2), along the bisector", "t-sm"))
    return svg(p, "Two tensions T leave a pulley with angle theta between them; resultant R lies along the bisector", 320, 235)


def case1_svg():
    px, py, r = 160, 60, 18
    p = ['<line class="ax" x1="100" y1="22" x2="220" y2="22"/>', f'<line class="ax" x1="{px}" y1="22" x2="{px}" y2="{py}"/>',
         f'<line class="ax" x1="{px - r}" y1="{py}" x2="{px - r}" y2="185"/>', f'<line class="ax" x1="{px + r}" y1="{py}" x2="{px + r}" y2="150"/>',
         f'<circle class="pto" cx="{px}" cy="{py}" r="{r}"/>',
         f'<rect class="fa" x="{px - r - 14}" y="185" width="28" height="24" rx="3"/>',
         f'<rect class="fa" x="{px + r - 14}" y="150" width="28" height="24" rx="3"/>']
    p.append(arr(px - r, py + 22, px - r, py + 62, "k s")); p.append(txt(px - r - 10, py + 50, "T", "t-s", "end"))
    p.append(arr(px + r, py + 22, px + r, py + 62, "k s")); p.append(txt(px + r + 10, py + 50, "T", "t-s", "start"))
    p.append(arr(px, py + 4, px, py + 130, "k b")); p.append(txt(px + 8, py + 145, "R = 2T", "t-b", "start"))
    p.append(txt(160, 240, "θ = 0°: both strings straight down", "t-sm"))
    return svg(p, "Case 1: both strings vertical, R = 2T vertically downwards", 320, 252)


def case2_svg():
    p = ['<rect class="fb" x="20" y="100" width="200" height="110"/>',
         '<line class="ax" x1="20" y1="100" x2="220" y2="100"/>', '<line class="ax" x1="220" y1="100" x2="220" y2="210"/>',
         '<rect class="fa" x="70" y="72" width="34" height="28" rx="3"/>']
    q, _, _ = pulley_parts(232, 86, [180, -90], slen=(128, 82), rlen=95)
    p += q
    p.append('<rect class="fa" x="220" y="168" width="24" height="22" rx="3"/>')
    p.append(txt(160, 240, "θ = 90°: R = T√2 at 45° below the horizontal", "t-sm"))
    return svg(p, "Case 2: pulley at the edge of a table, R = T root 2 at 45 degrees", 320, 252)


def case3_svg():
    al = 25
    x0, y0, x1 = 20, 210, 250
    y1 = y0 - (x1 - x0) * math.tan(math.radians(al))
    p = [f'<path class="ax fb" d="M{x0},{y0} L{x1},{y1:.1f} L{x1},{y0} Z"/>',
         f'<path class="g" style="stroke-dasharray:none" d="M{x0 + 40},{y0} A40,40 0 0 0 {x0 + 40 * math.cos(math.radians(al)):.1f},{y0 - 40 * math.sin(math.radians(al)):.1f}"/>']
    p.append(txt(x0 + 50, y0 - 6, "α", "t-pt", "start"))
    q, _, _ = pulley_parts(x1 + 12, y1 - 12, [180 + al, -90], slen=(110, 100), rlen=110)
    p += q
    p.append(f'<rect class="fa" x="{x1}" y="{y1 + 88:.1f}" width="24" height="22" rx="3"/>')
    p.append(txt(150, 240, "θ = 90° − α between the strings", "t-sm"))
    return svg(p, "Case 3: pulley at the top of an incline at alpha, other particle hanging", 320, 252)


def case4_svg():
    al, be = 30, 50
    ax_, apx, apy = 30, 150, 118
    lx = apx - (210 - apy) / math.tan(math.radians(al))
    rx = apx + (210 - apy) / math.tan(math.radians(be))
    p = [f'<path class="ax fb" d="M{lx:.1f},210 L{apx},{apy} L{rx:.1f},210 Z"/>']
    p.append(txt(lx + 34, 204, "α", "t-pt", "start"))
    p.append(txt(rx - 34, 204, "β", "t-pt", "end"))
    q, bis, th = pulley_parts(apx, apy - 12, [180 + al, -be], slen=(95, 80), rlen=90)
    p += q
    p.append(txt(160, 232, "θ = 180° − α − β", "t-sm"))
    return svg(p, "Case 4: pulley at the apex of a wedge with faces at alpha and beta", 320, 245)


def build():
    C = []
    C.append(card("cover", "Start", "Force on a pulley", "Cover", r"""
<p class="sec" style="margin:0">CAIE 9709 · AS Level · Paper 4 · Newton's laws</p>
<p class="cover-k">R</p>
<h1>Force exerted on a pulley</h1>
<p class="lede">Connected pulley systems: one formula, four cases. Built from Puan Syazwani's <i>Connected pulley systems 2</i> note. \(g = 10\ \text{m s}^{-2}\), answers to 3 s.f.</p>
<div class="stat"><div><b>4</b>cases</div><div><b>3</b>worked examples</div><div><b>4</b>practice Qs</div></div>
<p><a href="index.html">Open Revision Hub</a></p>
<div class="swipehint">Swipe or use the arrows · tap ☰ for contents</div>""", sec="Start"))

    C.append(card("idea", "Start", "The one idea", "Overview", r"""
<h2>The string pulls the pulley twice</h2>
<p class="lede">Smooth, light pulley + light, inextensible string ⇒ the tension \(T\) is the <b>same on both sides</b>. Each segment pulls the pulley <b>along itself, away from the pulley</b>. The force on the pulley is the <b>vector sum</b> of the two tensions.</p>
<figure class="dg">""" + general_svg() + r"""<figcaption>θ is the angle <b>between the two string segments</b> at the pulley.</figcaption></figure>
<div class="formula">\(R = 2T\cos\left(\dfrac{\theta}{2}\right)\), along the bisector of θ</div>
<div class="note link"><b>Why</b>Resolve along the bisector: each tension gives \(T\cos\frac{\theta}{2}\). Across the bisector the two components are equal and opposite, so they cancel.</div>""", sec="Start"))

    C.append(card("method", "Start", "Two-step method", "Concept", r"""
<h2>Every pulley-force question in two steps</h2>
<div class="chain"><span>1 · N2L on one particle ⇒ \(T\)</span><i>→</i><span>2 · Geometry ⇒ θ, then \(R = 2T\cos\frac{\theta}{2}\) + direction</span></div>
<ul>
<li><b>Step 1 first, always.</b> \(T\) equals the hanging weight <b>only in equilibrium</b>. If the system accelerates, \(T \neq mg\).</li>
<li>Get \(a\) from the whole system (external forces ÷ total mass), then \(T\) from one particle on its own.</li>
<li><b>Step 2:</b> find θ from the diagram. If unsure of θ, resolve horizontally and vertically instead and use Pythagoras.</li>
</ul>
<div class="note tip"><b>The support</b>The clamp/axle holding the pulley exerts a force <b>equal and opposite</b> to \(R\). "Force exerted by the string on the pulley" and "force needed to hold the pulley" have the same magnitude.</div>""", sec="Start"))

    S = "The four cases"
    C.append(card("c1", S, "Case 1: both strings vertical", "Concept", r"""
<h2>Case 1 · Both strings hanging vertically</h2>
<figure class="dg">""" + case1_svg() + r"""<figcaption>Two masses hang straight down on either side.</figcaption></figure>
<div class="tw"><table>
<tr><td class="k">Angle between strings</td><td>\(\theta = 0°\)</td></tr>
<tr><td class="k">Magnitude</td><td>\(R = 2T\cos 0° = 2T\)</td></tr>
<tr><td class="k">Direction</td><td>Vertically downwards</td></tr>
</table></div>
<div class="note trap"><b>Trap</b>\(R = 2T\), <b>not</b> the total weight. With 3 kg and 5 kg released, \(T = 37.5\) N, so \(R = 75\) N, not 80 N.</div>""", sec=S))

    C.append(card("c2", S, "Case 2: edge of a table", "Concept", r"""
<h2>Case 2 · Pulley at the edge of a horizontal table</h2>
<figure class="dg">""" + case2_svg() + r"""<figcaption>One particle on the table, the other hanging.</figcaption></figure>
<div class="tw"><table>
<tr><td class="k">Angle between strings</td><td>\(\theta = 90°\)</td></tr>
<tr><td class="k">Magnitude</td><td>\(R = 2T\cos45°\)<br>\(\phantom{R} = T\sqrt2\)</td></tr>
<tr><td class="k">Direction</td><td>\(45°\) below the horizontal, towards the table (bisects the right angle)</td></tr>
</table></div>
<div class="note tip"><b>Rough table?</b>Friction changes \(a\) and so \(T\), but <b>not</b> the geometry: still \(R = T\sqrt2\) at \(45°\).</div>""", sec=S))

    C.append(card("c3", S, "Case 3: top of an incline", "Concept", r"""
<h2>Case 3 · Pulley at the top of an inclined plane</h2>
<figure class="dg">""" + case3_svg() + r"""<figcaption>One particle on the slope at α, the other hanging vertically.</figcaption></figure>
<div class="tw"><table>
<tr><td class="k">Angle between strings</td><td>\(\theta = 90° - \alpha\)</td></tr>
<tr><td class="k">Magnitude</td><td>\(R = 2T\cos\left(45° - \frac{\alpha}{2}\right)\)<br>\(\phantom{R} = T\sqrt{2(1+\sin\alpha)}\)</td></tr>
<tr><td class="k">Direction</td><td>At \(45° - \frac{\alpha}{2}\) to the vertical, on the slope side</td></tr>
</table></div>
<div class="note trap"><b>Trap</b>θ is <b>not</b> the slope angle. On a \(20°\) slope, \(\theta = 70°\).</div>""", sec=S))

    C.append(card("c3check", S, "Case 3 by resolving", "Concept", r"""
<h2>Check Case 3 without the formula</h2>
<p class="lede">One string runs down the slope at α below the horizontal; the other hangs vertically.</p>
<div class="def"><div class="lab">Resolve the two tensions</div>
<p>\(R_x = T\cos\alpha\)</p>
<p>\(R_y = T + T\sin\alpha\)</p>
<p>\(R^2 = T^2\cos^2\alpha + T^2(1+\sin\alpha)^2\)</p>
<p>\(\phantom{R^2} = T^2(2 + 2\sin\alpha)\)</p>
<p>\(R = T\sqrt{2(1 + \sin\alpha)}\)</p></div>
<p>Same as \(2T\cos\left(45° - \frac{\alpha}{2}\right)\), because</p>
<p>\(4\cos^2\left(45° - \frac{\alpha}{2}\right) = 2\left(1 + \sin\alpha\right)\)</p>
<div class="note tip"><b>Exam fallback</b>Resolving always works for any geometry. If you're not sure what θ is, resolve, then \(\tan\phi = R_y / R_x\) gives the direction.</div>""", sec=S))

    C.append(card("c4", S, "Case 4: apex of a wedge", "Concept", r"""
<h2>Case 4 · Pulley at the apex of a wedge</h2>
<figure class="dg">""" + case4_svg() + r"""<figcaption>A particle on each face, faces inclined at α and β.</figcaption></figure>
<div class="tw"><table>
<tr><td class="k">Angle between strings</td><td>\(\theta = 180° - \alpha - \beta\)</td></tr>
<tr><td class="k">Magnitude</td><td>\(R = 2T\cos\left(90° - \frac{\alpha+\beta}{2}\right)\)<br>\(\phantom{R} = 2T\sin\left(\frac{\alpha+\beta}{2}\right)\)</td></tr>
<tr><td class="k">Direction</td><td>Bisects the angle between the faces, into the wedge</td></tr>
</table></div>
<div class="note link"><b>Special case</b>\(\alpha + \beta = 90°\) ⇒ \(\theta = 90°\) ⇒ \(R = T\sqrt2\), like Case 2.</div>""", sec=S))

    C.append(card("table", S, "All four cases", "Summary", r"""
<h2>The four cases side by side</h2>
<div class="tw"><table>
<tr><th>Case</th><th>θ</th><th>R</th></tr>
<tr><td class="k">1 · Both vertical</td><td>\(0°\)</td><td>\(2T\), vertically down</td></tr>
<tr><td class="k">2 · Table edge</td><td>\(90°\)</td><td>\(T\sqrt2\), \(45°\) below horizontal</td></tr>
<tr><td class="k">3 · Incline at α</td><td>\(90° - \alpha\)</td><td>\(2T\cos\left(45° - \frac{\alpha}{2}\right)\)</td></tr>
<tr><td class="k">4 · Wedge α, β</td><td>\(180° - \alpha - \beta\)</td><td>\(2T\sin\frac{\alpha+\beta}{2}\)</td></tr>
</table></div>
<div class="note tip"><b>Pattern</b>The smaller θ (strings closer together), the bigger \(R\). Maximum \(R = 2T\) when both strings point the same way.</div>""", sec=S))

    W = "Worked examples"
    C.append(card("we1", W, "Example 1: vertical strings", "Worked example", r"""
<h2>Example 1 · 3 kg and 5 kg over a pulley</h2>
<p><b>Q:</b> Particles of mass 3 kg and 5 kg hang on either side of a fixed smooth pulley and are released from rest. Find the force exerted on the pulley by the string.</p>
<ol class="steps">
<li><b>Directions:</b> 5 kg down positive, 3 kg up positive.</li>
<li>""" + tg("M1") + r""" N2L (5 kg): \(50 - T = 5a\); N2L (3 kg): \(T - 30 = 3a\)</li>
<li>""" + tg("A1") + r""" Add: \(20 = 8a \Rightarrow a = 2.5\ \text{m s}^{-2}\), so \(T = 30 + 3(2.5) = 37.5\ \text{N}\)</li>
<li>""" + tg("M1") + r""" Case 1, \(\theta = 0°\): \(R = 2T\)</li>
<li>""" + tg("A1") + r""" \(R = 75\ \text{N}\), vertically downwards</li>
</ol>
<div class="note trap"><b>Where marks go</b>Writing \(R = 80\) N (total weight) scores 0. The system accelerates, so \(T < 50\) N.</div>""", sec=W))

    C.append(card("we2", W, "Example 2: table edge", "Worked example", r"""
<h2>Example 2 · Block on a table, particle hanging</h2>
<p><b>Q:</b> A 4 kg block on a smooth horizontal table is connected over a smooth pulley at the edge to a 1 kg hanging particle. Find the magnitude and direction of the force on the pulley.</p>
<ol class="steps">
<li>""" + tg("M1") + r""" System (external forces only): \(10 = (4+1)a \Rightarrow a = 2\ \text{m s}^{-2}\)</li>
<li>""" + tg("A1") + r""" N2L (4 kg block): \(T = 4a = 8\ \text{N}\)</li>
<li>""" + tg("M1") + r""" Case 2, \(\theta = 90°\): \(R = T\sqrt2\)</li>
<li>""" + tg("A1") + r""" \(R = 8\sqrt2 = 11.3\ \text{N}\) at \(45°\) below the horizontal</li>
</ol>
<div class="note tip"><b>Check</b>\(T = 8 &lt; 10\) N (hanging weight), as it must be while the 1 kg particle accelerates down.</div>""", sec=W))

    C.append(card("we3", W, "Example 3: incline (Trial 2023 Q4)", "Worked example", r"""
<h2>Example 3 · KYUEM Trial 2023 Q4 extension</h2>
<p><b>Q:</b> Block B (2 kg) is on a smooth plane inclined at \(20°\), connected over a pulley at the top to ball A (3 kg) hanging freely. Find the force on the pulley while A falls.</p>
<ol class="steps">
<li>""" + tg("M1") + r""" System: \(30 - 20\sin20° = 5a \Rightarrow a = 4.632\ \text{m s}^{-2}\)</li>
<li>""" + tg("A1") + r""" N2L (A, down +): \(30 - T = 3a \Rightarrow T = 16.10\ \text{N}\)</li>
<li>""" + tg("B1") + r""" Case 3: \(\theta = 90° - 20° = 70°\)</li>
<li>""" + tg("M1") + r""" \(R = 2(16.10)\cos35°\)</li>
<li>""" + tg("A1") + r""" \(R = 26.4\ \text{N}\) at \(35°\) to the vertical, on the slope side</li>
</ol>
<div class="note link"><b>Check by resolving</b>\(R_x = 16.10\cos20° = 15.13\), \(R_y = 16.10(1 + \sin20°) = 21.61\), so \(R = \sqrt{15.13^2 + 21.61^2} = 26.4\) N ✓</div>""", sec=W))

    C.append(card("traps", "Mistakes", "Common mistakes", "Concept", r"""
<h2>Where marks are lost</h2>
<div class="note trap"><b>Using \(mg\) as \(T\)</b>Only true in equilibrium. If anything accelerates, find \(T\) with N2L first.</div>
<div class="note trap"><b>Slope angle as θ</b>θ is the angle <b>between the strings</b>. On a \(20°\) incline, \(\theta = 70°\).</div>
<div class="note trap"><b>Different tensions each side</b>Smooth light pulley ⇒ one \(T\) throughout the string.</div>
<div class="note trap"><b>No direction</b>"Find the force on the pulley" usually means magnitude <b>and</b> direction. State the angle and the reference line.</div>
<div class="note trap"><b>\(T\) pulling towards the pulley</b>On the <b>pulley</b>, each tension points <b>away</b> from it, along the string towards the particle.</div>""", sec="Mistakes"))

    C.append(card("pr", "Practice", "Practice questions", "Practice", r"""
<h2>Practice · Force on a pulley</h2>
<div class="pq"><div class="qh"><span>Q1 · Case 1</span><span class="mk">[4]</span></div>
<p class="qt">Particles of mass 6 kg and 4 kg hang on either side of a fixed smooth pulley and are released from rest. Find the force exerted on the pulley by the string.</p>
<div class="ans"><b>Answer</b>\(20 = 10a \Rightarrow a = 2\); \(T = 40 + 4(2) = 48\) N; \(R = 2T = 96\) N vertically downwards.</div></div>
<div class="pq"><div class="qh"><span>Q2 · Case 2, rough table</span><span class="mk">[5]</span></div>
<p class="qt">A 5 kg block on a rough horizontal table (\(\mu = 0.2\)) is connected over a pulley at the edge to a 3 kg hanging particle. Find the magnitude and direction of the force on the pulley.</p>
<div class="ans"><b>Answer</b>\(30 - 0.2(50) = 8a \Rightarrow a = 2.5\); \(T = 3(10 - 2.5) = 22.5\) N; \(R = 22.5\sqrt2 = 31.8\) N at \(45°\) below the horizontal.</div></div>
<div class="pq"><div class="qh"><span>Q3 · Case 4, wedge</span><span class="mk">[6]</span></div>
<p class="qt">A wedge has smooth faces inclined at \(30°\) and \(60°\). A 4 kg particle on the \(30°\) face and a 6 kg particle on the \(60°\) face are connected over a pulley at the apex. Find the force on the pulley.</p>
<div class="ans"><b>Answer</b>\(60\sin60° - 40\sin30° = 10a \Rightarrow a = 3.196\); \(T = 20 + 4a = 32.8\) N; \(\theta = 90°\), \(R = 2T\sin45° = 46.4\) N, at \(15°\) to the vertical towards the \(30°\) face.</div></div>
<div class="pq"><div class="qh"><span>Q4 · Case 3, equilibrium</span><span class="mk">[4]</span></div>
<p class="qt">A 5 kg block rests on a smooth plane inclined at \(30°\), held in equilibrium by a string over a pulley at the top attached to a hanging particle of mass \(m\) kg. Find \(m\) and the force on the pulley.</p>
<div class="ans"><b>Answer</b>Equilibrium: \(T = 50\sin30° = 25\) N, so \(m = 2.5\). \(\theta = 60°\): \(R = 2(25)\cos30° = 43.3\) N at \(30°\) to the vertical.</div></div>""", sec="Practice"))

    C.append(card("sheet", "Summary", "Formula card", "Summary", r"""
<h2>Everything on one card</h2>
<div class="formula">\(R = 2T\cos\left(\dfrac{\theta}{2}\right)\) · along the bisector · θ = angle between strings</div>
<div class="tw"><table>
<tr><th>Case</th><th>θ</th><th>R</th></tr>
<tr><td class="k">Vertical</td><td>\(0°\)</td><td>\(2T\), down</td></tr>
<tr><td class="k">Table</td><td>\(90°\)</td><td>\(T\sqrt2\), \(45°\)</td></tr>
<tr><td class="k">Incline α</td><td>\(90° - \alpha\)</td><td>\(T\sqrt{2(1+\sin\alpha)}\)</td></tr>
<tr><td class="k">Wedge α, β</td><td>\(180° - \alpha - \beta\)</td><td>\(2T\sin\frac{\alpha+\beta}{2}\)</td></tr>
</table></div>
<div class="note tip"><b>Before you write R</b>Did you find \(T\) from N2L (not \(mg\))? Is θ between the <b>strings</b>? Did you state the direction?</div>""", sec="Summary"))
    return C


FLASH = [
    ["Pulley", "Force on a smooth pulley from a string with tension T, angle θ between the segments?", "R = 2T cos(θ/2), along the bisector of θ."],
    ["Pulley", "Why is T the same on both sides of the pulley?", "The pulley is smooth and light and the string is light."],
    ["Pulley", "Direction of each tension acting ON the pulley?", "Along the string, away from the pulley (towards its particle)."],
    ["Pulley", "Case 1 (both strings vertical): R?", "θ = 0°, R = 2T vertically downwards."],
    ["Pulley", "Case 2 (edge of a table): R?", "θ = 90°, R = T√2 at 45° below the horizontal."],
    ["Pulley", "Case 3 (top of incline at α, other hanging): θ?", "θ = 90° − α."],
    ["Pulley", "Case 3 magnitude without the formula?", "Resolve: R² = (T cos α)² + (T + T sin α)² ⇒ R = T√(2(1 + sin α))."],
    ["Pulley", "Case 4 (wedge with faces α and β): θ?", "θ = 180° − α − β, so R = 2T sin((α + β)/2)."],
    ["Pulley", "When does T equal the hanging weight?", "Only in equilibrium. If accelerating, use N2L to find T."],
    ["Pulley", "3 kg and 5 kg over a pulley, released: R?", "a = 2.5, T = 37.5 N, R = 75 N (not 80 N)."],
    ["Pulley", "Force exerted by the support on the pulley?", "Equal and opposite to R (Newton's third law)."],
]

QUIZ = [
    {"s": "Pulley", "q": "Two strings leave a smooth pulley with 60° between them. T = 20 N. Force on the pulley?",
     "o": ["20 N", "34.6 N", "40 N", "17.3 N"], "c": 1,
     "e": "R = 2(20)cos30° = 34.6 N. C is the θ = 0° case."},
    {"s": "Pulley", "q": "A 2 kg block on a smooth table is connected over the edge to a 2 kg hanging particle. Force on the pulley?",
     "o": ["20√2 N", "10√2 N", "20 N", "40 N"], "c": 1,
     "e": "a = 20/4 = 5, T = 2(5) = 10 N, R = 10√2 = 14.1 N. A wrongly uses T = mg = 20 N."},
    {"s": "Pulley", "q": "Pulley at the top of a 40° incline, other particle hanging. Angle between the strings?",
     "o": ["40°", "50°", "90°", "140°"], "c": 1,
     "e": "θ = 90° − α = 50°. A uses the slope angle."},
    {"s": "Pulley", "q": "Masses 4 kg and 4 kg hang over a smooth pulley in equilibrium. Force on the pulley?",
     "o": ["40 N", "80 N", "56.6 N", "0 N"], "c": 1,
     "e": "Equilibrium: T = 40 N. θ = 0° ⇒ R = 2T = 80 N."},
    {"s": "Pulley", "q": "Wedge faces at 35° and 55°, apex pulley, T = 12 N. Force on the pulley?",
     "o": ["12 N", "12√2 N", "24 N", "6√2 N"], "c": 1,
     "e": "α + β = 90° ⇒ θ = 90° ⇒ R = 2(12)sin45° = 12√2 = 17.0 N."},
    {"s": "Pulley", "q": "Which is TRUE about R as θ increases from 0° to 180°?",
     "o": ["R increases", "R decreases", "R is constant", "R = 0 at θ = 90°"], "c": 1,
     "e": "R = 2T cos(θ/2) falls from 2T (θ = 0°) to 0 (θ = 180°, string straight across)."},
]


def write():
    meta = {"title": "Force on a Pulley Deck", "short": "Pulley force", "bar": "Mechanics · Force on a pulley",
            "code": "9709 · Paper 4 · Newton's laws", "key": "deck-9709-pulley"}
    cards = build()
    out = engine.render(meta, cards, FLASH, QUIZ, math=True)
    out = out.replace("<b>Paper 1 quiz</b>", "<b>Pulley quiz</b>")
    (HERE / "deck-maths-pulley.html").write_text(out, encoding="utf8")
    print("pulley", len(out), "bytes,", len(cards), "cards,", len(FLASH), "flashcards,", len(QUIZ), "quiz")
    return cards


if __name__ == "__main__":
    write()
