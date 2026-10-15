"""Animated teaser for ICIP 2026: MoIR, Multi-modal Information Router."""
import io
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrow, FancyBboxPatch
import numpy as np
from PIL import Image

OUT, PHOTO = sys.argv[1], sys.argv[2]
FPS = 20
W, H, DPI = 8.0, 4.2, 100

PINK = np.array([0.88, 0.20, 0.47])
BLUE = np.array([0.05, 0.40, 0.80])
ATTN = "#b3121f"

IMG0 = [0.55, 0.12, 0.08, 0.22]   # sparse visual tokens
TXT0 = [0.80, 0.95, 0.85, 0.40]   # dense text tokens
IMG1 = [0.62, 0.58, 0.52, 0.60]   # after routing
TXT1 = [0.82, 0.92, 0.85, 0.62]

# keyframes: time, img vals, txt vals, attention share to image, arrow alpha, routing progress
KEYS = [
    (0.0,  IMG0, TXT0, 0.50, 0.0, 0.0),
    (1.6,  IMG0, TXT0, 0.50, 0.0, 0.0),
    (2.2,  IMG0, TXT0, 0.15, 1.0, 0.0),
    (4.2,  IMG0, TXT0, 0.15, 1.0, 0.0),
    (4.8,  IMG0, TXT0, 0.15, 0.25, 0.0),
    (7.8,  IMG1, TXT1, 0.15, 0.25, 1.0),
    (8.4,  IMG1, TXT1, 0.47, 1.0, 1.0),
    (10.8, IMG1, TXT1, 0.47, 1.0, 1.0),
    (11.4, IMG0, TXT0, 0.50, 0.0, 1.0),
]
# caption segments: start, end, title, subtitle
CAPS = [
    (0.0, 1.9, "Information disparity", "sparse visual tokens vs. dense text tokens"),
    (1.9, 4.5, "Modality dominance", "attention flows mostly to the text tokens"),
    (4.5, 8.1, "MoIR: Information Router", "routes complementary information into less informative channels"),
    (8.1, 11.1, "Balanced modality usage", "information-dense tokens on both sides"),
    (11.1, 11.4, "Information disparity", "sparse visual tokens vs. dense text tokens"),
]
FADE = 0.3
TOTAL = KEYS[-1][0]

IMG_X = [0.08 + 0.09 * i for i in range(4)]
TXT_X = [0.56 + 0.09 * i for i in range(4)]
TOK_W, TOK_Y, TOK_H = 0.08, 0.49, 0.095
DEC_Y, DEC_H = 0.83, 0.1


def ease(t):
    return t * t * (3 - 2 * t)


def params(t):
    for a, b in zip(KEYS, KEYS[1:]):
        if a[0] <= t <= b[0]:
            s = 0.0 if b[0] == a[0] else (t - a[0]) / (b[0] - a[0])
            # routing progress moves linearly so the dots flow at a steady pace
            r = a[5] + s * (b[5] - a[5])
            s = ease(s)
            lerp = lambda x, y: (1 - s) * np.array(x, float) + s * np.array(y, float)
            return lerp(a[1], b[1]), lerp(a[2], b[2]), float(lerp(a[3], b[3])), float(lerp(a[4], b[4])), r
    return params(TOTAL)


def caption(t):
    for start, end, title, sub in CAPS:
        if start <= t < end:
            alpha = min(1.0, (t - start) / FADE if start > 0 else 1.0, (end - t) / FADE if end < TOTAL else 1.0)
            return title, sub, max(alpha, 0.0)
    return CAPS[-1][2], CAPS[-1][3], 1.0


def tok_color(base, v):
    return tuple(1 - v * (1 - base))


def bezier(p0, p1, p2, s):
    return (1 - s) ** 2 * p0 + 2 * (1 - s) * s * p1 + s ** 2 * p2


