"""9702 Physics · Chapter 5 Work, energy and power.
Built from Tuah's Topical Notes (Work, KE & Work-Energy Theorem, Potential Energy, Efficiency) plus the
syllabus power section. Cambridge notation, g = 9.81 m s⁻², answers to 2-3 s.f."""
import pathlib
import engine
from fixids import unique_markers
from engine import card
from diagrams import fig
from phys_graphs import Plot, tg

HERE = pathlib.Path(__file__).parent


def epe():
    p = Plot(xr=(0, 10), yr=(0, 10), xl="x", yl="F", aria="force-extension straight line, triangle area is elastic potential energy", w=300, h=190)
    p.fill([(0, 0), (8, 8), (8, 0)], "fb").path([(0, 0), (9, 9)]).hg(8, 8, "F").vg(8, 8, "x")
    p.t(5.6, 2.4, "½Fx = ½kx²", "t-pt", 0, 0, "middle")
    return fig(p, caption="Work done stretching = area under F–x. Average force is ½F because the force grows from 0.")


def build():
    C = []
    C.append(card("cover", "Start", "Work, energy and power", "Cover", r"""
<p class="sec" style="margin:0">CAIE 9702 · AS Level · Chapter 5</p>
<p class="cover-k">W</p>
<h1>Work, energy and power</h1>
<p class="lede">Work done, the work–energy theorem, kinetic, gravitational and elastic potential energy, conservation of energy, efficiency and power. Built from your Chapter 5 topical notes.</p>
<div class="stat"><div><b>4</b>worked examples</div><div><b>5</b>practice Qs</div><div><b>22</b>flashcards</div></div>
<p><a href="index.html">Open Revision Hub</a></p>
<div class="swipehint">Swipe or use the arrows · tap ☰ for contents</div>""", sec="Start"))

    C.append(card("big", "Start", "The big picture", "Overview", r"""
<h2>Energy is transferred by doing work</h2>
<div class="chain"><span>Work \(= Fs\cos\theta\)</span><i>→</i><span>\(W_{\text{net}} = \Delta KE\)</span><i>→</i><span>Energy conserved</span><i>→</i><span>Efficiency, power</span></div>
<div class="note tip"><b>When to use energy</b>If a question gives heights, distances and speeds but no time, energy is usually faster than SUVAT, and it works when the force or acceleration isn't constant.</div>""", sec="Start"))

    S = "Work and energy"
    C.append(card("work", S, "Work done", "Concept", r"""
<h2>Defining work</h2>
<div class="def"><div class="lab">Work done</div><p>The product of the force and the <b>displacement in the direction of the force</b>: \(W = Fs\cos\theta\). Unit J.</p></div>
<div class="def"><div class="lab">The joule</div><p>The work done when a force of 1 N moves its point of application 1 m in the direction of the force.</p></div>
<ul>
<li>\(\theta = 0°\): \(W = Fs\). \(\theta = 90°\): \(W = 0\) (e.g. weight on horizontal motion).</li>
<li>\(\theta = 180°\): \(W = -Fs\) (friction, braking): energy is removed.</li>
</ul>
<div class="note trap"><b>Fix in your notes</b>"Work = energy transferred to work" is circular. Say: <b>work done = energy transferred</b>, by a force moving through a distance.</div>""", sec=S))

    C.append(card("energy", S, "Energy and the work–energy theorem", "Concept", r"""
<h2>From \(v^2 = u^2 + 2as\) to \(\Delta KE\)</h2>
<div class="def"><div class="lab">Derivation of \(E_k = \tfrac12mv^2\)</div>
<p>Constant force \(F\) on mass \(m\) over \(s\): \(v^2 = u^2 + 2as\)</p>
<p>× \(\tfrac12m\): \(\tfrac12mv^2 = \tfrac12mu^2 + mas\)</p>
<p>\(Fs = mas = \tfrac12mv^2 - \tfrac12mu^2\)</p></div>
<div class="formula">\(W_{\text{net}} = \Delta KE\)</div>
<p>The net (resultant) work done on an object equals its change in kinetic energy.</p>
<div class="note tip"><b>From your notes</b>Not all forces do work: whether a force does work depends on the angle between the force and the displacement.</div>""", sec=S))

    C.append(card("gpe", S, "Gravitational potential energy", "Concept", r"""
<h2>Lifting against gravity</h2>
<div class="def"><div class="lab">Derivation of \(\Delta E_p = mg\Delta h\)</div>
<p>Lift at constant speed: applied force = weight = \(mg\)</p>
<p>Work done = force × distance = \(mg\Delta h\)</p>
<p>This work is stored as gravitational potential energy</p></div>
<div class="formula">\(\Delta E_p = mg\Delta h\)</div>
<div class="note trap"><b>Uniform field only</b>\(mg\Delta h\) assumes \(g\) is constant, true close to Earth's surface (height changes small compared with Earth's radius). Your note "max height 1 km" is a sensible rule of thumb, not an exam fact.</div>""", sec=S))

    C.append(card("epe", S, "Elastic potential energy", "Concept", r"""
<h2>Energy stored by deformation</h2>
<p>Elastic potential (strain) energy is stored when an object is <b>stretched, compressed or deformed</b> elastically.</p>
""" + epe() + r"""
<div class="formula">\(E_P = \tfrac12Fx = \tfrac12kx^2\)</div>
<div class="note trap"><b>Within the limit of proportionality</b>\(\tfrac12kx^2\) needs a straight-line F–x graph. Otherwise use the area under the curve. (See your Chapter 6 deck.)</div>""", sec=S))

    C.append(card("cons", S, "Conservation of energy", "Concept", r"""
<h2>Energy is transferred, never lost</h2>
<div class="def"><div class="lab">Principle of conservation of energy</div><p>Energy cannot be created or destroyed, only <b>transferred from one form to another</b>. The total energy of a closed system is constant.</p></div>
<ul>
<li>No friction: \(\tfrac12mv^2 + mgh\) = constant ⇒ falling from \(h\): \(v = \sqrt{2gh}\).</li>
<li>With friction or air resistance: loss in \(E_p\) = gain in \(E_k\) + work done against resistance.</li>
</ul>
<div class="note link"><b>June 12 P22 (from class)</b>A ball falls, bounces and rises lower. Total mechanical energy decreases: energy goes to thermal energy and sound in the ball and ground on impact (deformation), not "lost".</div>""", sec=S))

    P = "Efficiency and power"
    C.append(card("eff", P, "Efficiency", "Concept", r"""
<h2>How much is useful?</h2>
<div class="def"><div class="lab">Efficiency</div><p>The ratio of <b>useful energy output</b> to <b>total energy input</b>.</p></div>
<div class="formula">\(\eta = \dfrac{\text{useful energy out}}{\text{total energy in}} = \dfrac{\text{useful power out}}{\text{total power in}}\)</div>
<p>× 100 for a percentage. Efficiency is always less than 100% for real machines; the rest is usually thermal energy.</p>""", sec=P))

    C.append(card("power", P, "Power", "Concept", r"""
<h2>The rate of doing work</h2>
<div class="def"><div class="lab">Power</div><p>The <b>work done per unit time</b> (rate of energy transfer): \(P = \dfrac{W}{t}\). Unit W.</p></div>
<div class="def"><div class="lab">The watt</div><p>One joule per second.</p></div>
<div class="def"><div class="lab">Derivation of \(P = Fv\)</div>
<p>\(P = \dfrac Wt = \dfrac{Fs}{t} = F\dfrac st = Fv\)</p></div>
<div class="note tip"><b>Vehicles at constant speed</b>Driving force = resistive force, so power = resistive force × speed. Up a slope, add \(mg\sin\theta\) to the force.</div>""", sec=P))

    W = "Worked examples"
    C.append(card("we1", W, "Example 1: work at an angle", "Worked example", r"""
<h2>Example 1 · Pulling a sledge</h2>
<p><b>Q:</b> A rope pulls a sledge 8.0 m along level ground with a tension of 50 N at 30° above the horizontal. Find the work done by the tension.</p>
<ol class="steps">
<li>""" + tg("C1") + r""" \(W = Fs\cos\theta\)</li>
<li>""" + tg("A1") + r""" \(W = 50(8.0)\cos30° = 350\) J</li>
</ol>
<div class="note trap"><b>Where marks go</b>Using 50 × 8.0 = 400 J ignores the angle. Only the component along the motion does work.</div>""", sec=W))

    C.append(card("we2", W, "Example 2: efficiency (your notes)", "Worked example", r"""
<h2>Example 2 · KE converted to GPE</h2>
<p><b>Q:</b> A 700 kg vehicle moving at 3.5 m s⁻¹ is brought to rest. 20% of its kinetic energy is used to lift a load through 12 m. Find the mass of the load.</p>
<ol class="steps">
<li>""" + tg("C1") + r""" \(E_k = \tfrac12(700)(3.5)^2 = 4290\) J</li>
<li>""" + tg("C1") + r""" Useful: \(0.20 \times 4287.5 = 858\) J</li>
<li>""" + tg("M1") + r""" \(mg\Delta h = 858 \Rightarrow m(9.81)(12) = 858\)</li>
<li>""" + tg("A1") + r""" \(m = 7.3\) kg</li>
</ol>""", sec=W))

    C.append(card("we3", W, "Example 3: power up a slope", "Worked example", r"""
<h2>Example 3 · Car on a hill</h2>
<p><b>Q:</b> A 1200 kg car climbs a 5.0° slope at a constant 15 m s⁻¹ against a resistive force of 500 N. Find the power output.</p>
<ol class="steps">
<li>""" + tg("M1") + r""" Constant speed ⇒ driving force = \(500 + mg\sin5.0°\)</li>
<li>""" + tg("A1") + r""" \(F = 500 + 1200(9.81)\sin5.0° = 1530\) N</li>
<li>""" + tg("A1") + r""" \(P = Fv = 1530 \times 15 = 2.3\times10^4\) W</li>
</ol>""", sec=W))

    C.append(card("we4", W, "Example 4: energy with friction", "Worked example", r"""
<h2>Example 4 · Sledge down a hill</h2>
<p><b>Q:</b> A 40 kg sledge starts from rest and descends 12 m vertically along a 60 m slope, reaching 14 m s⁻¹ at the bottom. Find the energy dissipated and the average resistive force.</p>
<ol class="steps">
<li>""" + tg("C1") + r""" Loss of \(E_p = 40(9.81)(12) = 4709\) J</li>
<li>""" + tg("C1") + r""" Gain of \(E_k = \tfrac12(40)(14)^2 = 3920\) J</li>
<li>""" + tg("A1") + r""" Work against friction \(= 789 \approx 790\) J</li>
<li>""" + tg("A1") + r""" \(F = 789/60 = 13\) N</li>
</ol>""", sec=W))

    C.append(card("traps", "Mistakes", "Common mistakes", "Concept", r"""
<h2>Where marks are lost</h2>
<div class="note trap"><b>Ignoring the angle</b>Work uses the component of displacement along the force.</div>
<div class="note trap"><b>Energy "lost"</b>Energy is transferred (to thermal energy, sound), never destroyed.</div>
<div class="note trap"><b>Weight doing work on horizontal motion</b>Force ⟂ displacement does no work.</div>
<div class="note trap"><b>Efficiency > 1</b>Check output < input; useful ÷ total.</div>
<div class="note trap"><b>P = Fv with the wrong F</b>At constant speed, F is the driving force, which equals the total resistance (plus mg sin θ on a slope).</div>
<div class="note trap"><b>½kx² outside Hooke's law</b>Use the area under the curve.</div>""", sec="Mistakes"))

    C.append(card("pr", "Practice", "Practice questions", "Practice", r"""
<h2>Practice · Work, energy and power</h2>
<div class="pq"><div class="qh"><span>Q1 · Free fall energy</span><span class="mk">[2]</span></div>
<p class="qt">A ball is dropped from 5.0 m. Ignoring air resistance, find its speed just before it hits the ground.</p>
<div class="ans"><b>Answer</b>\(mgh = \tfrac12mv^2 \Rightarrow v = \sqrt{2(9.81)(5.0)} = 9.9\) m s⁻¹.</div></div>
<div class="pq"><div class="qh"><span>Q2 · Spring launcher</span><span class="mk">[3]</span></div>
<p class="qt">A spring (k = 200 N m⁻¹) is compressed 0.10 m and launches a 0.050 kg ball vertically. Find the maximum height (no losses).</p>
<div class="ans"><b>Answer</b>\(E_P = \tfrac12(200)(0.10)^2 = 1.0\) J = \(mgh \Rightarrow h = 1.0/(0.050 \times 9.81) = 2.0\) m.</div></div>
<div class="pq"><div class="qh"><span>Q3 · Lift motor</span><span class="mk">[3]</span></div>
<p class="qt">A motor lifts an 800 kg lift 15 m in 20 s at constant speed. It is 60% efficient. Find the useful power output and the power input.</p>
<div class="ans"><b>Answer</b>Useful \(= 800(9.81)(15)/20 = 5.9\) kW; input \(= 5886/0.60 = 9.8\) kW.</div></div>
<div class="pq"><div class="qh"><span>Q4 · Car power</span><span class="mk">[2]</span></div>
<p class="qt">A car travels at a constant 25 m s⁻¹ on level ground against a 600 N resistance. Find its power output.</p>
<div class="ans"><b>Answer</b>Driving force = 600 N; \(P = 600 \times 25 = 15\) kW.</div></div>
<div class="pq"><div class="qh"><span>Q5 · Derive</span><span class="mk">[3]</span></div>
<p class="qt">Show that the kinetic energy of a mass m moving at speed v is ½mv².</p>
<div class="ans"><b>Answer</b>Constant force F accelerates m from rest over s: \(v^2 = 2as\). Work done \(= Fs = mas = m(v^2/2) = \tfrac12mv^2\), which is the KE gained.</div></div>""", sec="Practice"))

    C.append(card("sheet", "Summary", "Formula card", "Summary", r"""
<h2>Everything on one card</h2>
<div class="tw"><table>
<tr><td class="k">Work</td><td>\(W = Fs\cos\theta\) · J</td></tr>
<tr><td class="k">Work–energy</td><td>\(W_{\text{net}} = \Delta KE\)</td></tr>
<tr><td class="k">KE</td><td>\(\tfrac12mv^2\)</td></tr>
<tr><td class="k">GPE</td><td>\(mg\Delta h\) (uniform field)</td></tr>
<tr><td class="k">EPE</td><td>\(\tfrac12Fx = \tfrac12kx^2\)</td></tr>
<tr><td class="k">Conservation</td><td>loss of \(E_p\) = gain of \(E_k\) + work against resistance</td></tr>
<tr><td class="k">Efficiency</td><td>useful out ÷ total in</td></tr>
<tr><td class="k">Power</td><td>\(P = W/t = Fv\) · W</td></tr>
</table></div>""", sec="Summary"))
    return C


