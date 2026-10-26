"""Build the HTML pages for the Pawlet Club product images.

Reads brand/product-images/spec.json and writes one HTML page per image into the
output folder. render_product_images.js turns them into JPGs.

Usage:
    python3 brand/tools/make_product_images.py SPEC CUTOUT_DIR OUT_DIR

CUTOUT_DIR holds the transparent product cutouts (PNG) named in the spec.
"""

import json
import os
import sys

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOGO = os.path.join(ROOT, "brand", "logo", "png", "pawlet-logo-horizontal.png")
LOGO_WHITE = os.path.join(ROOT, "brand", "logo", "png", "pawlet-logo-horizontal-white.png")

NAVY = "#1B2B48"
PEACH = "#FF9F6E"
CREAM = "#FFF3EA"
PEACH_SOFT = "#FFE7D6"
SLATE = "#3B4A66"
SAND = "#E7DFD6"
WARM = "#F6EFE8"

SIZE = 1600

STROKE = 'fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"'
PAW_SHAPES = (
    '<ellipse cx="30" cy="55" rx="9" ry="11.5" transform="rotate(-20 30 55)"/>'
    '<ellipse cx="47" cy="39" rx="9.5" ry="12" transform="rotate(-6 47 39)"/>'
    '<ellipse cx="73" cy="39" rx="9.5" ry="12" transform="rotate(6 73 39)"/>'
    '<ellipse cx="90" cy="55" rx="9" ry="11.5" transform="rotate(20 90 55)"/>'
    '<path d="M60 62 C 74 62, 88 76, 88 90 C 88 101, 79 106, 70 104 C 66 103, 63 101, 60 101 '
    'C 57 101, 54 103, 50 104 C 41 106, 32 101, 32 90 C 32 76, 46 62, 60 62 Z"/>'
)
ICONS = {
    "paw": f'<svg viewBox="15 21 90 90" fill="currentColor">{PAW_SHAPES}</svg>',
    "box": f'<svg viewBox="0 0 24 24" {STROKE}><path d="M3 8.5 12 4l9 4.5v7L12 20l-9-4.5z"/><path d="m3 8.5 9 4.5 9-4.5M12 13v7"/></svg>',
    "heart": f'<svg viewBox="0 0 24 24" {STROKE}><path d="M12 20s-7-4.4-9-9.2C1.7 7.6 3.8 4.5 7 4.5c2 0 3.4 1.1 5 3 1.6-1.9 3-3 5-3 3.2 0 5.3 3.1 4 6.3-2 4.8-9 9.2-9 9.2z"/></svg>',
    "truck": f'<svg viewBox="0 0 24 24" {STROKE}><path d="M2 6h11v10H2zM13 9h4.5l3.5 3.5V16h-8z"/><circle cx="6" cy="17.5" r="1.8"/><circle cx="17" cy="17.5" r="1.8"/></svg>',
    "ball": f'<svg viewBox="0 0 24 24" {STROKE}><circle cx="12" cy="12" r="9"/><path d="M5.5 5.8c3.4 2.6 3.4 9.8 0 12.4M18.5 5.8c-3.4 2.6-3.4 9.8 0 12.4"/></svg>',
    "brush": f'<svg viewBox="0 0 24 24" {STROKE}><path d="M4 20 13 11M13 11l2-2 6 6-2 2zM15 9l4-4"/><path d="M16 12l1 1M18 10l1 1"/></svg>',
    "check": f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>',
    "star": f'<svg viewBox="0 0 24 24" {STROKE}><path d="m12 3.5 2.6 5.3 5.9.9-4.3 4.1 1 5.8L12 16.9l-5.2 2.7 1-5.8-4.3-4.1 5.9-.9z"/></svg>',
    "chat": f'<svg viewBox="0 0 24 24" {STROKE}><path d="M4 5h16v11H9l-5 4z"/><path d="M8.5 10.5h.01M12 10.5h.01M15.5 10.5h.01"/></svg>',
    "sparkle": f'<svg viewBox="0 0 24 24" {STROKE}><path d="M12 3c.6 4.6 2.4 6.4 7 7-4.6.6-6.4 2.4-7 7-.6-4.6-2.4-6.4-7-7 4.6-.6 6.4-2.4 7-7zM19 16c.2 1.6.9 2.3 2.5 2.5-1.6.2-2.3.9-2.5 2.5-.2-1.6-.9-2.3-2.5-2.5 1.6-.2 2.3-.9 2.5-2.5z"/></svg>',
    "shield": f'<svg viewBox="0 0 24 24" {STROKE}><path d="M12 3 4.5 6v5.5c0 4.6 3.2 8.4 7.5 9.5 4.3-1.1 7.5-4.9 7.5-9.5V6z"/><path d="m8.8 12.2 2.3 2.3 4.3-4.6"/></svg>',
    "lock": f'<svg viewBox="0 0 24 24" {STROKE}><rect x="4.5" y="10.5" width="15" height="10" rx="2"/><path d="M8 10.5V7.8a4 4 0 0 1 8 0v2.7M12 14.5v2.5"/></svg>',
    "refresh": f'<svg viewBox="0 0 24 24" {STROKE}><path d="M20 11a8 8 0 0 0-14.3-4.9L4 8"/><path d="M4 3.5V8h4.5M4 13a8 8 0 0 0 14.3 4.9L20 16"/><path d="M20 20.5V16h-4.5"/></svg>',
    "pin": f'<svg viewBox="0 0 24 24" {STROKE}><path d="M12 21s-6.5-5.6-6.5-11a6.5 6.5 0 0 1 13 0c0 5.4-6.5 11-6.5 11z"/><circle cx="12" cy="10" r="2.3"/></svg>',
    "ruler": f'<svg viewBox="0 0 24 24" {STROKE}><path d="M3 15.5 15.5 3 21 8.5 8.5 21z"/><path d="m7 11.5 2 2M10 8.5l2 2M13 5.5l2 2"/></svg>',
}


