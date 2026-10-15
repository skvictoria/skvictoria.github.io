"""Generate the small animated SVG icons shown beside each publication.

Usage (from the repo root): python3 scripts/make_icons.py
Writes images/icons/<name>.svg. geopid.svg is hand-written and not generated here.
"""
import math
import os
import random

OUT = "images/icons"
EASE = 'calcMode="spline" keySplines="{}"'

HEAD = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="120" height="120">\n'
BADGE = '  <circle cx="60" cy="60" r="52" fill="#fbfbfb" stroke="#cfcfcf" stroke-width="1.5"/>\n'


def anim(attr, values, key_times, dur, extra=""):
    """SMIL animate with smooth easing on every segment."""
    splines = ";".join(["0.4 0 0.2 1"] * (len(values) - 1))
    vals = ";".join(str(v) for v in values)
    kts = ";".join(str(k) for k in key_times)
    return (f'<animate attributeName="{attr}" values="{vals}" keyTimes="{kts}" dur="{dur}s" '
            f'repeatCount="indefinite" {EASE.format(splines)}{extra}/>')


def write(name, body):
    with open(os.path.join(OUT, f"{name}.svg"), "w") as f:
        f.write(HEAD + BADGE + body + "</svg>\n")
    print("wrote", name)


def wacv2026():
    """Eigenvalue bars: collapsed spectrum -> balanced spectrum after rank-targeted fusion."""
    colors = ["#8b0a1a", "#e8504f", "#f2a09c", "#08519c", "#4ba3dc", "#9fd0f0"]
    collapsed = [40, 9, 5, 38, 8, 4]
    balanced = [36, 31, 25, 36, 31, 25]
    base, w, gap, x0 = 84, 9, 3, 25.5
    kt = [0, 0.25, 0.5, 0.9, 1]
    body = f'  <line x1="22" y1="{base}" x2="98" y2="{base}" stroke="#555" stroke-width="2" stroke-linecap="round"/>\n'
    for i, (c, lo, hi) in enumerate(zip(colors, collapsed, balanced)):
        x = x0 + i * (w + gap)
        h = [lo, lo, hi, hi, lo]
        y = [base - v for v in h]
        body += (f'  <rect x="{x}" y="{base - lo}" width="{w}" height="{lo}" rx="2" fill="{c}">\n'
                 f'    {anim("height", h, kt, 4)}\n    {anim("y", y, kt, 4)}\n  </rect>\n')
    return body


def icip2026():
    """MoIR: information dots flow from dense text tokens into sparse visual tokens."""
    body = ""
    ys = [30, 46, 62, 78]
    pink_lo = [0.85, 0.2, 0.15, 0.3]
    for y, lo in zip(ys, pink_lo):
        hi = max(lo, 0.8)
        body += (f'  <rect x="24" y="{y}" width="20" height="12" rx="3" fill="#e0457b" fill-opacity="{lo}" '
                 f'stroke="#b8325f" stroke-width="1.2">\n'
                 f'    {anim("fill-opacity", [lo, lo, hi, hi, lo], [0, 0.2, 0.6, 0.9, 1], 4)}\n  </rect>\n')
    for y, op in zip(ys, [0.9, 1.0, 0.95, 0.55]):
        body += (f'  <rect x="76" y="{y}" width="20" height="12" rx="3" fill="#1f6fd1" fill-opacity="{op}" '
                 f'stroke="#174f96" stroke-width="1.2"/>\n')
    # dots travel along arcs from blue tokens to the pale pink ones
    for k, (sy, dy) in enumerate([(36, 52), (52, 68), (68, 84)]):
        path = f"M76,{sy} Q60,{min(sy, dy) - 14} 44,{dy}"
        body += (f'  <circle r="3.5" fill="#1f6fd1" opacity="0">\n'
                 f'    <animateMotion path="{path}" dur="4s" repeatCount="indefinite" '
                 f'keyPoints="0;0;1;1" keyTimes="0;{0.15 + 0.1 * k:.2f};{0.5 + 0.1 * k:.2f};1" calcMode="linear"/>\n'
                 f'    <animate attributeName="opacity" values="0;0;1;1;0;0" '
                 f'keyTimes="0;{0.14 + 0.1 * k:.2f};{0.2 + 0.1 * k:.2f};{0.45 + 0.1 * k:.2f};{0.52 + 0.1 * k:.2f};1" '
                 f'dur="4s" repeatCount="indefinite"/>\n  </circle>\n')
    return body


