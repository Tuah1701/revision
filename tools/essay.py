"""9708 AS Paper 2 essay technique deck (from Tuah's Essay Framework, plus the marking notes in the Ch1/Ch2 decks)."""
import pathlib
import engine
from engine import card

ORIG = "https://claude.ai/code/artifact/31acac57-ce47-4e2f-9fb6-be4a409e475c"


def build():
    C = []
    C.append(card("cover", "Start", "Essay technique", "Cover", """
<p class="sec" style="margin:0">CAIE 9708 · AS Level · Paper 2 Sections B and C</p>
<p class="cover-k">8+12</p>
<h1>Writing Economics essays that score</h1>
<p class="lede">Your Essay Framework as a deck: structure, the paragraph unit, evaluation, conclusions and the exam checklist.</p>
<div class="stat"><div><b>20</b>marks per essay</div><div><b>3</b>worked examples</div><div><b>24</b>flashcards</div><div><b>12</b>quiz questions</div></div>
<p class="swipehint">Swipe left to start. Tap ☰ for contents.</p>
<p><a href="index.html">Open Revision Hub</a></p>""", sec="Start"))

    C.append(card("format", "Start", "What you're writing", "Overview", """
<h2>AS essays are 8 + 12, not 25</h2>
<p>Paper 2 is 2 hours for 60 marks: <b>Section A</b> data response (20), then one essay from <b>Section B</b> (micro, 20) and one from <b>Section C</b> (macro, 20). Every essay has two parts, (a) 8 and (b) 12, and everything in this deck is built for that length.</p>
<div class="tw"><table><tr><th>Part</th><th>Command words</th><th class="n">AO1</th><th class="n">AO2</th><th class="n">AO3</th><th>Marking</th></tr>
<tr><td class="k">(a) 8</td><td>Explain… and consider…</td><td class="n">3</td><td class="n">3</td><td class="n">2</td><td>Point-based</td></tr>
<tr><td class="k">(b) 12</td><td>Assess… (older papers: Discuss)</td><td class="n" colspan="2">8, levels</td><td class="n">4</td><td>Levels-based</td></tr></table></div>
<div class="two">
<div><h4>AO1 · Knowledge</h4><p>Precise definitions, correct terms, an accurate labelled diagram.</p></div>
<div><h4 class="t">AO2 · Analysis</h4><p>Developed chains of reasoning from cause to effect, using the diagram.</p></div>
<div><h4 class="g">AO3 · Evaluation</h4><p>What the answer depends on and why, then a justified conclusion to the exact question.</p></div>
</div>
<div class="note tip"><b>Timing</b>The paper is 2 hours for 60 marks: 2 minutes per mark. About 16 minutes for an 8-mark part and 24 for a 12-mark part, with planning time inside that.</div>""", sec="Overview"))

    C.append(card("mark8", "Marking", "How (a) 8 is marked", "Concept", """
<h2>Part (a): 8 marks, point-based</h2>
<p>Each valid point earns a mark, up to the limit for each objective.</p>
<div class="tw"><table><tr><th>AO</th><th>Typical marks (PPC example)</th></tr>
<tr><td class="k">AO1 · 3</td><td>1 accurate diagram · 1 correctly labelled named axes · 1 definition</td></tr>
<tr><td class="k">AO2 · 3</td><td>Explain the reallocation · the sacrifice · how it is measured</td></tr>
<tr><td class="k">AO3 · 2</td><td>1 reasoned "however / it depends" · <b>1 reserved for a justified conclusion</b></td></tr></table></div>
<h3>Structure: "Explain… and consider whether…"</h3>
<ol><li>Define or distinguish A, with an example.</li><li>Define or distinguish B, with an example (or draw the diagram and explain it).</li><li><b>Consider:</b> what the market alone does, what government adds, then one limit ("depends on funding / efficiency").</li><li>One-line conclusion answering the question.</li></ol>
<div class="note trap"><b>Don't lose the easy mark</b>The conclusion mark is reserved. Even one sentence that answers the question earns it.</div>""", sec="Marking · Part (a)"))

    C.append(card("mark12", "Marking", "How (b) 12 is marked", "Concept", """
<h2>Part (b): 12 marks, levels-based</h2>
<div class="tw"><table><tr><th>AO1 + AO2 /8</th><th>What it looks like</th></tr>
<tr><td class="k">L3 · 6–8</td><td>Detailed, accurate, balanced, fully explained</td></tr>
<tr><td class="k">L2 · 3–5</td><td>Some accuracy; may be one-sided or partly explained</td></tr>
<tr><td class="k">L1 · 1–2</td><td>Assertive, descriptive, little relevance</td></tr></table></div>
<div class="tw"><table><tr><th>AO3 /4</th><th>What it looks like</th></tr>
<tr><td class="k">L2 · 3–4</td><td>Justified conclusion to the specific question + developed evaluative comments</td></tr>
<tr><td class="k">L1 · 1–2</td><td>Vague or general judgement</td></tr></table></div>
<div class="note trap"><b>One-sided = 0 for AO3</b>A one-sided answer is capped at Level 2 for AO1/AO2 and gets no evaluation marks at all.</div>""", sec="Marking · Part (b)"))

    C.append(card("struct12", "Structure", "The 12-mark structure", "Concept", """
<h2>12 marks: "Assess / Evaluate / Discuss"</h2>
<div class="tw"><table><tr><th>Part</th><th>Job</th><th>Length</th></tr>
<tr><td class="k">Intro</td><td>Define the key term; say what the answer depends on</td><td>1–2 lines</td></tr>
<tr><td class="k">Case FOR</td><td>Point → explain → example</td><td>1–3 paras</td></tr>
<tr><td class="k">Case AGAINST</td><td>"However…" with the same chain</td><td>1–3 paras</td></tr>
<tr><td class="k">Evaluation</td><td>Limits, or "it depends on…"</td><td>1–2 paras</td></tr>
<tr><td class="k">Conclusion</td><td>Direct judgement plus one reason</td><td>2–3 lines</td></tr></table></div>
<div class="note tip"><b>Evaluate throughout</b>Don't save all evaluation for the last line. A "however" or "this depends on" inside each side lifts the whole answer.</div>""", sec="Structure · Part (b)"))

    C.append(card("cmd", "Structure", "Command words", "Concept", """
<h2>Circle the command word first</h2>
<div class="tw wide"><table><tr><th>Word</th><th>CAIE meaning</th><th>What to do</th></tr>
<tr><td class="k">Define</td><td>Give precise meaning</td><td>One exact sentence</td></tr>
<tr><td class="k">Explain</td><td>Set out reasons; make relationships evident</td><td>Definition + chain + diagram. Not a list</td></tr>
<tr><td class="k">Analyse</td><td>Examine in detail to show relationships</td><td>"because… which leads to… therefore…"</td></tr>
<tr><td class="k">Consider</td><td>Review and respond to given information</td><td>One reasoned "however" + a one-line judgement</td></tr>
<tr><td class="k">Assess</td><td>Make an informed judgement</td><td>Both sides, weighed, then a conclusion</td></tr>
<tr><td class="k">Discuss</td><td>Write about issues in depth</td><td>Same as assess (older papers)</td></tr>
<tr><td class="k">Evaluate</td><td>Judge quality, importance or value</td><td>Weigh significance, don't just list</td></tr>
<tr><td class="k">Compare</td><td>Similarities and/or differences</td><td>Point by point, "whereas"</td></tr></table></div>
<p>"Assess" and "evaluate" need a judgement; "explain" doesn't.</p>""", sec="Structure · Command words"))

    C.append(card("para", "Paragraphs", "The paragraph unit", "Concept", """
<h2>Point → Explain → Example → Link</h2>
<div class="chain"><span>Point</span><i>→</i><span>Explain (chain of reasoning)</span><i>→</i><span>Example</span><i>→</i><span>Link to the question</span></div>
<p><b>Q:</b> "Are producers the only ones to benefit from more investment?"</p>
<div class="two">
<div><h4>Point</h4><p>Consumers gain in the long run.</p></div>
<div><h4>Explain</h4><p>Investment shifts the PPC outward, so more goods are available at lower cost.</p></div>
<div><h4>Example</h4><p>Factory automation lowers car prices.</p></div>
<div><h4>Link</h4><p>So producers are <i>not</i> the only beneficiaries.</p></div>
</div>
<div class="note tip"><b>One real example per paragraph</b>Malaysian examples work well: targeted RON95 subsidies, PLUS tolls, Klinik Kesihatan, the sugar tax, Penang semiconductors.</div>""", sec="Paragraphs"))

    C.append(card("chain", "Paragraphs", "Assertion vs chain", "Concept", """
<h2>From L1 assertion to L3 chain</h2>
<div class="two">
<div><h4 class="r">Weak · L1</h4><p>"Free markets cause pollution."</p></div>
<div><h4 class="g">Strong · L3</h4><p>Firms maximise profit, so they minimise private costs and ignore costs imposed on third parties, such as river pollution from palm oil mills. Because these external costs aren't in the price, output is above the social optimum, so resources are over-allocated.</p></div>
<div><h4 class="r">Weak · L1</h4><p>"Planned economies are inefficient."</p></div>
<div><h4 class="g">Strong · L3</h4><p>Without prices, planners have no signal of what consumers want, so they forecast demand; errors cause shortages and surpluses. Managers aren't rewarded with profit, so they have little incentive to cut costs, so the economy may produce inside its PPC.</p></div>
</div>
<div class="note tip"><b>Connective words carry the marks</b><b>because · so · which leads to · therefore · as a result</b>. If a sentence has none, it's probably an assertion.</div>""", sec="Paragraphs · AO2"))

    C.append(card("eval", "Evaluation", "It depends on…", "Concept", """
<h2>Evaluation: "it depends on…"</h2>
<p>Generic "it depends" earns little. Say <b>on what</b> and <b>why</b>.</p>
<div class="tw wide"><table><tr><th>Lever</th><th>Sentence starter</th></tr>
<tr><td class="k">Time period</td><td>"In the short run… but in the long run…"</td></tr>
<tr><td class="k">Elasticity</td><td>"How far price rises depends on PED: with inelastic demand, as for rice, most of the cost is passed on…"</td></tr>
<tr><td class="k">Development level</td><td>"In a low-income economy with weak institutions…"</td></tr>
<tr><td class="k">Type of good / investment</td><td>"Public investment in education differs from export machinery because…"</td></tr>
<tr><td class="k">Quality of government</td><td>"Only if the government has the funding, information and efficiency to… otherwise government failure…"</td></tr>
<tr><td class="k">Size of shift</td><td>"If the fall in supply is larger than the rise in demand…"</td></tr>
<tr><td class="k">Who is affected</td><td>"Low-income households spend a larger share of income on food, so…"</td></tr>
<tr><td class="k">Value judgement</td><td>"Whether this is desirable depends on whether society prioritises equity or efficiency."</td></tr></table></div>""", sec="Evaluation · AO3"))

    C.append(card("concl", "Evaluation", "Conclusion template", "Concept", """
<h2>A conclusion that picks a side</h2>
<div class="formula">Overall, [answer to the question] because [strongest reason]. However, this depends on [key factor], so [qualified final judgement].</div>
<div class="def"><span class="lab">Example</span><p>"Overall, a pure market economy is not always best because it fails to provide merit and public goods. However, planned systems lack efficiency, so a mixed economy is the more defensible answer."</p></div>
<ul><li>Answer the <b>exact words</b>: "always" → "not always, because… unless…"; "only" → "not only…".</li><li>Never just summarise the essay.</li><li>Never sit on the fence ("both have pros and cons").</li><li>Give the condition under which the other side would win.</li></ul>""", sec="Evaluation · Conclusion"))

    C.append(card("bad", "Evaluation", "What sample essays get wrong", "Mistakes", """
<h2>Don't copy these mistakes</h2>
<div class="two">
<div><h4 class="r">Weak conclusions</h4><p>"A more inclusive growth model" doesn't answer "only producers?". Say: <i>No, because X, though producers gain most in the short run because Y.</i></p></div>
<div><h4 class="r">Loose logic</h4><p>"Investment → higher taxes → higher prices → shortages" skips steps. Use <b>opportunity cost</b>: resources move from consumer to capital goods, so short-run consumption falls (a movement along the PPC).</p></div>
<div><h4 class="r">Imprecise terms</h4><p>Public goods are underprovided because of the <b>free-rider problem</b>, not just "no profit".</p></div>
<div><h4 class="r">No diagrams</h4><p>A PPC shift would earn marks in investment questions. Use a diagram wherever one fits.</p></div>
</div>
<h3>Common examiner-report errors</h3>
<ul><li>Axes labelled X and Y when the question names the goods.</li><li>Listing advantages and disadvantages without explaining any (stuck at L1–L2).</li><li>"Price rises so demand falls": write <b>quantity demanded</b>.</li><li>One-sided 12-markers: AO3 = 0.</li></ul>""", sec="Mistakes"))

    C.append(card("diag", "Evaluation", "Diagrams that earn marks", "Concept", """
<h2>Diagram checklist</h2>
<ul><li>Axes labelled with the question's goods or Price / Quantity; origin O.</li>
<li>Curves labelled (PPC, D0, D1, S0, S1) with a shift arrow.</li>
<li>Equilibria dashed to both axes: P0, Q0, P1, Q1.</li>
<li>Shade and name any area you discuss (CS, PS, tax revenue).</li>
<li>Refer to it: "as shown in Figure 1, price rises from P0 to P1".</li></ul>
<div class="tw"><table><tr><th>Question about…</th><th>Draw</th></tr>
<tr><td class="k">Scarcity, opportunity cost, growth, investment</td><td>PPC (movement or shift)</td></tr>
<tr><td class="k">Prices, shocks, taxes, subsidies</td><td>Demand and supply</td></tr>
<tr><td class="k">Price controls, buffer stocks</td><td>D/S with a target or maximum price</td></tr>
<tr><td class="k">Revenue and PED</td><td>TR gain/loss rectangles</td></tr></table></div>""", sec="AO1 · Diagrams"))

    C.append(card("check", "Exam day", "Exam checklist", "Checklist", """
<h2>Exam checklist</h2>
<ol class="steps">
<li>Circle the <b>command word</b>. "Assess" and "evaluate" need a judgement.</li>
<li><b>Plan for 2 minutes:</b> 2 points for, 2 against, 1 "depends on" factor, and your verdict.</li>
<li>Use <b>precise key terms</b>: opportunity cost, allocative efficiency, externality, free-rider, consumer sovereignty.</li>
<li><b>One real example per paragraph.</b></li>
<li><b>Evaluate throughout</b>, not only in the last line.</li>
<li><b>Add a diagram</b> where one fits, and refer to it.</li>
<li><b>Finish with a conclusion that picks a side</b> and gives a reason.</li>
</ol>""", sec="Exam day"))

    # worked examples
    C.append(card("we1", "Worked examples", "Plan a 12-marker in 2 min", "Worked example", """
<h2>Plan a 12-marker in two minutes</h2>
<p><b>Q:</b> Assess whether the allocation of resources by the free market is always desirable for an economy. [12]</p>
<ol class="steps">
<li><b>Command word:</b> "Assess" + "always" → two sides, then a judgement that says "not always" and when.</li>
<li><b>Define:</b> free market = allocation by the price mechanism, private ownership, minimal intervention.</li>
<li><b>For (2):</b> efficiency from competition and the profit motive; consumer sovereignty (e-commerce growth after 2020).</li>
<li><b>Against (2):</b> negative externalities (haze, river pollution); public goods not provided and merit goods under-provided.</li>
<li><b>Depends on:</b> type of good and degree of market failure; risk of government failure if we intervene instead.</li>
<li><b>Verdict:</b> not always; desirable for private goods in competitive markets, a mixed economy is better where market failure is significant.</li>
</ol>""", sec="Worked example 1 · Planning"))

    C.append(card("we2", "Worked examples", "Build one paragraph", "Worked example", """
<h2>Build a paragraph with PEEL</h2>
<p><b>Q:</b> Assess whether governments should provide merit goods free of charge. [12] Write one "for" paragraph.</p>
<ol class="steps">
<li><b>Point:</b> Free provision raises consumption towards the socially optimal level.</li>
<li><b>Explain:</b> Consumers underestimate the benefits of merit goods (information failure) and ignore external benefits, so in a free market consumption is below the social optimum. A zero price removes the cost barrier, so consumption rises.</li>
<li><b>Example:</b> Free childhood vaccinations at Klinik Kesihatan raise coverage, protecting others too.</li>
<li><b>Link:</b> Therefore free provision corrects under-consumption, which supports the view, especially for low-income households.</li>
<li><b>Evaluate inside the paragraph:</b> however, this depends on the cause: if under-consumption is due to information failure, an information campaign may be cheaper than free provision.</li>
</ol>""", sec="Worked example 2 · Paragraph"))

    C.append(card("we3", "Worked examples", "Fix a weak conclusion", "Worked example", """
<h2>Fix a weak conclusion</h2>
<p><b>Q:</b> Discuss the view that the only goods a government should produce are public goods. [12]</p>
<p><b>Weak:</b> "In conclusion, there are arguments on both sides and the government should consider them carefully."</p>
<ol class="steps">
<li><b>Problem:</b> it sits on the fence and never answers "only". AO3 L1 at best.</li>
<li><b>Answer the exact word:</b> "The view is too narrow: governments should not produce <i>only</i> public goods."</li>
<li><b>Strongest reason:</b> "because merit goods and essential natural monopolies are under-provided or overpriced by markets."</li>
<li><b>Depends on:</b> "However, this depends on government efficiency: where corruption or poor information is significant, subsidising private producers may be better than producing directly."</li>
<li><b>Full version:</b> "Overall, the view is too narrow because markets under-provide merit goods as well as public goods. However, this depends on the government's efficiency, so where government failure is likely, funding private providers is the better route."</li>
</ol>""", sec="Worked example 3 · Conclusion"))

    # practice
    C.append(card("pr1", "Practice", "Practice: upgrade these", "Practice", """
<h2>Practice · Upgrade each sentence</h2>
<button class="btn" type="button" data-revealall>Reveal all answers</button>
<div class="pq"><div class="qh"><span>Q1 · AO2</span><span class="mk">Chain</span></div>
<p class="qt">"A tax on sugary drinks reduces consumption." Turn it into an analysis chain.</p>
<div class="ans"><b>Model</b>The tax raises firms' costs, so supply shifts left; price rises, so quantity demanded contracts. Because consumers now pay closer to the full social cost, consumption falls towards the social optimum.</div></div>
<div class="pq"><div class="qh"><span>Q2 · AO3</span><span class="mk">Evaluate</span></div>
<p class="qt">"However, it depends." Make this specific for the sugar tax.</p>
<div class="ans"><b>Model</b>However, how much consumption falls depends on PED: if demand is price inelastic because of habit, price rises a lot but quantity falls only a little, so the tax raises revenue more than it changes behaviour.</div></div>
<div class="pq"><div class="qh"><span>Q3 · AO1</span><span class="mk">Define</span></div>
<p class="qt">"Public goods are not made by firms because there's no profit." Make it precise.</p>
<div class="ans"><b>Model</b>Public goods are non-excludable and non-rival, so consumers can free ride; no effective demand is revealed, firms cannot charge, so the market provides none (a missing market).</div></div>
<div class="pq"><div class="qh"><span>Q4 · Conclusion</span><span class="mk">AO3</span></div>
<p class="qt">Write a conclusion for: "Assess whether a buffer stock scheme's benefits always outweigh its disadvantages."</p>
<div class="ans"><b>Model</b>Overall, the benefits do not always outweigh the costs because storage and funding are expensive and the scheme fails after repeated bad harvests. However, this depends on the product, so a buffer stock is most likely to succeed for a storable staple such as rice with a realistic target price, and least likely for perishables.</div></div>""", sec="Practice"))

    C.append(card("pr2", "Practice", "Practice: plan these", "Practice", """
<h2>Practice · Two-minute plans</h2>
<p class="lede">Plan each: 2 for, 2 against, 1 "depends on", verdict.</p>
<div class="pq"><div class="qh"><span>Q5</span><span class="mk">[12]</span></div>
<p class="qt">Assess whether a planned economy is more likely than a market economy to achieve a fair distribution of resources.</p>
<div class="ans"><b>Plan</b>For: state distributes evenly, rations essentials, provides merit goods. Against: planning errors cause shortages; corruption favours insiders. Depends on: what "fair" means (a value judgement). Verdict: planned systems aim at fair outcomes but often fail to deliver; a mixed economy is more likely to be fair and efficient.</div></div>
<div class="pq"><div class="qh"><span>Q6</span><span class="mk">[12]</span></div>
<p class="qt">Assess whether knowledge of price elasticity of demand is more useful to a government than to a firm.</p>
<div class="ans"><b>Plan</b>Firm: pricing and revenue, used constantly. Government: which goods to tax for revenue; whether sin taxes change behaviour. Depends on: the goal (revenue vs behaviour change) and data quality. Verdict: more directly useful to a firm; matters more to a government only when the aim is tax revenue.</div></div>
<div class="pq"><div class="qh"><span>Q7</span><span class="mk">[8]</span></div>
<p class="qt">Explain the difference between human and physical capital and consider which is more important for growth in a middle-income economy such as Malaysia.</p>
<div class="ans"><b>Plan</b>Define both with examples; both raise productivity and shift the PPC out. Consider: physical capital drives growth at lower incomes; at middle income, human capital is needed to move up the value chain. Conclude: human capital matters more for Malaysia now, though the two are complements.</div></div>""", sec="Practice"))

    C.append(card("sum", "Summary", "One-card summary", "Summary", f"""
<h2>Essay technique on one card</h2>
<div class="tw"><table>
<tr><td class="k">(a) 8</td><td>Explain… consider · AO 3/3/2 · conclusion mark reserved</td></tr>
<tr><td class="k">(b) 12</td><td>Assess · L3 6–8 + AO3 4 · one-sided = 0 AO3</td></tr>
<tr><td class="k">Timing</td><td>2 min per mark · plan 2 min</td></tr>
<tr><td class="k">12-mark shape</td><td>Intro · For · Against · Evaluate · Conclude</td></tr>
<tr><td class="k">Paragraph</td><td>Point → Explain → Example → Link</td></tr>
<tr><td class="k">Chain words</td><td>because · so · which leads to · therefore</td></tr>
<tr><td class="k">Depends on</td><td>Time · elasticity · development · type of good · government quality</td></tr>
<tr><td class="k">Conclusion</td><td>Overall [answer] because [reason]. However, depends on [factor], so [qualified judgement].</td></tr>
<tr><td class="k">Diagram</td><td>Named axes, labels, referred to in the text</td></tr>
</table></div>
<p class="lede" style="font-size:15px">Original framework: <a href="{ORIG}" target="_blank" rel="noopener">CIE AS Economics Essay Framework</a></p>""", sec="Summary"))
    return C


