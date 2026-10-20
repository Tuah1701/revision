"""Deck engine: turns a list of cards + flashcards + MCQs into one self-contained, swipeable HTML page."""
import json, html as _h
import notes_ui

CSS = r"""
/* Layout: one-card-per-screen swipe track (CSS scroll-snap) between a slim top bar and a bottom progress bar.
   Each card scrolls vertically on its own; content column caps at ~680px so iPad landscape still reads like a page. */
:root{
  --bg:#11151C; --surface:#191E28; --surface2:#222937; --line:#2D3544;
  --fg:#E7EAF0; --muted:#98A1B0; --accent:#F0B44A; --accent-soft:#3A2D12; --on-accent:#1B1404;
  --teal:#5CC6BF; --teal-soft:#14302F; --good:#6FD39A; --good-soft:#15301F; --bad:#F2897F; --bad-soft:#3A1C1A;
  --fill-a:rgba(240,180,74,.28); --fill-b:rgba(92,198,191,.26); --fill-c:rgba(242,137,127,.32);
  --f-disp:"Bricolage Grotesque","Avenir Next","Segoe UI",system-ui,sans-serif;
  --f-body:"Atkinson Hyperlegible","Segoe UI",system-ui,-apple-system,sans-serif;
  --f-mono:"JetBrains Mono",ui-monospace,Menlo,Consolas,monospace;
  color-scheme:dark;
}
@media (prefers-color-scheme: light){:root:not([data-theme="dark"]){
  --bg:#F4F5F8; --surface:#FFFFFF; --surface2:#ECEEF3; --line:#D7DBE3;
  --fg:#171B23; --muted:#576070; --accent:#A66F07; --accent-soft:#FBEFD6; --on-accent:#FFFFFF;
  --teal:#13807A; --teal-soft:#DDF2F0; --good:#1E7A47; --good-soft:#DDF1E5; --bad:#B23A30; --bad-soft:#F9E1DE;
  --fill-a:rgba(214,150,30,.25); --fill-b:rgba(19,128,122,.20); --fill-c:rgba(178,58,48,.22);
  color-scheme:light}}
:root[data-theme="light"]{
  --bg:#F4F5F8; --surface:#FFFFFF; --surface2:#ECEEF3; --line:#D7DBE3;
  --fg:#171B23; --muted:#576070; --accent:#A66F07; --accent-soft:#FBEFD6; --on-accent:#FFFFFF;
  --teal:#13807A; --teal-soft:#DDF2F0; --good:#1E7A47; --good-soft:#DDF1E5; --bad:#B23A30; --bad-soft:#F9E1DE;
  --fill-a:rgba(214,150,30,.25); --fill-b:rgba(19,128,122,.20); --fill-c:rgba(178,58,48,.22);
  color-scheme:light}
*{box-sizing:border-box}
[hidden]{display:none!important}
html,body{height:100%;background:var(--bg);overscroll-behavior:none}
body{margin:0;color:var(--fg);font:17px/1.55 var(--f-body);display:grid;grid-template-rows:auto 1fr auto;overflow:hidden;-webkit-text-size-adjust:100%}
button{font:inherit;color:inherit}
:focus-visible{outline:2px solid var(--accent);outline-offset:2px}

/* top bar */
.top{display:flex;align-items:center;gap:8px;padding:8px 12px;border-bottom:1px solid var(--line);background:var(--bg);min-width:0}
.ib{all:unset;cursor:pointer;display:inline-grid;place-items:center;min-width:44px;height:44px;border-radius:10px;color:var(--fg)}
.ib:hover{background:var(--surface2)}
.ib svg{width:22px;height:22px;stroke:currentColor;fill:none;stroke-width:1.9;stroke-linecap:round;stroke-linejoin:round}
.ttl{flex:1;min-width:0;line-height:1.15}
.ttl b{display:block;font:700 15px/1.2 var(--f-disp);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.ttl small{display:block;font:500 11.5px/1.3 var(--f-mono);color:var(--muted);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.mode{all:unset;cursor:pointer;height:36px;padding:0 12px;border-radius:999px;border:1px solid var(--line);font:600 13.5px/36px var(--f-body);white-space:nowrap}
.mode:hover{border-color:var(--accent)}
@media (max-width:430px){.mode .lg{display:none}.mode{padding:0 10px}}

/* track */
.track{display:flex;overflow-x:auto;overflow-y:hidden;scroll-snap-type:x mandatory;scrollbar-width:none;min-height:0;overscroll-behavior-x:contain}
.track::-webkit-scrollbar{display:none}
.card{flex:0 0 100%;width:100%;scroll-snap-align:start;scroll-snap-stop:always;overflow-y:auto;overflow-x:hidden;-webkit-overflow-scrolling:touch;padding-inline:16px}
.ci{max-width:680px;margin:0 auto;padding-block:20px 48px;min-width:0}
.ch{display:flex;justify-content:space-between;gap:10px;align-items:center;margin-bottom:10px}
.sec{font:600 11.5px/1 var(--f-mono);letter-spacing:.06em;text-transform:uppercase;color:var(--accent)}
.kind{font:600 10.5px/1 var(--f-mono);letter-spacing:.08em;text-transform:uppercase;color:var(--muted);border:1px solid var(--line);border-radius:999px;padding:5px 8px}
h1{font:800 clamp(34px,9vw,52px)/1.02 var(--f-disp);letter-spacing:-.02em;margin:.2em 0 .3em;text-wrap:balance}
h2{font:750 clamp(25px,6.4vw,32px)/1.12 var(--f-disp);letter-spacing:-.01em;margin:0 0 .5em;text-wrap:balance}
h3{font:700 19px/1.25 var(--f-disp);margin:1.4em 0 .45em;text-wrap:balance}
p{margin:.5em 0} ul,ol{margin:.4em 0 .8em;padding-left:1.25em} li{margin:.28em 0}
b,strong{font-weight:700}
.lede{color:var(--muted);font-size:17.5px}
.mono{font-family:var(--f-mono);font-size:.88em}
.def{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:12px 15px;margin:12px 0}
.def .lab{display:flex;justify-content:space-between;gap:8px;font:600 11px/1.3 var(--f-mono);letter-spacing:.07em;text-transform:uppercase;color:var(--accent);margin-bottom:5px}
.def .lab i{font-style:normal;color:var(--muted)}
.def p{margin:.2em 0}
.note{border-radius:12px;padding:11px 14px;margin:12px 0;font-size:16px}
.note>b:first-child{display:block;font:600 11px/1.3 var(--f-mono);letter-spacing:.08em;text-transform:uppercase;margin-bottom:3px}
.note.trap{background:var(--bad-soft)} .note.trap>b:first-child{color:var(--bad)}
.note.tip{background:var(--good-soft)} .note.tip>b:first-child{color:var(--good)}
.note.link{background:var(--teal-soft)} .note.link>b:first-child{color:var(--teal)}
.two{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,240px),1fr));gap:10px;margin:12px 0}
.two>div{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:11px 14px;min-width:0}
.two h4{font:700 12px/1.3 var(--f-mono);letter-spacing:.06em;text-transform:uppercase;color:var(--accent);margin:0 0 4px}
.two h4.t{color:var(--teal)} .two h4.g{color:var(--good)} .two h4.r{color:var(--bad)}
.two p,.two ul{margin:.2em 0;font-size:16px}
.chain{display:flex;flex-wrap:wrap;gap:6px;align-items:center;margin:12px 0;font:600 14.5px/1.3 var(--f-body)}
.chain span{background:var(--surface);border:1px solid var(--line);border-radius:8px;padding:6px 9px}
.chain i{font-style:normal;color:var(--accent);font-weight:800}
.formula{font:600 15px/1.5 var(--f-mono);background:var(--surface);border:1px dashed var(--muted);border-radius:10px;padding:9px 12px;margin:10px 0;overflow-x:auto}
.tw{overflow-x:auto;margin:12px 0;border:1px solid var(--line);border-radius:12px;overscroll-behavior-x:contain}
table{border-collapse:collapse;width:100%;font-size:15px;line-height:1.4;background:var(--surface)}
.tw.wide table{min-width:560px}
th,td{padding:8px 10px;text-align:left;vertical-align:top;border-bottom:1px solid var(--line)}
tr:last-child td{border-bottom:0}
th{font:600 10.5px/1.3 var(--f-mono);letter-spacing:.06em;text-transform:uppercase;color:var(--muted);background:var(--surface2)}
td.n,th.n{text-align:right;font-family:var(--f-mono);font-variant-numeric:tabular-nums;font-size:14px}
td.k{font-weight:700}
.tag{display:inline-block;font:600 10.5px/1 var(--f-mono);letter-spacing:.05em;text-transform:uppercase;color:var(--accent);background:var(--accent-soft);padding:4px 7px;border-radius:6px;margin-right:6px;vertical-align:2px}

/* diagrams */
figure.dg{margin:14px 0;display:grid;gap:10px}
figure.dg.multi{grid-template-columns:repeat(auto-fit,minmax(min(100%,250px),1fr))}
.pnl{min-width:0}
.ptitle{font:600 11px/1.3 var(--f-mono);letter-spacing:.05em;text-transform:uppercase;color:var(--muted);margin:0 0 4px}
figure.dg svg{width:100%;height:auto;display:block;background:var(--surface);border:1px solid var(--line);border-radius:12px}
figcaption{font-size:14.5px;color:var(--muted);grid-column:1/-1}
svg text{font-family:var(--f-body);fill:var(--fg)}
svg .ax{stroke:var(--fg);stroke-width:1.5;fill:none}
svg .k{fill:none;stroke-width:2.6;stroke-linecap:round}
svg .d{stroke:var(--accent)} svg .s{stroke:var(--teal)} svg .o{stroke:var(--muted);stroke-dasharray:6 4;stroke-width:2}
svg .b{stroke:var(--bad)} svg .gr{stroke:var(--good)}
svg .g{stroke:var(--muted);stroke-width:1;stroke-dasharray:3 3;fill:none}
svg .ar{stroke:var(--fg);stroke-width:1.8} svg .arh{fill:var(--fg)}
svg .pt{fill:var(--fg)} svg .pto{fill:var(--surface);stroke:var(--fg);stroke-width:1.6}
svg .fa{fill:var(--fill-a)} svg .fb{fill:var(--fill-b)} svg .fc{fill:var(--fill-c)}
svg .t-ax{font-size:12px;font-weight:700;fill:var(--muted)}
svg .t-axl{font-size:12px;font-weight:700;fill:var(--fg)}
svg .t-pt{font-size:13px;font-weight:700}
svg .t-sm{font-size:11.5px;fill:var(--muted)}
svg .t-d{fill:var(--accent);font-size:12.5px;font-weight:700} svg .t-s{fill:var(--teal);font-size:12.5px;font-weight:700}
svg .t-o{fill:var(--muted);font-size:12.5px;font-weight:700} svg .t-b{fill:var(--bad);font-size:12.5px;font-weight:700}
svg .t-gr{fill:var(--good);font-size:12.5px;font-weight:700}

/* reveal: worked-example steps and practice answers */
ol.steps{list-style:none;padding:0;margin:12px 0;counter-reset:st;display:grid;gap:8px}
ol.steps>li{counter-increment:st;background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:10px 14px 10px 46px;position:relative;margin:0}
ol.steps>li::before{content:counter(st);position:absolute;left:12px;top:10px;width:24px;height:24px;border-radius:50%;background:var(--accent-soft);color:var(--accent);font:700 13px/24px var(--f-mono);text-align:center}
.rvbar{display:flex;gap:8px;flex-wrap:wrap;margin:10px 0}
.btn{all:unset;cursor:pointer;min-height:44px;padding:0 16px;border-radius:12px;display:inline-flex;align-items:center;gap:8px;font:700 15px/1 var(--f-body);border:1px solid var(--line);background:var(--surface)}
.btn.pri{background:var(--accent);color:var(--on-accent);border-color:var(--accent)}
.btn[disabled]{opacity:.45;cursor:default}
.btn.good{border-color:var(--good);color:var(--good)} .btn.bad{border-color:var(--bad);color:var(--bad)}
.pq{background:var(--surface);border:1px solid var(--line);border-radius:14px;padding:12px 14px;margin:12px 0}
.pq .qh{display:flex;justify-content:space-between;gap:8px;font:600 11px/1.3 var(--f-mono);letter-spacing:.05em;text-transform:uppercase;color:var(--muted)}
.pq .qh .mk{color:var(--accent)}
.pq .qt{margin:.35em 0 .5em}
.pq .ans{border-top:1px dashed var(--line);margin-top:8px;padding-top:8px}
.pq .ans>b:first-child{font:600 11px/1 var(--f-mono);letter-spacing:.07em;text-transform:uppercase;color:var(--good);margin-right:6px}
.swipehint{display:flex;align-items:center;gap:8px;color:var(--muted);font-size:14.5px;margin-top:22px}
.toc-mini{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,200px),1fr));gap:8px;margin:14px 0}
.toc-mini button{all:unset;cursor:pointer;background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:10px 12px}
.toc-mini button:hover{border-color:var(--accent)}
.toc-mini b{display:block;font:800 20px/1 var(--f-disp);color:var(--accent);margin-bottom:4px}
.toc-mini span{font-size:14.5px;color:var(--muted)}
.cover-k{font:800 clamp(80px,26vw,150px)/.85 var(--f-disp);color:var(--accent);letter-spacing:-.04em;margin:8px 0 0}
.stat{display:flex;gap:18px;flex-wrap:wrap;margin:16px 0;font:600 14px/1.3 var(--f-mono);color:var(--muted)}
.stat b{display:block;font:800 26px/1 var(--f-disp);color:var(--fg)}
a{color:var(--accent)}

/* bottom bar */
.bot{display:grid;grid-template-columns:auto 1fr auto;align-items:center;gap:10px;padding:8px 12px;border-top:1px solid var(--line);background:var(--bg)}
.prog{display:grid;gap:5px;min-width:0}
.bar{height:4px;background:var(--surface2);border-radius:4px;overflow:hidden}
.bar i{display:block;height:100%;width:0;background:var(--accent);transition:width .25s}
.cnt{font:600 12.5px/1 var(--f-mono);color:var(--muted);text-align:center;font-variant-numeric:tabular-nums;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}

/* sheets (contents, flashcards, quiz) */
.sheet{position:fixed;inset:0;z-index:20;background:var(--bg);display:grid;grid-template-rows:auto 1fr;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}
.sheet .top{border-bottom:1px solid var(--line)}
.sbody{overflow-y:auto;padding-inline:16px;-webkit-overflow-scrolling:touch}
.sbody>.in{max-width:680px;margin:0 auto;padding-block:14px 40px}
.tocgrp{font:600 11px/1.3 var(--f-mono);letter-spacing:.07em;text-transform:uppercase;color:var(--accent);margin:18px 0 6px}
.tocitem{all:unset;cursor:pointer;display:grid;grid-template-columns:32px 1fr auto;gap:8px;align-items:baseline;width:100%;box-sizing:border-box;padding:10px 8px;border-radius:10px}
.tocitem:hover,.tocitem.cur{background:var(--surface)}
.tocitem .no{font:600 12px/1 var(--f-mono);color:var(--muted)}
.tocitem .kd{font:600 10px/1 var(--f-mono);letter-spacing:.06em;text-transform:uppercase;color:var(--muted)}
.chips{display:flex;flex-wrap:wrap;gap:6px;margin:4px 0 12px}
.chip{all:unset;cursor:pointer;min-height:34px;padding:0 12px;border-radius:999px;border:1px solid var(--line);font:600 13.5px/34px var(--f-body)}
.chip[aria-pressed="true"]{background:var(--accent);border-color:var(--accent);color:var(--on-accent)}
.fc{perspective:1200px;height:min(56vh,380px);cursor:pointer;margin:6px 0 12px}
.fc-in{position:relative;width:100%;height:100%;transition:transform .45s;transform-style:preserve-3d}
.fc.flip .fc-in{transform:rotateY(180deg)}
.fc-f{position:absolute;inset:0;backface-visibility:hidden;-webkit-backface-visibility:hidden;border-radius:18px;border:1px solid var(--line);background:var(--surface);padding:42px 22px 30px;display:flex;flex-direction:column;justify-content:center;overflow:auto;font-size:19px;line-height:1.45}
.fc-f.back{transform:rotateY(180deg);background:var(--accent-soft);font-size:17.5px}
.fc-f .ft{position:absolute;top:14px;left:18px;right:18px;display:flex;justify-content:space-between;font:600 11px/1 var(--f-mono);letter-spacing:.06em;text-transform:uppercase;color:var(--muted)}
.fc-f.front .q{font:700 21px/1.3 var(--f-disp)}
.fcrow{display:flex;gap:8px;flex-wrap:wrap;justify-content:space-between}
.mcq{background:var(--surface);border:1px solid var(--line);border-radius:14px;padding:14px;margin:12px 0}
.mcq .qh{display:flex;justify-content:space-between;gap:8px;font:600 11px/1.3 var(--f-mono);letter-spacing:.05em;text-transform:uppercase;color:var(--muted)}
.mcq .qt{margin:.4em 0 .7em;font-weight:700}
.opts{display:grid;gap:6px}
.opt{all:unset;cursor:pointer;display:grid;grid-template-columns:26px 1fr;gap:8px;align-items:baseline;padding:10px 12px;border:1px solid var(--line);border-radius:10px;font-size:16px;line-height:1.4}
.opt b{font:700 13px/1 var(--f-mono);color:var(--accent)}
.opt.right{background:var(--good-soft);border-color:var(--good)} .opt.wrong{background:var(--bad-soft);border-color:var(--bad)}
.mcq.done .opt{cursor:default}
.mcq .ex{margin-top:10px;font-size:15.5px;border-top:1px dashed var(--line);padding-top:10px}
.score{position:sticky;top:0;z-index:2;background:var(--bg);padding-block:10px;display:flex;justify-content:space-between;align-items:center;gap:10px;border-bottom:1px solid var(--line);font:600 14px var(--f-body)}
.score .num{font:700 16px var(--f-mono);color:var(--accent);font-variant-numeric:tabular-nums}
mjx-container{max-width:100%;overflow-x:auto;overflow-y:hidden}
""" + notes_ui.CSS + r"""
@media (prefers-reduced-motion:reduce){.fc-in,.bar i{transition:none}.track{scroll-behavior:auto}}
"""

