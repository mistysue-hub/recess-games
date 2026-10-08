"""One picture per map location, for all nine hub games. Run: python3 scenes.py
Writes places/<game>.places.twee (setup.placeArt) and a preview page places/preview.html."""
import json, pathlib, html
from kit import *

HERE = pathlib.Path(__file__).parent


def svg(key, label, body):
    return (f'<svg class="art placepic" viewBox="0 0 640 190" role="img" aria-label="{html.escape(label, quote=True)}" '
            f'preserveAspectRatio="xMidYMid slice">{body}</svg>')


S = {}  # game -> {passage: (color, label, body or None)}

# ---------------- M01 The Missing Smile (Paris, 1911) ----------------
S["the-missing-smile"] = {
 "Wall": ("#a3231d", None, None),
 "Stairwell": ("#7a5c3e", "A narrow back staircase behind a plain door, with an empty picture frame leaning against the wall.",
   room("#cbb48c", "#7a5c3e", "#5c4630") + at(70, 40, 1, door("#6e4a2e")) + at(190, 150, 1, stairs("#a8977c", 7))
   + at(470, 70, 1.1, painting(70, 56, "#c9a14a", "empty"), False) + at(560, 30, 1, window(50, 70, "sky")) + at(420, 140, .9, glass_shards())),
 "Staff": ("#6b5d4f", "A cramped museum office stacked with ledgers, a desk lamp glowing over a list of workers' names.",
   room("#d8c7a0", "#6e5238", "#4f3a28", wainscot="#b8a27a") + at(40, 30, .9, bookshelf(5, 3, 2)) + at(250, 100, 1.2, desk(220))
   + at(300, 82, 1, papers(5)) + at(420, 64, 1, lamp("#2f6b3a")) + at(360, 72, .9, letter()) + at(540, 40, 1, clock())),
 "Guards": ("#2f4a7a", "Three tired museum guards in blue uniforms standing in a side office.",
   room("#cfc2a3", "#6e5238", "#4f3a28") + at(60, 30, 1, window(110, 80, "sky")) + at(260, 76, 1, person("#2f4a7a", hat="police"))
   + at(330, 78, 1, person("#2f4a7a", hair="#777", hat="police")) + at(400, 76, 1, person("#2f4a7a", hair="#5a3a1a", hat="police")) + at(520, 100, .8, desk(110))),
 "Photographers": ("#5c3b22", "A studio under the roof, with big wooden cameras on tripods and glass plates drying on racks.",
   room("#d9cdb0", "#8a6a4a", "#5c4630") + at(60, 20, 1, window(140, 70, "sky")) + at(320, 70, 1.05, camera_tripod()) + at(470, 72, .9, camera_tripod(), True)
   + "".join(at(520 + i * 22, 40, 1, rect(0, 0, 16, 26, "#cfe3ef", 2, 'stroke="#7a7a7a"')) for i in range(4)) + rect(510, 64, 110, 4, "#5c3b22")),
 "Cafe": ("#b8860b", "A noisy Paris café with small round tables, an easel in the corner and people arguing about art.",
   room("#e3c48a", "#7a2f2a", "#5a1f1a", stripes="#d4b277") + at(80, 20, 1, window(110, 80, "sky")) + at(260, 104, 1, cafetable()) + at(470, 104, 1, cafetable())
   + at(200, 76, 1, person("#4a3a6a", hat="beret")) + at(330, 76, 1, person("#8a3a2a", hair="#2a1a0a")) + at(560, 60, 1, easel())),
 "Records": ("#5c3b22", "A long, dim room at police headquarters, filled floor to ceiling with wooden fingerprint drawers.",
   room("#bfae8a", "#5c4630", "#3d2e20") + at(30, 20, 1, drawers(5, 4)) + at(410, 20, 1, drawers(6, 4)) + at(250, 100, .9, desk(120)) + at(290, 86, 1, magnifier())),
 "Newspaper": ("#2a2420", "A busy newspaper office with typewriters, a ringing telephone and fresh papers piled up.",
   room("#d8cfb8", "#6e5238", "#4f3a28") + at(40, 100, 1.1, desk(200)) + at(80, 70, 1, typewriter()) + at(170, 78, .8, phone())
   + at(330, 40, 1.1, newspaper("EXTRA!")) + at(460, 76, 1, person("#f3ead2", hair="#2a1a0a")) + at(530, 104, 1, papers(6))),
 "Workers": ("#6e5238", "A row of workers' white smocks hanging on pegs in a museum workroom, with tools on a bench.",
   room("#cbb48c", "#7a5c3e", "#5c4630") + "".join(at(60 + i * 70, 30, 1, path("M0 0 L36 0 L44 70 L-8 70 Z", fill="#f3f0e6", extra='stroke="#cdbf9f"') + circ(18, -4, 4, "#5c3b22")) for i in range(5))
   + at(420, 110, 1, rect(0, 0, 190, 10, "#7a5234") + rect(10, 10, 8, 30, "#5a3b24") + rect(172, 10, 8, 30, "#5a3b24")) + at(450, 80, .9, toolbox()) + at(540, 66, .8, ladder(84))),
}