def icip2025():
    """Action anticipation: observed frames, then coarse and fine future segments fill in."""
    body = ""
    for i in range(3):
        x = 18 + i * 20
        body += (f'  <rect x="{x}" y="34" width="17" height="22" rx="3" fill="#7d9bc1" stroke="#4e6b91" stroke-width="1.2"/>\n'
                 f'  <circle cx="{x + 8.5}" cy="42" r="3" fill="#f3f6fb"/>\n'
                 f'  <path d="M{x + 3},54 Q{x + 8.5},{46} {x + 14},54" fill="#f3f6fb"/>\n')
    body += ('  <rect x="80" y="34" width="20" height="22" rx="3" fill="none" stroke="#999" stroke-width="1.5" stroke-dasharray="3 2.5"/>\n'
             '  <text x="90" y="51" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" font-size="15" font-weight="bold" fill="#e07a2a">?\n'
             f'    {anim("opacity", [1, 0.25, 1], [0, 0.5, 1], 2)}\n  </text>\n')
    # observed part of the two label levels
    body += ('  <rect x="18" y="64" width="57" height="8" rx="3" fill="#2e7d6b"/>\n')
    for i, c in enumerate(["#8fd1c0", "#5fb8a3", "#8fd1c0"]):
        body += f'  <rect x="{18 + i * 19}" y="76" width="17" height="8" rx="3" fill="{c}"/>\n'
    # anticipated future segments grow in
    kt = [0, 0.2, 0.55, 0.9, 1]
    body += (f'  <rect x="78" y="64" width="0" height="8" rx="3" fill="#e07a2a">\n'
             f'    {anim("width", [0, 0, 22, 22, 0], kt, 4)}\n  </rect>\n')
    for i, c in enumerate(["#f5b27a", "#f0975a"]):
        k2 = [0, 0.3 + 0.1 * i, 0.65 + 0.1 * i, 0.9, 1]
        body += (f'  <rect x="{78 + i * 12}" y="76" width="0" height="8" rx="3" fill="{c}">\n'
                 f'    {anim("width", [0, 0, 10, 10, 0], k2, 4)}\n  </rect>\n')
    return body


def icassp2026():
    """Speaker drift: a waveform whose color (speaker identity) slowly shifts along the utterance."""
    # gradient spans the whole waveform rather than each bar
    body = ('  <defs><linearGradient id="drift" gradientUnits="userSpaceOnUse" x1="23" x2="100" y1="0" y2="0">'
            '<stop offset="0" stop-color="#1f6fd1"/><stop offset="0.55" stop-color="#1f6fd1"/>'
            '<stop offset="1" stop-color="#e8504f"/></linearGradient></defs>\n')
    heights = [10, 22, 34, 18, 40, 26, 14, 30, 42, 20, 32, 12]
    for i, h in enumerate(heights):
        x = 23 + i * 6.6
        lo, hi = h * 0.45, h
        vals = [hi, lo, hi] if i % 2 else [lo, hi, lo]
        body += (f'  <rect x="{x:.1f}" y="{60 - hi / 2:.1f}" width="4" height="{hi}" rx="2" fill="url(#drift)">\n'
                 f'    {anim("height", vals, [0, 0.5, 1], 1.6)}\n'
                 f'    {anim("y", [round(60 - v / 2, 1) for v in vals], [0, 0.5, 1], 1.6)}\n  </rect>\n')
    # drift marker under the waveform
    body += ('  <path d="M34,90 L86,90" stroke="#bbb" stroke-width="1.5" stroke-dasharray="2 3"/>\n'
             '  <circle cx="34" cy="90" r="4" fill="#1f6fd1"/>\n'
             '  <circle cx="34" cy="90" r="4" fill="#e8504f">\n'
             f'    {anim("cx", [34, 34, 86, 86, 34], [0, 0.15, 0.7, 0.9, 1], 4)}\n'
             f'    {anim("opacity", [0, 0, 1, 1, 0], [0, 0.15, 0.7, 0.9, 1], 4)}\n  </circle>\n')
    return body


