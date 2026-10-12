from essays import figs

TOPIC = {
    "no": 10, "level": "A2", "short": "10 Policy conflicts",
    "title": "Government macroeconomic intervention (A Level)",
    "syllabus": "Objectives · conflicts · Phillips curve · policy effectiveness",
    "why": "A Level policy essays reward seeing trade-offs: what you gain on one objective you often lose on another. The Phillips curve is the standard diagram for that, and supply-side policy is the standard 'way out'.",
    "recycle": {
        "defs": [
            ("Macroeconomic objectives", "<mark>Sustainable growth, low unemployment, stable low inflation, a sustainable balance of payments</mark>, and often a fair distribution of income."),
            ("Short-run Phillips curve", "An <mark>inverse relationship</mark> between unemployment and inflation in the short run."),
            ("Long-run Phillips curve", "<mark>Vertical</mark> at the natural rate of unemployment: no lasting trade-off once expectations adjust."),
            ("Expectations-augmented", "Workers build <mark>expected inflation</mark> into wage claims, so the SRPC shifts up when inflation expectations rise."),
            ("Policy conflict", "When policy to achieve one objective <mark>makes another worse</mark>."),
        ],
        "chains": [
            ("Growth vs inflation", ["AD rises fast", "Output nears capacity", "Bottlenecks", "Inflation rises"]),
            ("Growth vs current account", ["Incomes rise", "Spending on imports rises (high MPM)", "Current account worsens"]),
            ("Unemployment vs inflation (SR)", ["AD up", "Unemployment down", "Labour shortages", "Wages up", "Inflation up"]),
            ("Long run (expectations)", ["Workers expect higher inflation", "Demand higher wages", "SRAS shifts left / SRPC shifts up", "Unemployment back to natural rate at higher inflation"]),
        ],
        "diagrams": [
            ("SRPC and LRPC", "Trade-off and why it disappears in the long run"),
            ("LRAS shift right", "How supply-side policy reduces conflicts"),
            ("AD/AS", "Demand-side policy trade-offs"),
        ],
        "eval": [
            ("Time period", "A trade-off may exist in the short run but disappear in the long run as expectations adjust."),
            ("Supply-side policy", "Shifting LRAS right allows faster growth with lower inflation and unemployment at the same time."),
            ("External shocks", "Global recessions and commodity price swings can push objectives off target whatever the government does."),
            ("Credibility", "An independent central bank with a credible inflation target can lower expectations and ease the trade-off."),
            ("Starting position", "With spare capacity, growth and falling unemployment can coexist with low inflation."),
        ],
        "examples": [
            ("Low inflation, low unemployment", "Malaysia combined steady growth with low inflation through much of the 2010s."),
            ("Conflict", "2022: rising inflation led Bank Negara to raise rates as the economy recovered."),
            ("Central bank independence", "Bank Negara's mandate is set out in the Central Bank of Malaysia Act 2009."),
            ("Supply-side", "Investment in digital infrastructure and skills to raise productivity."),
        ],
        "traps": [
            "Drawing the Phillips curve with output on the axis. It's <b>unemployment</b> against <b>inflation</b>.",
            "Stating the trade-off as permanent. The long-run curve is vertical.",
            "Listing objectives without explaining <i>why</i> they conflict.",
        ],
    },
    "questions": [
        {
            "id": "t10q1", "marks": 8, "title": "The Phillips curve trade-off",
            "q": "Explain the relationship shown by the short-run Phillips curve and consider whether this trade-off exists in the long run.",
            "src": "Past-paper style",
            "keys": [
                ("AO1", "<mark>Diagram</mark>: SRPC (inverse), LRPC vertical at the natural rate; axes inflation and unemployment."),
                ("AO2", "Chain: AD up → unemployment down → <mark>labour shortages</mark> → <mark>wages up</mark> → costs and prices up."),
                ("AO3", "Long run: <mark>expectations adjust</mark> → wage claims include expected inflation → SRPC shifts up → <mark>back to natural rate</mark> at higher inflation."),
                ("AO3", "Conclusion: trade-off is <mark>short-run only</mark>; supply-side policy is needed to lower the natural rate."),
            ],
            "plan": ["Diagram", "A→B: chain of the trade-off", "B→C: expectations", "Verdict: no LR trade-off"],
            "fig": figs.phillips(),
            "answer": [
                ("i", "Define", "The short-run Phillips curve shows an <mark>inverse relationship between unemployment and inflation</mark>: lower unemployment is associated with higher inflation."),
                ("a", "Explain", "If the government raises aggregate demand, firms increase output and hire more workers, so <mark>unemployment falls</mark>, a movement from A to B. As the labour market tightens, firms compete for scarce workers and trade unions are in a stronger position, so <mark>money wages rise</mark>. Higher wages raise firms' costs and, with strong demand, they raise prices, so <mark>inflation rises</mark>. The government seems able to choose lower unemployment at the cost of higher inflation."),
                ("e", "Consider", "In the long run this trade-off is unlikely to last. Once workers notice higher inflation, they <mark>expect it to continue</mark> and demand higher wage rises to protect their real wages. Real labour costs rise again, firms cut back hiring, and unemployment returns to the <mark>natural rate</mark> (Un), but now at a higher inflation rate, point C on a higher SRPC. Repeating the stimulus only raises inflation further, so the <mark>long-run Phillips curve is vertical</mark>."),
                ("c", "Conclusion", "So the trade-off exists only in the <mark>short run</mark>. To reduce unemployment permanently without raising inflation, governments need <mark>supply-side policies</mark> that lower the natural rate itself."),
            ],
            "why": "The diagram points A, B and C structure the whole answer. The analysis explains the mechanism (wages) instead of just stating the inverse relationship, and the evaluation is the key A Level idea of expectations, leading to a policy conclusion.",
        },
        {
            "id": "t10q2", "marks": 12, "title": "Can all objectives be met at once?",
            "q": "Assess whether a government can achieve all of its macroeconomic objectives at the same time.",
            "src": "Past-paper style",
            "keys": [
                ("AO1", "Name the <mark>objectives</mark>: growth, low unemployment, stable inflation, BOP stability."),
                ("AO2", "Conflicts with chains: <mark>unemployment vs inflation</mark> (Phillips curve), <mark>growth vs current account</mark> (imports), <mark>growth vs environment</mark>/sustainability."),
                ("AO2", "Policy example: <mark>higher interest rates</mark> cut inflation but slow growth and raise unemployment."),
                ("AO3", "Possible together: <mark>supply-side policies</mark> shift LRAS right → growth, lower inflation and unemployment, better competitiveness."),
                ("AO3", "Depends on <mark>time period</mark>, <mark>starting position</mark>, <mark>external shocks</mark>."),
                ("AO3", "Verdict: <mark>not in the short run</mark>; more possible in the long run."),
            ],
            "plan": ["List objectives", "Conflict 1: unemployment vs inflation", "Conflict 2: growth vs current account", "Way out: supply-side (LRAS)", "Depends: time, spare capacity, shocks", "Verdict"],
            "answer": [
                ("i", "Intro", "Governments usually aim for <mark>sustainable economic growth, low unemployment, low and stable inflation and a sustainable balance of payments</mark>. Whether these can be achieved together depends on whether the policies used work on <mark>demand or supply</mark>, and on the time period."),
                ("a", "Conflict 1", "Demand-side policies create <mark>conflicts</mark>. Expansionary fiscal or monetary policy raises AD, which increases output and reduces unemployment. But as the economy nears full capacity, labour shortages push up wages and prices, so <mark>inflation rises</mark>: the short-run Phillips curve trade-off. Using higher interest rates to bring inflation down has the opposite problem: it reduces consumption and investment, so growth slows and <mark>unemployment rises</mark>."),
                ("a", "Conflict 2", "Growth can also conflict with the <mark>current account</mark>. As incomes rise, households spend more on imports, especially in an economy with a high propensity to import like Malaysia, so the <mark>current account worsens</mark>. Rapid growth may also cause <mark>pollution and resource depletion</mark>, so it is not sustainable."),
                ("e", "But", "However, the objectives can be achieved together if <mark>supply-side policies</mark> succeed. Better education and training, infrastructure and investment in technology raise productivity, shifting <mark>LRAS to the right</mark>. The economy can then grow faster with <mark>lower inflation</mark>, and lower costs improve <mark>international competitiveness</mark>, helping the current account. If unemployment is structural, training also lowers the natural rate."),
                ("e", "Depends on", "It also depends on the <mark>starting position</mark>: with high unemployment and spare capacity, a rise in AD can increase growth and employment without inflation. But supply-side policies take <mark>years</mark> to work, and <mark>external shocks</mark> such as a global recession or a rise in oil prices can knock several objectives off course at once, whatever the government does."),
                ("c", "Conclusion", "Overall, a government <mark>cannot usually achieve all its objectives at the same time in the short run</mark>, because demand-side policies involve trade-offs. However, in the long run successful supply-side policies make it more possible, so the answer depends on the time period and on avoiding external shocks."),
            ],
            "why": "Conflicts are explained as cause-and-effect chains rather than a list of objectives. The counter-argument is a mechanism (LRAS shift) rather than an assertion, and the conclusion distinguishes short run from long run, which is the judgement examiners want.",
        },
    ],
    "flash": [
        ["T10 Policy conflicts", "Shape of the long-run Phillips curve, and why?", "<b>Vertical</b> at the natural rate: expectations adjust, so wage claims rise and unemployment returns to Un."],
        ["T10 Policy conflicts", "Why can growth worsen the current account?", "Higher incomes raise spending on <b>imports</b>."],
        ["T10 Policy conflicts", "Which policy can reduce several conflicts at once?", "<b>Supply-side</b> policy: LRAS shifts right → growth with lower inflation and better competitiveness."],
        ["T10 Policy conflicts", "Name the four main macro objectives.", "Growth · low unemployment · stable low inflation · sustainable balance of payments."],
    ],
    "quiz": [
        {"s": "T10 Policy conflicts", "q": "The short-run Phillips curve shows…", "o": ["Output vs prices", "An inverse relation between unemployment and inflation", "A positive relation between growth and inflation", "Interest rates vs investment"], "c": 1, "e": "Lower unemployment comes with higher inflation in the short run."},
        {"s": "T10 Policy conflicts", "q": "Which policy is most likely to cut unemployment AND inflation together in the long run?", "o": ["Higher interest rates", "Higher government spending", "Successful supply-side policy", "A tariff"], "c": 2, "e": "Shifting LRAS right raises output and lowers inflationary pressure."},
    ],
}
