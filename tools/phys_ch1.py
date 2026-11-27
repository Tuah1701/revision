"""9702 Physics · Chapter 1 Physical quantities and units.
Built from Tuah's Topical Notes (Units, 1.3 Dimensions, Scalars and Vectors, Errors and Uncertainties,
Cathode Ray Oscilloscope, Tools). Cambridge notation, answers to 2-3 s.f."""
import pathlib
import engine
from fixids import unique_markers
from engine import card
from phys_graphs import tg

HERE = pathlib.Path(__file__).parent


def build():
    C = []
    C.append(card("cover", "Start", "Physical quantities and units", "Cover", r"""
<p class="sec" style="margin:0">CAIE 9702 · AS Level · Chapter 1</p>
<p class="cover-k">SI</p>
<h1>Physical quantities and units</h1>
<p class="lede">SI units, prefixes, homogeneity, significant figures, scalars and vectors, errors and uncertainties, measuring instruments and the CRO. Built from your Chapter 1 topical notes (Puan Harlina's slides + your annotations).</p>
<div class="stat"><div><b>3</b>worked examples</div><div><b>5</b>practice Qs</div><div><b>25</b>flashcards</div></div>
<p><a href="index.html">Open Revision Hub</a></p>
<div class="swipehint">Swipe or use the arrows · tap ☰ for contents</div>""", sec="Start"))

    C.append(card("big", "Start", "The big picture", "Overview", r"""
<h2>The toolkit for every other chapter</h2>
<p class="lede">Chapter 1 is about <b>writing physics correctly</b>: the right unit, the right number of significant figures, the right direction, and an honest uncertainty.</p>
<div class="chain"><span>Base units</span><i>→</i><span>Derived units & homogeneity</span><i>→</i><span>Scalars vs vectors</span><i>→</i><span>Errors & uncertainties</span></div>
<div class="note tip"><b>Where it's examined</b>Paper 1 MCQs (units, prefixes, vectors, uncertainty) and the start of Paper 2. Paper 3 uses uncertainties and instrument readings in every question.</div>""", sec="Start"))

    S = "Units"
    C.append(card("base", S, "SI base units", "Concept", r"""
<h2>The six base quantities you need</h2>
<div class="tw"><table>
<tr><th>Base quantity</th><th>Unit</th><th>Symbol</th></tr>
<tr><td class="k">Mass</td><td>kilogram</td><td>kg</td></tr>
<tr><td class="k">Length</td><td>metre</td><td>m</td></tr>
<tr><td class="k">Time</td><td>second</td><td>s</td></tr>
<tr><td class="k">Current</td><td>ampere</td><td>A</td></tr>
<tr><td class="k">Temperature</td><td>kelvin</td><td>K</td></tr>
<tr><td class="k">Amount of substance</td><td>mole</td><td>mol</td></tr>
</table></div>
<p>The seventh SI base unit, the candela (luminous intensity), is <b>not</b> used in 9702.</p>
<div class="note trap"><b>Trap</b>The base unit of mass is the <b>kilogram</b>, not the gram. Charge (C) and voltage (V) are <b>derived</b>, not base.</div>""", sec=S))

    C.append(card("derived", S, "Derived units", "Concept", r"""
<h2>Building units from definitions</h2>
<p>Write the <b>defining equation</b>, then replace each quantity by its base units.</p>
<div class="tw"><table>
<tr><th>Quantity</th><th>Equation</th><th>Base units</th><th>Name</th></tr>
<tr><td class="k">Force</td><td>\(F = ma\)</td><td>kg m s⁻²</td><td>newton</td></tr>
<tr><td class="k">Work, energy</td><td>\(W = Fs\)</td><td>kg m² s⁻²</td><td>joule</td></tr>
<tr><td class="k">Power</td><td>\(P = W/t\)</td><td>kg m² s⁻³</td><td>watt</td></tr>
<tr><td class="k">Pressure</td><td>\(p = F/A\)</td><td>kg m⁻¹ s⁻²</td><td>pascal</td></tr>
<tr><td class="k">Charge</td><td>\(Q = It\)</td><td>A s</td><td>coulomb</td></tr>
<tr><td class="k">p.d.</td><td>\(V = W/Q\)</td><td>kg m² s⁻³ A⁻¹</td><td>volt</td></tr>
<tr><td class="k">Resistance</td><td>\(R = V/I\)</td><td>kg m² s⁻³ A⁻²</td><td>ohm</td></tr>
</table></div>
<div class="note tip"><b>Check via KE</b>\(\tfrac12mv^2\) ⇒ kg (m s⁻¹)² = kg m² s⁻², the same as the joule. Numbers like ½ have no unit.</div>""", sec=S))

    C.append(card("prefix", S, "Prefixes", "Concept", r"""
<h2>Prefixes from pico to tera</h2>
<div class="tw"><table>
<tr><th>Prefix</th><th>Symbol</th><th>Value</th><th>Prefix</th><th>Symbol</th><th>Value</th></tr>
<tr><td class="k">tera</td><td>T</td><td>10¹²</td><td class="k">deci</td><td>d</td><td>10⁻¹</td></tr>
<tr><td class="k">giga</td><td>G</td><td>10⁹</td><td class="k">centi</td><td>c</td><td>10⁻²</td></tr>
<tr><td class="k">mega</td><td>M</td><td>10⁶</td><td class="k">milli</td><td>m</td><td>10⁻³</td></tr>
<tr><td class="k">kilo</td><td>k</td><td>10³</td><td class="k">micro</td><td>μ</td><td>10⁻⁶</td></tr>
<tr><td></td><td></td><td></td><td class="k">nano</td><td>n</td><td>10⁻⁹</td></tr>
<tr><td></td><td></td><td></td><td class="k">pico</td><td>p</td><td>10⁻¹²</td></tr>
</table></div>
<div class="note link"><b>Your mnemonic</b><i>Dad Has Kept Many Good Things, Packed Every Zippy Yo-yo</i>: deca, hecto, kilo, mega, giga, tera, peta, exa, zetta, yotta.</div>
<div class="note trap"><b>Squared prefixes</b>1 cm² = (10⁻²)² m² = 10⁻⁴ m². 1 mm³ = 10⁻⁹ m³. Square/cube the prefix too.</div>""", sec=S))

    C.append(card("homog", S, "Homogeneity", "Concept", r"""
<h2>Checking an equation with base units</h2>
<div class="def"><div class="lab">Homogeneous equation</div><p>An equation in which <b>every term has the same base units</b>.</p></div>
<p>Method: write the base units of <b>each term</b> separately. Terms added or subtracted must match; both sides must match.</p>
<div class="tw"><table>
<tr><th>Quantity</th><th>Dimension</th><th>Unit</th></tr>
<tr><td class="k">velocity</td><td>[L T⁻¹]</td><td>m s⁻¹</td></tr>
<tr><td class="k">acceleration</td><td>[L T⁻²]</td><td>m s⁻²</td></tr>
<tr><td class="k">force</td><td>[M L T⁻²]</td><td>kg m s⁻²</td></tr>
</table></div>
<div class="note trap"><b>Homogeneous ≠ correct</b>\(s = ut + at^2\) is homogeneous but wrong (the ½ is missing). Base units can't check pure numbers.</div>
<div class="note tip"><b>Spotting a wrong one</b>From your notes: \(s = ut + mg\) fails, because \(mg\) is kg m s⁻², not m.</div>""", sec=S))

    C.append(card("sf", S, "Significant figures", "Concept", r"""
<h2>Counting significant figures</h2>
<div class="tw"><table>
<tr><th>Number</th><th>s.f.</th><th>Why</th></tr>
<tr><td class="k">456</td><td>3</td><td>all non-zero digits count</td></tr>
<tr><td class="k">10204</td><td>5</td><td>zeros between digits count</td></tr>
<tr><td class="k">0.00546</td><td>3</td><td>leading zeros don't count</td></tr>
<tr><td class="k">1.30</td><td>3</td><td>trailing zeros after the point count</td></tr>
<tr><td class="k">1300</td><td>2, 3 or 4</td><td>ambiguous: write 1.30 × 10³ to show 3</td></tr>
</table></div>
<div class="note tip"><b>Rule for answers</b>Give the final answer to the <b>same s.f. as the least precise data</b> (usually 2 or 3). Never round in the middle of a calculation.</div>""", sec=S))

    V = "Scalars and vectors"
    C.append(card("sv", V, "Scalars vs vectors", "Concept", r"""
<h2>Magnitude only, or magnitude and direction?</h2>
<div class="def"><div class="lab">Scalar</div><p>A quantity with <b>magnitude only</b>.</p></div>
<div class="def"><div class="lab">Vector</div><p>A quantity with <b>magnitude and direction</b>.</p></div>
<div class="tw"><table>
<tr><th>Scalars</th><th>Vectors</th></tr>
<tr><td>distance, speed, mass, time, temperature, energy, work, power, density, pressure, volume</td><td>displacement, velocity, acceleration, force, weight, momentum, torque, electric field</td></tr>
</table></div>
<div class="note trap"><b>Work and energy are scalars</b>Work can be <b>negative</b> (force opposite to displacement, \(\theta = 180°\)), but that sign is not a direction.</div>
<div class="note trap"><b>Pressure is a scalar</b>It acts in all directions; the <b>force</b> it produces on a surface is the vector.</div>""", sec=V))

    C.append(card("add", V, "Adding vectors", "Concept", r"""
<h2>Two methods for a resultant</h2>
<div class="tw"><table>
<tr><th>Graphical (scale drawing)</th><th>Calculation</th></tr>
<tr><td>Draw vectors <b>tip to tail</b> to scale; resultant runs from the first tail to the last tip. Measure its length and angle.</td><td>Perpendicular: Pythagoras + \(\tan\). Any angle: resolve both into components, add components, recombine.</td></tr>
</table></div>
<div class="def"><div class="lab">Resolving</div><p>A vector \(F\) at angle \(\theta\) to the x-axis: \(F_x = F\cos\theta\), \(F_y = F\sin\theta\).</p></div>
<div class="note link"><b>Subtracting</b>\(\Delta\vec v = \vec v - \vec u = \vec v + (-\vec u)\): reverse \(\vec u\), then add tip to tail.</div>
<div class="note tip"><b>Order doesn't matter</b>\(V_1 + V_2 + V_3\) in any order gives the same resultant (your notes check this).</div>""", sec=V))

    E = "Errors and uncertainties"
    C.append(card("errors", E, "Random and systematic errors", "Concept", r"""
<h2>Two kinds of error</h2>
<div class="tw"><table>
<tr><th></th><th>Random error</th><th>Systematic error</th></tr>
<tr><td class="k">Effect</td><td>readings <b>scattered</b> about the true value, above and below</td><td>all readings shifted by the <b>same amount</b> (or same proportion) in one direction</td></tr>
<tr><td class="k">Examples</td><td>reaction time, fluctuating readings, judging a scale between marks</td><td>zero error, wrongly calibrated meter, parallax always from the same side</td></tr>
<tr><td class="k">Reduce by</td><td><b>repeating and averaging</b>, plotting a graph</td><td>correcting the zero error, recalibrating; <b>averaging does not help</b></td></tr>
</table></div>
<div class="note trap"><b>Fix in your notes</b>Random errors aren't just "human error", and averaging <b>reduces</b> them, it doesn't <b>eliminate</b> them.</div>""", sec=E))

    C.append(card("pa", E, "Precision vs accuracy", "Concept", r"""
<h2>Two words examiners test every year</h2>
<div class="def"><div class="lab">Accuracy</div><p>How close a measurement (or the mean) is to the <b>true value</b>. Spoilt by <b>systematic</b> error.</p></div>
<div class="def"><div class="lab">Precision</div><p>How close repeated measurements are to <b>each other</b> (small spread). Spoilt by <b>random</b> error.</p></div>
<div class="note trap"><b>Fix in your June 16/23 answer</b>You wrote precision = "the size of the smallest division". That's the instrument's <b>resolution</b>. Precision is the spread of repeated readings about their mean.</div>
<div class="note tip"><b>Mark-scheme wording (June 16/23 Q2)</b>Systematic: readings <b>all larger (or all smaller)</b> than the true value by the same amount. Random: readings <b>scattered about</b> the true value.</div>""", sec=E))

    C.append(card("instr", E, "Instruments and readings", "Concept", r"""
<h2>Read to the instrument's resolution</h2>
<div class="tw"><table>
<tr><th>Instrument</th><th>Smallest reading</th><th>Range</th><th>Example</th></tr>
<tr><td class="k">Metre rule</td><td>1 mm</td><td>up to 1 m</td><td>0.828 m</td></tr>
<tr><td class="k">Vernier calipers</td><td>0.01 cm (0.1 mm)</td><td>up to ~15 cm</td><td>2.53 cm</td></tr>
<tr><td class="k">Micrometer screw gauge</td><td>0.01 mm</td><td>up to ~25 mm</td><td>1.57 mm</td></tr>
<tr><td class="k">Electronic balance</td><td>0.001 g</td><td></td><td>0.450 g</td></tr>
<tr><td class="k">Protractor</td><td>1°</td><td></td><td>39°</td></tr>
</table></div>
<div class="note tip"><b>Recording</b>Keep trailing zeros that the instrument shows: 0.450 g, not 0.45 g. Check micrometers and calipers for <b>zero error</b> before measuring.</div>""", sec=E))

    C.append(card("comb", E, "Combining uncertainties", "Concept", r"""
<h2>The three rules</h2>
<div class="tw"><table>
<tr><th>Operation</th><th>Rule</th></tr>
<tr><td class="k">\(Q = A \pm B\)</td><td><b>add absolute</b> uncertainties: \(\Delta Q = \Delta A + \Delta B\)</td></tr>
<tr><td class="k">\(Q = AB\) or \(A/B\)</td><td><b>add fractional</b> (or %) uncertainties: \(\dfrac{\Delta Q}{Q} = \dfrac{\Delta A}{A} + \dfrac{\Delta B}{B}\)</td></tr>
<tr><td class="k">\(Q = A^n\)</td><td>multiply the fractional uncertainty by \(n\): \(\dfrac{\Delta Q}{Q} = n\dfrac{\Delta A}{A}\)</td></tr>
</table></div>
<div class="note trap"><b>Never subtract uncertainties</b>Even for \(Q = A/B\) or \(Q = A - B\), uncertainties always <b>add</b>.</div>
<div class="note tip"><b>Final answer</b>Absolute uncertainty to <b>1 s.f.</b> (2 if it starts with 1); the value rounded to the <b>same decimal place</b> as the uncertainty.</div>""", sec=E))

    C.append(card("cro", E, "Cathode-ray oscilloscope", "Concept", r"""
<h2>Reading a CRO trace</h2>
<div class="tw"><table>
<tr><td class="k">Electron gun</td><td>filament + cathode emit electrons; anodes accelerate and focus them into a beam</td></tr>
<tr><td class="k">Y-plates</td><td>deflect the beam <b>vertically</b> by the input p.d.</td></tr>
<tr><td class="k">X-plates</td><td>sweep the beam <b>horizontally</b> at constant speed using a <b>sawtooth</b> p.d. (the time-base)</td></tr>
<tr><td class="k">Screen</td><td>fluorescent coating glows where the beam hits</td></tr>
</table></div>
<div class="formula">voltage = divisions × Y-gain (V div⁻¹) · time = divisions × time-base (s div⁻¹)</div>
<p>\(f = 1/T\). Measure peak-to-peak and halve it for the amplitude, to reduce reading error.</p>
<div class="note tip"><b>Dual channel</b>Two traces at once, so two signals can be compared (e.g. phase difference).</div>""", sec=E))

    W = "Worked examples"
    C.append(card("we1", W, "Example 1: homogeneity", "Worked example", r"""
<h2>Example 1 · Is \(s = ut + \tfrac12at^2\) homogeneous?</h2>
<p><b>Q:</b> Show that the equation \(s = ut + \tfrac12 at^2\) is homogeneous.</p>
<ol class="steps">
<li>""" + tg("B1") + r""" LHS: \(s\) has units m</li>
<li>""" + tg("B1") + r""" \(ut\): (m s⁻¹)(s) = m</li>
<li>""" + tg("B1") + r""" \(\tfrac12 at^2\): (m s⁻²)(s²) = m (½ has no unit)</li>
<li>""" + tg("A1") + r""" Every term is m, so the equation is homogeneous</li>
</ol>
<div class="note trap"><b>Where marks go</b>Show each term separately. "Both sides are m" without working the RHS terms out scores 0.</div>""", sec=W))

    C.append(card("we2", W, "Example 2: density ± uncertainty", "Worked example", r"""
<h2>Example 2 · June 16/21 Q1(b)</h2>
<p><b>Q:</b> A wire has \(d = 0.38 \pm 0.01\) mm, \(L = 25.0 \pm 0.1\) cm and \(M = 0.225 \pm 0.001\) g. Given \(V = \pi d^2L/4\), calculate the density with its absolute uncertainty.</p>
<ol class="steps">
<li>""" + tg("C1") + r""" \(V = \dfrac{\pi(0.38\times10^{-3})^2(0.250)}{4} = 2.84\times10^{-8}\ \text{m}^3\)</li>
<li>""" + tg("A1") + r""" \(\rho = \dfrac{0.225\times10^{-3}}{2.84\times10^{-8}} = 7.94\times10^{3}\ \text{kg m}^{-3}\)</li>
<li>""" + tg("C1") + r""" \(\dfrac{\Delta\rho}{\rho} = 2\left(\dfrac{0.01}{0.38}\right) + \dfrac{0.1}{25.0} + \dfrac{0.001}{0.225} = 0.061\) (6.1%)</li>
<li>""" + tg("A1") + r""" \(\Delta\rho = 0.061 \times 7940 \approx 500\), so \(\rho = (7.9 \pm 0.5)\times10^{3}\ \text{kg m}^{-3}\)</li>
</ol>
<div class="note trap"><b>Where marks go</b>\(d\) is squared, so its % counts <b>twice</b>. Convert mm and g to m and kg before computing \(\rho\) (your notes stopped at mixed units).</div>""", sec=W))

    C.append(card("we3", W, "Example 3: resultant force", "Worked example", r"""
<h2>Example 3 · Two forces at 40°</h2>
<p><b>Q:</b> Forces of 8.0 N and 6.0 N act from the same point with 40° between them. Find the resultant.</p>
<ol class="steps">
<li>""" + tg("M1") + r""" Components along the 8.0 N: \(R_x = 8.0 + 6.0\cos40° = 12.6\) N; \(R_y = 6.0\sin40° = 3.86\) N</li>
<li>""" + tg("A1") + r""" \(R = \sqrt{12.6^2 + 3.86^2} = 13.2\) N</li>
<li>""" + tg("A1") + r""" \(\tan\phi = 3.86/12.6 \Rightarrow \phi = 17°\) from the 8.0 N force</li>
</ol>
<div class="note link"><b>Check by scale drawing</b>Your parallelogram gave 13.2 N, which matches. Scale drawings get full marks only if drawn carefully with a stated scale.</div>""", sec=W))

    C.append(card("traps", "Mistakes", "Common mistakes", "Concept", r"""
<h2>Where marks are lost</h2>
<div class="note trap"><b>Gram as base unit</b>Base unit of mass is the kilogram.</div>
<div class="note trap"><b>Prefix not squared</b>1 cm² = 10⁻⁴ m², not 10⁻² m².</div>
<div class="note trap"><b>"Homogeneous so it's correct"</b>Homogeneity can't detect a missing ½ or 2.</div>
<div class="note trap"><b>Precision = resolution</b>Precision is the spread of repeated readings; resolution is the smallest division.</div>
<div class="note trap"><b>Subtracting uncertainties</b>Always add, whatever the operation.</div>
<div class="note trap"><b>Uncertainty to 3 s.f.</b>Uncertainty to 1 s.f.; round the value to match its decimal place.</div>
<div class="note trap"><b>Energy as a vector</b>Energy, work, power and pressure are scalars.</div>""", sec="Mistakes"))

    C.append(card("pr", "Practice", "Practice questions", "Practice", r"""
<h2>Practice · Chapter 1</h2>
<div class="pq"><div class="qh"><span>Q1 · Base units</span><span class="mk">[2]</span></div>
<p class="qt">Use \(V = W/Q\) to express the volt in SI base units.</p>
<div class="ans"><b>Answer</b>\(W\): kg m² s⁻²; \(Q = It\): A s. So V = kg m² s⁻² / (A s) = kg m² s⁻³ A⁻¹.</div></div>
<div class="pq"><div class="qh"><span>Q2 · Uncertainty</span><span class="mk">[3]</span></div>
<p class="qt">\(I = 2.0 \pm 0.1\) A and \(R = 10.0 \pm 0.2\ \Omega\). Find \(P = I^2R\) with its absolute uncertainty.</p>
<div class="ans"><b>Answer</b>\(P = 40\) W. % = 2(5%) + 2% = 12%. \(\Delta P = 4.8 \approx 5\) W, so \(P = 40 \pm 5\) W.</div></div>
<div class="pq"><div class="qh"><span>Q3 · Change in velocity</span><span class="mk">[2]</span></div>
<p class="qt">A car's velocity changes from 10 m s⁻¹ east to 10 m s⁻¹ north. Find the change in velocity.</p>
<div class="ans"><b>Answer</b>\(\Delta\vec v = \vec v - \vec u\): add 10 north to 10 <b>west</b>. Magnitude \(\sqrt{200} = 14\) m s⁻¹, direction north-west (45° west of north).</div></div>
<div class="pq"><div class="qh"><span>Q4 · CRO</span><span class="mk">[3]</span></div>
<p class="qt">A sine wave on a CRO has peak-to-peak height 6.0 div with Y-gain 0.50 V div⁻¹. One cycle covers 5.0 div with time-base 2.0 ms div⁻¹. Find the amplitude and frequency.</p>
<div class="ans"><b>Answer</b>Amplitude = ½ × 6.0 × 0.50 = 1.5 V. \(T = 5.0 \times 2.0 = 10\) ms, so \(f = 100\) Hz.</div></div>
<div class="pq"><div class="qh"><span>Q5 · Errors</span><span class="mk">[2]</span></div>
<p class="qt">A student's micrometer reads +0.03 mm with the jaws closed. State the type of error and its effect on the diameters measured, and how to correct it.</p>
<div class="ans"><b>Answer</b>Systematic (zero) error: every reading is 0.03 mm too large. Subtract 0.03 mm from each reading. Averaging would not remove it.</div></div>""", sec="Practice"))

    C.append(card("sheet", "Summary", "Summary card", "Summary", r"""
<h2>Everything on one card</h2>
<div class="tw"><table>
<tr><td class="k">Base units</td><td>kg, m, s, A, K, mol</td></tr>
<tr><td class="k">Homogeneous</td><td>every term has the same base units</td></tr>
<tr><td class="k">Resolving</td><td>\(F_x = F\cos\theta\), \(F_y = F\sin\theta\)</td></tr>
<tr><td class="k">Random error</td><td>scatter about true value; reduce by averaging</td></tr>
<tr><td class="k">Systematic error</td><td>constant shift; correct zero/calibration</td></tr>
<tr><td class="k">Accuracy</td><td>closeness to the true value</td></tr>
<tr><td class="k">Precision</td><td>closeness of repeated readings to each other</td></tr>
<tr><td class="k">± or −</td><td>add absolute uncertainties</td></tr>
<tr><td class="k">× or ÷</td><td>add fractional uncertainties</td></tr>
<tr><td class="k">Power \(n\)</td><td>\(n\) × fractional uncertainty</td></tr>
<tr><td class="k">CRO</td><td>V = div × Y-gain; t = div × time-base; \(f = 1/T\)</td></tr>
</table></div>""", sec="Summary"))
    return C


