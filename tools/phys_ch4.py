"""9702 Physics · Chapter 4 Forces, density and pressure.
Built from Tuah's Topical Notes (Moment of Force, Couple, Translational and Rotational Motion,
Gravitational Force, Upthrust). Cambridge notation, g = 9.81 m s⁻², answers to 2-3 s.f."""
import pathlib
import engine
from fixids import unique_markers
from engine import card
from phys_graphs import tg

HERE = pathlib.Path(__file__).parent

from phys_graphs import DEFS


def ar(x1, y1, x2, y2):
    return f'<line class="ar" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" marker-end="url(#gh)"/>'


def tx(x, y, s, cls="t-sm", a="middle"):
    return f'<text class="{cls}" x="{x}" y="{y}" text-anchor="{a}">{s}</text>'


def moment_svg():
    p = ['<line class="ax" x1="40" y1="40" x2="250" y2="150"/>', '<circle class="pt" cx="40" cy="40" r="4"/>',
         tx(32, 34, "pivot", "t-s", "end"), ar(250, 150, 250, 210), tx(258, 200, "F", "t-pt", "start"),
         '<line class="g" x1="40" y1="40" x2="250" y2="40"/>', '<line class="g" x1="250" y1="40" x2="250" y2="150"/>',
         tx(145, 32, "perpendicular distance d", "t-s")]
    return (f'<figure class="dg" style="max-width:420px"><svg viewBox="0 0 300 220" role="img" aria-label="moment: force times perpendicular distance from pivot to line of action">{DEFS}'
            + "".join(p) + '</svg><figcaption>Moment = F × d, where d is measured <b>perpendicular to the line of action</b> of F, not along the bar.</figcaption></figure>')


def couple_svg():
    p = ['<circle class="ax" cx="150" cy="100" r="70" fill="none"/>', '<circle class="pt" cx="150" cy="100" r="3"/>',
         ar(80, 100, 80, 40), ar(220, 100, 220, 160), tx(70, 50, "F", "t-pt", "end"), tx(230, 155, "F", "t-pt", "start"),
         '<line class="g" x1="80" y1="185" x2="220" y2="185"/>', tx(150, 200, "d (between the lines of action)", "t-s")]
    return (f'<figure class="dg" style="max-width:420px"><svg viewBox="0 0 300 210" role="img" aria-label="couple: two equal opposite parallel forces on a wheel">{DEFS}'
            + "".join(p) + '</svg><figcaption>Torque of a couple = F × d. Resultant force is zero, so there is turning but no linear acceleration.</figcaption></figure>')


