"""A tiny flat-illustration kit for Cold Case Academy location pictures.
Every prop is drawn around its own origin and placed with at(x, y, scale).
All scenes are 640x190. Original drawings; no real logos or likenesses."""

W, H = 640, 190
FLOOR = 150


def at(x, y, s, body, flip=False):
    sx = -s if flip else s
    return f'<g transform="translate({x} {y}) scale({sx} {s})">{body}</g>'


def rect(x, y, w, h, fill, rx=0, extra=""):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" {extra}/>'


def circ(x, y, r, fill, extra=""):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" {extra}/>'


def path(d, fill="none", stroke=None, sw=2, extra=""):
    st = f' stroke="{stroke}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"' if stroke else ""
    return f'<path d="{d}" fill="{fill}"{st} {extra}/>'


def text(x, y, s, size=14, fill="#2a2420", anchor="middle", font="Special Elite, Courier New, monospace", weight="400"):
    return f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" font-weight="{weight}">{s}</text>'


# ---------- backgrounds ----------
def room(wall="#d9c9a8", floor="#8a6a4a", trim="#6e5238", stripes=None, wainscot=None):
    out = rect(0, 0, W, FLOOR, wall)
    if stripes:
        out += "".join(rect(x, 0, 14, FLOOR, stripes) for x in range(10, W, 40))
    if wainscot:
        out += rect(0, 100, W, 50, wainscot)
        out += rect(0, 98, W, 4, trim)
    out += rect(0, FLOOR, W, H - FLOOR, floor) + rect(0, FLOOR - 4, W, 6, trim)
    out += "".join(f'<line x1="{x}" y1="{FLOOR+2}" x2="{x-30}" y2="{H}" stroke="{trim}" stroke-width="1.5" opacity=".35"/>' for x in range(40, W + 40, 70))
    return out


def sky(top="#8fc1e3", bottom="#e6f2f8", gid="sk"):
    return (f'<defs><linearGradient id="{gid}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{top}"/>'
            f'<stop offset="1" stop-color="{bottom}"/></linearGradient></defs>' + rect(0, 0, W, H, f"url(#{gid})"))


def night(gid="nt", top="#0e1a2e", bottom="#2c4a6e", moon=True):
    s = sky(top, bottom, gid)
    s += "".join(circ(x, y, r, "#fff", 'opacity=".8"') for x, y, r in [(40, 22, 1.4), (130, 14, 1), (220, 36, 1.2), (330, 12, 1), (430, 28, 1.3), (520, 16, 1), (600, 40, 1.2), (280, 50, 1)])
    if moon:
        s += circ(560, 44, 18, "#f3ead2") + circ(568, 39, 16, top)
    return s


def ground(color="#7a9a5a", y=150):
    return rect(0, y, W, H - y, color)


def water(y=140, color="#3f7f9a", line="#d7eef5"):
    out = rect(0, y, W, H - y, color)
    out += "".join(f'<line x1="{x}" y1="{y+12+(i%3)*12}" x2="{x+50}" y2="{y+12+(i%3)*12}" stroke="{line}" stroke-width="2" opacity=".5"/>' for i, x in enumerate(range(20, W, 90)))
    return out


# ---------- furniture & objects ----------
def desk(w=200, top="#7a5234", leg="#5a3b24"):
    return (rect(0, 0, w, 10, top, 2) + rect(6, 10, 10, 40, leg) + rect(w - 16, 10, 10, 40, leg)
            + rect(w - 70, 10, 54, 24, leg, 2) + rect(w - 50, 20, 14, 3, "#c9a46a"))


def lamp(c="#2f6b3a"):
    return (rect(-14, 36, 28, 5, "#333", 2) + path("M0 36 L8 10", stroke="#333", sw=3)
            + path("M-4 2 L22 14 L14 22 Z", fill=c) + path("M14 22 L40 54 L-8 54 Z", fill="#fff6c0", extra='opacity=".35"'))


def typewriter():
    return (path("M0 30 L8 6 L62 6 L70 30 Z", fill="#2f3a44") + rect(10, -6, 50, 12, "#f6f1e3")
            + rect(4, 2, 62, 6, "#1f262d", 2) + "".join(circ(14 + i * 7, 22, 2.4, "#d9d2c4") for i in range(7)))


def phone(c="#1f1f1f"):
    return (path("M0 20 Q4 4 30 4 Q56 4 60 20 Z", fill=c) + rect(4, 18, 52, 10, c, 4)
            + circ(30, 14, 7, "#e9e2d0") + circ(30, 14, 2, c) + path("M2 4 Q30 -10 58 4", stroke=c, sw=7))


def papers(n=4, c="#fbf6e8"):
    out = ""
    for i in range(n):
        out += rect(i * 2 - 2, -i * 3, 46, 8, c, 1, f'stroke="#cdbf9f" stroke-width="1" transform="rotate({(-1)**i*3} 20 0)"')
    return out


def folder(c="#d9b979", label=None):
    out = path("M0 6 L14 6 L18 0 L36 0 L40 6 L70 6 L70 46 L0 46 Z", fill=c) + rect(4, 12, 62, 30, "#fbf6e8", 1)
    out += "".join(rect(10, 18 + i * 7, 46 - i * 6, 2.5, "#9c8f7a") for i in range(3))
    if label:
        out += rect(18, 30, 40, 12, "none", 2, 'stroke="#a3231d" stroke-width="2" transform="rotate(-8 38 36)"') + text(38, 40, label, 8, "#a3231d")
    return out


def filebox(c="#c9a875"):
    return rect(0, 0, 60, 34, c, 2) + rect(0, 0, 60, 8, "#b08d58", 2) + rect(20, 16, 20, 8, "#fbf6e8", 1)


def drawers(cols=6, rows=4, c="#8a5a35", h="#d9b979"):
    out = rect(-4, -4, cols * 34 + 8, rows * 26 + 8, "#5c3b22", 3)
    for r in range(rows):
        for k in range(cols):
            out += rect(k * 34, r * 26, 30, 22, c, 2) + rect(k * 34 + 9, r * 26 + 9, 12, 4, h, 1) + rect(k * 34 + 11, r * 26 + 3, 8, 4, "#f3ead2")
    return out