FLASH = [
    ["Units", "Six SI base quantities used in 9702?", "Mass (kg), length (m), time (s), current (A), temperature (K), amount of substance (mol)."],
    ["Units", "Force in base units?", "kg m s⁻²."],
    ["Units", "Energy (joule) in base units?", "kg m² s⁻²."],
    ["Units", "Power (watt) in base units?", "kg m² s⁻³."],
    ["Units", "Pressure (pascal) in base units?", "kg m⁻¹ s⁻²."],
    ["Units", "Volt in base units?", "kg m² s⁻³ A⁻¹."],
    ["Units", "Ohm in base units?", "kg m² s⁻³ A⁻²."],
    ["Units", "What is a homogeneous equation?", "One in which every term has the same base units."],
    ["Units", "Why can a homogeneous equation still be wrong?", "Base units can't check pure numbers (e.g. a missing ½)."],
    ["Units", "1 cm² in m²? 1 mm³ in m³?", "10⁻⁴ m²; 10⁻⁹ m³."],
    ["Units", "Values of nano, micro, mega, giga?", "10⁻⁹, 10⁻⁶, 10⁶, 10⁹."],
    ["Units", "Significant figures in 0.00546 and 1.30?", "3 and 3."],
    ["Vectors", "Define a scalar and a vector.", "Scalar: magnitude only. Vector: magnitude and direction."],
    ["Vectors", "Is work a vector? Can it be negative?", "Scalar. Yes, negative when the force opposes the displacement."],
    ["Vectors", "Components of F at θ to the horizontal?", "Horizontal F cos θ, vertical F sin θ."],
    ["Vectors", "How do you subtract vectors?", "Reverse the second vector and add tip to tail: v − u = v + (−u)."],
    ["Errors", "Random error: effect and how to reduce?", "Readings scattered about the true value; repeat and average."],
    ["Errors", "Systematic error: effect and how to reduce?", "All readings shifted by the same amount; correct zero error/recalibrate."],
    ["Errors", "Define accuracy.", "How close a measurement is to the true value."],
    ["Errors", "Define precision.", "How close repeated measurements are to each other."],
    ["Errors", "Uncertainty rule for Q = A × B or A/B?", "Add the fractional (percentage) uncertainties."],
    ["Errors", "Uncertainty rule for Q = A − B?", "Add the absolute uncertainties."],
    ["Errors", "Uncertainty in Q = A³?", "3 × fractional uncertainty in A."],
    ["Errors", "Resolution of a micrometer and vernier calipers?", "Micrometer 0.01 mm; vernier 0.01 cm (0.1 mm)."],
    ["CRO", "What do the time-base and Y-gain set?", "Time-base: s per horizontal division. Y-gain: V per vertical division."],
]

