"""Cut products out of supplier photos (transparent PNG) for the Pawlet product images.

Usage:
    python cutout_products.py BASE_DIR JOBS_FILE

BASE_DIR holds src/ (supplier photos) and receives cut/ (cutouts).
Each line of JOBS_FILE: <name> <photo path inside src/> <crop_top> [model]
  crop_top: fraction of the height to drop first (removes supplier labels such as "Gray").
  model: rembg model, isnet-general-use by default; u2net keeps light details such as a white pom-pom.

Requires: pip install "rembg[cpu]"
"""

import os
import sys

from PIL import Image
from rembg import new_session, remove

base, jobs_file = sys.argv[1:3]
os.makedirs(os.path.join(base, "cut"), exist_ok=True)
sessions = {}

for line in open(jobs_file):
    if not line.strip() or line.startswith("#"):
        continue
    name, src, crop_top, *rest = line.split()
    model = rest[0] if rest else "isnet-general-use"
    session = sessions.setdefault(model, new_session(model))

    im = Image.open(os.path.join(base, "src", src)).convert("RGB")
    if float(crop_top) > 0:
        w, h = im.size
        im = im.crop((0, int(h * float(crop_top)), w, h))

    out = remove(im, session=session, post_process_mask=model != "u2net")
    out = out.crop(out.getchannel("A").point(lambda a: 255 if a > 12 else 0).getbbox())
    out.save(os.path.join(base, "cut", name + ".png"))
    print(name, out.size)
