"""Original illustrations and per-case color themes for the Cold Case Academy games.
Run: python3 art.py  (rewrites the Banner/Scene/Theme passages in each game's .twee and adds map icons)."""
import re, pathlib

G = pathlib.Path(__file__).parent

SVG_OPEN = '<svg class="art" viewBox="0 0 640 220" role="img" aria-label="{label}" preserveAspectRatio="xMidYMid slice">'

FLIGHT_BANNER = SVG_OPEN.format(label="A jet airliner flies through a stormy night sky, its back stairs lowered under the tail.") + '''
<defs><linearGradient id="sky1" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0d1b2e"/><stop offset="1" stop-color="#2c4a6e"/></linearGradient></defs>
<rect width="640" height="220" fill="url(#sky1)"/>
<g fill="#ffffff" opacity=".8"><circle cx="40" cy="30" r="1.5"/><circle cx="120" cy="18" r="1"/><circle cx="210" cy="42" r="1.3"/><circle cx="300" cy="14" r="1"/><circle cx="560" cy="24" r="1.4"/><circle cx="610" cy="60" r="1"/><circle cx="470" cy="12" r="1"/></g>
<circle cx="560" cy="58" r="22" fill="#f3ead2"/><circle cx="570" cy="52" r="20" fill="#1a2d47"/>
<g fill="#6f8aa8" opacity=".55"><ellipse cx="120" cy="190" rx="160" ry="34"/><ellipse cx="380" cy="205" rx="200" ry="32"/><ellipse cx="600" cy="185" rx="120" ry="30"/></g>
<g transform="translate(150 70)">
<path d="M0 40 C10 30 40 26 80 26 L300 26 C318 26 330 32 340 40 C330 48 318 52 300 52 L80 52 C40 52 10 50 0 40 Z" fill="#c9d3dd"/>
<path d="M270 26 L300 -14 L322 -14 L312 26 Z" fill="#aab6c2"/>
<rect x="282" y="16" width="34" height="12" rx="6" fill="#8e9aa7"/>
<path d="M150 40 L215 92 L238 92 L196 40 Z" fill="#aab6c2"/>
<path d="M150 38 L200 6 L218 6 L194 38 Z" fill="#9aa6b3"/>
<g fill="#ffe9a8"><rect x="60" y="34" width="6" height="6" rx="1"/><rect x="76" y="34" width="6" height="6" rx="1"/><rect x="92" y="34" width="6" height="6" rx="1"/><rect x="108" y="34" width="6" height="6" rx="1"/><rect x="124" y="34" width="6" height="6" rx="1"/><rect x="230" y="34" width="6" height="6" rx="1"/><rect x="246" y="34" width="6" height="6" rx="1"/></g>
<path d="M296 52 L318 88 L324 86 L306 52 Z" fill="#7d8996"/>
<g stroke="#5c6875" stroke-width="2"><line x1="300" y1="60" x2="309" y2="58"/><line x1="304" y1="67" x2="313" y2="65"/><line x1="308" y1="74" x2="317" y2="72"/><line x1="312" y1="81" x2="321" y2="79"/></g>
</g>
<g stroke="#9fc3e6" stroke-width="1.2" opacity=".5"><line x1="20" y1="80" x2="10" y2="100"/><line x1="90" y1="60" x2="80" y2="80"/><line x1="450" y1="140" x2="440" y2="160"/><line x1="520" y1="110" x2="510" y2="130"/><line x1="610" y1="140" x2="600" y2="160"/></g>
</svg>'''

