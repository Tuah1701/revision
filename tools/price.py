"""9708 Chapter 2 · The price system (merges Price System deck, Functions of Price, Four Elasticities)."""
import pathlib, json
import engine
from engine import card
from diagrams import Fig, fig

ORIG = "https://claude.ai/code/artifact/5dbc6cca-15c2-4658-bb6a-db0c7688855f"
ORIG_FN = "https://claude.ai/code/artifact/5fbf385c-b27a-4d56-b85f-f4593065026c"
ORIG_EL = "https://claude.ai/code/artifact/58d9ef5b-30f1-4508-84f8-7ae4e8276858"


def at_y(a, b, y):
    return a[0] + (y - a[1]) * (b[0] - a[0]) / (b[1] - a[1])


# ---------- diagrams ----------
D = ((1, 9.5), (9, 1))
mv = Fig(aria="Movement along the demand curve")
mv.line(*D, "d", "D", off=(4, 14))
A = (at_y(*D, 6.5), 6.5); B = (at_y(*D, 3.5), 3.5)
mv.guide(A, "Q1", "P1").guide(B, "Q2", "P2").pt(A, "A").pt(B, "B").arrow((A[0] + .35, A[1] - .2), (B[0] - .25, B[1] + .45))
D1 = ((3.5, 9.5), (10, 2.6))
sh = Fig(aria="Shift of demand from D0 to D1")
sh.line(*D, "o", "D0", off=(4, 14)).line(*D1, "d", "D1", off=(-6, 14), anchor="end")
p0 = (at_y(*D, 5), 5); p1 = (at_y(*D1, 5), 5)
sh.guide(p0, "Q0", "P0").guide(p1, "Q1").pt(p0).pt(p1).arrow((p0[0] + .3, 5), (p1[0] - .3, 5))
FIG_MOVE = fig(("Own price changes · movement", mv), ("Non-price factor · shift", sh))

sp = Fig(aria="Specific tax: parallel upward shift of supply")
sp.line((1, 1), (9, 7), "s", "S", off=(4, 4)).line((1, 3), (9, 9), "b", "S + tax", off=(-4, -6), anchor="end")
sp.arrow((5, 4.1), (5, 5.9)).text((5.2, 5), "$2", "t-pt", off=(4, 4))
av = Fig(aria="Ad valorem tax: supply pivots, gap widens as price rises")
av.line((1, 1), (8, 6), "s", "S", off=(4, 4)).line((1, 1.3), (8, 7.8), "b", "S + tax", off=(-4, -6), anchor="end")
av.arrow((3, 2.45), (3, 3.1)).arrow((7, 5.3), (7, 6.85))
FIG_TAX = fig(("Specific (unit) tax", sp), ("Ad valorem tax", av))

eq = Fig(aria="Equilibrium with excess supply above and excess demand below")
eq.line((1, 9), (9, 1), "d", "D", off=(4, 14)).line((1, 1), (9, 9), "s", "S", off=(4, -2))
eq.guide((5, 5), "Q*", "P*").pt((5, 5), "E", off=(9, 4))
eq.path([(0, 7), (7, 7)], "o").text((5, 7), "excess supply", "t-sm", off=(0, -6), anchor="middle")
eq.path([(0, 3), (7, 3)], "o").text((5, 3), "excess demand", "t-sm", off=(0, 14), anchor="middle")
FIG_EQ = fig(eq, caption="Above P* sellers can't sell all they make, so price falls. Below P* buyers bid price up. Price settles at E where Qd = Qs.")

Di = ((3.5, 10), (6, 0))
ti = Fig(aria="Inelastic demand: revenue gained exceeds revenue lost after a price rise")
q4, q6 = at_y(*Di, 4), at_y(*Di, 6)
ti.poly([(0, 4), (0, 6), (q6, 6), (q6, 4)], "fb").poly([(q6, 0), (q6, 4), (q4, 4), (q4, 0)], "fc")
ti.line(*Di, "d", "D", off=(6, -2)).guide((q6, 6), None, "P1").guide((q4, 4), None, "P0")
De = ((0, 7), (10, 2))
te = Fig(aria="Elastic demand: revenue lost exceeds revenue gained after a price rise")
e4, e5 = at_y(*De, 4), at_y(*De, 5)
te.poly([(0, 4), (0, 5), (e5, 5), (e5, 4)], "fb").poly([(e5, 0), (e5, 4), (e4, 4), (e4, 0)], "fc")
te.line(*De, "d", "D", off=(-4, -8), anchor="end").guide((e5, 5), None, "P1").guide((e4, 4), None, "P0")
FIG_TR = fig(("Inelastic · TR rises", ti), ("Elastic · TR falls", te),
             caption="Teal: revenue gained on units still sold at the higher price. Red: revenue lost on units no longer sold.")

cs = Fig(aria="Consumer and producer surplus at equilibrium")
cs.poly([(0, 9), (0, 5), (4, 5)], "fa").poly([(0, 5), (4, 5), (0, 1)], "fb")
cs.line((0, 9), (9, 0), "d", "D", off=(-4, -6), anchor="end").line((0, 1), (8, 9), "s", "S", off=(4, 4))
cs.guide((4, 5), "Q*", "P*").pt((4, 5), "E", off=(8, 4))
cs.text((1.2, 6.2), "CS", "t-pt").text((1.2, 3.5), "PS", "t-pt")
FIG_CS = fig(cs, caption="CS: below demand, above price. PS: above supply, below price. Total welfare CS + PS is maximised at the free-market equilibrium.")

ra = Fig(aria="Rationing: supply falls, price rises, movement up demand")
ra.line((1, 9), (9, 1), "d", "D", off=(4, 14)).line((2, 1), (10, 9), "o", "S1", off=(-4, -6), anchor="end").line((0, 1), (8, 9), "s", "S2", off=(-4, -6), anchor="end")
ra.guide((5.5, 4.5), "B", "P1").guide((4.5, 5.5), "A", "P2").pt((5.5, 4.5)).pt((4.5, 5.5))
inc = Fig(aria="Incentive: demand rises, price rises, movement up supply")
inc.line((1, 1), (9, 9), "s", "S", off=(4, -2)).line((0, 9), (9, 0), "o", "D1", off=(-4, -6), anchor="end").line((1, 10), (10, 1), "d", "D2", off=(-4, -6), anchor="end")
inc.guide((4.5, 4.5), "A", "P1").guide((5.5, 5.5), "B", "P2").pt((4.5, 4.5)).pt((5.5, 5.5))
FIG_FN = fig(("Rationing", ra), ("Incentive", inc),
             caption="Left: supply falls, price rises, quantity demanded contracts from OB to OA (movement up D). Right: demand rises, price rises, quantity supplied extends from OA to OB (movement up S). In both, the price change is the signal.")


