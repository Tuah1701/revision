"""9702 Physics · Definitions & comparisons deck, built from Muhammad Afiq bin Abdul Wahid's
"Physics Definition & Comparison by Chapters" sheet. Definitions are kept in the sheet's wording
(obvious typos fixed); blanks in the sheet are filled and labelled 'added'."""
import html, pathlib
import engine
from engine import card

HERE = pathlib.Path(__file__).parent
e = html.escape

# (chapter number, chapter title, [(term, definition, added?)])
CHAPTERS = [
    (1, "Physical quantities & units", [
        ("Base quantities", "Fundamental units that are not consist of combination of any units"),
        ("Derived quantities", "Unit that are expressed in terms of base units"),
        ("Vector quantity", "Quantity that has both magnitude and direction"),
        ("Scalar quantity", "Quantity that has only magnitude but no direction"),
    ]),
    (2, "Measurement techniques", [
        ("Systematic error", "Readings are consistently being either above or below true value"),
        ("Random error", "Readings are scattered around true value"),
        ("Accuracy", "The degree to which the values obtained approach true value and is influenced by size of systematic error"),
        ("Precision", "How close repeated readings are to each other; determined by the size of random error", "corrected"),
        ("Uncertainty", "The total range of values within which the measurement is likely to lie"),
    ]),
    (3, "Kinematics", [
        ("Distance", "The total length of path covered by a moving object irrespective of the direction of the motion"),
        ("Displacement", "The shortest distance an object travels from a reference point in a specified direction"),
        ("Velocity", "The rate of change of displacement"),
        ("Speed", "The rate of change of distance"),
        ("Acceleration", "The rate of change of velocity"),
    ]),
    (4, "Dynamics", [
        ("Newton's First Law", "Every body continues in a state of rest, or with uniform velocity, unless acted on by an external force."),
        ("Newton's Second Law", "For a body of a constant mass, the resultant force is proportional to the rate of change of its momentum."),
        ("Newton's Third Law", "When two bodies interact, the forces they exert on each other are equal in magnitude and opposite in direction."),
        ("Conservation of Momentum", "In any closed system, the total momentum of the system remains constant given there is no external force."),
        ("Force", "Rate of change of momentum"),
        ("Momentum", "The product of its mass and its velocity"),
        ("Weight", "The force of gravity on a mass of object"),
        ("Elastic collision", "Total kinetic energy before = after collision"),
    ]),
    (5, "Forces, density and pressure", [
        ("Torque", "The product of one of the forces and the perpendicular distance between the lines of action of the forces", "corrected"),
        ("Centre of gravity", "The point at which the whole weight of a body seems to act."),
        ("Couple", "A pair of equal parallel forces that are opposite in direction in which the line do not coincide."),
        ("Moment", "The product of the force and the perpendicular distance between the line of the action of the force from the pivot"),
        ("The principle of moments", "For a body to be in rotational equilibrium, the sum of the clockwise moment at any point must be = to the sum of the anti clockwise moment about the same point"),
        ("Density", "Mass per unit volume"),
        ("Pressure", "Force acting perpendicularly per unit cross sectional area"),
    ]),
    (6, "Work, energy and power", [
        ("Work", "The product of force and the distance moved in the direction of the force"),
        ("Principle of Conservation of Energy", "Energy can neither be created nor destroyed. It can only be converted from one form to another."),
        ("Gravitational Potential Energy", "Energy stored due to position of a mass in a gravitational field."),
        ("Kinetic Energy", "Energy stored by a mass due to its motion."),
        ("Elastic Potential Energy", "Energy stored due to deformation of the object; by either compressing or stretching."),
        ("Electrostatic potential energy", "Energy stored due to position of a charge in an electric field"),
        ("Power", "Rate of doing work"),
        ("Efficiency", "Useful energy output per total energy input"),
    ]),
    (9, "Deformation of solids", [
        ("Hooke's Law", "Applied force is directly proportional to the extension produced provided that the limit of proportionality is not exceeded.", "corrected"),
        ("Plastic Deformation", "The ability of object to change its shape and hence does not return to its original shape after applied force is removed"),
        ("Elastic Deformation", "The ability of object to change its shape and hence return to its original shape after applied force is removed"),
        ("Stress", "Force per unit original cross sectional area"),
        ("Strain", "The ratio of extension to its original length"),
        ("Young's Modulus", "The ratio of stress over strain given that limit of proportionality is not exceeded."),
        ("Elastic Limit", "The point beyond which material does not return to its original shape when force applied is removed."),
        ("Ultimate tensile stress", "Maximum force per unit original cross sectional area that an object can support before it breaks"),
    ]),
    (14, "Waves", [
        ("Frequency", "The number of oscillation per unit time of the source"),
        ("Transverse wave", "Wave in which the vibration of the particles on the wave is normal to the direction of the propagation of the wave's energy."),
        ("Longitudinal wave", "Wave in which the vibration of the particles on the wave is parallel to the direction of the propagation of the wave's energy."),
        ("Polarisation", "The condition of waves in which particles are made to vibrate in one direction on a single plane."),
        ("Doppler Effect", "The change in frequency observed due to the relative motion between wave source and observer."),
        ("Displacement", "The distance of a point on wave from its undisturbed or rest position"),
        ("Amplitude", "The max distance of a point on wave from its undisturbed or rest position"),
        ("Wavelength", "The shortest distance between two successive points that are in phase"),
        ("Period", "The time for one complete oscillation to occur"),
        ("Intensity", "The rate of energy transmitted per unit perpendicular area to the direction of wave propagation"),
        ("Phase difference", "The fraction of a cycle (expressed as an angle, in degrees or radians) by which one oscillation leads or lags another.", True),
        ("Speed", "The distance travelled by the wave (wavefront) per unit time.", True),
    ]),
    (15, "Superposition", [
        ("Principle of Superposition of Waves", "When two or more waves meet at a point, the resultant displacement is equal to the sum of the individual displacement of the waves."),
        ("Coherent Source", "Waves of same frequency and constant phase difference."),
        ("Coherence", "Two or more waves that originates from a source which have constant phase difference and same frequency and wavelength."),
        ("Diffraction", "The spreading or bending of waves when passing through a gap or rounding an obstacle"),
        ("Node", "The point with no displacement as a result of destructive interference"),
        ("Antinode", "The point with maximum displacement as a result of constructive interference."),
        ("Constructive interference", "When two waves with maximum displacement meet, resulting in a wave with amplitude of sum of the amplitudes of the individual waves"),
        ("Destructive interference", "When two waves with maximum and minimum displacement meet, resulting in a wave with zero displacement."),
        ("Condition of interference", "Same types of waves · meet at a point · same direction of polarisation"),
    ]),
    (17, "Electric fields", [
        ("Electric field", "The region of space where a stationary charge experiences force"),
        ("Electric field strength", "The force per unit positive charge at that point"),
        ("Direction of electric field", "Direction in which a positive charge would move if it is free to do so."),
    ]),
    (19, "Current of electricity", [
        ("Electric Current", "The rate of flow of electric charge"),
        ("Ohm's Law", "The current in a conductor is directly proportional to the potential difference across its ends, provided its temperature and other physical conditions remain constant."),
        ("Resistance", "The ratio of the potential difference across a conductor to the current flowing through it"),
        ("Potential difference", "Energy transferred from electrical energy to other forms of energy per unit charge from one point to another point."),
        ("Electromotive Force", "Energy transferred from other forms of energy to electrical energy per unit charge to move around a complete circuit."),
        ("Semiconductor", "Materials which have intermediate electrical conductivity which varies substantially with temperature"),
        ("Electrical power", "The rate of electrical energy transfer (work done per unit time): P = VI.", True),
    ]),
    (20, "D.C. circuits", [
        ("Kirchhoff's First Law", "The sum of the current entering a junction is equal to the sum of the current leaving it."),
        ("Kirchhoff's Second Law", "The sum of electromotive force is equal to the sum of potential difference for any closed loop in a circuit."),
    ]),
]