TENA_BANNER = SVG_OPEN.format(label="A sandy riverbank at dusk, with a small campfire and three bundles of old bills half buried in the sand.") + '''
<defs><linearGradient id="sky2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f2c38b"/><stop offset="1" stop-color="#f7e2c0"/></linearGradient></defs>
<rect width="640" height="220" fill="url(#sky2)"/>
<g fill="#4f6b4a"><path d="M0 92 L30 50 L60 92 Z"/><path d="M40 96 L80 40 L120 96 Z"/><path d="M500 92 L540 36 L580 92 Z"/><path d="M560 96 L600 50 L640 96 Z"/><rect x="0" y="90" width="640" height="16"/></g>
<rect y="104" width="640" height="46" fill="#3f8c87"/>
<g stroke="#dff1ee" stroke-width="2" opacity=".6"><line x1="60" y1="118" x2="120" y2="118"/><line x1="220" y1="128" x2="300" y2="128"/><line x1="420" y1="116" x2="480" y2="116"/><line x1="530" y1="136" x2="600" y2="136"/></g>
<path d="M0 150 C120 138 260 146 360 142 C470 138 560 146 640 140 L640 220 L0 220 Z" fill="#e3c98f"/>
<path d="M0 182 C140 172 300 186 640 176 L640 220 L0 220 Z" fill="#d4b676"/>
<g transform="translate(150 168)"><path d="M-22 18 L22 18" stroke="#6b4a2b" stroke-width="5" stroke-linecap="round"/><path d="M-18 14 L18 22 M18 14 L-18 22" stroke="#6b4a2b" stroke-width="4"/><path d="M0 -26 C10 -12 14 -4 8 8 C4 14 -4 14 -8 8 C-14 -2 -8 -14 0 -26 Z" fill="#e8742a"/><path d="M0 -10 C5 -3 6 2 3 7 C1 10 -2 10 -4 7 C-6 2 -4 -4 0 -10 Z" fill="#ffd25e"/></g>
<g transform="translate(400 176)"><ellipse cx="40" cy="14" rx="70" ry="12" fill="#c7a663"/>
<g><rect x="0" y="0" width="34" height="16" rx="2" fill="#7e9b6a" transform="rotate(-8)"/><rect x="28" y="2" width="34" height="16" rx="2" fill="#6f8c5c" transform="rotate(5 45 10)"/><rect x="56" y="-2" width="34" height="16" rx="2" fill="#86a374" transform="rotate(-3 73 6)"/></g>
<g stroke="#b8862e" stroke-width="2.5"><line x1="14" y1="-2" x2="16" y2="16"/><line x1="44" y1="2" x2="44" y2="19"/><line x1="72" y1="-2" x2="73" y2="15"/></g></g>
</svg>'''

DAWN_BANNER = SVG_OPEN.format(label="Alcatraz Island at dawn: the cellhouse and lighthouse on a rocky island, with a searchlight beam over the cold bay.") + '''
<defs><linearGradient id="sky3" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3a4b66"/><stop offset=".55" stop-color="#e59a7a"/><stop offset="1" stop-color="#f6d3a3"/></linearGradient></defs>
<rect width="640" height="220" fill="url(#sky3)"/>
<path d="M370 96 L640 40 L640 70 Z" fill="#fff6c8" opacity=".35"/>
<rect y="150" width="640" height="70" fill="#4f6577"/>
<g stroke="#c9d6e0" stroke-width="2" opacity=".45"><line x1="30" y1="170" x2="90" y2="170"/><line x1="140" y1="190" x2="220" y2="190"/><line x1="470" y1="176" x2="540" y2="176"/><line x1="560" y1="200" x2="620" y2="200"/></g>
<path d="M150 152 C190 120 240 112 300 110 C380 108 440 118 490 152 Z" fill="#3c3530"/>
<rect x="230" y="84" width="150" height="34" fill="#5a524b"/>
<g fill="#ffd98a"><rect x="242" y="92" width="6" height="8"/><rect x="258" y="92" width="6" height="8"/><rect x="274" y="92" width="6" height="8"/><rect x="290" y="92" width="6" height="8"/><rect x="306" y="92" width="6" height="8"/><rect x="322" y="92" width="6" height="8"/><rect x="338" y="92" width="6" height="8"/><rect x="354" y="92" width="6" height="8"/></g>
<rect x="362" y="56" width="10" height="40" fill="#d9d2c4"/><path d="M358 56 L376 56 L367 46 Z" fill="#a3231d"/><circle cx="367" cy="62" r="4" fill="#fff6c8"/>
<rect x="200" y="104" width="34" height="18" fill="#4a433d"/><rect x="420" y="112" width="28" height="12" fill="#4a433d"/>
</svg>'''

