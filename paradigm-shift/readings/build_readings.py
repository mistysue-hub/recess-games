"""Build notebook-style reading pages (one per module, ?level=core|extended) from the course markdown."""
import markdown, re, json, html, os, glob, sys
WS='/home/claude/paradigm-shift/workspace/resources'
OUT='/home/claude/paradigm-shift/games/paradigm-shift/readings'

def render(md_text):
    h = markdown.markdown(md_text, extensions=['tables','sane_lists'])
    # Side View paragraphs -> sticky note; Anomaly paragraphs -> red ink
    h = re.sub(r'<p>Side View:\s*(.*?)</p>', r'<aside class="sticky"><span class="label">Side View</span><p>\1</p></aside>', h, flags=re.S)
    h = re.sub(r'<p>Anomaly:\s*(.*?)</p>', r'<div class="anomaly"><span class="label">Anomaly</span><p>\1</p></div>', h, flags=re.S)
    h = h.replace('<table>','<div class="tablewrap"><table>').replace('</table>','</table></div>')
    return h

PAGE='''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>__TITLE__</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Special+Elite&family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">
<style>
  :root{--paper:#fdfdf8;--grid:#d6e4f0;--margin:#e08a8a;--ink:#1f2a36;--soft:#5a6875;--red:#b3261e;--sticky:#fff2a8;--line:#c9d6e2}
  *{box-sizing:border-box}
  html,body{margin:0}
  body{background:var(--paper);background-image:linear-gradient(var(--grid) 1px,transparent 1px),linear-gradient(90deg,var(--grid) 1px,transparent 1px);
    background-size:22px 22px;color:var(--ink);font-family:"Atkinson Hyperlegible",system-ui,sans-serif;font-size:19px;line-height:1.6;min-height:100vh}
  .page{max-width:780px;margin:0 auto;padding:22px 18px 48px 52px;position:relative;min-height:100vh}
  .page::before{content:"";position:absolute;left:34px;top:0;bottom:0;width:2px;background:var(--margin)}
  .tag{font-family:"Special Elite",ui-monospace,monospace;color:var(--soft);font-size:15px;margin:0 0 6px}
  h1,h2,h3{font-family:"Special Elite",ui-monospace,monospace;font-weight:400;line-height:1.2;text-wrap:balance}
  h1{font-size:30px;margin:0 0 14px} h2{font-size:23px;margin:28px 0 6px} h3{font-size:20px;margin:22px 0 6px}
  p{margin:9px 0;max-width:66ch} li{max-width:64ch;margin:5px 0}
  ul,ol{padding-left:26px}
  strong{font-weight:700}
  hr{border:0;border-top:1px solid var(--line);margin:28px 0 8px}
  hr + p{font-size:15px;color:var(--soft)}
  .sticky{display:block;background:var(--sticky);padding:14px 16px;margin:22px 0;box-shadow:2px 3px 0 rgba(0,0,0,.12);transform:rotate(-.3deg);max-width:64ch}
  .sticky p{margin:4px 0}
  .label{display:block;font-family:"Special Elite",ui-monospace,monospace;font-size:15px;letter-spacing:.04em;margin-bottom:2px}
  .anomaly{color:var(--red);margin:18px 0}
  .anomaly p{margin:2px 0}
  .tablewrap{overflow-x:auto;margin:12px 0}
  table{border-collapse:collapse;font-size:16px;background:rgba(255,255,255,.6)}
  th,td{border:1px solid var(--line);padding:6px 10px;text-align:left;vertical-align:top}
  th{font-family:"Special Elite",ui-monospace,monospace;font-weight:400}
  .done{margin-top:26px;font-family:"Special Elite",ui-monospace,monospace;font-size:17px}
  @media (max-width:480px){ .page{padding:18px 14px 40px 40px} .page::before{left:24px} body{font-size:18px} }
  @media (prefers-reduced-motion:reduce){ .sticky{transform:none} }
</style>
</head>
<body>
<main class="page" id="page"></main>
<script>
  var LEVELS = __DATA__;
  var level = new URLSearchParams(location.search).get('level') === 'extended' ? 'extended' : 'core';
  document.getElementById('page').innerHTML =
    '<p class="tag">Lab notebook · Module __N__ · ' + (level === 'core' ? 'Core' : 'Extended') + '</p>' +
    LEVELS[level] +
    '<p class="done">Finished reading? Go back to Rocky and say <b>done</b>.</p>';
  document.title = '__TITLE__ · ' + (level === 'core' ? 'Core' : 'Extended');
</script>
</body>
</html>
'''
mods = sys.argv[1:] or ['%02d'%i for i in range(1,13)]
for n in mods:
    core=open(f'{WS}/M{n}KuhnCore.md',encoding='utf-8').read()
    ext=open(f'{WS}/M{n}KuhnExtended.md',encoding='utf-8').read()
    title=re.search(r'^# (.*)$',ext,re.M).group(1)
    data=json.dumps({'core':render(core),'extended':render(ext)},ensure_ascii=False).replace('</','<\\/')
    page=PAGE.replace('__DATA__',data).replace('__TITLE__',html.escape(title)).replace('__N__',str(int(n)))
    os.makedirs(f'{OUT}/M{n}',exist_ok=True)
    open(f'{OUT}/M{n}/index.html','w',encoding='utf-8').write(page)
    print('built',n,len(page))