def font_face():
    fonts = os.environ.get("PAWLET_FONTS", os.path.join(ROOT, "brand", "fonts"))
    return f"""
    @font-face {{ font-family: Rubik; font-weight: 400; src: url('file://{fonts}/Rubik-400.ttf'); }}
    @font-face {{ font-family: Rubik; font-weight: 600; src: url('file://{fonts}/Rubik-600.ttf'); }}
    * {{ box-sizing: border-box; }}
    html, body {{ margin: 0; width: {SIZE}px; height: {SIZE}px; overflow: hidden; }}
    body {{ font-family: Rubik, sans-serif; color: {NAVY}; -webkit-font-smoothing: antialiased; }}
    svg {{ display: block; width: 100%; height: 100%; }}
    """


def page(body, css=""):
    return f"<!doctype html><html><head><meta charset='utf-8'><style>{font_face()}{css}</style></head><body>{body}</body></html>"


def img_size(path):
    with Image.open(path) as im:
        return im.size


def fit(path, box_w, box_h):
    w, h = img_size(path)
    s = min(box_w / w, box_h / h)
    return round(w * s), round(h * s)


def hero(cutouts, layout="single", box=(1240, 1120), gap=60):
    """Clean main image: cutout(s) on a warm studio backdrop with a soft floor shadow."""
    bw, bh = box
    items = []
    if layout == "single":
        w, h = fit(cutouts[0], bw, bh)
        items.append((cutouts[0], w, h))
    else:
        n = len(cutouts)
        each = (bw - gap * (n - 1)) / n
        for c in cutouts:
            w, h = fit(c, each, bh)
            items.append((c, w, h))
    total_w = sum(w for _, w, _ in items) + gap * (len(items) - 1)
    max_h = max(h for _, _, h in items)
    floor = 800 + max_h / 2
    x = (SIZE - total_w) / 2
    parts = []
    for c, w, h in items:
        top = floor - h
        parts.append(
            f"<div class='shadow' style='left:{x + w * 0.1:.0f}px;top:{floor - 38:.0f}px;width:{w * 0.8:.0f}px'></div>"
            f"<img src='file://{c}' style='left:{x:.0f}px;top:{top:.0f}px;width:{w}px;height:{h}px'>"
        )
        x += w + gap
    css = f"""
    body {{ position: relative; background: radial-gradient(circle at 50% 40%, #FFFCF8 0%, {WARM} 58%, #EFE4D8 100%); }}
    img {{ position: absolute; }}
    .shadow {{ position: absolute; height: 76px; border-radius: 50%;
      background: radial-gradient(ellipse at center, rgba(27,43,72,.26) 0%, rgba(27,43,72,.10) 45%, rgba(27,43,72,0) 72%);
      filter: blur(8px); }}
    """
    return page("".join(parts), css)


