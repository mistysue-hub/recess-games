#!/usr/bin/env python3
"""Builds the C# Launchpad reading pages (HTML, hosted on GitHub Pages) and the
plain-text fallback readings (resources/M0NSharp.md) from one source of truth,
so a reading change only ever happens here. Run: python3 build_readings.py"""
import html, json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_HTML = os.path.join(HERE, "readings")
OUT_MD = os.path.join(HERE, "resources")
os.makedirs(OUT_HTML, exist_ok=True); os.makedirs(OUT_MD, exist_ok=True)

# ---------- content: one dict per mission -------------------------------------
# Block kinds: brief (text), code (editor box), predict (commit a guess), tip,
# alert (Red Alert bug hunt), launch (build task), note (plain), rule (mini law)
MISSIONS = [
 {
  "num": "01", "slug": "hello-computer", "title": "Hello, Computer",
  "tagline": "Teach a machine to talk. It will only say exactly what you tell it.",
  "badge": "FIRST CONTACT",
  "blocks": [
   ("brief", "Welcome aboard, cadet. The ship's computer is called SHARP. SHARP is fast, powerful, and completely literal. It never guesses what you meant. It does exactly what you typed, in the order you typed it, and nothing else."),
   ("brief", "A program is a list of instructions. SHARP reads them top to bottom. Each instruction is called a statement, and every statement ends with a semicolon. Think of the semicolon as the period at the end of a sentence; forget it and SHARP refuses to move."),
   ("code", ["Console.WriteLine(\"Hello, Computer\");"]),
   ("rule", "Console", "the text screen.", "WriteLine", "write this, then start a new line.", "\"...\"", "the words to print. The quotes mark where the text starts and ends. They do not print."),
   ("tip", "The line <code>using System;</code> at the top is SHARP's toolbox; it's what makes <code>Console</code> work. Every program in this course starts with it. If the editor already shows it, leave it there."),
   ("tip", "SHARP cares about capital letters. <code>Console</code> works. <code>console</code> gets you a red error and a very unhelpful stare."),
   ("brief", "A comment is a note for humans. SHARP skips it completely. A comment starts with two slashes."),
   ("code", ["// SHARP ignores this line. Write notes to yourself here."]),
   ("predict", "Before you run the code below: what will the <b>second</b> line print? Say it in your head. Then run it."),
   ("code", ["using System;", "", "Console.WriteLine(\"Hello, Computer\");",
             "Console.WriteLine(\"My name is on the next line.\");",
             "// The computer ignores this comment.",
             "Console.WriteLine(\"Bye!\");"], "STARTER"),
   ("alert", "SHARP is stuck. One tiny thing is missing. Type this in, run it, read the red error, fix it.",
     ["Console.WriteLine(\"Lunch is at noon.\")", "Console.WriteLine(\"Bring a sandwich.\");"]),
   ("launch", "Make a sign for your door",
     ["At least <b>5</b> Console.WriteLine lines.",
      "At least <b>1</b> comment.",
      "One line is a row of symbols, like <code>========</code> or <code>~~~~~~~~</code>, so it looks like a sign.",
      "Paste your code <b>and</b> what it printed to Rocky."]),
  ],
 },
 {
  "num": "02", "slug": "boxes-with-labels", "title": "Boxes with Labels",
  "tagline": "Give SHARP a memory. Then make it tell a story.",
  "badge": "CARGO MASTER",
  "blocks": [
   ("brief", "A variable is a box with a label. You put a value in the box, and later you use the label to get it back. SHARP has unlimited boxes, but it is picky about what goes in each one."),
   ("brief", "Making a box takes three parts: the <b>type</b> of thing it holds, the <b>label</b>, and the <b>value</b>."),
   ("code", ["int age = 12;"]),
   ("rule", "int", "the type: whole numbers only.", "age", "the label you pick.", "12", "the value that goes in the box."),
   ("brief", "Four types you'll use constantly:"),
   ("code", ["int lives = 3;              // whole numbers",
             "double height = 1.52;       // numbers with a decimal point",
             "string hero = \"Kai\";        // text, always in double quotes",
             "bool hasKey = true;         // true or false, no quotes"]),
   ("brief", "To print a box inside a sentence, put a dollar sign before the opening quote and wrap the label in curly braces. SHARP swaps the label for the value."),
   ("code", ["Console.WriteLine($\"{hero} has {lives} lives.\");"]),
   ("tip", "Forget the <code>$</code> and SHARP prints the curly braces and the label as plain text. Do it once on purpose. You'll do it by accident later anyway."),
   ("predict", "What does the <b>last</b> line print: <code>I am {age}</code>, <code>I am age</code>, or <code>I am 12</code>? Decide. Then run."),
   ("code", ["using System;", "", "string hero = \"Kai\";", "int lives = 3;", "double height = 1.52;", "bool hasKey = true;",
             "Console.WriteLine($\"{hero} is {height} meters tall.\");",
             "Console.WriteLine($\"Lives left: {lives}\");",
             "Console.WriteLine($\"Has the key? {hasKey}\");",
             "int age = 12;", "Console.WriteLine($\"I am {age}\");"], "STARTER"),
   ("alert", "One box has the wrong type for what's inside it. SHARP will tell you, loudly. Fix it.",
     ["int favoriteFood = \"pizza\";", "int slices = 8;", "Console.WriteLine($\"{slices} slices of {favoriteFood}\");"]),
   ("launch", "Mad Libs",
     ["Make at least <b>4</b> boxes using at least <b>3</b> different types.",
      "Print a short story, at least <b>3</b> lines, each using a box inside <code>$\"...\"</code> text.",
      "Paste code and output to Rocky.",
      "Then change <b>one</b> box's value, run again, and paste the new output. Same code, new story."]),
  ],
 },
 {
  "num": "03", "slug": "math-that-lies", "title": "Math That Lies",
  "tagline": "SHARP does math perfectly. It also drops things on the floor.",
  "badge": "TRAP SPOTTER",
  "blocks": [
   ("brief", "SHARP does math with the symbols you expect, plus one you may not know:"),
   ("code", ["+   add", "-   subtract", "*   multiply", "/   divide", "%   remainder (what's left over after dividing)"]),
   ("brief", "Here is the trap. When <b>both</b> numbers are whole numbers (int), SHARP does whole-number division and throws away the leftover part. <code>7 / 2</code> is <code>3</code>. Not 3.5. Not rounded. Chopped. SHARP isn't wrong; it's doing exactly what <code>int</code> means. The leftover goes to <code>%</code>: <code>7 % 2</code> is <code>1</code>."),
   ("brief", "If at least one number has a decimal point, you get the decimal answer: <code>7.0 / 2</code> is <code>3.5</code>."),
   ("brief", "Text has tools too. <code>.Length</code> counts the characters. <code>.ToUpper()</code> SHOUTS."),
   ("code", ["string pet = \"ferret\";", "Console.WriteLine(pet.Length);      // 6", "Console.WriteLine(pet.ToUpper());   // FERRET"]),
   ("predict", "Guess the <b>fourth</b> line's output before running. (Hint: SHARP multiplies before it adds, like math class.)"),
   ("code", ["using System;", "", "Console.WriteLine(7 / 2);", "Console.WriteLine(7.0 / 2);", "Console.WriteLine(7 % 2);",
             "Console.WriteLine(3 + 4 * 2);", "string pet = \"ferret\";", "Console.WriteLine(pet.Length);",
             "Console.WriteLine(pet.ToUpper());"], "STARTER"),
   ("alert", "No red error this time. It runs. The answer is still wrong. This is the sneakiest kind of bug. Find out why and fix it.",
     ["int score1 = 90;", "int score2 = 85;", "int score3 = 88;",
      "int average = (score1 + score2 + score3) / 3;", "Console.WriteLine($\"Average: {average}\");"]),
   ("launch", "Allowance calculator (wrong, then right)",
     ["<b>Part 1, the trap:</b> make an <code>int</code> for weekly allowance (pick an odd number, like 7) and an <code>int</code> for how many people split it (like 2). Divide and print <code>Each person gets $___</code>. Run it. Look at the answer.",
      "<b>Part 2, the fix:</b> change both to <code>double</code>, run again, print the real amount.",
      "Paste <b>both</b> versions and both outputs to Rocky, plus one sentence: why was the first answer wrong?"]),
  ],
 },
]

