# Economics Essay Bank: how `/deck essay <topic>` works

`/deck essay <topic>` does **not** make a new deck. It adds to the Essay Bank (`econ-essay-bank.html` in the app,
built by `tools/essaybank.py`).

1. Map the topic to its syllabus file (e.g. "elasticity" → `t02_price_system.py`, "monopoly" → `t07_micro_a2.py`,
   "minimum wage" → `t08_gov_micro_a2.py`). Only create a new `tNN_*.py` if it genuinely fits no topic.
2. Add new question dicts to that file's `TOPIC["questions"]` (ids continue the sequence, e.g. `t2q3`).
   Attached past papers, mark schemes or teacher samples are the primary source.
3. Add anything newly recyclable to `TOPIC["recycle"]`, plus 2–4 `flash` cards and 1–2 `quiz` items.
4. `python3 essaybank.py && python3 app_build.py`, copy `revision-app/.` to the repo root, check 390px and 820px, push.

## Question schema
```python
{"id": "t2q3", "marks": 8 or 12, "title": "Short card title",
 "q": "Full question text", "src": "Past-paper style | 9708/22/M/J/24 Q5 | teacher sample",
 "keys": [("AO1"|"AO2"|"AO3", "point with <mark>highlighted</mark> mark-earning words"), ...],
 "plan": ["2-minute plan step", ...],
 "fig": figs.something(),      # optional, from essays/figs.py
 "answer": [("i"|"a"|"e"|"c", "Label", "paragraph with <mark>key phrases</mark>"), ...],  # intro/analysis/evaluation/conclusion
 "why": "Why this answer scores"}
```

## House rules for model answers
- Exam length: about 200–260 words for 8 marks, 320–400 for 12 marks (handwritten at ~22 words/min).
- Every analysis point is a chain (because → so → therefore), with one real example, Malaysian where possible.
- 12-markers: both sides developed, evaluation names *what it depends on and why*, conclusion answers the exact words of the question.
- Highlight with `<mark>` only what earns marks: precise terms, chain steps, the judgement.
