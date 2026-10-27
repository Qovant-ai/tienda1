"""Draw the Pawlet Club box (kraft box, navy logo badge, label; gift version with a ribbon).

Writes one HTML page per box (900 x 800). Screenshot them with Playwright using a transparent
background (page.screenshot({ omitBackground: true })) and crop the PNG to its visible area.

Usage:
    PAWLET_FONTS=<folder with Rubik-600.ttf> python3 brand/tools/make_club_box.py OUT_DIR
"""

import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOGO = os.path.join(ROOT, "brand", "logo", "pawlet-logo-stacked-white.svg")
FONTS = os.environ.get("PAWLET_FONTS", os.path.join(ROOT, "brand", "fonts"))


def box(label, gift=False):
    ribbon = '' if not gift else '''
      <div style="position:absolute;left:405px;top:150px;width:90px;height:600px;background:linear-gradient(90deg,#f08a57,#ff9f6e 40%,#f08a57);z-index:3"></div>
      <div style="position:absolute;left:60px;top:470px;width:780px;height:80px;background:linear-gradient(180deg,#f08a57,#ff9f6e 40%,#f08a57);z-index:3"></div>
      <div style="position:absolute;left:300px;top:70px;width:150px;height:110px;border:26px solid #ff9f6e;border-radius:50% 50% 50% 50%/60% 60% 40% 40%;transform:rotate(-18deg);z-index:4;box-sizing:border-box"></div>
      <div style="position:absolute;left:450px;top:70px;width:150px;height:110px;border:26px solid #ff9f6e;border-radius:50% 50% 50% 50%/60% 60% 40% 40%;transform:rotate(18deg);z-index:4;box-sizing:border-box"></div>
      <div style="position:absolute;left:418px;top:125px;width:64px;height:58px;border-radius:18px;background:#f08a57;z-index:5"></div>'''
    badge_top = 300 if not gift else 250
    badge = f'''<div style="position:absolute;left:{450-140 if not gift else 120}px;top:{badge_top if not gift else 250}px;width:280px;height:280px;border-radius:50%;background:#1b2b48;display:grid;place-items:center;z-index:2;box-shadow:inset 0 0 0 10px rgba(255,255,255,.12)">
        <img src="file://{LOGO}" style="width:200px"></div>''' if not gift else f'''<div style="position:absolute;left:110px;top:245px;width:210px;height:210px;border-radius:50%;background:#1b2b48;display:grid;place-items:center;z-index:2"><img src="file://{LOGO}" style="width:150px"></div>'''
    tag = f'''<div style="position:absolute;left:{450-130 if not gift else 560}px;top:{610 if not gift else 600}px;padding:16px 30px;border-radius:999px;background:#ff9f6e;color:#1b2b48;font:600 38px Rubik;letter-spacing:.06em;z-index:2;{'' if not gift else 'background:#fff;'}">{label}</div>'''
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:Rubik;src:url(file://{FONTS}/Rubik-600.ttf);font-weight:600}}
html,body{{margin:0;background:transparent}} body{{width:900px;height:800px;position:relative}}
</style></head><body>
<div style="position:absolute;left:60px;top:200px;width:780px;height:560px;border-radius:22px;background:linear-gradient(180deg,#d9a878,#c8915d);box-shadow:inset -40px 0 60px rgba(120,70,30,.18)"></div>
<div style="position:absolute;left:40px;top:150px;width:820px;height:130px;border-radius:20px;background:linear-gradient(180deg,#e4b787,#d29e6a);box-shadow:0 14px 18px -8px rgba(90,50,20,.35);z-index:1"></div>
{badge}{tag}{ribbon}
</body></html>'''


out = sys.argv[1]
os.makedirs(out, exist_ok=True)
for name, label, gift in [("box_dog", "CLUB DOG", False), ("box_cat", "CLUB CAT", False),
                          ("box_club", "THE CLUB", False), ("box_gift", "GIFT", True)]:
    open(os.path.join(out, name + ".html"), "w").write(box(label, gift))
    print(name)