# ---------------- M02 Flight 305 (1971) ----------------
S["flight-305"] = {
 "Schaffner": ("#3d6b8f", "Rows of airplane seats with the jump seat at the back, where a flight attendant sat beside the last row.",
   rect(0, 0, 640, 190, "#d9dfe4") + rect(0, 0, 640, 40, "#c4ccd3") + "".join(rect(30 + i * 90, 14, 40, 18, "#8fb6d0", 8) for i in range(7))
   + at(40, 96, 1.1, seats(3)) + at(330, 96, 1.1, seats(2)) + at(540, 76, 1, person("#2f5d8a", hair="#d9b06a")) + rect(500, 120, 100, 30, "#9aa3ad", 4)),
 "MoneyRoom": ("#4f6b3a", "A bank vault table covered in stacks of twenty-dollar bills, with a microfilm camera beside them.",
   room("#cfd6cf", "#5a5f5a", "#3a3f3a") + at(80, 100, 1.2, desk(300, "#6f7a6f", "#4a504a")) + at(130, 82, 1, money(3)) + at(240, 82, 1, money(3))
   + at(470, 60, .9, camera_tripod()) + at(560, 40, 1, rect(0, 0, 60, 80, "#7a7f84", 4) + circ(30, 40, 16, "#5a5f64", 'stroke="#aaa" stroke-width="3"'))),
 "Mitchell": ("#7a5234", "A college student in a sweater sitting in an airplane window seat.",
   rect(0, 0, 640, 190, "#d9dfe4") + at(250, 30, 1, rect(0, 0, 70, 50, "#2c4a6e", 20) + rect(8, 8, 54, 34, "#9fc3e6", 14)) + at(150, 96, 1.3, seats(3, "#7a8a6a"))
   + at(300, 70, 1, person("#8a5a35", hair="#4a2a1a"))),
 "Escort": ("#5f6f7f", "Two fighter jets and a training plane parked on an air base runway under a gray sky.",
   sky("#9aa8b4", "#d9dfe4", "esc") + ground("#7a7f74", 130) + rect(0, 140, 640, 20, "#4a4f54") + "".join(rect(x, 148, 30, 4, "#e8e6e0") for x in range(10, 640, 60))
   + at(80, 96, 1.4, fighter()) + at(300, 90, 1.4, fighter("#7f8b98")) + at(500, 30, 1, cloud("#c4ccd3")) + at(470, 104, 1, rect(0, 0, 100, 40, "#9a9f94") + path("M0 0 L50 -20 L100 0 Z", fill="#7a7f74"))),
 "Gate": ("#1f2a44", "An airport check-in counter with a gate sign, a clock and a suitcase waiting in line.",
   room("#e3ddd0", "#9a9f94", "#7a7f74") + at(200, 100, 1, counter("#7a5234", "GATE 4")) + at(560, 40, 1, clock()) + at(80, 76, 1, person("#2f3a44", hair="#2a1a0a"))
   + at(120, 114, 1, suitcase()) + at(470, 76, 1, person("#8a3a2a", hair="#c9a06a")) + at(80, 20, .8, window(90, 50, "sky"))),
 "Newsroom": ("#2a2420", "A 1970s newsroom with desks, typewriters, ringing phones and a front page about the hijacking.",
   room("#d8d2c0", "#6a6f74", "#4a4f54") + at(30, 100, 1.1, desk(210, "#6a6f74", "#4a4f54")) + at(60, 70, 1, typewriter()) + at(170, 78, .8, phone("#c0392b"))
   + at(300, 30, 1.2, newspaper("HIJACKER!")) + at(440, 76, 1, person("#f3ead2", hair="#2a1a0a")) + at(520, 76, 1, person("#2f5d8a", hair="#7a5a3a"))),
 "Plane": ("#3d6b8f", None, None),
 "Mucklow": ("#2f5d8a", "A flight attendant's galley at the back of a plane, with a tray, cups and a call light.",
   rect(0, 0, 640, 190, "#d9dfe4") + rect(0, 0, 640, 30, "#c4ccd3") + at(60, 40, 1, rect(0, 0, 200, 110, "#b9c2ca", 4) + "".join(rect(10 + i * 64, 10, 54, 40, "#9aa3ad", 3) for i in range(3)))
   + at(110, 104, 1, rect(0, 0, 80, 6, "#e8e6e0") + rect(10, -14, 12, 14, "#fbf6e8") + rect(30, -14, 12, 14, "#fbf6e8")) + at(380, 76, 1, person("#2f5d8a", hair="#8a5a2a")) + at(520, 50, 1, circ(0, 0, 10, "#ffd25e", 'stroke="#c9a14a" stroke-width="3"'))),
 "Cockpit": ("#1f2a44", "An airliner cockpit at night: dials glowing on the instrument panel and dark windows ahead.",
   rect(0, 0, 640, 190, "#2a2f36") + path("M60 20 L300 10 L320 80 L40 90 Z", fill="#14233a") + path("M340 10 L580 20 L600 90 L320 80 Z", fill="#14233a")
   + "".join(circ(x, y, 1.3, "#fff") for x, y in [(120, 30), (200, 50), (420, 40), (500, 60), (260, 40)]) + at(220, 110, 1, instrument_panel()) + at(70, 120, 1, rect(0, 0, 120, 70, "#3d4a5a", 10)) + at(450, 120, 1, rect(0, 0, 120, 70, "#3d4a5a", 10))),
}

