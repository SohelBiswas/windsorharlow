# -*- coding: utf-8 -*-
"""Dot-matrix world map generator.

Emits a <g id="wmDots"> for the shared SVG defs sprite, so the dots and the
animated overlay live in ONE coordinate system and cannot drift apart.
"""
import os, math

LAT_TOP, LAT_BOT = 78.0, -56.0
STEP = 3.2
W, H = 1000, 460

REGIONS = {
 "alaska":       [(-168,66),(-160,71),(-142,70),(-141,60),(-150,59),(-162,63)],
 "canada":       [(-141,60),(-141,70),(-125,70),(-110,69),(-95,72),(-82,74),(-70,73),(-62,60),
                  (-55,52),(-58,47),(-66,45),(-70,47),(-80,45),(-88,48),(-95,49),(-110,49),
                  (-123,49),(-130,54),(-135,58)],
 "usa":          [(-124,48),(-124,40),(-120,34),(-117,32),(-110,31),(-104,29),(-97,26),(-93,29),
                  (-88,30),(-82,25),(-80,32),(-76,35),(-74,40),(-70,43),(-67,45),(-83,45),
                  (-95,49),(-110,49)],
 "mexico":       [(-117,32),(-110,31),(-104,29),(-97,26),(-92,18),(-88,21),(-87,16),(-92,15),
                  (-98,16),(-105,20),(-110,24)],
 "cen_america":  [(-92,15),(-88,16),(-83,15),(-79,9),(-77,8),(-83,8),(-87,13)],
 "greenland":    [(-46,60),(-32,63),(-22,70),(-18,78),(-30,82),(-48,81),(-58,76),(-54,68)],
 "iceland":      [(-24,64),(-18,66),(-14,65),(-20,63)],
 "s_america":    [(-78,9),(-72,11),(-64,11),(-60,8),(-52,5),(-50,0),(-44,-2),(-38,-4),(-35,-7),
                  (-38,-13),(-40,-20),(-48,-25),(-53,-33),(-58,-38),(-62,-40),(-65,-45),
                  (-69,-52),(-73,-54),(-75,-46),(-73,-38),(-71,-30),(-70,-22),(-75,-15),
                  (-78,-6),(-80,-2),(-81,4)],
 "n_africa":     [(-17,21),(-16,28),(-10,31),(-2,35),(10,37),(20,33),(25,32),(33,31),(35,24),
                  (38,18),(43,12),(40,9),(32,10),(22,12),(15,14),(5,13),(-5,12),(-14,14)],
 "s_africa":     [(-5,12),(5,13),(15,14),(22,12),(32,10),(40,9),(43,12),(51,11),(48,3),(41,-2),
                  (40,-11),(37,-17),(33,-26),(26,-34),(18,-35),(13,-23),(12,-16),(9,-1),(8,5),
                  (0,6),(-8,5),(-13,9)],
 "madagascar":   [(43,-13),(48,-15),(50,-20),(47,-25),(44,-22)],
 "w_europe":     [(-10,37),(-9,43),(-2,43),(-2,49),(3,51),(7,53),(6,58),(9,58),(12,55),(11,59),
                  (16,62),(21,66),(25,70),(30,70),(31,60),(28,56),(24,54),(20,50),(17,48),
                  (13,46),(14,42),(17,40),(12,44),(8,44),(3,43),(-2,42)],
 "uk":           [(-6,50),(-5,54),(-3,58),(-1,58),(0,54),(1,51),(-4,50)],
 "ireland":      [(-10,52),(-7,55),(-5,53),(-9,51)],
 "e_europe":     [(20,50),(24,54),(28,56),(31,60),(32,66),(40,68),(48,67),(58,68),(60,60),
                  (56,52),(50,48),(44,44),(40,45),(34,45),(28,45),(24,46),(22,48)],
 "russia":       [(58,68),(66,72),(75,74),(85,77),(100,78),(112,76),(125,73),(140,72),(155,70),
                  (168,68),(178,66),(170,60),(160,58),(150,59),(142,54),(135,48),(130,44),
                  (127,50),(120,50),(110,49),(100,50),(90,48),(80,45),(73,40),(65,44),(58,50),
                  (55,55),(58,62)],
 "mid_east":     [(26,32),(32,31),(35,32),(38,37),(44,40),(48,38),(53,38),(58,37),(61,34),
                  (62,28),(58,24),(52,24),(48,29),(44,29),(43,13),(38,18),(35,24),(33,31)],
 "central_asia": [(48,44),(56,45),(65,45),(73,40),(75,37),(70,37),(66,38),(60,38),(55,40),(50,41)],
 "india":        [(68,24),(70,22),(73,17),(75,13),(77,8),(79,9),(80,13),(83,18),(86,21),(89,22),
                  (92,22),(95,25),(97,28),(92,28),(88,26),(84,27),(80,29),(77,33),(74,35),
                  (71,35),(69,29)],
 "sri_lanka":    [(80,9),(82,8),(82,6),(80,6)],
 "china":        [(73,40),(80,45),(90,48),(100,50),(110,49),(120,50),(127,50),(130,44),(126,40),
                  (122,40),(121,31),(118,24),(112,21),(108,21),(104,22),(100,25),(98,28),
                  (95,28),(92,28),(88,29),(82,33),(76,37)],
 "korea":        [(126,38),(129,38),(129,35),(126,34),(125,37)],
 "japan":        [(129,31),(131,34),(134,35),(137,36),(140,38),(142,41),(145,44),(146,43),
                  (144,41),(142,38),(140,35),(137,34),(134,32),(131,30)],
 "sea":          [(97,20),(100,20),(103,14),(106,10),(109,11),(105,9),(101,3),(104,2),(103,1),
                  (100,6),(98,8),(96,17)],
 "indonesia":    [(95,6),(99,2),(105,-6),(112,-8),(118,-9),(125,-9),(131,-4),(137,-3),(141,-3),
                  (147,-6),(151,-9),(150,-3),(143,0),(135,1),(128,1),(120,2),(112,3),(104,2),
                  (99,4)],
 "philippines":  [(120,18),(123,15),(126,9),(126,6),(122,7),(120,12),(118,16)],
 "australia":    [(114,-22),(119,-19),(126,-14),(131,-12),(137,-13),(142,-11),(146,-17),
                  (150,-22),(153,-28),(151,-34),(147,-38),(141,-38),(136,-35),(129,-32),
                  (120,-34),(115,-34)],
 "tasmania":     [(145,-41),(148,-41),(148,-43),(145,-43)],
 "new_zealand":  [(166,-46),(171,-44),(175,-41),(178,-38),(176,-37),(172,-40),(168,-44)],
 "png":          [(141,-3),(147,-6),(151,-9),(150,-3),(144,-2)],
}

