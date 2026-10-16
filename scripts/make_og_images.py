"""Extract still PNGs from the teaser GIFs for link-share previews (og:image).

Usage (from the repo root): python3 scripts/make_og_images.py
Slack and KakaoTalk do not reliably animate GIF previews, so each paper gets a
representative frame instead.
"""
import os

from PIL import Image, ImageSequence

OUT = "images/og"

# output name -> (source GIF, time in seconds of the frame to keep)
STILLS = {
    "wacv2026": ("images/featured/wacv2026.gif", 9.5),   # balanced spectrum after fusion
    "icip2026": ("images/featured/icip2026.gif", 9.5),   # balanced attention after routing
    "geopid": ("images/featured/geopid.gif", 10.0),      # steered vision-unique directions
    "icip2025": ("images/featured/demo-ver1.gif", 27.0),
    "dmlr2025": ("images/featured/darai.gif", 3.0),
}


def frame_at(path, t):
    im = Image.open(path)
    elapsed = 0.0
    last = None
    for frame in ImageSequence.Iterator(im):
        last = frame.convert("RGB")
        elapsed += frame.info.get("duration", 100) / 1000
        if elapsed > t:
            break
    return last


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for name, (src, t) in STILLS.items():
        dst = os.path.join(OUT, f"{name}.png")
        im = frame_at(src, t)
        im.thumbnail((1200, 1200))
        im.save(dst, optimize=True)
        print("wrote", dst)
