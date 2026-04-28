"""
Web generator — reads from data/*.json and builds a fully interactive static web app.
No Python files needed to use the course — everything runs in the browser.

Run: python3 generator_web.py
Output: web/
"""
import pathlib, json, html, random

# ── Helpers ───────────────────────────────────────────────────────────────────

def esc(s): return html.escape(str(s))

def load_lessons():
    data = pathlib.Path("data")
    lessons  = []
    articles = []
    for f in sorted(data.glob("[0-9][0-9]_*.json")):
        d = json.loads(f.read_text(encoding="utf-8"))
        d.setdefault("is_article", False)
        lessons.append(d)
    for f in sorted((data / "articles").glob("*.json")):
        d = json.loads(f.read_text(encoding="utf-8"))
        d["is_article"] = True
        articles.append(d)
    return lessons, articles

def make_mc_quiz(vocab, n=10):
    if len(vocab) < 4: return []
    items = random.sample(vocab, min(n, len(vocab)))
    all_en = [v["en"] for v in vocab]
    out = []
    for item in items:
        wrong = [e for e in all_en if e != item["en"]]
        opts  = random.sample(wrong, min(3, len(wrong))) + [item["en"]]
        random.shuffle(opts)
        out.append({"type": "mc", "prompt": item["cz"], "options": opts, "answer": item["en"]})
    return out