FLASH = [
    ["Marking", "How many marks are the two parts of an AS essay?", "Part (a) <b>8</b> and part (b) <b>12</b>: 20 in total."],
    ["Marking", "AO split for an 8-mark part (a)?", "AO1 3 · AO2 3 · AO3 2. One AO3 mark is reserved for a justified conclusion."],
    ["Marking", "How is part (b) marked?", "Levels: AO1+AO2 out of 8 (L1 1–2, L2 3–5, L3 6–8) and AO3 out of 4 (L1 1–2, L2 3–4)."],
    ["Marking", "What happens to a one-sided 12-mark answer?", "Capped at Level 2 for AO1/AO2 and <b>0 for AO3</b>."],
    ["Marking", "What is AO1?", "Knowledge and understanding: precise definitions, correct terms, an accurate labelled diagram."],
    ["Marking", "What is AO2?", "Analysis: developed chains of reasoning linking cause to effect, using the diagram."],
    ["Marking", "What is AO3?", "Evaluation: what the answer depends on and why, plus a justified conclusion to the exact question."],
    ["Marking", "Roughly how long per mark in Paper 2?", "2 minutes (2 hours for 60 marks)."],
    ["Structure", "Five parts of a 12-mark answer?", "Intro (define) · case for · case against · evaluation · conclusion."],
    ["Structure", "Three steps for \"Explain… and consider whether…\"?", "Define/distinguish A with an example; define/distinguish B with an example; consider: market alone vs what government adds, then one limit."],
    ["Structure", "Which command words need a judgement?", "Assess, evaluate, discuss (and consider in part a). \"Explain\" doesn't."],
    ["Structure", "What does \"consider\" ask for in part (a)?", "One reasoned \"however / it depends\" point plus a one-line judgement."],
    ["Structure", "What goes in a 2-minute plan?", "2 points for, 2 against, 1 \"depends on\" factor, and your verdict."],
    ["Paragraphs", "What is the paragraph unit?", "Point → Explain (chain of reasoning) → Example → Link to the question."],
    ["Paragraphs", "What turns an assertion into analysis?", "A chain of linked steps with connectives: because, so, which leads to, therefore."],
    ["Paragraphs", "How many examples per paragraph?", "One real example per paragraph."],
    ["Evaluation", "Five \"it depends on\" levers from your framework?", "Time period · elasticity · level of development · type of good or investment · quality of government."],
    ["Evaluation", "Why does generic \"it depends\" score little?", "It doesn't say on what or why. Name the factor and explain how it changes the answer."],
    ["Evaluation", "Where should evaluation go?", "Throughout the essay, not only in the last line."],
    ["Conclusion", "Conclusion template?", "Overall, [answer] because [strongest reason]. However, this depends on [key factor], so [qualified final judgement]."],
    ["Conclusion", "Question says \"always\". How should the conclusion start?", "Answer the exact word: \"not always, because… unless…\"."],
    ["Mistakes", "Why are public goods underprovided? (precise term)", "The <b>free-rider problem</b>: non-excludable, so no effective demand is revealed and firms can't charge."],
    ["Mistakes", "Investment and short-run consumption: what concept fixes the loose logic?", "Opportunity cost: resources move from consumer to capital goods, so short-run consumption falls (movement along the PPC)."],
    ["Mistakes", "Two common diagram mistakes?", "Axes labelled X/Y instead of the named goods; a diagram that isn't referred to in the text."],
]