# ---------------- M03 The Tena Bar Riddle (1980) ----------------
S["tena-bar-riddle"] = {
 "Lab": ("#2f5d8a", "A lab bench where soggy old bills are laid out next to a printed list of serial numbers and a microscope.",
   room("#dfe6e8", "#7a8a8e", "#5a6a6e") + at(60, 100, 1.2, desk(300, "#c9d3d6", "#7a8a8e")) + at(100, 84, 1, money(2)) + at(200, 56, 1, letter(7)) + at(300, 40, 1, microscope())
   + at(470, 30, 1, rect(0, 0, 130, 90, "#f3f0e6", 3, 'stroke="#9fb5bb"') + "".join(rect(10, 10 + i * 10, 110, 3, "#5a6a6e") for i in range(7)))),
 "Weather": ("#4a6a8a", "A weather office with a big rain map of the night of November 24, 1971 pinned to the wall.",
   room("#d6dde0", "#6a7a7e", "#4a5a5e") + at(60, 26, 1, wallmap(180, 100, "weather")) + at(320, 20, 1, cloud("#b9c6cf", True)) + at(300, 100, 1, desk(220, "#7a8a8e", "#5a6a6e")) + at(360, 70, 1, typewriter()) + at(470, 82, 1, papers(4))),
 "Files": ("#7a6a4a", "Boxes of old 1971 search files and a big grid map of the forest with circled squares.",
   room("#cfc2a3", "#6e5238", "#4f3a28") + at(40, 30, 1, wallmap(200, 100, "grid")) + at(300, 116, 1, filebox()) + at(370, 116, 1, filebox("#b99a65")) + at(334, 82, 1, filebox("#d1b07a"))
   + at(450, 100, 1, desk(160)) + at(480, 82, 1, folder("#d9b979", "1971"))),
 "Geologist": ("#9c7f4a", None, None),
 "Beach": ("#3f8c87", "A wide sandy beach on the Columbia River with a small campfire hole where the money was found.",
   sky("#f2c38b", "#f7e2c0", "bch") + rect(0, 70, 640, 20, "#4f6b4a") + "".join(at(x, 40, .7, pine(40)) for x in (40, 90, 520, 580)) + water(88, "#3f8c87")
   + path("M0 130 C120 118 260 126 360 122 C470 118 560 126 640 120 L640 190 L0 190 Z", fill="#e3c98f") + at(220, 150, 1, campfire()) + at(380, 150, 1, bills_in_sand())),
 "RiverMap": ("#3f7f9a", "A big wall map of the Columbia River and the rivers that flow into it, with arrows showing the current.",
   room("#d8cfb8", "#6e5238", "#4f3a28") + at(150, 20, 1.6, wallmap(200, 72, "river")) + at(60, 100, .8, desk(90)) + at(560, 60, 1, magnifier())),
 "Chutes": ("#c0392b", "An open parachute hanging in a records room, next to a file about the four parachutes.",
   room("#d6d0c0", "#6e5238", "#4f3a28") + at(170, 74, 1.2, parachute()) + at(320, 100, 1, desk(220)) + at(350, 74, 1, folder("#d9b979", "4 CHUTES")) + at(460, 84, 1, papers(4))),
 "Newsroom": ("#2a2420", "A newspaper office where the D.B. Cooper story is back on every front page.",
   room("#d8d2c0", "#6a6f74", "#4a4f54") + at(40, 100, 1.1, desk(210, "#6a6f74", "#4a4f54")) + at(80, 70, 1, typewriter()) + at(330, 30, 1.2, newspaper("$5,800 FOUND"))
   + at(470, 76, 1, person("#f3ead2", hair="#2a1a0a")) + at(540, 76, 1, person("#c0563b", hair="#7a5a3a"))),
}