ESTIMATES = [
    ("Acceleration of a family car", "2 m s⁻²"),
    ("Acceleration of free fall on the Moon", "1.6 m s⁻²", True),
    ("Walking speed", "1 m s⁻¹"),
    ("Car speed", "20 m s⁻¹"),
    ("Sprinter speed", "10 m s⁻¹"),
    ("Mass of an orange", "100 g"),
    ("Height of room in a house", "2 m"),
    ("Diameter of a pencil", "1 cm"),
    ("Volume of a small bean", "0.5 cm³"),
    ("Speed of a jet", "200 m s⁻¹"),
    ("Temperature of human body", "310 K"),
    ("Diameter of hair", "0.5 mm"),
    ("Young's modulus of a metal wire", "10¹¹ Pa"),
    ("Resistivity of copper", "10⁻⁸ Ω m"),
    ("Resistivity of an insulator", "10¹¹ Ω m"),
    ("EMF of a car battery", "12 V"),
    ("Current in domestic appliance", "13 A"),
]

COMPARE = [
    ("Stationary vs progressive waves", ["Stationary", "Progressive"], [
        ("A · Amplitude", "Varies between two nodes", "The same for all points"),
        ("P · Phase", "All points between two adjacent nodes are in phase", "Not in phase"),
        ("E · Energy", "Energy is not transmitted", "Energy is transmitted"),
    ]),
    ("Current vs static electricity", ["Current electricity", "Static electricity"], [
        ("Net flow of charge", "There <b>is</b> a net flow of charge in a certain direction", "There is <b>no</b> net flow of charge in a certain direction"),
    ]),
    ("Conductor vs insulator", ["Conductor", "Insulator"], [
        ("Mobile charge carriers", "Material that <b>has</b> mobile charge carriers (electrons and ions) which drift to constitute electric current", "Material that <b>doesn't have</b> mobile charge carriers"),
    ]),
]