def bookshelf(cols=5, rows=3, seed=1):
    pal = ["#a3231d", "#2f5d8a", "#2f6b3a", "#b8860b", "#6b4fa0", "#8a5a35", "#c0563b", "#3c6e71"]
    out = rect(0, 0, cols * 30 + 10, rows * 40 + 10, "#5c3b22", 2)
    i = seed
    for r in range(rows):
        x = 6
        while x < cols * 30:
            w = 6 + (i * 7) % 7
            hgt = 26 + (i * 5) % 9
            out += rect(x, r * 40 + 40 - hgt + 4, w, hgt, pal[i % len(pal)], 1)
            x += w + 1
            i += 3
        out += rect(0, r * 40 + 44, cols * 30 + 10, 5, "#3d2716")
    return out


def window(w=120, h=90, view="sky", frame="#5c3b22"):
    v = {"sky": "#bcdff2", "night": "#1a2d47", "dusk": "#f2b48b", "rain": "#8aa0b0"}.get(view, "#bcdff2")
    out = rect(-6, -6, w + 12, h + 12, frame, 3) + rect(0, 0, w, h, v)
    if view == "night":
        out += circ(w * .75, h * .3, 8, "#f3ead2") + "".join(circ(x, y, 1.2, "#fff") for x, y in [(15, 15), (40, 30), (70, 12), (25, 50)])
    if view == "rain":
        out += "".join(f'<line x1="{x}" y1="{y}" x2="{x-5}" y2="{y+12}" stroke="#dfe8ee" stroke-width="1.5"/>' for x, y in [(15, 10), (40, 30), (70, 15), (95, 40), (30, 60), (80, 65)])
    if view in ("sky", "dusk"):
        out += path(f"M0 {h*.75} L{w*.2} {h*.55} L{w*.35} {h*.7} L{w*.55} {h*.45} L{w*.8} {h*.68} L{w} {h*.55} L{w} {h} L0 {h} Z", fill="#7d8a96", extra='opacity=".7"')
    out += rect(w / 2 - 2, 0, 4, h, frame) + rect(0, h / 2 - 2, w, 4, frame)
    return out


def bay_window(w=200, h=100, frame="#3d2e23"):
    out = rect(-6, -6, w + 12, h + 12, frame, 3) + rect(0, 0, w, h * .7, "#a9cbe2") + rect(0, h * .7, w, h * .3, "#4f7f9a")
    out += path(f"M{w*.15} {h*.72} Q{w*.3} {h*.52} {w*.45} {h*.72} Z", fill="#5a524b")
    out += rect(w * .24, h * .52, w * .12, h * .08, "#6b625a")
    out += f'<g stroke="#c0392b" stroke-width="3" fill="none"><line x1="{w*.6}" y1="{h*.2}" x2="{w*.6}" y2="{h*.72}"/><line x1="{w*.88}" y1="{h*.2}" x2="{w*.88}" y2="{h*.72}"/><path d="M{w*.52} {h*.4} Q{w*.6} {h*.2} {w*.6} {h*.2} Q{w*.74} {h*.6} {w*.88} {h*.2} Q{w*.94} {h*.3} {w} {h*.4}"/><line x1="{w*.5}" y1="{h*.58}" x2="{w}" y2="{h*.58}"/></g>'
    return out


def painting(w=70, h=54, frame="#c9a14a", art="land"):
    out = rect(-6, -6, w + 12, h + 12, frame, 2) + rect(-2, -2, w + 4, h + 4, "#8a6a2a")
    if art == "land":
        out += rect(0, 0, w, h, "#9cc3d5") + path(f"M0 {h*.6} Q{w*.3} {h*.4} {w*.6} {h*.58} T{w} {h*.5} L{w} {h} L0 {h} Z", fill="#6f8f4a") + circ(w * .75, h * .25, 6, "#f3d27a")
    elif art == "sea":
        out += rect(0, 0, w, h, "#46607a") + path(f"M0 {h*.6} Q{w*.25} {h*.4} {w*.5} {h*.62} T{w} {h*.55} L{w} {h} L0 {h} Z", fill="#23394d") + path(f"M{w*.4} {h*.55} L{w*.5} {h*.15} L{w*.52} {h*.55} Z", fill="#e8dcc0")
    elif art == "portrait":
        out += rect(0, 0, w, h, "#3b3326") + circ(w / 2, h * .38, h * .16, "#d9b08c") + path(f"M{w*.2} {h} Q{w/2} {h*.5} {w*.8} {h} Z", fill="#1f1a14")
    elif art == "smile":
        out += rect(0, 0, w, h, "#6f7a4a") + path(f"M{w*.3} {h} Q{w/2} {h*.35} {w*.7} {h} Z", fill="#3b2c1a") + circ(w / 2, h * .36, h * .17, "#c9a171") + path(f"M{w*.32} {h*.3} Q{w/2} {h*.05} {w*.68} {h*.3} L{w*.66} {h*.6} Q{w/2} {h*.25} {w*.34} {h*.6} Z", fill="#2b2016")
    elif art == "empty":
        out += rect(0, 0, w, h, "#e8d9b6") + "".join(circ(x, y, 2, "#555") for x, y in [(6, 6), (w - 6, 6), (6, h - 6), (w - 6, h - 6)])
    elif art == "silk":
        out += rect(0, 0, w, h, "#7c8a5a") + "".join(path(f"M{x} 0 L{x} {h}", stroke="#8e9c69", sw=4) for x in range(6, int(w), 12))
    return out


def door(c="#6e4a2e", w=56, h=110):
    return (rect(0, 0, w, h, c, 2) + rect(6, 8, w - 12, h / 2 - 14, "#7e5a3e", 2) + rect(6, h / 2 + 2, w - 12, h / 2 - 12, "#7e5a3e", 2)
            + circ(w - 10, h / 2, 3.5, "#d9b979"))


def stairs(c="#9a8a74", n=6):
    out = ""
    for i in range(n):
        out += rect(i * 18, -i * 14, 120 - i * 18, 14, c if i % 2 else "#8a7a64")
    out += path(f"M0 -{n*14+20} L{n*18} -{n*14+20}", stroke="#5c4a36", sw=3)
    out += "".join(f'<line x1="{i*18+4}" y1="{-i*14}" x2="{i*18+4}" y2="{-i*14-26}" stroke="#5c4a36" stroke-width="2"/>' for i in range(n))
    return out