MARSHALS_BANNER = SVG_OPEN.format(label="A deputy marshal's star badge on a desk beside an old case folder, with the Golden Gate Bridge in the window.") + '''
<defs><linearGradient id="sky4" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#9fc0d8"/><stop offset="1" stop-color="#e8d9bd"/></linearGradient></defs>
<rect width="640" height="220" fill="#5b4636"/>
<rect x="330" y="16" width="290" height="130" rx="4" fill="url(#sky4)" stroke="#3d2e23" stroke-width="8"/>
<rect x="330" y="112" width="290" height="34" fill="#5f87a3"/>
<g stroke="#c0392b" stroke-width="5" fill="none"><line x1="400" y1="40" x2="400" y2="120"/><line x1="550" y1="40" x2="550" y2="120"/><path d="M340 70 Q400 40 400 40 Q475 108 550 40 Q560 52 610 70"/><line x1="335" y1="96" x2="615" y2="96"/></g>
<path d="M455 124 C465 116 485 114 500 118 L505 126 L450 126 Z" fill="#4a433d"/>
<rect y="146" width="640" height="74" fill="#7a5a40"/>
<g transform="translate(40 120) rotate(-4)"><rect width="230" height="88" rx="4" fill="#d9b979"/><rect x="0" y="-10" width="90" height="16" rx="3" fill="#d9b979"/><rect x="18" y="18" width="190" height="22" fill="#fbf6e8"/><text x="26" y="34" font-family="Special Elite, Courier New, monospace" font-size="12" fill="#2a2420">MORRIS · ANGLIN · ANGLIN</text><text x="26" y="66" font-family="Special Elite, Courier New, monospace" font-size="13" fill="#a3231d">OPEN · 1962</text></g>
<g transform="translate(330 186)"><path d="M0 -34 L9 -12 L33 -12 L14 3 L21 26 L0 12 L-21 26 L-14 3 L-33 -12 L-9 -12 Z" fill="#d4a62a" stroke="#8a6a12" stroke-width="2"/><circle r="10" fill="#e8c35a" stroke="#8a6a12" stroke-width="1.5"/></g>
</svg>'''