def render(t, photo):
    img, txt, share, arrow_a, route = params(t)
    title, sub, cap_a = caption(t)

    fig = plt.figure(figsize=(W, H), dpi=DPI, facecolor="white")
    fig.text(0.5, 0.92, title, ha="center", va="center", fontsize=21, fontweight="bold", color="#222222", alpha=cap_a)
    fig.text(0.5, 0.835, sub, ha="center", va="center", fontsize=13, color="#555555", style="italic", alpha=cap_a)

    ax = fig.add_axes([0, 0, 1, 0.79])
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.set_axis_off()

    # LLM decoder
    ax.add_patch(FancyBboxPatch((0.08, DEC_Y), 0.84, DEC_H, boxstyle="round,pad=0.005,rounding_size=0.015",
                                fc="#fdf0cc", ec="#7a6a45", lw=1.2))
    ax.text(0.5, DEC_Y + DEC_H / 2, "LLM Decoder", ha="center", va="center", fontsize=14, color="#333333")

    # tokens
    for xs, vals, base, label in ((IMG_X, img, PINK, "Visual tokens"), (TXT_X, txt, BLUE, "Text tokens")):
        for i, (x, v) in enumerate(zip(xs, vals)):
            fc = tok_color(base, v)
            ax.add_patch(FancyBboxPatch((x, TOK_Y), TOK_W, TOK_H, boxstyle="round,pad=0.003,rounding_size=0.01",
                                        fc=fc, ec="#444444", lw=1.0))
            ax.text(x + TOK_W / 2, TOK_Y + TOK_H / 2, f"T{i+1}", ha="center", va="center", fontsize=11,
                    color="white" if v > 0.6 else "#222222")
        ax.text(xs[0] + 2 * 0.09 - 0.005, TOK_Y - 0.06, label, ha="center", va="center", fontsize=11, color="#555555")

    # attention arrows from decoder to each modality, width ~ attention share
    if arrow_a > 0.01:
        top, bottom = DEC_Y - 0.01, TOK_Y + TOK_H + 0.015
        for cx, s in ((0.26, share), (0.74, 1 - share)):
            w = 0.006 + 0.05 * s
            ax.add_patch(FancyArrow(cx, top, 0, bottom - top, width=w, head_width=w * 1.9, head_length=0.04,
                                    length_includes_head=True, fc=ATTN, ec="none", alpha=arrow_a))
            ax.text(cx + 0.045, (top + bottom) / 2, f"{s*100:.0f}%", ha="left", va="center", fontsize=12,
                    fontweight="bold", color=ATTN, alpha=arrow_a)

    # information routing: dots flow between token rows
    if 0.0 < route < 1.0:
        ax.text(0.5, TOK_Y + TOK_H / 2, "MoIR", ha="center", va="center", fontsize=11, fontweight="bold",
                color="#1a7f37", bbox=dict(boxstyle="round,pad=0.25", fc="#e6f4ea", ec="#1a7f37", lw=1))
        flows = [(TXT_X[0], IMG_X[1], BLUE), (TXT_X[1], IMG_X[2], BLUE), (TXT_X[2], IMG_X[3], BLUE),
                 (TXT_X[1], IMG_X[1], BLUE), (IMG_X[0], TXT_X[3], PINK)]
        n_waves = 7
        for j, (sx, dx, col) in enumerate(flows):
            p0 = np.array([sx + TOK_W / 2, TOK_Y])
            p2 = np.array([dx + TOK_W / 2, TOK_Y])
            p0[1] = p2[1] = TOK_Y + TOK_H
            p1 = np.array([(p0[0] + p2[0]) / 2, TOK_Y + TOK_H + 0.32 + 0.05 * (j % 2)])
            for k in range(n_waves):
                s = route * (n_waves + 1) * 0.6 - 0.6 * k * 0.8 - 0.12 * j
                if 0 < s < 1:
                    x, y = bezier(p0, p1, p2, s)
                    ax.plot(x, y, "o", ms=9, color=tuple(col), alpha=0.9 * np.sin(np.pi * s) ** 0.5, mec="white", mew=0.8)

    # inputs
    ax.imshow(photo, extent=(0.13, 0.39, 0.02, 0.38), aspect="auto", zorder=0,
              alpha=1.0 if not (0 < route < 1) else 0.35)
    ax.text(0.74, 0.20, "“What is the woman\ncurrently making?”", ha="center", va="center", fontsize=14,
            family="serif", color="#222222", alpha=1.0 if not (0 < route < 1) else 0.35)

    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=DPI, facecolor="white")
    plt.close(fig)
    buf.seek(0)
    return Image.open(buf).convert("RGB")


photo = np.asarray(Image.open(PHOTO).convert("RGB"))
n = int(TOTAL * FPS)
images = [render(i / FPS, photo) for i in range(n)]

samples = images[:: max(1, len(images) // 10)]
sheet = Image.new("RGB", (images[0].width, images[0].height * len(samples)))
for k, im in enumerate(samples):
    sheet.paste(im, (0, im.height * k))
pal = sheet.quantize(colors=192, method=Image.Quantize.MEDIANCUT)
q = [im.quantize(palette=pal, dither=Image.Dither.NONE) for im in images]
q[0].save(OUT, save_all=True, append_images=q[1:], duration=int(1000 / FPS), loop=0, optimize=True)
print(len(q), "frames ->", OUT)