def camera_tripod():
    return (path("M0 0 L-24 70 M0 0 L24 70 M0 0 L0 72", stroke="#5c3b22", sw=4)
            + rect(-26, -34, 52, 34, "#7a5234", 3) + path("M26 -28 L48 -36 L48 -4 L26 -10 Z", fill="#2f2a26")
            + circ(52, -20, 7, "#1d1a17") + rect(-18, -44, 22, 10, "#4a3a2c", 2) + path("M-26 -26 L-44 -34 L-44 -14 L-26 -18 Z", fill="#1f1a14"))


def monitors(cols=3, rows=2):
    out = rect(-6, -6, cols * 70 + 8, rows * 52 + 8, "#2a2f36", 4)
    for r in range(rows):
        for k in range(cols):
            x, y = k * 70, r * 52
            out += rect(x, y, 64, 46, "#0d2a3a", 2) + rect(x + 3, y + 3, 58, 40, "#1d4f6a", 1)
            out += path(f"M{x+6} {y+36} L{x+20} {y+22} L{x+32} {y+30} L{x+46} {y+14} L{x+58} {y+26}", stroke="#7fd6ff", sw=1.5)
            out += text(x + 52, y + 12, f"0{r*cols+k+1}", 7, "#ffd25e")
    return out


def crt(screen="#0d3b2a", textcol="#7fff9e"):
    return (rect(0, 0, 80, 64, "#d8d0bd", 6) + rect(8, 8, 64, 44, screen, 3)
            + "".join(rect(14, 16 + i * 8, 40 - (i * 11) % 24, 3, textcol) for i in range(4)) + rect(26, 64, 28, 10, "#c4bba6") + rect(14, 74, 52, 6, "#b9b09b", 2))


def printer_paper():
    out = rect(0, 0, 70, 22, "#cfc7b2", 3) + rect(10, -40, 50, 42, "#fbf6e8", 1, 'stroke="#cdbf9f"')
    out += "".join(rect(14, -34 + i * 7, 36 - (i % 3) * 8, 2.5, "#4a4a4a") for i in range(5))
    out += "".join(circ(13, -36 + i * 8, 1.6, "#cdbf9f") + circ(57, -36 + i * 8, 1.6, "#cdbf9f") for i in range(5))
    return out


def laptop(face=True, screen="#bfe3f2"):
    out = rect(0, 0, 90, 58, "#2f3640", 4) + rect(5, 5, 80, 48, screen, 2) + path("M-10 58 L100 58 L92 66 L-2 66 Z", fill="#9aa3ad")
    if face:
        out += circ(45, 22, 9, "#d9a77c") + path("M28 53 Q45 30 62 53 Z", fill="#3d6b8f") + path("M36 18 Q45 8 54 18", fill="#4a3526")
    return out


def microscope():
    return (rect(-20, 60, 50, 8, "#3a3a3a", 2) + path("M0 60 L0 20 Q0 6 14 6", stroke="#4a4a4a", sw=8, fill="none")
            + rect(6, -20, 12, 34, "#6a6a6a", 2, 'transform="rotate(-20 12 0)"') + rect(-12, 40, 34, 4, "#7a7a7a") + circ(16, 30, 5, "#7fd6ff"))


def jars(n=4):
    pal = ["#c0563b", "#6f8f4a", "#2f5d8a", "#b8860b", "#6b4fa0"]
    out = ""
    for i in range(n):
        out += rect(i * 26, 0, 20, 34, "#e8f2f4", 4, 'stroke="#9fb5bb" stroke-width="1.5"') + rect(i * 26 + 2, 14, 16, 18, pal[i % 5], 3, 'opacity=".75"') + rect(i * 26 + 2, -4, 16, 6, "#7a7a7a", 1)
    return out


def bags(n=4):
    out = ""
    for i in range(n):
        out += path(f"M{i*30} 0 L{i*30+24} 0 L{i*30+26} 36 L{i*30-2} 36 Z", fill="#eef3f3", extra='stroke="#9fb5bb" stroke-width="1.5"')
        out += rect(i * 30 + 3, 4, 18, 5, "#c0392b", 1) + rect(i * 30 + 4, 16, 16, 14, ["#5a4a3a", "#2f2f2f", "#b8a07a", "#8a2a2a"][i % 4], 2, 'opacity=".55"')
    return out


def shelf(w=200, items=""):
    return items + rect(-6, 38, w, 6, "#5c3b22")


def magnifier():
    return circ(0, 0, 20, "#d7eef5", 'stroke="#4a3a2c" stroke-width="6" opacity=".95"') + path("M14 14 L36 36", stroke="#4a3a2c", sw=9)


def newspaper(headline="EXTRA!"):
    out = rect(0, 0, 90, 64, "#f3ecd9", 1, 'stroke="#bcae8e"') + text(45, 15, headline, 11, "#1f1a14")
    out += rect(6, 20, 78, 2, "#1f1a14") + rect(6, 26, 38, 30, "#c9bfa6") + "".join(rect(48, 27 + i * 6, 36, 2.5, "#7a6e5c") for i in range(5))
    return out


def corkboard(w=170, h=100, string=True):
    out = rect(-6, -6, w + 12, h + 12, "#6e4a2e", 3) + rect(0, 0, w, h, "#c79a5c")
    spots = [(20, 18), (80, 12), (130, 30), (40, 60), (110, 70), (150, 80)]
    for i, (x, y) in enumerate(spots):
        out += rect(x - 14, y - 6, 30, 22, ["#fbf6e8", "#f3e7c4", "#e8eef3"][i % 3], 1, f'transform="rotate({(-1)**i*6} {x} {y})"')
    if string:
        out += path("M20 18 L80 12 L130 30 L110 70 L40 60 Z", stroke="#c0392b", sw=1.5)
    out += "".join(circ(x, y, 3.5, "#c0392b") for x, y in spots)
    return out


