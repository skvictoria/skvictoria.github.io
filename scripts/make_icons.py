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


def intendiff():
    """IntenDiff: noisy action samples denoise into trajectories that stay within the global intention."""
    random.seed(7)
    gx, gy = 30, 60
    xs = [43, 53, 63, 73, 83, 91]
    targets = [44, 60, 76]
    kt = [0, 0.15, 0.55, 0.9, 1]
    # intention-consistent region spreading out from the global intention
    body = (f'  <path d="M{gx},{gy} L96,36 Q100,60 96,84 Z" fill="#f48fb1" fill-opacity="0.16" '
            f'stroke="#f48fb1" stroke-opacity="0.5" stroke-width="1"/>\n')
    for ty in targets:
        clean = [gy + (ty - gy) * ((x - gx) / (xs[-1] - gx)) ** 0.7 for x in xs]
        noisy = [c + random.uniform(-16, 16) for c in clean]
        d_noisy = f"M{gx},{gy} " + " ".join(f"L{x},{y:.1f}" for x, y in zip(xs, noisy))
        d_clean = f"M{gx},{gy} " + " ".join(f"L{x},{y:.1f}" for x, y in zip(xs, clean))
        body += (f'  <path d="{d_noisy}" fill="none" stroke="#aaa" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round">\n'
                 f'    {anim("d", [d_noisy, d_noisy, d_clean, d_clean, d_noisy], kt, 4)}\n'
                 f'    {anim("stroke", ["#aaa", "#aaa", "#d81b60", "#d81b60", "#aaa"], kt, 4)}\n  </path>\n')
    # predicted action blocks appear once the samples are denoised
    for ty, c in zip(targets, ["#f8bbd0", "#f06292", "#f8bbd0"]):
        body += (f'  <rect x="91" y="{ty - 4}" width="12" height="8" rx="2.5" fill="{c}" stroke="#d81b60" stroke-width="1" opacity="0">\n'
                 f'    {anim("opacity", [0, 0, 1, 1, 0], [0, 0.45, 0.6, 0.9, 1], 4)}\n  </rect>\n')
    # global intention: making coffee
    body += (f'  <circle cx="{gx}" cy="{gy}" r="14" fill="#fde4ec" stroke="#d81b60" stroke-width="1.8"/>\n'
             f'  <path d="M{gx - 6},{gy - 2} L{gx + 4},{gy - 2} L{gx + 3},{gy + 7} Q{gx - 1},{gy + 9} {gx - 5},{gy + 7} Z" fill="#7b4a2e"/>\n'
             f'  <path d="M{gx + 4},{gy} q4,0 4,3 q0,3 -4.5,3" fill="none" stroke="#7b4a2e" stroke-width="1.6"/>\n')
    for k, dx in enumerate([-3, 1]):
        body += (f'  <path d="M{gx + dx},{gy - 5} q-2,-2.5 0,-5 q2,-2.5 0,-5" fill="none" stroke="#b07a5a" '
                 f'stroke-width="1.3" stroke-linecap="round" opacity="0.2">\n'
                 f'    {anim("opacity", [0.2, 1, 0.2], [0, 0.5, 1], 1.6 + 0.4 * k)}\n  </path>\n')
    return body


# ---------------------------------------------------------------- patents

def car(x, y, color="#1f6fd1"):
    """Side-view car, 36 wide; (x, y) is the top-left of the body."""
    return (f'  <path d="M{x},{y + 10} L{x + 4},{y + 4} Q{x + 6},{y + 1} {x + 10},{y + 1} L{x + 22},{y + 1} '
            f'Q{x + 26},{y + 1} {x + 29},{y + 5} L{x + 34},{y + 6} Q{x + 36},{y + 7} {x + 36},{y + 10} '
            f'L{x + 36},{y + 13} L{x},{y + 13} Z" fill="{color}"/>\n'
            f'  <path d="M{x + 7},{y + 5} L{x + 9},{y + 3} L{x + 16},{y + 3} L{x + 16},{y + 6} Z '
            f'M{x + 18},{y + 3} L{x + 23},{y + 3} L{x + 26},{y + 6} L{x + 18},{y + 6} Z" fill="#e8f1fc"/>\n'
            f'  <circle cx="{x + 8}" cy="{y + 13}" r="3.6" fill="#333"/><circle cx="{x + 28}" cy="{y + 13}" r="3.6" fill="#333"/>\n')


