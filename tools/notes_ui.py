"""Handwriting notes for worked examples and practice questions (Apple Pencil friendly).
Every card of kind "Worked example" and every .pq practice question gets a "Write your working" button.
Notes are vector strokes saved on the device (localStorage), one notebook per question, with A4-ratio pages."""

CSS = r"""
/* ---------- handwriting notes ---------- */
.wrow{display:flex;flex-wrap:wrap;gap:10px;align-items:flex-start;margin:10px 0}
.btn.write{border-color:var(--teal);color:var(--teal)}
.btn.write svg{width:18px;height:18px;stroke:currentColor;fill:none;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
.wthumb{display:block;max-width:150px;width:100%;border:1px solid var(--line);border-radius:10px;cursor:pointer;background:var(--surface)}
.wmeta{font:600 11.5px/1.3 var(--f-mono);color:var(--muted)}
#noteSheet{display:flex;flex-direction:column;-webkit-user-select:none;user-select:none;-webkit-touch-callout:none}
#noteSheet>.npages{flex:1;min-height:0}
.ntools{display:flex;gap:6px;align-items:center;padding:6px 10px;border-bottom:1px solid var(--line);overflow-x:auto;scrollbar-width:none;background:var(--bg)}
.ntools::-webkit-scrollbar{display:none}
.tl{all:unset;cursor:pointer;flex:none;display:inline-grid;place-items:center;min-width:38px;height:40px;border-radius:10px;border:1px solid transparent;font:700 13px/1 var(--f-body)}
.tl svg{width:21px;height:21px;stroke:currentColor;fill:none;stroke-width:1.9;stroke-linecap:round;stroke-linejoin:round}
.tl[aria-pressed="true"]{border-color:var(--accent);background:var(--accent-soft);color:var(--accent)}
.tl[disabled]{opacity:.35;cursor:default}
.tl .dot{width:20px;height:20px;border-radius:50%;border:2px solid var(--line)}
.tl[aria-pressed="true"] .dot{border-color:var(--accent)}
.sep{flex:none;width:1px;height:26px;background:var(--line);margin:0 2px}
.nq{border-bottom:1px solid var(--line);background:var(--surface);padding:8px 16px;max-height:34vh;overflow-y:auto;font-size:15.5px}
.nq .in{max-width:680px;margin:0 auto}
.nq p{margin:.3em 0}
.nq .tw{margin:6px 0}
.npages{overflow:auto;padding:14px 12px 60px;background:var(--surface2);touch-action:none;overscroll-behavior:contain}
.npage{position:relative;margin:0 auto 14px;border-radius:6px;box-shadow:0 1px 3px rgba(0,0,0,.25);overflow:hidden}
.npage canvas{display:block;width:100%;height:auto;touch-action:none;-webkit-user-select:none;user-select:none;-webkit-touch-callout:none}
.npage .pn{position:absolute;right:10px;bottom:8px;font:600 11px/1 var(--f-mono);color:var(--muted);pointer-events:none}
.nhint{font-size:13px;color:var(--muted);text-align:center;margin:4px 0 0}
"""

ICON = {
    "pen": '<svg viewBox="0 0 24 24"><path d="M4 20l4-1 11-11-3-3L5 16l-1 4z"/><path d="M14 6l3 3"/></svg>',
    "hl": '<svg viewBox="0 0 24 24"><path d="M9 15l-3 5h6l1-2"/><path d="M9 15l7-11 4 3-7 11z"/></svg>',
    "er": '<svg viewBox="0 0 24 24"><path d="M8 20h12"/><path d="M4.5 14.5l9-9 6 6-7.5 7.5H9z"/></svg>',
    "undo": '<svg viewBox="0 0 24 24"><path d="M9 7L4 12l5 5"/><path d="M4 12h11a5 5 0 010 10h-2"/></svg>',
    "redo": '<svg viewBox="0 0 24 24"><path d="M15 7l5 5-5 5"/><path d="M20 12H9a5 5 0 000 10h2"/></svg>',
    "finger": '<svg viewBox="0 0 24 24"><path d="M9 11V5a1.5 1.5 0 013 0v6"/><path d="M12 10.5V9a1.5 1.5 0 013 0v2"/><path d="M15 11a1.5 1.5 0 013 0v3a6 6 0 01-6 6h-1a6 6 0 01-5-3l-2-3.5a1.5 1.5 0 012.5-1.6L9 13"/></svg>',
    "add": '<svg viewBox="0 0 24 24"><rect x="5" y="3" width="14" height="18" rx="2"/><path d="M12 9v6M9 12h6"/></svg>',
    "trash": '<svg viewBox="0 0 24 24"><path d="M4 7h16M10 11v6M14 11v6M6 7l1 13h10l1-13M9 7V4h6v3"/></svg>',
    "q": '<svg viewBox="0 0 24 24"><rect x="4" y="4" width="16" height="16" rx="3"/><path d="M9.5 9.5a2.5 2.5 0 114 2c-1 .7-1.5 1.2-1.5 2.5M12 17h.01"/></svg>',
}

