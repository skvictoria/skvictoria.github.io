"""Animated teaser for GeoPID: geometric decomposition and steering of visual information in VLMs."""
import io
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np
from PIL import Image

OUT, PHOTO = sys.argv[1], sys.argv[2]
FPS = 20
W, H, DPI = 8.0, 4.2, 100

VIS = ["#9cc3ee", "#4a8fdc", "#1b4f9c"]
TXT = ["#f5c28e", "#e98a3c", "#a8501c"]
RED = "#555555"
SYN = "#1f9d55"

# geometry: the two subspaces intersect along the redundant direction r
r = np.array([1.0, 0.0, 0.0])
a, b = np.radians(35), np.radians(-25)
v2 = np.array([0.0, np.cos(a), np.sin(a)])
t2 = np.array([0.0, np.cos(b), np.sin(b)])
syn = np.array([-0.35, -0.45, 1.0]); syn /= np.linalg.norm(syn)


def unit(x):
    return x / np.linalg.norm(x)


VIS_DIRS = [unit(0.45 * r + v2), unit(0.8 * r + v2), unit(1.2 * r + v2)]
TXT_DIRS = [unit(-0.3 * r - t2), unit(-0.6 * r - t2), unit(-0.9 * r - t2)]
RED_DIRS = [r, unit(r + 0.12 * v2), unit(r - 0.12 * t2)]

# keyframes: time, vis plane alpha, txt plane alpha, vis vec len, txt vec len, redundant len, synergy len, steer
KEYS = [
    (0.0,  1, 0, 0.75, 0.0, 0.0, 0.0, 0.0),
    (1.8,  1, 0, 0.75, 0.0, 0.0, 0.0, 0.0),
    (2.4,  0, 1, 0.0, 0.85, 0.0, 0.0, 0.0),
    (4.2,  0, 1, 0.0, 0.85, 0.0, 0.0, 0.0),
    (4.8,  1, 1, 0.45, 0.85, 0.8, 0.7, 0.0),
    (7.6,  1, 1, 0.45, 0.85, 0.8, 0.7, 0.0),
    (8.4,  1, 1, 0.95, 0.85, 0.8, 0.7, 1.0),
    (11.4, 1, 1, 0.95, 0.85, 0.8, 0.7, 1.0),
    (12.0, 1, 0, 0.75, 0.0, 0.0, 0.0, 0.0),
]
CAPS = [
    (0.0, 2.1, "Image representation space", "vision tokens span their own subspace"),
    (2.1, 4.5, "Text representation space", "“What a tidy room! The desk is spotless…”"),
    (4.5, 8.0, "GeoPID decomposition", "redundant, modality-unique, and synergistic directions"),
    (8.0, 11.7, "Steering along vision-unique directions", "training-free intervention at inference"),
    (11.7, 12.0, "Image representation space", "vision tokens span their own subspace"),
]
FADE = 0.3
TOTAL = KEYS[-1][0]


def ease(t):
    return t * t * (3 - 2 * t)


def params(t):
    for k0, k1 in zip(KEYS, KEYS[1:]):
        if k0[0] <= t <= k1[0]:
            s = 0.0 if k1[0] == k0[0] else ease((t - k0[0]) / (k1[0] - k0[0]))
            return [(1 - s) * x + s * y for x, y in zip(k0[1:], k1[1:])]
    return list(KEYS[-1][1:])


def caption(t):
    for start, end, title, sub in CAPS:
        if start <= t < end:
            alpha = min(1.0, (t - start) / FADE if start > 0 else 1.0, (end - t) / FADE if end < TOTAL else 1.0)
            return title, sub, max(alpha, 0.0)
    return CAPS[-1][2], CAPS[-1][3], 1.0


def disc(ax, u, v, color, alpha, radius=0.95):
    if alpha < 0.01:
        return
    th = np.linspace(0, 2 * np.pi, 60)
    pts = [radius * (np.cos(x) * u + 0.55 * np.sin(x) * v) for x in th]
    poly = Poly3DCollection([pts], facecolor=color, edgecolor=color, alpha=0.16 * alpha, linewidths=1.0)
    ax.add_collection3d(poly)


def arrow(ax, d, length, color, lw=3.5, alpha=1.0):
    if length < 0.02:
        return
    e = d * length
    ax.plot([0, e[0]], [0, e[1]], [0, e[2]], color=color, lw=lw, solid_capstyle="round", alpha=alpha)
    ax.scatter([e[0]], [e[1]], [e[2]], color=color, s=lw * 9, alpha=alpha, depthshade=False)


