"""Build notebook-style reading pages (one per module, ?level=core|extended) from the course markdown.
Words come straight from resources/MNNKuhnCore.md and MNNKuhnExtended.md; only the presentation is added here."""
import markdown, re, json, html, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sketches import S
WS = os.environ.get('WS', '/home/claude/paradigm-shift/workspace/resources')
OUT = os.environ.get('OUT', '/home/claude/paradigm-shift/games/paradigm-shift/readings')
CAPTIONS = {'01':'a gas that made a candle flare','02':'a Leyden jar, ready to shock','03':'a comet on a long, stretched orbit',
 '04':'two cards. One of them is wrong.','05':'an orbit that doesn\'t fit','06':'a circle riding on a circle',
 '07':'two coastlines that seem to fit','08':'planet, planet, planet, not a planet?','09':'one of many drawings of the atom',
 '10':'weighing two theories','11':'this course, under the magnifying glass','12':'a map of ideas, and a compass'}

def timeline_md(md_text):
    """Within a section, if two or more paragraphs open with a bold label holding a year,
    wrap the stretch from the first of them to the last bold-led paragraph in a timeline."""
    blocks = md_text.split('\n\n')
    out, i = [], 0
    sec = []
    def flush(sec):
        lead = [k for k,b in enumerate(sec) if b.startswith('**') and not b.startswith('**Weird but true')]
        dated = [k for k in lead if re.match(r'\*\*[^*]*\d{4}[^*]*\*\*', sec[k])]
        if len(dated) < 2: return sec
        a = dated[0]; z = max(k for k in lead if k >= a)
        res = sec[:a] + ['<div class="timeline" markdown="1">']
        for k in range(a, z+1):
            b = sec[k]
            res.append(b + ('\n{: .entry }' if k in lead else '\n{: .note }'))
        res += ['</div>'] + sec[z+1:]
        return res
    for b in blocks:
        if b.startswith('#'):
            out += flush(sec); sec = []; out.append(b)
        else:
            sec.append(b)
    out += flush(sec)
    return '\n\n'.join(out)

def render(md_text):
    h = markdown.markdown(timeline_md(md_text), extensions=['tables','sane_lists','md_in_html','attr_list'])
    # Opening paragraph (first <p> after the title) becomes the lede
    h = re.sub(r'(</h1>\s*)<p>', r'\1<p class="lede">', h, count=1)
    # Weird but true -> taped index card
    h = re.sub(r'<p><strong>Weird but true:</strong>\s*(.*?)</p>', r'<aside class="card"><span class="tape"></span><p class="card-title">Weird but true</p><p>\1</p></aside>', h, flags=re.S)
    # Terms -> glossary card
    h = re.sub(r'<h2>Terms</h2>\s*(<ul>.*?</ul>)', r'<section class="glossary"><h2>Terms</h2>\1</section>', h, flags=re.S)
    # Why it matters now -> pinned clipping
    h = re.sub(r'<p>Why it matters now:\s*(.*?)</p>', r'<aside class="now"><p class="now-title">Why it matters now</p><p>\1</p></aside>', h, flags=re.S)
    # Side View -> sticky note; Anomaly -> red ink
    h = re.sub(r'<p>Side View:\s*(.*?)</p>', r'<aside class="sticky"><p class="sticky-title">Side View</p><p>\1</p></aside>', h, flags=re.S)
    h = re.sub(r'<p>Anomaly:\s*(.*?)</p>', r'<div class="anomaly"><p class="anomaly-title">Anomaly</p><p>\1</p></div>', h, flags=re.S)
    h = re.sub(r'<p>Reveal:\s*(.*?)</p>', r'<div class="answercard locked"><p class="anomaly-title">The answer</p><p>\1</p></div>', h, flags=re.S)
    h = re.sub(r'<h2>(.*?)</h2>', r'<h2><span>\1</span></h2>', h)
    h = h.replace('<table>','<div class="tablewrap"><table>').replace('</table>','</table></div>')
    return h