def ground(y=80):
    return f'  <line x1="16" y1="{y}" x2="104" y2="{y}" stroke="#bbb" stroke-width="2" stroke-linecap="round"/>\n'


def pin(x, y, color="#e8504f"):
    """Location pin whose tip is at (x, y)."""
    return (f'<path d="M{x},{y} C{x - 3},{y - 5} {x - 7},{y - 8} {x - 7},{y - 13} A7,7 0 1 1 {x + 7},{y - 13} '
            f'C{x + 7},{y - 8} {x + 3},{y - 5} {x},{y} Z" fill="{color}"/>'
            f'<circle cx="{x}" cy="{y - 13}" r="2.6" fill="#fff"/>')


def bounce(dy, dur):
    return (f'<animateTransform attributeName="transform" type="translate" values="0 0;0 -{dy};0 0" '
            f'keyTimes="0;0.5;1" dur="{dur}s" repeatCount="indefinite" calcMode="spline" '
            f'keySplines="0.4 0 0.2 1;0.4 0 0.2 1"/>')


def object_position():
    """Car senses an object outside the vehicle and localizes it."""
    body = ground() + car(16, 63)
    body += '  <path d="M84,80 L90,62 L96,80 Z" fill="#f39c3d"/><rect x="85" y="69" width="10" height="3" fill="#fff"/>\n'
    for k, r in enumerate([10, 18, 26]):
        body += (f'  <path d="M{52 + r * 0.5:.1f},{70 - r * 0.6:.1f} A{r},{r} 0 0 1 {52 + r * 0.5:.1f},{70 + r * 0.6:.1f}" '
                 f'fill="none" stroke="#1f6fd1" stroke-width="2" stroke-linecap="round" opacity="0">\n'
                 f'    {anim("opacity", [0, 0, 0.9, 0], [0, 0.1 + 0.2 * k, 0.3 + 0.2 * k, 1], 2)}\n  </path>\n')
    body += f'  <g>{pin(90, 56)}{bounce(5, 1.2)}</g>\n'
    return body


def object_height():
    """Estimating the height of an object outside the vehicle."""
    body = ground() + car(14, 63)
    body += '  <rect x="72" y="42" width="18" height="38" rx="2" fill="#9aa5b1"/>\n'
    body += '  <rect x="75" y="46" width="12" height="6" rx="1" fill="#c9d1da"/><rect x="75" y="56" width="12" height="6" rx="1" fill="#c9d1da"/>\n'
    kt = [0, 0.15, 0.6, 0.9, 1]
    body += (f'  <line x1="98" y1="80" x2="98" y2="80" stroke="#e8504f" stroke-width="2.4" stroke-linecap="round">\n'
             f'    {anim("y2", [80, 80, 44, 44, 80], kt, 3)}\n  </line>\n'
             f'  <path d="M94,48 L98,42 L102,48" fill="none" stroke="#e8504f" stroke-width="2.4" stroke-linecap="round" '
             f'stroke-linejoin="round" opacity="0">\n    {anim("opacity", [0, 0, 1, 1, 0], kt, 3)}\n  </path>\n'
             f'  <line x1="94" y1="80" x2="102" y2="80" stroke="#e8504f" stroke-width="2.4" stroke-linecap="round"/>\n')
    return body


def road_facility():
    """A multi-modal camera recognizes road facilities such as signs."""
    body = ground(88)
    body += ('  <rect x="20" y="34" width="22" height="15" rx="3" fill="#455a64"/>\n'
             '  <circle cx="31" cy="41.5" r="4.6" fill="#90caf9" stroke="#fff" stroke-width="1.5"/>\n'
             '  <rect x="26" y="30" width="8" height="5" rx="1.5" fill="#455a64"/>\n'
             '  <line x1="31" y1="49" x2="31" y2="88" stroke="#78909c" stroke-width="3"/>\n')
    body += (f'  <path d="M42,38 L92,30 L92,74 L42,46 Z" fill="#ffd54f" opacity="0.15">\n'
             f'    {anim("opacity", [0.08, 0.35, 0.08], [0, 0.5, 1], 2)}\n  </path>\n')
    body += ('  <line x1="82" y1="60" x2="82" y2="88" stroke="#78909c" stroke-width="3"/>\n'
             '  <path d="M82,38 L95,61 L69,61 Z" fill="#fff" stroke="#e8504f" stroke-width="3.2" stroke-linejoin="round"/>\n'
             '  <rect x="80.7" y="46" width="2.6" height="7" rx="1" fill="#333"/><circle cx="82" cy="56.5" r="1.5" fill="#333"/>\n')
    kt = [0, 0.3, 0.45, 0.9, 1]
    body += (f'  <rect x="64" y="33" width="36" height="33" rx="3" fill="none" stroke="#1f9d55" stroke-width="2" '
             f'stroke-dasharray="4 3" opacity="0">\n    {anim("opacity", [0, 0, 1, 1, 0], kt, 3)}\n  </rect>\n')
    return body


