"""Genera los SVG del logo Pawlet Club (huella grande y chica, paleta 1).

Uso: python3 make_logo.py <carpeta_fuentes> <carpeta_salida>
"""
import os
import sys

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont

FONTS, OUT = sys.argv[1], sys.argv[2]
os.makedirs(OUT, exist_ok=True)

NAVY = "#1B2B48"
PEACH = "#FF9F6E"
WHITE = "#FFFFFF"

PRINT = (
    '<ellipse cx="30" cy="55" rx="9" ry="11.5" transform="rotate(-20 30 55)"/>'
    '<ellipse cx="47" cy="39" rx="9.5" ry="12" transform="rotate(-6 47 39)"/>'
    '<ellipse cx="73" cy="39" rx="9.5" ry="12" transform="rotate(6 73 39)"/>'
    '<ellipse cx="90" cy="55" rx="9" ry="11.5" transform="rotate(20 90 55)"/>'
    '<path d="M60 62 C 74 62, 88 76, 88 90 C 88 101, 79 106, 70 104 C 66 103, 63 101, 60 101 '
    'C 57 101, 54 103, 50 104 C 41 106, 32 101, 32 90 C 32 76, 46 62, 60 62 Z"/>'
)
BIG = 'translate(-11 7.3) scale(0.95) rotate(-12 60 66)'
SMALL = 'translate(69.6 0.96) scale(0.44) rotate(18 60 66)'


def icon(big, small, uid, dx=0.0, dy=0.0):
    """Huella grande + chica en una caja de 120x120; la chica recorta a la grande (transparente)."""
    return (
        f'<g transform="translate({dx:.2f} {dy:.2f})">'
        f'<defs><mask id="k{uid}" maskUnits="userSpaceOnUse" x="-20" y="-20" width="160" height="160">'
        f'<rect x="-20" y="-20" width="160" height="160" fill="#fff"/>'
        f'<g transform="{SMALL}" fill="#000" stroke="#000" stroke-width="10" stroke-linejoin="round">{PRINT}</g>'
        f'</mask></defs>'
        f'<g mask="url(#k{uid})"><g transform="{BIG}" fill="{big}">{PRINT}</g></g>'
        f'<g transform="{SMALL}" fill="{small}">{PRINT}</g>'
        f'</g>'
    )


class Word:
    def __init__(self, path):
        self.font = TTFont(path)
        self.gs = self.font.getGlyphSet()
        self.cmap = self.font.getBestCmap()
        self.upem = self.font["head"].unitsPerEm

    def render(self, text, size, x, baseline, tracking=-0.03):
        """Devuelve (d, ancho) del texto convertido a trazos."""
        scale = size / self.upem
        pen = SVGPathPen(self.gs)
        cursor = 0.0
        for ch in text:
            name = self.cmap[ord(ch)]
            glyph = self.gs[name]
            tpen = TransformPen(pen, (scale, 0, 0, -scale, x + cursor * scale, baseline))
            glyph.draw(tpen)
            cursor += glyph.width + tracking * self.upem
        width = (cursor - tracking * self.upem) * scale
        return pen.getCommands(), width


bold = Word(os.path.join(FONTS, "Rubik-600.ttf"))
regular = Word(os.path.join(FONTS, "Rubik-400.ttf"))


def wordmark(x, baseline, size, color):
    d1, w1 = bold.render("Pawlet", size, x, baseline)
    gap = size * 0.26
    d2, w2 = regular.render("Club", size, x + w1 + gap, baseline)
    svg = f'<path fill="{color}" d="{d1}"/><path fill="{color}" d="{d2}"/>'
    return svg, w1 + gap + w2


def write(name, w, h, body, bg=None):
    rect = f'<rect width="{w:.2f}" height="{h:.2f}" fill="{bg}"/>' if bg else ""
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.2f} {h:.2f}" '
        f'width="{w:.2f}" height="{h:.2f}" role="img" aria-label="Pawlet Club">'
        f"<title>Pawlet Club</title>{rect}{body}</svg>\n"
    )
    with open(os.path.join(OUT, name), "w") as fh:
        fh.write(svg)


# Horizontal: ícono 120 + palabra (64 px, mayúsculas centradas en el ícono).
SIZE = 64
CAP = 700 * SIZE / 1000
for suffix, big, small, text in (
    ("", NAVY, PEACH, NAVY),
    ("-white", PEACH, WHITE, WHITE),
):
    words, width = wordmark(0, 0, SIZE, text)  # medir
    pad = 4
    x_text = 120 + 14
    words, width = wordmark(x_text, 60 + CAP / 2, SIZE, text)
    total = x_text + width + pad
    write(f"pawlet-logo-horizontal{suffix}.svg", total, 120, icon(big, small, "h" + suffix.strip("-")) + words)

# Vertical: ícono arriba, palabra abajo.
SIZE_V = 44
CAP_V = 700 * SIZE_V / 1000
_, width_v = wordmark(0, 0, SIZE_V, NAVY)
W_V = max(width_v, 120) + 16
for suffix, big, small, text in (("", NAVY, PEACH, NAVY), ("-white", PEACH, WHITE, WHITE)):
    words, _ = wordmark((W_V - width_v) / 2, 120 + 14 + CAP_V, SIZE_V, text)
    write(f"pawlet-logo-stacked{suffix}.svg", W_V, 120 + 14 + CAP_V + 14,
          icon(big, small, "v" + suffix.strip("-"), dx=(W_V - 120) / 2) + words)

# Ícono solo (transparente) y favicon (fondo azul redondeado).
write("pawlet-icon.svg", 120, 120, icon(NAVY, PEACH, "i"))
write(
    "pawlet-favicon.svg", 120, 120,
    f'<rect width="120" height="120" rx="28" fill="{NAVY}"/>'
    f'<g transform="translate(60 60) scale(0.78) translate(-60 -60)">{icon(PEACH, WHITE, "f")}</g>',
)
print("\n".join(sorted(os.listdir(OUT))))