def defs(items, ch):
    out = []
    for it in items:
        term, d = it[0], it[1]
        flag = it[2] if len(it) > 2 else None
        tag = ("<i>corrected to mark scheme</i>" if flag == "corrected"
               else "<i>blank on sheet · added</i>" if flag else f"<i>Ch {ch}</i>")
        out.append(f'<div class="def"><div class="lab"><span>{e(term)}</span>{tag}</div><p>{e(d)}</p></div>')
    return "".join(out)


# exam-wording notes where the sheet's phrasing would lose marks (shown under the chapter card)
NOTES = {
    1: ('trap', "Mark-scheme wording", "Base quantities: <b>mass, length, time, current, temperature, amount of substance</b> (SI base units kg, m, s, A, K, mol). Learn the list; derived units are products/quotients of base units."),
    2: ('trap', "Precision", "Cambridge treats precision as <b>how close repeated readings are to each other</b> (small random error, small spread). Accuracy = how close to the true value (small systematic error)."),
    3: ('tip', "Speed vs velocity", "Speed is a scalar, velocity a vector. In the exam: velocity = <b>rate of change of displacement</b>, acceleration = <b>rate of change of velocity</b>. Don't write \"speed per time\"."),
    4: ('tip', "Newton's 2nd law", "\"Resultant force is proportional to the rate of change of momentum <b>and acts in the direction of</b> the change in momentum.\" The direction part is often the second mark."),
    5: ('trap', "Torque of a couple (lost 2 marks in Set 3)", "Write: <b>one of the forces × the perpendicular distance between the lines of action of the forces</b>. Say \"lines of action\", not just \"between forces\"."),
    6: ('trap', "GPE / KE (lost 2 marks in Set 3)", "Keyword pattern: energy stored <b>in</b> ___ <b>due to</b> ___. GPE: energy a mass has due to its position in a gravitational field. KE: energy a mass has due to its motion. Work: force × distance moved <b>in the direction of the force</b>."),
    9: ('tip', "Young modulus", "Stress/strain, valid only up to the <b>limit of proportionality</b>. Hooke's law: force ∝ extension up to the limit of proportionality."),
    14: ('tip', "Wavelength", "\"Distance between two adjacent points <b>in phase</b>\" (or adjacent crests). Intensity = power per unit area normal to the direction of travel; intensity ∝ amplitude²."),
    15: ('tip', "Coherent", "Coherent = <b>constant phase difference</b> (and so the same frequency). For observable two-source interference also need similar amplitudes."),
    17: ('tip', "Field strength", "Force per unit <b>positive</b> charge. The word \"positive\" is the mark."),
    19: ('tip', "p.d. vs e.m.f.", "p.d.: electrical → other forms, per unit charge. e.m.f.: other forms → electrical, per unit charge. Resistance = p.d. / current, NOT \"gradient of the I–V graph\"."),
    20: ('link', "What the laws conserve", "Kirchhoff 1 = conservation of <b>charge</b>. Kirchhoff 2 = conservation of <b>energy</b>."),
}