def build():
    C = []
    C.append(card("cover", "Start", "The price system", "Cover", """
<p class="sec" style="margin:0">CAIE 9708 · AS Level · Chapter 2</p>
<p class="cover-k">Ch2</p>
<h1>The price system: demand, supply &amp; elasticity</h1>
<p class="lede">Built from Puan Zaihan's 11 Chapter 2 handouts, plus your Functions of Price and Four Elasticities pages.</p>
<div class="stat"><div><b>5</b>topic blocks</div><div><b>6</b>worked examples</div><div><b>57</b>flashcards</div><div><b>20</b>quiz questions</div></div>
<p class="swipehint">Swipe left to start. Tap ☰ for contents.</p>
<p><a href="https://claude.ai/artifact/3MqyaRKgJG7ufb65fwrnoF" target="_blank" rel="noopener">Open Revision Hub</a></p>""", sec="Start"))

    C.append(card("big", "Start", "The big picture", "Overview", """
<h2>How Chapter 2 fits together</h2>
<p>Every topic here is one of three things: <b>what moves a curve</b>, <b>what happens to price and quantity</b> when it moves, or <b>how strongly something responds</b>. Draw the diagram and say how big the effect is, and you can answer almost any question.</p>
<div class="toc-mini">
<button type="button" data-goto="dem"><b>2.1–2.2</b><span>Demand &amp; supply</span></button>
<button type="button" data-goto="eq"><b>2.4</b><span>Market equilibrium</span></button>
<button type="button" data-goto="el0"><b>2.3</b><span>Elasticities: PED, PES, YED, XED</span></button>
<button type="button" data-goto="cs"><b>2.5</b><span>Consumer &amp; producer surplus</span></button>
<button type="button" data-goto="rel"><b>2.4.3–4</b><span>Related markets &amp; price mechanism</span></button>
<button type="button" data-goto="ex1"><b>P2</b><span>Turning notes into marks</span></button>
</div>
<div class="tw"><table><tr><th>Paper</th><th>How Chapter 2 is tested</th></tr>
<tr><td class="k">Paper 1</td><td>Which point is the new equilibrium? Shift vs movement traps, elasticity calculations, related-market chains.</td></tr>
<tr><td class="k">Paper 2 A</td><td>Calculate a % change or elasticity from a table, explain a price change with a diagram, judge a claim.</td></tr>
<tr><td class="k">Paper 2 B</td><td>(a) explain with a diagram or formula and "consider"; (b) "assess". Recent: CS/PS, wage rise, XED, PES, buffer stocks.</td></tr></table></div>""", sec="Overview"))

    # ---------- demand & supply ----------
    C.append(card("dem", "Demand & supply", "Demand: movement vs shift", "Concept", f"""
<h2>Demand</h2>
<div class="def"><span class="lab">Definition · Demand <i>2.1.1</i></span><p>The quantity consumers are <b>willing and able</b> to buy at different prices per period, ceteris paribus. "Able" makes it <b>effective demand</b>: desire backed by ability to pay.</p></div>
<p><b>Law of demand:</b> higher price → lower quantity demanded (inverse relationship). Market demand is the horizontal sum of individual demand curves.</p>
{FIG_MOVE}
<div class="tw"><table><tr><th>Change in…</th><th>Effect</th><th>Language</th></tr>
<tr><td class="k">Own price</td><td>Movement along D</td><td>"Change in <b>quantity demanded</b>": expansion / contraction</td></tr>
<tr><td class="k">Anything else</td><td>Shift of D</td><td>"<b>Increase / decrease in demand</b>": right / left</td></tr></table></div>""", sec="2.1 · Demand"))

    C.append(card("dem2", "Demand & supply", "What shifts demand", "Concept", """
<h2>Non-price determinants of demand</h2>
<div class="two">
<div><h4>1 · Related goods</h4><p><b>Substitutes</b> (Coke/Pepsi): coffee price ↑ → tea demand ↑. <b>Complements</b> (car/petrol): petrol price ↓ → car demand ↑.</p></div>
<div><h4>2 · Income</h4><p><b>Normal</b>: income ↑ → demand ↑. <b>Inferior</b>: income ↑ → demand ↓ (bus tickets, second-hand clothes).</p></div>
<div><h4>3 · Expected price</h4><p>Expect a price rise (milk powder) → stock up now → demand shifts right, usually temporarily.</p></div>
<div><h4>4 · Tastes</h4><p>Advertising or a trend raises demand; a health scare lowers it.</p></div>
<div><h4>5 · Government</h4><p>Laws (compulsory seat belts). Higher income tax → lower disposable income → normal goods ↓, inferior ↑.</p></div>
<div><h4>Also accepted</h4><p>Population size and age structure, credit availability, seasons.</p></div>
</div>
<h3>Exceptional upward-sloping demand</h3>
<div class="two">
<div><h4 class="t">Veblen goods</h4><p>Status goods (diamonds, luxury watches): a higher price signals prestige, so quantity demanded can rise.</p></div>
<div><h4 class="t">Giffen goods</h4><p>Highly inferior staples taking a large share of poor households' income (broken rice). A price rise makes better food unaffordable, so they buy more of the staple.</p></div>
</div>""", sec="2.1 · Syllabus 2.1.2–2.1.3"))

    C.append(card("sup", "Demand & supply", "Supply and what shifts it", "Concept", """
<h2>Supply</h2>
<div class="def"><span class="lab">Definition · Supply <i>2.2</i></span><p>The quantity producers are willing and able to sell at various prices per period, ceteris paribus.</p></div>
<p><b>Law of supply:</b> higher price → higher quantity supplied, because production is more profitable and covers rising marginal cost. Price ↑ → <b>expansion</b>; price ↓ → <b>contraction</b>.</p>
<div class="tw wide"><table><tr><th>Factor</th><th>Example</th><th>Shift</th></tr>
<tr><td class="k">Costs of production</td><td>Wages rise</td><td>S left</td></tr>
<tr><td class="k">Technology</td><td>Automation → lower MC</td><td>S right</td></tr>
<tr><td class="k">Indirect tax</td><td>$2 per unit</td><td>S up/left by $2</td></tr>
<tr><td class="k">Subsidy</td><td>$2 per unit to producers</td><td>S down/right by $2</td></tr>
<tr><td class="k">Joint supply</td><td>Beef price ↑ → more cattle slaughtered</td><td>Leather S right</td></tr>
<tr><td class="k">Competitive supply</td><td>Orange price ↑ → land moves from lemons</td><td>Lemon S left</td></tr>
<tr><td class="k">Expected price</td><td>Expect rise → hold stock back</td><td>S left today</td></tr>
<tr><td class="k">Number of firms</td><td>New firms enter</td><td>S right</td></tr>
<tr><td class="k">Nature</td><td>Floods, disease</td><td>S left</td></tr></table></div>""", sec="2.2 · Supply"))

    C.append(card("tax", "Demand & supply", "Specific vs ad valorem tax", "Concept", f"""
<h2>How taxes move supply</h2>
{FIG_TAX}
<div class="two">
<div><h4 class="r">Specific (unit) tax</h4><p>A fixed amount per unit, e.g. $2. Supply shifts up by $2 at every quantity: a <b>parallel</b> shift.</p></div>
<div><h4 class="r">Ad valorem tax</h4><p>A percentage of price, e.g. 20% VAT. The tax per unit grows with price, so the gap <b>widens</b>: $5 → $6, $10 → $12, $30 → $36.</p></div>
</div>
<p>A subsidy is the specific-tax diagram in reverse: S shifts down by the subsidy.</p>""", sec="2.2 · Taxes & subsidies"))

    # ---------- equilibrium ----------
    C.append(card("eq", "Equilibrium", "Market equilibrium", "Concept", f"""
<h2>Market equilibrium</h2>
<div class="def"><span class="lab">Definition · Equilibrium <i>2.4</i></span><p>The price at which quantity demanded equals quantity supplied, so there is no tendency for price to change. The market clears.</p></div>
{FIG_EQ}
<div class="formula">Demand Qd = a − bP · Supply Qs = c + dP · Equilibrium: Qd = Qs</div>""", sec="2.4 · Equilibrium"))

    C.append(card("eq2", "Equilibrium", "When both curves shift", "Concept", """
<h2>When curves shift</h2>
<p>One curve shifts: both P and Q move predictably. <b>Both</b> shift: one of P or Q is certain; the other depends on the relative size of the shifts.</p>
<div class="tw wide"><table><tr><th>Change</th><th>Price</th><th>Quantity</th><th>Example</th></tr>
<tr><td class="k">D ↑ only</td><td>Rises</td><td>Rises</td><td>Income ↑, normal good</td></tr>
<tr><td class="k">D ↓ only</td><td>Falls</td><td>Falls</td><td>Income ↑, inferior good</td></tr>
<tr><td class="k">S ↑ only</td><td>Falls</td><td>Rises</td><td>Costs fall</td></tr>
<tr><td class="k">S ↓ only</td><td>Rises</td><td>Falls</td><td>Costs rise</td></tr>
<tr><td class="k">D ↑ S ↑</td><td>Depends</td><td><b>Rises</b></td><td>Cake: tastes ↑, costs ↓</td></tr>
<tr><td class="k">D ↓ S ↓</td><td>Depends</td><td><b>Falls</b></td><td>Coffee: tea cheaper, fewer sellers</td></tr>
<tr><td class="k">D ↑ S ↓</td><td><b>Rises</b></td><td>Depends</td><td>Pantene: more ads, higher costs</td></tr>
<tr><td class="k">D ↓ S ↑</td><td><b>Falls</b></td><td>Depends</td><td>Petrol demand ↓, car tech ↑</td></tr></table></div>
<div class="note tip"><b>MCQ shortcut</b>Quantity certain, price uncertain → curves shift the <b>same</b> direction. Price certain, quantity uncertain → <b>opposite</b> directions.</div>
<div class="note trap"><b>Careful</b>Some handout lines compare "the increase in price" with "the increase in quantity". You can't compare them in general; it depends on the slopes. Say which variable is certain and which depends on the relative shifts.</div>""", sec="2.4 · Shifts"))

    # ---------- elasticities ----------
    C.append(card("el0", "Elasticities", "One formula, four questions", "Concept", r"""
<h2>One formula, four questions</h2>
<p>Every elasticity answers: "If X changes by 1%, by what % does Y respond?"</p>
<div class="formula">\( E = \dfrac{\%\Delta \text{ in what responds}}{\%\Delta \text{ in what caused it}} \qquad \%\Delta = \dfrac{\text{new} - \text{original}}{\text{original}} \times 100 \)</div>
<div class="tw wide"><table><tr><th></th><th>Question it answers</th><th>Formula</th><th>On the diagram</th></tr>
<tr><td class="k">PED</td><td>If I change my price, what happens to quantity and revenue?</td><td class="mono">%ΔQd ÷ %ΔP</td><td>Movement along D</td></tr>
<tr><td class="k">PES</td><td>If price rises, how much can producers raise output?</td><td class="mono">%ΔQs ÷ %ΔP</td><td>Movement along S</td></tr>
<tr><td class="k">YED</td><td>If incomes change, what happens to demand?</td><td class="mono">%ΔQd ÷ %ΔY</td><td>Shift of D</td></tr>
<tr><td class="k">XED</td><td>If another good's price changes, what happens to mine?</td><td class="mono">%ΔQd(A) ÷ %ΔP(B)</td><td>Shift of D for A</td></tr></table></div>
<div class="note tip"><b>Memory hook</b>"<b>P</b>rice measures <b>p</b>ass along the curve; the others push it." For YED and XED the <b>sign</b> is the answer to "what type of good"; for PED and PES the <b>size</b> matters.</div>""", sec="2.3 · Elasticities"))

    C.append(card("ped", "Elasticities", "PED: values and revenue", "Concept", f"""
<h2>Price elasticity of demand</h2>
<div class="def"><span class="lab">Definition · PED</span><p>The responsiveness of quantity demanded to a change in the good's own price, ceteris paribus. Usually negative; quote the absolute value.</p></div>
<div class="tw"><table><tr><th class="n">Value</th><th>Name</th><th>Meaning</th></tr>
<tr><td class="n">0</td><td class="k">Perfectly inelastic</td><td>No quantity change; vertical</td></tr>
<tr><td class="n">0–1</td><td class="k">Inelastic</td><td>%ΔQd &lt; %ΔP (necessities, addictive)</td></tr>
<tr><td class="n">1</td><td class="k">Unitary</td><td>TR unchanged</td></tr>
<tr><td class="n">&gt;1</td><td class="k">Elastic</td><td>%ΔQd &gt; %ΔP (close substitutes, luxuries)</td></tr>
<tr><td class="n">∞</td><td class="k">Perfectly elastic</td><td>Any price rise → zero demand; horizontal</td></tr></table></div>
{FIG_TR}
<div class="tw"><table><tr><th>Demand is…</th><th>Raise price</th><th>Cut price</th></tr>
<tr><td class="k">Inelastic</td><td>TR rises</td><td>TR falls</td></tr><tr><td class="k">Elastic</td><td>TR falls</td><td>TR rises</td></tr><tr><td class="k">Unitary</td><td>TR same</td><td>TR same</td></tr></table></div>""", sec="2.3 · PED"))

    C.append(card("ped2", "Elasticities", "PED along a line; determinants", "Concept", """
<h2>PED changes along a straight line</h2>
<p>Same slope everywhere, but P/Q changes, so PED changes. Above the midpoint demand is elastic, below it inelastic; TR peaks at the midpoint.</p>
<div class="tw"><table><tr><th class="n">P ($)</th><th class="n">Qd</th><th class="n">PED</th><th class="n">TR ($)</th></tr>
<tr><td class="n">20</td><td class="n">10</td><td class="n">4</td><td class="n">200</td></tr>
<tr><td class="n">15</td><td class="n">20</td><td class="n">1.5</td><td class="n">300</td></tr>
<tr><td class="n">12.50</td><td class="n">25</td><td class="n">1</td><td class="n">312.50</td></tr>
<tr><td class="n">10</td><td class="n">30</td><td class="n">0.67</td><td class="n">300</td></tr>
<tr><td class="n">5</td><td class="n">40</td><td class="n">0.25</td><td class="n">200</td></tr></table></div>
<p class="lede" style="font-size:14.5px">Q = 50 − 2P, point PED = 2 × P/Q.</p>
<h3>Determinants of PED</h3>
<ul><li><b>Substitutes</b>: the most important; more and closer → more elastic.</li>
<li><b>Share of income</b>: a 10% rise on a $1,000 staycation matters far more than on $100 of bus fares.</li>
<li><b>Necessity vs luxury</b>: rice inelastic, luxury watches elastic.</li>
<li><b>Habit / addiction</b>: cigarettes → inelastic.</li>
<li><b>Time</b>: more elastic in the long run.</li>
<li><b>Breadth of definition</b>: food inelastic; one brand of bread elastic.</li></ul>""", sec="2.3 · PED"))

    C.append(card("ped3", "Elasticities", "Using PED", "Concept", """
<h2>Applications of PED</h2>
<div class="two">
<div><h4>Firms</h4><p>Raise price if inelastic, cut if elastic. Advertising and branding aim to make demand <b>more inelastic</b>; measuring PED afterwards shows whether it worked.</p></div>
<div><h4 class="t">Government</h4><p>Tax goods with inelastic demand for revenue. Sin taxes on cigarettes and sugary drinks raise revenue but cut consumption only a little. Subsidies change consumption most when demand is elastic.</p></div>
</div>
<p>The same tax raises more revenue when demand is inelastic, because quantity barely falls. With elastic demand quantity falls a lot and producers bear most of the tax.</p>
<div class="note tip"><b>Evaluating PED</b>Estimates rely on past data; ceteris paribus rarely holds; PED differs along the curve and over time; rivals may react; firms care about profit, not just revenue. A useful guide, not a precise forecast.</div>""", sec="2.3 · PED"))

    C.append(card("pes", "Elasticities", "PES", "Concept", """
<h2>Price elasticity of supply</h2>
<div class="def"><span class="lab">Definition · PES</span><p>The responsiveness of quantity supplied to a change in price, ceteris paribus. PES = %ΔQs ÷ %ΔP. Positive.</p></div>
<p>Straight-line supply: starts on the price axis → elastic; through the origin → unitary at every point; starts on the quantity axis → inelastic. Horizontal = perfectly elastic; vertical = perfectly inelastic.</p>
<h3>Determinants</h3>
<ul><li><b>Spare capacity</b>: idle machines and workers → elastic.</li>
<li><b>Stocks</b>: storable goods → elastic; perishables → inelastic.</li>
<li><b>Factor mobility</b>: easy to switch resources → elastic.</li>
<li><b>Time</b>: supply becomes more elastic as time passes.</li>
<li><b>Nature of the good</b>: agricultural goods low PES (growing seasons).</li></ul>
<div class="two">
<div><h4 class="g">Uses</h4><p>Firms: production planning, inventory, just-in-time. Government: low farm PES causes volatile prices → buffer stocks; infrastructure, cold storage and training raise PES.</p></div>
<div><h4 class="r">Limits</h4><p>Hard to estimate; ceteris paribus; very different SR vs LR. Rubber trees take years to mature, so higher prices can't raise supply this season.</p></div>
</div>""", sec="2.3 · PES"))

    C.append(card("yx", "Elasticities", "YED and XED", "Concept", """
<h2>Income and cross elasticity</h2>
<div class="def"><span class="lab">Definition · YED</span><p>Responsiveness of demand to a change in income, ceteris paribus. YED = %ΔQd ÷ %ΔY.</p></div>
<div class="tw"><table><tr><th class="n">YED</th><th>Type</th></tr>
<tr><td class="n">&gt; 1</td><td><b>Luxury</b> (normal): demand rises more than income</td></tr>
<tr><td class="n">0–1</td><td><b>Necessity</b> (normal): rises less than income</td></tr>
<tr><td class="n">&lt; 0</td><td><b>Inferior</b>: demand falls as income rises</td></tr></table></div>
<p><b>Firms</b> plan over the business cycle and diversify ranges (luxury, everyday, no-frills shampoo). <b>Government</b> taxes luxuries in booms; rising demand for inferior goods signals hardship. A good can switch category as a country gets richer.</p>
<div class="def"><span class="lab">Definition · XED</span><p>Responsiveness of demand for A to a change in the price of B. XED = %ΔQd(A) ÷ %ΔP(B). Sign = relationship; size = strength.</p></div>
<div class="chain"><span>−∞ close complements</span><i>·</i><span>0 unrelated</span><i>·</i><span>close substitutes +∞</span></div>
<p>Main determinant: how closely the goods meet the same need (Coke is closer to Pepsi than to mineral water). Firms watch rivals' prices and bundle complements; governments predict knock-on effects (fuel tax → public transport).</p>""", sec="2.3 · YED & XED"))

    C.append(card("elcmp", "Elasticities", "All four side by side", "Concept", """
<h2>All four, side by side</h2>
<div class="tw wide"><table><tr><th></th><th>PED</th><th>PES</th><th>YED</th><th>XED</th></tr>
<tr><td class="k">Usual sign</td><td>Negative</td><td>Positive</td><td>+ normal / − inferior</td><td>+ subs / − comps</td></tr>
<tr><td class="k">Key value</td><td>|1|</td><td>1</td><td>0 and +1</td><td>0, distance from 0</td></tr>
<tr><td class="k">Determinants</td><td>Substitutes, income share, necessity, habit, time</td><td>Spare capacity, stocks, mobility, time, nature</td><td>Necessity vs luxury, income level</td><td>Closeness of goods</td></tr>
<tr><td class="k">Most useful over</td><td>Short run (pricing)</td><td>SR and LR (capacity)</td><td>Long run / cycle</td><td>SR (rivals) and strategy</td></tr>
<tr><td class="k">Special limit</td><td>Varies along a line; ignores costs</td><td>Very different SR vs LR</td><td>Goods change category</td><td>Only related goods; not symmetrical</td></tr></table></div>
<h3>Which is most useful?</h3>
<div class="tw"><table>
<tr><td class="k">Firm setting price now</td><td>PED: links its own decision to revenue</td></tr>
<tr><td class="k">Firm planning 5 years</td><td>YED: which products grow or shrink</td></tr>
<tr><td class="k">Firm in a competitive market</td><td>XED with rivals</td></tr>
<tr><td class="k">Long production times</td><td>PES: can it exploit higher prices?</td></tr>
<tr><td class="k">Government raising tax</td><td>PED (and PES)</td></tr>
<tr><td class="k">Stabilising food prices</td><td>PES: low farm PES causes the swings</td></tr>
<tr><td class="k">Growth or recession</td><td>YED</td></tr></table></div>""", sec="2.3 · Compared"))

    # ---------- CS & PS ----------
    C.append(card("cs", "Surplus", "Consumer & producer surplus", "Concept", f"""
<h2>Consumer and producer surplus</h2>
<div class="def"><span class="lab">Consumer surplus <i>2.5</i></span><p>The difference between the maximum price consumers are willing and able to pay and the price they actually pay.</p></div>
<div class="def"><span class="lab">Producer surplus</span><p>The difference between the price producers receive and the minimum they'd accept (their marginal cost).</p></div>
{FIG_CS}
<div class="tw wide"><table><tr><th>Event</th><th>Price</th><th>CS</th><th>PS</th></tr>
<tr><td class="k">Demand ↑</td><td>↑</td><td>Usually ↑</td><td>↑</td></tr>
<tr><td class="k">Demand ↓</td><td>↓</td><td>↓</td><td>↓</td></tr>
<tr><td class="k">Supply ↑ (lower costs)</td><td>↓</td><td>↑</td><td>Usually ↑</td></tr>
<tr><td class="k">Supply ↓ (higher costs)</td><td>↑</td><td>↓</td><td>Usually ↓</td></tr></table></div>
<div class="note link"><b>Elasticity decides the CS loss</b>After the same cost rise, inelastic demand means price rises further, so consumers lose more surplus in total. This is 9708/22 M/J 2023 Q2(a).</div>""", sec="2.5 · Surplus"))

    # ---------- related markets & price mechanism ----------
    C.append(card("rel", "Price mechanism", "Related markets", "Concept", """
<h2>Relationships between markets</h2>
<p><b>Method:</b> change in market A → new price in A → shift in market B → new equilibrium in B. Draw two diagrams side by side.</p>
<div class="two">
<div><h4>Substitutes</h4><p>Coffee costs rise → coffee S left → coffee price ↑ → tea relatively cheaper → tea D right → tea P and Q rise.</p></div>
<div><h4>Complements</h4><p>New tech → washing machine S right → price ↓, Q ↑ → washing powder D right → its P and Q rise.</p></div>
<div><h4>Derived demand</h4><p>Factors are wanted for what they produce. Supermarket demand ↑ → demand for supermarket workers ↑ → wages and jobs rise.</p></div>
<div><h4>Joint supply</h4><p>Two goods from one process. Beef demand ↑ → more beef → leather S right → leather price ↓, quantity ↑.</p></div>
</div>""", sec="2.4.3 · Related markets"))

    C.append(card("fn", "Price mechanism", "Three functions of price", "Concept", f"""
<h2>Rationing, signalling, incentive</h2>
<div class="def"><span class="lab">Price mechanism <i>2.4.4</i></span><p>Demand and supply set prices, and changes in those prices allocate scarce resources between competing uses, without central direction.</p></div>
<div class="tw"><table><tr><th>Function</th><th>Answers</th><th>Acts on</th><th>On the diagram</th></tr>
<tr><td class="k">Signalling</td><td>What</td><td>Both</td><td>The change in P itself</td></tr>
<tr><td class="k">Incentive</td><td>How much</td><td>Mainly producers</td><td>Movement along S</td></tr>
<tr><td class="k">Rationing</td><td>For whom</td><td>Consumers</td><td>Movement along D</td></tr></table></div>
{FIG_FN}
<p><b>Transmission of preferences:</b> consumers "vote" with spending; the price change passes their wants to producers automatically.</p>
<div class="note trap"><b>Common error</b>The incentive function is a <b>movement along S</b> (extension), not a shift. Rationing is a contraction of quantity demanded, not a fall in demand.</div>""", sec="2.4.4 · Functions of price"))

    C.append(card("fn2", "Price mechanism", "One chain, and its limits", "Concept", """
<h2>How the three work as one chain</h2>
<div class="chain"><span>Shock: Covid-19, mask demand surges</span><i>→</i><span>Price bid up</span><i>→</i><span>Signal: masks highly valued</span><i>→</i><span>Incentive: lines switch, new producers</span><i>→</i><span>Rationing: high price limits masks</span><i>→</i><span>Supply rises, price falls back</span></div>
<p>Explaining them as a sequence from one price change lifts an answer from listing (L1–2) to analysis (L3).</p>
<h3>When the price mechanism fails</h3>
<div class="tw wide"><table><tr><th>Weakness</th><th>Why it limits the functions</th><th>Example</th></tr>
<tr><td class="k">Inequity</td><td>Rations by ability to pay, not need</td><td>Rice, medicines, masks</td></tr>
<tr><td class="k">Time lags / low PES</td><td>Incentive works slowly, so high prices persist</td><td>Durian and rubber trees; housing</td></tr>
<tr><td class="k">Price controls</td><td>A maximum price blocks signal and incentive</td><td>Malaysia's 2022 chicken and egg shortages under capped prices</td></tr>
<tr><td class="k">Imperfect information</td><td>Signals misread; speculation</td><td>Panic buying</td></tr>
<tr><td class="k">Market power</td><td>A monopoly keeps prices high without raising output</td><td>Single dominant supplier</td></tr>
<tr><td class="k">Externalities</td><td>Prices ignore third parties (Chapter 3)</td><td>Pollution; vaccinations</td></tr></table></div>
<div class="note tip"><b>It works well when…</b>the good is a private good, information is good, markets are competitive and supply is elastic.</div>""", sec="2.4.4 · Evaluation"))

    # ---------- worked examples ----------
    C.append(card("we1", "Worked examples", "Solve for equilibrium", "Worked example", r"""
<h2>Solve the equilibrium, then add a tax</h2>
<p><b>Q:</b> \(Q_d = 50 - 5P\) and \(Q_s = 2 + 3P\). Find P* and Q*. Then a $2 specific tax is imposed. Who bears it?</p>
<ol class="steps">
<li>Set \(Q_d = Q_s\): \(50 - 5P = 2 + 3P\).</li>
<li>\(48 = 8P\), so <b>P* = $6</b>.</li>
<li>\(Q^* = 50 - 5(6) = 20\). Check: \(2 + 3(6) = 20\). <b>Q* = 20 units</b>.</li>
<li>The tax means producers keep \(P - 2\): new supply \(Q_s = 2 + 3(P - 2) = 3P - 4\).</li>
<li>\(50 - 5P = 3P - 4 \Rightarrow 54 = 8P \Rightarrow P = \$6.75\); \(Q = 50 - 5(6.75) = 16.25\).</li>
<li>Consumers pay $0.75 more; producers keep $4.75, i.e. $1.25 less. Consumers bear <b>$0.75 of the $2</b>, producers $1.25.</li>
</ol>""", sec="Worked example 1 · 2.4"))

    C.append(card("we2", "Worked examples", "PED and revenue", "Worked example", """
<h2>Calculate PED and use it</h2>
<p><b>Q:</b> Price rises from $12 to $18 and quantity demanded falls from 200,000 to 180,000. Calculate PED and state what happened to total revenue.</p>
<ol class="steps">
<li>%ΔP = (18 − 12) ÷ 12 × 100 = <b>+50%</b>.</li>
<li>%ΔQd = (180,000 − 200,000) ÷ 200,000 × 100 = <b>−10%</b>.</li>
<li>PED = −10 ÷ 50 = <b>−0.2</b>, so |PED| = 0.2 &lt; 1: <b>inelastic</b>. A 1% price rise cuts Qd by 0.2%.</li>
<li>TR before = 12 × 200,000 = $2.4m. TR after = 18 × 180,000 = $3.24m.</li>
<li>TR <b>rose by $0.84m</b>, as expected for an inelastic good: the gain on units still sold outweighs the loss on units no longer sold.</li>
</ol>""", sec="Worked example 2 · PED"))

    C.append(card("we3", "Worked examples", "PES and YED", "Worked example", """
<h2>PES and YED from handout data</h2>
<p><b>Q1:</b> Price $16 → $18.40; quantity supplied 28,000 → 28,840. PES?</p>
<ol class="steps">
<li>%ΔP = 2.40 ÷ 16 = <b>+15%</b>. %ΔQs = 840 ÷ 28,000 = <b>+3%</b>.</li>
<li>PES = 3 ÷ 15 = <b>0.2</b>: inelastic. Producers can barely raise output, typical of farm goods in the short run.</li>
</ol>
<p><b>Q2:</b> Income $800 → $1,000; clothes bought 100 → 140. YED and type?</p>
<ol class="steps">
<li>%ΔY = 200 ÷ 800 = <b>+25%</b>. %ΔQd = 40 ÷ 100 = <b>+40%</b>.</li>
<li>YED = 40 ÷ 25 = <b>+1.6</b>. Positive → normal; above 1 → a <b>luxury</b>.</li>
</ol>""", sec="Worked example 3 · PES & YED"))

    C.append(card("we4", "Worked examples", "XED: read the sign", "Worked example", """
<h2>XED: two examples</h2>
<p><b>Q1:</b> Coffee $10 → $12; orange juice bought 1,500 → 1,650 kg. XED?</p>
<ol class="steps">
<li>%ΔP coffee = +20%. %ΔQd juice = 150 ÷ 1,500 = +10%.</li>
<li>XED = +10 ÷ +20 = <b>+0.5</b>: positive, below 1 → <b>weak substitutes</b>.</li>
</ol>
<p><b>Q2:</b> Pencils $1.00 → $1.30; erasers bought 1,000 → 800. XED?</p>
<ol class="steps">
<li>%ΔP pencils = +30%. %ΔQd erasers = −200 ÷ 1,000 = <b>−20%</b>.</li>
<li>XED = −20 ÷ +30 ≈ <b>−0.67</b>: negative → <b>complements</b>, weak.</li>
</ol>
<div class="note trap"><b>Handout correction</b>The handout uses 400 instead of 800, getting −60% and XED = −2, then calls the goods "close substitutes". A negative XED always means complements. Example 1 also mentions tea where the table uses orange juice. Check with Puan Zaihan.</div>""", sec="Worked example 4 · XED"))

    C.append(card("we5", "Worked examples", "Surplus by hand", "Worked example", """
<h2>Consumer and producer surplus</h2>
<p><b>Q1:</b> You'd pay $1.00 for one drink and $0.90 for a second. The price is $0.75. Total CS?</p>
<ol class="steps"><li>Drink 1: 1.00 − 0.75 = $0.25. Drink 2: 0.90 − 0.75 = $0.15.</li><li>Total CS = <b>$0.40</b>.</li></ol>
<p><b>Q2:</b> A firm would sell unit 1 for $2.00 and unit 2 for $2.20. Market price $3.00. PS?</p>
<ol class="steps"><li>Unit 1: 3.00 − 2.00 = $1.00. Unit 2: 3.00 − 2.20 = $0.80.</li><li>PS = <b>$1.80</b>.</li></ol>
<p><b>Q3:</b> On a linear diagram, PS is a triangle with base 8 units and height $4. PS?</p>
<ol class="steps"><li>Area = ½ × base × height = ½ × 8 × 4 = <b>$16</b>.</li></ol>""", sec="Worked example 5 · 2.5"))

    C.append(card("we6", "Worked examples", "8-mark plan: wage rise", "Worked example", """
<h2>Equilibrium after a wage rise [8]</h2>
<p><b>Q (9708/22 M/J 2023 Q3a):</b> Using a diagram, explain market equilibrium and consider how far a general rise in wages would change the equilibrium price and quantity of a product.</p>
<ol class="steps">
<li><b>AO1:</b> define equilibrium (Qd = Qs, no tendency to change); diagram with D0, S0, E0 at P0, Q0; explain surplus above, shortage below.</li>
<li><b>AO2 supply side:</b> wages are a cost, so S shifts left to S1: price up to P1, quantity down to Q1.</li>
<li><b>AO2 demand side:</b> wages are income; for a normal good D shifts right to D1, pushing price up further to P2.</li>
<li><b>AO3:</b> price almost certainly rises. Quantity depends on relative shifts: labour-intensive haircuts → S shift dominates, Q falls; high-YED restaurant meals → D shift may dominate, Q rises; inferior goods → D falls.</li>
<li><b>Conclude:</b> price rises; how far quantity changes, and in which direction, depends on labour intensity and YED (and PED, PES).</li>
</ol>""", sec="Worked example 6 · Paper 2"))

    # ---------- exam technique ----------
    C.append(card("ex1", "Exam technique", "Plans & evaluation", "Exam", """
<h2>Using this in the exam</h2>
<div class="tw"><table><tr><th>Part</th><th class="n">AO1</th><th class="n">AO2</th><th class="n">AO3</th></tr>
<tr><td class="k">(a) 8 · Explain… consider…</td><td class="n">3</td><td class="n">3</td><td class="n">2</td></tr>
<tr><td class="k">(b) 12 · Assess…</td><td class="n" colspan="2">8 (levels)</td><td class="n">4</td></tr></table></div>
<p>One-sided 12-markers are capped at Level 2 for AO1/AO2 and get <b>0 for AO3</b>.</p>
<div class="two">
<div><h4>8-mark plan · ~15 min</h4><ul><li>Define every term; give the formula</li><li>One fully labelled diagram</li><li>Explain step by step, citing labels</li><li>Consider 1–2 "it depends" factors</li><li>Conclude in 1–2 sentences</li></ul></div>
<div><h4>12-mark plan · ~22 min</h4><ul><li>Intro: define, say what you'll weigh</li><li>For: diagram + developed chain</li><li>Against: developed the same way</li><li>Evaluation woven in: SR vs LR, which goods</li><li>Judgement: "on balance… because… unless…"</li></ul></div>
</div>
<h3>Elasticity as your evaluation tool</h3>
<div class="tw wide"><table><tr><th>Essay about…</th><th>Use</th><th>Sentence frame</th></tr>
<tr><td class="k">Tax, cost rise, subsidy</td><td>PED</td><td>"How far price rises depends on PED: with inelastic demand, as for petrol, most of the tax is passed on…"</td></tr>
<tr><td class="k">Recession, growth</td><td>YED</td><td>"Demand for luxuries such as overseas holidays falls sharply, while inferior goods may even rise."</td></tr>
<tr><td class="k">Related good's price</td><td>XED</td><td>"Pepsi is a close substitute for Coke, so the effect would be large."</td></tr>
<tr><td class="k">Shortages, farming</td><td>PES</td><td>"In the short run supply is inelastic, so higher demand mainly raises price…"</td></tr>
<tr><td class="k">CS / PS</td><td>PED</td><td>"The loss of CS is largest when demand is inelastic."</td></tr></table></div>""", sec="Paper 2 · Exam technique"))

    C.append(card("mist", "Exam technique", "Mistakes & diagram checklist", "Mistakes", """
<h2>Common mistakes that cost marks</h2>
<ul>
<li>"Price rises so demand falls." Write <b>quantity demanded</b> falls (movement).</li>
<li>Shifting demand when the question is about a cost or tax (that shifts supply).</li>
<li>Judging elasticity from slope alone across different diagrams or units.</li>
<li>Forgetting the sign: negative XED = complements; negative YED = inferior.</li>
<li>Calling the incentive function a shift of supply.</li>
<li>A conclusion that only repeats the essay. It must make a judgement.</li>
</ul>
<h3>Diagram checklist</h3>
<ul><li>Axes labelled Price and Quantity; origin O.</li><li>Curves D0, D1, S0, S1 with a shift arrow.</li><li>Equilibria dashed to both axes: P0, Q0, P1, Q1.</li><li>Shade and name any area (CS, PS, tax revenue, TR gain/loss).</li><li>Refer to it: "as shown in Figure 1, price rises from P0 to P1".</li><li>Inelastic curves visibly steep, elastic flat, in separate diagrams.</li></ul>
<div class="note tip"><b>Data response calculations</b>Write the formula, show both % changes with signs, give the answer to 2 d.p., then interpret it in words ("inelastic, so…").</div>""", sec="Paper 2 · Mistakes"))

    # ---------- practice ----------
    C.append(card("pr1", "Practice", "Practice: MCQ pack picks", "Practice", """
<h2>Practice · Paper 1 style</h2>
<button class="btn" type="button" data-revealall>Reveal all answers</button>
<div class="pq"><div class="qh"><span>Q1 · Pack Q6</span><span class="mk">[1]</span></div>
<p class="qt">Supply of a good falls and its price rises. What is the only certain outcome on the demand side?</p>
<div class="ans"><b>Contraction</b>A fall in quantity demanded: a movement up along D. Demand itself hasn't changed.</div></div>
<div class="pq"><div class="qh"><span>Q2 · Pack Q23</span><span class="mk">[1]</span></div>
<p class="qt">A tax on cigarettes cuts restaurant meal sales. What happens in each market?</p>
<div class="ans"><b>Answer</b>Cigarettes: the tax shifts S, so a movement along D. Meals (a complement for smokers): demand shifts left.</div></div>
<div class="pq"><div class="qh"><span>Q3 · Pack Q26</span><span class="mk">[1]</span></div>
<p class="qt">The government advises people to drink less fizzy drink. Effect on the sugar market?</p>
<div class="ans"><b>Answer</b>Fizzy drink D shifts left. Sugar demand is derived from it, so sugar demand falls: a movement down the sugar supply curve.</div></div>
<div class="pq"><div class="qh"><span>Q4 · Pack Q1</span><span class="mk">[1]</span></div>
<p class="qt">A car park has a fixed number of spaces and demand varies by day. How can price clear the market each day?</p>
<div class="ans"><b>Vary the price</b>Supply is fixed (vertical S), so charge a different price each day where that day's demand meets the fixed supply.</div></div>
<div class="pq"><div class="qh"><span>Q5 · Calculation</span><span class="mk">[2]</span></div>
<p class="qt">A firm's PED is 0.4. It raises price by 10%. By how much does quantity demanded change, and what happens to revenue?</p>
<div class="ans"><b>−4%; TR rises</b>%ΔQd = 0.4 × 10 = 4% fall. Inelastic, so the price rise increases total revenue.</div></div>""", sec="Practice · Paper 1"))

    C.append(card("pr2", "Practice", "Practice: essay plans", "Practice", """
<h2>Practice · Paper 2 essays</h2>
<div class="pq"><div class="qh"><span>Q6 · PED</span><span class="mk">[8]</span></div>
<p class="qt">Explain, using a diagram, how a firm can use PED to decide its pricing, and consider whether raising price will always raise its revenue.</p>
<div class="ans"><b>Plan</b>Define PED + formula; TR gain/loss diagrams for inelastic vs elastic. Consider: only if demand is inelastic at the current price; PED changes along the curve; rivals may not follow; revenue isn't profit. Conclude: not always.</div></div>
<div class="pq"><div class="qh"><span>Q7 · YED</span><span class="mk">[8]</span></div>
<p class="qt">Explain the difference between a normal and an inferior good using YED, and consider whether a producer of luxury goods should worry about a recession.</p>
<div class="ans"><b>Plan</b>YED formula; + vs −; luxury &gt; 1. Hotel with YED +2.5: incomes −5% → demand ≈ −12.5%. Consider: depends on its customers' incomes (the very rich may be little affected), brand strength, and whether it can add budget lines.</div></div>
<div class="pq"><div class="qh"><span>Q8 · Price mechanism</span><span class="mk">[12]</span></div>
<p class="qt">Assess whether the price mechanism is the best way to allocate a staple food, such as rice, after a sudden fall in supply.</p>
<div class="ans"><b>Plan</b>For: S left → price ↑ → rationing, signal to farmers and importers, incentive over time; no bureaucracy. Against: rice is a necessity with low PED, a big share of poor budgets → harsh rationing by ability to pay; low PES → slow response. Alternatives: maximum price (blocks the signal), buffer stock release, transfers, imports. Judge: short run, targeted transfers or stock release; long run, let price signal more supply.</div></div>
<div class="pq"><div class="qh"><span>Q9 · Elasticity</span><span class="mk">[12]</span></div>
<p class="qt">Assess whether PED is more useful than YED to a firm.</p>
<div class="ans"><b>Plan</b>PED: price the firm controls → TR decision now. YED: plan output over the cycle (car maker YED +2, incomes −3% → demand ≈ −6%). Evaluate: PED wins in the short run with price-setting power; YED wins for luxury or inferior goods over the cycle; both rely on past data. Judge: PED for most firms, with that exception.</div></div>""", sec="Practice · Paper 2"))

    C.append(card("pp", "Practice", "Past paper questions", "Past papers", f"""
<h2>Real 9708 questions on Chapter 2</h2>
<div class="tw wide"><table><tr><th>Paper</th><th>Question (paraphrased)</th><th class="n">Marks</th></tr>
<tr><td class="k">22 M/J 2023 Q2(a)</td><td>Explain CS and PS; consider whether a cost-driven price rise always reduces CS.</td><td class="n">8</td></tr>
<tr><td class="k">22 M/J 2023 Q3(a)</td><td>Explain equilibrium; consider how far a general wage rise changes equilibrium P and Q.</td><td class="n">8</td></tr>
<tr><td class="k">21 M/J 2023 Q3(a)</td><td>Explain XED with a formula; consider which factors most decide its sign and size.</td><td class="n">8</td></tr>
<tr><td class="k">21 M/J 2023 Q3(b)</td><td>Assess whether a buffer stock's benefits always outweigh its disadvantages.</td><td class="n">12</td></tr>
<tr><td class="k">2023 Specimen Q3(a)</td><td>Explain PES with a formula; consider which factors matter most.</td><td class="n">8</td></tr>
<tr><td class="k">2023 Specimen Q3(b)</td><td>Assess two policies to make agricultural supply more price elastic.</td><td class="n">12</td></tr>
<tr><td class="k">22 M/J 2023 Q2(b)</td><td>Maximum price vs transfers for rice (Chapter 3, built on Chapter 2).</td><td class="n">12</td></tr></table></div>
<div class="note link"><b>Model essays</b>Full highlighted model answers for five of these are in your original notes. <a href="{ORIG}" target="_blank" rel="noopener">Price System notes</a> · <a href="{ORIG_FN}" target="_blank" rel="noopener">Functions of Price</a> · <a href="{ORIG_EL}" target="_blank" rel="noopener">Four Elasticities</a></div>""", sec="Practice · Past papers"))

    C.append(card("sum", "Summary", "Formula sheet", "Summary", r"""
<h2>Chapter 2 formula &amp; summary sheet</h2>
<div class="tw"><table>
<tr><td class="k">% change</td><td>\(\dfrac{\text{new} - \text{old}}{\text{old}} \times 100\)</td></tr>
<tr><td class="k">PED</td><td>\(\dfrac{\%\Delta Q_d}{\%\Delta P}\) · &lt;1 inelastic → raise P, TR ↑</td></tr>
<tr><td class="k">PES</td><td>\(\dfrac{\%\Delta Q_s}{\%\Delta P}\) · spare capacity, stocks, time</td></tr>
<tr><td class="k">YED</td><td>\(\dfrac{\%\Delta Q_d}{\%\Delta Y}\) · &gt;1 luxury · 0–1 necessity · &lt;0 inferior</td></tr>
<tr><td class="k">XED</td><td>\(\dfrac{\%\Delta Q_{d,A}}{\%\Delta P_B}\) · + substitutes · − complements</td></tr>
<tr><td class="k">Equilibrium</td><td>Set \(Q_d = Q_s\), solve for P, substitute back</td></tr>
<tr><td class="k">Specific tax t</td><td>New supply: replace P with \(P - t\)</td></tr>
<tr><td class="k">CS, PS</td><td>Triangle area \(\tfrac12 \times Q \times \Delta P\)</td></tr>
<tr><td class="k">Movement vs shift</td><td>Own price → along; anything else → shift</td></tr>
<tr><td class="k">Both curves shift</td><td>Same direction → Q certain; opposite → P certain</td></tr>
<tr><td class="k">Price functions</td><td>Signal (what) · Incentive (how much, along S) · Rationing (for whom, along D)</td></tr>
<tr><td class="k">Essay marks</td><td>(a) 3/3/2 · (b) 8 + 4; one-sided = 0 AO3</td></tr>
</table></div>
<p class="lede" style="font-size:15px">Screenshot this card. Then open <b>Cards</b> or <b>Quiz</b> at the top.</p>""", sec="Summary"))
    return C