def inside(x, y, poly):
    n, hit, j = len(poly), False, len(poly) - 1
    for i in range(n):
        xi, yi = poly[i]; xj, yj = poly[j]
        if ((yi > y) != (yj > y)) and (x < (xj - xi) * (y - yi) / ((yj - yi) or 1e-9) + xi):
            hit = not hit
        j = i
    return hit

def project(lon, lat):
    return ((lon + 180.0) / 360.0 * W, (LAT_TOP - lat) / (LAT_TOP - LAT_BOT) * H)

def land(lon, lat):
    return any(inside(lon, lat, p) for p in REGIONS.values())

# ---- markers: major technology hubs ----
CITIES = [
 ("INDIA",      78.9,  21.5, "home", "mid",   -18),
 ("USA",      -100.0,  40.0, "pt",   "mid",   -14),
 ("CANADA",    -95.0,  56.0, "pt",   "mid",   -14),
 ("BRAZIL",    -50.0, -12.0, "pt",   "mid",    20),
 ("UK",         -2.0,  53.5, "pt",   "end",   -12),
 ("IRELAND",    -8.0,  53.2, "pt",   "end",    16),
 ("GERMANY",    10.4,  51.2, "pt",   "start",  -1),
 ("SWEDEN",     16.0,  61.0, "pt",   "start", -12),
 ("POLAND",     19.5,  52.0, "pt",   "start",  16),
 ("UAE",        54.5,  24.0, "pt",   "start",  16),
 ("SINGAPORE", 103.8,   1.4, "pt",   "start",  16),
 ("JAPAN",     139.5,  36.0, "pt",   "start",  -8),
 ("SOUTH KOREA",127.5, 36.5, "pt",   "end",    14),
 ("CHINA",     108.0,  34.0, "pt",   "mid",   -14),
 ("AUSTRALIA", 134.0, -25.0, "pt",   "mid",    22),
 ("NEW ZEALAND",173.0,-41.5, "pt",   "end",    18),
 ("SOUTH AFRICA",25.0,-29.0, "pt",   "mid",    22),
]