def wallmap(w=170, h=100, kind="river"):
    out = rect(-6, -6, w + 12, h + 12, "#5c3b22", 3) + rect(0, 0, w, h, "#efe4c4")
    if kind == "river":
        out += path(f"M0 {h*.7} Q{w*.3} {h*.5} {w*.5} {h*.62} T{w} {h*.4}", stroke="#3f7f9a", sw=7)
        out += path(f"M{w*.35} 0 Q{w*.4} {h*.3} {w*.38} {h*.55}", stroke="#3f7f9a", sw=4) + path(f"M{w*.7} 0 Q{w*.62} {h*.25} {w*.66} {h*.5}", stroke="#3f7f9a", sw=4)
        out += "".join(path(f"M{x} {y} l6 -3 l-2 6 z", fill="#c0392b") for x, y in [(w * .52, h * .6), (w * .37, h * .3)])
    elif kind == "grid":
        out += path(f"M{w*.1} {h*.8} Q{w*.4} {h*.6} {w*.9} {h*.75}", stroke="#3f7f9a", sw=5)
        out += "".join(f'<line x1="{x}" y1="0" x2="{x}" y2="{h}" stroke="#b9a982" stroke-width="1"/>' for x in range(0, int(w), 20))
        out += "".join(f'<line x1="0" y1="{y}" x2="{w}" y2="{y}" stroke="#b9a982" stroke-width="1"/>' for y in range(0, int(h), 20))
        out += "".join(circ(x, y, 9, "none", 'stroke="#c0392b" stroke-width="2"') for x, y in [(w * .3, h * .35), (w * .55, h * .45), (w * .42, h * .2)])
        out += "".join(path(f"M{x} {y} l4 -9 l4 9 z", fill="#4f6b4a") for x, y in [(30, 30), (60, 50), (90, 25), (120, 40), (140, 20), (50, 80)])
    elif kind == "route":
        out += path(f"M{w*.1} {h*.25} L{w*.4} {h*.35} L{w*.55} {h*.6} L{w*.9} {h*.7}", stroke="#c0392b", sw=3, extra='stroke-dasharray="6 4"')
        out += "".join(circ(x, y, 5, "#c0392b") for x, y in [(w * .1, h * .25), (w * .4, h * .35), (w * .55, h * .6), (w * .9, h * .7)])
        out += rect(0, h * .82, w, h * .18, "#9cc3d5")
    elif kind == "tower":
        out += rect(w * .1, h * .1, w * .8, h * .8, "none", 0, 'stroke="#7a6a4a" stroke-width="3"')
        out += rect(w * .38, h * .32, w * .24, h * .34, "#d9cdb0", 0, 'stroke="#7a6a4a" stroke-width="2"')
        out += "".join(circ(x, y, 7, "#d9cdb0", 'stroke="#7a6a4a" stroke-width="2"') for x, y in [(w * .1, h * .1), (w * .9, h * .1), (w * .1, h * .9), (w * .9, h * .9)])
    elif kind == "weather":
        out += path(f"M{w*.1} {h*.2} Q{w*.5} {h*.1} {w*.9} {h*.3} Q{w*.6} {h*.55} {w*.1} {h*.2}", fill="#9fb3c4")
        out += path(f"M{w*.15} {h*.85} L{w*.85} {h*.35}", stroke="#2f5d8a", sw=3, extra='stroke-dasharray="5 4"')
        out += "".join(f'<line x1="{x}" y1="{y}" x2="{x-4}" y2="{y+9}" stroke="#2f5d8a" stroke-width="2"/>' for x, y in [(50, 40), (70, 46), (90, 40), (110, 48), (130, 42)])
        out += text(w * .5, h * .95, "NOV 24 1971", 9, "#5c4a36")
    return out


def envelope(c="#f3ecd9"):
    return rect(0, 0, 80, 50, c, 2, 'stroke="#bcae8e"') + path("M0 0 L40 28 L80 0", stroke="#bcae8e", sw=2) + rect(56, 6, 16, 18, "#c0563b", 1)


def letter(lines=6):
    return rect(0, 0, 60, 76, "#fbf6e8", 1, 'stroke="#cdbf9f"') + "".join(rect(8, 10 + i * 9, 44 - (i * 13) % 18, 2.5, "#4a4a4a") for i in range(lines))


def badge_star(c="#d4af37"):
    pts = []
    import math
    for i in range(10):
        r = 26 if i % 2 == 0 else 12
        a = math.pi / 2 + i * math.pi / 5
        pts.append(f"{r*math.cos(a):.1f} {-r*math.sin(a):.1f}")
    return path("M" + " L".join(pts) + " Z", fill=c, extra='stroke="#8a6d1c" stroke-width="2"') + circ(0, 0, 8, "#e9cf6a", 'stroke="#8a6d1c" stroke-width="1.5"')


def scales(c="#b8860b"):
    return (rect(-4, 0, 8, 80, c) + rect(-24, 80, 48, 8, c, 2) + path("M-50 6 L50 6", stroke=c, sw=5)
            + path("M-50 6 L-64 40 M-50 6 L-36 40 M50 6 L36 34 M50 6 L64 34", stroke=c, sw=1.5)
            + path("M-68 40 Q-50 54 -32 40 Z", fill=c) + path("M32 34 Q50 48 68 34 Z", fill=c) + circ(0, 2, 6, c))


def money(n=3):
    out = ""
    for i in range(n):
        out += rect(i * 14, -i * 8, 54, 26, "#86a374", 2, 'stroke="#4f6b3a" stroke-width="1.5"') + rect(i * 14 + 20, -i * 8, 8, 26, "#d9c27a")
    return out


def parachute(c1="#e8eef3", c2="#c0392b"):
    out = path("M-60 0 Q0 -60 60 0 Z", fill=c1)
    out += "".join(path(f"M{x} 0 Q{x*0.6} -40 {x*0.2} -48", stroke=c2, sw=2) for x in (-40, -20, 0, 20, 40))
    out += path("M-60 0 L-6 58 M60 0 L6 58 M-20 0 L-3 58 M20 0 L3 58", stroke="#6b5d4f", sw=1)
    out += rect(-8, 56, 16, 20, "#5a4a3a", 3)
    return out


def jet(c="#c9d3dd", lights=True):
    out = path("M0 20 C8 12 30 10 60 10 L200 10 C214 10 222 14 228 20 C222 26 214 30 200 30 L60 30 C30 30 8 28 0 20 Z", fill=c)
    out += path("M180 10 L200 -18 L216 -18 L210 10 Z", fill="#aab6c2") + path("M100 20 L146 54 L162 54 L134 20 Z", fill="#aab6c2")
    out += path("M196 30 L212 52 L216 50 L204 30 Z", fill="#7d8996")
    if lights:
        out += "".join(rect(40 + i * 12, 16, 5, 5, "#ffe9a8", 1) for i in range(9))
    return out