EXTRA_FLASH = [
    ["Price mechanism", "Which function of price answers \"for whom\"? Which answers \"what\"?", "Rationing answers <b>for whom</b>; signalling answers <b>what</b>; the incentive function answers <b>how much</b>."],
    ["Price mechanism", "Is the incentive function a shift of supply?", "No. Higher price → extension in quantity supplied: a <b>movement along S</b>. Only non-price factors shift S."],
    ["Price mechanism", "Why did Malaysia's 2022 capped chicken and egg prices lead to shortages?", "A maximum price below equilibrium blocks the <b>signal</b> and <b>incentive</b>, so supply doesn't rise and excess demand persists."],
    ["Price mechanism", "Two weaknesses of rationing by price?", "It rations by <b>ability to pay, not need</b> (essentials like rice); and with <b>low PES</b> the incentive works slowly, so high prices persist."],
]

QUIZ = [
 {"s":"Demand","q":"The price of a good falls. What happens?","o":["Demand increases","Quantity demanded expands along the demand curve","The demand curve shifts right","Supply shifts left"],"c":1,"e":"A change in the good's own price is a movement along D. \"Increase in demand\" means a shift."},
 {"s":"Demand","q":"Which of these shifts the demand curve for cars to the right?","o":["A fall in the price of cars","A rise in the price of petrol","A fall in the price of petrol","A rise in the cost of steel"],"c":2,"e":"Petrol is a complement: cheaper petrol raises demand for cars. A is a movement; B shifts D left; D shifts supply."},
 {"s":"Demand","q":"Bus tickets are an inferior good. Incomes rise. What happens to demand for bus tickets?","o":["It increases","It decreases","It stays the same","Quantity demanded contracts along D"],"c":1,"e":"For an inferior good, YED &lt; 0: higher income shifts demand left as people switch to cars."},
 {"s":"Supply","q":"A $2 specific tax is placed on a good. What happens to the supply curve?","o":["It shifts up by $2 at every quantity (parallel)","It pivots, with the gap widening at higher prices","It shifts down by $2","It does not move; price rises by $2"],"c":0,"e":"A specific tax is a fixed amount per unit, so supply shifts up in parallel. B describes an ad valorem tax."},
 {"s":"Equilibrium","q":"Qd = 50 − 5P and Qs = 2 + 3P. What is the equilibrium?","o":["P = $6, Q = 20","P = $8, Q = 10","P = $4, Q = 30","P = $6, Q = 26"],"c":0,"e":"50 − 5P = 2 + 3P → 8P = 48 → P = 6; Q = 50 − 30 = 20."},
 {"s":"Equilibrium","q":"Demand and supply both increase. What can be predicted with certainty?","o":["Price rises","Price falls","Quantity rises","Quantity falls"],"c":2,"e":"Both shifts raise quantity. Price depends on which shift is larger."},
 {"s":"Equilibrium","q":"Demand increases while supply decreases. What is certain?","o":["Price rises","Price falls","Quantity rises","Quantity falls"],"c":0,"e":"Both shifts push price up. Quantity depends on the relative size of the shifts."},
 {"s":"PED","q":"Price rises from $12 to $18; quantity demanded falls from 200,000 to 180,000. What is |PED|?","o":["0.2","0.5","2","5"],"c":0,"e":"%ΔQd = −10%, %ΔP = +50%, so PED = −0.2: inelastic."},
 {"s":"PED","q":"A firm's demand has PED of 0.4. If it raises price, what happens to total revenue?","o":["It rises","It falls","It stays the same","It depends on supply"],"c":0,"e":"Inelastic demand: quantity falls proportionally less than price rises, so TR rises."},
 {"s":"PED","q":"Where on a straight-line demand curve is PED equal to 1?","o":["At the price-axis intercept","At the midpoint","At the quantity-axis intercept","Everywhere, because the slope is constant"],"c":1,"e":"PED depends on P/Q as well as slope. It is 1 at the midpoint, where TR is maximised."},
 {"s":"PED","q":"Which tax is likely to raise the most revenue for a government?","o":["A tax on a good with elastic demand","A tax on a good with inelastic demand","A tax on a good with many close substitutes","A tax on a luxury brand"],"c":1,"e":"With inelastic demand quantity barely falls, so the tax base stays large."},
 {"s":"YED","q":"A good has YED of −0.5. What type of good is it?","o":["A luxury","A necessity","An inferior good","A Giffen good necessarily"],"c":2,"e":"Negative YED means demand falls as income rises: an inferior good. A Giffen good is a special case, not implied."},
 {"s":"XED","q":"Pencils rise in price by 30% and demand for erasers falls by 20%. What is the relationship?","o":["Close substitutes","Weak substitutes","Weak complements","Unrelated"],"c":2,"e":"XED = −20 ÷ 30 ≈ −0.67. Negative means complements; below 1 in size means weak."},
 {"s":"PES","q":"Which is most likely to make supply more price elastic?","o":["Perishable output","Firms operating at full capacity","Spare capacity and large stocks","A very short time period"],"c":2,"e":"Spare capacity and stocks let output respond quickly. The others make supply inelastic."},
 {"s":"Surplus","q":"Higher costs raise a good's price. When is the absolute loss of consumer surplus largest?","o":["When demand is price elastic","When demand is price inelastic","When supply is perfectly elastic","When demand is perfectly elastic"],"c":1,"e":"With inelastic demand price rises most, so existing buyers pay much more per unit."},
 {"s":"Related markets","q":"Demand for beef rises. What happens in the leather market?","o":["Demand for leather rises","Supply of leather increases and its price falls","Supply of leather decreases and its price rises","Nothing changes"],"c":1,"e":"Joint supply: more cattle slaughtered for beef means more leather, so leather supply shifts right."},
 {"s":"Related markets","q":"Car prices fall. Cars and petrol are complements. What happens in the petrol market?","o":["Petrol demand shifts right","Petrol supply shifts right","Petrol demand shifts left","Movement along petrol demand"],"c":0,"e":"More cars are bought, so demand for the complement petrol increases."},
 {"s":"Pack Q9","q":"Cod is overfished while pollock is plentiful. How might the price mechanism limit cod depletion?","o":["Cod price falls and pollock price rises","Cod price rises and pollock price falls, so buyers switch","Both prices rise","The government fixes the cod price"],"c":1,"e":"The rising cod price rations it and the falling pollock price encourages switching. D isn't the price mechanism."},
 {"s":"Pack Q8","q":"A disease kills many sheep. What happens in the wool market?","o":["Demand for wool shifts left","Supply of wool shifts left","Supply of wool shifts right","Movement along the wool supply curve"],"c":1,"e":"Fewer sheep is a non-price factor reducing supply."},
 {"s":"Price mechanism","q":"Demand for face masks rises sharply. Which shows the incentive function?","o":["A shift of the supply curve to the right","A movement up the supply curve as firms expand output","A movement down the demand curve","A fall in the price of masks"],"c":1,"e":"The higher price makes supplying more profitable, so quantity supplied extends along S."},
]


def write(scratch, js_array):
    flash = json.loads((pathlib.Path(__file__).parent / "data/ch2-flash.json").read_text(encoding="utf8")) + EXTRA_FLASH
    meta = {"title": "Price System Deck", "short": "Econ Ch2", "bar": "The price system",
            "code": "9708 · AS Chapter 2", "key": "deck-9708-ch2"}
    out = engine.render(meta, build(), flash, QUIZ, math=True)
    pathlib.Path("deck-econ-ch2.html").write_text(out, encoding="utf8")
    print("ch2", len(out), "bytes,", len(flash), "flashcards,", len(QUIZ), "quiz")
