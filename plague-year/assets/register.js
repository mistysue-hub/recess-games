/* The Plague Year — shared page behaviour
   seals, choices, autosave/restore, progress bar, checkpoints, glosses, route chart,
   Evidence Locker, Questions for later, and the copy-for-Rocky box. */
(function(){
  const PY = window.PY = window.PY || {};
  const MOD = document.body.dataset.mod;            // e.g. "M01"
  const ORDER=['M01','M02','M03','M04','M05','M06','M07','M08'];
  const ROMAN={M01:'I',M02:'II',M03:'III',M04:'IV',M05:'V',M06:'VI',M07:'VII',M08:'VIII'};
  const answers = new Map();                         // key -> {label, value}
  const store = {
    get(k){ try{ return JSON.parse(localStorage.getItem(k)||'null'); }catch(e){ return null; } },
    set(k,v){ try{ localStorage.setItem(k,JSON.stringify(v)); }catch(e){} },
    del(k){ try{ localStorage.removeItem(k); }catch(e){} }
  };
  PY.store = store;
  const SKEY='plagueYear:'+MOD;
  const state = { opened:[], chunks:[], deeper:[], flags:[] };
  let restoring=false;
  function save(){ if(restoring||!MOD||MOD==='INDEX') return;
    const a={}; answers.forEach((v,k)=>a[k]=v);
    store.set(SKEY,{answers:a,opened:state.opened,chunks:state.chunks,deeper:state.deeper,flags:state.flags}); }

  PY.record = function(key, label, value){ answers.set(key,{label,value}); save(); refreshAll(); };
  PY.get = k => answers.has(k) ? answers.get(k).value : null;
  PY.unrecord = k => { if(answers.has(k)){ answers.delete(k); save(); refreshAll(); } };
  PY.flag = k => { if(!state.flags.includes(k)){ state.flags.push(k); save(); } };
  PY.hasFlag = k => state.flags.includes(k);

  /* ---------- the notary's signum ---------- */
  const SIGNUM='<svg viewBox="0 0 60 76" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">'+
    '<path d="M30 3v9M25 7.5h10"/>'+
    '<circle cx="30" cy="22" r="7"/><circle cx="22" cy="30" r="7"/><circle cx="38" cy="30" r="7"/><circle cx="30" cy="38" r="7"/>'+
    '<path d="M30 15v30M23 30h14"/>'+
    '<path d="M30 45v12"/><path d="M22 57h16v5H22zM16 62h28v5H16zM10 67h40v5H10z"/>'+
    '<path d="M6 40c-3-8 0-16 6-20M54 40c3-8 0-16-6-20" stroke-width="1.6"/>'+
    '</svg>';
  PY.SIGNUM=SIGNUM;
  document.querySelectorAll('.signum').forEach(el=>{ el.innerHTML=SIGNUM; el.style.color='#2a1f16'; });
  (function(){ const pg=document.querySelector('main.page'); if(!pg) return;   // torn right and bottom edges
    let seed=7; const r=()=>{seed=(seed*9301+49297)%233280; return seed/233280;};
    const pts=['0 0'];
    for(let i=0;i<=40;i++){ pts.push(`calc(100% - ${(r()*4).toFixed(1)}px) ${(i*2.5).toFixed(1)}%`); }
    for(let i=40;i>=0;i--){ pts.push(`${(i*2.5).toFixed(1)}% calc(100% - ${(r()*5).toFixed(1)}px)`); }
    pts.push('0 100%');
    pg.style.clipPath='polygon('+pts.join(',')+')';
  })();

  /* ---------- what counts as an answer ---------- */
  function fieldFor(k){ return document.querySelector('textarea[data-key="'+k+'"],input[data-key="'+k+'"]'); }
  function words(v){ return String(v||'').trim().split(/\s+/).filter(w=>/[A-Za-z0-9À-ÿ]/.test(w)).length; }
  function minWords(k){ const f=fieldFor(k); if(!f) return 0; return parseInt(f.dataset.minwords||'3',10); }
  function valid(k){ const v=PY.get(k); if(!v) return false; const m=minWords(k); return m? words(v)>=m : String(v).length>=1; }
  PY.valid=valid;

  /* ---------- single-choice option groups ---------- */
  function bindGroup(g){
    if(g.dataset.bound) return; g.dataset.bound='1';
    const key=g.dataset.key, label=g.dataset.label||key;
    g.querySelectorAll('.opt').forEach(b=>b.addEventListener('click',()=>{
      if(g.dataset.locked==='1') return;
      g.querySelectorAll('.opt').forEach(x=>x.classList.remove('chosen'));
      b.classList.add('chosen');
      PY.record(key,label,b.dataset.val||b.textContent.trim());
      g.dispatchEvent(new CustomEvent('chosen',{detail:b.dataset.val||b.textContent.trim()}));
    }));
  }
  document.querySelectorAll('.opts[data-key]').forEach(bindGroup);
  PY.bindGroup=bindGroup;

  /* ---------- free text fields ---------- */
  document.querySelectorAll('textarea[data-key],input[data-key]').forEach(f=>{
    f.addEventListener('input',()=>{ const v=f.value.trim(); if(v) PY.record(f.dataset.key,f.dataset.label||f.dataset.key,v); else {answers.delete(f.dataset.key); save(); refreshAll();} });
  });

  /* ---------- wax seals: open only after the learner commits ---------- */
  const seals=[...document.querySelectorAll('button.seal')];
  seals.forEach((s,i)=>{ s.dataset.sid=String(i); s.innerHTML='<span class="wax" style="color:#f3c7c0">'+SIGNUM+'</span><span class="lbl"></span>'; });
  function needsOf(s){ return (s.dataset.needs||'').split(',').map(x=>x.trim()).filter(Boolean); }
  function updateSeals(){
    seals.forEach(s=>{
      if(s.dataset.opened) return;
      const need=needsOf(s), ok=need.every(valid);
      s.disabled=!ok;
      const short=need.find(k=>PY.get(k)&&!valid(k));
      const l=s.querySelector('.lbl');
      if(l) l.textContent = ok ? (s.dataset.go||'Break the seal') : (short ? 'Add a bit more: at least '+minWords(short)+' words' : (s.dataset.wait||'Write or pick your answer first'));
    });
  }
  PY.updateSeals = updateSeals;
  function lockKey(k){
    const g=document.querySelector('.opts[data-key="'+k+'"]'); if(g){g.dataset.locked='1'; g.querySelectorAll('.opt').forEach(b=>b.disabled=true);}
    const f=fieldFor(k); if(f) f.readOnly=true;
  }
  function openSeal(s){
    const tgt=document.getElementById(s.dataset.target); if(tgt) tgt.classList.add('open');
    s.dataset.opened='1'; s.disabled=true; s.querySelector('.lbl').textContent='Seal broken';
    ['hook',...(s.dataset.lock||'').split(',')].filter(Boolean).forEach(lockKey);
    if(s.dataset.opens){ const c=document.getElementById(s.dataset.opens); if(c) c.classList.add('open'); }
    if(!state.opened.includes(s.dataset.sid)) state.opened.push(s.dataset.sid);
    s.dispatchEvent(new CustomEvent('broken'));
  }
  seals.forEach(s=>s.addEventListener('click',()=>{ if(s.disabled) return; openSeal(s); save(); refreshAll(); }));

  /* ---------- "Back to Rocky" checkpoints ---------- */
  document.querySelectorAll('.checkpoint').forEach(cp=>{
    cp.insertAdjacentHTML('beforeend','<p><button type="button" class="opt cp-copy">Copy my answers so far</button> <button type="button" class="opt cp-go">I\'ve checked in with Rocky: continue</button></p>');
    cp.querySelector('.cp-copy').addEventListener('click',e=>doCopy(e.target,'Copy my answers so far'));
    cp.querySelector('.cp-go').addEventListener('click',()=>{ const c=document.getElementById(cp.dataset.opens); if(c){ c.classList.add('open'); if(!state.chunks.includes(c.id)) state.chunks.push(c.id); save(); refreshAll(); }
      cp.querySelector('.cp-go').disabled=true; cp.querySelector('.cp-go').textContent='Continued ✓'; });
  });

  /* ---------- glosses (tap a dotted word) ---------- */
  document.querySelectorAll('.gloss[data-g]').forEach(g=>{
    g.setAttribute('tabindex','0'); g.setAttribute('role','button'); g.setAttribute('aria-label',g.textContent+': '+g.dataset.g);
    const show=()=>{ const open=g.querySelector('.gtip'); if(open){ open.remove(); return; }
      document.querySelectorAll('.gtip').forEach(t=>t.remove());
      const t=document.createElement('span'); t.className='gtip'; t.textContent=g.dataset.g; g.appendChild(t); };
    g.addEventListener('click',show); g.addEventListener('keydown',e=>{ if(e.key==='Enter'||e.key===' '){ e.preventDefault(); show(); } });
  });

  /* ---------- Deeper seals: record when opened ---------- */
  document.querySelectorAll('details.deeper').forEach(d=>{
    d.addEventListener('toggle',()=>{ if(d.open){ const t=d.querySelector('summary').textContent.replace(/\s+/g,' ').trim();
      if(!state.deeper.includes(t)){ state.deeper.push(t); save(); refreshAll(); } } });
  });

  /* ---------- route chart ---------- */
  const STOPS=[
    {n:0,name:'Chüy valley (Kyrgyzstan)',lat:42.8,lon:75.3,when:'1338–39',mod:'M01',far:true,lab:[-10,-10,'end']},
    {n:1,name:'Caffa',lat:45.03,lon:35.38,when:'1346',mod:'M01',from:0,lab:[-10,-10,'end']},
    {n:2,name:'Constantinople',lat:41.0,lon:28.97,when:'1347',mod:'M01',from:1,lab:[10,14,'start']},
    {n:3,name:'Messina',lat:38.19,lon:15.55,when:'Oct 1347',mod:'M02',from:2,lab:[10,14,'start']},
    {n:4,name:'Marseille',lat:43.3,lon:5.37,when:'Nov 1347',mod:'M02',from:3,lab:[-10,16,'end']},
    {n:5,name:'Genoa',lat:44.4,lon:8.93,when:'winter 1347–48',mod:'M02',from:3,lab:[-6,-20,'end']},
    {n:6,name:'Florence',lat:43.77,lon:11.25,when:'Mar 1348',mod:'M02',from:5,lab:[12,4,'start']},
    {n:7,name:'Pistoia',lat:43.93,lon:10.91,when:'spring 1348',mod:'M03',from:6,lab:[4,-22,'start']},
    {n:8,name:'Strasbourg',lat:48.58,lon:7.75,when:'1349',mod:'M04',from:4,lab:[10,-10,'start']},
    {n:9,name:'Ragusa (later, 1377)',lat:42.65,lon:18.09,when:'1377',mod:'M05',later:true,lab:[10,4,'start']},
    {n:10,name:'Givry',lat:46.78,lon:4.75,when:'Aug–Nov 1348',mod:'M06',from:4,lab:[-10,0,'end']},
    {n:11,name:'Siena',lat:43.32,lon:11.33,when:'1348',mod:'M06',from:6,lab:[12,22,'start']},
    {n:12,name:'Melcombe (England)',lat:50.61,lon:-2.45,when:'June 1348',mod:'M07',from:4,lab:[10,-10,'start']},
    {n:13,name:'Paris',lat:48.86,lon:2.35,when:'summer 1348',mod:'M07',from:4,lab:[10,4,'start']},
    {n:14,name:'Aleppo',lat:36.2,lon:37.16,when:'1348–49',mod:'M08',from:2,lab:[-10,-8,'end']},
    {n:15,name:'Bergen',lat:60.39,lon:5.32,when:'summer 1349',mod:'M08',from:12,lab:[10,-4,'start']},
    {n:16,name:'Pskov & Novgorod',lat:58.2,lon:29.8,when:'1352',mod:'M08',from:15,lab:[10,-6,'start']},
    {n:17,name:'Moscow',lat:55.75,lon:37.62,when:'1353',mod:'M08',from:16,lab:[-10,18,'end']}
  ];
  PY.STOPS=STOPS;
  const W=800,H=520;
  function xy(s){ if(s.far) return [760,(62-s.lat)/28*480+20]; return [(s.lon+8)/50*740+20,(62-s.lat)/28*480+20]; }
  function drawMap(el,showMods,highlightMod){
    const shown=STOPS.filter(s=>showMods.includes(s.mod));
    const narrow=(el.clientWidth||800)<520, k=narrow?1.8:1;
    let g='';
    const cx=130,cy=420;
    for(let a=0;a<16;a++){const r=a*Math.PI/8;g+=`<line x1="${cx}" y1="${cy}" x2="${cx+900*Math.cos(r)}" y2="${cy+900*Math.sin(r)}" stroke="#c9b48e" stroke-width="0.6" opacity=".55"/>`;}
    g+=`<circle cx="${cx}" cy="${cy}" r="26" fill="none" stroke="#9b1c1c" stroke-width="1.2"/><path d="M${cx} ${cy-34} L${cx+6} ${cy} L${cx} ${cy+34} L${cx-6} ${cy} Z" fill="#9b1c1c"/><text x="${cx}" y="${cy-40}" text-anchor="middle" font-size="${14*k}" fill="#9b1c1c">N</text>`;
    if(!narrow) g+=`<text x="${W-10}" y="${(62-42.8)/28*480+20+18}" text-anchor="end" font-size="11" fill="#5a4a3a" font-style="italic">(not to scale) →</text>`;
    shown.forEach(s=>{ if(s.from===undefined) return; const f=STOPS[s.from]; if(!shown.includes(f)) return;
      const [x1,y1]=xy(f),[x2,y2]=xy(s); g+=`<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="#9b1c1c" stroke-width="${2*k}" stroke-dasharray="6 5" opacity=".75"/>`; });
    shown.forEach(s=>{const [x,y]=xy(s);const hi=s.mod===highlightMod;
      g+=`<circle cx="${x}" cy="${y}" r="${(hi?8:5.5)*k}" fill="${s.later?'#2c4a6b':(hi?'#a51f1f':'#5a4a3a')}" stroke="#f3ead6" stroke-width="2"/>`;
      if(narrow){ g+=`<text x="${x}" y="${y+5*k}" text-anchor="middle" font-size="${10*k}" fill="#fff" font-weight="600">${s.n}</text>`; return; }
      const [dx,dy,an]=s.lab||[10,-8,'start'], tx=x+dx, ty=y+dy;
      g+=`<text x="${tx}" y="${ty}" text-anchor="${an}" font-size="${hi?16:13}" fill="#2b2118" font-family="EB Garamond,Georgia,serif" font-weight="${hi?600:400}">${s.n}. ${s.name}</text><text x="${tx}" y="${ty+14}" text-anchor="${an}" font-size="11" fill="#5a4a3a" font-family="EB Garamond,Georgia,serif">${s.when}</text>`;});
    const list = narrow&&shown.length ? '<ol class="stoplist" start="0">'+STOPS.map(s=>shown.includes(s)?`<li value="${s.n}"${s.mod===highlightMod?' class="new"':''}>${s.name} · ${s.when}</li>`:'').join('')+'</ol>' : '';
    el.innerHTML=`<svg viewBox="0 0 ${W} ${H}" role="img" aria-label="Route chart of the plague's spread"><rect width="${W}" height="${H}" fill="#efe3c8"/>${g}</svg>${list}<div class="legend">Route chart (positions by latitude and longitude; coastlines not drawn; Central Asia pulled in from far to the east). Red dashes: how the plague spread between stops (simplified). Blue: an event after the course years.</div>`;
  }
  PY.drawMap=drawMap;
  document.querySelectorAll('.routemap').forEach(el=>{
    const upto=ORDER.indexOf(MOD), before=ORDER.slice(0,upto), full=ORDER.slice(0,upto+1);
    const target=el.querySelector('.mapdraw');
    drawMap(target,before.length?before:['__none__'],null);
    const seal=el.querySelector('button.seal');
    if(seal) seal.addEventListener('broken',()=>drawMap(target,full,MOD)); else drawMap(target,full,MOD);
  });

  /* ---------- Evidence Locker ---------- */
  function lockerData(){ return store.get('plagueYearLocker')||{}; }
  PY.lockerData=lockerData;
  function renderLocker(){
    document.querySelectorAll('.locker-list').forEach(el=>{
      const d=lockerData(); const keys=ORDER.filter(k=>d[k]);
      el.innerHTML = keys.length ? '<ol>'+keys.map(k=>`<li><b>Leaf ${ROMAN[k]}</b>: ${d[k].item}<span class="angle">Renaissance angle: ${d[k].angle}</span></li>`).join('')+'</ol>'
        : '<p><i>Your locker is empty so far. (It is saved in this browser only. If it ever looks empty, each leaf can re-seal its item.)</i></p>';
    });
  }
  document.querySelectorAll('.locker-add').forEach(el=>{
    const btn=el.querySelector('button'), need=(el.dataset.needs||'').split(',').filter(Boolean);
    el._chk=()=>{ if(btn.dataset.done) return; btn.disabled=!need.every(valid); };
    btn.addEventListener('click',()=>{
      const d=lockerData(); d[MOD]={item:el.dataset.item,angle:el.dataset.angle}; store.set('plagueYearLocker',d);
      PY.record('locker','Evidence Locker','sealed "'+el.dataset.item+'"');
      btn.dataset.done='1'; btn.textContent='Sealed into your Locker ✓'; btn.disabled=true; renderLocker();
    });
  });
  renderLocker();

  /* ---------- Questions for later ---------- */
  function laterQs(){ return (store.get('plagueYearLater')||[]).filter(q=>q.startsWith(MOD+': ')).map(q=>q.slice(5)); }
  document.querySelectorAll('.later-add').forEach(el=>{
    const ta=el.querySelector('textarea'), b=el.querySelector('button'), list=el.querySelector('.later-list');
    const draw=()=>{const q=store.get('plagueYearLater')||[]; list.innerHTML=q.length?'<ul>'+q.map(x=>`<li>${x.replace(/</g,'&lt;')}</li>`).join('')+'</ul>':'';};
    b.addEventListener('click',()=>{const v=ta.value.trim(); if(!v) return; const q=store.get('plagueYearLater')||[]; q.push(MOD+': '+v); store.set('plagueYearLater',q); ta.value=''; draw(); refreshAll();});
    draw();
  });

  /* ---------- progress bar + start over ---------- */
  const box=document.querySelector('.copybox');
  const REQ= box ? (box.dataset.required||'').split(',').map(s=>s.trim()).filter(Boolean) : [];
  const LABELS= box ? JSON.parse(box.dataset.labels||'{}') : {};
  let bar=null;
  if(box){
    bar=document.createElement('div'); bar.className='pybar';
    bar.innerHTML='<span class="pybar-t"></span><span class="pybar-track"><span class="pybar-fill"></span></span><button type="button" class="pybar-reset">Start this leaf over</button>';
    document.body.insertBefore(bar,document.body.firstChild);
    const rb=bar.querySelector('.pybar-reset');
    rb.addEventListener('click',()=>{ if(!rb.dataset.arm){ rb.dataset.arm='1'; rb.textContent='Tap again to clear this leaf'; setTimeout(()=>{delete rb.dataset.arm; rb.textContent='Start this leaf over';},4000); return; }
      store.del(SKEY); location.reload(); });
  }

  /* ---------- copy for Rocky ---------- */
  function buildText(){
    if(!box) return {text:'',missing:[]};
    const missing=REQ.filter(k=>!valid(k)).map(k=>LABELS[k]||k);
    const lines=[`THE PLAGUE YEAR · Leaf ${ROMAN[MOD]} (${MOD}) · my answers for Rocky`];
    const keys=[...REQ.filter(k=>answers.has(k)),...[...answers.keys()].filter(k=>!REQ.includes(k))];
    keys.forEach(k=>{const v=answers.get(k); lines.push(`- ${v.label}: ${v.value}`);});
    lines.push('- Deeper seals opened: '+(state.deeper.length?state.deeper.join('; '):'none'));
    const lq=laterQs(); if(lq.length) lines.push('- Questions for later: '+lq.join(' | '));
    if(MOD==='M08'){ const d=lockerData(), ks=ORDER.slice(0,7).filter(k=>d[k]); lines.push(`- Evidence Locker: ${ks.length} of 7 leaves sealed${ks.length?' ('+ks.map(k=>'Leaf '+ROMAN[k]).join(', ')+')':''}`); }
    lines.push(missing.length?`(Not done yet: ${missing.join('; ')})`:'(All tasks on this page are done.)');
    return {text:lines.join('\n'),missing};
  }
  function refreshAll(){
    updateSeals();
    document.querySelectorAll('.locker-add').forEach(el=>el._chk&&el._chk());
    if(!box) return;
    const {text,missing}=buildText();
    box.querySelector('pre').textContent=text;
    box.querySelector('.status').innerHTML = missing.length?`<span class="missing">Still to do: ${missing.join(' · ')}</span>`:'<span class="done-msg">Everything is done. Copy this and paste it into the chat with Rocky.</span>';
    if(bar){ const done=REQ.length-missing.length; bar.querySelector('.pybar-t').textContent=`Leaf ${ROMAN[MOD]} · ${done} of ${REQ.length} done`;
      bar.querySelector('.pybar-fill').style.width=(REQ.length?100*done/REQ.length:0)+'%'; }
  }
  PY.refreshCopy=refreshAll;
  async function doCopy(btn,idle){
    const {text}=buildText(); let ok=false;
    try{ await navigator.clipboard.writeText(text); ok=true; }catch(e){}
    if(!ok){ try{ const ta=document.createElement('textarea'); ta.value=text; document.body.appendChild(ta); ta.select(); ok=document.execCommand('copy'); ta.remove(); }catch(e){} }
    if(!ok && box){ const pre=box.querySelector('pre'); const r=document.createRange(); r.selectNodeContents(pre); const s=getSelection(); s.removeAllRanges(); s.addRange(r); pre.scrollIntoView({block:'center'}); }
    btn.textContent= ok ? 'Copied! Now paste it to Rocky' : 'Copy didn\'t work: the text is selected below, copy it by hand';
    setTimeout(()=>btn.textContent=idle,4000);
  }
  const cb=document.querySelector('.copybtn');
  if(cb) cb.addEventListener('click',()=>doCopy(cb,'Copy my answers for Rocky'));

  /* ---------- restore a saved leaf ---------- */
  const saved=store.get(SKEY);
  if(saved && saved.answers){
    restoring=true;
    Object.entries(saved.answers).forEach(([k,v])=>{
      answers.set(k,v);
      const f=fieldFor(k); if(f) f.value=v.value;
      const g=document.querySelector('.opts[data-key="'+k+'"]');
      if(g){ const b=[...g.querySelectorAll('.opt')].find(o=>(o.dataset.val||o.textContent.trim())===v.value); if(b) b.classList.add('chosen'); }
    });
    state.flags=saved.flags||[]; state.deeper=saved.deeper||[];
    (saved.opened||[]).forEach(id=>{ const s=seals[+id]; if(s) openSeal(s); });
    (saved.chunks||[]).forEach(id=>{ const c=document.getElementById(id); if(c){ c.classList.add('open'); state.chunks.push(id);
      const cp=document.querySelector('.checkpoint[data-opens="'+id+'"] .cp-go'); if(cp){ cp.disabled=true; cp.textContent='Continued ✓'; } } });
    if(answers.has('locker')) document.querySelectorAll('.locker-add button').forEach(btn=>{ btn.dataset.done='1'; btn.textContent='Sealed into your Locker ✓'; btn.disabled=true; });
    restoring=false;
    document.dispatchEvent(new CustomEvent('py-restored'));
  }
  refreshAll();
})();