FLASH = [
    ["Work", "Define work done.", "Force × displacement in the direction of the force; W = Fs cos θ."],
    ["Work", "Define the joule.", "Work done when 1 N moves its point of application 1 m in the direction of the force."],
    ["Work", "Work done by a force perpendicular to motion?", "Zero."],
    ["Work", "Work done by friction on a moving object?", "Negative: the force opposes the displacement."],
    ["Work", "State the work–energy theorem.", "Net work done on an object equals its change in kinetic energy."],
    ["Energy", "Define energy.", "The capacity to do work."],
    ["Energy", "Derive KE = ½mv².", "Fs = mas and v² = 2as ⇒ Fs = ½mv²."],
    ["Energy", "Derive ΔEp = mgΔh.", "Lift at constant speed: force = mg; work = mgΔh."],
    ["Energy", "When is ΔEp = mgΔh valid?", "Uniform gravitational field, i.e. near Earth's surface."],
    ["Energy", "Elastic potential energy formula?", "½Fx = ½kx² (within the limit of proportionality)."],
    ["Energy", "State the principle of conservation of energy.", "Energy cannot be created or destroyed, only transferred between forms."],
    ["Energy", "Falling from rest through h (no resistance): speed?", "v = √(2gh)."],
    ["Energy", "Falling with air resistance: energy equation?", "Loss of Ep = gain of Ek + work done against air resistance."],
    ["Efficiency", "Define efficiency.", "Useful energy (or power) output ÷ total energy (or power) input."],
    ["Efficiency", "Where does wasted energy usually go?", "Thermal energy (and sound)."],
    ["Power", "Define power.", "Work done (energy transferred) per unit time."],
    ["Power", "Define the watt.", "One joule per second."],
    ["Power", "Derive P = Fv.", "P = W/t = Fs/t = Fv."],
    ["Power", "Car at constant speed: driving force?", "Equal to the total resistive force (plus mg sin θ on a slope)."],
    ["Power", "Base units of the watt?", "kg m² s⁻³."],
    ["Energy", "Bouncing ball rises lower each time. Why?", "Kinetic energy is transferred to thermal energy and sound on impact."],
    ["Work", "Work from a force–displacement graph?", "Area under the graph."],
]