QUIZ = [
    {"s": "Units", "q": "Which is an SI base unit?", "o": ["newton", "coulomb", "ampere", "volt"], "c": 2,
     "e": "Ampere is base; the others are derived."},
    {"s": "Units", "q": "The base units of power are:", "o": ["kg m² s⁻²", "kg m² s⁻³", "kg m s⁻²", "kg m s⁻³"], "c": 1,
     "e": "W = J s⁻¹ = kg m² s⁻² ÷ s."},
    {"s": "Units", "q": "4.5 mm² in m² is:", "o": ["4.5 × 10⁻³", "4.5 × 10⁻⁴", "4.5 × 10⁻⁶", "4.5 × 10⁻⁹"], "c": 2,
     "e": "(10⁻³)² = 10⁻⁶."},
    {"s": "Vectors", "q": "Which list contains only vectors?", "o": ["speed, force, mass", "weight, momentum, acceleration", "energy, velocity, displacement", "pressure, torque, weight"], "c": 1,
     "e": "Speed, mass, energy and pressure are scalars."},
    {"s": "Vectors", "q": "A 10 N force acts at 30° above the horizontal. Its vertical component is:", "o": ["5.0 N", "8.7 N", "10 N", "0.50 N"], "c": 0,
     "e": "10 sin 30° = 5.0 N."},
    {"s": "Errors", "q": "Readings that are close together but far from the true value are:", "o": ["accurate and precise", "precise but not accurate", "accurate but not precise", "neither"], "c": 1,
     "e": "Small spread = precise; systematic shift = inaccurate."},
    {"s": "Errors", "q": "Uncertainty in L is 2% and in T is 1%. Uncertainty in g = 4π²L/T²?", "o": ["1%", "3%", "4%", "5%"], "c": 2,
     "e": "2% + 2(1%) = 4%."},
    {"s": "Errors", "q": "Which reduces a random error?", "o": ["correcting the zero error", "repeating and averaging", "using a thinner wire", "recalibrating the meter"], "c": 1,
     "e": "Averaging reduces random scatter; it can't fix systematic errors."},
]


def write():
    meta = {"title": "Physical Quantities and Units Deck", "short": "Phys Ch1", "bar": "Physics · Quantities & units",
            "code": "9702 · AS · Chapter 1", "key": "deck-9702-ch1"}
    cards = build()
    out = engine.render(meta, cards, FLASH, QUIZ, math=True).replace("<b>Paper 1 quiz</b>", "<b>Chapter 1 quiz</b>")
    (HERE / "deck-phys-ch1.html").write_text(unique_markers(out), encoding="utf8")
    print("phys ch1", len(out), "bytes,", len(cards), "cards,", len(FLASH), "flashcards,", len(QUIZ), "quiz")
    return cards


if __name__ == "__main__":
    write()
