"""9702 Physics · Chapter 2 Kinematics.
Built from Tuah's Topical Notes (2.1 Displacement + graph drawing, 2.5 Motion at constant acceleration,
Free Fall, Projectile Motion). Cambridge notation, g = 9.81 m s⁻², answers to 2-3 s.f."""
import math, pathlib
import engine
from fixids import unique_markers
from engine import card
from diagrams import fig
from phys_graphs import Plot, tg

HERE = pathlib.Path(__file__).parent
G = 9.81


def up_down():
    u = 29.4
    T = 2 * u / G
    a = Plot(xr=(0, 6.2), yr=(0, 48), xl="t", yl="s", aria="s-t for a ball thrown up: parabola", dn="+ve ↑")
    a.curve(lambda t: u * t - 0.5 * G * t * t, 0, T)
    b = Plot(xr=(0, 6.2), yr=(-32, 32), xl="t", yl="v", aria="v-t for a ball thrown up: straight line from +u to −u", dn="+ve ↑")
    b.path([(0, u), (T, -u)]).t(3, 0, "v = 0 at top", "t-s", 4, -8)
    c = Plot(xr=(0, 6.2), yr=(-12, 4), xl="t", yl="a", aria="a-t: constant −9.81", dn="+ve ↑")
    c.path([(0, -G), (T, -G)]).t(1, -G, "−9.81", "t-s", 0, -8)
    return fig(("Displacement", a), ("Velocity", b), ("Acceleration", c),
               caption="Thrown up at 29.4 m s⁻¹ (up +). Velocity falls steadily through zero at the top; acceleration is −g throughout, even at the top.")


def terminal():
    p = Plot(xr=(0, 10), yr=(0, 10), xl="t", yl="v", aria="velocity-time with air resistance, curves to terminal velocity", w=310, h=200)
    p.curve(lambda t: 8 * (1 - math.exp(-t / 2.2)), 0, 10)
    p.path([(0, 0), (2.2, 8)], "s")
    p.guide([(0, 8), (10, 8)])
    p.t(2.2, 8, "gradient = g at t = 0", "t-s", 6, 4)
    p.t(7, 8, "terminal velocity", "t-s", 0, -8, "middle")
    return fig(p, caption="As v rises, drag rises, so resultant force (W − D) and acceleration fall. At terminal velocity D = W and a = 0.")


def trajectory():
    p = Plot(xr=(0, 10), yr=(0, 5), xl="x", yl="y", aria="projectile trajectory parabola with constant horizontal velocity and changing vertical velocity", w=320, h=190)
    p.curve(lambda x: 4.2 * (1 - ((x - 5) / 5) ** 2), 0, 10)
    p.arrow((0, 0), (1.4, 2.0)).t(0.7, 1.6, "u", "t-s", -6, 0, "end")
    p.arrow((5, 4.2), (6.4, 4.2)).t(5.7, 4.2, "uₓ only", "t-s", 0, -6, "middle")
    p.t(5, 0, "range", "t-s", 0, 14, "middle")
    return fig(p, caption="Horizontal: uₓ = u cos θ, constant (aₓ = 0). Vertical: u<sub>y</sub> = u sin θ, a<sub>y</sub> = −g. Link the two with the same time t.")