def benefits(item):
    rows = "".join(
        f"""<div class='row'>
          <div class='ic'>{ICONS[b['icon']]}</div>
          <div><div class='bt'>{b['title']}</div><div class='bx'>{b['text']}</div></div>
        </div>"""
        for b in item["benefits"]
    )
    cut = item["cutouts"][0]
    w, h = fit(cut, 540, 880)
    css = f"""
    body {{ background: {CREAM}; padding: 88px 88px 0; position: relative; }}
    .eyebrow {{ font-size: 34px; font-weight: 600; letter-spacing: .14em; text-transform: uppercase; color: {SLATE};
      display: flex; align-items: center; gap: 14px; }}
    .eyebrow .p {{ width: 44px; height: 44px; color: {PEACH}; }}
    h1 {{ margin: 16px 0 0; font-size: 96px; line-height: 1.02; font-weight: 600; letter-spacing: -.02em; max-width: 1424px; }}
    .grid {{ display: grid; grid-template-columns: 620px 1fr; gap: 60px; margin-top: 52px; height: 1030px; }}
    .panel {{ border-radius: 56px; background: #fff; display: grid; place-items: center;
      box-shadow: 0 30px 60px rgba(27,43,72,.08); }}
    .panel img {{ width: {w}px; height: {h}px; }}
    .list {{ display: flex; flex-direction: column; justify-content: space-evenly; }}
    .row {{ display: flex; gap: 32px; align-items: flex-start; }}
    .ic {{ flex: 0 0 120px; height: 120px; border-radius: 50%; background: {PEACH}; color: {NAVY}; padding: 30px; }}
    .bt {{ font-size: 54px; font-weight: 600; line-height: 1.08; margin-top: 4px; }}
    .bx {{ font-size: 38px; line-height: 1.28; color: {SLATE}; margin-top: 10px; }}
    .foot {{ position: absolute; left: 88px; right: 88px; bottom: 54px; display: flex; justify-content: space-between; align-items: center; }}
    .foot img {{ height: 72px; }}
    .foot span {{ font-size: 32px; color: {SLATE}; }}
    """
    body = f"""
    <div class='eyebrow'><div class='p'>{ICONS['paw']}</div>Why you'll love it</div>
    <h1>{item['name']}</h1>
    <div class='grid'><div class='panel'><img src='file://{cut}'></div><div class='list'>{rows}</div></div>
    <div class='foot'><img src='file://{LOGO}'><span>Free US shipping over $30 · 30-day returns</span></div>
    """
    return page(body, css)