def build():
    C = []
    C.append(card("cover", "Start", "Forces, density and pressure", "Cover", r"""
<p class="sec" style="margin:0">CAIE 9702 · AS Level · Chapter 4</p>
<p class="cover-k">τ</p>
<h1>Forces, density and pressure</h1>
<p class="lede">Weight and centre of gravity, moments, the principle of moments, couples and torque, equilibrium, density, pressure in fluids and upthrust. Built from your Chapter 4 topical notes and class past-paper questions.</p>
<div class="stat"><div><b>4</b>worked examples</div><div><b>5</b>practice Qs</div><div><b>24</b>flashcards</div></div>
<p><a href="index.html">Open Revision Hub</a></p>
<div class="swipehint">Swipe or use the arrows · tap ☰ for contents</div>""", sec="Start"))

    C.append(card("big", "Start", "The big picture", "Overview", r"""
<h2>Forces that make things move, turn, or float</h2>
<div class="chain"><span>Resultant force ⇒ translation</span><span>Resultant moment ⇒ rotation</span><span>Both zero ⇒ equilibrium</span></div>
<div class="tw"><table>
<tr><th>Topic</th><th>Key equation</th></tr>
<tr><td class="k">Moment</td><td>\(\tau = Fd\)</td></tr>
<tr><td class="k">Couple</td><td>\(\tau = Fd\) (d between the forces)</td></tr>
<tr><td class="k">Density</td><td>\(\rho = m/V\)</td></tr>
<tr><td class="k">Pressure</td><td>\(p = F/A\), \(\Delta p = \rho g\Delta h\)</td></tr>
<tr><td class="k">Upthrust</td><td>\(F = \rho gV\)</td></tr>
</table></div>""", sec="Start"))

    S = "Moments"
    C.append(card("cg", S, "Weight and centre of gravity", "Concept", r"""
<h2>One force standing in for many</h2>
<p>Every particle of an object is pulled by gravity. All these forces can be replaced by <b>one force, the weight</b>, acting at a single point.</p>
<div class="def"><div class="lab">Centre of gravity</div><p>The point at which the <b>whole weight</b> of an object may be considered to act.</p></div>
<div class="note tip"><b>Uniform objects</b>For a uniform rod or metre rule, the centre of gravity is at the <b>midpoint</b> (50 cm mark).</div>""", sec=S))

    C.append(card("moment", S, "Moment of a force", "Concept", r"""
<h2>The turning effect of a force</h2>
<div class="def"><div class="lab">Moment of a force</div><p>The product of the force and the <b>perpendicular distance from the pivot to the line of action</b> of the force.</p></div>
""" + moment_svg() + r"""
<p>Depends on two things: the <b>magnitude</b> of the force and the <b>perpendicular distance</b>. Unit N m.</p>
<div class="note tip"><b>Angled force</b>Either use the perpendicular component (\(F\sin\theta \times d\)) or the perpendicular distance (\(F \times d\sin\theta\)). They give the same answer.</div>""", sec=S))

    C.append(card("pom", S, "Principle of moments", "Concept", r"""
<h2>Balancing turning effects</h2>
<div class="def"><div class="lab">Principle of moments</div><p>For an object in equilibrium, the <b>sum of clockwise moments</b> about any point equals the <b>sum of anticlockwise moments</b> about the same point.</p></div>
<ul>
<li>Take moments about a point where an <b>unknown force acts</b>: it has zero moment there and drops out.</li>
<li>Include the object's own weight at its centre of gravity.</li>
<li>Any point works if the object is in equilibrium. Pick the one that removes the most unknowns.</li>
</ul>
<div class="note link"><b>Ladder against a smooth wall (June 08)</b>Moments about the base: the wall's push \(F\) at height \(h\) balances the weight \(W\) at horizontal distance \(a\): \(Fh = Wa\). About the top, with friction at the base: \(Wa + Fh = 2Wa\).</div>""", sec=S))

    C.append(card("couple", S, "Couples and torque", "Concept", r"""
<h2>A pair of forces that only turns</h2>
<div class="def"><div class="lab">Couple</div><p>A pair of forces, <b>equal in magnitude</b>, <b>opposite in direction</b>, acting along <b>parallel lines</b> (not the same line), producing rotation only.</p></div>
<div class="def"><div class="lab">Torque of a couple</div><p>The product of <b>one of the forces</b> and the <b>perpendicular distance between</b> the forces.</p></div>
""" + couple_svg() + r"""
<div class="note link"><b>Same about any point</b>Your notes: 6 N forces 3 m apart. About P (1 m from one): 6(1) + 6(2) = 18 N m. About Q (on one force): 6(3) = 18 N m. The torque is independent of the axis.</div>
<div class="note trap"><b>Couple vs single moment</b>A couple has zero resultant force, so no linear acceleration. A single force off-centre gives both turning and translation.</div>""", sec=S))

    C.append(card("eq", S, "Conditions for equilibrium", "Concept", r"""
<h2>Two conditions, both needed</h2>
<div class="tw"><table>
<tr><th>Condition</th><th>Means</th></tr>
<tr><td class="k">Resultant force = 0</td><td>no <b>translational</b> acceleration (\(\sum F_x = 0\), \(\sum F_y = 0\))</td></tr>
<tr><td class="k">Resultant moment = 0</td><td>no <b>rotational</b> acceleration</td></tr>
</table></div>
<div class="def"><div class="lab">Translational motion</div><p>Every part moves in the same direction at the same speed.</p></div>
<div class="def"><div class="lab">Rotational motion</div><p>Every part moves in a circle about an axis.</p></div>
<div class="note link"><b>Three forces in equilibrium</b>Their lines of action pass through one point, and they form a <b>closed triangle</b> when drawn tip to tail.</div>
<div class="note link"><b>Ladder on icy ground (June 12/12)</b>No friction at the base, so the ground's force R is vertical; the rough wall provides both a horizontal push and an upward friction force.</div>""", sec=S))

    P = "Density and pressure"
    C.append(card("rho", P, "Density and pressure", "Concept", r"""
<h2>Definitions</h2>
<div class="def"><div class="lab">Density</div><p>Mass per unit volume: \(\rho = \dfrac mV\), unit kg m⁻³.</p></div>
<div class="def"><div class="lab">Pressure</div><p>Normal force per unit area: \(p = \dfrac FA\), unit Pa (N m⁻²).</p></div>
<div class="def"><div class="lab">Pressure in a fluid</div>
<p>Column of height \(h\), area \(A\): \(m = \rho V = \rho Ah\)</p>
<p>\(p = \dfrac{mg}{A} = \dfrac{\rho Ahg}{A} = \rho gh\)</p></div>
<div class="note tip"><b>Total pressure</b>Under a liquid open to the air: \(p = p_{\text{atm}} + \rho gh\). Higher altitude ⇒ less air above ⇒ lower atmospheric pressure.</div>""", sec=P))

    C.append(card("up", P, "Upthrust", "Concept", r"""
<h2>Why things float</h2>
<div class="def"><div class="lab">Upthrust</div><p>The upward force exerted by a fluid on a submerged object, caused by the <b>difference in pressure</b> between its bottom and top surfaces.</p></div>
<div class="def"><div class="lab">Derivation</div>
<p>Top at depth \(h_1\): \(F_1 = \rho gh_1A\) (down)</p>
<p>Bottom at depth \(h_2\): \(F_2 = \rho gh_2A\) (up)</p>
<p>Upthrust \(= F_2 - F_1 = \rho gA(h_2 - h_1) = \rho_f gV\)</p></div>
<p>\(\rho_f V g = m_f g\): upthrust = <b>weight of fluid displaced</b> (Archimedes' principle).</p>
<div class="note tip"><b>Floating</b>Upthrust = weight. A floating block of density 600 kg m⁻³ in water (1000) sits with 60% of its volume submerged.</div>""", sec=P))

    W = "Worked examples"
    C.append(card("we1", W, "Example 1: metre rule (Nov 14/13)", "Worked example", r"""
<h2>Example 1 · Balancing a metre rule</h2>
<p><b>Q:</b> A uniform 100 g metre rule is pivoted at the 40 cm mark. A string at the 100 cm mark runs over a pulley to a 20 g mass, pulling the rule upwards. Where must a 50 g mass hang for the rule to balance?</p>
<ol class="steps">
<li>""" + tg("B1") + r""" Moments about the pivot (g cancels, use grams and cm)</li>
<li>""" + tg("C1") + r""" Clockwise: rule's weight \(100 \times (50-40) = 1000\); anticlockwise: tension \(20 \times (100-40) = 1200\)</li>
<li>""" + tg("M1") + r""" Need 200 more clockwise: \(50 \times x = 200 \Rightarrow x = 4\) cm right of the pivot</li>
<li>""" + tg("A1") + r""" 44 cm mark</li>
</ol>
<div class="note trap"><b>Your working</b>You mixed metres and newtons with signs and got lost. Keep one consistent unit (g and cm is fine here, since g cancels) and list clockwise and anticlockwise separately.</div>""", sec=W))

    C.append(card("we2", W, "Example 2: torque of a couple", "Worked example", r"""
<h2>Example 2 · Steering wheel and lever (June 14/11)</h2>
<p><b>Q (a):</b> A driver pushes with 15 N on opposite sides of a wheel of diameter 0.40 m. Find the torque.</p>
<p><b>Q (b):</b> A 1.20 m lever turns a disc of radius 0.20 m, which winds a string lifting a 900 N weight. Equal forces F act at each end of the lever. Find the minimum F.</p>
<ol class="steps">
<li>""" + tg("A1") + r""" (a) \(\tau = 15 \times 0.40 = 6.0\) N m</li>
<li>""" + tg("M1") + r""" (b) Couple torque = load torque: \(F(1.20) = 900(0.20)\)</li>
<li>""" + tg("A1") + r""" \(F = 150\) N</li>
</ol>""", sec=W))

    C.append(card("we3", W, "Example 3: beam on two supports", "Worked example", r"""
<h2>Example 3 · Person on a plank</h2>
<p><b>Q:</b> A uniform 4.0 m plank of weight 200 N rests on supports at each end. A 500 N person stands 1.0 m from the left end. Find both support forces.</p>
<ol class="steps">
<li>""" + tg("M1") + r""" Moments about the left support: \(R_R(4.0) = 200(2.0) + 500(1.0)\)</li>
<li>""" + tg("A1") + r""" \(R_R = 225\) N</li>
<li>""" + tg("A1") + r""" Vertical forces: \(R_L = 700 - 225 = 475\) N</li>
</ol>
<div class="note tip"><b>Sense check</b>The person is nearer the left, so the left support carries more.</div>""", sec=W))

    C.append(card("we4", W, "Example 4: upthrust and pressure", "Worked example", r"""
<h2>Example 4 · Object in water</h2>
<p><b>Q:</b> An object of volume \(2.0\times10^{-4}\) m³ weighs 5.0 N in air. Find the upthrust when fully submerged in water (1000 kg m⁻³), its apparent weight, and the pressure due to the water at 12 m depth.</p>
<ol class="steps">
<li>""" + tg("A1") + r""" \(U = \rho gV = 1000(9.81)(2.0\times10^{-4}) = 1.96\) N</li>
<li>""" + tg("A1") + r""" Apparent weight \(= 5.0 - 1.96 = 3.0\) N</li>
<li>""" + tg("A1") + r""" \(\Delta p = \rho gh = 1000(9.81)(12) = 1.2\times10^5\) Pa</li>
</ol>""", sec=W))

    C.append(card("traps", "Mistakes", "Common mistakes", "Concept", r"""
<h2>Where marks are lost</h2>
<div class="note trap"><b>Distance along the bar</b>Moment uses the perpendicular distance to the line of action.</div>
<div class="note trap"><b>Forgetting the object's own weight</b>A uniform beam's weight acts at its midpoint.</div>
<div class="note trap"><b>Couple definition missing "parallel"</b>Equal, opposite, parallel, not along the same line.</div>
<div class="note trap"><b>Only one equilibrium condition</b>State both: resultant force zero and resultant moment zero.</div>
<div class="note trap"><b>Upthrust from the object's density</b>Use the <b>fluid's</b> density and the displaced volume.</div>
<div class="note trap"><b>Pressure as a vector</b>Pressure is a scalar; it acts in all directions.</div>""", sec="Mistakes"))

    C.append(card("pr", "Practice", "Practice questions", "Practice", r"""
<h2>Practice · Forces, density and pressure</h2>
<div class="pq"><div class="qh"><span>Q1 · Define</span><span class="mk">[2]</span></div>
<p class="qt">Define the moment of a force and the torque of a couple.</p>
<div class="ans"><b>Answer</b>Moment: force × perpendicular distance from the pivot to its line of action. Torque of a couple: one force × perpendicular distance between the two forces.</div></div>
<div class="pq"><div class="qh"><span>Q2 · Principle of moments</span><span class="mk">[3]</span></div>
<p class="qt">A uniform 2.0 m rod of weight 30 N is pivoted at its centre. A 40 N weight hangs 0.60 m left of the pivot. Where must a 60 N weight hang to balance it?</p>
<div class="ans"><b>Answer</b>Rod's weight acts at the pivot (no moment). \(40(0.60) = 60x \Rightarrow x = 0.40\) m right of the pivot.</div></div>
<div class="pq"><div class="qh"><span>Q3 · Pressure</span><span class="mk">[2]</span></div>
<p class="qt">Find the pressure due to 0.80 m of oil (density 850 kg m⁻³), and the total pressure if atmospheric pressure is \(1.01\times10^5\) Pa.</p>
<div class="ans"><b>Answer</b>\(\rho gh = 850(9.81)(0.80) = 6.7\times10^3\) Pa; total \(= 1.08\times10^5\) Pa.</div></div>
<div class="pq"><div class="qh"><span>Q4 · Floating</span><span class="mk">[2]</span></div>
<p class="qt">A wooden cube of side 0.10 m and density 600 kg m⁻³ floats in water. How deep does it sit?</p>
<div class="ans"><b>Answer</b>Upthrust = weight: \(1000 \times 0.10^2 \times h = 600 \times 0.10^3 \Rightarrow h = 0.060\) m.</div></div>
<div class="pq"><div class="qh"><span>Q5 · Explain</span><span class="mk">[2]</span></div>
<p class="qt">Explain why a submerged object experiences an upthrust.</p>
<div class="ans"><b>Answer</b>Pressure in a fluid increases with depth, so the pressure on the bottom surface is greater than on the top. This gives a greater upward force than downward force, so a resultant upward force.</div></div>""", sec="Practice"))

    C.append(card("sheet", "Summary", "Formula card", "Summary", r"""
<h2>Everything on one card</h2>
<div class="tw"><table>
<tr><td class="k">Moment</td><td>\(F \times\) perpendicular distance to line of action</td></tr>
<tr><td class="k">Principle of moments</td><td>Σ clockwise = Σ anticlockwise (equilibrium)</td></tr>
<tr><td class="k">Couple</td><td>torque = \(F \times d\) between forces; zero resultant force</td></tr>
<tr><td class="k">Equilibrium</td><td>resultant force = 0 and resultant moment = 0</td></tr>
<tr><td class="k">Density</td><td>\(\rho = m/V\)</td></tr>
<tr><td class="k">Pressure</td><td>\(p = F/A\); \(\Delta p = \rho g\Delta h\)</td></tr>
<tr><td class="k">Upthrust</td><td>\(\rho_f gV\) = weight of fluid displaced</td></tr>
</table></div>""", sec="Summary"))
    return C


