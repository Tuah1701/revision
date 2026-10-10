"""9708 Chapter 1 · Basic economic ideas and resource allocation."""
import math
from engine import card
from diagrams import Fig, fig

ORIG = "https://claude.ai/code/artifact/f1636c3a-d24e-482e-8577-d8d7c8b138dc"


def concave(r):
    return lambda x: r * math.sqrt(max(0.0, 1 - (x / r) ** 2))


def convex(r):
    return lambda x: r - math.sqrt(max(0.0, r * r - (r - x) ** 2))


CG, KG = "Capital goods", "Consumer goods"

# ---------- diagrams ----------
f = concave(8.6)
main = Fig(xl=KG, yl=CG, aria="PPC with points A to F on the curve, U inside and H outside")
main.curve(f, 0, 8.6, "d").text((8.1, 4.4), "PPC", "t-d")
for x, l in zip([0, 2.6, 4.4, 5.8, 7.2, 8.6], "ABCDEF"):
    main.pt((x, f(x)), l, off=(7, -6) if x < 8 else (-8, -8), anchor="start" if x < 8 else "end")
main.pt((3.2, 3.6), "U", hollow=True).pt((7.0, 7.4), "H", hollow=True)
D_MAIN = fig(main, caption="On the curve (A–F): attainable and productively efficient. U inside: idle or wasted resources. H outside: unattainable, which shows scarcity.")

s1 = Fig(xl=KG, yl=CG, aria="Concave PPC").curve(concave(8.4), 0, 8.4, "d")
s2 = Fig(xl=KG, yl=CG, aria="Straight-line PPC").line((0, 8.4), (8.4, 0), "d")
s3 = Fig(xl=KG, yl=CG, aria="Convex PPC").curve(convex(8.4), 0, 8.4, "d")
for fg, fn in ((s1, concave(8.4)), (s2, lambda x: 8.4 - x), (s3, convex(8.4))):
    for a in (2, 4, 6):
        fg.path([(a, fn(a)), (a, fn(a + 2)), (a + 2, fn(a + 2))], "o")
D_SHAPES = fig(("Concave · rising OC", s1), ("Straight · constant OC", s2), ("Convex · falling OC", s3),
               caption="The dashed steps show capital goods given up for each equal extra amount of consumer goods.")

o = Fig(xl=KG, yl=CG, aria="Outward shift from PPC1 to PPC2")
o.curve(concave(6.4), 0, 6.4, "o", "PPC1", off=(-2, 14), anchor="end").curve(concave(8.6), 0, 8.6, "d", "PPC2", off=(-4, -10), anchor="end")
o.arrow((4.5, 4.6), (6.0, 6.2))
i = Fig(xl=KG, yl=CG, aria="Inward shift from PPC1 to PPC2")
i.curve(concave(8.6), 0, 8.6, "o", "PPC1", off=(-4, -10), anchor="end").curve(concave(6.4), 0, 6.4, "b", "PPC2", off=(-2, 14), anchor="end")
i.arrow((6.0, 6.2), (4.5, 4.6))
n = Fig(xl=KG, yl=CG, aria="Non-parallel shift: only the capital goods intercept rises")
n.curve(concave(7), 0, 7, "o", "PPC1", off=(-2, 14), anchor="end")
n.curve(lambda x: 9.2 * math.sqrt(max(0, 1 - (x / 7) ** 2)), 0, 7, "d", "PPC2", off=(6, -40), anchor="start")
n.arrow((0.5, 7.2), (0.5, 8.8))
D_SHIFTS = fig(("Outward · growth", o), ("Inward · loss of resources", i), ("Capital goods only", n))

gfig = Fig(xl=KG, yl=CG, aria="Actual growth from U to V, potential growth from PPC1 to PPC2")
gfig.curve(concave(7), 0, 7, "o", "PPC1", off=(-2, 14), anchor="end").curve(concave(9), 0, 9, "d", "PPC2", off=(-4, -10), anchor="end")
gfig.pt((2.6, 3.0), "U", hollow=True, off=(-8, 14), anchor="end").pt((4.2, concave(7)(4.2)), "V", off=(6, -6))
gfig.arrow((2.8, 3.2), (4.0, 5.3))
D_GROWTH = fig(gfig, caption="U → V is actual (short-run) growth at zero opportunity cost. PPC1 → PPC2 is potential (long-run) growth.")