def render(t, photo):
    va, ta, vl, tl, rl, sl, steer = params(t)
    title, sub, cap_a = caption(t)

    fig = plt.figure(figsize=(W, H), dpi=DPI, facecolor="white")
    fig.text(0.5, 0.92, title, ha="center", va="center", fontsize=21, fontweight="bold", color="#222222", alpha=cap_a)
    fig.text(0.5, 0.835, sub, ha="center", va="center", fontsize=13, color="#555555", style="italic", alpha=cap_a)

    # inputs on the left: image fades with the vision plane, text with the text plane
    axp = fig.add_axes([0.03, 0.30, 0.17, 0.44])
    axp.imshow(photo); axp.set_axis_off()
    for im in axp.images:
        im.set_alpha(0.25 + 0.75 * va)
    fig.text(0.115, 0.17, "“What a tidy room!\nThe desk is spotless…”", ha="center", va="center",
             fontsize=10.5, family="serif", color="#a8501c", alpha=0.3 + 0.7 * ta,
             bbox=dict(boxstyle="round,pad=0.4", fc="white", ec="#e98a3c", lw=1.2, alpha=0.3 + 0.7 * ta))

    # 3D representation space
    ax = fig.add_axes([0.18, -0.02, 0.50, 0.84], projection="3d")
    ax.set_axis_off()
    ax.set_xlim(-0.8, 0.8); ax.set_ylim(-0.8, 0.8); ax.set_zlim(-0.8, 0.8)
    ax.set_box_aspect((1, 1, 1))
    ax.view_init(elev=16, azim=-60 + 40 * np.sin(2 * np.pi * t / TOTAL))
    u = np.linspace(0, 2 * np.pi, 25); w = np.linspace(0, np.pi, 13)
    ax.plot_wireframe(0.95 * np.outer(np.cos(u), np.sin(w)), 0.95 * np.outer(np.sin(u), np.sin(w)),
                      0.95 * np.outer(np.ones_like(u), np.cos(w)), color="#d6d6d6", lw=0.4)
    disc(ax, r, v2, "#4a8fdc", va)
    disc(ax, r, t2, "#e98a3c", ta)

    for d, c in zip(RED_DIRS, [RED] * 3):
        arrow(ax, d, rl, c, lw=3)
    for d, c in zip(TXT_DIRS, TXT):
        arrow(ax, d, tl, c)
    for d, c in zip(VIS_DIRS, VIS):
        if steer > 0.01:  # ghost of the pre-intervention vector
            arrow(ax, d, 0.45, c, lw=2, alpha=0.35 * steer)
        arrow(ax, d, vl, c, lw=3.5 + 1.5 * steer)
    arrow(ax, syn, sl, SYN, lw=3.5)

    # legend + model answer on the right
    leg = [(SYN, "Synergy-eval."), (VIS[1], "Vision-unique"), (RED, "Redundant"), (TXT[1], "Text-unique")]
    show = min(1.0, rl / 0.8)
    for i, (c, name) in enumerate(leg):
        y = 0.68 - 0.075 * i
        fig.lines.append(plt.Line2D([0.70, 0.745], [y, y], color=c, lw=4, alpha=show, transform=fig.transFigure))
        fig.text(0.755, y, name, va="center", fontsize=12, color="#333333", alpha=show)

    before = "praising the room’s\ntidiness"
    after = "the room is messy,\ncontradicting\nthe praise"
    if show > 0.01:
        fig.text(0.70, 0.30, "VLM answer", fontsize=11, color="#777777", fontweight="bold", alpha=show)
        fig.text(0.70, 0.19, f"“{before}.”", fontsize=11.5, va="center", family="serif", color="#a8501c",
                 alpha=show * (1 - steer))
        fig.text(0.70, 0.19, f"“{after}.”", fontsize=11.5, va="center", family="serif", color="#1b4f9c",
                 alpha=show * steer, fontweight="bold")

    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=DPI, facecolor="white")
    plt.close(fig)
    buf.seek(0)
    return Image.open(buf).convert("RGB")


photo = np.asarray(Image.open(PHOTO).convert("RGB"))
n = int(TOTAL * FPS)
images = [render(i / FPS, photo) for i in range(n)]

samples = images[:: max(1, len(images) // 12)]
sheet = Image.new("RGB", (images[0].width, images[0].height * len(samples)))
for k, im in enumerate(samples):
    sheet.paste(im, (0, im.height * k))
pal = sheet.quantize(colors=192, method=Image.Quantize.MEDIANCUT)
q = [im.quantize(palette=pal, dither=Image.Dither.NONE) for im in images]
q[0].save(OUT, save_all=True, append_images=q[1:], duration=int(1000 / FPS), loop=0, optimize=True)
print(len(q), "frames ->", OUT)
