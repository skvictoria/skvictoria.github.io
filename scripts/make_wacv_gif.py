"""Animated teaser for WACV 2026: Countering Multi-modal Representation Collapse."""
import io
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

OUT = sys.argv[1]
FPS = 20
W, H, DPI = 8.0, 4.2, 100

REDS = ["#8b0a1a", "#e8504f", "#f7b6b2"]
BLUES = ["#08519c", "#4ba3dc", "#bfe0f5"]
COLORS = REDS + BLUES

# (label, sublabel, eigenvalues u1..u6, hold seconds)
STATES = [
    ("RGB", "eigenspectrum of RGB features", [0.90, 0.72, 0.50, 0.0, 0.0, 0.0], 1.4),
    ("Depth", "complementary directions", [0.0, 0.0, 0.0, 0.88, 0.70, 0.52], 1.4),
    ("Naive fusion", "feature collapse", [0.92, 0.14, 0.07, 0.86, 0.12, 0.06], 1.8),
    ("Naive fusion", "modality collapse", [0.85, 0.70, 0.52, 0.80, 0.0, 0.0], 1.8),
    ("Rank-enhancing Token Fuser", "balanced, high effective rank", [0.80, 0.70, 0.58, 0.80, 0.68, 0.58], 2.4),
]
TRANS = 0.6  # seconds of easing between states

# 6 eigen-directions on the sphere (unit vectors)
DIRS = np.array([
    [0, 0, -1], [0.85, 0.15, 0.25], [-0.6, 0.5, 0.35],
    [0, 0, 1], [-0.8, -0.3, 0.1], [0.55, -0.75, -0.2],
], dtype=float)
DIRS /= np.linalg.norm(DIRS, axis=1, keepdims=True)


def erank(vals):
    v = np.asarray(vals)
    v = v[v > 1e-6]
    p = v / v.sum()
    return float(np.exp(-(p * np.log(p)).sum()))


def ease(t):
    return t * t * (3 - 2 * t)


def timeline():
    frames = []
    n = len(STATES)
    for i, (label, sub, vals, hold) in enumerate(STATES):
        for _ in range(int(hold * FPS)):
            frames.append((label, sub, np.array(vals), 1.0))
        nxt = STATES[(i + 1) % n]
        for k in range(int(TRANS * FPS)):
            t = ease((k + 1) / (TRANS * FPS))
            v = (1 - t) * np.array(vals) + t * np.array(nxt[2])
            # crossfade the caption: old text fades out, new fades in
            if t < 0.5:
                frames.append((label, sub, v, 1 - 2 * t))
            else:
                frames.append((nxt[0], nxt[1], v, 2 * t - 1))
    return frames


def draw_sphere(ax, angle, vals):
    ax.set_axis_off()
    ax.set_xlim(-1, 1); ax.set_ylim(-1, 1); ax.set_zlim(-1, 1)
    ax.set_box_aspect((1, 1, 1))
    ax.view_init(elev=18, azim=angle)
    u = np.linspace(0, 2 * np.pi, 25)
    w = np.linspace(0, np.pi, 13)
    x = np.outer(np.cos(u), np.sin(w)); y = np.outer(np.sin(u), np.sin(w)); z = np.outer(np.ones_like(u), np.cos(w))
    ax.plot_wireframe(x, y, z, color="#c8c8c8", linewidth=0.5, rstride=1, cstride=1)
    for d, v, c in zip(DIRS, vals, COLORS):
        if v < 0.02:
            continue
        e = d * v
        ax.plot([0, e[0]], [0, e[1]], [0, e[2]], color=c, linewidth=4.5, solid_capstyle="round")


def render(label, sub, vals, alpha, angle):
    fig = plt.figure(figsize=(W, H), dpi=DPI, facecolor="white")
    fig.text(0.5, 0.92, label, ha="center", va="center", fontsize=21, fontweight="bold",
             color="#222222", alpha=alpha)
    fig.text(0.5, 0.835, sub, ha="center", va="center", fontsize=13, color="#555555",
             style="italic", alpha=alpha)

    # eigenvalue bars
    ax = fig.add_axes([0.07, 0.17, 0.45, 0.56])
    ax.bar(range(6), vals, color=COLORS, edgecolor="#333333", linewidth=0.8, width=0.72)
    ax.set_ylim(0, 1.0); ax.set_xlim(-0.6, 5.6)
    ax.set_xticks(range(6)); ax.set_xticklabels([f"$u_{i+1}$" for i in range(6)], fontsize=13)
    ax.set_yticks([])
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.set_ylabel("eigenvalue", fontsize=11, color="#555555")

    # effective rank readout
    er = erank(vals)
    fig.text(0.295, 0.06, f"Effective rank = {er:.2f}", ha="center", fontsize=13,
             color="#1a7f37" if er > 5.5 else "#333333", fontweight="bold")

    ax3 = fig.add_axes([0.53, 0.02, 0.46, 0.78], projection="3d")
    draw_sphere(ax3, angle, vals)

    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=DPI, facecolor="white")
    plt.close(fig)
    buf.seek(0)
    return Image.open(buf).convert("RGB")


frames = timeline()
images = []
for i, (label, sub, vals, alpha) in enumerate(frames):
    angle = 30 + 360 * i / len(frames)  # one full turn per loop
    images.append(render(label, sub, vals, alpha, angle))

# shared palette keeps colors stable across frames and the file small
samples = images[:: max(1, len(images) // 8)]
sheet = Image.new("RGB", (images[0].width, images[0].height * len(samples)))
for k, im in enumerate(samples):
    sheet.paste(im, (0, im.height * k))
pal = sheet.quantize(colors=128, method=Image.Quantize.MEDIANCUT)
q = [im.quantize(palette=pal, dither=Image.Dither.NONE) for im in images]
q[0].save(OUT, save_all=True, append_images=q[1:], duration=int(1000 / FPS), loop=0, optimize=True)
print(len(q), "frames ->", OUT)