def build():
    C = []
    C.append(card("cover", "Start", "Basic economic ideas", "Cover", f"""
<p class="sec" style="margin:0">CAIE 9708 · AS Level · Chapter 1</p>
<p class="cover-k">Ch1</p>
<h1>Basic economic ideas &amp; resource allocation</h1>
<p class="lede">The vocabulary the rest of the course is written in. Built from Puan Zaihan's 15 Chapter 1 handouts.</p>
<div class="stat"><div><b>6</b>syllabus sections</div><div><b>4</b>worked examples</div><div><b>53</b>flashcards</div><div><b>22</b>quiz questions</div></div>
<p class="swipehint">Swipe left to start. Tap ☰ for contents.</p>
<p><a href="https://claude.ai/artifact/3MqyaRKgJG7ufb65fwrnoF" target="_blank" rel="noopener">Open Revision Hub</a></p>""", sec="Start"))

    C.append(card("big", "Start", "The big picture", "Overview", f"""
<h2>One idea runs through the whole chapter</h2>
<div class="chain"><span>Scarcity</span><i>→</i><span>Choice</span><i>→</i><span>Opportunity cost</span><i>→</i><span>What · How · For whom?</span><i>→</i><span>Economic system</span><i>→</i><span>Goods the market gets wrong</span></div>
<p>Resources are scarce, so every agent must choose. Every choice has an opportunity cost. Society must decide what, how and for whom to produce, through a market, planned or mixed system. The market fails for public, merit and demerit goods. The <b>PPC</b> shows the first four links at once.</p>
<div class="toc-mini">
<button type="button" data-goto="s11"><b>1.1</b><span>Scarcity, choice, opportunity cost</span></button>
<button type="button" data-goto="s12a"><b>1.2</b><span>Economic methodology</span></button>
<button type="button" data-goto="s13a"><b>1.3</b><span>Factors of production</span></button>
<button type="button" data-goto="s14a"><b>1.4</b><span>Economic systems</span></button>
<button type="button" data-goto="s15a"><b>1.5</b><span>Production possibility curves</span></button>
<button type="button" data-goto="s16a"><b>1.6</b><span>Classification of goods</span></button>
</div>""", sec="Overview"))

    C.append(card("exams", "Start", "Where it's tested", "Overview", """
<h2>Where Chapter 1 shows up in your exams</h2>
<div class="tw"><table><tr><th>Paper</th><th>How Chapter 1 is tested</th></tr>
<tr><td class="k">Paper 1<br><span class="mono">30 MCQs</span></td><td>PPC reading (which point, which shift, opportunity cost as a distance on an axis), "which is normative?", "which factor?", features of market and planned economies.</td></tr>
<tr><td class="k">Paper 2 A<br><span class="mono">Data response · 20</span></td><td>Short parts like "explain the contribution of enterprise…" [4] or "discuss whether government intervention in a mixed economy…" [6], set in a real country.</td></tr>
<tr><td class="k">Paper 2 B<br><span class="mono">Essay · 8 + 12</span></td><td>(a) explain with a diagram, then "consider" a claim. (b) "assess" a big claim, e.g. is the free market always desirable?</td></tr></table></div>
<div class="note tip"><b>Study route</b>Read a section's cards, flip that section's flashcards (Cards → filter), then do the quiz. Plan your own essay before reading any model answer.</div>""", sec="Overview"))

    # ---------- 1.1 ----------
    C.append(card("s11", "1.1 Scarcity & choice", "Scarcity & opportunity cost", "Concept", """
<h2>Scarcity, choice and opportunity cost</h2>
<div class="def"><span class="lab">Definition · Scarcity <i>1.1.1</i></span><p>A situation where there are insufficient resources to satisfy all the needs and wants of people. Resources are finite; wants are unlimited.</p></div>
<ul><li>Applies to <b>every agent</b>: individuals, firms, governments, international agencies.</li>
<li><b>Needs</b> are essentials (food, shelter, clothing). <b>Wants</b> are less important desires (a new TV).</li>
<li>Scarcity is <b>relative</b>, not a shortage. Even rich countries face it because wants keep growing.</li></ul>
<div class="def"><span class="lab">Definition · Opportunity cost <i>1.1.3</i></span><p>The benefit forgone from the <b>next best alternative</b> when a choice is made. One alternative, not the sum of all of them.</p></div>
<div class="tw"><table><tr><th>Agent</th><th>Choice</th><th>Opportunity cost</th></tr>
<tr><td class="k">Student</td><td>Movie, homework or friends; picks movie, homework 2nd</td><td>The homework</td></tr>
<tr><td class="k">Government</td><td>$10m: hospital (1st) or university (2nd)</td><td>The university</td></tr>
<tr><td class="k">Firm</td><td>New IT system or new factory; picks IT</td><td>The factory</td></tr></table></div>
<div class="note trap"><b>Exam trap</b>"The opportunity cost of the movie is the homework <i>and</i> friends" is wrong: only the next best counts. And opportunity cost is not the money price: a free concert ticket still costs your time.</div>""", sec="1.1 · Syllabus 1.1.1–1.1.3"))

    C.append(card("s11b", "1.1 Scarcity & choice", "The three questions", "Concept", """
<h2>The three basic questions of resource allocation</h2>
<div class="two">
<div><h4>What to produce?</h4><p>Which goods and how many. Consumer goods (give utility directly: phones, curry) vs capital goods (make other goods: machines, factories). Should Bata Malaysia make sports shoes, casual shoes or sandals?</p></div>
<div><h4>How to produce?</h4><p>Which mix of factors. <b>Labour-intensive</b>: high labour relative to capital (hand-stitched shoes). <b>Capital-intensive</b>: high capital relative to labour (machine-made). Firms pick the cheapest efficient method.</p></div>
<div><h4>For whom to produce?</h4><p>Who gets the output, which decides how equal society is. Market: whoever has purchasing power. Planned: whoever the state decides.</p></div>
</div>
<div class="note link"><b>Links to 1.4</b>The answers depend on the economic system: the price mechanism (market), a central planning authority (command), or both (mixed).</div>""", sec="1.1 · Syllabus 1.1.4"))

    # ---------- 1.2 ----------
    C.append(card("s12a", "1.2 Methodology", "Economics as a social science", "Concept", """
<h2>How economists think</h2>
<ul><li><b>Social</b>: it studies human behaviour and how society works.</li>
<li><b>Science</b>: observe behaviour, form a theory, test it.</li>
<li>A theory is usually expressed as a <b>model</b>: a simplified representation of reality. The PPC and demand–supply diagram are both models.</li></ul>
<div class="note tip"><b>Evaluation hook</b>Economists can't run controlled experiments on whole economies and people don't always behave predictably, so predictions are less certain than in natural sciences. That's why assumptions like ceteris paribus are needed.</div>
<div class="two">
<div><h4>Micro · mikros, small</h4><p>Individual markets and decision-makers: households, firms, one labour market. Demand for durians; demand for nurses.</p></div>
<div><h4 class="t">Macro · makros, large</h4><p>The whole economy via aggregates: AD, national output, inflation, unemployment, growth, trade.</p></div>
</div>
<p>The line is blurred: a rise in demand for cars (micro) can change a country's imports and exports (macro).</p>""", sec="1.2 · Syllabus 1.2.1"))

    C.append(card("s12b", "1.2 Methodology", "Positive vs normative", "Concept", """
<h2>Positive vs normative statements</h2>
<div class="def"><span class="lab">Positive · fact-based</span><p>Objective; can be tested, verified or refuted by evidence. May be true or false. Often cause-and-effect. <i>"Malaysia's population in 2019 was over 30 million."</i></p></div>
<div class="def"><span class="lab">Normative · value judgement</span><p>Subjective opinion about good/bad, fair/unfair. Cannot be tested. Often contains <b>should, ought, fair, better</b>. <i>"The government should spend more on education."</i></p></div>
<div class="note trap"><b>Exam traps</b>
(1) A positive statement can be false and still be positive. (2) A forecast is positive. (3) "If firms raise prices, profits will rise" is positive. (4) Questions too: "What is the impact of removing petrol subsidies?" is positive; "How <i>should</i> the government remove subsidies?" is normative.</div>
<div class="note tip"><b>In essays</b>When a question asks whether something is "desirable" or "should" happen, say the answer partly depends on a value judgement about equity vs efficiency. That is AO3.</div>""", sec="1.2 · Syllabus 1.2.2"))

    C.append(card("s12c", "1.2 Methodology", "Ceteris paribus & time", "Concept", """
<h2>Ceteris paribus and time periods</h2>
<div class="def"><span class="lab">Definition · Ceteris paribus <i>Latin</i></span><p>"All other things remaining equal." The effect of one variable is considered in isolation while every other influence is held constant.</p></div>
<p>It isolates one cause, e.g. a price change's effect on quantity demanded with income, tastes and other prices unchanged. In reality many things change at once: a standard limitation of any model.</p>
<div class="tw"><table><tr><th>Period</th><th>Definition</th><th>How output rises</th></tr>
<tr><td class="k">Short run</td><td>At least one factor fixed (usually capital or land)</td><td>Only by adding the variable factor, typically labour</td></tr>
<tr><td class="k">Long run</td><td>All factors variable; technology constant</td><td>Change quantity and quality of all inputs</td></tr>
<tr><td class="k">Very long run</td><td>Technology, regulation and social attitudes also change</td><td>Technical progress; policy change; social change (WW1 brought more women into work)</td></tr></table></div>
<div class="note tip"><b>Most reusable evaluation</b>Short run vs long run. In Chapter 1: a PPC shift needs the long run; a transition economy suffers in the short run but may gain later; specialisation raises output now but can de-skill workers.</div>""", sec="1.2 · Syllabus 1.2.3–1.2.4"))

    # ---------- 1.3 ----------
    C.append(card("s13a", "1.3 Factors of production", "Four factors and rewards", "Concept", """
<h2>Factors of production</h2>
<div class="tw wide"><table><tr><th>Factor</th><th>Definition</th><th>Examples</th><th>Reward</th></tr>
<tr><td class="k">Land</td><td>Natural resources, "gifts of nature", on and under the earth</td><td>Farmland, forests, oil, the flow of a river</td><td class="k">Rent</td></tr>
<tr><td class="k">Labour</td><td>Physical and mental effort of workers, incl. skills</td><td>Factory workers, teachers, accountants</td><td class="k">Wages</td></tr>
<tr><td class="k">Capital</td><td>Man-made physical resources used to produce other goods. <b>Not money.</b></td><td>Machinery, factories, IT, roads, pipelines</td><td class="k">Interest</td></tr>
<tr><td class="k">Enterprise</td><td>The organising, risk-taking factor; a specialised form of labour</td><td>A founder starting a business with her savings</td><td class="k">Profit</td></tr></table></div>
<div class="note trap"><b>Exam traps</b>$10,000 in a savings account is not capital (it's money). A robot is capital, not labour. A company accountant is labour, not enterprise. Training or changing industry is still labour; setting up a business is enterprise.</div>""", sec="1.3 · Syllabus 1.3.1"))

    C.append(card("s13b", "1.3 Factors of production", "Entrepreneur & capital types", "Concept", """
<h2>The entrepreneur, and two kinds of capital</h2>
<div class="two">
<div><h4>1 · Organises</h4><p>Decides how to combine land, labour and capital to raise efficiency and output: the "how to produce" question at firm level.</p></div>
<div><h4>2 · Bears risk</h4><p>Invests own funds under uncertainty. Risk-taking separates the entrepreneur from other workers; profit is the reward.</p></div>
</div>
<p>Enterprise drives innovation, jobs and growth, so an "enterprise culture" (start-up grants, easier regulation) shifts the PPC out. In Malaysia: SME and start-up support via MDEC and Cradle.</p>
<div class="def"><span class="lab">Physical capital <i>1.3.2</i></span><p>Man-made factors: machinery, buildings, infrastructure. Often the main source of growth in low- and lower-middle-income countries.</p></div>
<div class="def"><span class="lab">Human capital</span><p>Skills, knowledge and experience of the labour force, built through education and training.</p></div>
<div class="note link"><b>Growth, two ways</b>Both raise labour productivity, so both shift the PPC outward. Human capital links to merit goods (education) in 1.6.</div>""", sec="1.3 · Syllabus 1.3.2–1.3.5"))

    C.append(card("s13c", "1.3 Factors of production", "Division of labour", "Concept", """
<h2>Specialisation and the division of labour</h2>
<div class="def"><span class="lab">Definition · Specialisation</span><p>Individuals, firms, regions and economies concentrate on producing the goods and services where they have an advantage over others.</p></div>
<p>By firm (tyre makers), by region (semiconductors around Penang), by country (Brazil and coffee), by individual = <b>division of labour</b>.</p>
<div class="def"><span class="lab">Definition · Division of labour</span><p>Production is split into many small tasks and each worker specialises in one task.</p></div>
<p><b>Adam Smith's pin factory (1776):</b> one worker doing every step makes about 1 pin a day; split into 18 operations, output rose to about <b>5,000 pins per worker per day</b>.</p>
<div class="two">
<div><h4 class="g">Advantages</h4><ul><li>Workers do what they're best at → higher productivity</li><li>Training in one task only → lower training costs</li><li>No time lost switching tasks</li><li>Production lines and machinery → lower average costs</li></ul></div>
<div><h4 class="r">Disadvantages</h4><ul><li>Monotony can reduce productivity</li><li>Narrow skills if made redundant</li><li>One group's strike can halt the line</li><li>Identical, standardised products</li></ul></div>
</div>""", sec="1.3 · Syllabus 1.3.4"))

    # ---------- 1.4 ----------
    C.append(card("s14a", "1.4 Economic systems", "Three systems compared", "Concept", """
<h2>Resource allocation in different systems</h2>
<div class="def"><span class="lab">Definition · Economic system</span><p>The way an economy allocates scarce resources to answer what, how and for whom to produce.</p></div>
<div class="tw wide"><table><tr><th></th><th>Market</th><th>Planned</th><th>Mixed</th></tr>
<tr><td class="k">Allocated by</td><td>Price mechanism, the "invisible hand"</td><td>Central planning authority</td><td>Both</td></tr>
<tr><td class="k">Ownership</td><td>Private, protected by law</td><td>State owns all but labour</td><td>Private and state</td></tr>
<tr><td class="k">Motivation</td><td>Self-interest: utility, profit</td><td>Common good</td><td>Both, by sector</td></tr>
<tr><td class="k">Decisions</td><td>Decentralised; competition</td><td>Centralised; prices fixed</td><td>Choice in private sector</td></tr>
<tr><td class="k">Examples</td><td>None pure; Singapore, Hong Kong closest</td><td>North Korea, Cuba</td><td>Every real economy, incl. Malaysia</td></tr></table></div>
<p class="lede" style="font-size:14.5px">Swipe the table sideways on a phone.</p>""", sec="1.4 · Syllabus 1.4.1"))

    C.append(card("s14b", "1.4 Economic systems", "How each answers the 3 questions", "Concept", """
<h2>How each system answers the three questions</h2>
<div class="tw wide"><table><tr><th></th><th>Market</th><th>Planned</th><th>Mixed</th></tr>
<tr><td class="k">What?</td><td>Consumer demand: <b>consumer sovereignty</b></td><td>Planners, using statistics and national priorities</td><td>Mostly demand, plus public and merit goods</td></tr>
<tr><td class="k">How?</td><td>Cheapest method: capital-intensive where labour is dear (UK), labour-intensive where cheap (India)</td><td>State chooses on social welfare, often labour-intensive for full employment</td><td>Firms minimise cost; government regulates pollution and waste</td></tr>
<tr><td class="k">For whom?</td><td>Those with purchasing power</td><td>State distributes evenly: fixed prices and rationing</td><td>Income for private goods; redistribution via taxes and welfare</td></tr></table></div>""", sec="1.4 · Syllabus 1.4.1"))

    C.append(card("s14c", "1.4 Economic systems", "Market vs planned: pros & cons", "Concept", """
<h2>Market vs planned economy</h2>
<h3>Market economy</h3>
<div class="two">
<div><h4 class="g">Advantages</h4><ul><li><b>Efficiency</b>: profit motive cuts waste, drives R&amp;D</li><li><b>Consumer sovereignty</b></li><li>No allocating bureaucracy</li><li>More choice, increased by trade</li><li>Economic and political freedom</li></ul></div>
<div><h4 class="r">Disadvantages (each a market failure)</h4><ul><li>Negative externalities (pollution, deforestation)</li><li>Monopoly power</li><li>Public goods not provided</li><li>Merit goods under-provided</li><li>Inequality: the rich have more "votes"</li><li>Instability: no full-employment guarantee</li></ul></div>
</div>
<h3>Planned economy</h3>
<div class="two">
<div><h4 class="g">Advantages</h4><ul><li>More equal distribution; minimum living standard</li><li>No private monopoly exploitation</li><li>Stability: low unemployment</li><li>More public and merit goods</li></ul></div>
<div><h4 class="r">Disadvantages</h4><ul><li>No economic freedom</li><li>Inefficiency, little innovation, weak incentives</li><li>Bureaucracy and corruption</li><li>Planning errors without prices → shortages and surpluses</li></ul></div>
</div>""", sec="1.4 · Syllabus 1.4.1–1.4.2"))

    C.append(card("s14d", "1.4 Economic systems", "Mixed economy", "Concept", """
<h2>Mixed economy</h2>
<div class="def"><span class="lab">Definition · Mixed economy</span><p>Resources are allocated partly by the price mechanism in the <b>private sector</b> and partly by government planning in the <b>public sector</b>.</p></div>
<p>All real economies are mixed; they differ in the degree of intervention.</p>
<h3>What government does</h3>
<ul><li>Protects property rights and contracts; keeps markets competitive</li><li>Provides public goods (defence, street lights)</li><li>Corrects information failure: encourages merit goods, discourages demerit goods (taxes, subsidies, information, regulation, direct provision)</li><li>Deals with externalities; redistributes income; stabilises the economy</li></ul>
<div class="two">
<div><h4 class="g">Advantages</h4><p>Market efficiency plus correction of market failure; less inequality; variety of private, public and merit goods; more stability.</p></div>
<div><h4 class="r">Disadvantages</h4><p>Fear of nationalisation deters investment; higher taxes cut incentives; corruption and rent-seeking; <b>government failure</b>.</p></div>
</div>
<div class="note link"><b>Malaysian application</b>Private firms dominate manufacturing and services; the state controls strategic firms (Petronas, TNB, GLCs); public clinics and schools; price controls and subsidies. Targeted diesel (2024) and RON95 (2025) subsidies shift the balance back towards the price mechanism while protecting lower-income households.</div>""", sec="1.4 · Syllabus 1.4.2"))

    C.append(card("s14e", "1.4 Economic systems", "Transition economies", "Concept", """
<h2>Transition economies</h2>
<div class="def"><span class="lab">Definition · Transition economy</span><p>An economy moving from central planning to a market-oriented system: Russia and Central/Eastern Europe after 1991, China from 1978, Vietnam (Đổi Mới) from 1986.</p></div>
<div class="two">
<div><h4 class="t">The process</h4><ul><li>Privatise; allow new firms and FDI</li><li>Liberalise trade (Poland, Russia, Estonia abolished tariffs in 1992)</li><li>Abolish planning; free prices</li><li>Build banks, a stock exchange</li><li>Enforce private property law</li></ul></div>
<div><h4 class="r">Difficulties</h4><ul><li>Sharp fall in GDP</li><li>Lack of entrepreneurial skill</li><li>High unemployment (inside the PPC)</li><li>High inflation as prices are freed</li><li>Unfair privatisation, inequality</li><li>Less welfare; trade deficits</li></ul></div>
</div>
<div class="note tip"><b>Evaluation</b>Speed matters: "shock therapy" brings short-run unemployment and inflation but can raise long-run efficiency; China's gradual approach avoided Russia's deep fall in output.</div>
<div class="note trap"><b>Handout correction</b>Economic System Part 2 says land and capital in a market economy are "predominantly owned by the public sector". It should read <b>private</b> sector. Check with Puan Zaihan.</div>""", sec="1.4 · Syllabus 1.4.2"))

    # ---------- 1.5 ----------
    C.append(card("s15a", "1.5 PPC", "What a PPC shows", "Concept", f"""
<h2>Production possibility curves</h2>
<div class="def"><span class="lab">Definition · PPC <i>1.5.1</i></span><p>A curve showing the maximum combinations of two goods an economy can produce when all resources are fully and efficiently employed, given the state of technology.</p></div>
<p><b>Four assumptions:</b> full employment · fixed resources · constant technology · two goods only.</p>
{D_MAIN}
<div class="note tip"><b>Diagram mark</b>Label axes with the two named goods ("Capital goods", "Consumer goods"), never X and Y. Label the curve PPC, the origin O, and every point you discuss.</div>""", sec="1.5 · Syllabus 1.5.1"))

    C.append(card("s15b", "1.5 PPC", "Six ideas on one curve", "Concept", """
<h2>What the PPC illustrates</h2>
<div class="tw"><table><tr><th>Concept</th><th>How the PPC shows it</th></tr>
<tr><td class="k">Scarcity</td><td>Points outside (H) can't be produced.</td></tr>
<tr><td class="k">Choice</td><td>The economy must pick one point on the curve.</td></tr>
<tr><td class="k">Opportunity cost</td><td>The negative slope: more of one good means less of the other.</td></tr>
<tr><td class="k">Efficiency</td><td>Every point on the curve is productively efficient.</td></tr>
<tr><td class="k">Unemployment</td><td>Points inside (U): idle or misused resources.</td></tr>
<tr><td class="k">Growth</td><td>Short run: U towards the curve. Long run: the curve shifts out.</td></tr></table></div>
<div class="formula">OC of 1 more X = units of Y given up ÷ units of X gained</div>
<div class="note tip"><b>MCQ method</b>In diagram MCQs the opportunity cost is a <b>distance on the other axis</b>. Drop guide lines from the start and end points to the axis of the good given up and read off the gap.</div>""", sec="1.5 · Syllabus 1.5.1"))

    C.append(card("s15c", "1.5 PPC", "Shapes of the PPC", "Concept", f"""
<h2>The shape follows opportunity cost</h2>
{D_SHAPES}
<div class="two">
<div><h4>Concave · rising OC</h4><p>The usual case. Resources are specialised, so moving them to the good they suit less loses ever more of the other good.</p></div>
<div><h4>Straight · constant OC</h4><p>Resources equally efficient at both goods. Handout Table 2: each extra X costs 2 Y.</p></div>
<div><h4>Convex · falling OC</h4><p>Resources get better at X as more is made (economies of scale). Rare in exams.</p></div>
</div>""", sec="1.5 · Syllabus 1.5.2"))

    C.append(card("s15d", "1.5 PPC", "Shifts of the PPC", "Concept", f"""
<h2>Shifts of the PPC</h2>
{D_SHIFTS}
<div class="two">
<div><h4 class="g">Outward: causes</h4><ul><li>Better technology, more capital-intensive methods</li><li>New resources (mineral deposits)</li><li>Bigger labour force: births, net immigration, later retirement</li><li>Better human capital</li><li>Enterprise culture</li></ul></div>
<div><h4 class="r">Inward: causes</h4><ul><li>Disasters or war destroying capital</li><li>Depletion of natural resources</li><li>Net emigration; shorter legal working week</li><li>Cuts to education and training</li></ul></div>
</div>
<div class="note trap"><b>Shift vs movement</b>Higher unemployment does <b>not</b> shift the PPC; it moves the economy inside it. Reallocating resources is a movement along it. Only a change in the quantity or quality of resources, or technology, shifts it.</div>
<p>If only one good's resources or technology improve, only that intercept moves. If working hours are cut by law, the PPC shifts in more for the more labour-intensive good.</p>""", sec="1.5 · Syllabus 1.5.3"))

    C.append(card("s15e", "1.5 PPC", "Inside the PPC & growth", "Concept", f"""
<h2>A point inside the PPC</h2>
<p>Inside the curve, resources are unemployed or used inefficiently. Output of <b>both</b> goods could rise at zero opportunity cost. Reducing unemployment is "free" growth in the short run; moving along the curve always costs something.</p>
{D_GROWTH}
<h3>Capital vs consumer goods: today vs the future</h3>
<p>More capital goods now means less consumption today, but the PPC shifts out further later. Mostly consumer goods means more now and slower growth.</p>
<div class="note tip"><b>Evaluation</b>The "best" point depends on whether society values present or future consumption: a normative judgement.</div>""", sec="1.5 · Syllabus 1.5.4"))

    # ---------- 1.6 ----------
    C.append(card("s16a", "1.6 Classification of goods", "Free, economic, private goods", "Concept", """
<h2>Free goods vs economic goods</h2>
<div class="chain"><span>All goods</span><i>→</i><span>Free goods</span><span>Economic goods</span><i>→</i><span>Private · Public (pure / quasi) · Merit · Demerit</span></div>
<div class="def"><span class="lab">Free good <i>1.6.1</i></span><p>Unlimited in supply, needs no factors of production, so zero opportunity cost and no price: air, sunlight, seawater.</p></div>
<div class="def"><span class="lab">Economic good</span><p>Limited because it uses scarce resources, so it has an opportunity cost. Includes private, public, merit and demerit goods.</p></div>
<div class="note trap"><b>Trap</b>"Free of charge" isn't a free good. A toy in a cereal box used materials and labour. Free public healthcare is an economic good, paid for by taxes.</div>
<div class="def"><span class="lab">Definition · Private good</span><p><b>Excludable</b> (non-payers can be stopped) and <b>rival</b> (one person's use reduces what's left). Also rejectable. A plate of nasi goreng in the canteen.</p></div>""", sec="1.6 · Syllabus 1.6.1"))

    C.append(card("s16b", "1.6 Classification of goods", "Public goods & free riders", "Concept", """
<h2>Public goods and the free rider problem</h2>
<div class="def"><span class="lab">Definition · Public good <i>1.6.2</i></span><p><b>Non-excludable</b> (non-payers can't be stopped from benefiting) and <b>non-rival</b> (the marginal cost of an extra user is zero). Usually non-rejectable. Defence, street lights, flood control, lighthouses.</p></div>
<div class="tw"><table><tr><th></th><th>Rival</th><th>Non-rival</th></tr>
<tr><td class="k">Excludable</td><td><b>Private</b>: food, petrol</td><td><b>Club / toll</b>: pay-TV, uncongested toll road</td></tr>
<tr><td class="k">Non-excludable</td><td><b>Common resource</b>: crowded beach, fish in the sea</td><td><b>Pure public</b>: defence, flood control</td></tr></table></div>
<div class="chain"><span>Non-excludable</span><i>→</i><span>people free ride</span><i>→</i><span>no effective demand revealed</span><i>→</i><span>firms can't profit</span><i>→</i><span>missing market</span></div>
<p>Non-rivalry adds to this: with zero marginal cost, the efficient price is zero, so no profit-seeking firm supplies it. Government provides public goods, financed by taxation.</p>
<div class="def"><span class="lab">Definition · Free rider</span><p>Someone who enjoys a good's benefit without paying, because they can't be excluded.</p></div>""", sec="1.6 · Syllabus 1.6.2"))

    C.append(card("s16c", "1.6 Classification of goods", "Quasi-public goods", "Concept", """
<h2>Quasi-public goods</h2>
<div class="def"><span class="lab">Definition · Quasi-public good</span><p>Some but not all features of a public good. <b>Semi-non-rival</b> (can become congested: parks, beaches, roads at peak times) and/or <b>semi-non-excludable</b> (exclusion possible but costly: fencing a beach, toll booths).</p></div>
<p>Because exclusion is possible, the private sector can provide some quasi-public goods, such as the PLUS expressways.</p>
<div class="note link"><b>Malaysian example</b>KL's SMART Tunnel: as a flood-diversion tunnel it acts like a public good, but its motorway section charges a toll, so that part is excludable.</div>""", sec="1.6 · Syllabus 1.6.2"))

    C.append(card("s16d", "1.6 Classification of goods", "Merit & demerit goods", "Concept", """
<h2>Merit and demerit goods</h2>
<div class="def"><span class="lab">Definition · Merit good <i>1.6.3</i></span><p>A private good considered desirable but <b>under-consumed</b> and under-provided by the free market because of <b>information failure</b>: consumers underestimate its benefits. Often has positive externalities (SB &gt; PB). Education, healthcare, vaccinations.</p></div>
<p>Education: private benefits (skills, pay) plus external benefits (skilled workforce, growth) that individuals ignore. Vaccination protects others too.</p>
<div class="def"><span class="lab">Definition · Demerit good <i>1.6.4</i></span><p>A private good considered undesirable that is <b>over-consumed</b> because consumers underestimate its harm. Often has negative externalities. Cigarettes, alcohol, junk food.</p></div>
<p>Malaysian policy: excise duty on sugar-sweetened drinks (since 2019), cigarette taxes, the Control of Smoking Products for Public Health Act 2024.</p>
<div class="note trap"><b>Don't confuse</b>Merit goods are <b>not</b> public goods. Education is rival and excludable. Public goods: the market provides <b>none</b>. Merit goods: it provides <b>too little</b>.</div>
<div class="note link"><b>Forward link</b>1.6 is the entry point to Chapter 3 (market failure and government intervention).</div>""", sec="1.6 · Syllabus 1.6.3–1.6.4"))

    # ---------- worked examples ----------
    C.append(card("we1", "Worked examples", "Opportunity cost from a table", "Worked example", """
<h2>Calculate opportunity cost from a PPC table</h2>
<div class="tw"><table><tr><th>Point</th><th class="n">Good X</th><th class="n">Good Y</th></tr>
<tr><td>A</td><td class="n">0</td><td class="n">15</td></tr><tr><td>B</td><td class="n">1</td><td class="n">14</td></tr>
<tr><td>C</td><td class="n">2</td><td class="n">12</td></tr><tr><td>D</td><td class="n">3</td><td class="n">9</td></tr>
<tr><td>E</td><td class="n">4</td><td class="n">5</td></tr><tr><td>F</td><td class="n">5</td><td class="n">0</td></tr></table></div>
<p><b>Q:</b> What is the opportunity cost of moving from C to D? What happens to opportunity cost along the curve, and why?</p>
<ol class="steps">
<li>Write the formula: OC of one more X = Y given up ÷ X gained.</li>
<li>C → D: Y falls from 12 to 9, so 3 units of Y are given up; X rises from 2 to 3, so 1 unit gained.</li>
<li>OC = 3 ÷ 1 = <b>3 units of Y per unit of X</b>. State it as a positive amount of the good given up.</li>
<li>Repeat for each step: A→B 1, B→C 2, C→D 3, D→E 4, E→F 5 units of Y.</li>
<li>Each extra unit of X costs more Y: <b>increasing opportunity cost</b>, so the PPC is concave. Resources suited to Y are moved into X last.</li>
</ol>
<div class="note trap"><b>Handout note</b>The handout writes these as −1 … −5 (the slope). In an answer, write "the opportunity cost of the 3rd unit of X is 3 units of Y".</div>""", sec="Worked example 1 · 1.5"))

    C.append(card("we2", "Worked examples", "Straight-line PPC MCQ", "Worked example", """
<h2>Straight-line PPC: what is given up?</h2>
<p><b>Q (PPC pack Q8):</b> A PPC is a straight line from 1,000 units of Y (vertical intercept) to 2,000 units of X. The economy produces 1,200 X on the PPC. How much Y has it given up?</p>
<ol class="steps">
<li>Find the constant opportunity cost: 1,000 Y ÷ 2,000 X = <b>0.5 Y per unit of X</b>.</li>
<li>Y given up for 1,200 X: 1,200 × 0.5 = <b>600 Y</b>.</li>
<li>Check: it still produces 1,000 − 600 = 400 Y.</li>
<li>Answer <b>600</b>. The trap option is 400: that's what it still makes, not what it gave up.</li>
</ol>""", sec="Worked example 2 · 1.5"))

    C.append(card("we3", "Worked examples", "4-mark opportunity cost", "Worked example", """
<h2>Apply opportunity cost to a government [4]</h2>
<p><b>Q:</b> Malaysia's government has RM2 billion for either targeted fuel subsidies or new rural clinics. Explain opportunity cost using this example and say why it applies even though the government can borrow.</p>
<ol class="steps">
<li><b>Define [1]:</b> opportunity cost is the benefit of the next best alternative forgone.</li>
<li><b>Apply [1]:</b> if clinics are first priority, the opportunity cost is the benefit the fuel subsidy would have given (lower transport costs for households).</li>
<li><b>One alternative [1]:</b> it is that one next-best option, not every possible use of RM2 billion.</li>
<li><b>Borrowing [1]:</b> borrowed funds must be repaid from future taxes, so future spending is forgone; and the doctors, builders and land used for clinics can't be used elsewhere at the same time.</li>
</ol>""", sec="Worked example 3 · 1.1"))

    C.append(card("we4", "Worked examples", "8-mark plan: the beach", "Worked example", """
<h2>Is a beach a public good? [8]</h2>
<p><b>Q:</b> Explain the difference between a public good and a private good and consider the extent to which a beach could be described as a public good.</p>
<ol class="steps">
<li><b>AO1:</b> define rival/non-rival and excludable/non-excludable.</li>
<li><b>AO1:</b> apply: national defence (non-rival, non-excludable) vs nasi goreng (rival, excludable). Free rider → market provides no public goods.</li>
<li><b>AO2:</b> a quiet public beach (Port Dickson on a weekday) is largely non-rival and hard to fence off: close to a public good.</li>
<li><b>AO2:</b> but when crowded it becomes rival, and a resort-owned beach in Langkawi with entry fees is excludable: like a private good.</li>
<li><b>AO3:</b> it doesn't fully meet both criteria. The extent depends on congestion and ownership. Judgement: a <b>quasi-public good</b>.</li>
</ol>""", sec="Worked example 4 · 1.6 · Paper 2"))

    # ---------- exam technique ----------
    C.append(card("ex1", "Exam technique", "How essays are marked", "Exam", """
<h2>Turning Chapter 1 into essay marks</h2>
<div class="two">
<div><h4>AO1 · Knowledge</h4><p>Precise definitions, correct terms, an accurate fully labelled diagram.</p></div>
<div><h4 class="t">AO2 · Analysis</h4><p>Developed chains linking cause to effect, using the diagram.</p></div>
<div><h4 class="g">AO3 · Evaluation</h4><p>Say what the outcome depends on and why, then a justified conclusion that answers the exact question.</p></div>
</div>
<div class="tw"><table><tr><th>Part</th><th>Marking</th></tr>
<tr><td class="k">(a) 8 marks<br><span class="mono">Explain… and consider…</span></td><td>Point-based: AO1 3 · AO2 3 · AO3 2. One AO3 mark is reserved for a justified conclusion.</td></tr>
<tr><td class="k">(b) 12 marks<br><span class="mono">Assess…</span></td><td>Levels: AO1+AO2 /8 (L3 6–8, L2 3–5, L1 1–2) and AO3 /4. <b>A one-sided answer gets 0 for AO3.</b></td></tr></table></div>
<h3>Skeletons</h3>
<div class="two">
<div><h4>8-marker · ~20 min</h4><ul><li>Define every key term</li><li>Diagram with named axes, referred to</li><li>2–3 linked points from the diagram</li><li>One specific "however" + a one-line conclusion</li></ul></div>
<div><h4>12-marker · ~30 min</h4><ul><li>Intro: define, say what it depends on</li><li>Side 1: 2–3 developed chains</li><li>Side 2: 2–3 chains against</li><li>Weigh: which matters more, when, for whom</li><li>Conclusion answering the exact words</li></ul></div>
</div>
<p class="lede" style="font-size:15px">Paper 2 is 1 h 45 min for 40 marks: about 2.5 minutes per mark.</p>""", sec="Paper 2 · Exam technique"))

    C.append(card("ex2", "Exam technique", "Analysis chains & evaluation", "Exam", """
<h2>Build chains, then weigh them</h2>
<div class="two">
<div><h4 class="r">Weak · L1 assertion</h4><p>"Free markets cause pollution."</p></div>
<div><h4 class="g">Strong · L3 chain</h4><p>Firms maximise profit, so they ignore costs imposed on third parties such as river pollution from palm oil mills. Because external costs aren't in the price, output is above the social optimum: resources are over-allocated.</p></div>
</div>
<h3>Evaluation bank: "it depends on…"</h3>
<div class="tw wide"><table><tr><th>Topic</th><th>It depends on…</th><th>Because…</th></tr>
<tr><td class="k">PPC shape</td><td>How specialised resources are</td><td>Specialised resources lose a lot of output when moved, so OC rises</td></tr>
<tr><td class="k">PPC shifts</td><td>Time lags; quality vs quantity</td><td>Investment shifts the PPC only after a lag; more workers help only if employed and skilled</td></tr>
<tr><td class="k">Free markets</td><td>Competition, information, externalities, type of good</td><td>Markets work for private goods; fail for public, merit, demerit goods</td></tr>
<tr><td class="k">Intervention</td><td>Risk of government failure</td><td>Bureaucracy, poor information and tax's opportunity cost can make it worse</td></tr>
<tr><td class="k">Merit goods</td><td>Cause of under-consumption</td><td>Information failure → campaigns; low income → subsidies or free provision</td></tr>
<tr><td class="k">Transition</td><td>Speed of reform</td><td>Shock therapy hurts in SR, may help LR; China vs Russia</td></tr>
<tr><td class="k">Any "should"</td><td>Value judgements</td><td>Efficiency vs equity is normative; say whose priorities you use</td></tr></table></div>""", sec="Paper 2 · Exam technique"))

    C.append(card("mist", "Exam technique", "Common mistakes", "Mistakes", """
<h2>Common examiner-report errors</h2>
<ul>
<li>Axes labelled X and Y, or "good A / good B", when the question names the goods.</li>
<li>Saying unemployment shifts the PPC inward. It moves the economy <b>inside</b> the curve.</li>
<li>Calling opportunity cost the money price, or listing all alternatives instead of the next best.</li>
<li>Calling money "capital", or a merit good a public good.</li>
<li>Defining a public good as "provided by the government". Use non-excludable and non-rival.</li>
<li>Listing advantages and disadvantages without explaining any (stuck at L1–L2).</li>
<li>A conclusion that doesn't answer the question. If it asks "always", say "not always" and when.</li>
<li>One-sided 12-mark answers: AO3 = 0.</li>
</ul>
<div class="note tip"><b>Command words</b><b>Explain</b>: definition + chain + diagram, not a list. <b>Consider</b>: one reasoned "however" + a one-line judgement. <b>Assess</b>: both sides weighed, then a conclusion that answers "always?", "only?", "whether?".</div>""", sec="Paper 2 · Mistakes"))

    # ---------- practice ----------
    C.append(card("pr1", "Practice", "Practice: Paper 1 style", "Practice", """
<h2>Practice questions · Paper 1 style</h2>
<button class="btn" type="button" data-revealall>Reveal all answers</button>
<div class="pq"><div class="qh"><span>Q1 · 1.2</span><span class="mk">[1]</span></div>
<p class="qt">Which is a normative statement? (A) If firms spend more on advertising, sales may not rise. (B) If firms raise prices, profits will rise. (C) The government should reduce taxes on spending so that economic welfare will rise. (D) Export volumes will rise if the government lowers the exchange rate.</p>
<div class="ans"><b>C</b>"Should" signals a value judgement. A, B and D are cause-and-effect claims that can be tested, even if false.</div></div>
<div class="pq"><div class="qh"><span>Q2 · 1.3</span><span class="mk">[1]</span></div>
<p class="qt">Meera finished art college and starts a business making clay figures. Which factors of production must she buy from other businesses?</p>
<div class="ans"><b>Land and capital</b>She supplies her own labour (artistic skill) and enterprise (organising, taking the risk). She rents premises and buys clay (land) and a kiln and tools (capital).</div></div>
<div class="pq"><div class="qh"><span>Q3 · 1.4</span><span class="mk">[1]</span></div>
<p class="qt">A country moving from a planned to a market economy sells its transport services to private firms. Most likely consequence? (A) Government ownership increases. (B) Public sector services increase. (C) Central planning increases. (D) Consumer sovereignty increases.</p>
<div class="ans"><b>D</b>Privatisation moves allocation from planners to the price mechanism, so consumer spending decides what firms provide.</div></div>
<div class="pq"><div class="qh"><span>Q4 · 1.5</span><span class="mk">[1]</span></div>
<p class="qt">A PPC for capital and consumer goods shifts inward. Which could have caused it? (A) A rise in the retirement age. (B) More investment. (C) More net emigration. (D) Technological progress.</p>
<div class="ans"><b>C</b>Net emigration cuts the quantity of labour, so productive capacity falls. A, B and D shift the PPC outward.</div></div>""", sec="Practice · 1.2–1.5"))

    C.append(card("pr2", "Practice", "Practice: essay plans", "Practice", """
<h2>Practice · Paper 2 essays</h2>
<p class="lede">Plan each in 5 minutes, then compare.</p>
<div class="pq"><div class="qh"><span>Q5 · 1.5</span><span class="mk">[8]</span></div>
<p class="qt">With the help of a PPC diagram, explain the difference between actual and potential economic growth and consider whether an economy should devote more resources to capital goods.</p>
<div class="ans"><b>Plan</b>Define both; PPC with U → V (actual, zero OC) and PPC1 → PPC2 (potential). More capital goods: less consumption now, faster outward shift later. Consider: depends on time preference (normative) and whether the capital is productive; a poor economy may not afford lower consumption now.</div></div>
<div class="pq"><div class="qh"><span>Q6 · 1.3</span><span class="mk">[8]</span></div>
<p class="qt">Explain how the division of labour can increase productivity and consider whether it always benefits a firm.</p>
<div class="ans"><b>Plan</b>Define; pin factory; expertise, no switching time, machinery. Consider: needs a large market for high volume; monotony and strikes can cut productivity; narrow skills. Conclude: benefits a firm with high volume and repetitive tasks, less so for small or creative output.</div></div>
<div class="pq"><div class="qh"><span>Q7 · 1.4</span><span class="mk">[12]</span></div>
<p class="qt">Assess whether a planned economy is more likely than a market economy to achieve a fair distribution of resources.</p>
<div class="ans"><b>Plan</b>"Fair" is normative: define it (equality of outcome vs reward for effort). For: state distributes evenly, rations essentials, provides merit goods. Against: planning errors cause shortages, so fairness on paper isn't delivered; corruption favours insiders; mixed economies redistribute via tax and welfare while keeping incentives. Judge: planned systems aim at equal outcomes but often fail to deliver them; a mixed economy is more likely to achieve a fair <i>and</i> efficient result.</div></div>
<div class="pq"><div class="qh"><span>Q8 · 1.6</span><span class="mk">[12]</span></div>
<p class="qt">Assess whether governments should provide merit goods free of charge.</p>
<div class="ans"><b>Plan</b>For: information failure and positive externalities mean under-consumption; free provision raises use and equity. Against: zero price → over-use and waiting lists; tax cost and its opportunity cost; government failure. Evaluate: depends on cause (information → campaigns may be enough; low income → subsidies or free provision). Judge with the cause in mind.</div></div>""", sec="Practice · Paper 2"))

    C.append(card("pp", "Practice", "Past paper questions", "Past papers", f"""
<h2>Real 9708 questions on Chapter 1</h2>
<div class="tw wide"><table><tr><th>Paper</th><th>Question</th><th class="n">Marks</th></tr>
<tr><td class="k">21 M/J 2020 Q2(a)</td><td>With a PPC diagram, explain why scarcity makes choice inevitable for <b>firms</b> and how each choice has an opportunity cost.</td><td class="n">8</td></tr>
<tr><td class="k">21 M/J 2020 Q2(b)</td><td>Discuss the view that the only goods a government should produce are public goods.</td><td class="n">12</td></tr>
<tr><td class="k">21 M/J 2020 Q1(c)</td><td>Explain the contribution of the factor enterprise to the transformation of Lagos.</td><td class="n">4</td></tr>
<tr><td class="k">21 M/J 2020 Q1(e)</td><td>Discuss whether intervention to encourage private firms in a mixed economy is always likely to succeed.</td><td class="n">6</td></tr>
<tr><td class="k">22 M/J 2018 Q2(a)</td><td>How resources are allocated in a free market vs a mixed economy (topic from mark scheme).</td><td class="n">8</td></tr></table></div>
<div class="note trap"><b>2020 Q2(a) trap</b>It says <b>firms</b>, so draw a firm's PPC with two of its own products (tables and chairs), not capital vs consumer goods.</div>
<div class="note link"><b>Model essays</b>Five full model answers with mark highlighting are in your original notes deck. <a href="{ORIG}" target="_blank" rel="noopener">Open the full Chapter 1 notes</a></div>""", sec="Practice · Past papers"))

    C.append(card("sum", "Summary", "One-page summary", "Summary", """
<h2>Chapter 1 on one card</h2>
<div class="tw"><table>
<tr><td class="k">Scarcity</td><td>Finite resources, unlimited wants</td></tr>
<tr><td class="k">Opportunity cost</td><td>Benefit of the <b>next best</b> alternative forgone</td></tr>
<tr><td class="k">3 questions</td><td>What · How · For whom</td></tr>
<tr><td class="k">Positive / normative</td><td>Testable / value judgement ("should")</td></tr>
<tr><td class="k">Ceteris paribus</td><td>All other things equal</td></tr>
<tr><td class="k">SR / LR / VLR</td><td>≥1 factor fixed / all variable / + technology &amp; attitudes</td></tr>
<tr><td class="k">Factor rewards</td><td>Land–rent · Labour–wages · Capital–interest · Enterprise–profit</td></tr>
<tr><td class="k">Systems</td><td>Market (price) · Planned (state) · Mixed (both)</td></tr>
<tr><td class="k">PPC assumptions</td><td>Full employment · fixed resources · fixed tech · 2 goods</td></tr>
<tr><td class="k">PPC OC</td><td>Y given up ÷ X gained; concave = rising OC</td></tr>
<tr><td class="k">Shift vs move</td><td>Resources/tech shift it; unemployment = point inside</td></tr>
<tr><td class="k">Public good</td><td>Non-rival + non-excludable → free rider → missing market</td></tr>
<tr><td class="k">Merit / demerit</td><td>Under / over-consumed due to information failure</td></tr>
<tr><td class="k">Essay marks</td><td>(a) 3/3/2 points · (b) 8 + 4 levels; one-sided = 0 AO3</td></tr>
</table></div>
<p class="lede" style="font-size:15px">Screenshot this card for quick revision. Then open <b>Cards</b> or <b>Quiz</b> at the top.</p>""", sec="Summary"))
    return C