from missions_04_09 import MORE
MISSIONS += MORE

# ---------- HTML template ------------------------------------------------------
CSS = """
:root{--bg:#0a0f1f;--panel:#111a33;--panel2:#0d1530;--line:#223058;--ink:#e8edff;--dim:#8a97c4;
--lime:#b4ff5c;--cyan:#6fe3ff;--amber:#ffb84d;--pink:#ff6fae;--red:#ff5c5c;--mono:'JetBrains Mono',Consolas,'Courier New',monospace}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:17px/1.6 'Nunito',system-ui,sans-serif;
background-image:radial-gradient(circle at 20% 0,#1a2a5a 0,transparent 40%),radial-gradient(circle at 90% 100%,#2a1640 0,transparent 35%)}
.wrap{max-width:860px;margin:0 auto;padding:24px 16px 80px}
.win{background:var(--panel);border:1px solid var(--line);border-radius:14px;overflow:hidden;box-shadow:0 20px 60px #0008}
.bar{display:flex;align-items:center;gap:8px;padding:10px 14px;background:var(--panel2);border-bottom:1px solid var(--line);font:13px var(--mono);color:var(--dim)}
.bar i{width:12px;height:12px;border-radius:50%;display:inline-block}.bar i:nth-child(1){background:#ff5f57}.bar i:nth-child(2){background:#febc2e}.bar i:nth-child(3){background:#28c840}
.bar span{margin-left:8px}
.hero{padding:28px 28px 18px}.k{font:700 13px var(--mono);letter-spacing:.18em;color:var(--lime)}
h1{font:800 40px/1.1 'Nunito',sans-serif;margin:6px 0 8px;letter-spacing:-.01em}.tag{color:var(--dim);font-size:18px;margin:0}
.body{padding:8px 28px 28px}p{margin:14px 0}code{font:15px var(--mono);background:#0008;padding:2px 6px;border-radius:5px;color:var(--cyan)}
.ed{margin:18px 0;border:1px solid var(--line);border-radius:10px;overflow:hidden;background:#070b18}
.ed .t{display:flex;justify-content:space-between;font:12px var(--mono);letter-spacing:.14em;color:var(--dim);padding:7px 12px;background:#0b1226;border-bottom:1px solid var(--line)}
.ed .t b{color:var(--lime)}
.ed pre{margin:0;padding:12px 0;font:15px/1.65 var(--mono);overflow-x:auto}.ed .l{display:flex}.ed .n{width:44px;text-align:right;padding-right:14px;color:#3d4c7a;user-select:none;flex:none}
.s{color:#ffd37a}.c{color:#5d6b94;font-style:italic}.kw{color:#7fa8ff}.m{color:var(--cyan)}.num{color:var(--pink)}
.run{display:flex;align-items:center;gap:10px;padding:8px 12px;border-top:1px solid var(--line);font:13px var(--mono);color:var(--dim);background:#0b1226}
.run b{background:var(--lime);color:#0a0f1f;padding:3px 10px;border-radius:6px;font-weight:800}
.box{margin:22px 0;padding:16px 18px 16px 20px;border-radius:10px;border-left:5px solid;background:#ffffff08}
.box .h{font:800 12px var(--mono);letter-spacing:.18em;margin-bottom:6px}
.predict{border-color:var(--cyan)}.predict .h{color:var(--cyan)}
.tip{border-color:var(--amber)}.tip .h{color:var(--amber)}
.alert{border-color:var(--red);background:#ff5c5c12}.alert .h{color:var(--red)}
.launch{border-color:var(--lime);background:#b4ff5c10}.launch .h{color:var(--lime)}
.launch ol{margin:8px 0 0 20px;padding:0}.launch li{margin:6px 0}
.rule{display:grid;grid-template-columns:auto 1fr;gap:6px 14px;margin:14px 0;font-size:16px}.rule code{justify-self:start}
.badge{margin:34px 0 0;text-align:center}.badge .pill{display:inline-block;border:2px dashed var(--lime);color:var(--lime);border-radius:999px;padding:8px 18px;font:800 13px var(--mono);letter-spacing:.2em}
.badge p{color:var(--dim);font-size:15px;margin:10px 0 0}
.foot{color:#5d6b94;font-size:13px;text-align:center;margin-top:30px}
@media(max-width:520px){h1{font-size:30px}.hero,.body{padding-left:16px;padding-right:16px}.ed pre{font-size:13px}}
"""