# ---------------- M04 Count at Dawn (Alcatraz, 1962) ----------------
S["count-at-dawn"] = {
 "Cells": ("#5d6670", None, None),
 "Corridor": ("#3a4048", "A dark, narrow utility corridor behind the cells, full of pipes, lit by a guard's flashlight.",
   rect(0, 0, 640, 190, "#262a2f") + "".join(rect(0, y, 640, 8, "#4a4f54") for y in (24, 50, 120)) + "".join(rect(x, 0, 10, 190, "#3a3f44") for x in (120, 360, 560))
   + beam(0, 100, 640, 640, 40, "#fff6c0", ".22") + beam(0, 100, 640, 640, 170, "#fff6c0", ".0") + at(60, 76, 1, person("#5a6a7a", hat="police")) + at(260, 80, 1, vent()) + at(300, 80, 1, vent(False))),
 "Roof": ("#6a6058", "The dusty top of the cellblock: a secret workshop with raincoats, glue and a half-built raft.",
   room("#5a524b", "#4a433d", "#3a3430") + at(40, 30, 1, rect(0, 0, 100, 60, "#9fb3c4") + path("M0 0 L100 60 M100 0 L0 60", stroke="#3a3430", sw=3)) + at(200, 120, 1.6, raft())
   + "".join(at(440 + i * 34, 40, 1, path("M0 0 L24 0 L30 60 L-6 60 Z", fill="#e0b33a", extra='stroke="#9a7514"')) for i in range(4)) + at(470, 120, 1, toolbox())),
 "Music": ("#a3231d", "A prison music room with an accordion case, and the barbershop next door.",
   room("#c9c2b0", "#6a6f74", "#4a4f54") + at(80, 90, 1, accordion()) + at(200, 104, 1, rect(0, 0, 70, 46, "#4a3a2a", 4) + rect(4, 4, 62, 14, "#5c4a36", 2))
   + at(380, 60, 1, rect(0, 0, 70, 50, "#e8e6e0", 4, 'stroke="#aaa" stroke-width="3"')) + at(390, 110, 1, rect(0, 0, 50, 40, "#8a1f1a", 8) + rect(20, 40, 10, 10, "#555")) + at(520, 70, 1, person("#e8e6e0", hair="#3a2a1a"))),
 "Guards": ("#2f4a7a", "The guards' office: count sheets on a desk, a key ring and a wall clock reading dawn.",
   room("#cfc8b4", "#6a6f74", "#4a4f54") + at(80, 100, 1.2, desk(240, "#6a6f74", "#4a4f54")) + at(130, 82, 1, papers(5)) + at(260, 70, .9, phone()) + at(500, 50, 1, clock())
   + at(420, 76, 1, person("#2f4a7a", hat="police", hair="#777")) + at(560, 76, 1, person("#2f4a7a", hat="police"))),
 "West": ("#5d6670", "A prison cell with a half-chipped vent behind the sink, seen through the bars.",
   room("#bdb4a2", "#6a6f74", "#4a4f54") + at(200, 90, 1, vent()) + at(200, 120, 1, sink()) + at(300, 112, 1, cot()) + at(470, 76, 1, person("#9aa3ad", hair="#3a2a1a")) + at(0, 30, 1, cellbars(640, 120))),
 "Shops": ("#8a6a4a", "Prison workshops and a supply room with shelves of raincoats and tools.",
   room("#cbbfa6", "#6a6f74", "#4a4f54") + at(40, 30, 1, rect(0, 0, 220, 100, "#7a5234", 3) + "".join(rect(10 + i * 26, 10, 20, 36, "#e0b33a", 2) for i in range(8)) + "".join(rect(10 + i * 26, 56, 20, 36, "#c9a14a", 2) for i in range(8)))
   + at(340, 110, 1, toolbox()) + at(440, 80, 1, person("#5a6a7a", hair="#777")) + at(520, 40, 1, papers(4))),
 "Shore": ("#4f6577", "The rocky shore of the island at dawn, with the prison wall behind and cold water ahead.",
   sky("#3a4b66", "#f6d3a3", "shr") + rect(0, 40, 640, 80, "#5a524b") + "".join(rect(x, 54, 8, 10, "#ffd98a") for x in range(40, 600, 40)) + water(120, "#4f6577")
   + at(60, 112, 1.6, rocks()) + at(420, 116, 1.4, rocks("#5e544a")) + at(250, 130, 1, raft())),
 "Dock": ("#2f5d8a", "The island dock, with boats full of reporters circling in the bay.",
   sky("#8fb3cf", "#dfe8ee", "dck") + water(110, "#4f6f87") + rect(0, 96, 260, 20, "#6e5238") + "".join(rect(x, 116, 10, 40, "#5c3b22") for x in (20, 120, 220))
   + at(330, 110, 1, path("M0 0 L110 0 L96 26 L12 26 Z", fill="#e8e6e0") + rect(30, -20, 40, 20, "#c4ccd3")) + at(500, 120, .8, path("M0 0 L110 0 L96 26 L12 26 Z", fill="#c0563b") + rect(30, -20, 40, 20, "#e8e6e0"))
   + at(360, 70, .7, person("#f3ead2")) + at(530, 84, .6, person("#2f5d8a"))),
}

# ---------------- M05 The Marshals' File (Alcatraz hunt) ----------------
S["marshals-file"] = {
 "Hut": ("#2f5d8a", "A video call with a scientist, his laptop screen showing swirling tide arrows across the bay.",
   room("#dde3e6", "#7a8a8e", "#5a6a6e") + at(120, 60, 1.2, laptop(True)) + at(330, 30, 1, rect(0, 0, 220, 110, "#0d2a3a", 4)
   + "".join(path(f"M{20+i*40} {30+(i%2)*30} q20 -14 30 10", stroke="#7fd6ff", sw=3) + path(f"M{50+i*40} {40+(i%2)*30} l-6 -2 l2 -6", stroke="#7fd6ff", sw=3) for i in range(5)))),
 "Search": ("#4f6f87", None, None),
 "WestFile": ("#6b5d4f", "A typed statement on a desk, clipped to a photo of a half-open vent.",
   room("#d8cfb8", "#6e5238", "#4f3a28") + at(120, 100, 1.2, desk(300)) + at(170, 40, 1, letter(7)) + at(260, 50, 1, rect(0, 0, 60, 50, "#fbf6e8", 1) + at(12, 12, .9, vent())) + at(380, 56, 1, folder("#d9b979", "WEST")) + at(560, 40, 1, clock())),
 "Widner": ("#3c6e71", "A living room with old family photos on the wall and a box of letters on the table.",
   room("#d9c9a8", "#8a6a4a", "#6e5238", stripes="#cfbe9b") + "".join(at(80 + i * 80, 30, .7, painting(60, 50, "#8a6a4a", "portrait")) for i in range(3)) + at(340, 110, 1, sofa("#3c6e71")) + at(80, 116, 1, filebox()) + at(520, 76, 1, person("#3c6e71", hair="#5a3a1a"))),
 "Tests": ("#a3231d", "Video stills of people paddling a yellow raincoat raft across the bay, with a film clapper.",
   rect(0, 0, 640, 190, "#2a2a2a") + "".join(at(30 + i * 200, 30, 1, rect(0, 0, 180, 110, "#4f7f9a", 3) + rect(0, 70, 180, 40, "#3f6f8a") + at(30, 64, 1, raft())) for i in range(3))
   + "".join(rect(x, 8, 14, 10, "#555", 2) + rect(x, 168, 14, 10, "#555", 2) for x in range(10, 640, 28))),
 "Bay": ("#2f5d8a", "A Coast Guard station window looking out at Alcatraz and the Golden Gate Bridge, with binoculars on the sill.",
   room("#e3e6e8", "#7a8a8e", "#5a6a6e") + at(80, 18, 1.6, bay_window(240, 74)) + at(500, 104, 1, binoculars()) + at(470, 100, .8, desk(120, "#7a8a8e", "#5a6a6e"))),
 "Memo": ("#4a4a4a", "A short typed memo stamped CLOSED, with a newer note clipped to the back.",
   room("#d6d0c0", "#6e5238", "#4f3a28") + at(150, 100, 1.2, desk(300)) + at(220, 30, 1.1, letter(7)) + at(260, 64, 1, stamp_text("CLOSED 1979", "#a3231d", 13)) + at(330, 40, .9, rect(0, 0, 70, 60, "#f3e7c4", 1) + "".join(rect(8, 10 + i * 9, 50, 2.5, "#4a4a4a") for i in range(5)))),
 "Roderick": ("#b8860b", "A deputy marshal's star badge on an office desk beside a thick case file.",
   room("#d1c4a6", "#6e5238", "#4f3a28") + at(60, 20, 1, window(120, 80, "sky")) + at(260, 100, 1.2, desk(260)) + at(330, 70, 1.1, badge_star()) + at(400, 60, 1, folder("#d9b979", "WANTED")) + at(560, 76, 1, person("#4a5a6a", hair="#999"))),
 "Lab": ("#2f5d8a", "A lab table with a photocopied letter under a lamp, a microscope and test results.",
   room("#dfe6e8", "#7a8a8e", "#5a6a6e") + at(80, 100, 1.2, desk(320, "#c9d3d6", "#7a8a8e")) + at(140, 34, 1, letter(6)) + at(240, 40, 1, microscope()) + at(330, 70, 1, lamp("#2f5d8a")) + at(430, 76, 1, jars(4))),
 "Newsroom": ("#2a2420", "A busy newsroom on the anniversary of the escape, with an Alcatraz headline pinned up.",
   room("#d8d2c0", "#6a6f74", "#4a4f54") + at(40, 100, 1.1, desk(210, "#6a6f74", "#4a4f54")) + at(80, 70, 1, typewriter()) + at(320, 30, 1.2, newspaper("ESCAPE!"))
   + at(470, 76, 1, person("#f3ead2", hair="#2a1a0a")) + at(540, 76, 1, person("#6b4fa0", hair="#c9a06a"))),
}