QUIZ = [
 {"s":"PPC pack Q1","q":"A country's PPC for capital and consumer goods shifts inward. What could have caused this?","o":["A rise in the retirement age","An increase in investment","An increase in net emigration","A rise in technological progress"],"c":2,"e":"Net emigration shrinks the labour force, so productive capacity falls. A, B and D add to the quantity or quality of resources and shift the PPC outward."},
 {"s":"PPC pack Q5","q":"An economy's PPC for capital goods (vertical) and consumer goods (horizontal) is bowed outward. Which statement explains this shape?","o":["More efficient workers are drawn away from consumer goods","Resources cannot be switched between capital and consumer goods","The economy is more efficient at producing capital goods","The opportunity cost of capital goods increases the more capital goods are made"],"c":3,"e":"A concave PPC means increasing opportunity cost. B is wrong because the downward slope shows resources can be switched. C can't be read from the diagram, which shows no costs."},
 {"s":"PPC pack Q8","q":"A straight-line PPC runs from 1,000 units of Y (vertical intercept) to 2,000 units of X. The economy produces 1,200 X on the PPC. How much Y has it given up?","o":["400","600","800","1,000"],"c":1,"e":"Each X costs 0.5 Y. 1,200 × 0.5 = 600 Y given up; it still makes 400 Y. The trap is A."},
 {"s":"PPC pack Q7","q":"An economy's PPC is LM. What might cause it to shift inward to NP?","o":["A higher retirement age","A reallocation of resources","The depletion of natural resources","The underemployment of resources"],"c":2,"e":"Fewer natural resources reduce capacity. A shifts the PPC out; B is a movement along it; D is a point inside it."},
 {"s":"PPC pack Q6","q":"Good X is more labour-intensive than good Y. A law reduces working hours. What happens to the PPC?","o":["It shifts inward equally on both axes","It shifts inward, with maximum X falling proportionally more than Y","It shifts inward, with maximum Y falling proportionally more than X","It does not move; the economy moves inside it"],"c":1,"e":"Less labour cuts capacity for both goods, more so for the labour-intensive X. D is wrong: the law reduces the quantity of labour available."},
 {"s":"PPC pack Q10","q":"A country at P on its PPC (consumer vs military goods) prepares for war; the war then destroys much of its infrastructure. Which sequence fits?","o":["Movement towards consumer goods, then an outward shift","Movement towards military goods, then an inward shift","Inward shift, then a movement towards military goods","Movement inside the PPC, then an outward shift"],"c":1,"e":"Preparing for war reallocates resources (movement along). Destroying infrastructure reduces capital (inward shift)."},
 {"s":"PPC pack Q4","q":"A straight-line PPC in Year 2 lies inside and parallel to the Year 1 PPC. What can be concluded?","o":["Cost of production was lower in Year 2","Full-employment output was lower in Year 2","Opportunity cost was lower in Year 2","Unemployment rose between the years"],"c":1,"e":"Every point on a PPC is full-employment output, so potential output fell. Parallel lines have the same OC; unemployment is a point inside, not a shift."},
 {"s":"Systems Q1","q":"What is likely to be greater in a planned economy than in a market economy?","o":["Efficiency","Flexibility","Innovation","Stability"],"c":3,"e":"The state controls output, prices and jobs, so it can offer more stability. The others are market strengths."},
 {"s":"Systems Q4","q":"In a market economy, what determines the allocation of factors of production?","o":["Companies' market share","The needs of the country","The pattern of consumers' spending","The wealth of entrepreneurs"],"c":2,"e":"Consumer sovereignty: spending changes prices and profits, pulling factors into favoured industries."},
 {"s":"Systems Q5","q":"What is an essential feature of a pure market economy?","o":["Buyers and sellers have perfect knowledge","External costs are taxed","Prices respond to the demands of consumers","The government provides public goods"],"c":2,"e":"The price mechanism defines a market economy. B and D are government intervention; perfect knowledge isn't required."},
 {"s":"Systems Q6","q":"What is the defining characteristic of a mixed economy?","o":["Resources are allocated partly by the state and partly by producers and consumers","It has both monopolies and competitive industries","It has features of both developed and developing economies","It produces both agricultural and industrial goods"],"c":0,"e":"\"Mixed\" refers to the method of allocation: price mechanism plus government planning."},
 {"s":"Systems Q3","q":"What are most likely to be disadvantages of a market economy?","o":["Economic growth and state-owned companies","Merit goods and free competition","Public goods and economic specialisation","Unemployment and external costs"],"c":3,"e":"Markets don't guarantee full employment and ignore external costs. The rest are advantages or belong to other systems."},
 {"s":"Systems Q7","q":"Which country has achieved most indicators of a successful transition? (prices / exchange rate / stock exchange / inward investment)","o":["Administered / managed / yes / allowed","Administered / floating / no / controlled","Liberalised / floating / no / allowed","Liberalised / managed / yes / controlled"],"c":2,"e":"Market indicators: liberalised prices, floating rate, a stock exchange, allowed FDI. C has three of four."},
 {"s":"Systems Q10","q":"Which change in system brings the greatest rise in unemployment with the greatest fall in regulation?","o":["Market to mixed","Mixed to planned","Planned to market","Planned to mixed"],"c":2,"e":"Planned to market removes the most regulation, and state firms kept open regardless of demand close or shed labour."},
 {"s":"Systems Q8","q":"In which types of economy might a government control prices?","o":["Market and mixed only","Market and planned only","Market, mixed and planned","Mixed and planned only"],"c":3,"e":"Price controls are intervention: central to planned, selective in mixed. A pure market leaves prices to demand and supply."},
 {"s":"Factors Q2","q":"What is the income received by the factor enterprise called?","o":["Capital","Interest","Profit","Revenue"],"c":2,"e":"Land–rent, labour–wages, capital–interest, enterprise–profit. Revenue is sales income."},
 {"s":"Factors Q5","q":"Which factor and example are correctly linked?","o":["Capital: $10,000 in a savings account","Enterprise: a company accountant","Labour: a robot","Land: the flow of a river"],"c":3,"e":"A river's flow is a natural resource. Money isn't capital, an accountant is labour, a robot is capital."},
 {"s":"Factors Q4","q":"Which action would NOT be an action of the factor labour?","o":["Leaving college to work on the land","Moving to a capital-intensive industry to work","Setting up a new IT business","Taking a computer-skills course"],"c":2,"e":"Setting up a business means organising and taking risk: enterprise."},
 {"s":"Methodology Q1","q":"\"A positive statement is ..(1).. and ..(2).. be tested; a normative statement is ..(3).. and ..(4).. be tested.\"","o":["objective / can / subjective / cannot","objective / cannot / subjective / can","subjective / can / objective / cannot","subjective / cannot / objective / can"],"c":0,"e":"Positive = objective and testable; normative = subjective and untestable."},
 {"s":"Methodology Q2","q":"A government subsidises milk farms. Which question is normative?","o":["How much will milk production increase?","How should essential products such as milk be produced?","How will employment in the milk industry change?","How will milk prices change?"],"c":1,"e":"\"Should\" asks for a value judgement; the others ask about measurable effects."},
 {"s":"Classification","q":"Which is a free good in the economic sense?","o":["Seawater on a remote coastline","A toy given away in a cereal box","Free treatment at a government clinic","Free Wi-Fi in a café"],"c":0,"e":"A free good uses no scarce resources. The toy, clinic and Wi-Fi all have an opportunity cost."},
 {"s":"Classification","q":"Why is a vaccination programme a merit good rather than a public good?","o":["It is provided by the government","It creates external costs","It is rival and excludable, but under-consumed due to information failure","It is non-rival and non-excludable"],"c":2,"e":"A dose given to one person can't go to another and non-payers can be refused. It's under-consumed because people underestimate its benefits."},
]
