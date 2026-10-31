"""Build Faraday's-lab-diary reading pages, one per module, from resources/MNNFaraday.md.
Words come straight from the markdown; only the presentation is added here."""
import markdown, re, os, sys
WS = os.environ.get('WS', '/home/claude/faraday/workspace/resources')
OUT = os.environ.get('OUT', os.path.dirname(os.path.abspath(__file__)))
START = {}  # running paragraph count across the course, like Faraday's diary (filled in below)
DATES = {'01': 'Entry for the apprentice. Royal Institution, basement laboratory.',
         '02': 'Entry for the apprentice. On lines of force.',
         '03': 'Entry for the apprentice. 3 September 1821, by candlelight.',
         '04': 'Entry for the apprentice. 29 August 1831. New notebook.',
         '05': 'Entry for the apprentice. On the copper disk.',
         '06': 'Entry for the apprentice. Chemistry, and some new words.',
         '07': 'Entry for the apprentice. January 1836, inside the cube.',
         '08': 'Entry for the apprentice. 13 September 1845. Last page but one.'}
SKETCH = {
'01': ('a candle: the flame never touches the wax', '''<svg viewBox="0 0 260 200" aria-hidden="true">
<path class="ink" d="M100 190 L160 190 L158 96 Q130 88 102 96 Z"/>
<path class="ink thin" d="M110 110 q20 -8 40 0 M110 130 q20 6 40 0"/>
<path class="ink thin" d="M130 96 V72"/>
<path class="ink" d="M130 20 q-26 30 -12 50 q12 12 24 0 q14 -20 -12 -50 Z"/>
<path class="pencil" d="M130 42 q-9 14 -4 24 q4 6 8 0 q5 -10 -4 -24 Z"/>
<path class="pencil dash" d="M100 72 q30 -14 60 0"/>
<text x="178" y="70" class="label">vapor?</text>
<text x="178" y="100" class="label">cup</text>
<path class="pencil thin" d="M175 96 L160 104"/>
</svg>'''),
'02': ('iron filings over a magnet: the lines', '''<svg viewBox="0 0 260 200" aria-hidden="true">
<rect class="ink" x="80" y="88" width="100" height="26" rx="3"/>
<path class="ink thin" d="M130 88 V114"/>
<text x="92" y="107" class="label">N</text><text x="152" y="107" class="label">S</text>
<path class="pencil" d="M80 100 C 20 60, 20 20, 130 24 C 240 20, 240 60, 180 100"/>
<path class="pencil" d="M80 100 C 40 80, 60 50, 130 48 C 200 50, 220 80, 180 100"/>
<path class="pencil" d="M80 100 C 20 140, 20 180, 130 176 C 240 180, 240 140, 180 100"/>
<path class="pencil" d="M80 100 C 40 120, 60 150, 130 152 C 200 150, 220 120, 180 100"/>
<path class="red" d="M56 70 l10 -4 l-2 10"/>
<path class="red" d="M204 130 l-10 4 l2 -10"/>
<text x="196" y="40" class="label">real?</text>
</svg>'''),
'03': ('the wire goes round the magnet', '''<svg viewBox="0 0 260 200" aria-hidden="true">
<path class="ink" d="M60 150 q70 24 140 0 v26 q-70 24 -140 0 Z"/>
<path class="pencil" d="M60 150 q70 -24 140 0"/>
<rect class="ink" x="120" y="92" width="18" height="62" rx="2"/><text x="123" y="107" class="label">N</text>
<path class="ink" d="M60 30 h80 q8 0 8 8 v10 q0 6 6 6 h20 v100 l10 8"/>
<path class="pencil dash" d="M100 118 a40 20 0 1 0 60 0"/>
<path class="red" d="M160 118 l-6 -8 l-8 6"/>
<text x="150" y="52" class="label">round &amp; round</text>
</svg>'''),
'04': ('the iron ring, two coils, one jump', '''<svg viewBox="0 0 260 200" aria-hidden="true">
<circle class="ink" cx="130" cy="100" r="58"/><circle class="ink" cx="130" cy="100" r="36"/>
<path class="pencil" d="M72 80 q12 4 0 8 q12 4 0 8 q12 4 0 8 q12 4 0 8 q12 4 0 8 M70 76 h-30 M70 122 h-30"/>
<path class="pencil" d="M188 80 q-12 4 0 8 q-12 4 0 8 q-12 4 0 8 q-12 4 0 8 q-12 4 0 8 M190 76 h30 M190 122 h30"/>
<path class="ink thin" d="M20 60 v36 M34 70 v16"/><text x="8" y="52" class="label">battery</text>
<path class="ink thin" d="M230 88 l12 -22 l12 22" /><path class="red" d="M242 66 l10 -14"/><text x="206" y="56" class="label">jump!</text>
</svg>'''),
'05': ('a copper disk between the poles', '''<svg viewBox="0 0 260 200" aria-hidden="true">
<ellipse class="ink" cx="130" cy="100" rx="22" ry="70"/><path class="ink thin" d="M130 30 v140"/>
<path class="ink" d="M30 60 h60 v24 h-44 v32 h44 v24 h-60 Z"/><text x="44" y="76" class="label">N</text><text x="44" y="134" class="label">S</text>
<path class="pencil dash" d="M92 72 h28 M92 100 h28 M92 128 h28"/>
<path class="ink thin" d="M152 100 h40 M130 170 h62 v-70"/><path class="red" d="M200 96 l20 4 l-20 4"/>
<text x="178" y="60" class="label">crank it</text>
<path class="pencil" d="M130 30 a18 18 0 1 1 -14 10"/>
</svg>'''),
'06': ('two rods in water: twice the bubbles on one side', '''<svg viewBox="0 0 260 200" aria-hidden="true">
<path class="ink" d="M40 60 v120 h180 v-120"/><path class="pencil" d="M40 96 h180"/>
<rect class="ink thin" x="80" y="40" width="22" height="110"/><rect class="ink thin" x="158" y="40" width="22" height="110"/>
<path class="ink" d="M91 150 v24 M169 150 v24"/>
<path class="pencil" d="M80 112 h22 M158 72 h22"/>
<circle class="pencil" cx="88" cy="130" r="3"/><circle class="pencil" cx="95" cy="140" r="3"/><circle class="pencil" cx="86" cy="118" r="2"/>
<circle class="pencil" cx="165" cy="128" r="3"/><circle class="pencil" cx="172" cy="138" r="3"/><circle class="pencil" cx="168" cy="110" r="3"/><circle class="pencil" cx="163" cy="92" r="3"/><circle class="pencil" cx="174" cy="82" r="2"/>
<text x="70" y="30" class="label">+</text><text x="162" y="30" class="label">&#8211;</text>
<text x="190" y="60" class="label">2:1</text>
</svg>'''),
'07': ('lines of force stop at the box', '''<svg viewBox="0 0 260 200" aria-hidden="true">
<rect class="ink" x="90" y="60" width="80" height="80"/>
<path class="pencil" d="M10 70 h78 M10 100 h78 M10 130 h78 M172 70 h78 M172 100 h78 M172 130 h78"/>
<path class="pencil" d="M80 70 l8 0 l-5 -4 M80 100 l8 0 l-5 -4 M80 130 l8 0 l-5 -4 M242 70 l8 0 l-5 -4 M242 100 l8 0 l-5 -4 M242 130 l8 0 l-5 -4"/>
<text x="110" y="105" class="label">quiet</text>
<text x="96" y="52" class="label">&#8211; &#8211; &#8211;</text><text x="152" y="52" class="label">+ + +</text>
<path class="red" d="M30 170 q100 -10 200 0"/><text x="80" y="190" class="label">no trace inside</text>
</svg>'''),
'08': ('two filters, a glass rod, and a magnet', '''<svg viewBox="0 0 260 200" aria-hidden="true">
<rect class="ink" x="40" y="60" width="14" height="80"/><path class="ink thin" d="M47 66 v68"/>
<rect class="ink" x="206" y="60" width="14" height="80"/><path class="ink thin" d="M206 100 h14"/>
<rect class="ink" x="90" y="84" width="90" height="32" rx="4"/>
<path class="pencil" d="M96 80 q0 -10 10 -10 h68 q10 0 10 10 M96 120 q0 10 10 10 h68 q10 0 10 -10"/>
<path class="pencil dash" d="M10 100 h30"/><path class="pencil" d="M54 100 h36 M180 100 h26"/>
<path class="red" d="M120 100 q15 -14 30 0 q15 14 30 0"/>
<path class="pencil dash" d="M220 100 h30"/><path class="pencil" d="M244 96 l8 4 l-8 4"/>
<text x="92" y="150" class="label">magnet on: light!</text>
</svg>'''),
}