# ---------------- M06 The Sensor Log (Gardner, 1990) ----------------
S["sensor-log"] = {
 "Third": ("#6b4fa0", "A quiet top-floor gallery where every painting hangs exactly where it should.",
   room("#e6dcc6", "#8a6a4a", "#6e5238", wainscot="#d6c8a8") + at(70, 30, 1, painting(70, 54, "#c9a14a", "land")) + at(200, 24, 1, painting(80, 64, "#c9a14a", "portrait")) + at(350, 30, 1, painting(70, 54, "#c9a14a", "sea"))
   + at(480, 24, 1, painting(80, 64, "#c9a14a", "land")) + "".join(rect(x, 140, 30, 4, "#2f8a5a") for x in (100, 240, 380, 520))),
 "Newsroom": ("#2a2420", "A newspaper office on the morning of the theft, with an art-theft headline.",
   room("#d8d2c0", "#6a6f74", "#4a4f54") + at(40, 100, 1.1, desk(210, "#6a6f74", "#4a4f54")) + at(80, 66, 1, crt()) + at(320, 30, 1.2, newspaper("ART STOLEN")) + at(480, 76, 1, person("#f3ead2", hair="#2a1a0a"))),
 "Dutch": ("#5a3a2a", "A tall gallery with dark paintings, two empty frames and broken glass on the floor.",
   room("#5a4636", "#3d2e22", "#2a1f16", wainscot="#4a382a") + at(60, 24, 1, painting(80, 64, "#c9a14a", "portrait")) + at(220, 20, 1.1, painting(90, 70, "#c9a14a", "empty")) + at(390, 26, 1, painting(80, 60, "#c9a14a", "empty"))
   + at(530, 30, 1, painting(60, 54, "#c9a14a", "sea")) + at(200, 156, 1.2, glass_shards()) + at(420, 160, 1, glass_shards())),
 "Short": ("#8a6a2a", "A long, narrow hall of small drawings, with a glass case holding an old silk flag and an eagle on top.",
   room("#e3d6b8", "#8a6a4a", "#6e5238") + "".join(at(40 + i * 60, 34, .6, painting(60, 50, "#8a6a4a", "land")) for i in range(4)) + at(340, 90, 1.4, flag_case()) + "".join(at(540 + i * 40, 40, .5, painting(50, 60, "#8a6a4a", "portrait")) for i in range(2))),
 "Blue": ("#2f5fa8", "A quiet downstairs room with blue walls and one small, empty space where a picture used to hang.",
   room("#6f8fbf", "#5a4a3a", "#3d2e22", wainscot="#5f7faf") + at(80, 30, 1, painting(70, 56, "#c9a14a", "land")) + at(260, 36, 1, tophat_empty()) + at(420, 26, 1, painting(80, 66, "#c9a14a", "portrait")) + at(560, 110, .8, rect(0, 0, 60, 40, "#7a2f2a", 6))),
 "Security": ("#2f6b3a", None, None),
 "Street": ("#2f4a7a", "A city street at night outside the museum, with a police car under a streetlight.",
   night("str") + rect(0, 40, 640, 110, "#3a3a46") + "".join(rect(x, 60, 18, 24, "#ffd98a") for x in range(30, 620, 60)) + rect(0, 150, 640, 40, "#2a2a30")
   + at(130, 140, 1, streetlight()) + at(330, 110, 1.1, policecar()) + at(540, 76, 1, person("#1f2a44", hat="police"))),
 "Guard": ("#2a3a5a", "A night guard's desk by the side door, with a buzzer button, a logbook and a cup of coffee.",
   room("#c9c2b0", "#5a4a3a", "#3d2e22") + at(60, 40, 1, door("#4a3a2a", 60, 110)) + at(220, 100, 1.2, desk(240, "#5c4a36", "#3d2e22")) + at(260, 82, 1, openbook())
   + at(410, 84, 1, rect(0, 0, 30, 16, "#3a3a3a", 3) + circ(15, 8, 5, "#c0392b")) + at(470, 82, 1, path("M0 0 L18 0 L16 16 L2 16 Z", fill="#f3ead2")) + at(560, 40, 1, monitors(1, 1))),
 "Partner": ("#2a3a5a", "A quiet basement room with a single chair and a radio, where the second guard waited.",
   room("#a8a090", "#5a4a3a", "#3d2e22") + "".join(rect(x, 10, 8, 140, "#8a8270") for x in (100, 300, 500)) + at(260, 100, 1, rect(0, 0, 40, 6, "#5c3b22") + rect(4, 6, 4, 44, "#5c3b22") + rect(32, 6, 4, 44, "#5c3b22") + rect(2, -36, 36, 36, "#6e5238", 3))
   + at(400, 110, 1, rect(0, 0, 50, 30, "#3a3a3a", 4) + circ(14, 15, 7, "#888") + rect(30, 8, 14, 4, "#c0392b"))),
}

