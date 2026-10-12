"""9708 Economics Essay Bank deck.

One deck for every syllabus topic. Each topic lives in its own file, tools/essays/tNN_*.py, defining TOPIC
(see tools/essays/README.md for the schema). This module discovers those files, so `/deck essay <topic>`
only has to add questions to the right topic file and rebuild.

Per topic the deck shows:
  1. a "Recycle these" front page: definitions, analysis chains, diagrams, evaluation and examples worth
     memorising because they come back in essay after essay;
  2. one card per essay question: the key points the examiner wants (highlighted), a 2-minute plan,
     a diagram where one earns marks, and a model answer at real exam length behind a reveal button
     (with the Apple Pencil "Write your working" space attached).

Usage: python3 essaybank.py   -> writes deck-econ-essaybank.html
"""
import importlib, pathlib, re, html as _h
import engine
from engine import card

HERE = pathlib.Path(__file__).parent
WPM = 22  # realistic handwriting speed under exam pressure

# Minutes per mark: 2 hours for 60 marks (Tuah's confirmed paper format).
MIN_PER_MARK = {"AS": 2.0, "A2": 2.0}

EXTRA_CSS = """<style>
mark{background:var(--accent-soft);color:var(--fg);padding:0 .18em;border-radius:4px;-webkit-box-decoration-break:clone;box-decoration-break:clone;font-weight:600}
.qbox{background:var(--surface);border:1px solid var(--line);border-left:4px solid var(--accent);border-radius:12px;padding:12px 15px;margin:10px 0 6px}
.qbox p{margin:.35em 0 0;font-size:17.5px;line-height:1.5}
.meta{display:flex;flex-wrap:wrap;gap:6px;margin:8px 0 2px}
.meta span{font:600 11px/1 var(--f-mono);letter-spacing:.05em;text-transform:uppercase;color:var(--muted);border:1px solid var(--line);border-radius:999px;padding:5px 8px}
ul.keys{list-style:none;padding:0;margin:10px 0;display:grid;gap:7px}
ul.keys li{background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:9px 12px;margin:0;font-size:16px}
.ao{display:inline-block;font:700 10px/1 var(--f-mono);letter-spacing:.06em;padding:4px 6px;border-radius:6px;margin-right:7px;vertical-align:2px}
.ao.a1{color:var(--accent);background:var(--accent-soft)}
.ao.a2{color:var(--teal);background:var(--teal-soft)}
.ao.a3{color:var(--good);background:var(--good-soft)}
.ma p{margin:.75em 0;line-height:1.6}
.pl{display:inline-block;font:700 10px/1 var(--f-mono);letter-spacing:.06em;text-transform:uppercase;padding:4px 6px;border-radius:6px;margin-right:7px;vertical-align:2px;color:var(--teal);background:var(--teal-soft)}
.pl.i,.pl.c{color:var(--accent);background:var(--accent-soft)}
.pl.e{color:var(--good);background:var(--good-soft)}
.wc{font:600 12px/1.4 var(--f-mono);color:var(--muted);border-top:1px dashed var(--line);padding-top:8px;margin-top:10px}
.rc h3{display:flex;align-items:center;gap:8px}
.rc h3 .n{font:700 11px/1 var(--f-mono);color:var(--on-accent);background:var(--accent);border-radius:6px;padding:4px 6px}
.rc .def{margin:8px 0}
.rc .chain{margin:6px 0 12px}
.rc .chain span{font-size:14px}
.cname{font:600 11px/1.3 var(--f-mono);letter-spacing:.06em;text-transform:uppercase;color:var(--muted);margin:12px 0 0}
</style>"""


def esc(s):
    return _h.escape(s, quote=False)


# ---------------------------------------------------------------- discovery
def load_topics():
    topics = []
    for f in sorted((HERE / "essays").glob("t[0-9][0-9]_*.py")):
        mod = importlib.import_module(f"essays.{f.stem}")
        topics.append(mod.TOPIC)
    return sorted(topics, key=lambda t: t["no"])


