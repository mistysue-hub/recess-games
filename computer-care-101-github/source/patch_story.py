"""Patch the built Computer Care 101 game pages in place.
The original Python generators were lost with a cloud container (Nov 2026); the built index.html embeds
the whole story as JSON (const STORY=...), so edits are made here and re-injected.
Usage: python3 patch_story.py <index.html> [--check]
"""
import re, json, sys, html

def load(path):
    s = open(path, encoding='utf-8').read()
    m = re.search(r'const STORY=(\{.*?\});\n', s, re.S)
    return s, m, json.loads(m.group(1))

def save(path, s, m, story):
    s = s[:m.start(1)] + json.dumps(story, ensure_ascii=False) + s[m.end(1):]
    open(path, 'w', encoding='utf-8').write(s)

def relink(P, key, old, new):
    assert f'->{old}]]' in P[key], (key, old)
    P[key] = P[key].replace(f'->{old}]]', f'->{new}]]')

def patch_nov24(s, story, jr):
    P = story['passages']
    # 2. Track mini-game misses so the results line can report them (both courses).
    for k in list(P):
        m = re.match(r'^D(\d+) S\d+ W$', k)
        if m and '(set: $m' not in P[k]:
            P[k] = f'(set: $m{m.group(1)} to it + (a: "mini-game"))' + P[k]
    for k in list(P):
        if k.endswith(' Done') and 'rocky-copy' in P[k] and '{mini}' not in P[k]:
            P[k] = P[k].replace('Needed help with: {missed}.', 'Needed help with: {missed}. Mini-game misses: {mini}.')
    # 3. Shift bar: show the final exam next to the workday count.
    days = len([k for k in P if re.match(r'^D\d+ Start$', k)])
    P['Init'] = P['Init'] + '(set: $xd to 0)' if '$xd' not in P['Init'] else P['Init']
    if '$xd' not in P['Certificate']:
        P['Certificate'] = '(set: $xd to 1)' + P['Certificate']
    P['Shift Bar'] = (f'<div class="casebar">🛠️ Workdays done: (print: $days\'s length) / {days} · '
                      f'🎓 Final Exam: (if: $xd >= 1)[done](else:)[after Day {days}] · [[Work schedule->Shop]] · [[Toolbox->Toolbox]]</div>')
    if jr:
        # 1. Day 5: the mini-game ran before the Trackballs lesson that teaches two of its items. Move it after Mr. Patel.
        if '->D5 S1]]' in P['D5 J5 R']:
            relink(P, 'D5 J5 R', 'D5 S1', 'D5 L7')
            P['D5 J5 R'] = P['D5 J5 R'].replace('[[Next customer->D5 L7]]', '[[The Inspector has something to show you->D5 L7]]')
            relink(P, 'D5 J8 R', 'D5 L9', 'D5 S1')
            P['D5 J8 R'] = P['D5 J8 R'].replace('[[The Inspector has something to show you->D5 S1]]', '[[A quick sorting game->D5 S1]]')
            relink(P, 'D5 S7 R', 'D5 L7', 'D5 L9'); relink(P, 'D5 S7 W', 'D5 L7', 'D5 L9')
        # 4. Exam Q6: Mr. Chen is a grandfather (his grandson Ollie appears in Sr), not a kid with a little sister.
        P['X6'] = P['X6'].replace('His little sister splashed water on his laptop.', 'His grandson Ollie splashed water on his laptop.')
    # JS: fill {mini} and keep "mini-game" out of the first-try customer count.
    old = "const miss=[...new Set(S[b.dataset.key]||[])];const tot=+b.dataset.total;\n    const msg=b.dataset.msg.replace('{first}',String(Math.max(0,tot-miss.length))).replace('{missed}',miss.length?miss.join(', '):(b.dataset.none||'nobody'));"
    new = "const all=S[b.dataset.key]||[];const mini=all.filter(x=>x==='mini-game').length;const miss=[...new Set(all.filter(x=>x!=='mini-game'))];const tot=+b.dataset.total;\n    const msg=b.dataset.msg.replace('{first}',String(Math.max(0,tot-miss.length))).replace('{missed}',miss.length?miss.join(', '):(b.dataset.none||'nobody')).replace('{mini}',String(mini));"
    if old in s: s = s.replace(old, new)
    else: assert 'const mini=' in s, 'rocky JS not found'
    return s

if __name__ == '__main__':
    path = sys.argv[1]
    s, m, story = load(path)
    s = patch_nov24(s, story, jr='unit1' in path or 'computer-care-101/' in path or path.endswith('computer-care-101/index.html'))
    save(path, s, m, story)
    print('patched', path, len(story['passages']), 'passages')