QUIZ = [
    {"s": "Marking", "q": "How many AO3 marks are available in an 8-mark part (a)?", "o": ["0", "2", "3", "4"], "c": 1, "e": "AO1 3, AO2 3, AO3 2, with one AO3 mark reserved for a justified conclusion."},
    {"s": "Marking", "q": "A 12-mark answer explains only the benefits of a policy, in great detail. What is the maximum AO3 mark?", "o": ["0", "2", "3", "4"], "c": 0, "e": "A one-sided answer cannot gain any AO3 marks, and AO1/AO2 is capped at Level 2."},
    {"s": "Marking", "q": "How is part (b) marked?", "o": ["One mark per valid point", "Levels: AO1+AO2 out of 8, AO3 out of 4", "Out of 25 by levels", "AO1 4, AO2 4, AO3 4 by points"], "c": 1, "e": "Part (b) is levels-based: AO1+AO2 /8 and AO3 /4."},
    {"s": "Command words", "q": "Which command word does NOT require a judgement?", "o": ["Assess", "Evaluate", "Explain", "Discuss"], "c": 2, "e": "Explain needs reasons and relationships, not a verdict."},
    {"s": "Command words", "q": "In \"Explain… and consider whether…\", what does \"consider\" need?", "o": ["A second diagram", "A reasoned \"however\" and a short judgement", "A list of three examples", "Nothing extra"], "c": 1, "e": "Consider is the AO3 part of an 8-marker: one reasoned counterpoint plus a conclusion."},
    {"s": "Structure", "q": "What should the introduction to a 12-mark answer do?", "o": ["Summarise the conclusion", "Define the key term and say what the answer depends on", "List every argument you'll make", "Give a real-world example only"], "c": 1, "e": "1–2 lines: define, then signal what you'll weigh."},
    {"s": "Paragraphs", "q": "Which is the paragraph unit from your framework?", "o": ["Point → Example → Point → Example", "Point → Explain → Example → Link", "Define → List → Conclude", "Diagram → Definition → Evaluation"], "c": 1, "e": "Point, explain with a chain of reasoning, give an example, link back to the question."},
    {"s": "Paragraphs", "q": "Which sentence is an analysis chain rather than an assertion?", "o": ["Taxes reduce consumption.", "The tax is bad for consumers.", "The tax raises costs, so supply shifts left; price rises, so quantity demanded falls.", "Many economists support the tax."], "c": 2, "e": "Only C links cause to effect in steps with connectives."},
    {"s": "Evaluation", "q": "Which is the strongest evaluation?", "o": ["It depends.", "There are pros and cons.", "How far consumption falls depends on PED: with inelastic demand quantity barely falls.", "Some people may disagree."], "c": 2, "e": "It names the factor and explains how it changes the outcome."},
    {"s": "Conclusion", "q": "The question asks \"Are producers the only ones to benefit from more investment?\" Best conclusion opening?", "o": ["Investment leads to a more inclusive growth model.", "No, because consumers also gain from lower prices, though producers gain most in the short run.", "There are many stakeholders.", "Investment is important for growth."], "c": 1, "e": "It answers \"only\" directly with a reason and a qualification."},
    {"s": "Mistakes", "q": "Why are public goods underprovided by the market? (most precise)", "o": ["They make no profit", "The government owns them", "Non-excludability lets people free ride, so no effective demand is revealed", "They are too expensive to produce"], "c": 2, "e": "Use the free-rider problem, not just \"no profit\"."},
    {"s": "Timing", "q": "Roughly how long should a 12-mark part (b) take?", "o": ["About 10 minutes", "About 24 minutes", "About 45 minutes", "About 1 hour"], "c": 1, "e": "2 minutes per mark (2 hours for 60 marks), including a quick plan."},
]


def write():
    meta = {"title": "Essay Technique Deck", "short": "Econ Essays", "bar": "Essay technique",
            "code": "9708 · Paper 2 Sections B and C", "key": "deck-9708-essays"}
    out = engine.render(meta, build(), FLASH, QUIZ)
    pathlib.Path("deck-econ-essays.html").write_text(out, encoding="utf8")
    print("essays", len(out), "bytes,", len(FLASH), "flashcards,", len(QUIZ), "quiz")