ICONS = {
    "menu": '<svg viewBox="0 0 24 24"><path d="M4 7h16M4 12h16M4 17h10"/></svg>',
    "theme": '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="4.5"/><path d="M12 2.5v2M12 19.5v2M4.6 4.6l1.4 1.4M18 18l1.4 1.4M2.5 12h2M19.5 12h2M4.6 19.4L6 18M18 6l1.4-1.4"/></svg>',
    "prev": '<svg viewBox="0 0 24 24"><path d="M15 5l-7 7 7 7"/></svg>',
    "next": '<svg viewBox="0 0 24 24"><path d="M9 5l7 7-7 7"/></svg>',
    "close": '<svg viewBox="0 0 24 24"><path d="M6 6l12 12M18 6L6 18"/></svg>',
}

JS = r"""
(function(){
var KEY=DECK.key, root=document.documentElement;
function sget(k){try{return localStorage.getItem(KEY+':'+k)}catch(e){return null}}
function sset(k,v){try{localStorage.setItem(KEY+':'+k,v)}catch(e){}}
/* theme: dark by default, light on request */
root.setAttribute('data-theme',sget('theme')||'dark');
document.getElementById('themeBtn').addEventListener('click',function(){
  var t=root.getAttribute('data-theme')==='dark'?'light':'dark';root.setAttribute('data-theme',t);sset('theme',t);});

var track=document.getElementById('track'), cards=[].slice.call(track.querySelectorAll('.card'));
var N=cards.length, cur=0, bar=document.getElementById('barFill'), cnt=document.getElementById('cnt');
function width(){return track.clientWidth}
function update(i){cur=i;bar.style.width=((i+1)/N*100)+'%';
  cnt.textContent=(i+1)+' / '+N+' · '+cards[i].dataset.title;sset('pos',i);
  document.getElementById('prevBtn').disabled=i===0;document.getElementById('nextBtn').disabled=i===N-1;}
function go(i,smooth){i=Math.max(0,Math.min(N-1,i));
  track.scrollTo({left:i*width(),behavior:smooth===false?'auto':'smooth'});update(i);}
var t0;track.addEventListener('scroll',function(){clearTimeout(t0);t0=setTimeout(function(){
  var i=Math.round(track.scrollLeft/width());if(i!==cur)update(i);},80);},{passive:true});
window.addEventListener('resize',function(){track.scrollTo({left:cur*width(),behavior:'auto'});});
document.getElementById('prevBtn').addEventListener('click',function(){go(cur-1)});
document.getElementById('nextBtn').addEventListener('click',function(){go(cur+1)});
document.addEventListener('keydown',function(e){
  if(document.querySelector('.sheet:not([hidden])'))return;
  if(e.key==='ArrowRight'||e.key==='PageDown'){go(cur+1);e.preventDefault();}
  if(e.key==='ArrowLeft'||e.key==='PageUp'){go(cur-1);e.preventDefault();}});
document.querySelectorAll('[data-goto]').forEach(function(b){b.addEventListener('click',function(){
  var t=b.getAttribute('data-goto');for(var i=0;i<N;i++){if(cards[i].dataset.id===t){go(i);return;}}});});

/* tap-to-reveal: worked-example steps */
document.querySelectorAll('ol.steps').forEach(function(ol){
  var li=[].slice.call(ol.children),shown=0;li.forEach(function(x){x.hidden=true});
  var bar=document.createElement('div');bar.className='rvbar';
  var nb=document.createElement('button');nb.className='btn pri';nb.type='button';
  var ab=document.createElement('button');ab.className='btn';ab.type='button';ab.textContent='Show all';
  function paint(){nb.textContent=shown<li.length?('Show step '+(shown+1)+' of '+li.length):'All steps shown';
    nb.disabled=shown>=li.length;ab.hidden=shown>=li.length;}
  nb.addEventListener('click',function(){if(shown<li.length){li[shown].hidden=false;shown++;paint();}});
  ab.addEventListener('click',function(){li.forEach(function(x){x.hidden=false});shown=li.length;paint();});
  bar.appendChild(nb);bar.appendChild(ab);ol.parentNode.insertBefore(bar,ol.nextSibling);paint();});
/* tap-to-reveal: practice answers */
document.querySelectorAll('.pq').forEach(function(q){
  var a=q.querySelector('.ans');if(!a)return;a.hidden=true;
  var b=document.createElement('button');b.className='btn';b.type='button';b.textContent='Show answer';
  b.addEventListener('click',function(){a.hidden=!a.hidden;b.textContent=a.hidden?'Show answer':'Hide answer';});
  q.insertBefore(b,a);});
document.querySelectorAll('[data-revealall]').forEach(function(b){b.addEventListener('click',function(){
  var c=b.closest('.card');c.querySelectorAll('.pq .ans').forEach(function(a){a.hidden=false});
  c.querySelectorAll('.pq .btn').forEach(function(x){x.textContent='Hide answer'});});});

/* sheets */
function openSheet(id){document.getElementById(id).hidden=false;}
function closeSheets(){document.querySelectorAll('.sheet').forEach(function(s){s.hidden=true});}
document.querySelectorAll('[data-close]').forEach(function(b){b.addEventListener('click',closeSheets)});
document.addEventListener('keydown',function(e){if(e.key==='Escape')closeSheets();});

/* contents */
var toc=document.getElementById('tocList'),lastSec=null;
cards.forEach(function(c,i){
  var s=c.dataset.group;if(s!==lastSec){var g=document.createElement('div');g.className='tocgrp';g.textContent=s;toc.appendChild(g);lastSec=s;}
  var b=document.createElement('button');b.className='tocitem';b.type='button';
  b.innerHTML='<span class="no">'+(i+1)+'</span><span></span><span class="kd"></span>';
  b.children[1].textContent=c.dataset.title;b.children[2].textContent=c.dataset.kind;
  b.addEventListener('click',function(){closeSheets();go(i,false);});toc.appendChild(b);});
document.getElementById('tocBtn').addEventListener('click',function(){
  [].forEach.call(toc.querySelectorAll('.tocitem'),function(b,i){b.classList.toggle('cur',i===cur)});
  openSheet('tocSheet');var c=toc.querySelector('.cur');if(c)c.scrollIntoView({block:'center'});});

/* flashcards */
var F=DECK.flash,topics=['All'];F.forEach(function(c){if(topics.indexOf(c[0])<0)topics.push(c[0])});topics.push('Again pile');
var sel={},againMode=false,order=[],fi=0,again={};
try{JSON.parse(sget('fcsel')||'[]').forEach(function(t){if(topics.indexOf(t)>0)sel[t]=1})}catch(e){}
var chipBox=document.getElementById('fcChips'),fc=document.getElementById('fc');
function paintChips(){var none=!Object.keys(sel).length;
  [].forEach.call(chipBox.children,function(x){var t=x.textContent;
    x.setAttribute('aria-pressed',(t==='Again pile'?againMode:t==='All'?(!againMode&&none):(!againMode&&!!sel[t]))?'true':'false')});}
topics.forEach(function(t){var b=document.createElement('button');b.className='chip';b.type='button';b.textContent=t;
  b.addEventListener('click',function(){
    if(t==='Again pile'){againMode=!againMode;}
    else{againMode=false;if(t==='All')sel={};else if(sel[t])delete sel[t];else sel[t]=1;sset('fcsel',JSON.stringify(Object.keys(sel)));}
    paintChips();build();});
  chipBox.appendChild(b);});
function build(){var none=!Object.keys(sel).length;order=[];
  F.forEach(function(c,i){if(againMode?again[i]:(none||sel[c[0]]))order.push(i)});fi=0;paintChips();show();}
function show(){fc.classList.remove('flip');var q=document.getElementById('fcQ'),a=document.getElementById('fcA');
  if(!order.length){q.textContent=againMode?'Nothing in the Again pile yet.':'No cards.';a.textContent='';document.getElementById('fcN').textContent='0 cards';return;}
  var c=F[order[fi]];q.innerHTML=c[1];a.innerHTML=c[2];
  document.getElementById('fcT').textContent=c[0];document.getElementById('fcT2').textContent=c[0];
  document.getElementById('fcN').textContent=(fi+1)+' / '+order.length;}
fc.addEventListener('click',function(){fc.classList.toggle('flip')});
document.getElementById('fcPrev').addEventListener('click',function(){if(order.length){fi=(fi-1+order.length)%order.length;show();}});
document.getElementById('fcNext').addEventListener('click',function(){if(order.length){fi=(fi+1)%order.length;show();}});
document.getElementById('fcShuf').addEventListener('click',function(){for(var i=order.length-1;i>0;i--){var j=Math.floor(Math.random()*(i+1));var t=order[i];order[i]=order[j];order[j]=t;}fi=0;show();});
document.getElementById('fcAgain').addEventListener('click',function(){if(order.length){again[order[fi]]=1;fi=(fi+1)%order.length;show();}});
document.getElementById('fcGot').addEventListener('click',function(){if(!order.length)return;delete again[order[fi]];
  if(againMode){order.splice(fi,1);if(fi>=order.length)fi=0;}else fi=(fi+1)%order.length;show();});
document.addEventListener('keydown',function(e){if(document.getElementById('fcSheet').hidden)return;
  if(e.key===' '){fc.classList.toggle('flip');e.preventDefault();}
  if(e.key==='ArrowRight')document.getElementById('fcNext').click();
  if(e.key==='ArrowLeft')document.getElementById('fcPrev').click();});
document.getElementById('fcBtn').addEventListener('click',function(){openSheet('fcSheet');});
build();

/* quiz */
var Q=DECK.quiz,list=document.getElementById('qList'),right=0,done=0;
function renderQ(){list.innerHTML='';right=0;done=0;paintS();
  Q.forEach(function(it,qi){var box=document.createElement('div');box.className='mcq';
    box.innerHTML='<div class="qh"><span>Q'+(qi+1)+'</span><span></span></div><p class="qt"></p><div class="opts"></div>';
    box.querySelector('.qh span:last-child').textContent=it.s;box.querySelector('.qt').innerHTML=it.q;
    var opts=box.querySelector('.opts');
    it.o.forEach(function(t,oi){var b=document.createElement('button');b.type='button';b.className='opt';
      b.innerHTML='<b>'+'ABCD'[oi]+'</b><span></span>';b.querySelector('span').innerHTML=t;
      b.addEventListener('click',function(){if(box.classList.contains('done'))return;box.classList.add('done');done++;
        var ok=oi===it.c;if(ok)right++;b.classList.add(ok?'right':'wrong');opts.children[it.c].classList.add('right');
        var ex=document.createElement('div');ex.className='ex';
        ex.innerHTML='<b style="color:var('+(ok?'--good':'--bad')+')">'+(ok?'Correct. ':'Answer: '+'ABCD'[it.c]+'. ')+'</b>'+it.e;box.appendChild(ex);paintS();});
      opts.appendChild(b);});
    list.appendChild(box);});}
function paintS(){document.getElementById('qScore').textContent=right+' / '+done+' answered of '+Q.length;}
document.getElementById('qReset').addEventListener('click',function(){renderQ();list.parentNode.parentNode.scrollTop=0;});
document.getElementById('qBtn').addEventListener('click',function(){openSheet('qSheet');});
renderQ();

""" + notes_ui.JS + r"""
/* start where you left off */
var start=parseInt(sget('pos')||'0',10);if(!(start>=0&&start<N))start=0;
var h=(location.hash||'').slice(1);if(h){cards.forEach(function(c,i){if(c.dataset.id===h)start=i});}
requestAnimationFrame(function(){go(start,false);});
})();
"""