PAGE = r'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>__TITLE__</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Special+Elite&family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">
<style>
  :root{--paper:#fbfbf4;--grid:#d3e2ef;--margin:#e7a3a3;--ink:#1f2a36;--soft:#56636f;--pencil:#2d5f8b;--red:#b3261e;
        --sticky:#fff2a8;--hi:#ffe866;--card:#ffffff;--line:#c9d6e2;--tape:rgba(214,226,236,.85)}
  *{box-sizing:border-box}
  html,body{margin:0;overflow-x:clip}
  body{background:var(--paper);background-image:linear-gradient(var(--grid) 1px,transparent 1px),linear-gradient(90deg,var(--grid) 1px,transparent 1px);
    background-size:22px 22px;color:var(--ink);font-family:"Atkinson Hyperlegible",system-ui,sans-serif;font-size:19px;line-height:1.62}
  .page{max-width:760px;margin:0 auto;padding:22px 20px 56px 56px;position:relative;min-height:100vh}
  .page::before{content:"";position:absolute;left:36px;top:0;bottom:0;width:2px;background:var(--margin)}
  .ink-line{position:absolute;left:35px;top:0;width:4px;height:0;background:var(--red);border-radius:2px}
  .ink-line::after{content:"";position:absolute;left:-4px;bottom:-6px;width:12px;height:12px;border-radius:50%;background:var(--red)}
  .tag{font-family:"Special Elite",ui-monospace,monospace;color:var(--soft);font-size:15px;margin:0 0 10px}
  h1,h2,h3{font-family:"Special Elite",ui-monospace,monospace;font-weight:400;line-height:1.2;text-wrap:balance}
  h1{font-size:clamp(28px,6vw,38px);margin:0 0 6px}
  h2{font-size:24px;margin:34px 0 8px}
  h2 span{padding:0 6px;margin-left:-6px;-webkit-box-decoration-break:clone;box-decoration-break:clone;
     background:linear-gradient(transparent 52%,var(--hi) 52%,var(--hi) 90%,transparent 90%)}
  h3{font-size:20px;margin:24px 0 6px}
  p{margin:10px 0;max-width:64ch} li{max-width:62ch;margin:6px 0} ul,ol{padding-left:26px}
  strong{font-weight:700}
  .lede{font-size:1.18em;line-height:1.55;max-width:56ch}
  /* the taped-in sketch */
  .sketch{position:relative;margin:18px 0 20px;max-width:420px;background:var(--card);padding:14px 14px 8px;
          box-shadow:0 1px 0 var(--line),3px 5px 0 rgba(31,42,54,.08);transform:rotate(-1.2deg)}
  .sketch::before,.sketch::after{content:"";position:absolute;top:-10px;width:70px;height:22px;background:var(--tape)}
  .sketch::before{left:22px;transform:rotate(-6deg)} .sketch::after{right:22px;transform:rotate(5deg)}
  .sketch svg{display:block;width:100%;height:auto}
  .sketch svg path,.sketch svg circle,.sketch svg ellipse,.sketch svg rect{fill:none;stroke-linecap:round;stroke-linejoin:round}
  .sketch .ink{stroke:var(--ink);stroke-width:3} .sketch .red{stroke:var(--red);stroke-width:3}
  .sketch .pencil{stroke:var(--pencil);stroke-width:2;opacity:.8} .sketch .thin{stroke-width:2}
  .sketch .dash{stroke-dasharray:6 7} .sketch .fill.red{fill:var(--red)} .sketch .fill.ink,.sketch .fill.small{fill:var(--ink)}
  .sketch .pencil.fill{fill:var(--pencil)}
  .sketch figcaption{font-family:"Special Elite",ui-monospace,monospace;color:var(--pencil);font-size:15px;margin:4px 2px 2px}
  /* pencil timeline for dated history */
  .timeline{padding:0 0 0 28px;margin:16px 0;position:relative}
  .timeline::before{content:"";position:absolute;left:7px;top:12px;bottom:12px;width:2px;background:var(--pencil);opacity:.55}
  .timeline p{position:relative;margin:0 0 16px}
  .timeline .entry::before{content:"";position:absolute;left:-27px;top:7px;width:12px;height:12px;border-radius:50%;background:var(--paper);border:3px solid var(--pencil)}
  .timeline .entry > strong:first-child{display:block;font-family:"Special Elite",ui-monospace,monospace;font-weight:400;color:var(--pencil);font-size:18px}
  .timeline .note{color:var(--ink);padding:10px 14px;background:rgba(255,255,255,.7);border-radius:4px}
  /* index card */
  .card{position:relative;background:var(--card);margin:26px 0;padding:16px 18px;max-width:60ch;transform:rotate(.8deg);
        box-shadow:3px 5px 0 rgba(31,42,54,.1);background-image:linear-gradient(transparent 33px,#f2b8b8 33px,#f2b8b8 35px,transparent 35px)}
  .card .tape{position:absolute;top:-11px;left:50%;width:84px;height:22px;margin-left:-42px;background:var(--tape);transform:rotate(-3deg)}
  .card-title,.sticky-title,.anomaly-title{font-family:"Special Elite",ui-monospace,monospace;font-size:17px;margin:0 0 6px}
  .card-title{color:var(--red)}
  .now{position:relative;background:var(--card);margin:26px 0;padding:14px 18px 12px 18px;max-width:60ch;border:2px solid var(--pencil);border-radius:3px;
       transform:rotate(-.5deg);box-shadow:3px 5px 0 rgba(45,95,139,.18)}
  .now::before{content:"";position:absolute;top:-9px;left:22px;width:16px;height:16px;border-radius:50%;background:var(--red);box-shadow:0 2px 0 rgba(0,0,0,.25)}
  .now-title{font-family:"Special Elite",ui-monospace,monospace;color:var(--pencil);font-size:17px;margin:0 0 6px}
  .logbox{background:var(--card);margin:26px 0;padding:14px 16px;max-width:62ch;border:2px dashed var(--red);border-radius:4px}
  .logbox h3{margin:0 0 4px;font-size:19px;color:var(--red)}
  .logbox p{margin:4px 0;font-size:16px;color:var(--soft)}
  .logbox textarea{width:100%;min-height:96px;margin:8px 0;padding:10px;font:inherit;font-size:17px;color:var(--ink);background:var(--paper);
       border:1px solid var(--line);border-radius:4px;resize:vertical}
  .logbox textarea:focus-visible,.logbox button:focus-visible{outline:3px solid var(--pencil);outline-offset:2px}
  .logbox button{font:inherit;font-size:16px;padding:9px 14px;border-radius:6px;border:0;background:var(--red);color:#fff;cursor:pointer}
  .logbox .status{display:inline-block;margin-left:10px;font-size:15px;color:var(--pencil)}
  .logbox details{margin-top:12px} .logbox summary{cursor:pointer;font-size:16px;color:var(--pencil)}
  .logbox ol{margin:8px 0 0;padding-left:22px;font-size:16px} .logbox li{margin:6px 0}
  .logbox li b{font-family:"Special Elite",ui-monospace,monospace;font-weight:400;color:var(--red)}
  .glossary{background:var(--card);border-left:6px solid var(--pencil);padding:4px 18px 8px;margin:28px 0;box-shadow:3px 5px 0 rgba(31,42,54,.08)}
  .glossary h2{margin-top:14px}
  .sticky{display:block;background:var(--sticky);padding:16px 18px;margin:28px 0;box-shadow:3px 4px 0 rgba(0,0,0,.12);transform:rotate(-.6deg);max-width:62ch}
  .sticky p{margin:4px 0}
  .anomaly{color:var(--red);margin:24px 0;padding-left:14px;border-left:3px dashed var(--red)}
  .anomaly p{margin:3px 0}
  .anomaly.locked,.answercard.locked{display:none}
  .answercard{border:2px solid var(--ink);background:#fff;padding:12px 16px;margin:18px 0;border-radius:6px}
  .answercard p{margin:4px 0}
  .revealrow{margin-top:12px}
  .reveal{font:inherit;border:2px dashed var(--red);background:#fff;color:var(--red);padding:10px 14px;border-radius:10px;cursor:pointer;min-height:44px}
  .tick{list-style:none;padding-left:0}
  .tick li{margin:6px 0}
  .tick label{display:flex;gap:10px;align-items:flex-start;cursor:pointer}
  .tick input{width:22px;height:22px;margin-top:2px;flex:none}
  .score{font-family:"Special Elite",ui-monospace,monospace;color:var(--red);font-size:19px;margin:8px 0}
  .tablewrap{overflow-x:auto;margin:14px 0}
  table{border-collapse:collapse;font-size:16px;background:var(--card)}
  th,td{border:1px solid var(--line);padding:7px 10px;text-align:left;vertical-align:top}
  th{font-family:"Special Elite",ui-monospace,monospace;font-weight:400;color:var(--pencil)}
  hr{border:0;border-top:1px solid var(--line);margin:30px 0 8px}
  hr + p{font-size:15px;color:var(--soft)}
  .sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}
  .stamp{display:inline-block;margin:28px 0 8px;padding:10px 16px;border:3px solid var(--red);color:var(--red);border-radius:6px;
         font-family:"Special Elite",ui-monospace,monospace;font-size:18px;transform:rotate(-2deg)}
  .stamp b{font-weight:400;text-decoration:underline}
  @media (max-width:480px){ .page{padding:18px 14px 44px 42px} .page::before{left:24px} .ink-line{left:23px} body{font-size:18px} }
  @media (prefers-reduced-motion:no-preference){
    .sketch path,.sketch circle,.sketch ellipse,.sketch rect{stroke-dasharray:var(--len);stroke-dashoffset:var(--len);animation:draw 1.6s ease-out forwards}
    .sketch .dash{animation:none;stroke-dashoffset:0}
    @keyframes draw{to{stroke-dashoffset:0}}
  }
  @media (prefers-reduced-motion:reduce){ .sketch,.card,.sticky,.stamp{transform:none} }
  /* scroll motion (only when JS adds .anim, so text is never hidden without it) */
  body.anim .rv{opacity:0;translate:var(--dx,0) 18px;transition:opacity .55s ease-out,translate .75s cubic-bezier(.2,.9,.25,1.05)}
  body.anim .rv.in{opacity:1;translate:0 0}
  body.anim h2{opacity:0}
  body.anim h2.pop{opacity:1;animation:pop .55s cubic-bezier(.2,1.6,.4,1)}
  @keyframes pop{0%{scale:.4;rotate:-4deg}60%{scale:1.08;rotate:1deg}100%{scale:1;rotate:0deg}}
  .burst{position:absolute;pointer-events:none;z-index:5;width:0;height:0}
  .burst i{position:absolute;left:0;top:0;display:block;border-radius:50%}
  .burst b{position:absolute;left:-8px;top:-8px;width:16px;height:16px;border-radius:50%;border:4px solid var(--red)}
  h2{position:relative}
</style>
</head>
<body>
<main class="page" id="page"><div class="ink-line" id="ink"></div><div id="body"></div></main>
<script>
  var LEVELS = __DATA__;
  var level = new URLSearchParams(location.search).get('level') === 'extended' ? 'extended' : 'core';
  var sketch = '<figure class="sketch"><svg viewBox="0 0 320 170" role="img" aria-label="Sketch: __CAPTION__">__SVG__</svg><figcaption>Fig. __N__: __CAPTION__</figcaption></figure>';
  var body = LEVELS[level].replace(/(<\/h1>)/, '$1' + sketch);
  document.getElementById('body').innerHTML =
    '<p class="tag">Lab notebook, module __N__, ' + (level === 'core' ? 'Core' : 'Extended') + '</p>' + body +
    '<p class="stamp">Finished reading? Go back to Rocky and say <b>done</b>.</p>';
  document.title = '__TITLE__ (' + (level === 'core' ? 'Core' : 'Extended') + ')';
  // Anomaly Log box: saved only in this browser, with a Copy button for Rocky
  (function(){
    var N = '__N2__', KEY = 'paradigm-shift:anomaly-log:M';
    var store = null; try { localStorage.setItem('ps-test', '1'); localStorage.removeItem('ps-test'); store = localStorage; } catch(e) {}
    var box = document.createElement('section'); box.className = 'logbox';
    box.innerHTML = '<h3>Add to your log</h3>' +
      '<p>Jot what seemed too tidy, one-sided or left out in this module. ' + (store ? 'It stays on this device.' : 'This page can\'t save here, so copy it before you leave.') + '</p>' +
      '<label for="lg" class="sr">Anomaly Log entry for module __N__</label><textarea id="lg" placeholder="Anomaly: ..."></textarea>' +
      '<button type="button" id="cp">Copy for Rocky</button><span class="status" id="st" role="status"></span>' +
      (document.querySelector('#body .anomaly') ? '<div class="revealrow"><button type="button" id="rv" class="reveal">Now show me what the course planted</button><span class="status" id="rs" role="status"></span></div>' : '') +
      '<details id="past"><summary>Your log so far</summary><ol id="pl"></ol></details>';
    var planted = document.querySelector('#body .anomaly');
    var anchor = planted || document.querySelector('#body .stamp');
    if (planted) { planted.classList.add('locked'); anchor.parentNode.insertBefore(box, anchor); }
    else anchor.parentNode.insertBefore(box, anchor.nextSibling);
    var ta = box.querySelector('#lg'), st = box.querySelector('#st');
    if (store) { ta.value = store.getItem(KEY + N) || ''; }
    ta.addEventListener('input', function(){ if (store) { try { store.setItem(KEY + N, ta.value); st.textContent = 'Saved'; } catch(e) {} } });
    function list(){
      var pl = box.querySelector('#pl'), n = 0; pl.innerHTML = '';
      for (var i = 1; i <= 12; i++) { var k = (i < 10 ? '0' : '') + i, v = store ? store.getItem(KEY + k) : '';
        if (v && v.trim()) { var li = document.createElement('li'); li.innerHTML = '<b>Module ' + i + ':</b> '; li.appendChild(document.createTextNode(v)); pl.appendChild(li); n++; } }
      box.querySelector('#past').style.display = n ? '' : 'none';
    }
    list(); ta.addEventListener('change', list);
    var rv = box.querySelector('#rv');
    if (rv) rv.addEventListener('click', function(){
      var rs = box.querySelector('#rs');
      if (!ta.value.trim() && !rv.dataset.once) { rv.dataset.once = '1'; rs.textContent = 'Write your own guess first, even a rough one. Then tap again.'; return; }
      planted.classList.remove('locked'); planted.classList.add('in'); rv.style.display = 'none'; rs.textContent = '';
      planted.scrollIntoView({behavior:'smooth', block:'center'});
    });
    box.querySelector('#cp').addEventListener('click', function(){
      var text = 'Anomaly Log, module __N__: ' + ta.value.trim();
      function ok(){ st.textContent = 'Copied. Paste it to Rocky.'; }
      function fallback(){ var t = document.createElement('textarea'); t.value = text; document.body.appendChild(t); t.select();
        try { document.execCommand('copy'); ok(); } catch(e) { st.textContent = 'Select your note and copy it.'; } t.remove(); }
      if (!ta.value.trim()) { st.textContent = 'Write a note first, or tell Rocky "nothing this time."'; return; }
      if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(text).then(ok, fallback); else fallback();
    });
  })();
  // "Reveal:" answers stay hidden until the learner taps
  document.querySelectorAll('#body .answercard').forEach(function(card){
    var b = document.createElement('button'); b.type = 'button'; b.className = 'reveal'; b.textContent = 'I picked one. Show the answer';
    var wrap = document.createElement('div'); wrap.className = 'revealrow'; wrap.appendChild(b);
    card.parentNode.insertBefore(wrap, card);
    b.addEventListener('click', function(){ card.classList.remove('locked'); card.classList.add('in'); wrap.style.display = 'none'; });
  });
  // Module 11: tick the planted anomalies you caught
  (function(){
    if ('__N2__' !== '11') return;
    var ols = document.querySelectorAll('#body ol'), ol = null;
    ols.forEach(function(o){ if (o.children.length === 10) ol = o; });
    if (!ol) return;
    ol.classList.add('tick');
    var score = document.createElement('p'); score.className = 'score'; score.setAttribute('role', 'status');
    ol.parentNode.insertBefore(score, ol);
    function upd(){ score.textContent = 'You caught ' + ol.querySelectorAll('input:checked').length + ' of 10'; }
    Array.prototype.forEach.call(ol.children, function(li, i){
      var lab = document.createElement('label'), cb = document.createElement('input'), sp = document.createElement('span');
      cb.type = 'checkbox'; cb.setAttribute('aria-label', 'I caught number ' + (i + 1)); sp.innerHTML = li.innerHTML;
      lab.appendChild(cb); lab.appendChild(sp); li.innerHTML = ''; li.appendChild(lab); cb.addEventListener('change', upd);
    });
    upd();
  })();
  // stagger the sketch strokes so the drawing inks in once
  var parts = document.querySelectorAll('.sketch svg *');
  parts.forEach(function(el, i){ try{ var L = Math.ceil(el.getTotalLength()); el.style.setProperty('--len', L); el.style.animationDelay = (i * 0.12) + 's'; }catch(e){} });
  // the margin line fills with ink as you read
  var page = document.getElementById('page'), ink = document.getElementById('ink');
  function fill(){ var max = document.documentElement.scrollHeight - innerHeight;
    var f = max > 0 ? Math.min(1, scrollY / max) : 1; ink.style.height = (f * page.offsetHeight) + 'px'; }
  addEventListener('scroll', fill, {passive:true}); addEventListener('resize', fill); fill();
  // motion (Core only; Extended keeps the self-inking sketch and the margin line): paragraphs slide in from alternating sides; each section heading explodes into view
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  var calm = level === 'extended';
  if (!reduce && !calm && 'IntersectionObserver' in window && document.body.animate) {
    document.body.classList.add('anim');
    var root = document.getElementById('body');
    var blocks = root.querySelectorAll(':scope > p:not(.tag), :scope > ul > li, :scope > ol > li, :scope > aside, :scope > .anomaly, :scope > .answercard, :scope > .tablewrap, :scope > .stamp, :scope > .logbox, .timeline > p, .glossary li');
    blocks.forEach(function(el, i){
      el.classList.add('rv');
      var fromLeft = el.parentNode.classList && el.parentNode.classList.contains('timeline') ? true : (i % 2 === 0);
      el.style.setProperty('--dx', (fromLeft ? -46 : 46) + 'px');
    });
    var colors = ['#b3261e', '#2d5f8b', '#ffd400', '#1f2a36', '#e7a3a3'];
    var nBursts = 0;
    function burst(h){
      var sc = nBursts++ === 0 ? 1 : 0.7;
      var box = document.createElement('span'); box.className = 'burst';
      box.style.left = Math.min(h.offsetWidth * 0.45, 200) + 'px'; box.style.top = (h.offsetHeight / 2) + 'px'; h.appendChild(box);
      var ring = document.createElement('b'); box.appendChild(ring);
      ring.animate([{transform:'scale(.2)', opacity:1}, {transform:'scale(' + (12 * sc) + ')', opacity:0}], {duration:800, easing:'ease-out'});
      for (var k = 0; k < Math.round(34 * sc); k++) {
        var d = document.createElement('i'), size = (7 + Math.random() * 10) * sc, ang = Math.random() * Math.PI * 2, dist = (70 + Math.random() * 150) * sc;
        d.style.width = d.style.height = size + 'px'; d.style.background = colors[k % colors.length];
        d.style.marginLeft = d.style.marginTop = (-size / 2) + 'px'; box.appendChild(d);
        d.animate([{transform:'translate(0,0) scale(1.3)', opacity:1}, {opacity:1, offset:.6},
                   {transform:'translate(' + Math.cos(ang) * dist * 1.6 + 'px,' + Math.sin(ang) * dist * .7 + 'px) scale(0)', opacity:0}],
                  {duration:950 + Math.random() * 600, easing:'cubic-bezier(.1,.75,.3,1)', fill:'forwards'});
      }
      setTimeout(function(){ box.remove(); }, 1700);
    }
    var io = new IntersectionObserver(function(entries){
      entries.forEach(function(e){
        if (!e.isIntersecting) return;
        var el = e.target; io.unobserve(el);
        if (el.tagName === 'H2') { el.classList.add('pop'); burst(el); }
        else { el.classList.add('in'); }
      });
    }, {threshold: 0.12, rootMargin: '0px 0px -6% 0px'});
    root.querySelectorAll('h2').forEach(function(h){ io.observe(h); });
    blocks.forEach(function(el){ io.observe(el); });
  }
</script>
</body>
</html>
'''
mods = sys.argv[1:] or ['%02d'%i for i in range(1,13)]
for n in mods:
    core = open(f'{WS}/M{n}KuhnCore.md', encoding='utf-8').read()
    ext = open(f'{WS}/M{n}KuhnExtended.md', encoding='utf-8').read()
    title = re.search(r'^# (.*)$', ext, re.M).group(1)
    data = json.dumps({'core': render(core), 'extended': render(ext)}, ensure_ascii=False).replace('</', '<\\/')
    svg = S[n].replace('\n', '').replace("'", "\\'")
    page = (PAGE.replace('__DATA__', data).replace('__SVG__', svg).replace('__CAPTION__', html.escape(CAPTIONS[n]).replace("'", "\\'"))
                .replace('__TITLE__', html.escape(title)).replace('__N__', str(int(n))).replace('__N2__', n))
    os.makedirs(f'{OUT}/M{n}', exist_ok=True)
    open(f'{OUT}/M{n}/index.html', 'w', encoding='utf-8').write(page)
    print('built', n, len(page))
