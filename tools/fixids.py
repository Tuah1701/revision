"""Give every inline SVG its own marker ids. Decks hide inactive cards with display:none, and a
url(#id) reference resolves to the FIRST element with that id in the document; if that one sits in
a hidden card the marker (arrowhead) doesn't render anywhere. Unique ids per SVG fix it."""
import re


def unique_markers(html):
    n = [0]

    def per_svg(m):
        n[0] += 1
        s = m.group(0)
        ids = set(re.findall(r'<marker id="([^"]+)"', s))
        for i in ids:
            s = s.replace(f'id="{i}"', f'id="{i}{n[0]}"').replace(f'url(#{i})', f'url(#{i}{n[0]})')
        return s

    return re.sub(r"<svg\b.*?</svg>", per_svg, html, flags=re.S)
