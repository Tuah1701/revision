"""9702 Physics · Chapter 3 Dynamics (momentum, Newton's laws, collisions).
Built from Tuah's Topical Notes (Newton's 2nd Law, 3rd Law, Momentum incl. 2D, Collision, Relative speed).
Cambridge notation, g = 9.81 m s⁻², answers to 2-3 s.f."""
import pathlib
import engine
from fixids import unique_markers
from engine import card
from diagrams import fig
from phys_graphs import Plot, tg

HERE = pathlib.Path(__file__).parent


def ft():
    p = Plot(xr=(0, 10), yr=(0, 10), xl="t", yl="F", aria="force-time graph for a collision, area under it is the impulse", w=300, h=190)
    p.fill([(1, 0), (5, 8), (9, 0)], "fb").path([(0, 0), (1, 0), (5, 8), (9, 0), (10, 0)])
    p.t(5, 3, "area = impulse = Δp", "t-pt", 0, 0, "middle")
    return fig(p, caption="Impulse = FΔt = area under F–t = change in momentum. Longer contact time ⇒ smaller peak force for the same Δp.")


def build():
    C = []
    C.append(card("cover", "Start", "Dynamics", "Cover", r"""
<p class="sec" style="margin:0">CAIE 9702 · AS Level · Chapter 3</p>
<p class="cover-k">p</p>
<h1>Dynamics</h1>
<p class="lede">Momentum, Newton's three laws, impulse, conservation of momentum in one and two dimensions, elastic and inelastic collisions. Built from your Chapter 3 topical notes and the past-paper questions from class.</p>
<div class="stat"><div><b>4</b>worked examples</div><div><b>5</b>practice Qs</div><div><b>24</b>flashcards</div></div>
<p><a href="index.html">Open Revision Hub</a></p>
<div class="swipehint">Swipe or use the arrows · tap ☰ for contents</div>""", sec="Start"))

    C.append(card("big", "Start", "The big picture", "Overview", r"""
<h2>Forces change momentum</h2>
<div class="chain"><span>\(p = mv\)</span><i>→</i><span>\(F = \Delta p/\Delta t\)</span><i>→</i><span>Impulse \(F\Delta t = \Delta p\)</span><i>→</i><span>No external force ⇒ \(p\) conserved</span></div>
<div class="tw"><table>
<tr><th>Question says…</th><th>Use</th></tr>
<tr><td>force and acceleration</td><td>\(F = ma\)</td></tr>
<tr><td>force and a time / rate of mass flow</td><td>\(F = \Delta p/\Delta t\)</td></tr>
<tr><td>collision, explosion, coalesce</td><td>conservation of momentum</td></tr>
<tr><td>"elastic"</td><td>momentum + KE (or relative speeds)</td></tr>
</table></div>""", sec="Start"))

    S = "Newton's laws"
    C.append(card("mom", S, "Mass, weight and momentum", "Concept", r"""
<h2>Definitions</h2>
<div class="def"><div class="lab">Mass</div><p>The property of an object that <b>resists changes in its motion</b> (inertia).</p></div>
<div class="def"><div class="lab">Weight</div><p>The <b>gravitational force</b> on a mass: \(W = mg\). It acts at the centre of gravity.</p></div>
<div class="def"><div class="lab">Linear momentum</div><p>The <b>product of mass and velocity</b>: \(p = mv\), unit kg m s⁻¹ (= N s). A vector.</p></div>
<div class="note trap"><b>Mass ≠ weight</b>Mass in kg, a scalar, the same everywhere; weight in N, a vector, depends on g.</div>""", sec=S))

    C.append(card("laws", S, "Newton's three laws", "Concept", r"""
<h2>The three laws in examiner wording</h2>
<div class="def"><div class="lab">First law</div><p>A body remains at rest or moves with constant velocity unless acted on by a <b>resultant</b> force.</p></div>
<div class="def"><div class="lab">Second law</div><p>The resultant force on a body is <b>proportional to the rate of change of its momentum</b>, and acts in the direction of the change in momentum.</p></div>
<div class="def"><div class="lab">Third law</div><p>If body A exerts a force on body B, then B exerts a force on A that is <b>equal in magnitude and opposite in direction</b>.</p></div>
<div class="formula">\(F = \dfrac{\Delta p}{\Delta t} = \dfrac{mv - mu}{t}\); constant mass ⇒ \(F = ma\)</div>
<div class="note trap"><b>Third-law pairs</b>Act on <b>different</b> bodies and are the <b>same type</b> of force. Weight and normal reaction on a book are <b>not</b> a third-law pair (both act on the book).</div>""", sec=S))

    C.append(card("newton", S, "The newton", "Concept", r"""
<h2>Defining the unit of force</h2>
<div class="def"><div class="lab">The newton</div><p>The force that gives a mass of 1 kg an acceleration of 1 m s⁻² (in the direction of the force).</p></div>
<p>So 1 N = 1 kg m s⁻². \(F = ma\) is only valid with \(F\) in N, \(m\) in kg, \(a\) in m s⁻².</p>
<div class="note tip"><b>Always the resultant force</b>Draw all forces, find the net force along the motion, then \(F_{\text{net}} = ma\).</div>""", sec=S))

    I = "Impulse and momentum"
    C.append(card("imp", I, "Impulse", "Concept", r"""
<h2>Force × time = change in momentum</h2>
<div class="def"><div class="lab">Impulse</div><p>The product of force and the time for which it acts: \(F\Delta t = \Delta p\). Unit N s.</p></div>
""" + ft() + r"""
<div class="note link"><b>Collisions deform objects</b>During impact the large forces squash the ball (your deformed tennis ball sketch). Crumple zones and airbags increase \(\Delta t\), so \(F\) is smaller for the same \(\Delta p\).</div>
<div class="note trap"><b>Rebounds</b>Δp = m(v − u) with signs: 20 m s⁻¹ in and 15 m s⁻¹ out is a change of <b>35</b> m s⁻¹, not 5.</div>""", sec=I))

    C.append(card("cons", I, "Conservation of momentum", "Concept", r"""
<h2>The principle</h2>
<div class="def"><div class="lab">Principle of conservation of momentum</div><p>For a system of interacting bodies, the <b>total momentum remains constant</b>, provided <b>no resultant external force</b> acts.</p></div>
<div class="formula">\(m_1u_1 + m_2u_2 = m_1v_1 + m_2v_2\)</div>
<ul>
<li>Choose a positive direction; velocities the other way are <b>negative</b>.</li>
<li><b>Coalesce</b> (stick together): \(m_1u_1 + m_2u_2 = (m_1+m_2)v\).</li>
<li><b>Explosion</b> from rest: total momentum after = 0, so the pieces move in opposite directions.</li>
</ul>
<div class="note link"><b>Why it follows from Newton's laws</b>Third law: forces on A and B are equal and opposite, for the same time ⇒ equal and opposite impulses ⇒ total Δp = 0.</div>""", sec=I))

    C.append(card("el", I, "Elastic and inelastic collisions", "Concept", r"""
<h2>Is kinetic energy conserved?</h2>
<div class="tw"><table>
<tr><th></th><th>Elastic</th><th>Inelastic</th></tr>
<tr><td class="k">Momentum</td><td>conserved</td><td>conserved</td></tr>
<tr><td class="k">Kinetic energy</td><td>conserved</td><td><b>not</b> conserved (some → thermal, sound, deformation)</td></tr>
<tr><td class="k">Total energy</td><td>conserved</td><td>conserved</td></tr>
</table></div>
<div class="def"><div class="lab">Elastic collision shortcut</div><p>Relative speed of approach = relative speed of separation: \(u_1 - u_2 = v_2 - v_1\).</p></div>
<div class="note trap"><b>Elastic only</b>Use the relative-speed rule only for elastic collisions. Otherwise calculate KE before and after separately.</div>
<div class="note tip"><b>Relative speed</b>Opposite directions: <b>add</b> the speeds. Same direction: <b>subtract</b>.</div>""", sec=I))

    C.append(card("derive", I, "Where the relative-speed rule comes from", "Concept", r"""
<h2>Deriving \(u_1 + v_1 = u_2 + v_2\)</h2>
<div class="def"><div class="lab">Two conservation laws</div>
<p>Momentum: \(m_1(u_1 - v_1) = m_2(v_2 - u_2)\) … (1)</p>
<p>KE: \(m_1(u_1^2 - v_1^2) = m_2(v_2^2 - u_2^2)\) … (2)</p>
<p>(2) ÷ (1): \(u_1 + v_1 = v_2 + u_2\)</p>
<p>Rearranged: \(u_1 - u_2 = v_2 - v_1\)</p></div>
<div class="note trap"><b>Signs</b>Every \(u\) and \(v\) carries its sign from your chosen positive direction. N 03 Q12: X right at \(u_X\), Y left at \(u_Y\), separating with X left at \(v_X\), Y right at \(v_Y\): \(u_X + u_Y = v_X + v_Y\).</div>""", sec=I))

    C.append(card("twod", I, "Momentum in two dimensions", "Concept", r"""
<h2>Conserve each component separately</h2>
<ul>
<li>Resolve every momentum into x and y components.</li>
<li>Total x-momentum before = total x-momentum after; same for y.</li>
<li>If everything starts along x, the total y-momentum after must be <b>zero</b>.</li>
</ul>
<div class="formula">x: \(mu = mv_A\cos60° + mv_B\cos30°\) · y: \(0 = mv_A\sin60° - mv_B\sin30°\)</div>
<div class="note trap"><b>Not a scalar sum</b>You can't add momenta in different directions as plain numbers. Resolve first.</div>""", sec=I))

    W = "Worked examples"
    C.append(card("we1", W, "Example 1: coalescing", "Worked example", r"""
<h2>Example 1 · Trolleys stick together</h2>
<p><b>Q:</b> A 2.0 kg trolley at 3.0 m s⁻¹ hits a stationary 1.0 kg trolley and they move off together. Find the common velocity and the kinetic energy lost. Is the collision elastic?</p>
<ol class="steps">
<li>""" + tg("C1") + r""" \(2.0(3.0) + 0 = 3.0v\)</li>
<li>""" + tg("A1") + r""" \(v = 2.0\) m s⁻¹</li>
<li>""" + tg("C1") + r""" KE before \(= \tfrac12(2.0)(3.0)^2 = 9.0\) J; after \(= \tfrac12(3.0)(2.0)^2 = 6.0\) J</li>
<li>""" + tg("A1") + r""" 3.0 J lost ⇒ <b>inelastic</b> (KE not conserved)</li>
</ol>""", sec=W))

    C.append(card("we2", W, "Example 2: elastic collision (N 09 P11)", "Worked example", r"""
<h2>Example 2 · 2m and m, equal speeds</h2>
<p><b>Q:</b> Masses 2m and m approach head-on, each at speed u, and collide elastically. Show that after the collision 2m moves at u/3 backwards and m at 5u/3.</p>
<ol class="steps">
<li>""" + tg("B1") + r""" Right +. Momentum before: \(2mu - mu = mu\)</li>
<li>""" + tg("B1") + r""" After: \(2m(-u/3) + m(5u/3) = mu\) ✓</li>
<li>""" + tg("B1") + r""" Relative speed of approach \(= u + u = 2u\)</li>
<li>""" + tg("A1") + r""" Separation \(= 5u/3 + u/3 = 2u\) ✓ ⇒ elastic</li>
</ol>
<div class="note tip"><b>Paper 1 elimination</b>Option D (stick together) can't be elastic. Test the others for momentum first, then relative speed.</div>""", sec=W))

    C.append(card("we3", W, "Example 3: 2D collision (June 16/23)", "Worked example", r"""
<h2>Example 3 · Particles at 60° and 30°</h2>
<p><b>Q:</b> Particle A (mass m) at 500 m s⁻¹ hits stationary B (mass m) elastically. After, A moves at \(v_A\) at 60° to the x-direction and B at \(v_B\) at 30° on the other side. Find \(v_A\) and \(v_B\).</p>
<ol class="steps">
<li>""" + tg("M1") + r""" y: \(0 = mv_A\sin60° - mv_B\sin30° \Rightarrow v_B = \sqrt3\,v_A\)</li>
<li>""" + tg("M1") + r""" x: \(500m = mv_A\cos60° + mv_B\cos30° = \tfrac12mv_A + \tfrac32mv_A\)</li>
<li>""" + tg("A1") + r""" \(v_A = 250\) m s⁻¹</li>
<li>""" + tg("A1") + r""" \(v_B = 433\) m s⁻¹</li>
</ol>
<div class="note link"><b>Check elastic</b>\(250^2 + 433^2 = 2.5\times10^5 = 500^2\), so KE is conserved ✓. Initial momentum \(= 1.67\times10^{-27} \times 500 = 8.4\times10^{-25}\) N s.</div>""", sec=W))

    C.append(card("we4", W, "Example 4: impulse on a rebound", "Worked example", r"""
<h2>Example 4 · Ball hits a wall</h2>
<p><b>Q:</b> A 0.15 kg ball hits a wall at 20 m s⁻¹ and rebounds at 15 m s⁻¹. Contact time is 0.010 s. Find the impulse and the average force.</p>
<ol class="steps">
<li>""" + tg("C1") + r""" Towards wall +: \(\Delta p = 0.15(-15) - 0.15(20)\)</li>
<li>""" + tg("A1") + r""" \(\Delta p = -5.25\) N s (magnitude 5.3 N s, away from the wall)</li>
<li>""" + tg("A1") + r""" \(F = 5.25/0.010 = 530\) N</li>
</ol>""", sec=W))

    C.append(card("traps", "Mistakes", "Common mistakes", "Concept", r"""
<h2>Where marks are lost</h2>
<div class="note trap"><b>Forgetting the minus sign</b>Velocities opposite to your positive direction must be negative.</div>
<div class="note trap"><b>"Momentum is conserved" with no condition</b>Add: provided no resultant external force acts.</div>
<div class="note trap"><b>Third-law pair on the same body</b>The pair acts on two different bodies.</div>
<div class="note trap"><b>Relative speeds for inelastic collisions</b>Only valid for elastic collisions.</div>
<div class="note trap"><b>Energy "lost"</b>Total energy is always conserved; <b>kinetic</b> energy is what's lost (to thermal/sound).</div>
<div class="note trap"><b>Adding 2D momenta as numbers</b>Resolve into components first.</div>""", sec="Mistakes"))

    C.append(card("pr", "Practice", "Practice questions", "Practice", r"""
<h2>Practice · Dynamics</h2>
<div class="pq"><div class="qh"><span>Q1 · Rate of change of momentum</span><span class="mk">[2]</span></div>
<p class="qt">Water leaves a hose at 2.0 kg s⁻¹ and 15 m s⁻¹, hits a wall and stops. Find the force on the wall.</p>
<div class="ans"><b>Answer</b>\(F = \dfrac{\Delta p}{\Delta t} = 2.0 \times 15 = 30\) N.</div></div>
<div class="pq"><div class="qh"><span>Q2 · Elastic collision</span><span class="mk">[4]</span></div>
<p class="qt">A 3.0 kg ball at 4.0 m s⁻¹ collides elastically head-on with a stationary 1.0 kg ball. Find both velocities after.</p>
<div class="ans"><b>Answer</b>Momentum: \(12 = 3v_1 + v_2\). Relative speed: \(4 = v_2 - v_1\). So \(v_1 = 2.0\) m s⁻¹, \(v_2 = 6.0\) m s⁻¹ (both forwards). KE: 24 J before and after ✓.</div></div>
<div class="pq"><div class="qh"><span>Q3 · F–t graph</span><span class="mk">[3]</span></div>
<p class="qt">A 0.50 kg ball at rest is struck. The force rises steadily from 0 to 40 N and back to 0 over 0.20 s (triangle). Find the impulse and the ball's final speed.</p>
<div class="ans"><b>Answer</b>Impulse = area = ½(40)(0.20) = 4.0 N s. \(v = 4.0/0.50 = 8.0\) m s⁻¹.</div></div>
<div class="pq"><div class="qh"><span>Q4 · Explosion</span><span class="mk">[3]</span></div>
<p class="qt">A 60 kg skater at rest pushes a 40 kg skater, who moves off at 3.0 m s⁻¹. Find the first skater's velocity and explain the direction.</p>
<div class="ans"><b>Answer</b>Total momentum 0: \(0 = 40(3.0) + 60v \Rightarrow v = -2.0\) m s⁻¹, i.e. 2.0 m s⁻¹ the opposite way. Equal and opposite forces (N3) for the same time give equal and opposite momenta.</div></div>
<div class="pq"><div class="qh"><span>Q5 · Define</span><span class="mk">[2]</span></div>
<p class="qt">State Newton's second law and the principle of conservation of momentum.</p>
<div class="ans"><b>Answer</b>N2: resultant force is proportional to the rate of change of momentum (in the direction of the change). Conservation: total momentum of a system is constant provided no resultant external force acts.</div></div>""", sec="Practice"))

    C.append(card("sheet", "Summary", "Formula card", "Summary", r"""
<h2>Everything on one card</h2>
<div class="tw"><table>
<tr><td class="k">Momentum</td><td>\(p = mv\) · kg m s⁻¹ = N s · vector</td></tr>
<tr><td class="k">N2</td><td>\(F = \Delta p/\Delta t\); constant m ⇒ \(F = ma\)</td></tr>
<tr><td class="k">Impulse</td><td>\(F\Delta t = \Delta p\) = area under F–t</td></tr>
<tr><td class="k">Conservation</td><td>\(m_1u_1 + m_2u_2 = m_1v_1 + m_2v_2\) (no resultant external force)</td></tr>
<tr><td class="k">Elastic</td><td>KE conserved; \(u_1 - u_2 = v_2 - v_1\)</td></tr>
<tr><td class="k">Inelastic</td><td>KE not conserved; total energy still is</td></tr>
<tr><td class="k">2D</td><td>conserve x and y components separately</td></tr>
<tr><td class="k">N3 pair</td><td>equal, opposite, same type, different bodies</td></tr>
</table></div>""", sec="Summary"))
    return C


