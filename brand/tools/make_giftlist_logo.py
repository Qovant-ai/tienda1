"""Genera los SVG del logo Gift List Co (caja de regalo con moño + palabra en Rubik).

Uso: python3 make_giftlist_logo.py <carpeta_fuentes> <carpeta_salida>
La carpeta de fuentes debe tener Rubik-400.ttf y Rubik-600.ttf.
"""
import os
import sys

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont

FONTS, OUT = sys.argv[1], sys.argv[2]
os.makedirs(OUT, exist_ok=True)

INK = "#24203F"
RIBBON = "#F2675F"
WHITE = "#FFFFFF"
NAME = "Gift List Co"


def icon(box, ribbon, dx=0.0, dy=0.0):
    """Caja de regalo en 120x120: tapa, cuerpo, cinta vertical y moño de dos lazos."""
    return (
        f'<g transform="translate({dx:.2f} {dy:.2f})">'
        # moño (detrás de la tapa)
        f'<g fill="{ribbon}">'
        '<path d="M60 44 C 50 26, 30 18, 26 30 C 22 42, 42 46, 60 44 Z"/>'
        '<path d="M60 44 C 70 26, 90 18, 94 30 C 98 42, 78 46, 60 44 Z"/>'
        '</g>'
        # tapa y cuerpo
        f'<rect x="12" y="42" width="96" height="22" rx="6" fill="{box}"/>'
        f'<rect x="20" y="62" width="80" height="48" rx="6" fill="{box}"/>'
        # cinta
        f'<rect x="52" y="42" width="16" height="68" fill="{ribbon}"/>'
        f'<circle cx="60" cy="43" r="7" fill="{ribbon}"/>'
        '</g>'
    )


class Word:
    def __init__(self, path):
        self.font = TTFont(path)
        self.gs = self.font.getGlyphSet()
        self.cmap = self.font.getBestCmap()
        self.upem = self.font["head"].unitsPerEm

    def render(self, text, size, x, baseline, tracking=-0.02):
        scale = size / self.upem
        pen = SVGPathPen(self.gs)
        cursor = 0.0
        for ch in text:
            glyph = self.gs[self.cmap[ord(ch)]]
            tpen = TransformPen(pen, (scale, 0, 0, -scale, x + cursor * scale, baseline))
            glyph.draw(tpen)
            cursor += glyph.width + tracking * self.upem
        return pen.getCommands(), (cursor - tracking * self.upem) * scale


bold = Word(os.path.join(FONTS, "Rubik-600.ttf"))
regular = Word(os.path.join(FONTS, "Rubik-400.ttf"))


def wordmark(x, baseline, size, color, accent):
    d1, w1 = bold.render("Gift List", size, x, baseline)
    gap = size * 0.24
    d2, w2 = regular.render("Co", size, x + w1 + gap, baseline)
    return f'<path fill="{color}" d="{d1}"/><path fill="{accent}" d="{d2}"/>', w1 + gap + w2


def write(name, w, h, body, bg=None):
    rect = f'<rect width="{w:.2f}" height="{h:.2f}" fill="{bg}"/>' if bg else ""
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.2f} {h:.2f}" '
        f'width="{w:.2f}" height="{h:.2f}" role="img" aria-label="{NAME}">'
        f"<title>{NAME}</title>{rect}{body}</svg>\n"
    )
    with open(os.path.join(OUT, name), "w") as fh:
        fh.write(svg)


SIZE = 64
CAP = 700 * SIZE / 1000
for suffix, box, ribbon, text, accent in (
    ("", INK, RIBBON, INK, RIBBON),
    ("-white", WHITE, RIBBON, WHITE, RIBBON),
):
    x_text = 120 + 16
    words, width = wordmark(x_text, 66 + CAP / 2, SIZE, text, accent)
    write(f"giftlist-logo-horizontal{suffix}.svg", x_text + width + 4, 120, icon(box, ribbon) + words)

write("giftlist-icon.svg", 120, 120, icon(INK, RIBBON))
write(
    "giftlist-favicon.svg", 120, 120,
    f'<rect width="120" height="120" rx="28" fill="{INK}"/>'
    f'<g transform="translate(60 62) scale(0.8) translate(-60 -64)">{icon(WHITE, RIBBON)}</g>',
)
print("\n".join(sorted(f for f in os.listdir(OUT) if f.startswith("giftlist"))))