def build():
    C = []
    total = sum(len(x[2]) for x in CHAPTERS)
    C.append(card("cover", "Start", "Physics definitions", "Cover", f"""
<p class="sec" style="margin:0">CAIE 9702 · AS Level · Definitions</p>
<p class="cover-k">Def</p>
<h1>Definitions &amp; comparisons by chapter</h1>
<p class="lede">From Muhammad Afiq bin Abdul Wahid's definitions sheet. Blanks on the sheet are filled in and marked "added"; three definitions are corrected to mark-scheme wording.</p>
<div class="stat"><div><b>{total}</b>definitions</div><div><b>{len(ESTIMATES)}</b>estimates</div><div><b>{len(CHAPTERS)}</b>chapters</div></div>
<p><a href="index.html">Open Revision Hub</a></p>
<div class="swipehint">Swipe or use the arrows · tap ☰ for contents</div>""", sec="Start"))

    C.append(card("how", "Start", "How definitions are marked", "Overview", """
<h2>Definitions are free marks, if the wording is exact</h2>
<p class="lede">A "define" or "state" question usually has 1–2 marks for one or two key phrases. Vague words score zero.</p>
<div class="chain"><span>1 · Say what it is (quantity / ratio / rate)</span><i>→</i><span>2 · Key phrase ("per unit", "rate of change of")</span><i>→</i><span>3 · Condition (e.g. "limit of proportionality not exceeded")</span></div>
<div class="note tip"><b>Method tonight</b>Cover the definition, say it out loud, check it word for word. Use the Cards button (top right) to drill, and put misses in the "Again" pile.</div>
<div class="note trap"><b>Words that lose marks</b>"amount" instead of "rate of change", "distance" instead of "perpendicular distance", leaving out "positive" (field strength) or "original" (stress).</div>""", sec="Start"))

    for ch, title, items in CHAPTERS:
        grp = f"Ch {ch} · {title}"
        chunks = [items] if len(items) <= 8 else [items[:6], items[6:]]
        for i, chunk in enumerate(chunks):
            suffix = f" ({i + 1}/{len(chunks)})" if len(chunks) > 1 else ""
            body = f"<h2>Chapter {ch}: {e(title)}{suffix}</h2>" + defs(chunk, ch)
            if i == len(chunks) - 1 and ch in NOTES:
                kind, lab, txt = NOTES[ch]
                body += f'<div class="note {kind}"><b>{lab}</b>{txt}</div>'
            if ch == 6 and i == len(chunks) - 1:
                body += '<div class="note link"><b>Keyword (from the sheet)</b>Potential energy: energy stored in ____ due to ______.</div>'
            C.append(card(f"ch{ch}-{i}", grp, title + suffix, "Definitions", body, sec=f"Ch {ch}"))
        if ch == 1:
            rows = "".join(
                f'<tr><td class="k">{e(x[0])}</td><td>{e(x[1])}{" <i>(added)</i>" if len(x) > 2 else ""}</td></tr>' for x in ESTIMATES)
            C.append(card("est", grp, "Estimations", "Concept", f"""
<h2>Estimations (order of magnitude)</h2>
<div class="tw"><table><tr><th>Quantity</th><th>Estimate</th></tr>{rows}</table></div>
<div class="note tip"><b>Paper 1</b>Estimation MCQs only need the right power of ten. Eliminate options that are 100× out first.</div>""", sec="Ch 1"))

    for i, (title, heads, rows) in enumerate(COMPARE):
        tr = "".join(f'<tr><td class="k">{a}</td><td>{b}</td><td>{c}</td></tr>' for a, b, c in rows)
        extra = ('<div class="note tip"><b>Memory hook: A-P-E</b>Amplitude, Phase, Energy: three differences, one mark each.</div>'
                 if i == 0 else "")
        C.append(card(f"cmp{i}", "Comparisons", title, "Comparison", f"""
<h2>{e(title)}</h2>
<div class="tw"><table><tr><th></th><th>{heads[0]}</th><th>{heads[1]}</th></tr>{tr}</table></div>{extra}""", sec="Compare"))

    # worked examples: how marks are split on a definition question
    C.append(card("we1", "Worked examples", "Define the torque of a couple", "Worked example", """
<h2>Define the torque of a couple [2]</h2>
<p><b>Q:</b> Define the torque of a couple.</p>
<ol class="steps">
<li><b>B1:</b> one of the forces (not "the sum of the forces")</li>
<li><b>B1:</b> × the <b>perpendicular distance between the lines of action</b> of the forces</li>
<li><b>Full answer:</b> The torque of a couple is the product of one of the forces and the perpendicular distance between their lines of action.</li>
</ol>
<div class="note trap"><b>Where marks go</b>"Force × distance" alone scores 0: no "one of", no "perpendicular".</div>""", sec="Worked example"))

    C.append(card("we2", "Worked examples", "Distinguish p.d. and e.m.f.", "Worked example", """
<h2>Distinguish between e.m.f. and p.d. [2]</h2>
<p><b>Q:</b> Distinguish between the electromotive force of a source and the potential difference across a resistor.</p>
<ol class="steps">
<li><b>B1 (e.m.f.):</b> energy transferred from other forms <b>to electrical</b> energy per unit charge</li>
<li><b>B1 (p.d.):</b> energy transferred from electrical energy <b>to other forms</b> per unit charge</li>
<li>Both need "per unit charge"; the direction of the energy transfer is what distinguishes them.</li>
</ol>""", sec="Worked example"))

    C.append(card("we3", "Worked examples", "Stationary vs progressive", "Worked example", """
<h2>State two differences between stationary and progressive waves [2]</h2>
<ol class="steps">
<li><b>B1 (Amplitude):</b> in a stationary wave the amplitude varies between nodes; in a progressive wave all points have the same amplitude.</li>
<li><b>B1 (Phase):</b> between two adjacent nodes all points are in phase; in a progressive wave adjacent points are not in phase.</li>
<li><b>Alternative B1 (Energy):</b> a stationary wave does not transmit energy; a progressive wave does.</li>
</ol>
<div class="note tip"><b>Write both sides</b>Each difference must say what happens in <b>both</b> waves to earn the mark.</div>""", sec="Worked example"))

    C.append(card("mist", "Common mistakes", "Common mistakes", "Mistakes", """
<h2>Common mistakes on definitions</h2>
<div class="tw"><table><tr><th>Mistake</th><th>Fix</th></tr>
<tr><td class="k">Moment = force × distance</td><td>× <b>perpendicular</b> distance from the pivot to the <b>line of action</b></td></tr>
<tr><td class="k">Stress = force / area</td><td>Force per unit <b>original</b> cross-sectional area</td></tr>
<tr><td class="k">Field strength = force per unit charge</td><td>Per unit <b>positive</b> charge</td></tr>
<tr><td class="k">Work = force × distance</td><td>Distance moved <b>in the direction of the force</b></td></tr>
<tr><td class="k">Coherent = same frequency</td><td><b>Constant phase difference</b></td></tr>
<tr><td class="k">Resistance = gradient of V–I graph</td><td>Ratio V/I at that point</td></tr>
<tr><td class="k">Mixing up p.d. and e.m.f.</td><td>Direction of energy conversion</td></tr>
<tr><td class="k">Elastic collision = momentum conserved</td><td>Momentum is always conserved; elastic means <b>KE</b> conserved too</td></tr>
</table></div>""", sec="Mistakes"))

    pqs = [
        ("Ch 4", 2, "State Newton's second law of motion.", "For a body of constant mass, the resultant force is proportional to the rate of change of its momentum (and acts in the direction of the change in momentum)."),
        ("Ch 6", 1, "Define gravitational potential energy.", "Energy stored due to the position of a mass in a gravitational field."),
        ("Ch 9", 2, "Define the Young modulus.", "The ratio of stress to strain, provided the limit of proportionality is not exceeded."),
        ("Ch 15", 2, "State the principle of superposition.", "When two or more waves meet at a point, the resultant displacement is the sum of the individual displacements of the waves."),
        ("Ch 20", 2, "State Kirchhoff's second law and the quantity it conserves.", "The sum of the e.m.f.s equals the sum of the p.d.s around any closed loop in a circuit. It conserves energy."),
    ]
    body = "<h2>Practice · write them out</h2>" + "".join(
        f'<div class="pq"><div class="qh"><span>Q{i + 1} · {c}</span><span class="mk">[{m}]</span></div>'
        f'<p class="qt">{e(q)}</p><div class="ans"><b>Answer</b>{e(a)}</div></div>'
        for i, (c, m, q, a) in enumerate(pqs))
    C.append(card("pr", "Practice", "Practice: define it", "Practice", body, sec="Practice"))

    C.append(card("sum", "Summary", "One-line summary", "Summary", """
<h2>The patterns behind almost every definition</h2>
<div class="tw"><table><tr><th>Pattern</th><th>Examples</th></tr>
<tr><td class="k">Rate of change of ___</td><td>velocity, acceleration, force (of momentum), current (of charge), power (of work)</td></tr>
<tr><td class="k">___ per unit ___</td><td>density, pressure, stress, field strength, p.d., e.m.f., intensity</td></tr>
<tr><td class="k">Ratio ___ / ___</td><td>strain, Young modulus, resistance, efficiency</td></tr>
<tr><td class="k">Product ___ × ___</td><td>momentum, moment, torque, work</td></tr>
<tr><td class="k">Energy stored in ___ due to ___</td><td>GPE, KE, EPE, electric PE</td></tr>
<tr><td class="k">Law + condition</td><td>Hooke's, Ohm's, Young modulus, conservation of momentum</td></tr>
</table></div>""", sec="Summary"))
    return C