FLASH = [
    ["Moments", "Define centre of gravity.", "The point where the whole weight of an object may be considered to act."],
    ["Moments", "Define the moment of a force.", "Force × perpendicular distance from the pivot to the line of action of the force."],
    ["Moments", "State the principle of moments.", "In equilibrium, sum of clockwise moments = sum of anticlockwise moments about any point."],
    ["Moments", "Best point to take moments about?", "Where an unknown force acts, so it has no moment."],
    ["Moments", "Unit of moment?", "N m."],
    ["Couples", "Define a couple.", "Two equal, opposite, parallel forces (not in line) that produce rotation only."],
    ["Couples", "Define the torque of a couple.", "One force × perpendicular distance between the two forces."],
    ["Couples", "Resultant force of a couple?", "Zero, so no linear acceleration."],
    ["Couples", "Does the torque of a couple depend on the axis?", "No, it's the same about any point."],
    ["Equilibrium", "Two conditions for equilibrium?", "Resultant force zero and resultant moment zero."],
    ["Equilibrium", "Translational vs rotational motion?", "Translational: all parts move the same direction and speed. Rotational: all parts move in circles about an axis."],
    ["Equilibrium", "Three forces in equilibrium form what?", "A closed triangle; their lines of action meet at one point."],
    ["Equilibrium", "Single force through the centre of mass produces?", "Pure translational motion."],
    ["Density & pressure", "Define density.", "Mass per unit volume."],
    ["Density & pressure", "Define pressure.", "Normal force per unit area."],
    ["Density & pressure", "Pressure at depth h in a fluid?", "Δp = ρgh (add atmospheric pressure for total)."],
    ["Density & pressure", "Derive p = ρgh.", "Column weight = ρAhg on area A ⇒ p = ρgh."],
    ["Density & pressure", "Effect of altitude on atmospheric pressure?", "Higher altitude, lower pressure."],
    ["Upthrust", "Cause of upthrust?", "Pressure difference between the bottom and top surfaces of the object."],
    ["Upthrust", "Formula for upthrust?", "ρ_f g V = weight of fluid displaced."],
    ["Upthrust", "Condition for floating?", "Upthrust equals weight."],
    ["Upthrust", "Apparent weight in a fluid?", "Weight − upthrust."],
    ["Moments", "Uniform metre rule: where is its weight?", "At the 50 cm mark."],
    ["Moments", "Moment of an angled force F at angle θ to the bar, distance d?", "F d sin θ."],
]