def dmlr2025():
    """DARai: a person at home observed through several sensor modalities."""
    body = ('  <path d="M28,58 L60,32 L92,58" fill="none" stroke="#6b5b4b" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>\n'
            '  <path d="M34,54 L34,88 L86,88 L86,54" fill="#fff6e8" stroke="#6b5b4b" stroke-width="3" stroke-linejoin="round"/>\n'
            # person
            '  <circle cx="60" cy="60" r="5.5" fill="#e07a2a"/>\n'
            '  <path d="M60,66 L60,78 M60,70 L53,74 M60,70 L67,66 M60,78 L55,86 M60,78 L65,86" stroke="#e07a2a" stroke-width="3" stroke-linecap="round" fill="none"/>\n'
            # camera in the corner with pulsing signal arcs
            '  <rect x="37" y="57" width="9" height="6" rx="1.5" fill="#1f6fd1"/>\n')
    for k, r in enumerate([5, 9]):
        body += (f'  <path d="M{46 + r * 0.6:.1f},{60 - r * 0.8:.1f} A{r},{r} 0 0 1 {46 + r * 0.6:.1f},{60 + r * 0.8:.1f}" '
                 f'fill="none" stroke="#1f6fd1" stroke-width="1.6" stroke-linecap="round" opacity="0">\n'
                 f'    {anim("opacity", [0, 0, 1, 0], [0, 0.15 + 0.2 * k, 0.45 + 0.2 * k, 1], 2)}\n  </path>\n')
    # heart-rate trace drawing itself along the floor
    trace = "M38,99 L50,99 L53,93 L57,103 L60,96 L63,99 L82,99"
    body += (f'  <path d="{trace}" fill="none" stroke="#e8504f" stroke-width="2" stroke-linecap="round" '
             f'stroke-linejoin="round" stroke-dasharray="60" stroke-dashoffset="60">\n'
             f'    {anim("stroke-dashoffset", [60, 0, 0, -60], [0, 0.45, 0.7, 1], 2.4)}\n  </path>\n')
    # wearable on the wrist
    body += '  <circle cx="67" cy="66" r="2.6" fill="#2e7d6b"/>\n'
    return body


def hex2025():
    """HEX: scattered embeddings gradually organize into hierarchical clusters."""
    random.seed(3)
    groups = [((42, 40), "#1f6fd1"), ((42, 80), "#4ba3dc"), ((82, 60), "#e07a2a")]
    body = ""
    # super-cluster outline around the two blue groups, then each fine cluster
    kt = [0, 0.15, 0.55, 0.85, 1]
    body += (f'  <ellipse cx="42" cy="60" rx="18" ry="35" fill="none" stroke="#1f6fd1" stroke-width="1.5" stroke-dasharray="3 3" opacity="0">\n'
             f'    {anim("opacity", [0, 0, 0.8, 0.8, 0], kt, 4)}\n  </ellipse>\n')
    for (cx, cy), c in groups:
        body += (f'  <circle cx="{cx}" cy="{cy}" r="11" fill="{c}" fill-opacity="0.12" stroke="none" opacity="0">\n'
                 f'    {anim("opacity", [0, 0, 1, 1, 0], kt, 4)}\n  </circle>\n')
    for (cx, cy), c in groups:
        for _ in range(4):
            sx, sy = random.uniform(28, 92), random.uniform(28, 92)
            tx, ty = cx + random.uniform(-5, 5), cy + random.uniform(-5, 5)
            body += (f'  <circle cx="{sx:.1f}" cy="{sy:.1f}" r="3.3" fill="{c}">\n'
                     f'    {anim("cx", [round(sx, 1), round(sx, 1), round(tx, 1), round(tx, 1), round(sx, 1)], kt, 4)}\n'
                     f'    {anim("cy", [round(sy, 1), round(sy, 1), round(ty, 1), round(ty, 1), round(sy, 1)], kt, 4)}\n  </circle>\n')
    return body


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    write("wacv2026", wacv2026())
    write("icip2026", icip2026())
    write("icip2025", icip2025())
    write("icassp2026", icassp2026())
    write("dmlr2025", dmlr2025())
    write("hex", hex2025())