def build():
    C = []
    C.append(card("cover", "Start", "Kinematics", "Cover", r"""
<p class="sec" style="margin:0">CAIE 9702 · AS Level · Chapter 2</p>
<p class="cover-k">v</p>
<h1>Kinematics</h1>
<p class="lede">Displacement, velocity and acceleration; s–t, v–t and a–t graphs; SUVAT; stopping distance; free fall and terminal velocity; projectiles. Built from your Chapter 2 topical notes and the past-paper questions done in class.</p>
<div class="stat"><div><b>4</b>worked examples</div><div><b>6</b>practice Qs</div><div><b>24</b>flashcards</div></div>
<p><a href="index.html">Open Revision Hub</a></p>
<div class="swipehint">Swipe or use the arrows · tap ☰ for contents</div>""", sec="Start"))

    C.append(card("big", "Start", "The big picture", "Overview", r"""
<h2>Describing motion without forces</h2>
<div class="chain"><span>Choose + direction</span><i>→</i><span>List s u v a t</span><i>→</i><span>Pick the SUVAT missing one</span><i>→</i><span>Check sign of answer</span></div>
<div class="tw"><table>
<tr><th>Graph</th><th>Gradient</th><th>Area under</th></tr>
<tr><td class="k">s–t</td><td>velocity</td><td>(no meaning)</td></tr>
<tr><td class="k">v–t</td><td>acceleration</td><td>displacement</td></tr>
<tr><td class="k">a–t</td><td>(not needed)</td><td>change in velocity</td></tr>
</table></div>
<div class="note link"><b>More graphs</b>Your Physics Graphs deck has every shape (bouncing ball, air resistance, curved graphs) in detail.</div>""", sec="Start"))

    S = "Definitions"
    C.append(card("defs", S, "Displacement, velocity, acceleration", "Concept", r"""
<h2>Definitions to memorise</h2>
<div class="def"><div class="lab">Displacement</div><p>The distance moved <b>in a specified direction</b> from a fixed point: \(\Delta x = x_f - x_i\).</p></div>
<div class="def"><div class="lab">Speed</div><p>The <b>rate of change of distance</b>.</p></div>
<div class="def"><div class="lab">Velocity</div><p>The <b>rate of change of displacement</b>.</p></div>
<div class="def"><div class="lab">Acceleration</div><p>The <b>rate of change of velocity</b>.</p></div>
<div class="note tip"><b>Your notes</b>From −2.5 m to −10 m the displacement is −7.5 m; the sign shows direction. Average velocity = total displacement ÷ total time, which can be 0 for a round trip even though average speed isn't.</div>""", sec=S))

    C.append(card("graphs", S, "Sketching s–t to v–t to a–t", "Concept", r"""
<h2>Reading one graph off another</h2>
<ul>
<li><b>v at any instant</b> = gradient of the s–t graph (draw a <b>tangent</b> if curved).</li>
<li>s–t <b>straight</b> ⇒ constant v; <b>curving up</b> ⇒ speeding up; <b>flat</b> ⇒ at rest; <b>peak</b> ⇒ v = 0 (turning point).</li>
<li><b>a</b> = gradient of v–t. Straight v–t ⇒ constant a.</li>
<li>v–t <b>crosses the axis</b> ⇒ object reverses direction.</li>
</ul>
""" + up_down() + r"""
<div class="note trap"><b>Trap</b>At the top of the flight \(v = 0\) but \(a = -9.81\) m s⁻², <b>not</b> zero.</div>""", sec=S))

    C.append(card("bounce", S, "Bouncing ball graphs", "Concept", r"""
<h2>Ball dropped and bouncing (down +)</h2>
<ul>
<li><b>v–t:</b> straight lines of gradient \(+g\) while falling; at each bounce v <b>jumps</b> from \(+v\) to a smaller \(-v\) almost instantly; then the same gradient \(+g\) again.</li>
<li>Each rebound is <b>lower</b>: KE is lost to thermal energy and sound on impact.</li>
<li><b>a–t:</b> constant \(+g\), with large spikes during the short contact times.</li>
<li>The steep line at the bounce is the <b>change in momentum</b> over a short contact time ⇒ large force.</li>
</ul>
<div class="note tip"><b>State your direction</b>Always write "down positive" or "up positive" on the axis label. It flips every sign on the v–t graph.</div>""", sec=S))

    K = "SUVAT"
    C.append(card("suvat", K, "Equations of uniformly accelerated motion", "Concept", r"""
<h2>The four equations (constant acceleration only)</h2>
<div class="tw"><table>
<tr><td class="k">no \(s\)</td><td>\(v = u + at\)</td></tr>
<tr><td class="k">no \(a\)</td><td>\(s = \tfrac12(u + v)t\)</td></tr>
<tr><td class="k">no \(v\)</td><td>\(s = ut + \tfrac12at^2\)</td></tr>
<tr><td class="k">no \(t\)</td><td>\(v^2 = u^2 + 2as\)</td></tr>
</table></div>
<div class="def"><div class="lab">Derivation (asked for in Paper 2)</div>
<p>\(a = \dfrac{v - u}{t} \Rightarrow v = u + at\)</p>
<p>Area under v–t: \(s = \tfrac12(u+v)t\)</p>
<p>Substitute \(v\): \(s = \tfrac12(2u + at)t = ut + \tfrac12at^2\)</p>
<p>Substitute \(t = (v-u)/a\): \(2as = v^2 - u^2\)</p></div>
<div class="note trap"><b>Only for constant a</b>Not valid with air resistance or a changing force.</div>""", sec=K))

    C.append(card("stop", K, "Stopping distance", "Concept", r"""
<h2>Thinking + braking</h2>
<div class="formula">stopping distance = thinking distance + braking distance</div>
<div class="tw"><table>
<tr><td class="k">Thinking distance</td><td>travelled at <b>constant speed</b> during the reaction time: \(s = ut_r\)</td></tr>
<tr><td class="k">Braking distance</td><td>while decelerating: \(0 = u^2 + 2as \Rightarrow s = \dfrac{u^2}{2|a|}\)</td></tr>
</table></div>
<div class="note link"><b>Speed matters twice</b>Thinking distance ∝ \(u\), but braking distance ∝ \(u^2\): doubling speed quadruples braking distance.</div>
<div class="note tip"><b>Linking to forces</b>Braking force gives \(a = F/m\). Your notes: 1200 kg car, braking force 2400 N ⇒ \(a = -2\) m s⁻² ⇒ from 20 m s⁻¹, braking distance = 100 m.</div>""", sec=K))

    F = "Free fall"
    C.append(card("ff", F, "Free fall", "Concept", r"""
<h2>Acceleration of free fall, g</h2>
<p>With no air resistance every object falls with the same acceleration \(g = 9.81\) m s⁻², whatever its mass.</p>
<ul>
<li>Released from rest (down +): \(s = \tfrac12gt^2\), \(v = gt\).</li>
<li>s–t is a parabola; v–t a straight line through the origin with gradient \(g\); a–t flat at \(g\).</li>
<li>Measuring \(g\): time a fall through measured heights, plot \(s\) against \(t^2\); gradient \(= g/2\).</li>
</ul>
<div class="note link"><b>From class (June 02 Q9)</b>Ball released from rest a distance \(x\) above marker M₁; reaches M₁ at \(t_1\), M₂ (a further \(h\) below) at \(t_2\). Then \(x = \tfrac12at_1^2\) and \(x + h = \tfrac12at_2^2\), so \(a = \dfrac{2h}{t_2^2 - t_1^2}\).</div>
<div class="note tip"><b>g is not constant at large heights</b>It falls with distance from Earth. Near the surface (a few km) treat it as 9.81 m s⁻².</div>""", sec=F))

    C.append(card("term", F, "Air resistance and terminal velocity", "Concept", r"""
<h2>Falling with drag</h2>
""" + terminal() + r"""
<div class="formula">\(a = \dfrac{W - D}{m}\)</div>
<ol>
<li>At release \(v = 0\), so \(D = 0\) and \(a = g\).</li>
<li>As \(v\) increases, \(D\) increases, so the resultant force and \(a\) decrease.</li>
<li>When \(D = W\): resultant force zero, \(a = 0\), constant <b>terminal velocity</b>.</li>
</ol>
<div class="note link"><b>Heavier objects</b>Same shape and area but larger mass ⇒ larger W ⇒ drag must be larger to balance ⇒ higher terminal velocity, reached later. Since \(D \propto v^2\), \(v_t \propto \sqrt W\).</div>""", sec=F))

    P = "Projectiles"
    C.append(card("proj", P, "Projectile motion", "Concept", r"""
<h2>Two independent motions, one shared time</h2>
""" + trajectory() + r"""
<div class="tw"><table>
<tr><th>Horizontal</th><th>Vertical</th></tr>
<tr><td>\(u_x = u\cos\theta\), constant</td><td>\(u_y = u\sin\theta\)</td></tr>
<tr><td>\(a_x = 0\)</td><td>\(a_y = -g\) (up +)</td></tr>
<tr><td>\(s_x = u_xt\)</td><td>\(s_y = u_yt - \tfrac12gt^2\)</td></tr>
</table></div>
<div class="note tip"><b>Horizontal launch</b>\(u_y = 0\): find \(t\) from the drop height, \(t = \sqrt{2h/g}\), then range \(= u_xt\).</div>""", sec=P))

    C.append(card("range", P, "Time of flight, range, maximum height", "Concept", r"""
<h2>Launched from and landing on level ground</h2>
<div class="tw"><table>
<tr><td class="k">Time of flight</td><td>\(s_y = 0 \Rightarrow t = \dfrac{2u\sin\theta}{g}\)</td></tr>
<tr><td class="k">Range</td><td>\(R = u\cos\theta\cdot\dfrac{2u\sin\theta}{g} = \dfrac{u^2\sin2\theta}{g}\)</td></tr>
<tr><td class="k">Maximum height</td><td>\(v_y = 0 \Rightarrow H = \dfrac{(u\sin\theta)^2}{2g}\)</td></tr>
</table></div>
<p>Range is greatest when \(\sin2\theta = 1\), i.e. \(\theta = 45°\).</p>
<div class="note trap"><b>At the top</b>Velocity is <b>not</b> zero: \(v = u_x\). Only the vertical component is zero.</div>
<div class="note link"><b>Velocity after time t (June 03)</b>Vertical \(u\sin\alpha - gt\), horizontal \(u\cos\alpha\). The horizontal part never changes.</div>""", sec=P))

    W = "Worked examples"
    C.append(card("we1", W, "Example 1: stopping distance", "Worked example", r"""
<h2>Example 1 · Car at 20 m s⁻¹</h2>
<p><b>Q:</b> A driver travelling at 20 m s⁻¹ has a reaction time of 0.20 s. The brakes give a deceleration of 10 m s⁻². Find the stopping distance.</p>
<ol class="steps">
<li>""" + tg("A1") + r""" Thinking: \(s = 20 \times 0.20 = 4.0\) m</li>
<li>""" + tg("M1") + r""" Braking: \(0 = 20^2 + 2(-10)s\)</li>
<li>""" + tg("A1") + r""" \(s = 20\) m</li>
<li>""" + tg("A1") + r""" Stopping distance = 4.0 + 20 = 24 m</li>
</ol>""", sec=W))

    C.append(card("we2", W, "Example 2: ball hits a wall (Nov 11 P21)", "Worked example", r"""
<h2>Example 2 · Ball thrown at a wall</h2>
<p><b>Q:</b> A ball is thrown from S at 15.0 m s⁻¹, 60.0° to the horizontal. The wall is 9.95 m away horizontally. Find (a) the components of the initial velocity, (b) the height at which it hits the wall.</p>
<ol class="steps">
<li>""" + tg("A1") + r""" \(u_x = 15.0\cos60° = 7.50\) m s⁻¹</li>
<li>""" + tg("A1") + r""" \(u_y = 15.0\sin60° = 13.0\) m s⁻¹</li>
<li>""" + tg("C1") + r""" Time to wall: \(t = 9.95/7.50 = 1.33\) s</li>
<li>""" + tg("A1") + r""" \(s_y = 13.0(1.33) - \tfrac12(9.81)(1.33)^2 = 8.6\) m</li>
</ol>
<div class="note link"><b>Why it hits at right angles</b>At \(t = 1.33\) s, \(v_y = 13.0 - 9.81(1.33) \approx 0\): the ball is at the top of its path, moving horizontally.</div>""", sec=W))

    C.append(card("we3", W, "Example 3: thrown downwards (June 12 P22)", "Worked example", r"""
<h2>Example 3 · Ball thrown down past A</h2>
<p><b>Q:</b> A ball passes A, 5.0 m above the ground, moving down at 8.4 m s⁻¹. Calculate its speed on reaching the ground and show the time taken is 0.47 s.</p>
<ol class="steps">
<li>""" + tg("C1") + r""" Down +: \(v^2 = 8.4^2 + 2(9.81)(5.0)\)</li>
<li>""" + tg("A1") + r""" \(v = 13\) m s⁻¹</li>
<li>""" + tg("M1") + r""" \(v = u + at \Rightarrow 13.0 = 8.4 + 9.81t\)</li>
<li>""" + tg("A1") + r""" \(t = 0.47\) s</li>
</ol>
<div class="note trap"><b>Sign check</b>With down +, \(u = +8.4\) and \(a = +9.81\). Mixing signs is the most common slip here.</div>""", sec=W))

    C.append(card("we4", W, "Example 4: horizontal launch", "Worked example", r"""
<h2>Example 4 · Motorcycle stunt</h2>
<p><b>Q:</b> A motorcyclist leaves a ramp horizontally 1.25 m above the ground and lands 10 m away. Find the take-off speed.</p>
<ol class="steps">
<li>""" + tg("C1") + r""" Vertical, \(u_y = 0\): \(1.25 = \tfrac12(9.81)t^2\)</li>
<li>""" + tg("A1") + r""" \(t = 0.505\) s</li>
<li>""" + tg("A1") + r""" \(u_x = 10/0.505 = 20\) m s⁻¹</li>
</ol>""", sec=W))

    C.append(card("traps", "Mistakes", "Common mistakes", "Concept", r"""
<h2>Where marks are lost</h2>
<div class="note trap"><b>No positive direction</b>State "up +" or "down +" first; then g has one consistent sign.</div>
<div class="note trap"><b>a = 0 at the top</b>Only v is zero; a = g all the way.</div>
<div class="note trap"><b>SUVAT with drag</b>Only valid for constant acceleration.</div>
<div class="note trap"><b>Projectile speed at the top = 0</b>It's \(u\cos\theta\).</div>
<div class="note trap"><b>Using u (not uₓ) for range</b>Horizontal distance uses the horizontal component only.</div>
<div class="note trap"><b>Distance from a v–t graph that crosses zero</b>Displacement = area above − area below; distance = sum of both.</div>
<div class="note trap"><b>Vague terminal-velocity answers</b>Say what happens to drag, resultant force and acceleration, in that order.</div>""", sec="Mistakes"))

    C.append(card("pr", "Practice", "Practice questions", "Practice", r"""
<h2>Practice · Kinematics</h2>
<div class="pq"><div class="qh"><span>Q1 · Horizontal launch</span><span class="mk">[3]</span></div>
<p class="qt">A tiger leaps horizontally at 3.5 m s⁻¹ from a rock 6.5 m high. How far from the base of the rock does it land?</p>
<div class="ans"><b>Answer</b>\(t = \sqrt{2(6.5)/9.81} = 1.15\) s; \(x = 3.5 \times 1.15 = 4.0\) m.</div></div>
<div class="pq"><div class="qh"><span>Q2 · SUVAT</span><span class="mk">[2]</span></div>
<p class="qt">A car passes marker posts 100 m apart at 10 m s⁻¹ and then 20 m s⁻¹, accelerating uniformly. Find its acceleration.</p>
<div class="ans"><b>Answer</b>\(20^2 = 10^2 + 2a(100) \Rightarrow a = 1.5\) m s⁻².</div></div>
<div class="pq"><div class="qh"><span>Q3 · Vertical throw</span><span class="mk">[3]</span></div>
<p class="qt">A ball is thrown vertically up at 12 m s⁻¹. Find its maximum height and its total time in the air (returning to the same level).</p>
<div class="ans"><b>Answer</b>\(H = 12^2/(2 \times 9.81) = 7.3\) m; \(t = 2(12)/9.81 = 2.4\) s.</div></div>
<div class="pq"><div class="qh"><span>Q4 · Range</span><span class="mk">[2]</span></div>
<p class="qt">A ball is kicked at 20 m s⁻¹. What angle gives the maximum range on level ground, and what is that range?</p>
<div class="ans"><b>Answer</b>45°; \(R = u^2/g = 400/9.81 = 41\) m.</div></div>
<div class="pq"><div class="qh"><span>Q5 · Rebound</span><span class="mk">[2]</span></div>
<p class="qt">A ball rebounds vertically from the ground at 4.2 m s⁻¹. Find the maximum height it reaches.</p>
<div class="ans"><b>Answer</b>\(h = 4.2^2/(2 \times 9.81) = 0.90\) m.</div></div>
<div class="pq"><div class="qh"><span>Q6 · Explain</span><span class="mk">[3]</span></div>
<p class="qt">A skydiver jumps from a plane. Explain why she reaches a terminal velocity.</p>
<div class="ans"><b>Answer</b>Initially only weight acts, so a = g. As speed increases, air resistance increases, so the resultant force (W − D) decreases and acceleration decreases. When air resistance equals weight, resultant force is zero, a = 0, and she moves at constant (terminal) velocity.</div></div>""", sec="Practice"))

    C.append(card("sheet", "Summary", "Formula card", "Summary", r"""
<h2>Everything on one card</h2>
<div class="tw"><table>
<tr><td class="k">SUVAT</td><td>\(v = u + at\) · \(s = \tfrac12(u+v)t\) · \(s = ut + \tfrac12at^2\) · \(v^2 = u^2 + 2as\)</td></tr>
<tr><td class="k">s–t</td><td>gradient = velocity</td></tr>
<tr><td class="k">v–t</td><td>gradient = acceleration · area = displacement</td></tr>
<tr><td class="k">Stopping</td><td>\(ut_r + u^2/2|a|\)</td></tr>
<tr><td class="k">Free fall</td><td>\(a = g = 9.81\) m s⁻², independent of mass</td></tr>
<tr><td class="k">Drag</td><td>\(a = (W - D)/m\); terminal when \(D = W\)</td></tr>
<tr><td class="k">Projectile</td><td>\(u_x = u\cos\theta\) const; \(u_y = u\sin\theta\), \(a_y = -g\)</td></tr>
<tr><td class="k">Flight</td><td>\(t = 2u\sin\theta/g\) · \(R = u^2\sin2\theta/g\) · \(H = u^2\sin^2\theta/2g\)</td></tr>
</table></div>""", sec="Summary"))
    return C


