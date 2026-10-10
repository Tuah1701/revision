# Revision Hub

Tuah's A-Level revision app: swipeable decks for 9708 Economics (more subjects coming), an offline Exam Timer, and links to the Practice Tracker.

**Open it:** https://tuah1701.github.io/revision/ — in Safari on iPhone or iPad, tap Share → Add to Home Screen to install it as an app. It works offline after the first open.

## Layout
- `index.html` — the hub (home screen)
- `econ-ch1.html`, `econ-ch2.html` — decks
- `timer.html` — Exam Timer
- `sw.js`, `manifest.webmanifest`, `icon-*.png`, `mathjax/` — what makes it installable and offline
- `tools/` — the generator Claude uses to build decks (`build.py`, `app_build.py`, `engine.py`) and the deck content