# ---------------- M07 Frame by Frame (Gardner hunt) ----------------
S["frame-by-frame"] = {
 "Letter": ("#6b5d4f", "A typed, unsigned letter next to a folded newspaper with a coded message circled.",
   room("#d8cfb8", "#6e5238", "#4f3a28") + at(120, 100, 1.2, desk(320)) + at(180, 30, 1.1, letter(7)) + at(280, 34, 1, newspaper("THE GLOBE")) + path("M300 70 m-14 0 a14 10 0 1 0 28 0 a14 10 0 1 0 -28 0", stroke="#c0392b", sw=3) + at(450, 66, 1, envelope())),
 "FBI": ("#1f2a44", "An FBI press room with a podium, microphones and a stack of press releases.",
   room("#cfd3d8", "#4a4f54", "#3a3f44") + at(260, 60, 1, rect(0, 0, 110, 90, "#3a2a1a", 4) + circ(55, 30, 18, "#d4af37")) + at(300, 40, .5, mic()) + at(340, 40, .5, mic())
   + at(60, 100, 1, desk(140, "#5a5f64", "#3a3f44")) + at(90, 82, 1, papers(6)) + at(480, 30, 1, rect(0, 0, 100, 60, "#1f2a44", 3) + text(50, 36, "FBI", 22, "#fbf6e8"))),
 "Reward": ("#a3231d", "A reward poster on the wall showing all 13 missing works, beside a telephone.",
   room("#e3d6b8", "#8a6a4a", "#6e5238") + at(200, 22, 1.2, poster13()) + at(430, 100, 1, desk(160)) + at(470, 78, 1, phone("#2a2a2a")) + at(60, 40, 1, clock())),
 "Frames": ("#5a3a2a", None, None),
 "Sketches": ("#4a4a4a", "Two pencil sketches of men in police caps, pinned on a board under a desk lamp.",
   room("#d8d0bd", "#6e5238", "#4f3a28") + at(160, 26, 1.2, sketches()) + at(400, 100, 1, desk(180)) + at(470, 62, 1, lamp()) + at(420, 84, 1, magnifier())),
 "Lawyers": ("#3d2e22", "A prosecutor's office with law books, a desk and the scales of justice.",
   room("#d9c9a8", "#6e5238", "#4f3a28", wainscot="#a88a5e") + at(40, 20, 1, bookshelf(6, 3, 4)) + at(330, 100, 1.1, desk(240)) + at(420, 20, .9, scales()) + at(560, 76, 1, person("#2a2a3a", hair="#5a3a1a"))),
 "GuardFile": ("#6b5d4f", "An old file of interview notes and a printout of the motion-detector record.",
   room("#d6d0c0", "#6e5238", "#4f3a28") + at(100, 100, 1.2, desk(320)) + at(150, 56, 1, folder("#d9b979", "1990")) + at(260, 90, 1, printer_paper()) + at(400, 34, 1, letter(6))),
 "Connecticut": ("#5a6a3a", "A backyard with a wooden shed, its floor dug up to show an empty hiding hole.",
   sky("#a8c8e0", "#e6eef2", "ct") + ground("#7a9a5a", 120) + at(60, 50, 1, shed()) + at(250, 150, 1.4, hole()) + at(380, 60, 1, shovel()) + at(470, 40, 1, pine(70)) + at(560, 30, 1, pine(80))),
 "Warehouse": ("#6e3a2e", "A dark Brooklyn warehouse with stacked crates, lit by a flashlight beam.",
   brick() + rect(0, 150, 640, 40, "#3a2e26") + rect(0, 0, 640, 150, "#000", 0, 'opacity=".45"') + at(380, 106, 1.1, crates(3)) + beam(60, 70, 520, 600, 150, "#fff6c0", ".3")
   + at(60, 76, 1, person("#3a3a3a", hair="#2a1a0a"))),
 "Newsroom": ("#2a2420", "A radio studio with an ON AIR sign, a microphone and callers' lines blinking.",
   room("#3a3f46", "#2a2a30", "#1a1a20") + at(80, 30, 1, onair()) + at(280, 60, 1.1, mic()) + at(200, 100, 1, desk(240, "#4a4f54", "#2a2f34")) + at(470, 40, 1, rect(0, 0, 110, 50, "#1f2328", 4) + "".join(circ(16 + i * 20, 25, 5, "#c0392b" if i % 2 else "#2f8a5a") for i in range(5)))),
}

