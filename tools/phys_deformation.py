"""9702 Physics · Chapter 6 Deformation of solids (6.1 Stress and strain, 6.2 Elastic and plastic behaviour).
Built from Tuah's CollaNote notebooks 6.1, 6.2, Material Types and Exercise (KYUEM Physics slides + his annotations).
Cambridge notation, g = 9.81 m s⁻², answers to 2-3 s.f."""
import pathlib
import engine
from engine import card
from diagrams import fig
from phys_graphs import Plot, tg

HERE = pathlib.Path(__file__).parent


# ---------------------------------------------------------------- diagrams
def fx_full():
    p = Plot(xr=(0, 10), yr=(0, 10), xl="extension x", yl="F", aria="force-extension graph: straight line to the limit of proportionality, curve to the elastic limit, plastic region to the breaking point", w=330, h=220)
    p.path([(0, 0), (4, 6)])
    p.curve(lambda x: 6 + 1.6 * (1 - (1 - (x - 4) / 1.6) ** 2), 4, 5.6)
    p.curve(lambda x: 7.6 + 0.5 * (x - 5.6) - 0.16 * (x - 5.6) ** 2, 5.6, 9.4)
    p.pt(4, 6).pt(5.6, 7.6).pt(9.4, 7.19)
    p.t(4, 6, "P · limit of proportionality", "t-s", 6, 12)
    p.t(5.6, 7.6, "E · elastic limit", "t-s", -4, -9, "end")
    p.t(9.4, 7.19, "breaks", "t-s", 0, -9, "middle")
    p.t(1.6, 4.4, "F = kx", "t-d", 0, 0, "end")
    p.vg(4, 6).vg(5.6, 7.6)
    return fig(p, caption="O→P straight: Hooke's law. P→E curved but still elastic. Beyond E: plastic (permanent) deformation.")


def materials():
    a = Plot(xr=(0, 10), yr=(0, 10), xl="x", yl="F", aria="ductile: straight then long plastic region")
    a.path([(0, 0), (2.2, 6)]).curve(lambda x: 6 + 2.6 * (1 - ((x - 6) / 3.8) ** 2) if x < 6 else 8.6 - 0.12 * (x - 6) ** 2, 2.2, 9.5).pt(9.5, 7.13)
    b = Plot(xr=(0, 10), yr=(0, 10), xl="x", yl="F", aria="brittle: straight line then sudden break")
    b.path([(0, 0), (5, 8)]).pt(5, 8).t(5, 8, "breaks", "t-s", 6, 4)
    c = Plot(xr=(0, 10), yr=(0, 10), xl="x", yl="F", aria="polymeric rubber: curve flattens then steepens")
    c.curve(lambda x: 3.2 * x ** 0.5 if x < 2 else 4.53 + 0.25 * (x - 2) + 0.025 * (x - 2) ** 2.4, 0, 9.5)
    return fig(("Ductile (copper)", a), ("Brittle (glass)", b), ("Polymeric (rubber)", c),
               caption="Ductile: long plastic region. Brittle: straight line, then snaps with no plastic region. Polymeric: elastic but not Hooke's law.")


def unload():
    p = Plot(xr=(0, 10), yr=(0, 10), xl="x", yl="F", aria="ductile metal loaded past the elastic limit then unloaded along a parallel line, leaving a permanent extension", w=320, h=210)
    p.path([(0, 0), (2.5, 6)]).curve(lambda x: 6 + 2 * (1 - ((x - 6.5) / 4) ** 2), 2.5, 6.5)
    p.path([(6.5, 8), (3.17, 0)], "s")
    p.pt(6.5, 8).pt(3.17, 0, hollow=True)
    p.t(3.17, 0, "permanent extension", "t-s", 6, -6)
    p.t(6.5, 8, "unloaded here", "t-s", 4, -8)
    return fig(p, caption="Unloading line is parallel to the loading line (same k). The gap left on the x-axis is the permanent (plastic) extension.")


def energy():
    p = Plot(xr=(0, 10), yr=(0, 10), xl="x", yl="F", aria="energy stored equals area of triangle under the straight force-extension line", w=300, h=200)
    p.fill([(0, 0), (8, 8), (8, 0)], "fb").path([(0, 0), (9, 9)])
    p.hg(8, 8, "F").vg(8, 8, "x")
    p.t(5.6, 2.4, "E_P = ½Fx", "t-pt", 0, 0, "middle")
    return fig(p, caption="Work done = area under F–x. Straight line ⇒ triangle ⇒ ½Fx = ½kx². Curved ⇒ count squares.")


def lvf():
    p = Plot(xr=(0, 7), yr=(0, 1), xl="F / N", yl="ΔL / mm", aria="extension against force: straight line through origin, gradient = 1/k", w=310, h=200)
    p.path([(0, 0), (6.4, 0.98)])
    for f in (1, 2, 3, 4, 5, 6):
        p.pt(f, f * 0.153)
    p.guide([(1.5, 0.23), (6, 0.23), (6, 0.92)])
    p.t(3.8, 0.23, "ΔF (large)", "t-sm", 0, 13, "middle").t(6, 0.55, "ΔL", "t-sm", 6, 0)
    return fig(p, caption="Plot ΔL (y) against F (x). Gradient G = ΔL/F = 1/k, so E = 4L / (πd²G). Use a triangle over half the line.")