# ---------------------------------------------------------------- rendering
def recycle_html(t):
    r = t["recycle"]
    out = [f'<p class="lede">{t["why"]}</p>']
    n = 0

    def head(title):
        nonlocal n
        n += 1
        return f'<h3><span class="n">{n}</span>{title}</h3>'

    if r.get("defs"):
        out.append(head("Definitions to learn word for word"))
        for term, d in r["defs"]:
            out.append(f'<div class="def"><span class="lab">{term}</span><p>{d}</p></div>')
    if r.get("chains"):
        out.append(head("Analysis chains to recycle"))
        for name, steps in r["chains"]:
            out.append(f'<p class="cname">{name}</p><div class="chain">'
                       + '<i>→</i>'.join(f"<span>{s}</span>" for s in steps) + "</div>")
    if r.get("diagrams"):
        out.append(head("Diagrams to have ready"))
        out.append('<div class="tw"><table><tr><th>Diagram</th><th>Use it for</th></tr>'
                   + "".join(f'<tr><td class="k">{a}</td><td>{b}</td></tr>' for a, b in r["diagrams"])
                   + "</table></div>")
    if r.get("eval"):
        out.append(head("Evaluation you can reuse"))
        out.append('<div class="tw"><table><tr><th>It depends on…</th><th>Sentence to adapt</th></tr>'
                   + "".join(f'<tr><td class="k">{a}</td><td>{b}</td></tr>' for a, b in r["eval"])
                   + "</table></div>")
    if r.get("examples"):
        out.append(head("Examples to drop in"))
        out.append('<div class="two">' + "".join(f"<div><h4>{a}</h4><p>{b}</p></div>" for a, b in r["examples"]) + "</div>")
    if r.get("traps"):
        out.append('<div class="note trap"><b>Marks students lose here</b><ul>'
                   + "".join(f"<li>{x}</li>" for x in r["traps"]) + "</ul></div>")
    return "".join(out)


AO_CLASS = {"AO1": "a1", "AO2": "a2", "AO3": "a3"}
PL_CLASS = {"i": "i", "a": "", "e": "e", "c": "c"}


def words(html):
    return len(re.sub(r"<[^>]+>", " ", html).split())


def question_html(t, q):
    mins = round(q["marks"] * MIN_PER_MARK[t["level"]])
    # Sections: A = data response, B = micro essay, C = macro essay (Paper 2 AS, Paper 4 A Level)
    paper = ("Paper 2" if t["level"] == "AS" else "Paper 4") + (" · Sect B" if t["no"] in (1, 2, 3, 7, 8) else " · Sect C")
    keys = "".join(f'<li><span class="ao {AO_CLASS[ao]}">{ao}</span>{txt}</li>' for ao, txt in q["keys"])
    plan = '<div class="chain">' + "<i>→</i>".join(f"<span>{s}</span>" for s in q["plan"]) + "</div>"
    paras = "".join(f'<p><span class="pl {PL_CLASS[k]}">{lab}</span>{txt}</p>' for k, lab, txt in q["answer"])
    n = words(paras) - sum(len(lab.split()) for _, lab, _ in q["answer"])
    write_min = round(n / WPM)
    src = f'<span>{q["src"]}</span>' if q.get("src") else ""
    return f"""<h2>{q['title']}</h2>
<div class="qbox"><div class="meta"><span>{q['marks']} marks</span><span>{paper}</span><span>~{mins} min</span>{src}</div>
<p>{q['q']}</p></div>
<h3>Key points the examiner wants</h3>
<ul class="keys">{keys}</ul>
<h3>Two-minute plan</h3>
{plan}
{q.get('fig', '')}
<div class="pq"><div class="qh"><span>Your attempt, then the model</span><span class="mk">[{q['marks']}]</span></div>
<p class="qt">Write it first (paper, or the pencil space), timing yourself to ~{mins} min. Then reveal the model and compare the highlighted points.</p>
<div class="ans"><b>Model answer</b><div class="ma">{paras}</div>
<p class="wc">{n} words · about {write_min} min of handwriting at {WPM} words/min, plus planning</p></div></div>
<div class="note tip"><b>Why this scores</b>{q['why']}</div>"""