def card(cid, group, title, kind, body, sec=None):
    sec = sec or group
    return {"id": cid, "group": group, "title": title, "kind": kind, "body": body, "sec": sec}


def render(meta, cards, flash, quiz, math=False):
    e = _h.escape
    secs = []
    for c in cards:
        secs.append(
            f'<section class="card" data-id="{e(c["id"])}" data-group="{e(c["group"])}" data-title="{e(c["title"])}" data-kind="{e(c["kind"])}">'
            f'<div class="ci"><div class="ch"><span class="sec">{c["sec"]}</span><span class="kind">{e(c["kind"])}</span></div>'
            f'{c["body"]}</div></section>')
    data = json.dumps({"key": meta["key"], "flash": flash, "quiz": quiz}, ensure_ascii=False)
    mj = ""
    if math:
        mj = ('<script>window.MathJax={tex:{inlineMath:[["\\\\(","\\\\)"]]},svg:{fontCache:"global"},options:{enableMenu:false}};</script>'
              '<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.2/es5/tex-svg.js"></script>')
    return f"""<title>{e(meta['title'])}</title>
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="{e(meta['short'])}">
<meta name="theme-color" content="#11151C">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:wght@400;700&family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700;12..96,800&family=JetBrains+Mono:wght@500;600;700&display=swap">
<style>{CSS}</style>
{mj}
<header class="top">
  <button class="ib" id="tocBtn" type="button" aria-label="Contents">{ICONS['menu']}</button>
  <div class="ttl"><b>{e(meta['bar'])}</b><small>{e(meta['code'])}</small></div>
  <button class="mode" id="fcBtn" type="button">Cards<span class="lg"> · {len(flash)}</span></button>
  <button class="mode" id="qBtn" type="button">Quiz<span class="lg"> · {len(quiz)}</span></button>
  <button class="ib" id="themeBtn" type="button" aria-label="Switch light or dark">{ICONS['theme']}</button>
</header>
<main class="track" id="track">{''.join(secs)}</main>
<footer class="bot">
  <button class="ib" id="prevBtn" type="button" aria-label="Previous card">{ICONS['prev']}</button>
  <div class="prog"><div class="bar"><i id="barFill"></i></div><div class="cnt" id="cnt">1 / {len(cards)}</div></div>
  <button class="ib" id="nextBtn" type="button" aria-label="Next card">{ICONS['next']}</button>
</footer>

<div class="sheet" id="tocSheet" hidden>
  <header class="top"><div class="ttl"><b>Contents</b><small>{len(cards)} cards · tap to jump</small></div>
  <button class="ib" type="button" data-close aria-label="Close">{ICONS['close']}</button></header>
  <div class="sbody"><div class="in" id="tocList"></div></div>
</div>
<div class="sheet" id="fcSheet" hidden>
  <header class="top"><div class="ttl"><b>Flashcards</b><small>Tap the card to flip · Space flips on a keyboard</small></div>
  <button class="ib" type="button" data-close aria-label="Close">{ICONS['close']}</button></header>
  <div class="sbody"><div class="in">
    <div class="chips" id="fcChips"></div>
    <div class="fc" id="fc"><div class="fc-in">
      <div class="fc-f front"><div class="ft"><span id="fcT"></span><span>Question</span></div><div class="q" id="fcQ"></div></div>
      <div class="fc-f back"><div class="ft"><span id="fcT2"></span><span>Answer</span></div><div id="fcA"></div></div>
    </div></div>
    <div class="fcrow"><button class="btn bad" id="fcAgain" type="button">Again</button><span class="cnt" id="fcN" style="align-self:center"></span><button class="btn good" id="fcGot" type="button">Got it</button></div>
    <div class="fcrow" style="margin-top:8px"><button class="btn" id="fcPrev" type="button">← Prev</button><button class="btn" id="fcShuf" type="button">Shuffle</button><button class="btn" id="fcNext" type="button">Next →</button></div>
    <p class="lede" style="font-size:14.5px;margin-top:14px">Tap several topics to mix them; tap All to reset. "Again" puts the card in the Again pile so you can drill only the ones you missed.</p>
  </div></div>
</div>
<div class="sheet" id="qSheet" hidden>
  <header class="top"><div class="ttl"><b>Paper 1 quiz</b><small>Pick an answer to see the explanation</small></div>
  <button class="ib" type="button" data-close aria-label="Close">{ICONS['close']}</button></header>
  <div class="sbody"><div class="in">
    <div class="score"><span>Score <span class="num" id="qScore"></span></span><button class="btn" id="qReset" type="button">Reset</button></div>
    <div id="qList"></div>
  </div></div>
</div>
{notes_ui.HTML}
<script>var DECK={data};</script>
<script>{JS}</script>
"""