FLASH = [
    ["Definitions", "Define displacement.", "Distance moved in a specified direction from a fixed point."],
    ["Definitions", "Define velocity.", "Rate of change of displacement."],
    ["Definitions", "Define acceleration.", "Rate of change of velocity."],
    ["Definitions", "Speed vs velocity?", "Speed: rate of change of distance (scalar). Velocity: rate of change of displacement (vector)."],
    ["Graphs", "Gradient of s–t?", "Velocity."],
    ["Graphs", "Gradient and area of v–t?", "Gradient = acceleration; area = displacement."],
    ["Graphs", "Area under a–t?", "Change in velocity."],
    ["Graphs", "v–t line crosses the time axis. Meaning?", "The object momentarily stops and reverses direction."],
    ["Graphs", "Velocity from a curved s–t graph?", "Gradient of the tangent at that instant."],
    ["SUVAT", "Which equation has no s?", "v = u + at."],
    ["SUVAT", "Which equation has no t?", "v² = u² + 2as."],
    ["SUVAT", "Which equation has no v?", "s = ut + ½at²."],
    ["SUVAT", "Condition for using SUVAT?", "Constant acceleration in a straight line."],
    ["SUVAT", "Thinking vs braking distance dependence on speed?", "Thinking ∝ u; braking ∝ u²."],
    ["Free fall", "Value and condition for g = 9.81 m s⁻²?", "Near Earth's surface, no air resistance; same for all masses."],
    ["Free fall", "Velocity and acceleration at the top of a vertical throw?", "v = 0, a = −9.81 m s⁻² (still g)."],
    ["Free fall", "Acceleration of a falling object with drag?", "a = (W − D)/m."],
    ["Free fall", "Condition for terminal velocity?", "Drag equals weight, resultant force zero, acceleration zero."],
    ["Free fall", "Same shape, heavier object: terminal velocity?", "Higher, because drag must grow larger to balance the larger weight."],
    ["Projectiles", "Horizontal motion of a projectile?", "Constant velocity u cos θ; zero acceleration."],
    ["Projectiles", "Vertical motion of a projectile?", "Initial u sin θ; acceleration −g."],
    ["Projectiles", "Velocity at the top of a projectile's path?", "u cos θ, horizontal."],
    ["Projectiles", "Range on level ground?", "R = u² sin 2θ / g, maximum at 45°."],
    ["Projectiles", "Time to fall height h from a horizontal launch?", "t = √(2h/g)."],
]