def license_plate():
    """Locating the vehicle by recognizing license plates."""
    body = ('  <rect x="22" y="52" width="76" height="30" rx="5" fill="#fff" stroke="#333" stroke-width="2.5"/>\n'
            '  <text x="60" y="73" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" font-size="15" '
            'font-weight="bold" fill="#333" letter-spacing="1">12 3456</text>\n'
            '  <circle cx="28" cy="58" r="1.4" fill="#999"/><circle cx="92" cy="58" r="1.4" fill="#999"/>\n')
    body += (f'  <line x1="20" y1="54" x2="100" y2="54" stroke="#e8504f" stroke-width="2" opacity="0.85">\n'
             f'    {anim("y1", [54, 80, 54], [0, 0.5, 1], 2)}\n    {anim("y2", [54, 80, 54], [0, 0.5, 1], 2)}\n  </line>\n')
    body += (f'  <g opacity="0">{pin(60, 46, "#1f6fd1")}\n'
             f'    {anim("opacity", [0, 0, 1, 1, 0], [0, 0.35, 0.5, 0.9, 1], 4)}\n'
             f'    <animateTransform attributeName="transform" type="translate" values="0 -14;0 -14;0 0;0 0;0 -14" '
             f'keyTimes="0;0.35;0.5;0.9;1" dur="4s" repeatCount="indefinite"/>\n  </g>\n')
    return body


def road(body=""):
    """Road in perspective with a center lane, plus a top-view ego car."""
    return (body + '  <path d="M44,104 L54,22 L66,22 L76,104 Z" fill="#eceff1"/>\n'
            '  <path d="M44,104 L54,22 M76,104 L66,22" stroke="#90a4ae" stroke-width="2" fill="none"/>\n'
            '  <path d="M60,100 L60,26" stroke="#fff" stroke-width="1.6" stroke-dasharray="5 5"/>\n')


def ego(x=54, y=82):
    return (f'  <rect x="{x}" y="{y}" width="12" height="18" rx="3.5" fill="#1f6fd1"/>\n'
            f'  <rect x="{x + 2}" y="{y + 3}" width="8" height="4" rx="1" fill="#e8f1fc"/>\n')


def path_prediction():
    """Predicting the future driving path of the vehicle."""
    body = road() + ego()
    path = "M60,82 C60,66 60,58 66,46 S74,30 72,24"
    alt = "M60,82 C60,66 58,56 54,46 S48,30 50,24"
    body += (f'  <path d="{alt}" fill="none" stroke="#f39c3d" stroke-width="2.5" stroke-linecap="round" '
             f'stroke-dasharray="70" stroke-dashoffset="70" opacity="0.55">\n'
             f'    {anim("stroke-dashoffset", [70, 70, 0, 0, 70], [0, 0.25, 0.65, 0.9, 1], 3.5)}\n  </path>\n'
             f'  <path d="{path}" fill="none" stroke="#e8504f" stroke-width="3.2" stroke-linecap="round" '
             f'stroke-dasharray="70" stroke-dashoffset="70">\n'
             f'    {anim("stroke-dashoffset", [70, 0, 0, 70], [0, 0.45, 0.9, 1], 3.5)}\n  </path>\n')
    return body