def fighter(c="#8e9aa7"):
    return path("M0 10 L70 6 L90 10 L70 14 Z", fill=c) + path("M34 10 L52 -10 L60 -10 L50 10 Z", fill="#6f7b88") + path("M34 10 L52 30 L60 30 L50 10 Z", fill="#6f7b88") + path("M70 6 L80 -4 L86 -4 L82 8 Z", fill="#6f7b88")


def truck_lift(c="#f2f2ee"):
    out = rect(0, 0, 150, 40, c, 4) + rect(150, 10, 46, 30, c, 4) + rect(160, 14, 26, 14, "#8fb6d0", 2)
    out += circ(30, 44, 11, "#2a2a2a") + circ(170, 44, 11, "#2a2a2a") + circ(30, 44, 4, "#aaa") + circ(170, 44, 4, "#aaa")
    out += path("M30 0 L210 -110", stroke="#d9663a", sw=9) + path("M30 0 L210 -110", stroke="#f0a070", sw=3)
    out += rect(196, -128, 34, 22, "#5a5a5a", 2)
    return out


def scooter(c="#c0392b"):
    return (circ(0, 30, 12, "#2a2a2a") + circ(70, 30, 12, "#2a2a2a") + circ(0, 30, 4, "#aaa") + circ(70, 30, 4, "#aaa")
            + path("M0 30 L20 14 L56 14 L70 30 Z", fill=c) + path("M56 14 L66 -12", stroke="#3a3a3a", sw=4) + path("M58 -14 L74 -10", stroke="#3a3a3a", sw=4)
            + rect(18, 4, 30, 10, "#2a2a2a", 4))


def crown(c="#d4af37"):
    out = path("M0 40 L4 8 L20 24 L36 0 L52 24 L68 8 L72 40 Z", fill=c, extra='stroke="#8a6d1c" stroke-width="2"') + rect(-2, 40, 76, 10, c, 2, 'stroke="#8a6d1c" stroke-width="2"')
    out += "".join(circ(x, 45, 3.5, col) for x, col in [(12, "#2f8a5a"), (36, "#2f5fa8"), (60, "#2f8a5a")]) + "".join(circ(x, y, 3, "#fff") for x, y in [(4, 8), (36, 0), (68, 8)])
    return out


def necklace(stone="#2f5fa8"):
    out = path("M0 0 Q40 50 80 0", stroke="#d4af37", sw=3)
    out += "".join(circ(x, y, 5, stone, 'stroke="#d4af37" stroke-width="1.5"') for x, y in [(14, 18), (26, 28), (40, 32), (54, 28), (66, 18)])
    out += path("M40 36 L33 48 L40 60 L47 48 Z", fill=stone, extra='stroke="#d4af37" stroke-width="1.5"')
    return out


def tiara(stone="#ffffff"):
    return path("M0 30 Q40 -10 80 30", stroke="#d4af37", sw=5) + "".join(circ(x, y, 4, stone, 'stroke="#c9b37a"') for x, y in [(12, 18), (26, 8), (40, 4), (54, 8), (68, 18)]) + path("M34 10 L40 -8 L46 10 Z", fill=stone)


def displaycase(empty=True):
    out = rect(0, 30, 90, 40, "#6e4a2e", 2) + rect(4, 0, 82, 32, "#d7eef5", 2, 'opacity=".6" stroke="#9fb5bb" stroke-width="2"')
    if empty:
        out += path("M20 6 L34 22 L26 28", stroke="#9fb5bb", sw=1.5) + path("M60 4 L52 18 L66 26", stroke="#9fb5bb", sw=1.5)
    return out


def cellbars(w=150, h=120, c="#5d6670"):
    out = rect(0, 0, w, 8, c) + rect(0, h - 8, w, 8, c)
    out += "".join(rect(x, 0, 5, h, c) for x in range(6, int(w), 16))
    return out


def cot(c="#6e7a84"):
    return rect(0, 0, 110, 12, "#d9d2c4", 3) + rect(0, 12, 110, 6, c) + rect(4, 18, 6, 22, c) + rect(100, 18, 6, 22, c) + path("M6 2 Q14 -10 30 -2 Q22 6 6 2 Z", fill="#c9b37a") + circ(18, -4, 7, "#d9b08c")


def sink():
    return path("M0 0 L40 0 L36 18 L4 18 Z", fill="#e8e6e0", extra='stroke="#9a9890" stroke-width="2"') + rect(16, -12, 4, 12, "#9a9890") + rect(16, -12, 12, 3, "#9a9890")


def vent(broken=True):
    out = rect(0, 0, 36, 26, "#7a7f84", 2) + "".join(rect(4, 4 + i * 5, 28, 2.5, "#4a4f54") for i in range(4))
    if broken:
        out += path("M0 26 L6 18 L14 26 Z", fill="#3a3a3a") + path("M30 0 L36 8 L36 0 Z", fill="#3a3a3a")
    return out


def ladder(h=120, c="#8a6a4a"):
    return rect(0, 0, 6, h, c) + rect(36, 0, 6, h, c) + "".join(rect(0, y, 42, 5, c) for y in range(12, h, 20))


def toolbox():
    return rect(0, 10, 70, 30, "#c0392b", 3) + path("M20 10 Q35 -6 50 10", stroke="#7a1f19", sw=5) + rect(0, 20, 70, 4, "#7a1f19")


def raft(c="#e0b33a"):
    return path("M0 20 Q60 40 120 20 L114 6 Q60 22 6 6 Z", fill=c, extra='stroke="#9a7514" stroke-width="2"') + "".join(path(f"M{x} 8 L{x} 28", stroke="#9a7514", sw=1.2) for x in range(16, 110, 14))


def paddle(c="#8a6a4a"):
    return rect(0, 0, 5, 70, c) + path("M-6 70 L11 70 L9 96 L-4 96 Z", fill=c)


def lifevest(c="#e8762e"):
    return path("M0 0 L14 -6 L20 6 L30 6 L36 -6 L50 0 L48 50 L2 50 Z", fill=c, extra='stroke="#9a4614" stroke-width="2"') + rect(20, 8, 10, 40, "#d9663a") + "".join(rect(4, 18 + i * 12, 42, 3, "#3a3a3a") for i in range(2))