HTML = f"""
<div class="sheet" id="noteSheet" hidden>
  <header class="top">
    <div class="ttl"><b id="nTitle">Your working</b><small id="nSub">Saved on this device</small></div>
    <button class="tl" id="nQ" type="button" aria-pressed="true" aria-label="Show question">{ICON['q']}</button>
    <button class="tl" id="nUndo" type="button" aria-label="Undo">{ICON['undo']}</button>
    <button class="tl" id="nRedo" type="button" aria-label="Redo">{ICON['redo']}</button>
    <button class="btn pri" id="nDone" type="button">Done</button>
  </header>
  <div class="ntools" role="toolbar" aria-label="Writing tools">
    <button class="tl" data-tool="pen" type="button" aria-label="Pen" aria-pressed="true">{ICON['pen']}</button>
    <button class="tl" data-tool="hl" type="button" aria-label="Highlighter" aria-pressed="false">{ICON['hl']}</button>
    <button class="tl" data-tool="er" type="button" aria-label="Eraser" aria-pressed="false">{ICON['er']}</button>
    <span class="sep"></span>
    <button class="tl" data-col="ink" type="button" aria-label="Black ink" aria-pressed="true"><span class="dot" style="background:var(--fg)"></span></button>
    <button class="tl" data-col="blue" type="button" aria-label="Blue ink" aria-pressed="false"><span class="dot" style="background:#3E7BFA"></span></button>
    <button class="tl" data-col="red" type="button" aria-label="Red ink" aria-pressed="false"><span class="dot" style="background:#E5484D"></span></button>
    <button class="tl" data-col="green" type="button" aria-label="Green ink" aria-pressed="false"><span class="dot" style="background:#2FA36B"></span></button>
    <span class="sep"></span>
    <button class="tl" data-size="1" type="button" aria-label="Fine" aria-pressed="false">S</button>
    <button class="tl" data-size="2" type="button" aria-label="Medium" aria-pressed="true">M</button>
    <button class="tl" data-size="3" type="button" aria-label="Thick" aria-pressed="false">L</button>
    <span class="sep"></span>
    <button class="tl" data-bg="lined" type="button" aria-label="Lined paper" aria-pressed="true">≡</button>
    <button class="tl" data-bg="grid" type="button" aria-label="Grid paper" aria-pressed="false">#</button>
    <button class="tl" data-bg="blank" type="button" aria-label="Blank paper" aria-pressed="false">□</button>
    <span class="sep"></span>
    <button class="tl" id="nFinger" type="button" aria-label="Draw with finger" aria-pressed="false">{ICON['finger']}</button>
    <button class="tl" id="nZoom" type="button" aria-label="Zoom level, tap to reset" style="min-width:52px">100%</button>
    <button class="tl" id="nAdd" type="button" aria-label="Add page">{ICON['add']}</button>
    <button class="tl" id="nClear" type="button" aria-label="Clear this note">{ICON['trash']}</button>
  </div>
  <div class="nq" id="nQBox"><div class="in" id="nQText"></div></div>
  <div class="npages" id="nPages"></div>
</div>
"""

