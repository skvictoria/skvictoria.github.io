"""Shrink featured GIFs into lightweight thumbnails for the Publications list.

Usage: python3 scripts/make_thumbs.py SRC.gif DST.gif [width] [frame_step]
"""
import sys

from PIL import Image, ImageSequence

src, dst = sys.argv[1], sys.argv[2]
width = int(sys.argv[3]) if len(sys.argv) > 3 else 400
step = int(sys.argv[4]) if len(sys.argv) > 4 else 1

im = Image.open(src)
height = round(im.height * width / im.width)
frames, durations = [], []
for i, frame in enumerate(ImageSequence.Iterator(im)):
    if i % step:
        continue
    frames.append(frame.convert("RGB").resize((width, height), Image.LANCZOS))
    durations.append(frame.info.get("duration", 100) * step)

# build one shared palette from frames sampled across the clip
samples = frames[:: max(1, len(frames) // 8)]
sheet = Image.new("RGB", (width, height * len(samples)))
for k, f in enumerate(samples):
    sheet.paste(f, (0, height * k))
pal = sheet.quantize(colors=128, method=Image.Quantize.MEDIANCUT)
q = [f.quantize(palette=pal, dither=Image.Dither.NONE) for f in frames]
q[0].save(dst, save_all=True, append_images=q[1:], duration=durations, loop=0, optimize=True)
print(f"{len(q)} frames, {width}x{height} -> {dst}")