QUIZ = [
    {"s": "Graphs", "q": "The area under a velocity–time graph gives:", "o": ["acceleration", "displacement", "speed", "force"], "c": 1, "e": "Area = displacement; gradient = acceleration."},
    {"s": "SUVAT", "q": "A car speeds up from 10 m s⁻¹ to 20 m s⁻¹ over 100 m. Acceleration?", "o": ["0.67 m s⁻²", "1.5 m s⁻²", "2.5 m s⁻²", "6.0 m s⁻²"], "c": 1, "e": "v² = u² + 2as ⇒ 400 = 100 + 200a ⇒ a = 1.5."},
    {"s": "Free fall", "q": "A ball thrown upwards is at its highest point. Which is true?", "o": ["v = 0, a = 0", "v = 0, a = g downwards", "v = max, a = 0", "v = g, a = 0"], "c": 1, "e": "Acceleration is g throughout the flight."},
    {"s": "Free fall", "q": "A falling object has reached terminal velocity. The resultant force is:", "o": ["equal to its weight", "zero", "equal to drag", "decreasing"], "c": 1, "e": "Drag = weight, so resultant force = 0."},
    {"s": "Projectiles", "q": "A projectile is fired at speed u, angle α. Its velocity components after time t are:", "o": ["u sin α, u cos α", "u sin α − gt, u cos α − gt", "u sin α − gt (vertical), u cos α (horizontal)", "u cos α (vertical), u sin α − gt (horizontal)"], "c": 2, "e": "Only the vertical component changes (June 03)."},
    {"s": "Projectiles", "q": "A rider leaves a ramp horizontally 1.25 m up and lands 10 m away. Take-off speed?", "o": ["5 m s⁻¹", "10 m s⁻¹", "15 m s⁻¹", "20 m s⁻¹"], "c": 3, "e": "t = √(2×1.25/9.81) = 0.50 s; u = 10/0.50 = 20 m s⁻¹."},
    {"s": "Free fall", "q": "Released from rest, a ball passes markers x and x + h below its start at times t₁ and t₂. Its acceleration is:", "o": ["2h/t₂²", "2h/(t₂ + t₁)", "2h/(t₂ − t₁)²", "2h/(t₂² − t₁²)"], "c": 3, "e": "x = ½at₁², x + h = ½at₂² ⇒ h = ½a(t₂² − t₁²) (June 02)."},
    {"s": "SUVAT", "q": "Doubling a car's speed multiplies its braking distance by:", "o": ["√2", "2", "4", "8"], "c": 2, "e": "Braking distance = u²/2a ∝ u²."},
]


def write():
    meta = {"title": "Kinematics Deck", "short": "Phys Ch2", "bar": "Physics · Kinematics",
            "code": "9702 · AS · Chapter 2", "key": "deck-9702-ch2"}
    cards = build()
    out = engine.render(meta, cards, FLASH, QUIZ, math=True).replace("<b>Paper 1 quiz</b>", "<b>Kinematics quiz</b>").replace('<figure class="dg">', '<figure class="dg" style="max-width:520px">')
    (HERE / "deck-phys-ch2.html").write_text(unique_markers(out), encoding="utf8")
    print("phys ch2", len(out), "bytes,", len(cards), "cards,", len(FLASH), "flashcards,", len(QUIZ), "quiz")
    return cards


if __name__ == "__main__":
    write()