def path_training():
    """Training a path prediction model: the prediction converges to the ground-truth path."""
    body = road()
    body = body.replace("L54,22 L66,22", "L54,52 L66,52").replace("M44,104 L54,22 M76,104 L66,22", "M44,104 L54,52 M76,104 L66,52")
    body = body.replace("L60,26", "L60,56")
    body += ego(54, 86)
    # small network above the road
    layers = [[30, 46], [24, 38, 52], [38]]
    xs = [36, 60, 84]
    for (xa, la), (xb, lb) in zip(zip(xs, layers), zip(xs[1:], layers[1:])):
        for ya in la:
            for yb in lb:
                body += f'  <line x1="{xa}" y1="{ya}" x2="{xb}" y2="{yb}" stroke="#b0bec5" stroke-width="1.2"/>\n'
    for k, (x, la) in enumerate(zip(xs, layers)):
        for y in la:
            body += (f'  <circle cx="{x}" cy="{y}" r="4.2" fill="#7e57c2">\n'
                     f'    {anim("fill-opacity", [0.4, 1, 0.4], [0, 0.5, 1], 1.5 + 0.3 * k)}\n  </circle>\n')
    gt = "M60,86 C60,76 62,68 66,60 S70,54 70,52"
    bad = "M60,86 C60,76 54,70 50,64 S46,56 47,52"
    kt = [0, 0.15, 0.65, 0.9, 1]
    body += (f'  <path d="{gt}" fill="none" stroke="#1f9d55" stroke-width="2.2" stroke-dasharray="3 3" stroke-linecap="round"/>\n'
             f'  <path d="{bad}" fill="none" stroke="#e8504f" stroke-width="3" stroke-linecap="round">\n'
             f'    {anim("d", [bad, bad, gt, gt, bad], kt, 4)}\n  </path>\n')
    return body


def label_errors():
    """Detecting label errors in a training dataset."""
    body = ""
    cards = [(22, 30, "#1f9d55"), (63, 30, "#1f9d55"), (22, 64, "#1f9d55"), (63, 64, "#1f9d55")]
    for i, (x, y, c) in enumerate(cards):
        body += (f'  <rect x="{x}" y="{y}" width="35" height="27" rx="3" fill="#e3f2fd" stroke="#90a4ae" stroke-width="1.2"/>\n'
                 f'  <path d="M{x + 4},{y + 23} L{x + 13},{y + 13} L{x + 19},{y + 19} L{x + 24},{y + 15} L{x + 31},{y + 23} Z" fill="#90caf9"/>\n')
        if i == 3:
            kt = [0, 0.55, 0.65, 0.92, 1]
            body += (f'  <rect x="{x + 22}" y="{y - 4}" width="15" height="9" rx="2.5" fill="{c}">\n'
                     f'    {anim("fill", [c, c, "#e8504f", "#e8504f", c], kt, 4)}\n  </rect>\n'
                     f'  <text x="{x + 29.5}" y="{y + 3.6}" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" '
                     f'font-size="8" font-weight="bold" fill="#fff" opacity="0">!\n'
                     f'    {anim("opacity", [0, 0, 1, 1, 0], kt, 4)}\n  </text>\n')
        else:
            body += (f'  <rect x="{x + 22}" y="{y - 4}" width="15" height="9" rx="2.5" fill="{c}"/>\n'
                     f'  <path d="M{x + 26},{y + 0.5} L{x + 28.5},{y + 3} L{x + 33},{y - 2}" fill="none" stroke="#fff" stroke-width="1.6" stroke-linecap="round"/>\n')
    # magnifier visits each card and stops on the mislabeled one
    pts = "0 0;41 0;0 34;41 34;41 34;0 0"
    body += ('  <g>\n'
             '    <circle cx="36" cy="40" r="9" fill="#fff" fill-opacity="0.35" stroke="#455a64" stroke-width="3"/>\n'
             '    <line x1="42.5" y1="46.5" x2="50" y2="54" stroke="#455a64" stroke-width="4" stroke-linecap="round"/>\n'
             f'    <animateTransform attributeName="transform" type="translate" values="{pts}" '
             f'keyTimes="0;0.18;0.36;0.55;0.92;1" dur="4s" repeatCount="indefinite"/>\n  </g>\n')
    return body


def seat_position():
    """Learning-based seat position control."""
    body = ground(92)
    body += '  <rect x="30" y="86" width="60" height="4" rx="2" fill="#90a4ae"/>\n'
    seat = ('<path d="M40,74 L74,74 Q80,74 80,80 L80,82 L40,82 Q36,82 36,78 Z" fill="#5c6bc0"/>'
            '<g><path d="M40,76 L32,40 Q31,34 37,34 L41,34 Q45,34 46,39 L50,74 Z" fill="#7986cb"/>'
            '<rect x="30" y="24" width="15" height="10" rx="4" fill="#7986cb"/>'
            '<animateTransform attributeName="transform" type="rotate" values="0 46 76;-14 46 76;-14 46 76;0 46 76" '
            'keyTimes="0;0.35;0.75;1" dur="4s" repeatCount="indefinite" calcMode="spline" '
            'keySplines="0.4 0 0.2 1;0 0 1 1;0.4 0 0.2 1"/></g>'
            '<rect x="56" y="82" width="6" height="5" fill="#455a64"/>')
    body += (f'  <g>{seat}\n    <animateTransform attributeName="transform" type="translate" '
             f'values="0 0;10 0;10 0;0 0" keyTimes="0;0.35;0.75;1" dur="4s" repeatCount="indefinite" '
             f'calcMode="spline" keySplines="0.4 0 0.2 1;0 0 1 1;0.4 0 0.2 1"/>\n  </g>\n')
    # sparkle: the position is chosen by a learned model
    body += (f'  <path d="M88,34 L90,40 L96,42 L90,44 L88,50 L86,44 L80,42 L86,40 Z" fill="#ffb300">\n'
             f'    {anim("opacity", [0.3, 1, 0.3], [0, 0.5, 1], 1.6)}\n  </path>\n')
    return body