JS = r"""
/* ---------- handwriting notes ---------- */
(function(){
var NK=KEY+':note:', L=1000, PH=1414;              // logical page: 1000 × 1414 (A4)
var COLS={blue:'#3E7BFA',red:'#E5484D',green:'#2FA36B'};
var SIZES={1:2.2,2:3.6,3:6};
var sheet=document.getElementById('noteSheet'), pagesBox=document.getElementById('nPages');
var st={tool:'pen',col:'ink',size:2,finger:false}, note=null, nid=null, undo=[], redo=[], onSave=null;
try{var s=JSON.parse(localStorage.getItem(KEY+':notetools')||'null');if(s)for(var k in s)st[k]=s[k];}catch(e){}
function css(v){return getComputedStyle(document.documentElement).getPropertyValue(v).trim();}
function colOf(c){return c==='ink'?css('--fg'):(COLS[c]||c);}
function load(id){try{var n=JSON.parse(localStorage.getItem(NK+id)||'null');if(n&&n.pages)return n;}catch(e){}return {bg:'lined',pages:[[]]};}
function hasInk(n){return n.pages.some(function(p){return p.length;});}
var saveT;
function save(){clearTimeout(saveT);saveT=setTimeout(function(){
  var sub=document.getElementById('nSub');
  try{ if(hasInk(note)) localStorage.setItem(NK+nid,JSON.stringify(note)); else localStorage.removeItem(NK+nid);
    sub.textContent='Saved on this device';
  }catch(e){ sub.textContent='Storage full: clear an old note to keep saving'; }
  if(onSave)onSave();},350);}
function saveTools(){try{localStorage.setItem(KEY+':notetools',JSON.stringify(st));}catch(e){}}

/* drawing */
function paintBg(ctx,bg){
  ctx.fillStyle=css('--surface');ctx.fillRect(0,0,L,PH);
  ctx.strokeStyle=css('--line');ctx.lineWidth=1.2;ctx.beginPath();
  if(bg==='lined'){for(var y=110;y<PH-40;y+=44){ctx.moveTo(40,y);ctx.lineTo(L-40,y);}}
  if(bg==='grid'){for(var x=0;x<=L;x+=40){ctx.moveTo(x,0);ctx.lineTo(x,PH);}for(var y2=0;y2<=PH;y2+=40){ctx.moveTo(0,y2);ctx.lineTo(L,y2);}}
  ctx.stroke();
}
function drawStroke(ctx,s){
  var p=s.p;if(!p.length)return;
  ctx.lineCap='round';ctx.lineJoin='round';ctx.strokeStyle=colOf(s.c);
  if(s.t==='h'){ctx.globalAlpha=.32;ctx.lineWidth=s.w;ctx.beginPath();ctx.moveTo(p[0],p[1]);
    for(var i=3;i<p.length;i+=3)ctx.lineTo(p[i],p[i+1]);if(p.length===3)ctx.lineTo(p[0]+.1,p[1]);ctx.stroke();ctx.globalAlpha=1;return;}
  if(p.length===3){ctx.fillStyle=ctx.strokeStyle;ctx.beginPath();ctx.arc(p[0],p[1],s.w*(.35+p[2]/10)/2,0,7);ctx.fill();return;}
  for(var j=3;j<p.length;j+=3){ctx.lineWidth=s.w*(.35+(p[j+2]+p[j-1])/20);ctx.beginPath();
    var mx=(p[j-3]+p[j])/2,my=(p[j-2]+p[j+1])/2;
    if(j>3){ctx.moveTo((p[j-6]+p[j-3])/2,(p[j-5]+p[j-2])/2);ctx.quadraticCurveTo(p[j-3],p[j-2],mx,my);}else{ctx.moveTo(p[0],p[1]);ctx.lineTo(mx,my);}
    if(j===p.length-3)ctx.lineTo(p[j],p[j+1]);ctx.stroke();}
}
function render(ctx,page,bg){paintBg(ctx,bg);page.forEach(function(s){drawStroke(ctx,s);});}
function fit(cv){var w=cv.clientWidth||cv.parentNode.clientWidth,d=window.devicePixelRatio||1;
  cv.width=Math.round(w*d);cv.height=Math.round(w*PH/L*d);var ctx=cv.getContext('2d');ctx.setTransform(cv.width/L,0,0,cv.width/L,0,0);return ctx;}

/* pages: one gesture handler on the whole paper area (pen draws; one finger pans; two fingers pinch-zoom) */
var views=[], zoom=1, ZMIN=.5, ZMAX=4;
try{zoom=+localStorage.getItem(KEY+':notezoom')||1;}catch(e){}
function baseW(){return Math.max(240,Math.min(pagesBox.clientWidth-24,900));}
function pageW(){return Math.round(baseW()*zoom);}
function build(){pagesBox.innerHTML='';views=[];
  note.pages.forEach(function(pg,i){
    var wrap=document.createElement('div');wrap.className='npage';
    var cv=document.createElement('canvas');cv.setAttribute('aria-label','Writing page '+(i+1));
    var pn=document.createElement('span');pn.className='pn';pn.textContent=(i+1)+' / '+note.pages.length;
    wrap.appendChild(cv);wrap.appendChild(pn);pagesBox.appendChild(wrap);
    views.push({cv:cv,wrap:wrap,i:i});});
  var h=document.createElement('p');h.className='nhint';
  h.textContent=st.finger?'Finger draws. Pinch with two fingers to zoom.':'Write with Apple Pencil. One finger scrolls, two fingers pinch to zoom.';
  pagesBox.appendChild(h);
  layout();requestAnimationFrame(redrawAll);}
function layout(){var w=pageW();views.forEach(function(v){v.wrap.style.width=w+'px';});paintZoom();}
function fit(cv){var w=cv.clientWidth||pageW(),h=w*PH/L,d=window.devicePixelRatio||1;
  d=Math.min(d,Math.sqrt(16e6/(w*h)));                      // iPad canvas memory limit
  cv.width=Math.round(w*d);cv.height=Math.round(h*d);var ctx=cv.getContext('2d');ctx.setTransform(cv.width/L,0,0,cv.width/L,0,0);return ctx;}
function redraw(v){v.ctx=fit(v.cv);render(v.ctx,note.pages[v.i],note.bg);}
function redrawAll(){views.forEach(redraw);}
window.addEventListener('resize',function(){if(!sheet.hidden){layout();redrawAll();}});
function paintZoom(){var z=document.getElementById('nZoom');if(z)z.textContent=Math.round(zoom*100)+'%';}
function setZoom(z,cx,cy){ // keep the point (cx,cy) in the paper area fixed on screen
  z=Math.max(ZMIN,Math.min(ZMAX,z));var r=pagesBox.getBoundingClientRect(),ox=cx-r.left,oy=cy-r.top;
  var ax=(pagesBox.scrollLeft+ox)/zoom,ay=(pagesBox.scrollTop+oy)/zoom;zoom=z;layout();
  pagesBox.scrollLeft=ax*zoom-ox;pagesBox.scrollTop=ay*zoom-oy;}
var zt;function zoomDone(){clearTimeout(zt);zt=setTimeout(function(){redrawAll();try{localStorage.setItem(KEY+':notezoom',zoom);}catch(e){}},120);}

function viewAt(x,y){for(var i=0;i<views.length;i++){var r=views[i].cv.getBoundingClientRect();
  if(x>=r.left&&x<=r.right&&y>=r.top&&y<=r.bottom)return views[i];}return null;}
function pos(v,e){var r=v.cv.getBoundingClientRect(),k=L/r.width;
  var pr=e.pointerType==='pen'?(e.pressure||.5):.5;return [Math.round((e.clientX-r.left)*k*10)/10,Math.round((e.clientY-r.top)*k*10)/10,Math.round(pr*9)];}

/* iOS: stop Safari treating pen or finger movement as scrolling, text selection or the callout menu.
   Without this a quick vertical stroke after a horizontal one gets cancelled (the "+" problem). */
['touchstart','touchmove'].forEach(function(t){pagesBox.addEventListener(t,function(e){if(e.cancelable)e.preventDefault();},{passive:false});});
sheet.addEventListener('selectstart',function(e){e.preventDefault();});
pagesBox.addEventListener('contextmenu',function(e){e.preventDefault();});

var touches={},mode=null,cur=null,curV=null,drawPid=null,live=null,pan=null,pinch=null;
function nTouch(){return Object.keys(touches).length;}
function pinchInfo(){var k=Object.keys(touches),a=touches[k[0]],b=touches[k[1]];
  return {d:Math.hypot(a.x-b.x,a.y-b.y)||1,x:(a.x+b.x)/2,y:(a.y+b.y)/2};}
function startStroke(v,e){var p=pos(v,e);curV=v;
  if(st.tool==='er'){cur={er:true,removed:[]};erase(v,p);return;}
  cur={t:st.tool==='hl'?'h':'p',c:st.tool==='hl'?'#F5C400':st.col,w:st.tool==='hl'?SIZES[st.size]*5:SIZES[st.size],p:p.slice()};
  if(cur.t==='h')live=note.pages[v.i].slice();
  drawStroke(v.ctx,cur);}
function moveStroke(e){var v=curV,evs=e.getCoalescedEvents?e.getCoalescedEvents():[e];if(!evs.length)evs=[e];
  evs.forEach(function(ev){var p=pos(v,ev);
    if(cur.er){erase(v,p);return;}
    var q=cur.p,n=q.length;if(Math.abs(q[n-3]-p[0])+Math.abs(q[n-2]-p[1])<1.2)return;
    q.push(p[0],p[1],p[2]);
    if(cur.t==='p')drawStroke(v.ctx,{t:'p',c:cur.c,w:cur.w,p:q.slice(Math.max(0,q.length-9))});});
  if(cur.t==='h'){render(v.ctx,live,note.bg);drawStroke(v.ctx,cur);}}
function endStroke(keep){var v=curV;
  if(cur&&keep!==false){
    if(cur.er){if(cur.removed.length){undo.push({k:'er',i:v.i,items:cur.removed});redo=[];}}
    else{note.pages[v.i].push(cur);undo.push({k:'add',i:v.i,s:cur});redo=[];}}
  if(cur&&keep===false&&cur.er)cur.removed.slice().reverse().forEach(function(it){note.pages[v.i].splice(it.at,0,it.s);});
  cur=null;live=null;curV=null;drawPid=null;mode=null;if(v)redraw(v);paintUR();save();}
function erase(v,p){var pg=note.pages[v.i],r=14/Math.min(zoom,2)*1.2,hit=false;
  for(var i=pg.length-1;i>=0;i--){var q=pg[i].p;
    for(var j=0;j<q.length;j+=3){if(Math.abs(q[j]-p[0])<r&&Math.abs(q[j+1]-p[1])<r){cur.removed.push({s:pg[i],at:i});pg.splice(i,1);hit=true;break;}}}
  if(hit)render(v.ctx,pg,note.bg);}

pagesBox.addEventListener('pointerdown',function(e){
  try{var sel=window.getSelection&&window.getSelection();if(sel&&sel.removeAllRanges)sel.removeAllRanges();}catch(x){}
  if(e.pointerType==='pen'&&!st.penSeen){st.penSeen=true;saveTools();}
  var isTouch=e.pointerType==='touch';
  if(isTouch){
    if(mode==='draw'&&!drawIsTouch)return;                       // palm resting while the pen writes
    touches[e.pointerId]={x:e.clientX,y:e.clientY};try{pagesBox.setPointerCapture(e.pointerId);}catch(x){}
    if(nTouch()===2){if(mode==='draw')endStroke(false);var pi=pinchInfo();pinch={d:pi.d,z:zoom};pan=null;mode='pinch';return;}
    if(nTouch()>2)return;
    if(st.penSeen&&!st.finger){mode='pan';pan={x:e.clientX,y:e.clientY,l:pagesBox.scrollLeft,t:pagesBox.scrollTop};return;}
  }
  if(mode==='draw')return;
  var v=viewAt(e.clientX,e.clientY);if(!v)return;
  if(mode==='pan')pan=null;
  e.preventDefault();mode='draw';drawPid=e.pointerId;drawIsTouch=isTouch;
  if(!isTouch){try{pagesBox.setPointerCapture(e.pointerId);}catch(x){}}
  startStroke(v,e);});
var drawIsTouch=false;
pagesBox.addEventListener('pointermove',function(e){
  if(touches[e.pointerId]){touches[e.pointerId]={x:e.clientX,y:e.clientY};
    if(mode==='pinch'&&nTouch()>=2){var pi=pinchInfo();setZoom(pinch.z*pi.d/pinch.d,pi.x,pi.y);
      if(pinch.mx!=null){pagesBox.scrollLeft-=pi.x-pinch.mx;pagesBox.scrollTop-=pi.y-pinch.my;}
      pinch.mx=pi.x;pinch.my=pi.y;e.preventDefault();return;}
    if(mode==='pan'&&pan){pagesBox.scrollLeft=pan.l-(e.clientX-pan.x);pagesBox.scrollTop=pan.t-(e.clientY-pan.y);return;}}
  if(mode==='draw'&&e.pointerId===drawPid&&cur){e.preventDefault();moveStroke(e);}});
function up(e){
  if(touches[e.pointerId]){delete touches[e.pointerId];
    if(mode==='pinch'){if(nTouch()<2){mode=nTouch()?'wait':null;pan=null;zoomDone();}return;}
    if(mode==='wait'&&!nTouch())mode=null;
    if(mode==='pan'){mode=null;pan=null;return;}}
  if(mode==='draw'&&e.pointerId===drawPid)endStroke(true);}
pagesBox.addEventListener('pointerup',up);pagesBox.addEventListener('pointercancel',up);
pagesBox.addEventListener('wheel',function(e){if(!e.ctrlKey)return;e.preventDefault();setZoom(zoom*Math.exp(-e.deltaY/200),e.clientX,e.clientY);zoomDone();},{passive:false});
function paintUR(){document.getElementById('nUndo').disabled=!undo.length;document.getElementById('nRedo').disabled=!redo.length;}
document.getElementById('nUndo').addEventListener('click',function(){var a=undo.pop();if(!a)return;
  if(a.k==='add'){var pg=note.pages[a.i],k=pg.lastIndexOf(a.s);if(k>=0)pg.splice(k,1);}
  if(a.k==='er'){a.items.slice().reverse().forEach(function(it){note.pages[a.i].splice(it.at,0,it.s);});}
  if(a.k==='clear'){note.pages=a.pages;build();}
  if(a.k==='page'){note.pages.pop();build();}
  redo.push(a);if(views[a.i])redraw(views[a.i]);paintUR();save();});
document.getElementById('nRedo').addEventListener('click',function(){var a=redo.pop();if(!a)return;
  if(a.k==='add')note.pages[a.i].push(a.s);
  if(a.k==='er')a.items.forEach(function(it){var pg=note.pages[a.i],k=pg.indexOf(it.s);if(k>=0)pg.splice(k,1);});
  if(a.k==='clear'){note.pages=[[]];build();}
  if(a.k==='page'){note.pages.push([]);build();}
  undo.push(a);if(views[a.i])redraw(views[a.i]);paintUR();save();});

/* toolbar */
function paintTools(){
  sheet.querySelectorAll('[data-tool]').forEach(function(b){b.setAttribute('aria-pressed',b.dataset.tool===st.tool);});
  sheet.querySelectorAll('[data-col]').forEach(function(b){b.setAttribute('aria-pressed',b.dataset.col===st.col);});
  sheet.querySelectorAll('[data-size]').forEach(function(b){b.setAttribute('aria-pressed',+b.dataset.size===+st.size);});
  sheet.querySelectorAll('[data-bg]').forEach(function(b){b.setAttribute('aria-pressed',note&&b.dataset.bg===note.bg);});
  document.getElementById('nFinger').setAttribute('aria-pressed',!!st.finger);}
sheet.querySelectorAll('[data-tool]').forEach(function(b){b.addEventListener('click',function(){st.tool=b.dataset.tool;paintTools();saveTools();});});
sheet.querySelectorAll('[data-col]').forEach(function(b){b.addEventListener('click',function(){st.col=b.dataset.col;if(st.tool!=='pen')st.tool='pen';paintTools();saveTools();});});
sheet.querySelectorAll('[data-size]').forEach(function(b){b.addEventListener('click',function(){st.size=+b.dataset.size;paintTools();saveTools();});});
sheet.querySelectorAll('[data-bg]').forEach(function(b){b.addEventListener('click',function(){note.bg=b.dataset.bg;paintTools();redrawAll();save();});});
document.getElementById('nZoom').addEventListener('click',function(){var r=pagesBox.getBoundingClientRect();setZoom(1,r.left+r.width/2,r.top);zoomDone();});
document.getElementById('nFinger').addEventListener('click',function(){st.finger=!st.finger;paintTools();saveTools();build();});
document.getElementById('nAdd').addEventListener('click',function(){note.pages.push([]);undo.push({k:'page',i:note.pages.length-1});redo=[];build();paintUR();save();
  setTimeout(function(){pagesBox.scrollTop=pagesBox.scrollHeight;},60);});
var clearArm=false,clearBtn=document.getElementById('nClear');
clearBtn.addEventListener('click',function(){
  if(!clearArm){clearArm=true;document.getElementById('nSub').textContent='Tap the bin again to clear every page';setTimeout(function(){clearArm=false;document.getElementById('nSub').textContent='Saved on this device';},3000);return;}
  clearArm=false;undo.push({k:'clear',i:0,pages:note.pages});redo=[];note.pages=[[]];build();paintUR();save();});
var qBtn=document.getElementById('nQ');
qBtn.addEventListener('click',function(){var box=document.getElementById('nQBox');box.hidden=!box.hidden;qBtn.setAttribute('aria-pressed',!box.hidden);});

/* open / close */
function open(id,title,qNode,after){
  nid=id;note=load(id);undo=[];redo=[];onSave=after;
  document.getElementById('nTitle').textContent=title;document.getElementById('nSub').textContent='Saved on this device';
  var qt=document.getElementById('nQText');qt.innerHTML='';
  if(qNode){qNode.forEach(function(n){var c=n.cloneNode(true);c.querySelectorAll('button,.wrow,.ans,.rvbar').forEach(function(x){x.remove();});qt.appendChild(c);});}
  document.getElementById('nQBox').hidden=!qNode;qBtn.setAttribute('aria-pressed',!!qNode);
  sheet.hidden=false;paintTools();paintUR();build();pagesBox.scrollTop=0;
  if(window.MathJax&&MathJax.typesetPromise)MathJax.typesetPromise([qt]).catch(function(){});}
document.getElementById('nDone').addEventListener('click',function(){clearTimeout(saveT);
  try{if(hasInk(note))localStorage.setItem(NK+nid,JSON.stringify(note));else localStorage.removeItem(NK+nid);}catch(e){}
  sheet.hidden=true;if(onSave)onSave();});

/* thumbnails + buttons on cards */
function thumb(id){var n=load(id);if(!hasInk(n))return null;
  var c=document.createElement('canvas');c.width=360;c.height=Math.round(360*PH/L);var ctx=c.getContext('2d');
  ctx.setTransform(360/L,0,0,360/L,0,0);render(ctx,n.pages[0],n.bg);return {src:c.toDataURL('image/png'),pages:n.pages.length};}
var PEN='<svg viewBox="0 0 24 24"><path d="M4 20l4-1 11-11-3-3L5 16l-1 4z"/><path d="M14 6l3 3"/></svg>';
function attach(anchor,where,id,title,qNodes){
  var row=document.createElement('div');row.className='wrow';
  var b=document.createElement('button');b.type='button';b.className='btn write';
  var img=document.createElement('img');img.className='wthumb';img.alt='Your handwritten working';
  var meta=document.createElement('span');meta.className='wmeta';
  row.appendChild(b);row.appendChild(meta);
  function paint(){var t=thumb(id);
    b.innerHTML=PEN+(t?'Edit your working':'Write your working');
    if(t){img.src=t.src;meta.textContent=t.pages>1?t.pages+' pages':'';if(!img.parentNode)row.appendChild(img);}
    else{if(img.parentNode)img.remove();meta.textContent='';}}
  function go(){open(id,title,qNodes,paint);}
  b.addEventListener('click',go);img.addEventListener('click',go);
  if(where==='before')anchor.parentNode.insertBefore(row,anchor);else anchor.parentNode.insertBefore(row,anchor.nextSibling);
  paint();}
cards.forEach(function(c){
  var title=c.dataset.title, cid=c.dataset.id;
  if(c.dataset.kind==='Worked example'){
    var ci=c.querySelector('.ci'),first=ci.querySelector('ol.steps');
    if(first){var q=[].slice.call(ci.children).filter(function(n){return n.matches('p:not(.sec),.tw,figure,.formula');});
      attach(first,'before',cid,title,q);}}
  c.querySelectorAll('.pq').forEach(function(pq,i){var qt=pq.querySelector('.qt');if(!qt)return;
    var lab=pq.querySelector('.qh span');attach(qt,'after',cid+'-q'+(i+1),(lab?lab.textContent:'Question '+(i+1)),[qt]);});
});
})();
"""