QUIZ = [
    {"s": "Moments", "q": "A couple consists of:", "o": ["two equal forces in the same direction", "two equal, opposite, parallel forces not in line", "two equal, opposite forces in the same line", "a force and its reaction"], "c": 1, "e": "Opposite forces in the same line would cancel with no turning."},
    {"s": "Moments", "q": "100 g rule pivoted at 40 cm; 20 g pulls up at 100 cm. Where must 50 g hang to balance?", "o": ["4 cm", "36 cm", "44 cm", "64 cm"], "c": 2, "e": "1000 + 50x = 1200 ⇒ x = 4 cm right of pivot (Nov 14/13)."},
    {"s": "Moments", "q": "Forces 15 N each on opposite sides of a 0.40 m diameter wheel. Torque?", "o": ["3.0 N m", "6.0 N m", "12 N m", "30 N m"], "c": 1, "e": "15 × 0.40 = 6.0 N m."},
    {"s": "Equilibrium", "q": "For an object to be in equilibrium:", "o": ["resultant force zero only", "resultant moment zero only", "both resultant force and moment zero", "velocity zero"], "c": 2, "e": "Both conditions are needed."},
    {"s": "Pressure", "q": "Pressure due to 10 m of water (ρ = 1000):", "o": ["9.8 × 10² Pa", "9.8 × 10³ Pa", "9.8 × 10⁴ Pa", "9.8 × 10⁵ Pa"], "c": 2, "e": "1000 × 9.81 × 10 = 9.8 × 10⁴ Pa."},
    {"s": "Upthrust", "q": "Upthrust on a fully submerged object depends on:", "o": ["object's density", "object's mass", "fluid density and object's volume", "depth of the object"], "c": 2, "e": "ρ_f g V; independent of depth once fully submerged."},
    {"s": "Moments", "q": "A ladder rests on icy (frictionless) ground against a rough wall. The force from the ground is:", "o": ["horizontal", "vertical", "along the ladder", "zero"], "c": 1, "e": "No friction, so only a normal (vertical) reaction (June 12/12)."},
]


def write():
    meta = {"title": "Forces, Density and Pressure Deck", "short": "Phys Ch4", "bar": "Physics · Forces, density & pressure",
            "code": "9702 · AS · Chapter 4", "key": "deck-9702-ch4"}
    cards = build()
    out = engine.render(meta, cards, FLASH, QUIZ, math=True).replace("<b>Paper 1 quiz</b>", "<b>Chapter 4 quiz</b>")
    (HERE / "deck-phys-ch4.html").write_text(unique_markers(out), encoding="utf8")
    print("phys ch4", len(out), "bytes,", len(cards), "cards,", len(FLASH), "flashcards,", len(QUIZ), "quiz")
    return cards


if __name__ == "__main__":
    write()