SCENES = {
 "flight-305": ("Plane", '<svg class="art scene" viewBox="0 0 640 160" role="img" aria-label="The tail of the jet on the runway in Reno, its back stairs hanging down to the ground."><rect width="640" height="160" fill="#2c3e55"/><rect y="128" width="640" height="32" fill="#3b3b3b"/><g stroke="#e8d36a" stroke-width="4" stroke-dasharray="26 18"><line x1="0" y1="146" x2="640" y2="146"/></g><path d="M40 70 L420 70 C450 70 470 78 480 88 C470 98 450 104 420 104 L40 104 Z" fill="#c9d3dd"/><path d="M400 70 L440 10 L470 10 L456 70 Z" fill="#aab6c2"/><rect x="418" y="58" width="44" height="14" rx="7" fill="#8e9aa7"/><path d="M430 104 L478 128 L486 126 L446 104 Z" fill="#7d8996"/><g stroke="#5c6875" stroke-width="2"><line x1="440" y1="110" x2="452" y2="108"/><line x1="452" y1="116" x2="464" y2="114"/><line x1="464" y1="122" x2="476" y2="120"/></g><g fill="#ffe9a8"><rect x="80" y="80" width="8" height="8" rx="1"/><rect x="104" y="80" width="8" height="8" rx="1"/><rect x="128" y="80" width="8" height="8" rx="1"/><rect x="152" y="80" width="8" height="8" rx="1"/></g><circle cx="560" cy="40" r="6" fill="#e74c3c"/><circle cx="590" cy="40" r="6" fill="#3498db"/></svg>'),
 "tena-bar-riddle": ("Geologist", '<svg class="art scene" viewBox="0 0 640 170" role="img" aria-label="A cutaway of the beach like a layer cake: ordinary sand on top with the money in it, natural river sand below, then the gray clay from the 1974 dredge at the bottom."><rect width="640" height="170" fill="#f4ecd6"/><rect x="40" y="20" width="560" height="40" fill="#e3c98f"/><rect x="40" y="60" width="560" height="44" fill="#d2b77a"/><rect x="40" y="104" width="560" height="50" fill="#9a9a94"/><g fill="#7e9b6a"><rect x="300" y="32" width="30" height="12" rx="2"/><rect x="326" y="36" width="30" height="12" rx="2"/></g><g font-family="Atkinson Hyperlegible, sans-serif" font-size="14" fill="#2a2420"><text x="56" y="46">Beach sand (money found here)</text><text x="56" y="88">Natural river sand</text><text x="56" y="134" fill="#fff">Gray clay from the 1974 dredge</text></g><path d="M380 38 L470 38" stroke="#a3231d" stroke-width="2"/><text x="476" y="43" font-family="Atkinson Hyperlegible, sans-serif" font-size="13" fill="#a3231d">the money</text></svg>'),
 "count-at-dawn": ("Cells", '<svg class="art scene" viewBox="0 0 640 170" role="img" aria-label="Inside a narrow cell: a bed with a fake head on the pillow under a blanket, and a dark hole behind the sink."><rect width="640" height="170" fill="#bfb8aa"/><g stroke="#6b6458" stroke-width="6"><line x1="20" y1="0" x2="20" y2="170"/><line x1="60" y1="0" x2="60" y2="170"/><line x1="100" y1="0" x2="100" y2="170"/></g><rect y="140" width="640" height="30" fill="#8f877a"/><rect x="170" y="96" width="250" height="40" rx="4" fill="#6f7b86"/><rect x="170" y="88" width="250" height="16" rx="6" fill="#55626e"/><ellipse cx="200" cy="88" rx="26" ry="14" fill="#f2efe6"/><circle cx="214" cy="80" r="15" fill="#e5c8a8"/><path d="M200 70 C210 62 228 64 230 76 C224 72 212 72 204 76 Z" fill="#5a3b25"/><rect x="480" y="70" width="70" height="30" rx="4" fill="#e8e4da" stroke="#9a9384" stroke-width="2"/><rect x="510" y="56" width="6" height="16" fill="#9a9384"/><rect x="494" y="112" width="40" height="26" fill="#2a2420"/><g stroke="#7a7266" stroke-width="2"><line x1="494" y1="120" x2="534" y2="120"/><line x1="494" y1="128" x2="534" y2="128"/></g></svg>'),
 "marshals-file": ("Search", '<svg class="art scene" viewBox="0 0 640 160" role="img" aria-label="Evidence photos laid out on a table: a homemade wooden paddle, a life vest made of raincoat cloth, and a small packet wrapped in plastic."><rect width="640" height="160" fill="#8a6a4f"/><g transform="rotate(-3 160 80)"><rect x="40" y="20" width="200" height="120" fill="#fbf6e8"/><rect x="52" y="32" width="176" height="88" fill="#ddd3bf"/><path d="M70 76 L170 76 L210 62 L214 90 L170 84 L70 84 Z" fill="#8a5a33"/></g><g transform="rotate(2 330 80)"><rect x="230" y="18" width="190" height="124" fill="#fbf6e8"/><rect x="242" y="30" width="166" height="92" fill="#ddd3bf"/><path d="M290 40 L360 40 L372 110 L278 110 Z" fill="#4c4c4c"/><path d="M325 40 L325 110" stroke="#2a2420" stroke-width="3"/><g stroke="#c9b26b" stroke-width="3"><line x1="284" y1="62" x2="366" y2="62"/><line x1="282" y1="86" x2="368" y2="86"/></g></g><g transform="rotate(-2 520 80)"><rect x="430" y="24" width="180" height="116" fill="#fbf6e8"/><rect x="442" y="36" width="156" height="84" fill="#ddd3bf"/><rect x="480" y="56" width="80" height="44" rx="6" fill="#c9dbe6" stroke="#8fb0c4" stroke-width="3"/><rect x="494" y="66" width="52" height="24" fill="#f4ecd6"/></g></svg>'),
}

