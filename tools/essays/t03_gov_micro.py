from essays import figs

TOPIC = {
    "no": 3, "level": "AS", "short": "3 Gov micro",
    "title": "Government microeconomic intervention",
    "syllabus": "Price controls · taxes · subsidies · provision · inequality",
    "why": "Every intervention essay follows the same pattern: what market failure it fixes, the diagram, who gains and loses, and why it might not work. Learn that pattern once and reuse it for taxes, subsidies, price controls and direct provision.",
    "recycle": {
        "defs": [
            ("Maximum price", "A legal price ceiling set <mark>below equilibrium</mark> to make a good more affordable."),
            ("Minimum price", "A legal price floor set <mark>above equilibrium</mark> to raise producers' incomes or reduce consumption."),
            ("Indirect tax", "A tax on spending. <mark>Specific</mark>: fixed amount per unit (parallel shift). <mark>Ad valorem</mark>: percentage of price (pivot)."),
            ("Subsidy", "A payment from government to producers that <mark>lowers their costs</mark>, shifting supply to the right."),
            ("Incidence of a tax", "How the burden of a tax is <mark>shared between consumers and producers</mark>; depends on the relative elasticities."),
            ("Transfer payment", "Money paid by government <mark>with no good or service in return</mark>, e.g. cash aid to low-income households."),
        ],
        "chains": [
            ("Maximum price", ["Set below equilibrium", "Qd rises, Qs falls", "Shortage", "Queues, rationing, black markets"]),
            ("Indirect tax on a demerit good", ["Cost per unit rises", "Supply shifts left", "Price rises", "Qd contracts", "Consumption falls towards the social optimum"]),
            ("Subsidy on a merit good", ["Producers' costs fall", "Supply shifts right", "Price falls", "Consumption rises", "Opportunity cost for government"]),
            ("Direct provision", ["State funds the good from tax", "Free or low price at point of use", "Consumption rises", "Needs funding + efficient delivery"]),
        ],
        "diagrams": [
            ("Max / min price", "Shortage or surplus, black markets"),
            ("Indirect tax with incidence shaded", "Sin taxes, sugar tax, fuel tax"),
            ("Subsidy", "Merit goods, farm support, cost to government"),
        ],
        "eval": [
            ("PED", "How much consumption falls after a tax depends on PED: with inelastic demand, price rises but quantity barely falls."),
            ("Information", "The government needs to know the size of the market failure to set the right tax, subsidy or price, and it rarely does."),
            ("Enforcement", "Price controls need enforcement; without it, black markets develop."),
            ("Opportunity cost", "Money spent on subsidies cannot be spent on schools or hospitals."),
            ("Equity", "Indirect taxes are regressive: low-income households pay a larger share of their income."),
        ],
        "examples": [
            ("Price ceilings", "Malaysia's festive-season maximum price scheme on items like chicken and eggs."),
            ("Sin taxes", "Excise duty on sugary drinks (since 2019) and cigarettes."),
            ("Subsidies", "Fuel, rice and cooking-oil subsidies; the shift to targeted RON95 subsidies."),
            ("Direct provision", "Klinik Kesihatan, public schools, free vaccinations."),
        ],
        "traps": [
            "Drawing a maximum price above equilibrium. It has no effect there.",
            "Not shading or naming the tax incidence areas you talk about.",
            "Forgetting the cost to government (opportunity cost) of subsidies and provision.",
        ],
    },
    "questions": [
        {
            "id": "t3q1", "marks": 8, "title": "Do price ceilings help the poor?",
            "q": "Explain the effects of a maximum price set below the equilibrium price in the market for a staple food and consider whether it benefits low-income households.",
            "src": "Past-paper style",
            "keys": [
                ("AO1", "Define a maximum price; <mark>diagram</mark> with Pmax below Pe, Qs and Qd marked."),
                ("AO2", "<mark>Qd rises, Qs falls</mark> → <mark>shortage</mark> (excess demand)."),
                ("AO2", "Consequences: <mark>queues</mark>, rationing by first-come or favouritism, <mark>black markets</mark>."),
                ("AO3", "Consider: helps those who <mark>get the good</mark>, but lower supply means some get none; black-market price may exceed Pe."),
                ("AO3", "Conclusion: helps only if combined with supply measures or used briefly."),
            ],
            "plan": ["Define + diagram", "Shortage: Qd > Qs", "Queues, black market", "Consider: winners vs losers among the poor", "Verdict: short-term only"],
            "fig": figs.max_price(),
            "answer": [
                ("i", "Define", "A maximum price is a legal ceiling on the price of a good. To have any effect it must be set <mark>below the equilibrium price</mark>, as at Pmax in the figure."),
                ("a", "Effects", "At Pmax, the lower price makes the food more affordable, so <mark>quantity demanded rises</mark> from Qe to Qd. But producers receive less per unit, so less profitable farmers cut output and <mark>quantity supplied falls</mark> to Qs. The result is a <mark>shortage</mark> of Qd − Qs. Because price can no longer ration the good, it is rationed in other ways: <mark>queues</mark>, sellers favouring regular customers, or limits per buyer. Some buyers will pay more than Pmax, so a <mark>black market</mark> may develop, where the good sells illegally at prices up to Pbm."),
                ("e", "Consider", "Low-income households who manage to buy at Pmax clearly benefit, because a staple takes a large share of their income. However, total supply has fallen, so <mark>some poor households get nothing</mark>, and those without time to queue may have to pay the <mark>black-market price</mark>, which is higher than the original equilibrium. In the long run, lower farm incomes may reduce investment, making shortages worse."),
                ("c", "Conclusion", "So a maximum price helps low-income households <mark>only partly and only in the short term</mark>, such as Malaysia's festive-season ceilings. It works better alongside a subsidy to producers that keeps supply from falling."),
            ],
            "why": "The diagram does half the AO1 work. The chain is precise (quantity demanded and quantity supplied, not demand and supply). 'Consider' identifies winners and losers within the same group, which is a sharper evaluation than 'it has pros and cons'.",
        },
        {
            "id": "t3q2", "marks": 12, "title": "Is a tax the best way to cut sugar?",
            "q": "Assess whether an indirect tax is the most effective way for a government to reduce the consumption of sugary drinks.",
            "src": "Past-paper style",
            "keys": [
                ("AO1", "Define <mark>indirect tax</mark>; sugary drinks as a <mark>demerit good</mark>; <mark>diagram</mark> with incidence."),
                ("AO2", "Tax → <mark>supply shifts left</mark> → <mark>price rises</mark> → <mark>Qd contracts</mark>; also raises <mark>revenue</mark>; makes firms reformulate."),
                ("AO2", "Alternatives: <mark>information campaigns</mark>, <mark>regulation</mark> (limits, labelling, school bans), subsidising healthy options."),
                ("AO3", "Effectiveness <mark>depends on PED</mark>: habit-forming → inelastic → small fall in quantity."),
                ("AO3", "<mark>Regressive</mark>; needs the right rate; substitution to untaxed sugar."),
                ("AO3", "Verdict: most effective <mark>as part of a policy mix</mark>."),
            ],
            "plan": ["Define demerit good + tax", "For: price signal, revenue, reformulation", "Against: inelastic demand, regressive, substitution", "Compare: information, regulation", "Verdict: best in a mix"],
            "fig": figs.tax_inelastic(),
            "answer": [
                ("i", "Intro", "Sugary drinks are a <mark>demerit good</mark>: consumers underestimate the harm to their health, so they are <mark>over-consumed</mark> in a free market. An <mark>indirect tax</mark> is a tax on spending, such as Malaysia's excise duty on sugary drinks introduced in 2019. Whether it is the most effective tool depends largely on how consumers respond to price."),
                ("a", "For", "A tax raises producers' costs per unit, so <mark>supply shifts left</mark> by the amount of the tax. The equilibrium <mark>price rises</mark> from P0 to P1, so <mark>quantity demanded contracts</mark> from Q0 to Q1. Consumers now pay closer to the full cost of the drinks, so consumption moves towards the socially optimal level. The tax also <mark>raises revenue</mark>, which can fund health campaigns or clinics, and it gives firms an incentive to <mark>reformulate</mark> drinks with less sugar to avoid the tax."),
                ("e", "Against", "However, demand for sugary drinks is likely to be <mark>price inelastic</mark> because they are habit-forming and cheap relative to income. As the figure shows, most of the tax is passed on to consumers as a higher price, but <mark>quantity falls only a little</mark>, so the tax raises revenue more than it changes behaviour. The tax is also <mark>regressive</mark>, taking a bigger share of income from poorer households, and consumers may switch to untaxed sugary foods or homemade drinks."),
                ("a", "Alternatives", "Other policies attack the cause directly. <mark>Information campaigns</mark> and clear labelling correct the information failure behind over-consumption and may change habits permanently. <mark>Regulation</mark>, such as banning sugary drinks in school canteens, reduces consumption among children with certainty, though it is hard to enforce widely and removes choice."),
                ("c", "Conclusion", "Overall, an indirect tax is <mark>not the most effective policy on its own</mark>, because inelastic demand means consumption falls only slightly. However, it is a useful part of a <mark>policy mix</mark>: the tax revenue can fund education and labelling, which make demand more elastic over time, so the tax becomes more effective the longer it is combined with them."),
            ],
            "why": "The PED evaluation is tied to the diagram, which is exactly what examiners mean by 'developed' evaluation. The comparison with alternatives answers 'most effective', and the conclusion makes a judgement with a reason (inelastic demand) and a condition (policy mix makes demand more elastic).",
        },
    ],
    "flash": [
        ["T3 Gov micro", "Effect of a maximum price below equilibrium?", "Qd rises, Qs falls → <b>shortage</b> → queues, rationing, black markets."],
        ["T3 Gov micro", "Why is an indirect tax regressive?", "Low-income households pay a <b>larger share of their income</b> in the tax."],
        ["T3 Gov micro", "When does a sin tax mainly raise revenue rather than cut consumption?", "When demand is <b>price inelastic</b>."],
        ["T3 Gov micro", "Specific vs ad valorem tax on the diagram?", "Specific: <b>parallel</b> shift of S. Ad valorem: S <b>pivots</b>, gap widens as price rises."],
    ],
    "quiz": [
        {"s": "T3 Gov micro", "q": "A maximum price is set above the equilibrium price. The effect is…", "o": ["A shortage", "A surplus", "No effect", "A black market"], "c": 2, "e": "A ceiling above equilibrium doesn't bind: the market price is already lower."},
        {"s": "T3 Gov micro", "q": "Demand for cigarettes is very inelastic. A tax will mainly…", "o": ["Cut consumption sharply", "Raise revenue with a small fall in quantity", "Be paid by producers", "Lower the price"], "c": 1, "e": "Most of the tax is passed on and quantity barely changes."},
    ],
}