def hl(line):
    """Tiny C# syntax colorizer: tokenizes into comment / string / code first, so
    inserted span markup is never re-scanned."""
    def code(t):
        e = html.escape(t)
        e = re.sub(r'\b(int|double|string|bool|true|false|var|void|if|else|for|while|foreach|in|switch|case|break|default|return|class|public|new)\b', r'<span class="kw">\1</span>', e)
        e = re.sub(r'\b(Console|WriteLine|Length|ToUpper|List|Count|Add|Random|Next)\b', r'<span class="m">\1</span>', e)
        e = re.sub(r'(?<![\w&#.])(\d+\.?\d*)(?![\w;])', r'<span class="num">\1</span>', e)
        return e
    out, i, n = [], 0, len(line)
    while i < n:
        if line.startswith("//", i):
            out.append(f'<span class="c">{html.escape(line[i:])}</span>'); break
        if line[i] == '"':
            j = line.find('"', i + 1); j = n - 1 if j < 0 else j
            out.append(f'<span class="s">{html.escape(line[i:j+1])}</span>'); i = j + 1; continue
        j = i
        while j < n and line[j] != '"' and not line.startswith("//", j): j += 1
        out.append(code(line[i:j])); i = j
    return "".join(out)

def editor(lines, label="C#", show_run=True):
    rows = "".join(f'<div class="l"><span class="n">{i+1}</span><span>{hl(l)}</span></div>' for i, l in enumerate(lines))
    run = '<div class="run"><b>▶ RUN</b> output shows here. Guess first.</div>' if show_run else ""
    return f'<div class="ed"><div class="t"><span>Program.cs</span><b>{label}</b></div><pre>{rows}</pre>{run}</div>'