# ── CSS ───────────────────────────────────────────────────────────────────────

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
:root{--bg:#0f0f17;--surface:#1a1a2e;--surface2:#252540;--border:#2e2e50;
  --text:#e2e4f0;--muted:#6b6d8a;--accent:#7c9ef5;--green:#6fcf97;
  --yellow:#f2c94c;--red:#eb5757;--purple:#bb87fc;
  --shadow:0 4px 24px rgba(0,0,0,.4);--shadow-sm:0 2px 8px rgba(0,0,0,.3);
  --grad:linear-gradient(135deg,#7c9ef5 0%,#bb87fc 100%)}
body.light{--bg:#f5f6fa;--surface:#ffffff;--surface2:#eef0f8;--border:#dde1f0;
  --text:#1a1c2e;--muted:#8890b0;--accent:#4a6cf7;--green:#27ae60;
  --yellow:#e6a817;--red:#e53935;--purple:#7c3aed;
  --shadow:0 4px 24px rgba(100,120,200,.12);--shadow-sm:0 2px 8px rgba(100,120,200,.08);
  --grad:linear-gradient(135deg,#4a6cf7 0%,#7c3aed 100%)}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--text);
  font-family:'Inter',system-ui,sans-serif;line-height:1.65;min-height:100vh}
a{color:var(--accent);text-decoration:none}
a:hover{text-decoration:underline}
button{cursor:pointer;font-family:inherit}
::selection{background:var(--accent);color:#fff}
/* Header */
header{background:var(--surface);border-bottom:1px solid var(--border);
  padding:.75rem 2rem;display:flex;align-items:center;justify-content:space-between;
  gap:.8rem;position:sticky;top:0;z-index:100;flex-wrap:wrap;box-shadow:var(--shadow-sm)}
.logo{font-weight:700;font-size:1.05rem;letter-spacing:-.01em}
.logo a{color:var(--text)}
.hdr-nav{display:flex;gap:.4rem;align-items:center;flex-wrap:wrap}
.btn{background:var(--surface2);border:1px solid var(--border);color:var(--text);
  padding:.35rem .8rem;border-radius:8px;font-size:.82rem;font-weight:500;transition:all .15s}
.btn:hover{border-color:var(--accent);color:var(--accent)}
.btn-accent{background:var(--grad);color:#fff;border:none;font-weight:600;
  box-shadow:0 2px 12px rgba(124,158,245,.35)}
.btn-accent:hover{opacity:.9}
#search-input{background:var(--surface2);border:1px solid var(--border);color:var(--text);
  padding:.35rem .9rem;border-radius:8px;font-size:.85rem;width:190px;outline:none;
  transition:border-color .15s}
#search-input:focus{border-color:var(--accent)}
/* Layout */
main{max-width:980px;margin:0 auto;padding:2rem 1.5rem 5rem}
/* Hero */
.hero{background:var(--surface);border:1px solid var(--border);border-radius:16px;
  padding:2rem;margin-bottom:2rem;box-shadow:var(--shadow);
  background-image:radial-gradient(ellipse at 80% 0%,rgba(124,158,245,.08),transparent 60%)}
.hero h1{font-size:1.8rem;font-weight:700;letter-spacing:-.02em;margin-bottom:.5rem;
  background:var(--grad);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.hero-sub{color:var(--muted);font-size:.92rem;margin-bottom:1.2rem}
.hero-stats{display:flex;gap:1.5rem;flex-wrap:wrap}
.stat .stat-num{font-size:1.6rem;font-weight:700;color:var(--accent);line-height:1.1}
.stat .stat-label{font-size:.75rem;color:var(--muted)}
/* Section title */
.section-title{font-size:1rem;font-weight:700;padding:.4rem 0;margin:2rem 0 .7rem;
  display:flex;align-items:center;gap:.6rem}
.section-title::before{content:'';display:block;width:4px;height:1.1em;
  background:var(--grad);border-radius:2px}
.section-count{font-size:.76rem;color:var(--muted);font-weight:400;margin-left:auto}
/* Grid */
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(265px,1fr));gap:.8rem}
.card{background:var(--surface);border:1px solid var(--border);border-radius:12px;
  padding:1.1rem 1.2rem;transition:all .2s;display:block;
  text-decoration:none!important;color:var(--text)!important;box-shadow:var(--shadow-sm)}
.card:hover{border-color:var(--accent);transform:translateY(-3px);
  box-shadow:0 8px 32px rgba(124,158,245,.2)}
.card-num{font-size:.72rem;color:var(--muted);font-weight:600;
  text-transform:uppercase;letter-spacing:.05em;margin-bottom:.25rem}
.card-title{font-size:.93rem;font-weight:600;margin-bottom:.3rem;letter-spacing:-.01em}
.card-level{font-size:.72rem;color:var(--yellow);font-weight:600;margin-bottom:.3rem}
.card-topics{font-size:.71rem;color:var(--muted);margin-bottom:.7rem}
.progress-bar{height:3px;background:var(--border);border-radius:2px;overflow:hidden}
.progress-fill{height:100%;background:var(--grad);border-radius:2px;
  transition:width .6s cubic-bezier(.4,0,.2,1);width:0%}
/* Lesson */
.lesson-header{margin-bottom:1.5rem}
.lesson-header h1{font-size:1.5rem;font-weight:700;letter-spacing:-.02em;margin-bottom:.5rem}
.lesson-meta{display:flex;gap:.5rem;flex-wrap:wrap;font-size:.8rem}
.course-progress{background:var(--surface);border:1px solid var(--border);
  border-radius:10px;padding:.7rem 1.1rem;margin-bottom:1.2rem;
  display:flex;align-items:center;gap:.9rem;font-size:.82rem;box-shadow:var(--shadow-sm)}
.cp-bar{flex:1;height:6px;background:var(--border);border-radius:3px;overflow:hidden}
.cp-fill{height:100%;background:var(--grad);border-radius:3px;
  transition:width .8s cubic-bezier(.4,0,.2,1)}
.desc-box{background:var(--surface);border-left:3px solid var(--accent);
  padding:.8rem 1.1rem;border-radius:0 10px 10px 0;margin-bottom:1.2rem;
  font-size:.9rem;box-shadow:var(--shadow-sm)}
/* Section card */
.section{background:var(--surface);border:1px solid var(--border);border-radius:12px;
  padding:1.2rem;margin-bottom:1rem;box-shadow:var(--shadow-sm)}
.section h2{font-size:.95rem;font-weight:700;color:var(--accent);margin-bottom:.9rem;
  display:flex;align-items:center;gap:.4rem}
/* Vocabulary */
.vocab-table{width:100%;border-collapse:collapse}
.vocab-table tr{transition:background .12s}
.vocab-table tr:hover{background:var(--surface2)}
.vocab-table tr:not(:last-child){border-bottom:1px solid var(--border)}
.vocab-table td{padding:.4rem .3rem;font-size:.87rem;vertical-align:middle}
.vocab-en{font-weight:600;width:44%}
.vocab-cz{color:var(--green);width:44%;font-weight:500;transition:opacity .2s}
.vocab-toggle{background:none;border:1px solid var(--border);color:var(--muted);
  font-size:.72rem;padding:.15rem .45rem;border-radius:5px;transition:all .12s}
.vocab-toggle:hover{color:var(--accent);border-color:var(--accent)}
.hidden-cz{opacity:0;pointer-events:none}
/* Dialogue */
.dialogue{display:flex;flex-direction:column;gap:.6rem}
.bubble{padding:.55rem 1rem;border-radius:14px;font-size:.87rem;max-width:82%;line-height:1.5}
.bubble-a{background:var(--accent);color:#fff;align-self:flex-start;
  box-shadow:0 2px 12px rgba(124,158,245,.3)}
.bubble-b{background:var(--surface2);border:1px solid var(--border);align-self:flex-end}
.bubble-speaker{font-size:.7rem;font-weight:700;margin-bottom:.15rem;opacity:.75;
  text-transform:uppercase;letter-spacing:.04em}
/* Notes */
.note{background:var(--surface2);border-radius:8px;padding:.45rem .9rem;
  font-size:.83rem;font-family:'JetBrains Mono','Fira Code',monospace;
  margin-bottom:.4rem;color:var(--yellow);border-left:3px solid var(--yellow)}
/* Examples */
.example-row{margin-bottom:.7rem;padding-bottom:.7rem;border-bottom:1px solid var(--border)}
.example-row:last-child{border-bottom:none;margin-bottom:0}
.example-en{font-weight:600;font-size:.89rem}
.example-cz{color:var(--muted);font-size:.82rem;margin-top:.15rem}
/* Quiz */
.quiz-q{background:var(--surface);border:1px solid var(--border);border-radius:12px;
  padding:1.2rem;margin-bottom:.9rem;box-shadow:var(--shadow-sm);
  animation:fadeIn .25s ease}
@keyframes fadeIn{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}
.quiz-prompt{font-weight:700;font-size:1rem;margin-bottom:.9rem;letter-spacing:-.01em}
.quiz-counter{font-size:.72rem;color:var(--muted);float:right;margin-top:.1rem}
.quiz-options{display:grid;grid-template-columns:1fr 1fr;gap:.5rem}
.quiz-opt{background:var(--surface2);border:1.5px solid var(--border);
  padding:.6rem .9rem;border-radius:10px;font-size:.87rem;text-align:left;
  color:var(--text);font-weight:500;transition:all .15s;line-height:1.3}
.quiz-opt:hover:not(:disabled){border-color:var(--accent);background:var(--surface);
  transform:translateY(-1px)}
.quiz-opt.correct{background:rgba(111,207,151,.15);border-color:var(--green);
  color:var(--green);font-weight:600}
.quiz-opt.wrong{background:rgba(235,87,87,.12);border-color:var(--red);color:var(--red)}
.quiz-opt:disabled{cursor:default;transform:none}
.fill-blank{display:flex;align-items:center;gap:.5rem;flex-wrap:wrap}
.fill-blank input{background:var(--surface2);border:1.5px solid var(--border);
  color:var(--text);padding:.45rem .8rem;border-radius:8px;font-size:.87rem;
  outline:none;transition:border-color .15s;min-width:150px}
.fill-blank input:focus{border-color:var(--accent)}
.fill-blank .check-btn{background:var(--grad);border:none;color:#fff;
  padding:.45rem 1rem;border-radius:8px;font-size:.85rem;font-weight:600;
  box-shadow:0 2px 10px rgba(124,158,245,.3)}
.quiz-result{margin-top:.5rem;font-size:.85rem;font-weight:600}
.quiz-score{background:var(--surface);border:1px solid var(--border);border-radius:14px;
  padding:1.8rem;text-align:center;box-shadow:var(--shadow);animation:fadeIn .3s ease}
.score-num{font-size:2.8rem;font-weight:700;background:var(--grad);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;line-height:1}
.score-pct{font-size:1.1rem;color:var(--muted);margin-top:.2rem}
.score-msg{font-size:.95rem;margin-top:.6rem;font-weight:600}
/* Tasks */
.tasks-list{padding-left:1.3rem}
.tasks-list li{margin-bottom:.4rem;font-size:.88rem;line-height:1.5}
/* Article */
.article-text{font-size:.92rem;line-height:1.8;white-space:pre-line;
  border-left:3px solid var(--accent);padding-left:1.2rem;color:var(--text)}
.comprehension-q{margin-bottom:1rem;padding-bottom:1rem;border-bottom:1px solid var(--border)}
.comprehension-q:last-child{border-bottom:none}
.comprehension-q p{font-size:.9rem;font-weight:600;margin-bottom:.4rem}
.comprehension-q input{background:var(--surface2);border:1.5px solid var(--border);
  color:var(--text);padding:.4rem .8rem;border-radius:8px;font-size:.85rem;
  width:100%;max-width:420px;outline:none;transition:border-color .15s}
.comprehension-q input:focus{border-color:var(--accent)}
.model-answer{margin-top:.4rem;font-size:.83rem;color:var(--green);
  display:none;font-weight:600}
.show-answer{background:none;border:1px solid var(--border);color:var(--muted);
  font-size:.74rem;padding:.2rem .55rem;border-radius:5px;margin-left:.5rem;
  transition:all .12s}
.show-answer:hover{color:var(--accent);border-color:var(--accent)}
/* Flashcards */
.fc-area{display:flex;flex-direction:column;align-items:center;padding:1.5rem 0}
.fc-card{width:min(440px,90vw);height:220px;perspective:1200px;
  cursor:pointer;margin-bottom:1.5rem}
.fc-inner{width:100%;height:100%;position:relative;transform-style:preserve-3d;
  transition:transform .5s cubic-bezier(.4,0,.2,1)}
.fc-card.flipped .fc-inner{transform:rotateY(180deg)}
.fc-front,.fc-back{position:absolute;width:100%;height:100%;backface-visibility:hidden;
  border-radius:16px;display:flex;flex-direction:column;align-items:center;
  justify-content:center;padding:1.8rem;text-align:center;
  border:2px solid var(--border);box-shadow:var(--shadow)}
.fc-front{background:var(--surface)}
.fc-back{background:var(--surface2);transform:rotateY(180deg);border-color:var(--green)}
.fc-word{font-size:1.6rem;font-weight:700;letter-spacing:-.02em}
.fc-hint{font-size:.74rem;color:var(--muted);margin-top:.6rem}
.fc-translation{font-size:1.4rem;font-weight:700;color:var(--green)}
.fc-controls{display:flex;gap:.7rem;flex-wrap:wrap;justify-content:center}
.fc-counter{color:var(--muted);font-size:.84rem;margin-bottom:.6rem}
/* Progress */
.progress-row{display:flex;align-items:center;gap:.7rem;padding:.55rem .2rem;
  border-bottom:1px solid var(--border);font-size:.85rem;transition:background .1s}
.progress-row:hover{background:var(--surface2)}
.progress-status{font-size:1rem;width:1.6rem;text-align:center}
.progress-title{flex:1;font-weight:500}
.progress-pct{font-size:.78rem;color:var(--muted);min-width:38px;text-align:right}
.mini-bar{width:70px;height:5px;background:var(--border);border-radius:3px;overflow:hidden}
.mini-fill{height:100%;border-radius:3px;background:var(--grad)}
.streak-box{background:var(--surface);border:1px solid var(--border);border-radius:14px;
  padding:1.4rem;margin-bottom:1.5rem;display:flex;gap:2rem;align-items:center;
  box-shadow:var(--shadow)}
.streak-num{font-size:3rem;font-weight:700;color:var(--yellow);line-height:1}
/* Nav */
.lesson-nav{display:flex;justify-content:space-between;margin-top:1.8rem;
  padding-top:1rem;border-top:1px solid var(--border)}
.lesson-nav a{background:var(--surface);border:1px solid var(--border);
  padding:.5rem 1rem;border-radius:8px;font-size:.85rem;color:var(--accent);
  max-width:46%;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;
  font-weight:500;transition:all .15s;box-shadow:var(--shadow-sm)}
.lesson-nav a:hover{border-color:var(--accent);text-decoration:none;transform:translateY(-1px)}
/* Footer */
footer{text-align:center;padding:2rem;color:var(--muted);font-size:.77rem;
  border-top:1px solid var(--border)}
/* Utilities */
.hidden{display:none!important}
.tag{background:var(--surface2);border:1px solid var(--border);border-radius:20px;
  padding:.15rem .6rem;font-size:.73rem;color:var(--muted);font-weight:500}
.tag-level{background:rgba(242,201,76,.1);border-color:rgba(242,201,76,.3);color:var(--yellow)}
.tag-accent{background:rgba(124,158,245,.12);border-color:rgba(124,158,245,.3);color:var(--accent)}
.alert{background:rgba(242,201,76,.08);border:1px solid rgba(242,201,76,.3);
  border-radius:10px;padding:.8rem 1.1rem;font-size:.87rem;margin-bottom:1rem;color:var(--yellow)}
/* ─ Audio button ─ */
.audio-btn{background:none;border:none;color:var(--muted);font-size:.85rem;
  padding:0 .25rem;cursor:pointer;transition:color .12s;vertical-align:middle}
.audio-btn:hover{color:var(--accent)}
/* ─ PWA banner ─ */
.pwa-banner{display:none;align-items:center;justify-content:space-between;
  background:var(--surface);border:1px solid var(--accent);border-radius:10px;
  padding:.7rem 1rem;margin-bottom:1rem;gap:.8rem;flex-wrap:wrap}
.pwa-banner p{font-size:.88rem;color:var(--text)}
/* ─ Daily challenge ─ */
.daily-card{background:linear-gradient(135deg,rgba(124,158,245,.15),rgba(187,135,252,.1));
  border:1px solid rgba(124,158,245,.3);border-radius:14px;padding:1.2rem 1.5rem;
  margin-bottom:1.8rem;display:flex;align-items:center;gap:1.2rem}
.daily-emoji{font-size:2.2rem}
.daily-label{font-size:.75rem;color:var(--accent);font-weight:700;
  text-transform:uppercase;letter-spacing:.06em;margin-bottom:.2rem}
.daily-title{font-size:1rem;font-weight:700}
.daily-level{font-size:.78rem;color:var(--muted);margin-top:.15rem}
@media(max-width:600px){
  main{padding:1rem 1rem 4rem}
  .quiz-options{grid-template-columns:1fr}
  header{padding:.6rem 1rem}
  .hero h1{font-size:1.4rem}
  #search-input{width:120px}
  .daily-card{flex-direction:column;align-items:flex-start}
}
"""

# ── JavaScript ────────────────────────────────────────────────────────────────

JS_BASE = """
// ─ Theme ─
const themeBtn = document.getElementById('theme-btn');
if(localStorage.getItem('theme')==='light') document.body.classList.add('light');
function syncBtn(){ if(themeBtn) themeBtn.textContent = document.body.classList.contains('light')? '🌙 Dark':'☀️ Light'; }
syncBtn();
if(themeBtn) themeBtn.addEventListener('click',()=>{ document.body.classList.toggle('light'); localStorage.setItem('theme',document.body.classList.contains('light')?'light':'dark'); syncBtn(); });

// ─ Progress ─
function getScore(s){ return JSON.parse(localStorage.getItem('score_'+s)||'null'); }
function setScore(s,score,total){ const p=getScore(s); if(!p||score>=p.score){ localStorage.setItem('score_'+s,JSON.stringify({score,total,date:new Date().toISOString().slice(0,10)})); } const f=document.querySelector('.progress-fill[data-slug="'+s+'"]'); if(f) f.style.width=Math.round(score/total*100)+'%'; }

// ─ Streak ─
function checkStreak(){ const today=new Date().toISOString().slice(0,10); const d=JSON.parse(localStorage.getItem('streak_data')||'{"days":[],"longest":0}'); if(!d.days.includes(today)){ d.days.push(today); d.days.sort(); let s=1; for(let i=d.days.length-2;i>=0;i--){ const a=new Date(d.days[i]),b=new Date(d.days[i+1]); if((b-a)/86400000===1)s++; else break; } d.longest=Math.max(d.longest||0,s); localStorage.setItem('streak_data',JSON.stringify(d)); } }
checkStreak();

// ─ Audio pronunciation ─
function speak(text){
  if(!('speechSynthesis' in window)) return;
  window.speechSynthesis.cancel();
  const u = new SpeechSynthesisUtterance(text);
  u.lang = 'en-GB'; u.rate = 0.85; u.pitch = 1;
  window.speechSynthesis.speak(u);
}

// ─ Bookmarks ─
function getBookmarks(){ return JSON.parse(localStorage.getItem('bookmarks')||'[]'); }
function isBookmarked(slug){ return getBookmarks().includes(slug); }
function toggleBookmark(slug){
  const bm = getBookmarks();
  const idx = bm.indexOf(slug);
  if(idx>=0) bm.splice(idx,1); else bm.push(slug);
  localStorage.setItem('bookmarks', JSON.stringify(bm));
  const btn = document.getElementById('bm-btn');
  if(btn){ btn.textContent = bm.includes(slug) ? '★ Saved' : '☆ Save'; btn.classList.toggle('btn-accent', bm.includes(slug)); }
}
function initBookmarkBtn(){
  const btn = document.getElementById('bm-btn');
  if(!btn || !window.LESSON_SLUG) return;
  if(isBookmarked(window.LESSON_SLUG)){ btn.textContent='★ Saved'; btn.classList.add('btn-accent'); }
}
initBookmarkBtn();

// ─ PWA install ─
let deferredPrompt;
window.addEventListener('beforeinstallprompt', e => {
  e.preventDefault(); deferredPrompt = e;
  const banner = document.getElementById('pwa-banner');
  if(banner) banner.style.display = 'flex';
});
function installPWA(){
  if(!deferredPrompt) return;
  deferredPrompt.prompt();
  deferredPrompt.userChoice.then(()=>{ deferredPrompt=null; const b=document.getElementById('pwa-banner'); if(b) b.style.display='none'; });
}
"""

JS_INDEX = """
const s=document.getElementById('search-input');
if(s){ s.addEventListener('input',()=>{ const q=s.value.toLowerCase(); document.querySelectorAll('.card').forEach(c=>{ c.style.display=(!q||c.textContent.toLowerCase().includes(q))?'':'none'; }); }); }
document.querySelectorAll('.progress-fill[data-slug]').forEach(f=>{ const sc=getScore(f.dataset.slug); if(sc) f.style.width=Math.round(sc.score/sc.total*100)+'%'; });
"""

JS_LESSON = """
function toggleCz(btn){ const td=btn.closest('tr').querySelector('.vocab-cz'); if(td.classList.contains('hidden-cz')){ td.classList.remove('hidden-cz'); btn.textContent='Hide'; } else { td.classList.add('hidden-cz'); btn.textContent='Show'; } }
function toggleAllCz(){ const all=document.querySelectorAll('.vocab-cz'); const h=[...all].every(t=>t.classList.contains('hidden-cz')); all.forEach(t=>{ h?t.classList.remove('hidden-cz'):t.classList.add('hidden-cz'); }); document.getElementById('toggle-all-btn').textContent=h?'Hide all':'Show all'; }
function showModelAnswer(btn){ const el=btn.nextElementSibling; if(el){ el.style.display='block'; btn.style.display='none'; } }
const QUIZ=window.QUIZ_DATA||[]; let qIdx=0,correct=0;
function escH(s){ const d=document.createElement('div'); d.textContent=s; return d.innerHTML; }
function renderQuiz(){ const c=document.getElementById('quiz-area'); if(!c||!QUIZ.length) return; if(qIdx>=QUIZ.length){ showScore(); return; } const q=QUIZ[qIdx]; c.innerHTML=''; const div=document.createElement('div'); div.className='quiz-q';
  if(q.type==='mc'){ div.innerHTML='<div class="quiz-prompt">'+escH(q.prompt)+'<span class="quiz-counter">'+escH(qIdx+1+'/'+QUIZ.length)+'</span></div><div class="quiz-options"></div>'; const opts=div.querySelector('.quiz-options'); q.options.forEach(opt=>{ const btn=document.createElement('button'); btn.className='quiz-opt'; btn.textContent=opt; btn.addEventListener('click',()=>checkMC(btn,opt,q.answer,div)); opts.appendChild(btn); }); }
  else if(q.type==='fill'){ const parts=q.sentence.split('___'); div.innerHTML='<div class="quiz-prompt">'+escH(qIdx+1+'/'+QUIZ.length)+'</div><div class="fill-blank">'+escH(parts[0])+'<input id="fi" autocomplete="off" placeholder="answer...">'+escH(parts[1]||'')+'<button class="check-btn" onclick="checkFill()">Check</button></div><div class="quiz-result" id="fb"></div>'; }
  c.appendChild(div); }
function checkMC(btn,chosen,ans,div){ div.querySelectorAll('.quiz-opt').forEach(b=>{ b.disabled=true; if(b.textContent===ans) b.classList.add('correct'); }); if(chosen===ans){btn.classList.add('correct');correct++;} else btn.classList.add('wrong'); qIdx++; setTimeout(renderQuiz,900); }
function checkFill(){ const inp=document.getElementById('fi'); const fb=document.getElementById('fb'); if(!inp)return; const q=QUIZ[qIdx]; const ok=inp.value.trim().toLowerCase()===q.answer.toLowerCase(); if(ok){fb.innerHTML='<span style="color:var(--green)">✓ Correct!</span>';correct++;} else{fb.innerHTML='<span style="color:var(--red)">✗ Answer: <strong>'+escH(q.answer)+'</strong></span>';} inp.disabled=true; inp.closest('.fill-blank').querySelector('.check-btn').disabled=true; qIdx++; setTimeout(renderQuiz,1000); }
function showScore(){ const c=document.getElementById('quiz-area'); if(!c)return; const pct=Math.round(correct/QUIZ.length*100); const msg=pct>=90?'🏆 Excellent!':pct>=70?'👍 Good job!':pct>=50?'📖 Keep practising!':'💪 Review and try again!'; c.innerHTML='<div class="quiz-score"><div class="score-num">'+correct+'/'+QUIZ.length+'</div><div class="score-pct">'+pct+'%</div><div class="score-msg">'+msg+'</div><button class="btn btn-accent" style="margin-top:.8rem" onclick="restartQuiz()">Restart</button></div>'; setScore(window.LESSON_SLUG,correct,QUIZ.length); }
function restartQuiz(){ qIdx=0; correct=0; renderQuiz(); }
renderQuiz();
"""

JS_FC = """
const ALL=window.FC_DATA||[]; let cards=[...ALL],idx=0,ok=0,mode='cz-en';
function shuffle(a){ return [...a].sort(()=>Math.random()-.5); }

// ─ Spaced repetition (simplified SM-2) ─
function getSR(){ return JSON.parse(localStorage.getItem('sr_data')||'{}'); }
function saveSR(d){ localStorage.setItem('sr_data', JSON.stringify(d)); }
function updateSR(word, knew){
  const d = getSR();
  const k = btoa(encodeURIComponent(word)).slice(0,20);
  const c = d[k] || {interval:1, ef:2.5, reps:0};
  if(knew){ c.reps++; c.interval = c.reps===1?1:c.reps===2?6:Math.round(c.interval*c.ef); c.ef = Math.max(1.3, c.ef+(0.1-(5-4)*(0.08+(5-4)*0.02))); }
  else { c.reps=0; c.interval=1; c.ef=Math.max(1.3,c.ef-0.2); }
  c.next = new Date(Date.now()+c.interval*86400000).toISOString().slice(0,10);
  d[k]=c; saveSR(d);
}
function isDue(word){
  const d=getSR(), k=btoa(encodeURIComponent(word)).slice(0,20);
  const c=d[k]; if(!c) return true;
  return c.next <= new Date().toISOString().slice(0,10);
}

function start(){
  // prioritise due cards, then new cards
  const due   = ALL.filter(c=>isDue(mode==='cz-en'?c.cz:c.en));
  const other = ALL.filter(c=>!isDue(mode==='cz-en'?c.cz:c.en));
  cards = [...shuffle(due), ...shuffle(other)];
  idx=0; ok=0; render();
}
function render(){
  const card=document.getElementById('fc-card'),ctr=document.getElementById('fc-counter');
  if(!card||!cards.length)return;
  if(idx>=cards.length){done();return;}
  card.classList.remove('flipped');
  const front = mode==='cz-en'?cards[idx].cz:cards[idx].en;
  const back  = mode==='cz-en'?cards[idx].en:cards[idx].cz;
  document.getElementById('fc-front-word').textContent=front;
  document.getElementById('fc-back-word').textContent=back;
  document.getElementById('fc-front-hint').textContent=mode==='cz-en'?'Click / Space to flip':'Click / Space to flip';
  if(ctr) ctr.textContent=(idx+1)+'/'+cards.length;
  // audio button
  const audioBtn = document.getElementById('fc-audio');
  if(audioBtn) audioBtn.onclick = ()=>speak(mode==='cz-en'?back:front);
}
function flip(){ document.getElementById('fc-card').classList.toggle('flipped'); }
function answer(knew){
  const word = mode==='cz-en'?cards[idx]?.en:cards[idx]?.cz;
  if(word) updateSR(word, knew);
  if(knew)ok++; idx++; render();
}
function done(){
  const a=document.getElementById('fc-area'); if(!a)return;
  const pct=Math.round(ok/cards.length*100);
  a.innerHTML='<div class="quiz-score" style="max-width:360px;margin:2rem auto"><div class="score-num">'+ok+'/'+cards.length+'</div><div class="score-pct">'+pct+'% recalled</div><button class="btn btn-accent" style="margin-top:1rem" onclick="start()">New round</button></div>';
}
document.getElementById('fc-card').addEventListener('click',flip);
document.getElementById('mode-btn').addEventListener('click',()=>{ mode=mode==='cz-en'?'en-cz':'cz-en'; document.getElementById('mode-btn').textContent=mode==='cz-en'?'CZ → EN':'EN → CZ'; start(); });
document.querySelectorAll('.fc-filter-btn').forEach(btn=>{ btn.addEventListener('click',()=>{ document.querySelectorAll('.fc-filter-btn').forEach(b=>b.classList.remove('btn-accent')); btn.classList.add('btn-accent'); const lesson=btn.dataset.lesson; const base=lesson==='all'?ALL:ALL.filter(c=>c.lesson===lesson); const due=base.filter(c=>isDue(mode==='cz-en'?c.cz:c.en)); cards=[...shuffle(due),...shuffle(base.filter(c=>!isDue(mode==='cz-en'?c.cz:c.en)))]; idx=0;ok=0;render(); }); });

// ─ Keyboard shortcuts ─
document.addEventListener('keydown',e=>{
  if(e.code==='Space'){ e.preventDefault(); flip(); }
  else if(e.code==='ArrowRight') answer(true);
  else if(e.code==='ArrowLeft')  answer(false);
});
start();
"""

JS_PROGRESS = """
const SLUGS=window.ALL_SLUGS||[];
SLUGS.forEach(({slug})=>{ const s=getScore(slug); const row=document.getElementById('row-'+slug); if(!row||!s)return; const pct=Math.round(s.score/s.total*100); row.querySelector('.progress-status').textContent=pct>=80?'✅':pct>=50?'🔄':'❌'; row.querySelector('.progress-pct').textContent=pct+'%'; row.querySelector('.mini-fill').style.width=pct+'%'; });
const sd=JSON.parse(localStorage.getItem('streak_data')||'{"days":[],"longest":0}');
const today=new Date().toISOString().slice(0,10); let cur=0; if(sd.days.length){ const last=sd.days[sd.days.length-1]; if(last===today||last===(new Date(Date.now()-86400000).toISOString().slice(0,10))){ cur=1; for(let i=sd.days.length-2;i>=0;i--){ const a=new Date(sd.days[i]),b=new Date(sd.days[i+1]); if((b-a)/86400000===1)cur++; else break; } } }
const se=document.getElementById('streak-current'),le=document.getElementById('streak-longest'),te=document.getElementById('streak-total');
if(se)se.textContent=cur; if(le)le.textContent=sd.longest||0; if(te)te.textContent=sd.days.length;
"""

# ── Page wrapper ──────────────────────────────────────────────────────────────

SW_REG = """
if('serviceWorker' in navigator){
  navigator.serviceWorker.register('./sw.js').catch(()=>{});
}
"""

def page(title, body, js_extra="", back="index.html"):
    up = "" if back == "index.html" else "../"
    sw_path = f"{up}sw.js"
    manifest_path = f"{up}manifest.json"
    sw_js = f"""if('serviceWorker' in navigator){{ navigator.serviceWorker.register('{sw_path}').catch(()=>{{}}); }}"""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="theme-color" content="#7c9ef5">
<link rel="manifest" href="{manifest_path}">
<title>{esc(title)} — English Course</title>
<style>{CSS}</style>
</head>
<body>
<header>
  <div class="logo"><a href="{up}index.html">🇬🇧 English Course</a></div>
  <div class="hdr-nav">
    {"" if back=="index.html" else f'<a href="{up}index.html" class="btn">← Home</a>'}
    <a href="{up}flashkarty.html" class="btn">🎴 Flashcards</a>
    <a href="{up}pokrok.html" class="btn">📊 Progress</a>
    <a href="{up}slovnik.html" class="btn">📖 Vocab</a>
    <button class="btn" id="theme-btn">☀️ Light</button>
  </div>
</header>
<main>{body}</main>
<footer>English Interactive Course · A1–C2 · Everything runs in your browser · No Python needed</footer>
<script>{JS_BASE}{js_extra}{sw_js}</script>
</body>
</html>"""

# ── Sections ──────────────────────────────────────────────────────────────────

SECTIONS = [
    ("Basics",              "01","07"),
    ("Grammar — Core",      "08","15"),
    ("Grammar — Intermediate","16","20"),
    ("Everyday Topics",     "21","30"),
    ("Advanced Vocabulary", "31","40"),
    ("Advanced Grammar",    "41","50"),
    ("C1 — Style & Skills", "51","60"),
    ("C1/C2 — Mastery",     "61","80"),
]

def get_section(num):
    for name, s, e in SECTIONS:
        if s <= num <= e: return name
    return "Other"

# ── Index ─────────────────────────────────────────────────────────────────────

def build_index(lessons, articles):
    by_sec = {}
    for les in lessons:
        by_sec.setdefault(get_section(les["num"]), []).append(les)

    sections_html = ""
    for name, _, _ in SECTIONS:
        cards = by_sec.get(name, [])
        if not cards: continue
        grid = ""
        for les in cards:
            grid += f"""<a class="card" href="lekce/{les['slug']}.html" data-slug="{les['slug']}">
  <div class="card-num">Lesson {les['num']}</div>
  <div class="card-title">{esc(les['title'])}</div>
  <div class="card-level">{esc(les['level'])}</div>
  <div class="card-topics">{esc(les['topics'])}</div>
  <div class="progress-bar"><div class="progress-fill" data-slug="{les['slug']}"></div></div>
</a>\n"""
        sections_html += f'<div class="section-title">{name}<span class="section-count">{len(cards)} lessons</span></div>\n<div class="grid">{grid}</div>\n'

    art_grid = "".join(f"""<a class="card" href="clanky/{a['slug']}.html">
  <div class="card-num">Article {a['num']}</div>
  <div class="card-title">{esc(a['title'])}</div>
  <div class="card-level">{esc(a['level'])}</div>
  <div class="card-topics">{esc(a['topics'])}</div>
</a>\n""" for a in articles)
    if art_grid:
        sections_html += f'<div class="section-title">Reading Articles<span class="section-count">{len(articles)} articles</span></div>\n<div class="grid">{art_grid}</div>\n'

    # daily challenge — deterministic pick based on day of year
    import datetime
    day_idx = datetime.date.today().timetuple().tm_yday % len(lessons)
    daily = lessons[day_idx]
    daily_card = f"""<div class="daily-card">
  <div class="daily-emoji">⚡</div>
  <div>
    <div class="daily-label">Today's lesson</div>
    <a href="lekce/{daily['slug']}.html" style="text-decoration:none;color:var(--text)">
      <div class="daily-title">L{daily['num']} — {esc(daily['title'])}</div>
      <div class="daily-level">{esc(daily['level'])} · {esc(daily['topics'])}</div>
    </a>
  </div>
  <a href="lekce/{daily['slug']}.html" class="btn btn-accent" style="margin-left:auto;white-space:nowrap">Start →</a>
</div>"""

    pwa_banner = """<div class="pwa-banner" id="pwa-banner">
  <p>📱 Install this course as an app — works offline too!</p>
  <button class="btn btn-accent" onclick="installPWA()">Install</button>
  <button class="btn" onclick="document.getElementById('pwa-banner').style.display='none'">✕</button>
</div>"""

    hero = f"""<div class="hero">
  <h1>English Interactive Course</h1>
  <p class="hero-sub">Czech → English · A1 to C2 · Interactive quizzes · Runs entirely in your browser</p>
  <div class="hero-stats">
    <div class="stat"><span class="stat-num">{len(lessons)}</span><span class="stat-label">Lessons</span></div>
    <div class="stat"><span class="stat-num">{len(articles)}</span><span class="stat-label">Articles</span></div>
    <div class="stat"><span class="stat-num">A1–C2</span><span class="stat-label">All levels</span></div>
    <div class="stat"><span class="stat-num">0</span><span class="stat-label">Python needed</span></div>
  </div>
</div>
{pwa_banner}
{daily_card}"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>English Interactive Course — A1 to C2</title>
<style>{CSS}</style>
</head>
<body>
<header>
  <div class="logo">🇬🇧 English Course</div>
  <div class="hdr-nav">
    <input id="search-input" type="search" placeholder="🔍 Search..." style="width:160px">
    <a href="flashkarty.html" class="btn">🎴 Flashcards</a>
    <a href="pokrok.html" class="btn">📊 Progress</a>
    <a href="slovnik.html" class="btn">📖 Vocab</a>
    <button class="btn" id="theme-btn">☀️ Light</button>
  </div>
</header>
<main>
{hero}
{sections_html}
</main>
<footer>English Interactive Course · {len(lessons)} lessons · A1–C2 · No Python needed</footer>
<script>{JS_BASE}{JS_INDEX}</script>
</body>
</html>"""

# ── Lesson page ───────────────────────────────────────────────────────────────

def build_lesson(les, prev_l, next_l, total):
    num = int(les["num"])
    pct = int((num - 1) / total * 100)

    # vocabulary
    vocab_rows = "".join(
        f'<tr>'
        f'<td class="vocab-en">'
        f'  <button class="audio-btn" onclick="speak(\'{esc(v["en"])}\')">🔊</button>'
        f'  {esc(v["en"])}'
        f'</td>'
        f'<td class="vocab-cz hidden-cz">{esc(v["cz"])}</td>'
        f'<td><button class="vocab-toggle" onclick="toggleCz(this)">Show</button></td>'
        f'</tr>\n'
        for v in les.get("vocabulary", [])
    )
    vocab_sec = ""
    if vocab_rows:
        vocab_sec = f"""<div class="section">
<h2>📚 Vocabulary
  <button id="toggle-all-btn" class="btn" style="font-size:.75rem;padding:.2rem .6rem;margin-left:auto" onclick="toggleAllCz()">Show all</button>
</h2>
<table class="vocab-table">{vocab_rows}</table>
</div>"""

    # dialogue
    dialogue_sec = ""
    if les.get("dialogue"):
        bubbles = ""
        for d in les["dialogue"]:
            cls = "bubble-a" if d["speaker"] in ("A","Waiter","Doctor","Assistant","Interviewer","Teacher") else "bubble-b"
            bubbles += f'<div class="bubble {cls}"><div class="bubble-speaker">{esc(d["speaker"])}</div>{esc(d["text"])}</div>\n'
        dialogue_sec = f'<div class="section"><h2>💬 Dialogue</h2><div class="dialogue">{bubbles}</div></div>'

    # notes
    notes_sec = ""
    if les.get("notes"):
        items = "".join(f'<div class="note">{esc(n)}</div>' for n in les["notes"][:8])
        notes_sec = f'<div class="section"><h2>📝 Notes</h2>{items}</div>'

    # examples
    examples_sec = ""
    if les.get("examples"):
        rows = "".join(
            f'<div class="example-row"><div class="example-en">{esc(e["en"])}</div>'
            f'<div class="example-cz">→ {esc(e["cz"])}</div></div>'
            for e in les["examples"][:6]
        )
        examples_sec = f'<div class="section"><h2>💬 Examples</h2>{rows}</div>'

    # quiz
    mc = make_mc_quiz(les.get("vocabulary", []))
    fill = [{"type": "fill", **q} for q in les.get("quiz", [])[:5]]
    quiz_data = [{"type": "mc", **q} for q in mc[:8]] + fill
    random.shuffle(quiz_data)
    quiz_sec = ""
    if quiz_data:
        quiz_sec = '<div class="section"><h2>🎯 Quiz</h2><div id="quiz-area"></div></div>'

    # tasks
    tasks_sec = ""
    if les.get("tasks"):
        items = "".join(f"<li>{esc(t)}</li>" for t in les["tasks"])
        tasks_sec = f'<div class="section"><h2>✏️ Your Tasks</h2><ul class="tasks-list">{items}</ul></div>'

    prev_link = f'<a href="{prev_l["slug"]}.html">← {esc(prev_l["title"])}</a>' if prev_l else "<span></span>"
    next_link = f'<a href="{next_l["slug"]}.html">{esc(next_l["title"])} →</a>' if next_l else "<span></span>"

    body = f"""
<div class="lesson-header">
  <h1>{esc(les['title'])}</h1>
  <div class="lesson-meta">
    <span class="tag tag-accent">Lesson {les['num']}</span>
    <span class="tag tag-level">{esc(les['level'])}</span>
    <span style="color:var(--muted);font-size:.8rem">{esc(les['topics'])}</span>
    <button id="bm-btn" class="btn" style="margin-left:auto;font-size:.8rem" onclick="toggleBookmark('{les['slug']}')">☆ Save</button>
  </div>
</div>
<div class="course-progress">
  <span>Progress</span>
  <div class="cp-bar"><div class="cp-fill" style="width:{pct}%"></div></div>
  <span>{num}/{total}</span>
</div>
{('<div class="desc-box">'+esc(les['description'])+'</div>') if les.get('description') else ''}
{vocab_sec}{dialogue_sec}{notes_sec}{examples_sec}{quiz_sec}{tasks_sec}
<div class="lesson-nav">{prev_link}{next_link}</div>
"""
    js = f"window.LESSON_SLUG='{les['slug']}';\nwindow.QUIZ_DATA={json.dumps(quiz_data,ensure_ascii=False)};\n{JS_LESSON}"
    return page(les["title"], body, js_extra=js, back="lekce/x")

# ── Article page ──────────────────────────────────────────────────────────────

def build_article(art, all_articles):
    parts = [f"""
<div class="lesson-header">
  <h1>{esc(art['title'])}</h1>
  <div class="lesson-meta">
    <span class="tag tag-level">{esc(art['level'])}</span>
    <span style="color:var(--muted);font-size:.8rem">{esc(art['topics'])}</span>
  </div>
</div>"""]

    if art.get("article_text"):
        parts.append(f'<div class="section"><h2>📄 Article</h2><div class="article-text">{esc(art["article_text"])}</div></div>')

    if art.get("vocabulary"):
        rows = "".join(
            f'<tr><td class="vocab-en">{esc(v["en"])}</td>'
            f'<td class="vocab-cz hidden-cz">{esc(v["cz"])}</td>'
            f'<td><button class="vocab-toggle" onclick="toggleCz(this)">Show</button></td></tr>\n'
            for v in art["vocabulary"]
        )
        parts.append(f'<div class="section"><h2>📚 Vocabulary <button id="toggle-all-btn" class="btn" style="font-size:.75rem;padding:.2rem .6rem" onclick="toggleAllCz()">Show all</button></h2><table class="vocab-table">{rows}</table></div>')

    if art.get("examples"):
        qs = "".join(
            f'<div class="comprehension-q"><p>Q: {esc(e["en"])}</p>'
            f'<input type="text" placeholder="Your answer...">'
            f'<button class="show-answer" onclick="showModelAnswer(this)">Show</button>'
            f'<div class="model-answer">✓ {esc(e["cz"])}</div></div>'
            for e in art["examples"][:5]
        )
        parts.append(f'<div class="section"><h2>🎯 Comprehension</h2>{qs}</div>')

    if art.get("tasks"):
        items = "".join(f"<li>{esc(t)}</li>" for t in art["tasks"])
        parts.append(f'<div class="section"><h2>✏️ Tasks</h2><ul class="tasks-list">{items}</ul></div>')

    idx = next((i for i, a in enumerate(all_articles) if a["slug"] == art["slug"]), 0)
    prev_a = all_articles[idx-1] if idx > 0 else None
    next_a = all_articles[idx+1] if idx < len(all_articles)-1 else None
    pl = f'<a href="{prev_a["slug"]}.html">← {esc(prev_a["title"])}</a>' if prev_a else "<span></span>"
    nl = f'<a href="{next_a["slug"]}.html">{esc(next_a["title"])} →</a>' if next_a else "<span></span>"
    parts.append(f'<div class="lesson-nav">{pl}{nl}</div>')

    return page(art["title"], "\n".join(parts), js_extra=JS_LESSON, back="clanky/x")

# ── Flashcards ────────────────────────────────────────────────────────────────

def build_flashcards(lessons):
    cards = []
    nums  = []
    for les in lessons:
        for v in les.get("vocabulary", []):
            cards.append({"en": v["en"], "cz": v["cz"], "lesson": les["num"]})
        if les.get("vocabulary"):
            nums.append(les["num"])

    filter_btns = '<button class="btn btn-accent fc-filter-btn" data-lesson="all">All</button>\n'
    for n in nums:
        filter_btns += f'<button class="btn fc-filter-btn" data-lesson="{n}">L{n}</button>\n'

    body = f"""
<h1 style="font-size:1.3rem;font-weight:700;margin-bottom:1rem">🎴 Flashcards</h1>
<div style="display:flex;align-items:center;gap:.5rem;flex-wrap:wrap;margin-bottom:1rem">
  <button class="btn" id="mode-btn">CZ → EN</button>
  <span style="color:var(--muted);font-size:.82rem">Filter:</span>
  <div style="display:flex;gap:.3rem;flex-wrap:wrap">{filter_btns}</div>
</div>
<div id="fc-area" class="fc-area">
  <div class="fc-counter" id="fc-counter"></div>
  <div class="fc-card" id="fc-card">
    <div class="fc-inner">
      <div class="fc-front"><div class="fc-word" id="fc-front-word"></div><div class="fc-hint" id="fc-front-hint">Click to flip</div></div>
      <div class="fc-back"><div class="fc-translation" id="fc-back-word"></div></div>
    </div>
  </div>
  <div class="fc-controls">
    <button class="btn" onclick="answer(false)">✗ Didn't know</button>
    <button class="btn" onclick="flip()">🔄 Flip</button>
    <button class="btn btn-accent" onclick="answer(true)">✓ Knew it</button>
  </div>
</div>"""

    return page("Flashcards", body, js_extra=f"window.FC_DATA={json.dumps(cards,ensure_ascii=False)};\n{JS_FC}")

# ── Progress ──────────────────────────────────────────────────────────────────

def build_progress(lessons):
    rows = ""
    slugs = []
    for les in lessons:
        rows += f"""<div class="progress-row" id="row-{les['slug']}">
  <span class="progress-status">⬜</span>
  <span class="progress-title"><a href="lekce/{les['slug']}.html">L{les['num']} {esc(les['title'])}</a></span>
  <div class="mini-bar"><div class="mini-fill" style="width:0%"></div></div>
  <span class="progress-pct">—</span>
</div>\n"""
        slugs.append({"slug": les["slug"]})

    body = f"""
<h1 style="font-size:1.3rem;font-weight:700;margin-bottom:1rem">📊 Your Progress</h1>
<div class="streak-box">
  <div><div class="streak-num" id="streak-current">0</div><div style="font-size:.8rem;color:var(--muted)">day streak 🔥</div></div>
  <div><div style="font-size:1.3rem;font-weight:700" id="streak-longest">0</div><div style="font-size:.8rem;color:var(--muted)">longest</div></div>
  <div><div style="font-size:1.3rem;font-weight:700" id="streak-total">0</div><div style="font-size:.8rem;color:var(--muted)">total days</div></div>
</div>
<div class="alert">✅ = 80%+  &nbsp; 🔄 = 50–79%  &nbsp; ❌ = below 50%  &nbsp; ⬜ = not attempted</div>
<div class="section"><h2>📚 Lessons</h2>{rows}</div>
<p style="text-align:center;margin-top:1rem">
  <button class="btn" style="color:var(--red);border-color:var(--red)" onclick="if(confirm('Reset all progress?')){{Object.keys(localStorage).filter(k=>k.startsWith('score_')||k==='streak_data').forEach(k=>localStorage.removeItem(k));location.reload()}}">🗑 Reset all progress</button>
</p>"""

    return page("Progress", body, js_extra=f"window.ALL_SLUGS={json.dumps(slugs,ensure_ascii=False)};\n{JS_PROGRESS}")

# ── Vocabulary ────────────────────────────────────────────────────────────────

def build_vocab(lessons):
    sections = ""
    for les in lessons:
        v = les.get("vocabulary", [])
        if not v: continue
        rows = "".join(
            f'<div style="background:var(--surface);border:1px solid var(--border);border-radius:6px;'
            f'padding:.4rem .8rem;display:flex;justify-content:space-between;font-size:.85rem;margin-bottom:.3rem">'
            f'<span style="font-weight:500">{esc(w["en"])}</span>'
            f'<span style="color:var(--muted)">{esc(w["cz"])}</span></div>'
            for w in v
        )
        sections += f'<div style="margin-bottom:1.5rem"><h3 style="color:var(--accent);font-size:.9rem;margin-bottom:.5rem;border-bottom:1px solid var(--border);padding-bottom:.3rem">L{les["num"]} {esc(les["title"])}</h3>{rows}</div>\n'

    body = f"""
<h1 style="font-size:1.3rem;font-weight:700;margin-bottom:.5rem">📖 Vocabulary</h1>
<input id="search-input" type="search" placeholder="🔍 Filter..." style="margin-bottom:1rem;width:100%;max-width:300px;background:var(--surface);border:1px solid var(--border);color:var(--text);padding:.4rem .8rem;border-radius:6px;font-size:.85rem;outline:none">
<div id="vocab-list">{sections}</div>"""

    js = """const vs=document.getElementById('search-input'); if(vs){ vs.addEventListener('input',()=>{ const q=vs.value.toLowerCase(); document.querySelectorAll('#vocab-list>div>div').forEach(r=>{ r.style.display=(!q||r.textContent.toLowerCase().includes(q))?'':'none'; }); }); }"""
    return page("Vocabulary", body, js_extra=js)

# ── Main ──────────────────────────────────────────────────────────────────────

def build_pwa_files(out, lessons, articles):
    """Generate PWA manifest and service worker."""
    manifest = {
        "name": "English Interactive Course",
        "short_name": "English Course",
        "description": "Interactive English course A1–C2 for Czech speakers",
        "start_url": "./index.html",
        "display": "standalone",
        "background_color": "#0f0f17",
        "theme_color": "#7c9ef5",
        "icons": [
            {"src": "icon-192.png", "sizes": "192x192", "type": "image/png"},
            {"src": "icon-512.png", "sizes": "512x512", "type": "image/png"}
        ]
    }
    (out / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    # Generate a simple SVG icon (blue gradient flag emoji style)
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 192 192">
<rect width="192" height="192" rx="32" fill="#1a1a2e"/>
<text x="96" y="130" font-size="120" text-anchor="middle">🇬🇧</text>
</svg>'''
    (out / "icon-192.png").write_bytes(b'')   # placeholder — GitHub Actions can't generate PNG
    (out / "icon-512.png").write_bytes(b'')

    # All pages to cache
    all_pages = ["./index.html", "./flashkarty.html", "./pokrok.html", "./slovnik.html"]
    for les in lessons:
        all_pages.append(f"./lekce/{les['slug']}.html")
    for art in articles:
        all_pages.append(f"./clanky/{art['slug']}.html")

    sw = f"""const CACHE = 'english-course-v2';
const URLS = {json.dumps(all_pages, indent=2)};

self.addEventListener('install', e => {{
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(URLS)));
}});
self.addEventListener('activate', e => {{
  e.waitUntil(caches.keys().then(keys =>
    Promise.all(keys.filter(k=>k!==CACHE).map(k=>caches.delete(k)))
  ));
}});
self.addEventListener('fetch', e => {{
  e.respondWith(caches.match(e.request).then(r => r || fetch(e.request)));
}});
"""
    (out / "sw.js").write_text(sw, encoding="utf-8")

def main():
    out      = pathlib.Path("web")
    lekce    = out / "lekce"
    clanky   = out / "clanky"
    lekce.mkdir(parents=True, exist_ok=True)
    clanky.mkdir(parents=True, exist_ok=True)

    lessons, articles = load_lessons()

    (out / "index.html").write_text(build_index(lessons, articles),   encoding="utf-8")
    (out / "flashkarty.html").write_text(build_flashcards(lessons),    encoding="utf-8")
    (out / "pokrok.html").write_text(build_progress(lessons),          encoding="utf-8")
    (out / "slovnik.html").write_text(build_vocab(lessons),            encoding="utf-8")

    for i, les in enumerate(lessons):
        (lekce / f"{les['slug']}.html").write_text(
            build_lesson(les, lessons[i-1] if i>0 else None, lessons[i+1] if i<len(lessons)-1 else None, len(lessons)),
            encoding="utf-8"
        )

    for art in articles:
        (clanky / f"{art['slug']}.html").write_text(build_article(art, articles), encoding="utf-8")

    build_pwa_files(out, lessons, articles)

    print(f"✓ Built {len(lessons)} lessons + {len(articles)} articles → web/")

if __name__ == "__main__":
    main()
