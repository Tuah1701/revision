from essays import figs

TOPIC = {
    "no": 4, "level": "AS", "short": "4 Macroeconomy",
    "title": "The macroeconomy",
    "syllabus": "National income · AD/AS · growth · unemployment · inflation",
    "why": "AD/AS is the macro equivalent of demand and supply: almost every macro essay needs it. The shape of the AS curve is your strongest 'it depends on' in this whole topic.",
    "recycle": {
        "defs": [
            ("Aggregate demand", "Total planned spending on an economy's goods and services at each price level: <mark>AD = C + I + G + (X − M)</mark>."),
            ("Aggregate supply", "Total output producers are willing and able to supply at each price level."),
            ("Inflation", "A <mark>sustained rise in the general price level</mark>, measured by a price index such as the CPI."),
            ("Demand-pull inflation", "Inflation caused by <mark>AD rising faster than the economy's capacity</mark> to produce."),
            ("Cost-push inflation", "Inflation caused by <mark>rising costs of production</mark> (wages, imported raw materials, energy) shifting AS left."),
            ("Unemployment", "People of working age who are <mark>willing and able to work and actively seeking work</mark> but without a job."),
            ("Real GDP", "GDP adjusted for inflation, so it measures changes in the <mark>volume of output</mark>."),
        ],
        "chains": [
            ("AD rise with spare capacity", ["AD rises", "Firms use idle resources", "Output and employment rise", "Little pressure on prices"]),
            ("AD rise near capacity", ["AD rises", "Bottlenecks, labour shortages", "Costs and prices rise", "Demand-pull inflation"]),
            ("Cost-push", ["Oil or import prices rise", "Firms' costs rise", "AS shifts left", "Price level up AND output down (stagflation)"]),
            ("Inflation → competitiveness", ["Domestic prices rise faster than rivals'", "Exports dearer, imports cheaper", "X falls, M rises", "Current account worsens"]),
        ],
        "diagrams": [
            ("Keynesian AS (three ranges)", "Whether higher AD causes output or inflation"),
            ("AD shift", "Demand-pull inflation, growth from spending"),
            ("SRAS shift left", "Cost-push inflation, stagflation"),
            ("LRAS shift right", "Long-run growth, supply-side improvements"),
        ],
        "eval": [
            ("Spare capacity", "The effect of higher AD depends on where the economy is on its AS curve: with high unemployment, output rises with little inflation."),
            ("Cause", "Which policy works depends on whether inflation is demand-pull or cost-push."),
            ("Anticipated or not", "Anticipated inflation does less harm, because wages and contracts adjust."),
            ("Openness", "In an open economy like Malaysia, a large share of inflation is imported through food, energy and the exchange rate."),
        ],
        "examples": [
            ("Imported inflation", "Global food and energy prices in 2022 and a weaker ringgit in 2023 raised Malaysian import costs."),
            ("Demand-side growth", "Post-pandemic recovery in consumer spending and tourism."),
            ("Policy body", "Bank Negara Malaysia sets the Overnight Policy Rate (OPR)."),
            ("Structural unemployment", "Workers displaced by automation in manufacturing."),
        ],
        "traps": [
            "Calling any price rise 'inflation'. It must be a <b>sustained rise in the general price level</b>.",
            "Saying inflation means 'prices are high'. A falling inflation rate still means prices are rising, just more slowly.",
            "Drawing AD/AS without labelling the axes 'Price level' and 'Real output'.",
        ],
    },
    "questions": [
        {
            "id": "t4q1", "marks": 8, "title": "Demand-pull vs cost-push",
            "q": "Explain the difference between demand-pull and cost-push inflation and consider which type is likely to be more harmful to an economy.",
            "src": "Past-paper style",
            "keys": [
                ("AO1", "Define <mark>inflation</mark>; define both types precisely."),
                ("AO2", "Demand-pull: <mark>AD shifts right</mark> beyond capacity → price level rises, <mark>output rises</mark>."),
                ("AO2", "Cost-push: <mark>AS shifts left</mark> → price level rises, <mark>output falls</mark> (<mark>stagflation</mark>)."),
                ("AO3", "Consider: cost-push is usually <mark>more harmful</mark> (inflation + unemployment, policy dilemma)."),
                ("AO3", "But demand-pull can become embedded via <mark>wage-price spiral</mark>; depends on size and persistence."),
            ],
            "plan": ["Define inflation", "Demand-pull: AD right, output ↑", "Cost-push: AS left, output ↓", "Consider: stagflation + policy dilemma", "Verdict: cost-push usually worse"],
            "answer": [
                ("i", "Define", "Inflation is a <mark>sustained rise in the general price level</mark>. The two types differ in whether the cause is on the demand side or the supply side."),
                ("a", "Demand-pull", "<mark>Demand-pull inflation</mark> occurs when aggregate demand rises faster than the economy's capacity, for example after a consumer boom or a large rise in government spending. AD shifts right; as the economy nears full employment, firms face shortages of labour and materials, so they raise prices. The <mark>price level rises but so does real output</mark>."),
                ("a", "Cost-push", "<mark>Cost-push inflation</mark> occurs when firms' costs rise, for example higher imported energy and food prices or a weaker currency. AS shifts left, so firms raise prices to protect profits while cutting output. The <mark>price level rises while output falls</mark> and unemployment rises: <mark>stagflation</mark>."),
                ("e", "Consider", "Cost-push inflation is usually <mark>more harmful</mark>, because it combines rising prices with falling output and jobs, and it creates a <mark>policy dilemma</mark>: raising interest rates to fight inflation deepens the fall in output. Demand-pull at least comes with growth. However, if demand-pull inflation persists, workers demand higher wages, starting a <mark>wage-price spiral</mark> that is hard to stop."),
                ("c", "Conclusion", "So cost-push inflation is generally more harmful, although <mark>persistent demand-pull inflation</mark> can become just as damaging once expectations rise."),
            ],
            "why": "The difference is shown through what happens to output, not just the cause, which is the AO2 insight markers look for. 'Consider' gives a reason (stagflation and the policy dilemma) and a counterpoint (wage-price spiral), then a one-line verdict.",
        },
        {
            "id": "t4q2", "marks": 12, "title": "Does more AD always mean inflation?",
            "q": "Assess whether an increase in aggregate demand will always lead to inflation.",
            "src": "Past-paper style",
            "keys": [
                ("AO1", "Define <mark>AD</mark> (C + I + G + X − M) and <mark>inflation</mark>; Keynesian AS <mark>diagram</mark> with three AD curves."),
                ("AO2", "With <mark>spare capacity</mark>: idle resources → <mark>output rises, prices stable</mark>."),
                ("AO2", "Near <mark>full employment</mark>: bottlenecks → <mark>prices rise</mark>; at capacity only prices rise."),
                ("AO3", "Depends on: <mark>size of the AD increase</mark>, <mark>where the economy starts</mark>, whether <mark>AS also shifts</mark> (investment raises capacity)."),
                ("AO3", "Classical view: in the long run AS is vertical, so only prices rise."),
                ("AO3", "Verdict: <mark>not always</mark>."),
            ],
            "plan": ["Define AD + inflation", "Diagram: 3 ranges", "Spare capacity → output", "Near capacity → prices", "Depends: start point, size, AS shifts", "Verdict: not always"],
            "fig": figs.keynes_as(),
            "answer": [
                ("i", "Intro", "<mark>Aggregate demand</mark> is total planned spending in an economy, C + I + G + (X − M). <mark>Inflation</mark> is a sustained rise in the general price level. Whether higher AD causes inflation depends on how much <mark>spare capacity</mark> the economy has, which is shown by the shape of the aggregate supply curve."),
                ("a", "No inflation", "When the economy has high unemployment and idle factories, AS is horizontal. An increase from AD1 raises <mark>real output without raising the price level</mark>, because firms can expand by employing idle workers and machines at existing wages and costs. For example, in a recovery after a recession, higher consumer spending raises output and employment with little effect on prices. Here higher AD does <mark>not</mark> cause inflation."),
                ("a", "Inflation", "As the economy approaches full capacity (AD2), some industries face <mark>bottlenecks</mark> and shortages of skilled labour, so firms bid up wages and raise prices; both output and the price level rise. At full employment output Yfe, AS is vertical: a rise to AD3 cannot increase output, so <mark>only the price level rises</mark>. This is pure demand-pull inflation."),
                ("e", "Depends on", "So the outcome depends on <mark>where the economy starts</mark> and <mark>how large the increase is</mark>: a small rise in AD in a recession is unlikely to be inflationary, but a large stimulus near full employment will be. It also depends on whether AS shifts at the same time: if the rise in AD comes from <mark>investment</mark>, it also adds to productive capacity, shifting AS right and reducing inflationary pressure. In an open economy like Malaysia, some extra spending <mark>leaks into imports</mark>, so less of it reaches domestic prices. Classical economists argue that in the long run AS is vertical, so any lasting rise in AD only raises prices."),
                ("c", "Conclusion", "Overall, an increase in AD will <mark>not always</mark> lead to inflation, because with spare capacity it mainly raises output. However, the closer the economy is to full employment, the more of the increase turns into inflation, so the risk is greatest when unemployment is already low."),
            ],
            "why": "The Keynesian AS diagram carries the whole argument: each range is one paragraph. The evaluation goes beyond 'it depends on spare capacity' to the size of the change, investment shifting AS, and import leakage, and the conclusion answers 'always' with the condition that would make it true.",
        },
    ],
    "flash": [
        ["T4 Macroeconomy", "Components of AD?", "C + I + G + (X − M)."],
        ["T4 Macroeconomy", "Cost-push inflation: what happens to output?", "AS shifts left, so <b>output falls</b> while prices rise (stagflation)."],
        ["T4 Macroeconomy", "Why might higher AD not cause inflation?", "If there is <b>spare capacity</b>, firms raise output using idle resources without raising prices."],
        ["T4 Macroeconomy", "Define inflation (precise).", "A <b>sustained rise in the general price level</b>."],
    ],
    "quiz": [
        {"s": "T4 Macroeconomy", "q": "On the vertical range of the Keynesian AS curve, a rise in AD causes…", "o": ["Higher output, same prices", "Higher prices, same output", "Both rise equally", "Lower prices"], "c": 1, "e": "At full capacity output can't rise, so only the price level increases."},
        {"s": "T4 Macroeconomy", "q": "A sharp rise in world oil prices is most likely to cause…", "o": ["Demand-pull inflation", "Cost-push inflation and lower output", "Deflation", "Higher output and lower prices"], "c": 1, "e": "Higher costs shift AS left: stagflation."},
    ],
}