# ---------------- M08 The Tower Ledger (1483) ----------------
S["tower-ledger"] = {
 "Tower": ("#6b4fa0", "The Tower of London guidebook open beside a map of its walls and towers.",
   room("#e3d6b8", "#7a5c3e", "#5c4630") + at(60, 26, 1, wallmap(160, 100, "tower")) + at(300, 30, .8, tower_castle()) + at(420, 100, 1, openbook())),
 "Mancini": ("#6b4fa0", None, None),
 "Law": ("#5c3b22", "A long old parliamentary roll with a wax seal, unrolled on a library table.",
   room("#cbb48c", "#5c4630", "#3d2e20") + at(40, 20, 1, bookshelf(4, 3, 5)) + at(250, 30, 1.2, scroll()) + at(420, 100, 1, desk(180)) + at(450, 70, 1, magnifier())),
 "More": ("#7a2a22", "A printed history book of Richard III beside a copy of a famous play.",
   room("#d9c9a8", "#6e5238", "#4f3a28") + at(60, 20, 1, bookshelf(5, 3, 3)) + at(280, 80, 1.2, openbook()) + at(460, 50, 1, rect(0, 0, 60, 80, "#7a2a22", 3) + rect(6, 8, 48, 14, "#d4af37", 1))),
 "Warbeck": ("#2f5d8a", "Letters from foreign courts with red seals, and a signed confession.",
   room("#d8cfb8", "#6e5238", "#4f3a28") + at(100, 100, 1.2, desk(340)) + at(140, 56, 1, envelope()) + at(240, 60, 1, envelope("#e8dcc0")) + at(360, 30, 1, letter(7)) + at(460, 66, 1, stamp_text("CONFESSION", "#2f5d8a", 11))),
 "Bones": ("#7a6a5a", "An old staircase drawing and a white marble urn, like the one in Westminster Abbey.",
   room("#d6cdb8", "#7a6a5a", "#5a4a3a") + at(80, 150, 1, stairs("#b0a48c", 6)) + at(380, 76, 1.1, urn()) + at(510, 30, 1, letter(5))),
 "Exam": ("#2f5d8a", "A 1930s science report with measuring calipers and photographs on a desk.",
   room("#dfe2df", "#7a7a72", "#5a5a52") + at(100, 100, 1.2, desk(340, "#8a8a7a", "#5a5a52")) + at(150, 30, 1, letter(7)) + at(250, 44, 1, rect(0, 0, 60, 46, "#3a3a3a", 2) + rect(4, 4, 52, 38, "#8a8a8a"))
   + at(360, 70, 1, path("M0 0 L60 0 M10 0 L10 30 M50 0 L50 30", stroke="#7a7a7a", sw=4))),
 "Langley": ("#3c6e71", "A stack of new history books, a documentary playing on a laptop and a pile of reviews.",
   room("#e1dccf", "#7a6a5a", "#5a4a3a") + at(80, 100, 1.2, desk(340)) + at(130, 50, 1, laptop(False, "#3c6e71")) + "".join(at(280 + i * 6, 80 - i * 12, 1, rect(0, 0, 70, 12, ["#a3231d", "#2f5d8a", "#3c6e71", "#b8860b"][i], 2)) for i in range(4)) + at(400, 70, 1, papers(5))),
 "Suspects": ("#a3231d", "Three folders on a shelf, each with a crown, a coat of arms or a rose on the front.",
   room("#d9c9a8", "#6e5238", "#4f3a28") + at(100, 40, 1.2, folder("#c9a14a")) + at(250, 40, 1.2, folder("#b8a07a")) + at(400, 40, 1.2, folder("#d9b979")) + at(124, 52, .5, crown()) + at(290, 64, 1, circ(0, 0, 12, "#2f5d8a")) + at(440, 64, 1, circ(0, 0, 10, "#c0392b") + circ(0, 0, 5, "#f3ead2"))),
 "Giftshop": ("#2a2440", "A museum gift shop with a postcard rack, ghost-tour flyers and dramatic paperbacks.",
   room("#e8dfc8", "#8a6a4a", "#6e5238") + at(120, 40, 1, postcards()) + at(240, 70, 1, ghostflyer()) + at(300, 70, 1, ghostflyer()) + at(380, 100, 1, counter("#7a5234")) + at(400, 70, 1, rect(0, 0, 40, 30, "#6b4fa0", 2))),
}