def book_statistics():
    """Open statistics book: a dot climbs the steps on the left page, a bell curve draws on the right."""
    body = ('  <path d="M60,40 Q44,32 22,36 L22,86 Q44,82 60,90 Z" fill="#fffaf0" stroke="#8d6e63" stroke-width="2" stroke-linejoin="round"/>\n'
            '  <path d="M60,40 Q76,32 98,36 L98,86 Q76,82 60,90 Z" fill="#fffaf0" stroke="#8d6e63" stroke-width="2" stroke-linejoin="round"/>\n'
            '  <path d="M22,86 Q44,82 60,90 Q76,82 98,86 L98,90 Q76,86 60,94 Q44,86 22,90 Z" fill="#8d6e63"/>\n'
            '  <line x1="60" y1="40" x2="60" y2="90" stroke="#8d6e63" stroke-width="1.5"/>\n')
    # steps on the left page, with a dot hopping up one tread at a time
    n, x0, y0, w = 5, 25, 80, 6
    d = f"M{x0},{y0} " + " ".join(f"L{x0 + w * (k + 1)},{y0 - w * k} L{x0 + w * (k + 1)},{y0 - w * (k + 1)}" for k in range(n - 1))
    d += f" L{x0 + w * n},{y0 - w * (n - 1)}"
    body += f'  <path d="{d}" fill="none" stroke="#1f6fd1" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>\n'
    cx = ";".join(str(x0 + w * k + w / 2) for k in range(n)) + f";{x0 + w / 2}"
    cy = ";".join(str(y0 - w * k - 3.4) for k in range(n)) + f";{y0 - 3.4}"
    kts = ";".join(f"{k / n:.2f}" for k in range(n)) + ";1"
    body += (f'  <circle r="2.8" fill="#e8504f">\n'
             f'    <animate attributeName="cx" values="{cx}" keyTimes="{kts}" dur="3s" repeatCount="indefinite" calcMode="discrete"/>\n'
             f'    <animate attributeName="cy" values="{cy}" keyTimes="{kts}" dur="3s" repeatCount="indefinite" calcMode="discrete"/>\n'
             f'  </circle>\n')
    # bell curve on the right page
    pts = []
    for i in range(25):
        x = 65 + i * 1.2
        z = (x - 79.4) / 6.0
        pts.append(f"{x:.1f},{78 - 30 * math.exp(-z * z / 2):.1f}")
    curve = "M" + " L".join(pts)
    body += ('  <line x1="64" y1="78" x2="95" y2="78" stroke="#8d6e63" stroke-width="1.2"/>\n'
             f'  <path d="{curve}" fill="none" stroke="#1f9d55" stroke-width="2.4" stroke-linecap="round" '
             f'stroke-dasharray="80" stroke-dashoffset="80">\n'
             f'    {anim("stroke-dashoffset", [80, 0, 0, 80], [0, 0.5, 0.85, 1], 3)}\n  </path>\n')
    return body


PATENT_ICONS = {
    "patent-object-position": object_position,
    "patent-object-height": object_height,
    "patent-road-facility": road_facility,
    "patent-license-plate": license_plate,
    "patent-path-prediction": path_prediction,
    "patent-path-training": path_training,
    "patent-label-errors": label_errors,
    "patent-seat-position": seat_position,
}


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    write("wacv2026", wacv2026())
    write("icip2026", icip2026())
    write("icip2025", icip2025())
    write("icassp2026", icassp2026())
    write("dmlr2025", dmlr2025())
    write("hex", hex2025())
    write("intendiff", intendiff())
    for name, fn in PATENT_ICONS.items():
        write(name, fn())
    write("book-statistics", book_statistics())