def render_html(m):
    out = []
    for b in m["blocks"]:
        k = b[0]
        if k == "brief": out.append(f"<p>{b[1]}</p>")
        elif k == "code": out.append(editor(b[1], b[2] if len(b) > 2 else "C#", show_run=(len(b) > 2)))
        elif k == "rule":
            parts = b[1:]; cells = "".join(f"<code>{html.escape(parts[i])}</code><span>{html.escape(parts[i+1])}</span>" for i in range(0, len(parts), 2))
            out.append(f'<div class="rule">{cells}</div>')
        elif k == "tip": out.append(f'<div class="box tip"><div class="h">⚠ HEADS UP</div>{b[1]}</div>')
        elif k == "predict": out.append(f'<div class="box predict"><div class="h">🔮 PREDICT</div>{b[1]}</div>')
        elif k == "alert": out.append(f'<div class="box alert"><div class="h">🚨 RED ALERT: BUG HUNT</div>{b[1]}{editor(b[2], "BROKEN", False) if len(b) > 2 else ""}</div>')
        elif k == "launch":
            items = "".join(f"<li>{s}</li>" for s in b[2])
            out.append(f'<div class="box launch"><div class="h">🚀 LAUNCH: {html.escape(b[1]).upper()}</div><ol>{items}</ol></div>')
    body = "\n".join(out)
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Mission {m['num']}: {html.escape(m['title'])} · C# Launchpad</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Nunito:wght@400;700;800&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body><div class="wrap"><div class="win">
<div class="bar"><i></i><i></i><i></i><span>C# LAUNCHPAD · MISSION {m['num']}</span></div>
<div class="hero"><div class="k">MISSION {m['num']} OF 09</div><h1>{html.escape(m['title'])}</h1><p class="tag">{html.escape(m['tagline'])}</p></div>
<div class="body">{body}
<div class="badge"><div class="pill">BADGE: {m['badge']}</div><p>Earn it by finishing the Launch and the debrief with Rocky.</p></div>
</div></div><p class="foot">Written for C# Launchpad. No material copied from any book or site. Fonts by Google Fonts.</p></div></body></html>"""

def strip_tags(s):
    s = re.sub(r"<code>(.*?)</code>", r"`\1`", s); s = re.sub(r"<b>(.*?)</b>", r"**\1**", s)
    s = re.sub(r"</?(i|br)\s*/?>", "", s)
    return html.unescape(s)

def render_md(m):
    out = [f"# Mission {m['num']}: {m['title']}", "", f"*{m['tagline']}*", ""]
    for b in m["blocks"]:
        k = b[0]
        if k == "brief": out += [strip_tags(b[1]), ""]
        elif k == "code": out += [f"**{b[2]}**" if len(b) > 2 else "", "```csharp", *b[1], "```", ""]
        elif k == "rule": out += [f"- `{b[i]}` — {strip_tags(b[i+1])}" for i in range(1, len(b), 2)] + [""]
        elif k == "tip": out += ["> **HEADS UP:** " + strip_tags(b[1]), ""]
        elif k == "predict": out += ["> **PREDICT:** " + strip_tags(b[1]), ""]
        elif k == "alert": out += ["## RED ALERT: Bug Hunt", strip_tags(b[1]), ""] + (["```csharp", *b[2], "```", ""] if len(b) > 2 else [])
        elif k == "launch": out += [f"## LAUNCH: {b[1]}", *[f"{i+1}. {strip_tags(s)}" for i, s in enumerate(b[2])], ""]
    out += [f"**Badge: {m['badge']}** — earned by finishing the Launch and the debrief with Rocky.", "",
            "Written for C# Launchpad. No material was copied from any book or site."]
    return "\n".join(out).replace("\n\n\n", "\n\n")

for m in MISSIONS:
    with open(os.path.join(OUT_HTML, f"M{m['num']}.html"), "w") as f: f.write(render_html(m))
    with open(os.path.join(OUT_MD, f"M{m['num']}Sharp.md"), "w") as f: f.write(render_md(m))
    print("built", m["num"], m["title"])