# ---------------------------------------------------------------- cards
def build():
    C = []
    C.append(card("cover", "Start", "Deformation of solids", "Cover", r"""
<p class="sec" style="margin:0">CAIE 9702 · AS Level · Chapter 6</p>
<p class="cover-k">E</p>
<h1>Deformation of solids</h1>
<p class="lede">6.1 Stress and strain · 6.2 Elastic and plastic behaviour. Built from your 6.1, 6.2, Material Types and Exercise notebooks, with the wording fixed to mark-scheme standard.</p>
<div class="stat"><div><b>4</b>worked examples</div><div><b>6</b>practice Qs</div><div><b>1</b>required practical</div></div>
<p><a href="index.html">Open Revision Hub</a></p>
<div class="swipehint">Swipe or use the arrows · tap ☰ for contents</div>""", sec="Start"))

    C.append(card("big", "Start", "The big picture", "Overview", r"""
<h2>What the chapter is really about</h2>
<p class="lede">A force can change an object's <b>shape</b> as well as its motion. Chapter 6 asks: how much does it stretch, does it come back, and how much energy does it store?</p>
<div class="chain"><span>Force ⇒ deformation</span><i>→</i><span>Hooke's law \(F = kx\)</span><i>→</i><span>Stress, strain, \(E\)</span><i>→</i><span>Elastic or plastic?</span><i>→</i><span>Energy \(\tfrac12Fx\)</span></div>
<div class="tw"><table>
<tr><th>6.1 Stress and strain</th><th>6.2 Elastic and plastic</th></tr>
<tr><td>tensile and compressive forces; load, extension, compression, limit of proportionality; Hooke's law; \(k = F/x\); stress, strain, Young modulus; Young modulus experiment</td><td>elastic vs plastic deformation; elastic limit; F–x graph shapes (ductile, brittle, polymeric); elastic potential energy = area under F–x; \(E_P = \tfrac12Fx = \tfrac12kx^2\)</td></tr>
</table></div>""", sec="Start"))

    S = "6.1 Stress and strain"
    C.append(card("tc", S, "Tension and compression", "Concept", r"""
<h2>Two ways to deform in one dimension</h2>
<div class="tw"><table>
<tr><th></th><th>Tensile force (tension)</th><th>Compressive force</th></tr>
<tr><td class="k">Forces</td><td>pull outwards, away from each other</td><td>push inwards, towards each other</td></tr>
<tr><td class="k">Effect</td><td>longer and thinner</td><td>shorter and fatter</td></tr>
<tr><td class="k">Length</td><td>\(L_0 + \Delta L\)</td><td>\(L_0 - \Delta L\)</td></tr>
<tr><td class="k">Example</td><td>steel cable, bottom of a loaded beam</td><td>building column, top of a loaded beam</td></tr>
</table></div>
<div class="note link"><b>Loaded beam</b>A beam bent by a load: the <b>top surface is compressed</b> (particles closer), the <b>bottom is stretched</b> (particles further apart), and the <b>neutral axis</b> in the middle doesn't change length.</div>
<div class="note tip"><b>Why it springs back</b>Displaced molecules feel a <b>restoring force</b> pulling them back to their equilibrium separation. That is what makes a material elastic.</div>""", sec=S))

    C.append(card("terms", S, "Load, extension, compression", "Concept", r"""
<h2>Definitions to memorise</h2>
<div class="def"><div class="lab">Load</div><p>The force applied to an object that causes it to deform.</p></div>
<div class="def"><div class="lab">Extension</div><p>The <b>increase in length</b> of an object when a tensile force is applied: \(x = L - L_0\).</p></div>
<div class="def"><div class="lab">Compression</div><p>The <b>decrease in length</b> of an object when a compressive force is applied.</p></div>
<div class="def"><div class="lab">Limit of proportionality</div><p>The point beyond which the extension is <b>no longer proportional</b> to the load (Hooke's law no longer applies).</p></div>
<div class="note trap"><b>Trap</b>Extension is the <b>change</b> in length, not the new length. Read both scale positions and subtract.</div>""", sec=S))

    C.append(card("hooke", S, "Hooke's law and the F–x graph", "Concept", r"""
<h2>Hooke's law</h2>
<div class="def"><div class="lab">Hooke's law</div><p>The extension of an object is <b>directly proportional</b> to the load applied, provided the <b>limit of proportionality is not exceeded</b>.</p></div>
<div class="formula">\(F = kx\)</div>
""" + fx_full() + r"""
<div class="note trap"><b>P ≠ E</b>Between the limit of proportionality and the elastic limit the graph is curved (no Hooke's law) but the object <b>still returns</b> to its original length.</div>""", sec=S))

    C.append(card("k", S, "Spring constant", "Concept", r"""
<h2>The spring constant \(k\)</h2>
<div class="def"><div class="lab">Spring constant</div><p>The <b>force per unit extension</b>: \(k = \dfrac{F}{x}\), unit N m⁻¹. It measures <b>stiffness</b>.</p></div>
<p>Bigger \(k\) ⇒ more force needed for the same extension ⇒ stiffer. It's the <b>gradient</b> of F–x (or <b>1 ÷ gradient</b> of x–F).</p>
<div class="tw"><table>
<tr><th>Factor</th><th>Change</th><th>Effect on \(k\)</th></tr>
<tr><td class="k">Material</td><td>stronger bonding between atoms</td><td>larger</td></tr>
<tr><td class="k">Coil diameter</td><td>larger diameter</td><td>smaller</td></tr>
<tr><td class="k">Wire thickness</td><td>thicker wire</td><td>larger</td></tr>
<tr><td class="k">Natural length</td><td>longer spring</td><td>smaller</td></tr>
</table></div>
<div class="note trap"><b>Fix in your notes</b>\(k\) is <b>not</b> "how easy it is to break". That's <b>strength</b>. \(k\) is force per unit extension.</div>""", sec=S))

    C.append(card("combo", S, "Springs in series and parallel", "Concept", r"""
<h2>Combining springs</h2>
<div class="tw"><table>
<tr><th></th><th>Series (end to end)</th><th>Parallel (side by side)</th></tr>
<tr><td class="k">Force in each</td><td>same \(F\) in both</td><td>shared: \(F/2\) each (identical)</td></tr>
<tr><td class="k">Extension</td><td>add: \(x = x_1 + x_2\)</td><td>same \(x\) for both</td></tr>
<tr><td class="k">Rule</td><td>\(\dfrac1{k_{\text{eff}}} = \dfrac1{k_1} + \dfrac1{k_2}\)</td><td>\(k_{\text{eff}} = k_1 + k_2\)</td></tr>
<tr><td class="k">Two identical</td><td>\(k_{\text{eff}} = \dfrac k2\) (less stiff)</td><td>\(k_{\text{eff}} = 2k\) (stiffer)</td></tr>
</table></div>
<div class="note link"><b>Careful wording</b>The individual springs don't change. It's the <b>arrangement</b> that is stiffer or less stiff.</div>
<div class="note tip"><b>Memory hook</b>Spring rules are the <b>opposite</b> of resistor rules: springs in series combine like resistors in parallel.</div>""", sec=S))

    C.append(card("ss", S, "Stress and strain", "Concept", r"""
<h2>Removing the size of the object</h2>
<div class="def"><div class="lab">Stress</div><p>The <b>force per unit cross-sectional area</b>: \(\sigma = \dfrac{F}{A}\), unit Pa (N m⁻²).</p></div>
<div class="def"><div class="lab">Strain</div><p>The <b>extension per unit original length</b>: \(\varepsilon = \dfrac{x}{L}\), no unit.</p></div>
<div class="def"><div class="lab">Young modulus</div><p>The <b>ratio of stress to strain</b>, within the limit of proportionality: \(E = \dfrac{\sigma}{\varepsilon}\), unit Pa.</p></div>
<div class="formula">\(E = \dfrac{F/A}{x/L} = \dfrac{FL}{Ax}\)</div>
<div class="note trap"><b>Fix in your notes</b>"Stress = how big a force can affect the object" scores 0. Say <b>force per unit cross-sectional area</b>.</div>
<div class="note trap"><b>Area of a wire</b>\(A = \dfrac{\pi d^2}{4}\). The micrometer gives the <b>diameter</b>; don't use it as the radius.</div>""", sec=S))

    C.append(card("intr", S, "k vs E: extrinsic vs intrinsic", "Concept", r"""
<h2>Why we bother with \(E\)</h2>
<div class="tw"><table>
<tr><th></th><th>Spring constant \(k\)</th><th>Young modulus \(E\)</th></tr>
<tr><td class="k">Type</td><td><b>extrinsic</b>: depends on the sample's dimensions</td><td><b>intrinsic</b>: depends only on the material</td></tr>
<tr><td class="k">Unit</td><td>N m⁻¹</td><td>Pa</td></tr>
<tr><td class="k">Same material, longer wire</td><td>smaller</td><td>unchanged</td></tr>
</table></div>
<div class="formula">\(k = \dfrac{EA}{L}\)</div>
<p>Dividing \(F\) by \(A\) and \(x\) by \(L\) cancels out the physical dimensions, leaving a property of the material alone. A cylinder is stiffer with a larger \(E\) or larger \(A\); a longer one is easier to stretch.</p>
<div class="note link"><b>Beyond the syllabus</b>Young modulus is one of three elastic moduli: <b>Young</b> (force perpendicular to the cross-section), <b>shear</b> (force parallel to a face) and <b>bulk</b> (pressure from all directions). Only Young is examined at AS.</div>""", sec=S))

    P = "Required practical"
    C.append(card("exp1", P, "Young modulus: horizontal wire", "Concept", r"""
<h2>Measuring \(E\) for a copper wire</h2>
<p class="lede">Wire clamped at one end, run over a pulley, masses on a hanger. A marker on the wire moves along a scale on the bench.</p>
<ol>
<li>Add a <b>small initial load</b> to make the wire taut and free from kinks.</li>
<li>Measure the original length \(L\) (clamp to marker) with a metre rule. Use a <b>long wire (over 2 m)</b> so the extension is big enough to measure.</li>
<li>Measure \(d\) with a <b>micrometer screw gauge</b> at several points and orientations; take the <b>mean</b> (the wire may not be uniform; averaging reduces random error).</li>
<li>Add masses one at a time; record the marker position each time. \(F = mg\).</li>
<li>Remove the loads and check the marker returns to zero: <b>elastic limit not exceeded</b>.</li>
<li>Plot \(\Delta L\) against \(F\); gradient \(G\); \(E = \dfrac{4L}{\pi d^2 G}\).</li>
</ol>
<div class="note tip"><b>Plot, don't substitute</b>Take at least 5–6 readings and use the gradient of a best-fit line. One reading can't show an anomaly; a line averages out random error.</div>""", sec=P))

    C.append(card("exp2", P, "Young modulus: two-wire method", "Concept", r"""
<h2>Vertical two-wire (Searle's) method</h2>
<div class="tw"><table>
<tr><td class="k">Test wire</td><td>copper, carries the slotted masses</td></tr>
<tr><td class="k">Reference wire</td><td>same material, hangs beside it, carries the <b>main scale</b></td></tr>
<tr><td class="k">Vernier scale</td><td>attached to the test wire, slides against the main scale</td></tr>
</table></div>
<div class="note link"><b>Why a reference wire</b>Anything affecting <b>both</b> wires cancels out: <b>temperature changes</b> (thermal expansion) and the beam/support <b>sagging</b> or the clamps slipping. Only the load's extension is measured.</div>
<div class="note link"><b>Why a vernier</b>The extension is <b>small</b> (fractions of a mm), so it needs a more <b>precise</b> reading than a metre rule gives.</div>
<ul>
<li>Small initial tension makes both wires taut.</li>
<li>Add masses <b>gradually</b> so the elastic limit isn't passed.</li>
<li>Original length over 2 m ⇒ larger \(\Delta L\) ⇒ smaller percentage uncertainty.</li>
</ul>""", sec=P))

    C.append(card("graph", P, "From the graph to E", "Concept", r"""
<h2>The graph method</h2>
""" + lvf() + r"""
<div class="def"><div class="lab">Derivation (as in Exercise Q4(c)(i))</div>
<p>\(E = \dfrac{FL}{A\,\Delta L} = \dfrac{F}{\Delta L}\cdot\dfrac{L}{\pi d^2/4}\)</p>
<p>\(G = \dfrac{\Delta L}{F}\Rightarrow\dfrac{F}{\Delta L} = \dfrac1G\)</p>
<p>\(E = \dfrac{4L}{\pi d^2 G}\)</p></div>
<div class="note trap"><b>Units</b>Graph read in mm: convert \(G\) to m N⁻¹ before substituting. 0.13 mm N⁻¹ = \(1.3\times10^{-4}\) m N⁻¹.</div>
<div class="note tip"><b>If F is on the y-axis</b>The gradient is \(k\) directly and \(E = kL/A\). Always check which way round the axes are.</div>""", sec=P))

    C.append(card("errors", P, "Errors and improvements", "Concept", r"""
<h2>Evaluating the experiment</h2>
<div class="tw"><table>
<tr><th>Source</th><th>Effect</th><th>Improvement</th></tr>
<tr><td class="k">\(d\) read too small (or \(d\) used as radius the wrong way)</td><td>\(A\) too small ⇒ \(E\) too <b>high</b></td><td>mean of several micrometer readings; check zero error</td></tr>
<tr><td class="k">Extension read too small (parallax, slipping clamp)</td><td>\(E\) too <b>high</b></td><td>vernier scale; read at eye level; reference wire</td></tr>
<tr><td class="k">Extension too small to read precisely</td><td>huge % uncertainty</td><td>longer, thinner wire</td></tr>
<tr><td class="k">Elastic limit exceeded</td><td>line curves; \(E\) not valid</td><td>check wire returns on unloading</td></tr>
<tr><td class="k">Temperature change</td><td>extra expansion counted as extension</td><td>reference wire</td></tr>
</table></div>
<div class="note link"><b>Your copper-wire lab</b>An extension of 0.2 cm on a metre rule (±0.1 cm) is about <b>±50%</b> uncertainty. That, plus a single reading, explains the 67% difference far more than parallax does.</div>""", sec=P))

    S2 = "6.2 Elastic and plastic"
    C.append(card("ep", S2, "Elastic vs plastic deformation", "Concept", r"""
<h2>Does it come back?</h2>
<div class="def"><div class="lab">Elastic deformation</div><p>The object <b>returns to its original shape and size</b> when the load is removed.</p></div>
<div class="def"><div class="lab">Plastic deformation</div><p>The object <b>does not return</b> to its original shape when the load is removed; it is permanently deformed.</p></div>
<div class="def"><div class="lab">Elastic limit</div><p>The maximum load beyond which the object will <b>not return</b> to its original length when the load is removed.</p></div>
""" + unload() + r"""
<div class="note tip"><b>Testing the elastic limit</b>Remove the extra load and check the pointer returns to its original position (no permanent extension).</div>""", sec=S2))

    C.append(card("mat", S2, "Ductile, brittle, polymeric", "Concept", r"""
<h2>Three types of material</h2>
""" + materials() + r"""
<div class="tw"><table>
<tr><td class="k">Ductile</td><td>shows <b>both</b> elastic and plastic behaviour; large plastic region; can be drawn into wires (copper, aluminium)</td></tr>
<tr><td class="k">Brittle</td><td>elastic up to breaking; <b>breaks suddenly</b> with little or no plastic deformation (glass, ceramics)</td></tr>
<tr><td class="k">Polymeric</td><td>elastic (recovers) but does <b>not obey Hooke's law</b>; curve steepens at large extension (rubber)</td></tr>
</table></div>
<div class="note link"><b>Mechanical properties</b><b>Strength</b> = force needed to break; <b>stiffness</b> = resistance to deformation (large \(k\) or \(E\)); <b>ductility</b> = can be drawn into wires; <b>brittleness</b> = snaps at the elastic limit.</div>""", sec=S2))

    C.append(card("energy", S2, "Elastic potential energy", "Concept", r"""
<h2>Energy stored = area under F–x</h2>
<p>Stretching needs work done against the <b>restoring force</b>; that work is stored as elastic (strain) potential energy: \(W = \Delta E\).</p>
""" + energy() + r"""
<div class="def"><div class="lab">Derivation</div>
<p>Force rises from 0 to \(F\), so average force \(= \dfrac{F}{2}\)</p>
<p>\(W = \dfrac F2\times x = \dfrac12Fx\)</p>
<p>With \(F = kx\): \(E_P = \dfrac12kx^2\)</p></div>
<div class="note trap"><b>Only within the limit of proportionality</b>\(\tfrac12kx^2\) needs a straight line. For a curve, <b>count squares</b> under it.</div>
<div class="note link"><b>Hard ball vs soft ball (Ex Q2c)</b>The soft ball deforms a lot and absorbs much of its KE as its <b>own</b> strain energy. The hard ball barely deforms, so <b>more energy goes to the glass</b> as strain energy ⇒ it breaks.</div>""", sec=S2))

    W = "Worked examples"
    C.append(card("we1", W, "Example 1: stress, strain, E", "Worked example", r"""
<h2>Example 1 · Steel wire</h2>
<p><b>Q:</b> A steel wire of length 2.50 m and diameter 0.50 mm extends by 2.5 mm under a load of 40 N. Calculate (a) the stress, (b) the strain, (c) the Young modulus, (d) the energy stored.</p>
<ol class="steps">
<li>""" + tg("C1") + r""" \(A = \dfrac{\pi d^2}{4} = \dfrac{\pi(0.50\times10^{-3})^2}{4} = 1.96\times10^{-7}\ \text{m}^2\)</li>
<li>""" + tg("A1") + r""" \(\sigma = \dfrac FA = \dfrac{40}{1.96\times10^{-7}} = 2.04\times10^{8}\ \text{Pa}\)</li>
<li>""" + tg("A1") + r""" \(\varepsilon = \dfrac xL = \dfrac{2.5\times10^{-3}}{2.50} = 1.0\times10^{-3}\) (no unit)</li>
<li>""" + tg("A1") + r""" \(E = \dfrac\sigma\varepsilon = \dfrac{2.04\times10^8}{1.0\times10^{-3}} = 2.0\times10^{11}\ \text{Pa}\)</li>
<li>""" + tg("C1", "A1") + r""" \(E_P = \tfrac12Fx = \tfrac12(40)(2.5\times10^{-3}) = 0.050\ \text{J}\)</li>
</ol>
<div class="note trap"><b>Where marks go</b>Forgetting mm → m, or using \(\pi d^2\) instead of \(\pi d^2/4\) (makes \(E\) 4× too small).</div>""", sec=W))

    C.append(card("we2", W, "Example 2: graph method", "Worked example", r"""
<h2>Example 2 · E from a ΔL–F graph</h2>
<p><b>Q:</b> A copper wire of original length 2.20 m and mean diameter 0.38 mm is loaded. A graph of extension ΔL against force F is a straight line through (0, 0) and (6.0 N, 0.92 mm). Determine the Young modulus.</p>
<ol class="steps">
<li>""" + tg("C1") + r""" \(G = \dfrac{\Delta L}{F} = \dfrac{0.92\times10^{-3}}{6.0} = 1.53\times10^{-4}\ \text{m N}^{-1}\)</li>
<li>""" + tg("C1") + r""" \(E = \dfrac{4L}{\pi d^2 G}\)</li>
<li>""" + tg("A1") + r""" \(E = \dfrac{4(2.20)}{\pi(0.38\times10^{-3})^2(1.53\times10^{-4})} = 1.3\times10^{11}\ \text{Pa}\)</li>
</ol>
<div class="note tip"><b>Sanity check</b>Copper ≈ \(1.1\)–\(1.3\times10^{11}\) Pa. An answer near \(10^{8}\) or \(10^{14}\) means a units slip.</div>""", sec=W))

    C.append(card("we3", W, "Example 3: springs and energy", "Worked example", r"""
<h2>Example 3 · One spring vs two</h2>
<p><b>Q:</b> Each spring has \(k = 200\) N m⁻¹. A 6.0 N load hangs from (a) one spring, (b) two in series, (c) two in parallel. Find the extension and the energy stored in each case.</p>
<ol class="steps">
<li>""" + tg("A1") + r""" One: \(x = \dfrac{6.0}{200} = 0.030\) m; \(E_P = \tfrac12(6.0)(0.030) = 0.090\) J</li>
<li>""" + tg("A1") + r""" Series: \(k_{\text{eff}} = 100\) N m⁻¹; \(x = 0.060\) m; \(E_P = \tfrac12(6.0)(0.060) = 0.18\) J</li>
<li>""" + tg("A1") + r""" Parallel: \(k_{\text{eff}} = 400\) N m⁻¹; \(x = 0.015\) m; \(E_P = \tfrac12(6.0)(0.015) = 0.045\) J</li>
</ol>
<div class="note link"><b>Pattern</b>Same load: the less stiff arrangement stretches more and stores <b>more</b> energy.</div>""", sec=W))

    C.append(card("we4", W, "Example 4: glass fibre (Ex Q2)", "Worked example", r"""
<h2>Example 4 · Brittle glass fibre</h2>
<p><b>Q:</b> A glass fibre, length 0.24 m, area \(7.9\times10^{-7}\) m², breaks at \(F = 60\) N with \(x = 3.0\times10^{-4}\) m (straight line throughout). Find (a) the ultimate tensile stress, (b) the Young modulus, (c) the energy stored just before it breaks.</p>
<ol class="steps">
<li>""" + tg("B1") + r""" Straight line to fracture ⇒ <b>brittle</b></li>
<li>""" + tg("C1", "A1") + r""" \(\sigma = \dfrac{60}{7.9\times10^{-7}} = 7.6\times10^{7}\ \text{Pa}\)</li>
<li>""" + tg("C1") + r""" \(\varepsilon = \dfrac{3.0\times10^{-4}}{0.24} = 1.25\times10^{-3}\)</li>
<li>""" + tg("A1") + r""" \(E = \dfrac{7.6\times10^7}{1.25\times10^{-3}} = 6.1\times10^{10}\ \text{Pa}\)</li>
<li>""" + tg("C1", "A1") + r""" \(E_P = \tfrac12(60)(3.0\times10^{-4}) = 9.0\times10^{-3}\ \text{J}\)</li>
</ol>""", sec=W))

    C.append(card("traps", "Mistakes", "Common mistakes", "Concept", r"""
<h2>Where marks are lost</h2>
<div class="note trap"><b>mm left in mm</b>Diameters and extensions are usually given in mm. Convert to m before using them.</div>
<div class="note trap"><b>Diameter as radius</b>\(A = \pi r^2 = \pi d^2/4\). Mixing them up is a factor of 4.</div>
<div class="note trap"><b>Strain with a unit</b>Strain is a ratio of two lengths: <b>no unit</b>.</div>
<div class="note trap"><b>\(Fx\) instead of \(\tfrac12Fx\)</b>The force builds up from zero, so use the area of the triangle.</div>
<div class="note trap"><b>\(\tfrac12kx^2\) on a curve</b>Only valid up to the limit of proportionality. Beyond it, use the area under the curve.</div>
<div class="note trap"><b>Limit of proportionality = elastic limit</b>Not the same point. Between them: curved but still elastic.</div>
<div class="note trap"><b>Vague definitions</b>"How easy it is to deform" won't score. Use <b>per unit</b> wording: force per unit extension, force per unit area, extension per unit length.</div>
<div class="note trap"><b>Axes the wrong way round</b>ΔL–F gradient = \(1/k\); F–ΔL gradient = \(k\). Check before you invert.</div>""", sec="Mistakes"))

    C.append(card("pr", "Practice", "Practice questions", "Practice", r"""
<h2>Practice · Deformation of solids</h2>
<div class="pq"><div class="qh"><span>Q1 · Extension of a wire</span><span class="mk">[3]</span></div>
<p class="qt">A copper wire (\(E = 1.2\times10^{11}\) Pa) of length 1.50 m and diameter 0.30 mm supports a 2.0 kg mass. Calculate the stress and the extension.</p>
<div class="ans"><b>Answer</b>\(A = 7.07\times10^{-8}\) m²; \(\sigma = 19.62/A = 2.8\times10^{8}\) Pa; \(x = \sigma L/E = 3.5\times10^{-3}\) m (3.5 mm).</div></div>
<div class="pq"><div class="qh"><span>Q2 · Spring energy</span><span class="mk">[3]</span></div>
<p class="qt">A spring extends 5.0 cm under 4.0 N (within the limit of proportionality). Find \(k\), then the energy stored when it is stretched by 3.0 cm.</p>
<div class="ans"><b>Answer</b>\(k = 4.0/0.050 = 80\) N m⁻¹; \(E_P = \tfrac12(80)(0.030)^2 = 0.036\) J.</div></div>
<div class="pq"><div class="qh"><span>Q3 · Two-wire experiment</span><span class="mk">[3]</span></div>
<p class="qt">In a two-wire experiment, a copper test wire of length 2.80 m and diameter 0.46 mm extends by 2.70 mm when 2.0 kg is added. Calculate \(E\) and state why a reference wire is used.</p>
<div class="ans"><b>Answer</b>\(A = 1.66\times10^{-7}\) m²; \(E = \dfrac{(19.62)(2.80)}{(1.66\times10^{-7})(2.70\times10^{-3})} = 1.2\times10^{11}\) Pa. Reference wire compensates for temperature changes and sagging of the support.</div></div>
<div class="pq"><div class="qh"><span>Q4 · Combinations</span><span class="mk">[4]</span></div>
<p class="qt">Springs of \(k_1 = 150\) N m⁻¹ and \(k_2 = 300\) N m⁻¹ support a 9.0 N load. Find the total extension when they are (a) in series, (b) in parallel (assume the load stays level).</p>
<div class="ans"><b>Answer</b>(a) \(1/k = 1/150 + 1/300 \Rightarrow k = 100\) N m⁻¹, \(x = 0.090\) m. (b) \(k = 450\) N m⁻¹, \(x = 0.020\) m.</div></div>
<div class="pq"><div class="qh"><span>Q5 · Uncertainty</span><span class="mk">[3]</span></div>
<p class="qt">\(d = 0.40 \pm 0.01\) mm, \(L = 2.000 \pm 0.002\) m, \(\Delta L = 0.80 \pm 0.02\) mm, \(F = 10.0 \pm 0.1\) N. Find the percentage uncertainty in \(E = 4FL/(\pi d^2\Delta L)\). Which measurement dominates?</p>
<div class="ans"><b>Answer</b>\(2(2.5\%) + 0.1\% + 2.5\% + 1.0\% = 8.6\%\). The diameter dominates (counted twice because it is squared).</div></div>
<div class="pq"><div class="qh"><span>Q6 · Explain</span><span class="mk">[3]</span></div>
<p class="qt">A copper wire is loaded beyond its elastic limit and then unloaded. Sketch the F–x graph and explain why the wire does not return to its original length.</p>
<div class="ans"><b>Answer</b>Straight line, curve to a maximum point, then a straight unloading line <b>parallel</b> to the original line reaching the x-axis at a positive extension. Beyond the elastic limit the deformation is plastic: layers of atoms have moved permanently, so a permanent extension remains.</div></div>""", sec="Practice"))

    C.append(card("sheet", "Summary", "Formula card", "Summary", r"""
<h2>Everything on one card</h2>
<div class="tw"><table>
<tr><td class="k">Hooke's law</td><td>\(F = kx\) (up to the limit of proportionality)</td></tr>
<tr><td class="k">Stress</td><td>\(\sigma = F/A\) · Pa</td></tr>
<tr><td class="k">Strain</td><td>\(\varepsilon = x/L\) · no unit</td></tr>
<tr><td class="k">Young modulus</td><td>\(E = \sigma/\varepsilon = FL/(Ax)\) · Pa</td></tr>
<tr><td class="k">Wire area</td><td>\(A = \pi d^2/4\)</td></tr>
<tr><td class="k">Link</td><td>\(k = EA/L\)</td></tr>
<tr><td class="k">Graph method</td><td>\(G = \Delta L/F\) ⇒ \(E = 4L/(\pi d^2G)\)</td></tr>
<tr><td class="k">Springs</td><td>series \(1/k = 1/k_1 + 1/k_2\); parallel \(k = k_1 + k_2\)</td></tr>
<tr><td class="k">Energy</td><td>\(E_P = \tfrac12Fx = \tfrac12kx^2\) = area under F–x</td></tr>
</table></div>
<div class="note tip"><b>Before you write the answer</b>mm → m? Diameter not radius? ½ in the energy? Inside the limit of proportionality?</div>""", sec="Summary"))
    return C