def size_guide(item):
    sg = item["size"]
    css = f"""
    body {{ background: #fff; padding: 96px; position: relative; }}
    .eyebrow {{ font-size: 30px; font-weight: 600; letter-spacing: .14em; text-transform: uppercase; color: {SLATE};
      display: flex; align-items: center; gap: 14px; }}
    .eyebrow .p {{ width: 40px; height: 40px; color: {PEACH}; }}
    h1 {{ margin: 18px 0 0; font-size: 84px; line-height: 1.04; font-weight: 600; letter-spacing: -.02em; }}
    .sub {{ font-size: 36px; color: {SLATE}; margin-top: 18px; }}
    .stage {{ position: absolute; left: 96px; right: 96px; top: 400px; bottom: 200px; }}
    .stage img {{ position: absolute; }}
    .card {{ position: absolute; border-radius: 40px; background: {CREAM}; }}
    .lbl {{ position: absolute; text-align: center; }}
    .lbl b {{ display: block; font-size: 64px; font-weight: 600; }}
    .lbl span {{ display: block; font-size: 34px; color: {SLATE}; margin-top: 6px; line-height: 1.3; }}
    .dim {{ position: absolute; background: {NAVY}; }}
    .dim::before, .dim::after {{ content: ''; position: absolute; background: {NAVY}; }}
    .v {{ width: 4px; }} .v::before, .v::after {{ left: -14px; width: 32px; height: 4px; }} .v::before {{ top: 0; }} .v::after {{ bottom: 0; }}
    .h {{ height: 4px; }} .h::before, .h::after {{ top: -14px; height: 32px; width: 4px; }} .h::before {{ left: 0; }} .h::after {{ right: 0; }}
    .tag {{ position: absolute; background: {NAVY}; color: #fff; border-radius: 999px; padding: 14px 30px; font-size: 38px; font-weight: 600; white-space: nowrap; }}
    .foot {{ position: absolute; left: 96px; right: 96px; bottom: 72px; display: flex; justify-content: space-between; align-items: center; }}
    .foot img {{ height: 64px; }}
    .foot span {{ font-size: 28px; color: {SLATE}; }}
    """
    stage_w, stage_h = SIZE - 192, SIZE - 400 - 200
    parts = []
    if sg["type"] == "scale":
        # side-by-side sizes, scaled relative to each other
        n = len(sg["sizes"])
        col = stage_w / n
        largest = max(s["rel"] for s in sg["sizes"])
        cut = item["cutouts"][0]
        base_w, base_h = fit(cut, col - 60, stage_h - 300)
        for i, s in enumerate(sg["sizes"]):
            k = s["rel"] / largest
            w, h = base_w * k, base_h * k
            cx = col * i + col / 2
            img_bottom = stage_h - 280
            parts.append(f"<div class='card' style='left:{col * i + 14:.0f}px;top:0;width:{col - 28:.0f}px;height:{stage_h:.0f}px'></div>")
            parts.append(f"<img src='file://{cut}' style='left:{cx - w / 2:.0f}px;top:{img_bottom - h:.0f}px;width:{w:.0f}px;height:{h:.0f}px'>")
            parts.append(f"<div class='lbl' style='left:{col * i:.0f}px;width:{col:.0f}px;top:{stage_h - 250:.0f}px'><b>{s['label']}</b><span>{s['text']}</span></div>")
    else:
        cut = item["cutouts"][0]
        w, h = fit(cut, stage_w - 420, stage_h - 120)
        x = (stage_w - w) / 2 - 60
        y = (stage_h - h) / 2
        if "height" in sg:
            parts.append(f"<div class='dim v' style='left:{x + w + 90:.0f}px;top:{y:.0f}px;height:{h:.0f}px'></div>")
            parts.append(f"<div class='tag' style='left:{x + w + 140:.0f}px;top:{y + h / 2 - 40:.0f}px'>{sg['height']}</div>")
        if "width" in sg:
            parts.append(f"<div class='dim h' style='left:{x:.0f}px;top:{y + h + 50:.0f}px;width:{w:.0f}px'></div>")
            parts.append(f"<div class='tag' style='left:{x + w / 2:.0f}px;top:{y + h + 80:.0f}px;transform:translateX(-50%)'>{sg['width']}</div>")
        parts.append(f"<img src='file://{cut}' style='left:{x:.0f}px;top:{y:.0f}px;width:{w}px;height:{h}px'>")
    body = f"""
    <div class='eyebrow'><div class='p'>{ICONS['ruler']}</div>Size guide</div>
    <h1>{sg['title']}</h1>
    <div class='sub'>{sg.get('subtitle', '')}</div>
    <div class='stage'>{''.join(parts)}</div>
    <div class='foot'><img src='file://{LOGO}'><span>{sg.get('note', '')}</span></div>
    """
    return page(body, css)


