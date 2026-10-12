"""Build the Economics swipe decks. Usage: python3 build.py"""
import json, re, sys, pathlib
import engine, bei

SCRATCH = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path(".")


def js_array(path, name):
    """Pull a JS array literal of double-quoted strings out of the original deck's script."""
    src = pathlib.Path(path).read_text(encoding="utf8")
    m = re.search(r"(?:var|const) " + name + r"=\[(.*?)\n\];", src, re.S)
    body = "[" + m.group(1) + "]"
    if name == "CARDS":  # single-quoted JS strings in the Price deck
        body = re.sub(r"'((?:[^'\\]|\\.)*)'", lambda k: json.dumps(k.group(1).replace("\\'", "'")), body)
        body = re.sub(r",\s*\]$", "]", body.strip())
    return json.loads(body)


def build_bei():
    flash = json.loads((pathlib.Path(__file__).parent / "data/ch1-flash.json").read_text(encoding="utf8"))
    meta = {"title": "Basic Economic Ideas Deck", "short": "Econ Ch1", "bar": "Basic economic ideas",
            "code": "9708 · AS Chapter 1", "key": "deck-9708-ch1"}
    out = engine.render(meta, bei.build(), flash, bei.QUIZ)
    pathlib.Path("deck-econ-ch1.html").write_text(out, encoding="utf8")
    print("ch1", len(out), "bytes,", len(flash), "flashcards,", len(bei.QUIZ), "quiz")


if __name__ == "__main__":
    build_bei()
    import essay
    essay.write()
    import essaybank
    essaybank.write()
    try:
        import price
        price.write(SCRATCH, js_array)
    except ImportError:
        pass