FLASH = [
    ["Definitions", "Define mass.", "The property of an object that resists changes in its motion."],
    ["Definitions", "Define weight.", "The gravitational force on an object; W = mg."],
    ["Definitions", "Define linear momentum.", "The product of mass and velocity; p = mv."],
    ["Definitions", "Units of momentum?", "kg m s⁻¹, equivalent to N s."],
    ["Definitions", "Define the newton.", "The force that gives a 1 kg mass an acceleration of 1 m s⁻²."],
    ["Laws", "State Newton's first law.", "A body stays at rest or at constant velocity unless a resultant force acts on it."],
    ["Laws", "State Newton's second law.", "Resultant force is proportional to the rate of change of momentum, in the direction of the change."],
    ["Laws", "State Newton's third law.", "If A exerts a force on B, B exerts an equal and opposite force on A."],
    ["Laws", "Properties of a third-law pair?", "Equal magnitude, opposite direction, same type of force, act on different bodies."],
    ["Laws", "Are weight and normal reaction on a book a third-law pair?", "No: both act on the book (and are different types)."],
    ["Impulse", "Define impulse.", "Force × time it acts; equals change in momentum."],
    ["Impulse", "Impulse from a force–time graph?", "Area under the graph."],
    ["Impulse", "Why do airbags reduce injury?", "They increase the collision time, so the force for the same change in momentum is smaller."],
    ["Conservation", "State the principle of conservation of momentum.", "Total momentum of a system is constant provided no resultant external force acts."],
    ["Conservation", "Momentum after an explosion from rest?", "Total zero: pieces have equal and opposite momenta."],
    ["Conservation", "Equation for coalescing bodies?", "m₁u₁ + m₂u₂ = (m₁ + m₂)v."],
    ["Collisions", "Elastic collision: what is conserved?", "Momentum, kinetic energy and total energy."],
    ["Collisions", "Inelastic collision: what is conserved?", "Momentum and total energy; not kinetic energy."],
    ["Collisions", "Relative-speed rule and when it applies?", "Speed of approach = speed of separation; elastic collisions only."],
    ["Collisions", "Relative speed of two objects moving towards each other?", "Add their speeds."],
    ["Collisions", "Where does 'lost' KE go in an inelastic collision?", "Thermal energy, sound, and work done deforming the objects."],
    ["Collisions", "How to apply conservation of momentum in 2D?", "Conserve x and y components separately."],
    ["Collisions", "Ball 20 m s⁻¹ in, 15 m s⁻¹ out: change in velocity?", "35 m s⁻¹ (directions opposite)."],
    ["Laws", "F = ma requires what?", "Constant mass; F is the resultant force in N."],
]