FLASH = []
for ch, title, items in CHAPTERS:
    for it in items:
        FLASH.append([f"Ch {ch}", f"Define: {it[0]}", it[1]])
for x in ESTIMATES:
    FLASH.append(["Estimate", f"Estimate: {x[0]}", x[1]])
FLASH += [
    ["Compare", "Stationary vs progressive: amplitude?", "Stationary: varies between nodes. Progressive: same for all points."],
    ["Compare", "Stationary vs progressive: phase?", "Stationary: all points between adjacent nodes in phase. Progressive: not in phase."],
    ["Compare", "Stationary vs progressive: energy?", "Stationary: not transmitted. Progressive: transmitted."],
    ["Compare", "Current vs static electricity?", "Current: there is a net flow of charge in a certain direction. Static: there is none."],
    ["Compare", "Conductor vs insulator?", "Conductor has mobile charge carriers (electrons and ions) that drift to form a current; insulator doesn't."],
]

QUIZ = [
    {"s": "Ch 2", "q": "Readings that are consistently above the true value show…", "o": ["random error", "systematic error", "high precision", "zero error only when using a ruler"], "c": 1,
     "e": "Systematic error: readings consistently above or below the true value. Random error scatters readings around it."},
    {"s": "Ch 2", "q": "Accuracy is mainly affected by the size of the…", "o": ["random error", "smallest division", "systematic error", "number of readings"], "c": 2,
     "e": "Accuracy = closeness to the true value, influenced by systematic error."},
    {"s": "Ch 1", "q": "Which is a scalar?", "o": ["Displacement", "Momentum", "Weight", "Kinetic energy"], "c": 3,
     "e": "Energy has magnitude only. The other three have direction."},
    {"s": "Ch 3", "q": "Velocity is defined as the rate of change of…", "o": ["distance", "speed", "displacement", "acceleration"], "c": 2,
     "e": "Velocity = rate of change of displacement; speed = rate of change of distance."},
    {"s": "Ch 4", "q": "Force is defined as the…", "o": ["product of mass and velocity", "rate of change of momentum", "mass × distance", "rate of change of kinetic energy"], "c": 1,
     "e": "Force = rate of change of momentum. A is momentum."},
    {"s": "Ch 4", "q": "In an elastic collision, which is conserved?", "o": ["Momentum only", "Kinetic energy only", "Both momentum and total kinetic energy", "Neither"], "c": 2,
     "e": "Momentum is always conserved (no external force); elastic means total KE before = after as well."},
    {"s": "Ch 5", "q": "A couple consists of…", "o": ["two equal forces along the same line in opposite directions", "two equal parallel forces in opposite directions whose lines do not coincide", "two unequal parallel forces", "one force and a pivot"], "c": 1,
     "e": "Equal, parallel, opposite, and the lines of action do not coincide. A would give zero torque."},
    {"s": "Ch 5", "q": "Pressure is…", "o": ["force × area", "force acting perpendicularly per unit area", "force per unit volume", "mass per unit area"], "c": 1,
     "e": "Pressure = normal force per unit cross-sectional area."},
    {"s": "Ch 6", "q": "Efficiency is defined as…", "o": ["total input / useful output", "useful energy output / total energy input", "work done / time", "wasted energy / total energy"], "c": 1,
     "e": "Efficiency = useful energy output per total energy input."},
    {"s": "Ch 9", "q": "Stress is force per unit…", "o": ["extension", "original length", "original cross-sectional area", "volume"], "c": 2,
     "e": "Stress uses the ORIGINAL cross-sectional area."},
    {"s": "Ch 9", "q": "The Young modulus is stress/strain provided that…", "o": ["the wire is copper", "the limit of proportionality is not exceeded", "the wire has broken", "the extension is constant"], "c": 1,
     "e": "Valid only up to the limit of proportionality."},
    {"s": "Ch 14", "q": "In a transverse wave, particles vibrate…", "o": ["parallel to energy propagation", "normal to energy propagation", "in circles only", "not at all"], "c": 1,
     "e": "Transverse: normal (perpendicular). Longitudinal: parallel."},
    {"s": "Ch 14", "q": "Wavelength is the shortest distance between two successive points that are…", "o": ["at rest", "in phase", "in antiphase", "at maximum displacement only"], "c": 1,
     "e": "Successive points in phase."},
    {"s": "Ch 15", "q": "Two sources are coherent if they have…", "o": ["the same amplitude", "a constant phase difference", "the same intensity", "different frequencies"], "c": 1,
     "e": "Coherent = constant phase difference (hence same frequency)."},
    {"s": "Ch 15", "q": "Which is TRUE of a stationary wave?", "o": ["Energy is transmitted", "All points have the same amplitude", "All points between adjacent nodes are in phase", "Adjacent points are never in phase"], "c": 2,
     "e": "A-P-E: amplitude varies, points between adjacent nodes in phase, no energy transmitted."},
    {"s": "Ch 17", "q": "Electric field strength is the force per unit…", "o": ["charge", "positive charge", "mass", "area"], "c": 1,
     "e": "Per unit POSITIVE charge. Leaving out 'positive' loses the mark."},
    {"s": "Ch 19", "q": "E.m.f. is energy transferred…", "o": ["from electrical to other forms per unit charge", "from other forms to electrical per unit charge", "per unit time", "per unit current"], "c": 1,
     "e": "E.m.f.: other → electrical. P.d.: electrical → other."},
    {"s": "Ch 20", "q": "Kirchhoff's first law is a consequence of conservation of…", "o": ["energy", "momentum", "charge", "mass"], "c": 2,
     "e": "Current in = current out at a junction: charge is conserved. The second law conserves energy."},
]


def write():
    meta = {"title": "Physics Definitions Deck", "short": "Phys Defs", "bar": "Physics · Definitions",
            "code": "9702 · AS · all chapters", "key": "deck-9702-defs"}
    cards = build()
    out = engine.render(meta, cards, FLASH, QUIZ)
    out = out.replace("<b>Paper 1 quiz</b>", "<b>Definitions quiz</b>")
    (HERE / "deck-phys-defs.html").write_text(out, encoding="utf8")
    print("phys defs", len(out), "bytes,", len(cards), "cards,", len(FLASH), "flashcards,", len(QUIZ), "quiz")
    return cards


if __name__ == "__main__":
    write()