# ---------------- M09 The Apollo Gallery (Louvre, 2025) ----------------
S["apollo-gallery"] = {
 "Curator": ("#2f5fa8", "A curator's office with photographs of the missing jewels pinned to the wall: sapphires, emeralds and diamonds.",
   room("#e6dcc6", "#8a6a4a", "#6e5238") + at(40, 30, 1, corkboard(180, 90, False)) + at(60, 50, .5, necklace("#2f5fa8")) + at(150, 50, .5, necklace("#2f8a5a")) + at(90, 96, .5, tiara())
   + at(320, 40, 1.1, necklace("#2f5fa8")) + at(440, 50, 1, tiara()) + at(380, 100, 1, desk(220))),
 "Gallery": ("#b8860b", "A long golden hall with a painted ceiling and empty spaces where the display cases used to stand.",
   rect(0, 0, 640, 60, "#c99a3a") + "".join(path(f"M{x} 10 q30 30 60 0", stroke="#e9cf6a", sw=3) for x in range(0, 640, 70)) + rect(0, 60, 640, 90, "#8a5a2a") + rect(0, 150, 640, 40, "#5c3b22")
   + "".join(at(x, 70, .7, painting(60, 60, "#d4af37", "portrait")) for x in (40, 200, 360, 520)) + "".join(rect(x, 140, 70, 8, "#3d2716", 2, 'opacity=".5"') for x in (110, 270, 430))),
 "Control": ("#1d4f6a", "A security control room with a wall of screens showing camera footage and time stamps.",
   room("#2a2f36", "#1a1f24", "#111") + at(150, 20, 1.2, monitors(3, 2)) + at(120, 120, 1, rect(0, 0, 400, 20, "#3a3f46", 3)) + at(560, 76, 1, person("#2f3a44", hair="#2a1a0a"))),
 "Archive": ("#7a6a4a", "A yellowed 1911 newspaper showing an empty wall with four iron hooks.",
   room("#cfc2a3", "#6e5238", "#4f3a28") + at(60, 20, 1, bookshelf(4, 3, 7)) + at(260, 30, 1.3, newspaper("1911")) + at(286, 64, 1, rect(0, 0, 30, 24, "#efe4c4") + "".join(circ(x, y, 1.6, "#333") for x, y in [(4, 4), (26, 4), (4, 20), (26, 20)])) + at(470, 100, 1, desk(150))),
 "Guard": ("#2f3a44", "A museum guard in uniform beside a velvet rope in a gallery.",
   room("#e6dcc6", "#8a6a4a", "#6e5238") + at(80, 30, 1, painting(80, 64, "#c9a14a", "land")) + at(260, 120, 1, rect(0, 0, 6, 30, "#b8860b") + rect(150, 0, 6, 30, "#b8860b") + path("M3 4 Q80 30 153 4", stroke="#7a1f19", sw=5))
   + at(500, 76, 1, person("#2f3a44", hair="#5a3a1a")) + at(560, 30, .8, painting(60, 50, "#c9a14a", "portrait"))),
 "Quay": ("#d9663a", None, None),
 "Escape": ("#c0392b", "A street map with a dotted red line showing the escape route and dots where things were found.",
   room("#d8d0bd", "#6e5238", "#4f3a28") + at(100, 20, 1.6, wallmap(200, 76, "route")) + at(520, 120, 1, scooter())),
 "TV": ("#6b4fa0", "A TV talk show set with a sofa, studio lights and a camera pointed at the guests.",
   rect(0, 0, 640, 190, "#2a2440") + "".join(circ(x, 16, 8, "#fff3b0") for x in range(40, 640, 80)) + at(170, 96, 1, sofa("#6b4fa0")) + at(210, 76, .9, person("#c0563b", hair="#2a1a0a")) + at(270, 76, .9, person("#2f5d8a", hair="#c9a06a"))
   + at(480, 60, 1, tvcam()) + rect(0, 150, 640, 40, "#1f1a30")),
 "Update": ("#7a6a4a", "A thin folder marked 2026, open on a desk with a few new pages.",
   room("#d8cfb8", "#6e5238", "#4f3a28") + at(150, 100, 1.2, desk(320)) + at(220, 40, 1.4, folder("#d9b979", "2026")) + at(380, 50, 1, letter(5)) + at(560, 40, 1, clock())),
 "Lab": ("#2f8a5a", "A forensics lab with sealed evidence bags on a shelf, a microscope and a DNA model.",
   room("#dfe8e6", "#7a8a8a", "#5a6a6a") + at(40, 24, 1, shelf(170, bags(5))) + at(40, 86, 1, shelf(170, jars(6))) + at(300, 100, 1, desk(260, "#c9d3d6", "#7a8a8e")) + at(340, 40, 1, microscope()) + at(500, 20, 1, dna())),
 "Prosecutor": ("#3d2e22", "A prosecutor's office in Paris with law books, a desk and the scales of justice.",
   room("#e3d6b8", "#6e5238", "#4f3a28", wainscot="#b89a6e") + at(40, 20, 1, bookshelf(6, 3, 6)) + at(330, 100, 1.1, desk(240)) + at(420, 20, .9, scales()) + at(560, 76, 1, person("#2a2a3a", hair="#7a5a3a"))),
}


def build():
    out_all = []
    for game, places in S.items():
        data = {}
        for key, (color, label, body) in places.items():
            data[key] = {"color": color}
            if body:
                data[key]["svg"] = svg(key, label, body)
                out_all.append((game, key, label, data[key]["svg"]))
        js = "setup.placeArt = " + json.dumps(data, ensure_ascii=False) + ";"
        (HERE / f"{game}.places.twee").write_text(f":: PlaceArt [script]\n{js}\n")
    page = ['<!doctype html><meta charset="utf-8"><style>body{background:#3b2f26;font:13px sans-serif;color:#fbf6e8;margin:0;padding:10px}'
            'div{display:inline-block;width:300px;margin:6px;vertical-align:top}svg{width:300px;height:auto;border-radius:6px;display:block}</style>']
    for g, k, l, s in out_all:
        page.append(f"<div>{s}<b>{g.split('-')[0]}/{k}</b></div>")
    (HERE / "preview.html").write_text("".join(page))
    print(len(out_all), "pictures")


if __name__ == "__main__":
    build()