THEMES = {
 "flight-305": "#24496f",
 "tena-bar-riddle": "#2f7f79",
 "count-at-dawn": "#c0664a",
 "marshals-file": "#b8860b",
}

ICONS = {
 # Flight 305
 "Gate": "🎫", "Schaffner": "🗣️", "Mucklow": "🗣️", "Cockpit": "👨‍✈️", "Mitchell": "💺", "Plane": "✈️", "MoneyRoom": "💵", "Escort": "🛩️", "Newsroom": "📰",
 # Tena Bar
 "Beach": "🏖️", "Lab": "🔬", "Geologist": "🪨", "RiverMap": "🗺️", "Chutes": "🪂", "Weather": "🌧️", "Files": "🗂️",
 # Count at Dawn
 "Cells": "🛏️", "West": "🗣️", "Corridor": "🔦", "Roof": "🏚️", "Shore": "🌊", "Shops": "🧰", "Music": "🪗", "Guards": "📋", "Dock": "📰",
 # Marshals
 "Search": "🛶", "WestFile": "📄", "Bay": "⚓", "Memo": "📁", "Widner": "🗣️", "Roderick": "⭐", "Hut": "💻", "Tests": "🎬",
}

def themed_css(color):
    return f''':: CaseTheme [stylesheet]
:root {{ --accent: {color}; }}
#passages {{ border-top-color: var(--accent); }}
h1 {{ color: var(--accent); }}
.map a {{ border-left: 6px solid var(--accent); }}
.map .opt.revisit a {{ border-left-color: var(--line); }}
.actions a, .actions .macro-link {{ background: var(--accent); }}
.actions.secondary a, .actions.secondary .macro-link {{ background: transparent; color: var(--accent); border-color: var(--accent); }}
.headline {{ border-left: 6px solid var(--accent); }}
.card {{ border-top-color: var(--accent); }}
svg.art {{ display: block; width: 100%; height: auto; border-radius: 6px; margin: 0 0 16px; box-shadow: 0 2px 8px rgba(0,0,0,.25); }}
svg.art.scene {{ margin: 6px 0 14px; }}
'''

for game, banner in [("flight-305", FLIGHT_BANNER), ("tena-bar-riddle", TENA_BANNER), ("count-at-dawn", DAWN_BANNER), ("marshals-file", MARSHALS_BANNER)]:
    p = G / game / f"{game}.twee"
    s = p.read_text()
    # strip anything this script added before, so it can be re-run
    s = re.split(r"\n\n:: Banner \[art\]", s)[0].rstrip() + "\n"
    s = s.replace('<<include "Banner">>\n', "").replace('<<include "Scene">>\n', "")
    scene_passage, scene_svg = SCENES[game]
    # Banner on Start and CaseClosed
    s = re.sub(r'(:: Start \[nobar\]\n)', r'\1<<include "Banner">>\n', s, count=1)
    s = re.sub(r'(:: CaseClosed \[nobar\]\n)', r'\1<<include "Banner">>\n', s, count=1)
    # Scene under the heading of one location
    s = re.sub(r'(:: %s\n<h2>[^\n]*</h2>\n)' % scene_passage, r'\1<<include "Scene">>\n', s, count=1)
    # Map icons (idempotent: skip labels that already start with an icon)
    def icon(m):
        dest, label = m.group(1), m.group(2)
        ic = ICONS.get(dest)
        if not ic or label.startswith(ic): return m.group(0)
        return f'<<maplink "{dest}" "{ic} {label}">>'
    s = re.sub(r'<<maplink "([^"]+)" "([^"]+)">>', icon, s)
    s += "\n\n:: Banner [art]\n" + banner + "\n\n\n:: Scene [art]\n" + scene_svg + "\n\n\n" + themed_css(THEMES[game])
    p.write_text(s)
    print("updated", game)