def pine(h=60, c="#3f6a46"):
    return path(f"M0 0 L{h*.35} {h*.55} L{h*.2} {h*.55} L{h*.45} {h} L{-h*.45} {h} L{-h*.2} {h*.55} L{-h*.35} {h*.55} Z", fill=c) + rect(-4, h, 8, 10, "#5c3b22")


def rocks(c="#6e6258"):
    return path("M0 30 Q10 0 30 6 Q44 -4 60 12 Q74 4 84 30 Z", fill=c) + path("M20 30 Q30 14 44 18 Q54 12 62 30 Z", fill="#857a70")


def cloud(c="#c9d3dd", rain=False):
    out = path("M0 30 Q-4 10 18 12 Q22 -6 44 2 Q62 -8 72 12 Q92 12 88 30 Z", fill=c)
    if rain:
        out += "".join(f'<line x1="{x}" y1="36" x2="{x-6}" y2="54" stroke="#6f9fc4" stroke-width="2.5" stroke-linecap="round"/>' for x in (14, 32, 50, 68))
    return out


def accordion(c="#a3231d"):
    out = rect(0, 0, 22, 54, c, 3) + rect(62, 0, 22, 54, c, 3)
    out += "".join(path(f"M{22+i*8} 0 L{26+i*8} 27 L{22+i*8} 54", stroke="#3a3a3a", sw=2) for i in range(6))
    out += "".join(circ(70 + (i % 2) * 6, 10 + i * 7, 2, "#f3ead2") for i in range(6))
    return out


def tower_castle(c="#d9cdb0"):
    out = rect(0, 30, 120, 90, c) + "".join(rect(x, 22, 12, 10, c) for x in range(0, 120, 20))
    for x in (-6, 106):
        out += rect(x, 0, 20, 120, "#cdbf9f") + path(f"M{x-2} 0 L{x+10} -18 L{x+22} 0 Z", fill="#7a5c4a")
    out += "".join(rect(x, y, 8, 14, "#5c4a36", 3) for x, y in [(26, 60), (56, 60), (86, 60), (26, 92), (86, 92)]) + path("M48 120 L48 96 Q60 84 72 96 L72 120 Z", fill="#5c4a36")
    return out


def scroll(c="#f3e7c4"):
    return (rect(10, 0, 70, 86, c) + rect(0, -6, 90, 12, "#d9c58f", 6) + rect(0, 82, 90, 12, "#d9c58f", 6)
            + "".join(rect(18, 12 + i * 9, 50 - (i * 7) % 20, 2.5, "#6b5d4f") for i in range(7)) + circ(66, 72, 7, "#a3231d"))


def openbook(c="#fbf6e8"):
    return (path("M0 6 Q30 -4 60 6 L60 56 Q30 46 0 56 Z", fill=c, extra='stroke="#9c8f7a" stroke-width="1.5"')
            + path("M60 6 Q90 -4 120 6 L120 56 Q90 46 60 56 Z", fill=c, extra='stroke="#9c8f7a" stroke-width="1.5"')
            + "".join(rect(8, 12 + i * 7, 44, 2, "#8a7f72") + rect(68, 12 + i * 7, 44, 2, "#8a7f72") for i in range(5)) + rect(-4, 54, 128, 6, "#7a2a22", 2))


def urn(c="#e8e2d0"):
    return path("M10 0 L50 0 L46 8 Q62 30 48 60 L12 60 Q-2 30 14 8 Z", fill=c, extra='stroke="#9c9480" stroke-width="2"') + rect(6, 60, 48, 8, "#9c9480", 2) + rect(14, -8, 32, 8, "#9c9480", 2)


