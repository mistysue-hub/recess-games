#!/usr/bin/env python3
"""Build the Wild and Crazy set-card pages (site/readings/mNN.html) from resources/MNNStandup.md.
Run from the course root: python3 tools/build_readings.py
Edit the reading in BOTH places: the resources/ file (Recess) and the page (GitHub Pages) come from the same source, so rerun this after any change."""
import re, html, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
TEMPLATE = (ROOT / "tools" / "reading_template.html").read_text()

def md_inline(s):
    s = html.escape(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"\*(.+?)\*", r"<em>\1</em>", s)
    return s

def build(src):
    text = src.read_text().strip().split("\n")
    title = text[0].lstrip("# ").strip()
    num = re.search(r"Set Card (\d+)", title).group(1)
    short = title.split(":", 1)[1].strip() if ":" in title else title
    cards, cur, note, fine = [], None, None, None
    for line in text[1:]:
        line = line.rstrip()
        if not line:
            continue
        if line.startswith("## "):
            cur = {"h": line[3:].strip(), "p": []}
            cards.append(cur)
        elif line.startswith("**A note before we start.**"):
            note = line.replace("**A note before we start.**", "").strip()
        elif line.startswith("*Written for this course"):
            fine = line.strip("*")
        else:
            (cur["p"] if cur else []).append(line)
    body = ""
    if note:
        body += f'<div class="note">Heads up: {md_inline(note)}</div>\n'
    for i, c in enumerate(cards):
        inner = "".join(f"<p>{md_inline(p)}</p>" for p in c["p"])
        if i == len(cards) - 1 and fine:
            inner += f'<p class="fine">{html.escape(fine)}</p>'
        note_html = body if i == 0 else ""
        body = "" if i == 0 else body
        cards_html = f'<section class="card"><span class="pin"></span>{note_html}<h2>{md_inline(c["h"])}</h2>{inner}</section>\n'
        body += cards_html
    page = TEMPLATE.replace("{{TITLE}}", html.escape(f"Set Card {num}: {short}")).replace("{{NUM}}", num).replace("{{SHORT}}", html.escape(short)).replace("{{BODY}}", body)
    out = ROOT / "site" / "readings" / f"m{int(num):02d}.html"
    out.write_text(page)
    return out

if __name__ == "__main__":
    for src in sorted((ROOT / "resources").glob("M??Standup.md")):
        print("built", build(src))