QUIZ = [
    {"s": "Work", "q": "A 50 N force at 60° to the direction of motion moves an object 4.0 m. Work done?", "o": ["50 J", "100 J", "173 J", "200 J"], "c": 1, "e": "50 × 4.0 × cos60° = 100 J."},
    {"s": "Energy", "q": "A 2.0 kg mass speeds up from 3.0 to 5.0 m s⁻¹. Net work done on it?", "o": ["4.0 J", "8.0 J", "16 J", "34 J"], "c": 2, "e": "½(2)(25 − 9) = 16 J."},
    {"s": "Energy", "q": "Ball dropped from 20 m (no air resistance). Speed at the ground?", "o": ["14 m s⁻¹", "19.8 m s⁻¹", "39 m s⁻¹", "392 m s⁻¹"], "c": 1, "e": "√(2 × 9.81 × 20) = 19.8 m s⁻¹. D forgets the square root."},
    {"s": "Power", "q": "A crane lifts 500 kg through 10 m in 25 s. Useful power?", "o": ["200 W", "1.96 kW", "4.9 kW", "49 kW"], "c": 1, "e": "500 × 9.81 × 10 / 25 = 1962 W."},
    {"s": "Efficiency", "q": "A motor takes 2.0 kW and lifts at a useful 1.5 kW. Efficiency?", "o": ["25%", "67%", "75%", "133%"], "c": 2, "e": "1.5/2.0 = 75%."},
    {"s": "Power", "q": "A car's engine gives 30 kW at a constant 20 m s⁻¹. Resistive force?", "o": ["600 N", "1500 N", "3000 N", "6.0 × 10⁵ N"], "c": 1, "e": "F = P/v = 30000/20 = 1500 N."},
    {"s": "Energy", "q": "Spring k = 400 N m⁻¹ stretched 5.0 cm. Energy stored?", "o": ["0.50 J", "1.0 J", "10 J", "20 J"], "c": 0, "e": "½ × 400 × 0.050² = 0.50 J."},
]


def write():
    meta = {"title": "Work, Energy and Power Deck", "short": "Phys Ch5", "bar": "Physics · Work, energy & power",
            "code": "9702 · AS · Chapter 5", "key": "deck-9702-ch5"}
    cards = build()
    out = engine.render(meta, cards, FLASH, QUIZ, math=True).replace("<b>Paper 1 quiz</b>", "<b>Chapter 5 quiz</b>").replace('<figure class="dg">', '<figure class="dg" style="max-width:520px">')
    (HERE / "deck-phys-ch5.html").write_text(unique_markers(out), encoding="utf8")
    print("phys ch5", len(out), "bytes,", len(cards), "cards,", len(FLASH), "flashcards,", len(QUIZ), "quiz")
    return cards


if __name__ == "__main__":
    write()