def build():
    topics = load_topics()
    nq = sum(len(t["questions"]) for t in topics)
    C = []
    toc = "".join(f'<button type="button" data-goto="t{t["no"]}"><b>{t["no"]}</b><span>{t["title"]}'
                  f' · {len(t["questions"])} essay{"s" if len(t["questions"]) != 1 else ""}</span></button>' for t in topics)
    C.append(card("cover", "Start", "Essay Bank", "Cover", EXTRA_CSS + f"""
<p class="sec" style="margin:0">CAIE 9708 · AS and A Level · Essays</p>
<p class="cover-k">{len(topics)}</p>
<h1>Economics Essay Bank</h1>
<p class="lede">Every syllabus topic: what to recycle, the key points examiners reward, and model answers written at the length you can actually produce in the exam.</p>
<div class="stat"><div><b>{len(topics)}</b>topics</div><div><b>{nq}</b>model essays</div></div>
<div class="toc-mini">{toc}</div>
<p class="swipehint">Tap a topic, or swipe left to start. ☰ shows every card.</p>
<p><a href="index.html">Open Revision Hub</a></p>""", sec="Start"))

    C.append(card("how", "Start", "How to use this deck", "Overview", """
<h2>How to use the Essay Bank</h2>
<ol class="steps">
<li><b>Learn the front page of each topic first.</b> The definitions, chains and evaluation lines there turn up in question after question, so they are worth memorising word for word.</li>
<li><b>Read the question and the key points.</b> <mark>Highlighted</mark> text is what earns marks: the precise term, the step in the chain, the judgement.</li>
<li><b>Attempt it before you look.</b> Plan for 2 minutes, then write against the timer on the card. Tap <i>Write your working</i> to use Apple Pencil.</li>
<li><b>Reveal the model and compare.</b> Each paragraph is tagged: <span class="pl i">Intro</span><span class="pl">Analysis</span><span class="pl e">Evaluation</span><span class="pl c">Conclusion</span>. Check you hit every highlighted point.</li>
</ol>
<div class="note link"><b>Where these sit in the paper</b>2 hours, 60 marks, 2 minutes per mark. Section A is the data response (20). Section B is one micro essay (topics 1–3 at AS, 7–8 at A Level) and Section C one macro essay (topics 4–6, 9–11), each (a) 8 + (b) 12. So each essay gets about 40 minutes: ~16 for (a), ~24 for (b).</div>
<div class="note tip"><b>Length is a skill</b>Model answers are about 200–260 words for an 8-marker and 320–400 for a 12-marker: what you can hand-write in the time with planning, and every sentence earns something. Your teacher's sample PED/YED essay is about 1,500 words, which would take over an hour to write by hand.</div>
<div class="note link"><b>Adding more</b>Type <b>/deck essay</b> and a topic (e.g. <i>/deck essay elasticity</i> or <i>/deck essay monopoly</i>) to add new questions and model answers to that topic in this deck.</div>""", sec="Start"))

    for t in topics:
        sec = f"Topic {t['no']} · {t['level']}"
        C.append(card(f"t{t['no']}", t["short"], f"{t['no']}. {t['title']}: recycle these", "Recycle",
                      f'<h2>{t["no"]}. {t["title"]}</h2><div class="meta"><span>{t["level"]}</span><span>{t["syllabus"]}</span></div>'
                      f'<div class="rc">{recycle_html(t)}</div>', sec=sec + " · Recycle"))
        for i, q in enumerate(t["questions"], 1):
            C.append(card(q["id"], t["short"], q["title"], "Model essay", question_html(t, q),
                          sec=f"{sec} · Essay {i}"))
    return C, topics


def write():
    cards, topics = build()
    flash = [f for t in topics for f in t.get("flash", [])]
    quiz = [q for t in topics for q in t.get("quiz", [])]
    meta = {"title": "Economics Essay Bank", "short": "Essay Bank", "bar": "Economics Essay Bank",
            "code": "9708 · Essays · all topics", "key": "deck-9708-essaybank"}
    out = engine.render(meta, cards, flash, quiz)
    (HERE / "deck-econ-essaybank.html").write_text(out, encoding="utf8")
    print("essay bank", len(out), "bytes,", len(cards), "cards,", len(flash), "flashcards,", len(quiz), "quiz")
    return cards, topics


if __name__ == "__main__":
    write()