FLASH = [
    ["6.1 Definitions", "Define load.", "The force applied to an object that causes it to deform."],
    ["6.1 Definitions", "Define extension.", "The increase in length of an object when a tensile force is applied."],
    ["6.1 Definitions", "Define the limit of proportionality.", "The point beyond which extension is no longer proportional to the load."],
    ["6.1 Definitions", "State Hooke's law.", "Extension is directly proportional to the load applied, provided the limit of proportionality is not exceeded."],
    ["6.1 Definitions", "Define the spring constant.", "Force per unit extension, k = F/x, unit N m⁻¹."],
    ["6.1 Definitions", "Define stress.", "Force per unit cross-sectional area, σ = F/A, unit Pa."],
    ["6.1 Definitions", "Define strain.", "Extension per unit original length, ε = x/L, no unit."],
    ["6.1 Definitions", "Define the Young modulus.", "Ratio of stress to strain (within the limit of proportionality), E = σ/ε, unit Pa."],
    ["6.1 Concepts", "Tensile vs compressive force: effect on shape?", "Tensile: longer and thinner. Compressive: shorter and fatter."],
    ["6.1 Concepts", "Loaded horizontal beam: which surface is in tension?", "Bottom stretched (tension); top compressed; neutral axis unchanged."],
    ["6.1 Concepts", "Why is E intrinsic but k extrinsic?", "E depends only on the material; k also depends on length and area (k = EA/L)."],
    ["6.1 Concepts", "Two identical springs in series / parallel: k_eff?", "Series k/2 (less stiff); parallel 2k (stiffer)."],
    ["6.1 Concepts", "Four factors affecting a spring's k?", "Material (stronger bonding ⇒ larger), coil diameter (larger ⇒ smaller), wire thickness (thicker ⇒ larger), natural length (longer ⇒ smaller)."],
    ["Practical", "Why a small initial load on the wire?", "To make the wire taut and remove kinks."],
    ["Practical", "Why measure the diameter at several places?", "The wire may not be uniform; the mean reduces random error."],
    ["Practical", "Why use a long wire (over 2 m)?", "Larger extension ⇒ smaller percentage uncertainty."],
    ["Practical", "Purpose of the reference wire?", "Compensates for temperature changes and sagging of the support."],
    ["Practical", "Why a vernier scale?", "The extension is small, so a more precise reading is needed."],
    ["Practical", "ΔL against F: gradient G. Formula for E?", "E = 4L / (πd²G)."],
    ["Practical", "How to check the elastic limit was not exceeded?", "Remove the load and check the wire returns to its original length/pointer position."],
    ["6.2 Elastic & plastic", "Define elastic deformation.", "The object returns to its original shape and size when the load is removed."],
    ["6.2 Elastic & plastic", "Define plastic deformation.", "The object does not return to its original shape when the load is removed."],
    ["6.2 Elastic & plastic", "Define the elastic limit.", "The maximum load beyond which the object will not return to its original length when the load is removed."],
    ["6.2 Elastic & plastic", "Ductile: F–x shape and example?", "Straight, then long plastic region before breaking. Copper."],
    ["6.2 Elastic & plastic", "Brittle: F–x shape and example?", "Straight line then sudden fracture, no plastic region. Glass."],
    ["6.2 Elastic & plastic", "Polymeric: F–x shape and example?", "Elastic but not Hooke's law; curve steepens at large extension. Rubber."],
    ["6.2 Energy", "Elastic potential energy from an F–x graph?", "Area under the graph."],
    ["6.2 Energy", "E_P for a material obeying Hooke's law?", "E_P = ½Fx = ½kx²."],
    ["6.2 Energy", "Why ½Fx, not Fx?", "The force rises from 0 to F; the average force is F/2."],
    ["6.2 Energy", "Unloading after plastic deformation: shape of the unloading line?", "Straight, parallel to the loading line; it meets the x-axis at the permanent extension."],
]

