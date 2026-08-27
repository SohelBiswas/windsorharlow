# -*- coding: utf-8 -*-
"""Isometric layered-platform diagram for the intro section.

Four stacked planes — Infrastructure, Data, Services, Interface — each a grid
of cells that light up as a build pulse travels up the stack.
"""
import random, os
random.seed(7)

W, H = 640, 620
CX = 300
HW, HH = 208, 82          # half-width / half-height of each plane
N = 4                     # cells per side
LAYERS = [
    ("Interface",      118, "Web, mobile and design-system surfaces"),
    ("Services",       248, "APIs, workers, queues and orchestration"),
    ("Data",           378, "Stores, streams, retrieval and models"),
    ("Infrastructure", 508, "Cloud, containers, pipelines and policy"),
]

def cells(cy):
    """Subdivide an isometric rhombus into an N x N grid."""
    L = (CX - HW, cy)
    ax, ay = HW / N, -HH / N      # left -> top edge
    bx, by = HW / N, HH / N       # left -> bottom edge
    out = []
    for i in range(N):
        for j in range(N):
            px, py = L[0] + i * ax + j * bx, L[1] + i * ay + j * by
            pts = [(px, py), (px + ax, py + ay), (px + ax + bx, py + ay + by), (px + bx, py + by)]
            out.append((i, j, " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)))
    return out

parts = []
for li, (name, cy, _desc) in enumerate(LAYERS):
    delay = round(li * 0.34, 2)
    parts.append(f'      <g class="pf-layer" style="--d:{delay}s">')
    # outline
    parts.append(
        f'        <polygon class="pf-plane" points="{CX} {cy-HH} {CX+HW} {cy} {CX} {cy+HH} {CX-HW} {cy}"/>')
    # cells, a handful lit
    lit = set(random.sample(range(N * N), 5))
    for k, (i, j, pts) in enumerate(cells(cy)):
        cls = "pf-cell"
        if k in lit:
            cls += " lit" if k % 2 else " lit alt"
        cd = round(delay + 0.25 + (i + j) * 0.09, 2)
        parts.append(f'        <polygon class="{cls}" points="{pts}" style="--d:{cd}s"/>')
    # edge highlight along the top-left face
    parts.append(f'        <path class="pf-edge" d="M{CX-HW} {cy} L{CX} {cy-HH} L{CX+HW} {cy}"/>')
    parts.append(f'        <text class="pf-name" x="{CX+HW+22}" y="{cy-2}">{name.upper()}</text>')
    parts.append(f'        <line class="pf-tick" x1="{CX+HW+4}" y1="{cy-6}" x2="{CX+HW+16}" y2="{cy-6}"/>')
    parts.append('      </g>')

# the column that carries a pulse up through the stack
column = (f'      <line class="pf-spine" x1="{CX}" y1="{LAYERS[-1][1]+HH}" x2="{CX}" y2="{LAYERS[0][1]-HH}"/>\n'
          f'      <line class="pf-pulse" x1="{CX}" y1="{LAYERS[-1][1]+HH}" x2="{CX}" y2="{LAYERS[0][1]-HH}"/>')

svg = f'''<svg class="platform" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg"
         role="img" aria-label="The four layers Windsor Harlow builds: infrastructure, data, services and interface"
         preserveAspectRatio="xMidYMid meet">
{column}
{chr(10).join(parts)}
    </svg>'''

open(os.path.join(os.path.dirname(__file__), "platform.svg.txt"), "w").write(svg)
print(f"{len(LAYERS)} layers x {N*N} cells  ·  {len(svg)//1024} KB")
for name, cy, _ in LAYERS:
    print(f"  {name:<15} centre y={cy}  spans {cy-HH}..{cy+HH}")
print("\nvertical extent:", LAYERS[0][1]-HH, "to", LAYERS[-1][1]+HH, "within viewBox height", H)
