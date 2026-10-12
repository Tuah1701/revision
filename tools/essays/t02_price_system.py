from essays import figs

TOPIC = {
    "no": 2, "level": "AS", "short": "2 Price system",
    "title": "The price system and the microeconomy",
    "syllabus": "Demand · supply · elasticities · equilibrium · surplus",
    "why": "Elasticity is the most recyclable idea in AS Economics. It decides tax incidence, revenue, how much a price changes after a shock, and it's the go-to 'it depends on' in almost every micro essay.",
    "recycle": {
        "defs": [
            ("Effective demand", "The quantity consumers are <mark>willing and able</mark> to buy at each price, ceteris paribus."),
            ("PED", "The <mark>responsiveness of quantity demanded to a change in the good's own price</mark>, ceteris paribus. %ΔQd ÷ %ΔP."),
            ("YED", "The responsiveness of demand to a <mark>change in income</mark>. Positive = <mark>normal</mark> good (0–1 necessity, &gt;1 luxury); negative = <mark>inferior</mark>."),
            ("XED", "The responsiveness of demand for good A to a change in the price of good B. Positive = <mark>substitutes</mark>, negative = <mark>complements</mark>."),
            ("PES", "The responsiveness of <mark>quantity supplied</mark> to a change in price. %ΔQs ÷ %ΔP."),
            ("Consumer surplus", "The difference between what consumers are <mark>willing to pay</mark> and what they <mark>actually pay</mark>."),
        ],
        "chains": [
            ("Revenue and PED", ["Demand elastic", "Price cut → proportionately larger rise in Qd", "TR rises", "(Inelastic: raise price to raise TR)"]),
            ("Tax incidence", ["Indirect tax shifts S up", "If demand inelastic", "Consumers can't switch", "Most of the tax is passed on as a higher price"]),
            ("PES and time", ["Price rises", "Short run: fixed capacity, crops take time", "Qs barely rises (inelastic)", "Long run: new capacity, planting", "Qs rises more (elastic)"]),
            ("Price after a supply shock", ["Supply falls", "Shortage at old price", "Price rises", "How much depends on PED"]),
        ],
        "diagrams": [
            ("D/S shift", "Any shock: new equilibrium price and quantity"),
            ("TR rectangles", "Pricing decisions and PED"),
            ("CS / PS", "Welfare effects of a price change"),
            ("Steep vs flat curve", "Inelastic vs elastic demand or supply"),
        ],
        "eval": [
            ("Accuracy of estimates", "Elasticity values are estimated from past data when other factors were also changing, so they may be unreliable guides to the future."),
            ("Time period", "Demand and supply are more elastic in the long run, as buyers find substitutes and firms expand capacity."),
            ("Position on the curve", "PED is not constant along a straight-line demand curve, so a price change may push the good into a different elasticity range."),
            ("Rival reactions", "A firm's own price elasticity depends on whether competitors match its price change."),
        ],
        "examples": [
            ("Inelastic demand", "RON95 petrol, rice, cigarettes: few substitutes, necessities or habit-forming."),
            ("Elastic demand", "A single brand of mass-market car or smartphone with many close substitutes."),
            ("YED", "Luxury cars YED &gt;1; budget models and buses may be inferior as incomes rise."),
            ("Inelastic supply", "Durians and palm oil in the short run: trees take years to mature."),
        ],
        "traps": [
            "Writing 'price rises so demand falls'. It's <b>quantity demanded</b> (a movement), not demand (a shift).",
            "Forgetting 'ceteris paribus' in an elasticity definition.",
            "Saying inelastic means 'consumers don't respond at all'. That's perfectly inelastic (PED = 0).",
        ],
    },
    "questions": [
        {
            "id": "t2q1", "marks": 8, "title": "Why is farm supply inelastic?",
            "q": "Explain the factors that determine the price elasticity of supply of a product and consider why the price elasticity of supply of agricultural products such as durians is often lower than that of manufactured goods.",
            "src": "Past-paper style",
            "keys": [
                ("AO1", "Define PES with the formula: <mark>%ΔQs ÷ %ΔP</mark>; elastic &gt;1, inelastic &lt;1."),
                ("AO2", "Determinants: <mark>spare capacity</mark>, <mark>stocks</mark>, <mark>time period</mark>, <mark>factor mobility</mark>, length of the production period."),
                ("AO2", "Each explained as a chain: why it lets firms raise output quickly or not."),
                ("AO3", "Consider: durians have a <mark>long growing period</mark>, are <mark>perishable</mark> (no stocks) and depend on <mark>weather</mark>."),
                ("AO3", "Conclusion: lower in the short run, but the gap narrows in the long run."),
            ],
            "plan": ["Define PES", "Capacity, stocks, time, factor mobility", "Consider: durians vs factory goods", "Verdict: short run yes, long run less so"],
            "answer": [
                ("i", "Define", "Price elasticity of supply (PES) measures the <mark>responsiveness of quantity supplied to a change in price</mark>, ceteris paribus, calculated as %ΔQs ÷ %ΔP. Supply is elastic if PES is greater than 1 and inelastic if it is less than 1."),
                ("a", "Factors", "PES depends on how easily firms can raise output when price rises. If firms have <mark>spare capacity</mark>, they can increase production quickly by using idle machines and workers, so supply is elastic. If they hold <mark>stocks</mark> of finished goods, they can release them onto the market immediately. <mark>Time</mark> matters: in the short run at least one factor is fixed, but in the long run firms can build new factories, so supply becomes more elastic. Finally, if <mark>factors of production are mobile</mark> and can easily be switched from another product, output can respond faster."),
                ("e", "Consider", "Agricultural products like durians usually have lower PES. A durian tree takes several years to bear fruit, so the <mark>production period is long</mark> and farmers cannot respond to a higher price this season. Durians are <mark>perishable</mark>, so no stocks can be held, and output depends on <mark>weather</mark>, not just farmers' decisions. A factory making electronics, by contrast, can add a shift or draw on inventory within weeks."),
                ("c", "Conclusion", "So durian supply is much less elastic than manufactured goods in the short run. In the long run, however, farmers can plant more trees and cold storage can extend shelf life, so the <mark>gap narrows over time</mark>."),
            ],
            "why": "Four determinants, each with a 'so…' explaining the mechanism, is enough for full AO2. The 'consider' part applies three of them specifically to durians rather than repeating the list, and the conclusion adds time as the qualifier.",
        },
        {
            "id": "t2q2", "marks": 12, "title": "PED or YED for a car firm?",
            "q": "Assess whether price elasticity of demand (PED) or income elasticity of demand (YED) is likely to be of greater importance to a firm producing cars.",
            "src": "Your teacher's sample, rewritten to exam length",
            "keys": [
                ("AO1", "Define <mark>PED</mark> and <mark>YED</mark> precisely, with ceteris paribus."),
                ("AO1", "Diagram: <mark>TR rectangles</mark> for elastic and inelastic demand."),
                ("AO2", "PED → <mark>pricing and total revenue</mark>: elastic → cut price; inelastic → raise price; passing on cost increases."),
                ("AO2", "YED → cars are <mark>normal goods</mark>, luxury cars <mark>YED &gt; 1</mark> → sales swing with the <mark>business cycle</mark> → output, capacity and product-mix planning."),
                ("AO3", "Weigh: firm <mark>controls price</mark> but <mark>cannot control income</mark>; <mark>rivals react</mark> in an oligopoly; estimates are unreliable."),
                ("AO3", "Judgement <mark>depends on time horizon and segment</mark> (mass-market vs luxury)."),
            ],
            "plan": ["Define PED + YED", "PED: pricing, TR, cost pass-through", "YED: business cycle, planning, product mix", "Weigh: control, rivals, data", "Verdict: PED short run, YED long run / luxury"],
            "fig": figs.ped_tr(),
            "answer": [
                ("i", "Intro", "<mark>PED</mark> measures the responsiveness of quantity demanded to a change in the good's own price, ceteris paribus, while <mark>YED</mark> measures the responsiveness of demand to a change in consumers' income. Which matters more to a car producer depends on the <mark>time horizon</mark> and the <mark>type of car</mark> it sells."),
                ("a", "PED", "PED is important because it tells the firm how a price change will affect <mark>total revenue</mark>. A mass-market brand such as Proton competes with close substitutes like Perodua and Toyota, so its demand is likely to be <mark>price elastic</mark>: a price cut causes a proportionately larger rise in quantity demanded, so revenue rises, as shown by the gain area exceeding the loss area in the figure. A luxury brand with loyal buyers has more <mark>inelastic</mark> demand, so it can raise price and increase revenue. PED also tells the firm how much of a <mark>cost increase</mark>, such as dearer steel or a higher sales tax, it can pass on without losing many sales."),
                ("a", "YED", "YED matters because cars are <mark>normal goods</mark> with high positive YED, and luxury cars may have <mark>YED greater than 1</mark>. Cars are expensive and often bought on credit, so when incomes rise in a boom, demand rises more than proportionately, and in a recession sales collapse. Knowing YED helps the firm <mark>plan output, capacity and stock levels</mark> for the business cycle, and to <mark>diversify its product range</mark>, for example adding cheaper models whose sales hold up better when incomes fall."),
                ("e", "Weighing", "PED is more <mark>immediately useful</mark> because price is a variable the firm <mark>controls</mark>, while it cannot control incomes and must rely on uncertain forecasts. However, the car market is an <mark>oligopoly</mark>, so if rivals match a price cut, the firm's demand is far less elastic than it estimated. Income changes, in contrast, shift the <mark>whole demand curve</mark>, and are often the largest source of swings in car sales. Both measures assume ceteris paribus, while car demand also depends on interest rates and government incentives such as tax exemptions for electric vehicles."),
                ("c", "Conclusion", "Overall, PED is likely to be of greater importance for a mass-market car firm in the <mark>short run</mark>, because it directly guides pricing and revenue. However, YED is more important for <mark>long-run planning</mark>, and especially for luxury producers whose sales depend on the economic cycle, so the answer depends on the segment the firm competes in."),
            ],
            "why": "This keeps every point from your teacher's sample that earns marks but drops repetition, so it fits the 24 minutes a 12-marker gets. Both sides are applied to cars, not explained in general. The evaluation weighs the two against each other (control, rivals, size of income shocks) instead of listing limitations separately, and the conclusion picks a side with conditions.",
        },
    ],
    "flash": [
        ["T2 Price system", "Define PED.", "Responsiveness of <b>quantity demanded</b> to a change in the good's <b>own price</b>, ceteris paribus. %ΔQd ÷ %ΔP."],
        ["T2 Price system", "Demand is price elastic. How should a firm change price to raise TR?", "<b>Cut</b> the price: Qd rises proportionately more, so TR rises."],
        ["T2 Price system", "YED of a luxury good?", "Positive and <b>greater than 1</b>."],
        ["T2 Price system", "Four determinants of PES.", "Spare capacity · stocks · time period · factor mobility (plus length of production period)."],
        ["T2 Price system", "Who bears most of an indirect tax when demand is inelastic?", "<b>Consumers</b>: they can't easily switch, so most of the tax is passed on in a higher price."],
    ],
    "quiz": [
        {"s": "T2 Price system", "q": "A car firm's demand has PED = −1.5. A 10% price cut will…", "o": ["Reduce TR", "Raise Qd by 15% and raise TR", "Raise Qd by 1.5%", "Leave TR unchanged"], "c": 1, "e": "Elastic: %ΔQd (15%) exceeds %ΔP (10%), so total revenue rises."},
        {"s": "T2 Price system", "q": "Why is YED often more important to a luxury car brand than to a budget brand?", "o": ["Luxury cars are inferior goods", "Luxury cars have YED > 1, so sales swing strongly with the business cycle", "Luxury buyers never respond to income", "Budget cars have no substitutes"], "c": 1, "e": "High YED means demand rises and falls more than proportionately with income."},
    ],
}