dots, lat = [], LAT_TOP
while lat >= LAT_BOT:
    lon = -180.0
    while lon <= 180.0:
        if land(lon, lat):
            dots.append(project(lon, lat))
        lon += STEP
    lat -= STEP

# small nations (Singapore, Israel, Ireland) are finer than a 3.2-degree grid,
# so guarantee a dot cluster under every marker rather than leaving it at sea
for _n, _lo, _la, _k, _a, _d in CITIES:
    px, py = project(_lo, _la)
    if min((math.hypot(dx - px, dy - py) for dx, dy in dots), default=999) > 5.0:
        for ox, oy in ((0, 0), (5, 0), (0, 5)):
            dots.append((px + ox, py + oy))

D = 3
path = "".join(f"M{int(x)} {int(y)}h{D}v{D}h-{D}z" for x, y in dots)
group = f'    <g id="wmDots" fill="#16536B"><path d="{path}"/></g>'

# snap every marker onto the nearest generated dot so none float in open sea
def snap(lo, la):
    px, py = project(lo, la)
    best = min(dots, key=lambda d: (d[0] - px) ** 2 + (d[1] - py) ** 2)
    return round(best[0] + D / 2, 1), round(best[1] + D / 2, 1), math.hypot(best[0] - px, best[1] - py)

print(f"{len(dots)} dots  ·  path {len(path)//1024} KB\n")
print("marker snapping (every marker pinned to the nearest land dot):")
SNAPPED = []
for name, lo, la, kind, anchor, dy in CITIES:
    x, y, drift = snap(lo, la)
    SNAPPED.append({"name": name, "x": x, "y": y, "kind": kind, "anchor": anchor, "dy": dy})
    flag = "   " if drift < 6 else "adj"
    print(f"  {flag} {name:<13} -> x {x:6.1f} y {y:6.1f}   (moved {drift:4.1f}px onto land)")

# ---- keep labels from colliding: nudge dy until boxes clear ----
CH, PAD = 15.0, 3.0
def box(m):
    w = len(m["name"]) * 8.4 + 10
    x = m["x"] - (w / 2 if m["anchor"] == "mid" else (w if m["anchor"] == "end" else 0))
    return (x, m["y"] + m["dy"] - CH, w, CH)
def hits(a, b):
    ax, ay, aw, ah = box(a); bx, by, bw, bh = box(b)
    return not (ax + aw + PAD < bx or bx + bw + PAD < ax or ay + ah + PAD < by or by + bh + PAD < ay)
for _ in range(60):
    moved = False
    for i in range(len(SNAPPED)):
        for j in range(i + 1, len(SNAPPED)):
            if hits(SNAPPED[i], SNAPPED[j]):
                lo_i = SNAPPED[i] if SNAPPED[i]["dy"] > SNAPPED[j]["dy"] else SNAPPED[j]
                lo_i["dy"] += 3.5
                moved = True
    if not moved:
        break
oob = [m for m in SNAPPED if box(m)[0] < -2 or box(m)[0] + box(m)[2] > W + 2
       or box(m)[1] < -2 or box(m)[1] + box(m)[3] > H + 2]
if oob:
    print("\n!! labels outside the canvas:", [m["name"] for m in oob])
else:
    print("\nlabels outside canvas: 0")
print("label collisions after layout:",
      sum(1 for i in range(len(SNAPPED)) for j in range(i + 1, len(SNAPPED)) if hits(SNAPPED[i], SNAPPED[j])))

# ---- ASCII proof: does this actually look like the world? ----
print("\nASCII verification (# land, · marker):")
mark = {(round(m["x"] / W * 118), round(m["y"] / H * 40)) for m in SNAPPED}
for row in range(40):
    la = LAT_TOP - row * (LAT_TOP - LAT_BOT) / 40
    line = ""
    for col in range(118):
        lo = -180 + col * 360 / 118
        line += "O" if (col, row) in mark else ("#" if land(lo, la) else " ")
    print("  " + line)

out = os.path.join(os.path.dirname(__file__), "..", "public", "assets", "brand", "world-dots.svg")
open(out, "w").write(
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-label="World map">\n'
    f'{group}\n  <use href="#wmDots"/>\n</svg>\n')

open(os.path.join(os.path.dirname(__file__), "wmdots.svg.txt"), "w").write(group)

import json
open(os.path.join(os.path.dirname(__file__), "wmcities.json"), "w").write(json.dumps(SNAPPED, indent=1))
print(f"\nwrote {out}")