QUIZ = [
    {"s": "6.1", "q": "Which is the correct definition of stress?",
     "o": ["How much a force can deform an object", "Force per unit cross-sectional area", "Extension per unit length", "Force per unit extension"], "c": 1,
     "e": "Stress = F/A. D is the spring constant; C is strain."},
    {"s": "6.1", "q": "A wire of diameter 0.20 mm carries 10 N. Stress?",
     "o": ["8.0 × 10⁷ Pa", "3.2 × 10⁸ Pa", "8.0 × 10⁸ Pa", "2.5 × 10⁸ Pa"], "c": 1,
     "e": "A = π(0.20×10⁻³)²/4 = 3.14×10⁻⁸ m², σ = 3.2×10⁸ Pa. A uses πd² instead of πd²/4."},
    {"s": "6.1", "q": "A wire is replaced by one of the same material, twice the length and twice the diameter. The new spring constant is:",
     "o": ["k/2", "k", "2k", "4k"], "c": 2,
     "e": "k = EA/L: A × 4, L × 2 ⇒ k × 2."},
    {"s": "6.1", "q": "Two identical springs, each k = 50 N m⁻¹, are in series. Extension under 10 N?",
     "o": ["0.05 m", "0.10 m", "0.20 m", "0.40 m"], "c": 3,
     "e": "k_eff = 25 N m⁻¹ ⇒ x = 10/25 = 0.40 m."},
    {"s": "Practical", "q": "In the ΔL–F graph method, the gradient G is in mm N⁻¹. What must you do before using E = 4L/(πd²G)?",
     "o": ["Nothing", "Multiply G by 10⁻³", "Multiply G by 10³", "Take 1/G"], "c": 1,
     "e": "mm → m: × 10⁻³. The formula already contains the 1/G."},
    {"s": "Practical", "q": "In Searle's two-wire method, the reference wire mainly corrects for:",
     "o": ["parallax error", "zero error on the micrometer", "temperature change and sag of the support", "the wire not being uniform"], "c": 2,
     "e": "Both wires expand/sag together, so only the test wire's load extension is read."},
    {"s": "6.2", "q": "A graph that is a straight line ending suddenly at fracture describes a:",
     "o": ["ductile material", "brittle material", "polymeric material", "plastic material"], "c": 1,
     "e": "Brittle: no plastic region (glass)."},
    {"s": "6.2", "q": "A spring with k = 400 N m⁻¹ is stretched 5.0 cm. Energy stored?",
     "o": ["0.50 J", "1.0 J", "10 J", "20 J"], "c": 0,
     "e": "½(400)(0.050)² = 0.50 J. B forgets the ½; D uses x in cm."},
    {"s": "6.2", "q": "Between the limit of proportionality and the elastic limit, a wire:",
     "o": ["obeys Hooke's law", "deforms plastically", "does not obey Hooke's law but returns to its original length", "breaks"], "c": 2,
     "e": "Curved region, still elastic."},
    {"s": "6.2", "q": "Energy stored in a stretched rubber band (curved F–x graph) is best found from:",
     "o": ["½kx²", "Fx", "the area under the F–x curve", "the gradient of the curve"], "c": 2,
     "e": "½kx² only works for a straight line; count squares under the curve."},
]


def write():
    meta = {"title": "Deformation of Solids Deck", "short": "Phys Ch6", "bar": "Physics · Deformation of solids",
            "code": "9702 · AS · Chapter 6", "key": "deck-9702-deformation"}
    cards = build()
    out = engine.render(meta, cards, FLASH, QUIZ, math=True)
    out = out.replace("<b>Paper 1 quiz</b>", "<b>Deformation quiz</b>").replace('<figure class="dg">', '<figure class="dg" style="max-width:520px">')
    (HERE / "deck-phys-deformation.html").write_text(out, encoding="utf8")
    print("phys deformation", len(out), "bytes,", len(cards), "cards,", len(FLASH), "flashcards,", len(QUIZ), "quiz")
    return cards


if __name__ == "__main__":
    write()