def promise():
    tiles = [
        ("truck", "Free US shipping", "On every order of $30 or more"),
        ("refresh", "30-day happiness guarantee", "Easy returns if it's not a fit"),
        ("pin", "Ships from the US", "Fast delivery with tracking"),
        ("lock", "Secure checkout", "Pay safely with PayPal"),
    ]
    cells = "".join(
        f"<div class='t'><div class='ic'>{ICONS[i]}</div><div class='tt'>{a}</div><div class='tx'>{b}</div></div>"
        for i, a, b in tiles
    )
    css = f"""
    body {{ background: {NAVY}; color: #fff; padding: 110px 100px; position: relative; }}
    .top {{ display: flex; justify-content: center; }}
    .top img {{ height: 92px; }}
    h1 {{ text-align: center; font-size: 96px; font-weight: 600; letter-spacing: -.02em; margin: 70px 0 16px; }}
    .sub {{ text-align: center; font-size: 38px; color: rgba(255,255,255,.78); }}
    .grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 36px; margin-top: 90px; }}
    .t {{ background: rgba(255,255,255,.07); border: 2px solid rgba(255,255,255,.12); border-radius: 44px; padding: 54px 48px; }}
    .ic {{ width: 116px; height: 116px; border-radius: 50%; background: {PEACH}; color: {NAVY}; padding: 28px; }}
    .tt {{ font-size: 50px; font-weight: 600; margin-top: 34px; line-height: 1.1; }}
    .tx {{ font-size: 34px; color: rgba(255,255,255,.78); margin-top: 12px; }}
    .foot {{ position: absolute; left: 0; right: 0; bottom: 92px; text-align: center; font-size: 34px; color: {PEACH}; font-weight: 600; }}
    """
    body = f"""
    <div class='top'><img src='file://{LOGO_WHITE}'></div>
    <h1>The Pawlet promise</h1>
    <div class='sub'>Hand-picked for dogs and cats, backed by real humans.</div>
    <div class='grid'>{cells}</div>
    <div class='foot'>Questions? We reply in English and español.</div>
    """
    return page(body, css)


def main():
    spec_path, cut_dir, out_dir = sys.argv[1:4]
    spec = json.load(open(spec_path))
    os.makedirs(out_dir, exist_ok=True)

    def cut(name):
        return os.path.abspath(os.path.join(cut_dir, name + ".png"))

    written = []

    def write(name, html):
        path = os.path.join(out_dir, name + ".html")
        open(path, "w").write(html)
        written.append(path)

    write("promise", promise())
    for handle, item in spec["products"].items():
        item = dict(item)
        item["cutouts"] = [cut(c) for c in item["hero"]]
        write(f"{handle}__hero", hero(item["cutouts"], item.get("hero_layout", "single")))
        bitem = dict(item, cutouts=[cut(item.get("benefits_cutout", item["hero"][0]))])
        write(f"{handle}__benefits", benefits(bitem))
        if "size" in item:
            sitem = dict(item, cutouts=[cut(item["size"].get("cutout", item["hero"][0]))])
            write(f"{handle}__size", size_guide(sitem))
        for vname, vcuts in item.get("variants", {}).items():
            layout = "row" if len(vcuts) > 1 else "single"
            write(f"{handle}__v_{vname}", hero([cut(c) for c in vcuts], layout))
    print("\n".join(written))


if __name__ == "__main__":
    main()
