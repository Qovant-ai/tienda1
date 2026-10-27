"""Build the HTML pages for the Pawlet scene images (category cards, "Why" band, Club).

Each scene is a solid brand color with a soft circle and transparent cutouts (pets,
products, the Club box) placed at fixed positions, with a floor shadow under each one.

Usage:
    python3 brand/tools/compose_scenes.py SCENES_JSON CUTOUT_DIR OUT_DIR [scene names...]

SCENES_JSON: list of {name, size: [w, h], bg, deco: [circle|blob], items: [...]}.
Each item: file (PNG name in CUTOUT_DIR), h or w, cx (center x), bottom (y of its base),
and optional rot, flip, shadow (false to skip), sw (shadow width), so (shadow opacity).
render_scenes.js turns the pages into JPGs.
"""

import json
import os
import sys

from PIL import Image

spec_path, cut_dir, out_dir, *only = sys.argv[1:]
os.makedirs(out_dir, exist_ok=True)

for t in json.load(open(spec_path)):
    if only and t["name"] not in only:
        continue
    W, H = t["size"]
    parts = []
    for d in t.get("deco", []):
        if d["type"] == "circle":
            r = d["r"]
            parts.append(
                f'<div style="position:absolute;left:{d["cx"] - r}px;top:{d["cy"] - r}px;width:{2 * r}px;'
                f'height:{2 * r}px;border-radius:50%;background:{d["color"]}"></div>'
            )
        if d["type"] == "blob":
            parts.append(
                f'<div style="position:absolute;left:{d["x"]}px;top:{d["y"]}px;width:{d["w"]}px;height:{d["h"]}px;'
                f'border-radius:{d.get("radius", "50%")};background:{d["color"]};transform:rotate({d.get("rot", 0)}deg)"></div>'
            )
    for it in t["items"]:
        f = os.path.abspath(os.path.join(cut_dir, it["file"] + ".png"))
        w0, h0 = Image.open(f).size
        if "h" in it:
            h = it["h"]
            w = w0 * h / h0
        else:
            w = it["w"]
            h = h0 * w / w0
        x = it["cx"] - w / 2
        y = it["bottom"] - h
        if it.get("shadow", True):
            sw = w * it.get("sw", 0.85)
            sh = max(18, sw * 0.09)
            parts.append(
                f'<div style="position:absolute;left:{it["cx"] - sw / 2 + it.get("sx", 0)}px;top:{it["bottom"] - sh * 0.55}px;'
                f'width:{sw}px;height:{sh}px;border-radius:50%;'
                f'background:radial-gradient(closest-side,rgba(27,43,72,{it.get("so", 0.28)}),rgba(27,43,72,0));filter:blur(4px)"></div>'
            )
        tr = []
        if it.get("rot"):
            tr.append(f'rotate({it["rot"]}deg)')
        if it.get("flip"):
            tr.append("scaleX(-1)")
        parts.append(
            f'<img src="file://{f}" style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;'
            f'transform:{" ".join(tr) or "none"};filter:drop-shadow(0 {h * 0.02:.0f}px {h * 0.03:.0f}px rgba(27,43,72,.16))">'
        )
    html = (
        f'<!doctype html><html><head><meta charset="utf-8"><meta name="size" content="{W}x{H}">'
        f"<style>html,body{{margin:0}}body{{width:{W}px;height:{H}px;position:relative;overflow:hidden;"
        f'background:{t["bg"]}}}</style></head><body>{"".join(parts)}</body></html>'
    )
    open(os.path.join(out_dir, t["name"] + ".html"), "w").write(html)
    print(t["name"])