QUIZ = [
    {"s": "Laws", "q": "Which pair of forces is a Newton's third law pair?", "o": ["weight of a book and table's push on it", "Earth's pull on the book and the book's pull on Earth", "friction and driving force on a car", "tension and weight on a hanging mass"], "c": 1, "e": "Same type (gravitational), different bodies."},
    {"s": "Impulse", "q": "Units of impulse:", "o": ["N s⁻¹", "N s", "kg m s⁻²", "J s"], "c": 1, "e": "FΔt ⇒ N s = kg m s⁻¹."},
    {"s": "Conservation", "q": "A 2 kg mass at 6 m s⁻¹ joins a 4 kg mass at rest. Common velocity?", "o": ["1.5 m s⁻¹", "2.0 m s⁻¹", "3.0 m s⁻¹", "6.0 m s⁻¹"], "c": 1, "e": "12 = 6v ⇒ v = 2.0."},
    {"s": "Collisions", "q": "In every collision with no external force:", "o": ["KE is conserved", "momentum is conserved", "the objects stick", "relative speed is conserved"], "c": 1, "e": "Momentum always; KE only if elastic."},
    {"s": "Collisions", "q": "X moves right at u_X, Y left at u_Y. After an elastic collision X moves left at v_X, Y right at v_Y. Which is correct?", "o": ["u_X + u_Y = v_X + v_Y", "u_X + u_Y = v_X − v_Y", "u_X − u_Y = v_X + v_Y", "u_X − u_Y = v_X − v_Y"], "c": 0, "e": "Approach (u_X + u_Y) = separation (v_X + v_Y) (N 03)."},
    {"s": "Impulse", "q": "A 0.20 kg ball at 10 m s⁻¹ rebounds at 10 m s⁻¹. Change in momentum magnitude:", "o": ["0", "2.0 N s", "4.0 N s", "20 N s"], "c": 2, "e": "0.20 × 20 = 4.0 N s."},
    {"s": "Collisions", "q": "Masses 2m and m approach each other at speed u and collide elastically. After:", "o": ["2m: u/3 back, m: 5u/3", "2m: u/6 back, m: 2u/3", "2m: u/6, m: 2u/3 same way", "they stick at u/3"], "c": 0, "e": "Momentum mu ✓; relative speeds 2u = 2u ✓ (N 09 P11)."},
]


def write():
    meta = {"title": "Dynamics Deck", "short": "Phys Ch3", "bar": "Physics · Dynamics",
            "code": "9702 · AS · Chapter 3", "key": "deck-9702-ch3"}
    cards = build()
    out = engine.render(meta, cards, FLASH, QUIZ, math=True).replace("<b>Paper 1 quiz</b>", "<b>Dynamics quiz</b>").replace('<figure class="dg">', '<figure class="dg" style="max-width:520px">')
    (HERE / "deck-phys-ch3.html").write_text(unique_markers(out), encoding="utf8")
    print("phys ch3", len(out), "bytes,", len(cards), "cards,", len(FLASH), "flashcards,", len(QUIZ), "quiz")
    return cards


if __name__ == "__main__":
    write()