def render(md_text):
    h = markdown.markdown(md_text, extensions=['tables','sane_lists'])
    h = re.sub(r'(</h1>\s*)<p>', r'\1<p class="lede">', h, count=1)
    h = re.sub(r'<p><strong>Weird but true:</strong>\s*(.*?)</p>', r'<aside class="card"><span class="tape"></span><p class="card-title">Weird but true</p><p>\1</p></aside>', h, flags=re.S)
    h = re.sub(r'<p>Reveal:\s*(.*?)</p>', r'<div class="answercard locked"><p>\1</p></div>', h, flags=re.S)
    h = re.sub(r'<p>Verdict:\s*(.*?)</p>', r'<p class="verdict"><span class="stamp">Verdict: \1</span></p>', h, flags=re.S)
    h = re.sub(r'<h2>Words for your diary</h2>\s*(<ul>.*?</ul>)', r'<section class="glossary"><h2><span>Words for your diary</span></h2>\1</section>', h, flags=re.S)
    h = re.sub(r'<h2>(?!<span>)(.*?)</h2>', r'<h2><span>\1</span></h2>', h)
    return h

PAGE = r'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>__TITLE__</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=IM+Fell+English:ital@0;1&family=Lora:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">
<style>
  :root{--paper:#f3ead3;--laid:rgba(120,90,40,.08);--ink:#3a2412;--brown:#6b3f1a;--soft:#7a5a3a;--pencil:#5a4632;--red:#8a2f1f;
        --card:#fbf5e4;--line:#d6c6a0;--tape:rgba(230,215,170,.9);--stampink:#7a3b1c}
  *{box-sizing:border-box}
  html,body{margin:0;overflow-x:clip}
  body{background:var(--paper);
    background-image:repeating-linear-gradient(0deg,transparent 0 3px,var(--laid) 3px 4px),
      radial-gradient(ellipse at 20% 0%,rgba(255,250,235,.7),transparent 60%),
      radial-gradient(ellipse at 100% 100%,rgba(120,80,30,.12),transparent 55%);
    color:var(--ink);font-family:"Lora",Georgia,serif;font-size:19px;line-height:1.66}
  .page{max-width:760px;margin:0 auto;padding:26px 22px 60px 72px;position:relative;min-height:100vh;counter-reset:para __START__}
  .page::before{content:"";position:absolute;left:52px;top:0;bottom:0;width:1px;background:var(--brown);opacity:.35}
  .tag{font-family:"IM Fell English",Georgia,serif;font-style:italic;color:var(--soft);font-size:16px;margin:0 0 10px}
  h1,h2,h3{font-family:"IM Fell English",Georgia,serif;font-weight:400;line-height:1.15;color:var(--brown);text-wrap:balance}
  h1{font-size:clamp(30px,6.5vw,42px);margin:0 0 8px}
  h2{font-size:26px;margin:36px 0 8px}
  h2 span{border-bottom:2px solid var(--brown);padding-bottom:2px}
  p{margin:11px 0;max-width:62ch;position:relative} li{max-width:60ch;margin:6px 0} ul,ol{padding-left:26px}
  .page > p:not(.verdict):not(.tag):not(.colophon)::before{counter-increment:para;content:counter(para);position:absolute;left:-44px;top:3px;
     font-family:"IM Fell English",Georgia,serif;font-size:15px;color:var(--soft);width:34px;text-align:right}
  .lede{font-size:1.16em;line-height:1.55;max-width:56ch;font-style:italic}
  strong{font-weight:700;color:var(--brown)}
  .sketch{position:relative;margin:18px 0 22px;max-width:380px;background:var(--card);padding:14px 14px 6px;
          box-shadow:0 1px 0 var(--line),3px 5px 0 rgba(58,36,18,.12);transform:rotate(-1.6deg)}
  .sketch::before,.sketch::after{content:"";position:absolute;top:-10px;width:70px;height:22px;background:var(--tape)}
  .sketch::before{left:22px;transform:rotate(-6deg)} .sketch::after{right:22px;transform:rotate(5deg)}
  .sketch svg{display:block;width:100%;height:auto}
  .sketch svg path,.sketch svg rect{fill:none;stroke-linecap:round;stroke-linejoin:round}
  .sketch .ink{stroke:var(--ink);stroke-width:3} .sketch .thin{stroke-width:2}
  .sketch .pencil{stroke:var(--pencil);stroke-width:2;opacity:.85} .sketch .dash{stroke-dasharray:5 7}
  .sketch .red{stroke:var(--red);stroke-width:3}
  .sketch .label{font-family:"IM Fell English",Georgia,serif;font-size:15px;fill:var(--pencil)}
  .sketch figcaption{font-family:"IM Fell English",Georgia,serif;font-style:italic;color:var(--pencil);font-size:15px;margin:4px 2px 2px}
  .card{position:relative;background:var(--card);margin:28px 0;padding:16px 18px;max-width:60ch;transform:rotate(.8deg);
        box-shadow:3px 5px 0 rgba(58,36,18,.12);background-image:linear-gradient(transparent 44px,#dcbfae 44px,#dcbfae 46px,transparent 46px)}
  .card .tape{position:absolute;top:-11px;left:50%;width:84px;height:22px;margin-left:-42px;background:var(--tape);transform:rotate(-3deg)}
  .card p::before{content:none}
  .card-title{font-family:"IM Fell English",Georgia,serif;color:var(--red);font-size:18px;margin:0 0 10px;line-height:1.1}
  .answercard{margin:16px 0 22px;max-width:60ch}
  .answercard.locked > p{display:none}
  .answercard p{background:var(--card);border:1px solid var(--line);border-left:5px solid var(--brown);padding:12px 16px;margin:0}
  .answercard p::before{content:none}
  .answercard button{font:inherit;font-family:"IM Fell English",Georgia,serif;font-size:17px;padding:8px 14px;border-radius:4px;border:1px solid var(--brown);
     background:var(--card);color:var(--brown);cursor:pointer;box-shadow:2px 3px 0 rgba(58,36,18,.15)}
  .answercard button:focus-visible{outline:3px solid var(--red);outline-offset:2px}
  .answercard .note{display:block;font-size:15px;color:var(--soft);margin:6px 0 0;font-style:italic}
  .verdict{margin:26px 0 10px}
  .stamp{display:inline-block;padding:9px 16px;border:3px double var(--stampink);color:var(--stampink);border-radius:4px;
         font-family:"IM Fell English",Georgia,serif;font-size:19px;transform:rotate(-2.5deg);letter-spacing:.02em;opacity:.9}
  .glossary{background:var(--card);border-left:6px solid var(--brown);padding:4px 18px 10px;margin:30px 0;box-shadow:3px 5px 0 rgba(58,36,18,.1)}
  .glossary h2{margin-top:14px}
  .glossary p::before{content:none}
  hr{border:0;border-top:1px solid var(--line);margin:30px 0 8px}
  .colophon{font-size:15px;color:var(--soft);font-style:italic}
  .colophon::before{content:none !important}
  @media (max-width:480px){ .page{padding:18px 14px 44px 50px} .page::before{left:36px} .page > p::before{left:-38px;width:30px} body{font-size:18px} }
  @media (prefers-reduced-motion:reduce){ .sketch,.card,.stamp{transform:none} }
</style>
</head>
<body>
<main class="page">
<p class="tag">Faraday's Basement Lab · __DATE__</p>
__BODY__
<hr>
<p class="colophon">Written for this course. No material was copied. Short quotations in quotation marks are Faraday's own words from the 1800s, now public domain. The paragraph numbers are the apprentice's; Mr. Faraday didn't start counting until 29 August 1831.</p>
</main>
<script>
(function(){
  var cards=document.querySelectorAll('.answercard.locked');
  cards.forEach(function(c){
    var b=document.createElement('button'); b.type='button'; b.textContent='Show the answer';
    var n=document.createElement('span'); n.className='note'; n.textContent='Decide your answer first. Then look.';
    b.addEventListener('click',function(){ c.classList.remove('locked'); b.remove(); n.remove(); c.querySelector('p').setAttribute('tabindex','-1'); c.querySelector('p').focus(); });
    c.appendChild(b); c.appendChild(n);
  });
})();
</script>
</body>
</html>
'''

def build(nn):
    md = open(os.path.join(WS, f'M{nn}Faraday.md'), encoding='utf-8').read()
    title = re.match(r'# (.*)', md).group(1)
    body = render(md)
    cap, svg = SKETCH[nn]
    fig = f'<figure class="sketch">{svg}<figcaption>{cap}</figcaption></figure>'
    body = re.sub(r'(<p class="lede">.*?</p>)', r'\1' + fig.replace('\\', '\\\\'), body, count=1, flags=re.S)
    page = PAGE.replace('__TITLE__', f'{title} · Faraday\'s Basement Lab').replace('__BODY__', body) \
               .replace('__START__', str(START[nn]-1)).replace('__DATE__', DATES[nn])
    d = os.path.join(OUT, f'M{nn}'); os.makedirs(d, exist_ok=True)
    open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(page)
    print('built', d, len(page))

def count_numbered(nn):
    html = render(open(os.path.join(WS, f'M{nn}Faraday.md'), encoding='utf-8').read())
    # numbered = top-level <p> that are not inside cards/answercards/glossary/verdict
    stripped = re.sub(r'<aside.*?</aside>|<div class="answercard.*?</div>|<section class="glossary">.*?</section>', '', html, flags=re.S)
    return len(re.findall(r'<p(?: class="lede")?>', stripped))

if __name__ == '__main__':
    n = 1
    for nn in sorted(DATES):
        START[nn] = n
        n += count_numbered(nn)
    for nn in (sys.argv[1:] or sorted(DATES)):
        build(nn)