def postcards():
    out = rect(0, 0, 8, 100, "#7a7a7a") + rect(-30, 100, 68, 6, "#7a7a7a")
    pal = ["#2f5d8a", "#c0563b", "#6f8f4a", "#b8860b", "#6b4fa0", "#a3231d"]
    for i in range(6):
        out += rect(-30 + (i % 2) * 38, 6 + (i // 2) * 30, 30, 24, pal[i], 2) + rect(-26 + (i % 2) * 38, 10 + (i // 2) * 30, 22, 8, "#fbf6e8", 1, 'opacity=".6"')
    return out


def ghostflyer():
    return rect(0, 0, 50, 64, "#2a2440", 2) + path("M14 50 L14 26 Q25 8 36 26 L36 50 L31 45 L25 50 L19 45 Z", fill="#e8e6f2") + circ(21, 28, 2, "#2a2440") + circ(29, 28, 2, "#2a2440")


def cafetable():
    out = rect(-50, 0, 100, 8, "#8a5a35", 3) + rect(-4, 8, 8, 40, "#5c3b22") + rect(-22, 46, 44, 5, "#5c3b22", 2)
    out += path("M-34 0 L-30 -16 L-20 -16 L-16 0 Z", fill="#f3ead2") + path("M14 0 L16 -30 L22 -38 L28 -30 L30 0 Z", fill="#2f6b3a")
    return out


def easel():
    return path("M0 0 L-20 90 M0 0 L20 90 M0 0 L0 90", stroke="#8a6a4a", sw=4) + rect(-30, 10, 60, 46, "#f3ead2", 1) + path("M-24 46 Q-6 20 10 36 T26 26", stroke="#2f5d8a", sw=4) + circ(14, 22, 5, "#e8762e")


def person(shirt="#2f5d8a", skin="#d9a77c", hair="#3a2a1a", hat=None, pants="#3a3a46", scale_body=1.0):
    out = rect(-12, 40, 10, 34, pants, 3) + rect(2, 40, 10, 34, pants, 3)
    out += path("M-18 44 L-16 10 Q0 2 16 10 L18 44 Z", fill=shirt)
    out += rect(-24, 12, 7, 28, shirt, 3) + rect(17, 12, 7, 28, shirt, 3) + circ(-20, 41, 4, skin) + circ(20, 41, 4, skin)
    out += circ(0, -6, 12, skin) + path("M-12 -8 Q0 -24 12 -8 Q8 -14 0 -14 Q-8 -14 -12 -8 Z", fill=hair)
    if hat == "police":
        out += path("M-14 -12 L14 -12 L12 -22 L-12 -22 Z", fill="#1f2a44") + rect(-16, -13, 32, 4, "#111", 2) + circ(0, -17, 2.5, "#d4af37")
    elif hat == "beret":
        out += path("M-14 -12 Q0 -26 16 -14 Z", fill="#1f1f1f")
    elif hat == "cap":
        out += path("M-12 -12 Q0 -24 12 -12 Z", fill="#c0392b") + rect(4, -14, 14, 4, "#c0392b", 2)
    elif hat == "bowler":
        out += path("M-11 -13 Q0 -30 11 -13 Z", fill="#1f1f1f") + rect(-15, -14, 30, 4, "#1f1f1f", 2)
    return out


def streetlight():
    return rect(-3, 0, 6, 120, "#3a3a3a") + path("M0 0 Q0 -10 24 -10", stroke="#3a3a3a", sw=5) + path("M16 -10 L32 -10 L28 0 L20 0 Z", fill="#3a3a3a") + path("M20 0 L28 0 L44 60 L4 60 Z", fill="#fff3b0", extra='opacity=".25"')


def policecar():
    out = path("M0 30 L10 12 L40 4 L110 4 L136 14 L150 30 Z", fill="#e8e6e0") + rect(0, 30, 150, 16, "#1f2a44", 3)
    out += rect(46, 8, 26, 12, "#9fc3e6", 2) + rect(78, 8, 30, 12, "#9fc3e6", 2) + rect(64, -4, 22, 8, "#c0392b", 2) + rect(74, -4, 12, 8, "#2f5fa8", 2)
    out += circ(32, 46, 11, "#1a1a1a") + circ(118, 46, 11, "#1a1a1a") + circ(32, 46, 4, "#999") + circ(118, 46, 4, "#999")
    return out


def oldcar(c="#6f8fa8"):
    out = path("M0 28 Q4 14 24 12 L44 0 L104 0 L124 12 Q146 14 150 28 Z", fill=c) + rect(0, 26, 150, 14, c, 6)
    out += rect(50, 3, 24, 10, "#cfe3ef", 2) + rect(78, 3, 22, 10, "#cfe3ef", 2) + circ(32, 40, 11, "#1a1a1a") + circ(118, 40, 11, "#1a1a1a") + circ(32, 40, 4, "#ccc") + circ(118, 40, 4, "#ccc")
    return out


def shed(c="#8a6a4a"):
    return (path("M0 30 L50 0 L100 30 Z", fill="#5c3b22") + rect(6, 30, 88, 60, c) + "".join(rect(x, 30, 2, 60, "#6e5238") for x in range(14, 94, 12))
            + rect(36, 50, 26, 40, "#3d2716"))


def hole():
    return path("M0 10 Q40 -6 80 10 Q40 26 0 10 Z", fill="#2a1f16") + path("M4 10 Q40 -2 76 10", stroke="#6e5238", sw=3)


def crates(n=3):
    out = ""
    for i in range(n):
        x, y = (i % 2) * 52 + (i // 2) * 26, -(i // 2) * 44
        out += rect(x, y, 48, 42, "#b08d58", 2, 'stroke="#7a5c34" stroke-width="2"') + path(f"M{x} {y} L{x+48} {y+42} M{x+48} {y} L{x} {y+42}", stroke="#7a5c34", sw=2)
    return out


def brick(w=W, h=FLOOR, c="#8a4a3a", m="#6e3a2e"):
    out = rect(0, 0, w, h, c)
    for r, y in enumerate(range(0, h, 16)):
        out += f'<line x1="0" y1="{y}" x2="{w}" y2="{y}" stroke="{m}" stroke-width="2"/>'
        out += "".join(f'<line x1="{x}" y1="{y}" x2="{x}" y2="{y+16}" stroke="{m}" stroke-width="2"/>' for x in range((r % 2) * 20, w, 40))
    return out


def beam(x1, y1, x2a, x2b, y2, c="#fff6c0", op=".35"):
    return path(f"M{x1} {y1} L{x2a} {y2} L{x2b} {y2} Z", fill=c, extra=f'opacity="{op}"')


def mic():
    return rect(-4, 20, 8, 50, "#4a4a4a") + rect(-16, 68, 32, 6, "#4a4a4a", 2) + rect(-12, -10, 24, 34, "#2a2a2a", 12) + "".join(rect(-10, -4 + i * 6, 20, 2, "#555") for i in range(4))


def onair():
    return rect(0, 0, 90, 30, "#2a1a1a", 4) + text(45, 21, "ON AIR", 16, "#ff5a4a")


def tvcam():
    return (rect(0, 0, 70, 40, "#3a3f46", 4) + circ(76, 20, 12, "#1f2328") + circ(76, 20, 6, "#4a7fa8")
            + path("M35 40 L15 100 M35 40 L55 100 M35 40 L35 100", stroke="#2a2a2a", sw=4) + rect(8, -8, 14, 8, "#c0392b", 2))


def sofa(c="#2f5d8a"):
    return rect(0, 20, 120, 30, c, 6) + rect(0, 0, 120, 26, c, 8, 'opacity=".85"') + rect(-8, 14, 16, 36, c, 6) + rect(112, 14, 16, 36, c, 6)


def clapper():
    return rect(0, 14, 70, 46, "#2a2a2a", 3) + path("M0 14 L70 2 L70 12 L0 24 Z", fill="#f3ead2") + "".join(path(f"M{x} {14-x*0.17} L{x+8} {12-x*0.17-2} L{x+12} {22-x*0.17} L{x+4} {24-x*0.17}", fill="#2a2a2a") for x in (6, 26, 46)) + text(35, 46, "TAKE 1", 10, "#f3ead2")


def filmreel():
    return circ(0, 0, 26, "#3a3a3a") + "".join(circ(x, y, 7, "#cfc7b2") for x, y in [(0, -14), (12, 7), (-12, 7)]) + circ(0, 0, 4, "#cfc7b2")


def binoculars():
    return rect(0, 0, 22, 34, "#2a2a2a", 8) + rect(28, 0, 22, 34, "#2a2a2a", 8) + rect(18, 8, 14, 10, "#3a3a3a") + circ(11, 30, 7, "#4a7fa8") + circ(39, 30, 7, "#4a7fa8")


def dna(c1="#2f5fa8", c2="#c0392b"):
    out = path("M0 0 Q20 20 0 40 Q-20 60 0 80", stroke=c1, sw=4) + path("M0 0 Q-20 20 0 40 Q20 60 0 80", stroke=c2, sw=4)
    out += "".join(f'<line x1="-12" y1="{y}" x2="12" y2="{y}" stroke="#8a8a8a" stroke-width="2"/>' for y in (10, 30, 50, 70))
    return out


def poster13():
    out = rect(0, 0, 120, 96, "#fbf6e8", 2, 'stroke="#a3231d" stroke-width="3"') + text(60, 16, "REWARD", 13, "#a3231d")
    for i in range(13):
        x, y = 8 + (i % 5) * 21, 24 + (i // 5) * 22
        out += rect(x, y, 18, 18, "#c9a14a", 1) + rect(x + 3, y + 3, 12, 12, ["#46607a", "#6f7a4a", "#3b3326", "#8a6a4a"][i % 4])
    return out


def sketches():
    out = ""
    for k in range(2):
        x = k * 70
        out += rect(x, 0, 62, 80, "#fbf6e8", 1, 'stroke="#cdbf9f"') + circ(x + 31, 34, 14, "none", 'stroke="#5a5a5a" stroke-width="1.5"')
        out += path(f"M{x+15} 26 L{x+47} 26 L{x+44} 16 L{x+18} 16 Z", fill="#5a5a5a") + path(f"M{x+12} 76 Q{x+31} 48 {x+50} 76", stroke="#5a5a5a", sw=1.5)
        out += path(f"M{x+24} 42 Q{x+31} 46 {x+38} 42", stroke="#5a5a5a", sw=1.2)
    return out


def instrument_panel():
    out = rect(0, 0, 200, 60, "#2a2f36", 6)
    out += "".join(circ(24 + i * 38, 22, 13, "#0d1b24", 'stroke="#8a9aa8" stroke-width="2"') + path(f"M{24+i*38} 22 L{30+i*38} {14+i%3*3}", stroke="#ffd25e", sw=2) for i in range(5))
    out += "".join(rect(14 + i * 22, 44, 14, 8, ["#c0392b", "#2f8a5a", "#ffd25e"][i % 3], 2) for i in range(8))
    return out


def seats(n=3, c="#3d6b8f"):
    return "".join(rect(i * 46, 0, 40, 34, c, 6) + rect(i * 46, 30, 40, 14, c, 4, 'opacity=".8"') + rect(i * 46 + 4, 4, 32, 8, "#e8eef3", 2) for i in range(n))


def counter(c="#7a5234", sign=None):
    out = rect(0, 0, 200, 50, c, 2) + rect(-4, -6, 208, 8, "#5c3b22", 2)
    if sign:
        out += rect(40, -70, 120, 30, "#1f2a44", 3) + text(100, -50, sign, 13, "#ffd25e")
    return out


def suitcase(c="#8a4a3a"):
    return rect(0, 0, 50, 36, c, 4) + path("M16 0 Q25 -10 34 0", stroke="#3a2a1a", sw=4) + rect(0, 16, 50, 3, "#3a2a1a")


def layers():
    out = ""
    pal = ["#e3c98f", "#c7a663", "#9c7f4a", "#d4b676", "#7a6448"]
    for i, c in enumerate(pal):
        out += path(f"M0 {i*16} Q60 {i*16-6} 120 {i*16+4} L120 {i*16+16} Q60 {i*16+12} 0 {i*16+16} Z", fill=c)
    return out + rect(0, 0, 3, 80, "#5c3b22") + path("M30 34 L52 30", stroke="#c0392b", sw=3)


def shovel():
    return rect(0, 0, 5, 70, "#8a6a4a") + path("M-8 70 L13 70 L10 96 Q2 104 -5 96 Z", fill="#8a8a8a")


def campfire():
    return path("M-22 18 L22 18", stroke="#6b4a2b", sw=5) + path("M0 -26 C10 -12 14 -4 8 8 C4 14 -4 14 -8 8 C-14 -2 -8 -14 0 -26 Z", fill="#e8742a") + path("M0 -10 C5 -3 6 2 3 7 C1 10 -2 10 -4 7 C-6 2 -4 -4 0 -10 Z", fill="#ffd25e")


def bills_in_sand():
    return path("M-10 18 Q40 6 90 18 Z", fill="#c7a663") + rect(0, 4, 26, 12, "#86a374", 2, 'transform="rotate(-8)"') + rect(30, 6, 26, 12, "#6f8c5c", 2) + rect(58, 2, 26, 12, "#86a374", 2, 'transform="rotate(5 70 8)"')


def stamp_text(s, c="#a3231d", size=16):
    w = len(s) * size * 0.68 + 16
    return rect(-w / 2, -size, w, size * 1.5, "none", 3, f'stroke="{c}" stroke-width="3"') + text(0, size * .2, s, size, c)


def flag_case():
    return rect(0, 20, 100, 30, "#6e4a2e", 2) + rect(4, 0, 92, 22, "#d7eef5", 2, 'opacity=".7" stroke="#9fb5bb" stroke-width="2"') + rect(10, 4, 70, 14, "#c9b37a", 1) + path("M10 4 L80 4 L80 18 L10 18", stroke="#a3231d", sw=1.5) + circ(92, 4, 5, "#b8860b") + path("M86 -6 L98 -6 L92 -16 Z", fill="#b8860b")


def glass_shards():
    return "".join(path(f"M{x} {y} l{a} -{b} l{b} {a} z", fill="#d7eef5", extra='stroke="#9fb5bb" stroke-width="1" opacity=".9"') for x, y, a, b in [(0, 0, 8, 12), (30, 4, 10, 6), (60, -2, 6, 10), (90, 6, 12, 8), (120, 0, 7, 9)])


def tophat_empty():
    return rect(0, 0, 70, 54, "#e8e2d0", 2, 'stroke="#c9a14a" stroke-width="5" stroke-dasharray="6 5"') + text(35, 34, "?", 24, "#9c8f7a")


def clock():
    return circ(0, 0, 22, "#fbf6e8", 'stroke="#5c3b22" stroke-width="4"') + path("M0 0 L0 -14 M0 0 L10 4", stroke="#2a2420", sw=2.5)


def sign(s, w=120, bg="#1f2a44", fg="#fbf6e8", size=13):
    return rect(-w / 2, -14, w, 26, bg, 3) + text(0, 4, s, size, fg)
