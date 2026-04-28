"""
Web generator — builds a fully interactive static web app.
No Python needed to USE the course — everything runs in the browser.

Run: python3 generator_web.py
Output: web/  (deploy to GitHub Pages)
"""
import pathlib, re, json, html, unicodedata, random

# ── Helpers ───────────────────────────────────────────────────────────────────

def slugify(text):
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = re.sub(r"[^\w\s-]", "", text.lower())
    return re.sub(r"[-\s]+", "_", text).strip("_")

def esc(s):
    return html.escape(str(s))

# ── Lesson parser ─────────────────────────────────────────────────────────────

def parse_lesson(path):
    src = path.read_text(encoding="utf-8")
    num = path.stem[:2]
    is_article = path.parent.name == "clanky"

    # --- metadata from docstring ---
    doc = re.match(r'"""(.*?)"""', src, re.DOTALL)
    docstring = doc.group(1).strip() if doc else ""
    lines = docstring.splitlines()
    title = re.sub(r"^(LESSON \d+|ARTICLE \d+):\s*", "", lines[0].strip()) if lines else path.stem
    level, topics, desc_lines = "", "", []
    for line in lines[2:]:
        s = line.strip()
        if s.startswith("⭐") or "Level:" in s: level = s
        elif s.lower().startswith("topics:"): topics = s[7:].strip()
        elif s: desc_lines.append(s)
    description = " ".join(desc_lines)

    # --- vocabulary dicts (NAME = {"en": "cz", ...}) ---
    vocab = []
    for m in re.finditer(
        r'^[A-Z_]+\s*=\s*\{([^}]+)\}',
        src, re.MULTILINE | re.DOTALL
    ):
        block = m.group(1)
        for pair in re.finditer(
            r'["\']([A-Za-z /\-\'\.,!?&()]+?)["\']\s*:\s*["\']([^"\']{1,80})["\']',
            block
        ):
            en, cz = pair.group(1).strip(), pair.group(2).strip()
            if len(en) > 1 and len(cz) > 1 and not any(c in en for c in "{}[]\\="):
                vocab.append({"en": en, "cz": cz})

    # deduplicate keeping order
    seen = set()
    vocab_clean = []
    for v in vocab:
        k = v["en"].lower()
        if k not in seen:
            seen.add(k)
            vocab_clean.append(v)

    # --- dialogue tuples ---
    dialogue = []
    for m in re.finditer(
        r'\(\s*["\']([AB]|Waiter|Customer|Doctor|Patient|Assistant|Candidate|Interviewer|Teacher|Student)["\'],\s*["\']([^"\']{4,180})["\']',
        src
    ):
        dialogue.append({"speaker": m.group(1), "text": m.group(2)})

    # --- grammar/note lines from print statements ---
    notes = []
    for m in re.finditer(r'print\(["\']([^"\']{10,200})["\']', src):
        s = m.group(1)
        if any(c in s for c in ["✓", "✗", "⚠️", "→", "≠", "NOT", "NE:"]):
            notes.append(s.replace("  ", " ").strip())

    # --- example pairs (EN, CZ) ---
    examples = []
    for m in re.finditer(
        r'\(\s*["\']([A-Z][^"\']{8,120}[.!?])["\'],\s*\n?\s*["\']([^"\']{4,120})["\']',
        src
    ):
        en, cz = m.group(1).strip(), m.group(2).strip()
        if not any(c in en for c in ["→", "✓", "✗", "=", "("]):
            examples.append({"en": en, "cz": cz})

    # --- quiz items (sentence_with_blank, answer) ---
    quiz_items = []
    for m in re.finditer(
        r'\(\s*["\']([^"\']+___[^"\']*)["\'],\s*\n?\s*["\']([^"\']{1,60})["\']',
        src
    ):
        quiz_items.append({"sentence": m.group(1).strip(), "answer": m.group(2).strip()})

    # --- article text ---
    article_text = ""
    if is_article:
        am = re.search(r'ARTICLE\s*=\s*"""(.*?)"""', src, re.DOTALL)
        if am:
            article_text = am.group(1).strip()

    # --- tasks ---
    tasks = []
    for m in re.finditer(r'#\s*(\d+\.\s.+)', src):
        tasks.append(m.group(1).strip())

    slug_base = path.stem[3:] if len(path.stem) > 3 else path.stem
    return {
        "num":         num,
        "stem":        path.stem,
        "slug":        slugify(slug_base),
        "title":       title,
        "level":       level,
        "topics":      topics,
        "description": description,
        "vocab":       vocab_clean[:50],
        "dialogue":    dialogue[:12],
        "notes":       notes[:20],
        "examples":    examples[:10],
        "quiz_items":  quiz_items[:10],
        "article_text":article_text,
        "tasks":       tasks[:6],
        "is_article":  is_article,
    }

def make_mc_quiz(vocab, n=10):
    """Generate multiple-choice questions from vocabulary."""
    if len(vocab) < 4:
        return []
    items = random.sample(vocab, min(n, len(vocab)))
    all_en = [v["en"] for v in vocab]
    questions = []
    for item in items:
        wrong = [e for e in all_en if e != item["en"]]
        distractors = random.sample(wrong, min(3, len(wrong)))
        options = distractors + [item["en"]]
        random.shuffle(options)
        questions.append({
            "type":    "mc",
            "prompt":  item["cz"],
            "options": options,
            "answer":  item["en"],
        })
    return questions

# ── CSS ───────────────────────────────────────────────────────────────────────

CSS = """
:root{
  --bg:#1e1e2e;--surface:#2a2a3e;--surface2:#313244;--border:#3a3a5e;
  --text:#cdd6f4;--muted:#6c7086;--accent:#89b4fa;--green:#a6e3a1;
  --yellow:#f9e2af;--red:#f38ba8;--purple:#cba6f7;
}
body.light{
  --bg:#eff1f5;--surface:#e6e9ef;--surface2:#dce0e8;--border:#bcc0cc;
  --text:#4c4f69;--muted:#9ca0b0;--accent:#1e66f5;--green:#40a02b;
  --yellow:#df8e1d;--red:#d20f39;--purple:#8839ef;
}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--text);font-family:system-ui,-apple-system,sans-serif;
  line-height:1.65;min-height:100vh}
a{color:var(--accent);text-decoration:none}
a:hover{text-decoration:underline}
button{cursor:pointer;font-family:inherit}

/* ─ Header ─ */
header{background:var(--surface);border-bottom:1px solid var(--border);
  padding:.7rem 1.5rem;display:flex;align-items:center;justify-content:space-between;
  gap:.8rem;position:sticky;top:0;z-index:100;flex-wrap:wrap}
.logo{font-weight:700;font-size:1rem;color:var(--text)}
.logo a{color:inherit}
.hdr-nav{display:flex;gap:.4rem;align-items:center;flex-wrap:wrap}
.btn{background:var(--surface2);border:1px solid var(--border);color:var(--text);
  padding:.3rem .75rem;border-radius:6px;font-size:.82rem;transition:border-color .15s}
.btn:hover{border-color:var(--accent)}
.btn-accent{background:var(--accent);color:#1e1e2e;border-color:var(--accent);font-weight:600}
.btn-accent:hover{opacity:.9}
#search-input{background:var(--surface2);border:1px solid var(--border);color:var(--text);
  padding:.3rem .8rem;border-radius:6px;font-size:.85rem;width:200px;outline:none}
#search-input:focus{border-color:var(--accent)}

/* ─ Layout ─ */
main{max-width:960px;margin:0 auto;padding:1.5rem 1.5rem 4rem}

/* ─ Index grid ─ */
.section-title{font-size:1.1rem;font-weight:700;color:var(--accent);
  border-bottom:1px solid var(--border);padding-bottom:.3rem;
  margin:1.8rem 0 .6rem;display:flex;justify-content:space-between;align-items:baseline}
.section-count{font-size:.8rem;color:var(--muted);font-weight:400}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:.8rem}
.card{background:var(--surface);border:1px solid var(--border);border-radius:10px;
  padding:1rem 1.1rem;transition:border-color .15s,transform .15s;display:block;
  text-decoration:none!important;color:var(--text)!important}
.card:hover{border-color:var(--accent);transform:translateY(-2px)}
.card-num{font-size:.75rem;color:var(--muted);margin-bottom:.2rem}
.card-title{font-size:.92rem;font-weight:600;margin-bottom:.25rem}
.card-level{font-size:.75rem;color:var(--yellow);margin-bottom:.25rem}
.card-topics{font-size:.72rem;color:var(--muted);margin-bottom:.5rem}
.progress-bar{height:3px;background:var(--border);border-radius:2px}
.progress-fill{height:100%;background:var(--accent);border-radius:2px;
  transition:width .4s ease;width:0%}

/* ─ Lesson page ─ */
.lesson-header{margin-bottom:1.2rem}
.lesson-header h1{font-size:1.4rem;font-weight:700;margin-bottom:.3rem}
.lesson-meta{display:flex;gap:.6rem;flex-wrap:wrap;font-size:.82rem;color:var(--muted)}
.course-progress{background:var(--surface);border:1px solid var(--border);
  border-radius:8px;padding:.6rem 1rem;margin-bottom:1.2rem;
  display:flex;align-items:center;gap:.8rem;font-size:.82rem}
.cp-bar{flex:1;height:5px;background:var(--border);border-radius:3px}
.cp-fill{height:100%;background:var(--accent);border-radius:3px}
.desc-box{background:var(--surface);border-left:3px solid var(--accent);
  padding:.7rem 1rem;border-radius:0 6px 6px 0;margin-bottom:1.2rem;font-size:.9rem}

/* ─ Sections ─ */
.section{background:var(--surface);border:1px solid var(--border);border-radius:10px;
  padding:1.1rem;margin-bottom:1rem}
.section h2{font-size:1rem;font-weight:700;color:var(--accent);margin-bottom:.8rem;
  display:flex;align-items:center;gap:.4rem}

/* ─ Vocabulary table ─ */
.vocab-table{width:100%;border-collapse:collapse}
.vocab-table tr:not(:last-child){border-bottom:1px solid var(--border)}
.vocab-table td{padding:.35rem .2rem;font-size:.88rem;vertical-align:middle}
.vocab-en{font-weight:500;width:45%}
.vocab-cz{color:var(--green);width:45%}
.vocab-toggle{background:none;border:none;color:var(--muted);font-size:.75rem;
  padding:.15rem .4rem;border-radius:4px;border:1px solid var(--border)}
.vocab-toggle:hover{color:var(--accent);border-color:var(--accent)}
.hidden-cz{visibility:hidden}

/* ─ Dialogue ─ */
.dialogue{display:flex;flex-direction:column;gap:.5rem}
.bubble{padding:.5rem .9rem;border-radius:12px;font-size:.88rem;max-width:85%}
.bubble-a{background:var(--accent);color:#1e1e2e;align-self:flex-start}
.bubble-b{background:var(--surface2);border:1px solid var(--border);align-self:flex-end}
.bubble-speaker{font-size:.72rem;font-weight:600;margin-bottom:.15rem;opacity:.7}

/* ─ Notes ─ */
.note{background:var(--surface2);border-radius:6px;padding:.4rem .8rem;
  font-size:.84rem;font-family:monospace;margin-bottom:.35rem;color:var(--yellow)}

/* ─ Examples ─ */
.example-row{margin-bottom:.6rem;font-size:.88rem}
.example-en{font-weight:500}
.example-cz{color:var(--muted);font-size:.83rem;margin-top:.1rem}

/* ─ Quiz ─ */
#quiz-section{margin-bottom:1rem}
.quiz-q{background:var(--surface);border:1px solid var(--border);border-radius:10px;
  padding:1rem;margin-bottom:.8rem}
.quiz-prompt{font-weight:600;font-size:.95rem;margin-bottom:.7rem}
.quiz-options{display:grid;grid-template-columns:1fr 1fr;gap:.4rem}
.quiz-opt{background:var(--surface2);border:1px solid var(--border);
  padding:.5rem .8rem;border-radius:8px;font-size:.85rem;text-align:left;
  color:var(--text);transition:border-color .15s}
.quiz-opt:hover:not(:disabled){border-color:var(--accent)}
.quiz-opt.correct{background:#1e3a2f;border-color:var(--green);color:var(--green)}
.quiz-opt.wrong{background:#3a1e2f;border-color:var(--red);color:var(--red)}
.quiz-opt:disabled{cursor:default}
.fill-blank input{background:var(--surface2);border:1px solid var(--border);
  color:var(--text);padding:.4rem .7rem;border-radius:6px;font-size:.88rem;
  width:200px;outline:none;margin-right:.5rem}
.fill-blank input:focus{border-color:var(--accent)}
.fill-blank .check-btn{background:var(--accent);border:none;color:#1e1e2e;
  padding:.4rem .9rem;border-radius:6px;font-size:.85rem;font-weight:600}
.quiz-result{margin-top:.4rem;font-size:.83rem}
.quiz-score{background:var(--surface);border:1px solid var(--border);border-radius:10px;
  padding:1rem;text-align:center;margin-top:.5rem}
.score-num{font-size:2rem;font-weight:700;color:var(--accent)}
.score-pct{font-size:1rem;color:var(--muted)}
.score-msg{font-size:.9rem;margin-top:.4rem}

/* ─ Tasks ─ */
.tasks-list{padding-left:1.2rem}
.tasks-list li{margin-bottom:.35rem;font-size:.88rem}

/* ─ Article ─ */
.article-text{font-size:.92rem;line-height:1.75;white-space:pre-line;
  border-left:3px solid var(--accent);padding-left:1rem;margin-bottom:1rem;
  color:var(--text)}
.comprehension-q{margin-bottom:.8rem}
.comprehension-q p{font-size:.9rem;font-weight:600;margin-bottom:.3rem}
.comprehension-q input{background:var(--surface2);border:1px solid var(--border);
  color:var(--text);padding:.35rem .7rem;border-radius:6px;font-size:.85rem;
  width:100%;max-width:400px;outline:none}
.comprehension-q input:focus{border-color:var(--accent)}
.model-answer{margin-top:.3rem;font-size:.82rem;color:var(--green);display:none}
.show-answer{background:none;border:1px solid var(--border);color:var(--muted);
  font-size:.75rem;padding:.15rem .5rem;border-radius:4px;margin-left:.5rem}
.show-answer:hover{color:var(--accent);border-color:var(--accent)}

/* ─ Flashcards ─ */
.fc-area{display:flex;flex-direction:column;align-items:center;padding:2rem 0}
.fc-card{width:min(420px,90vw);height:200px;perspective:1000px;cursor:pointer;margin-bottom:1.5rem}
.fc-inner{width:100%;height:100%;position:relative;transform-style:preserve-3d;
  transition:transform .4s}
.fc-card.flipped .fc-inner{transform:rotateY(180deg)}
.fc-front,.fc-back{position:absolute;width:100%;height:100%;backface-visibility:hidden;
  border-radius:14px;display:flex;flex-direction:column;align-items:center;
  justify-content:center;padding:1.5rem;text-align:center;border:2px solid var(--border)}
.fc-front{background:var(--surface)}
.fc-back{background:var(--surface2);transform:rotateY(180deg);color:var(--green)}
.fc-word{font-size:1.4rem;font-weight:700}
.fc-hint{font-size:.75rem;color:var(--muted);margin-top:.5rem}
.fc-translation{font-size:1.3rem;font-weight:600}
.fc-controls{display:flex;gap:.6rem;flex-wrap:wrap;justify-content:center}
.fc-counter{color:var(--muted);font-size:.85rem;margin-bottom:.5rem}

/* ─ Progress page ─ */
.progress-row{display:flex;align-items:center;gap:.7rem;padding:.5rem;
  border-bottom:1px solid var(--border);font-size:.85rem}
.progress-status{font-size:1rem;width:1.5rem;text-align:center}
.progress-title{flex:1;font-weight:500}
.progress-pct{font-size:.8rem;color:var(--muted);min-width:40px;text-align:right}
.mini-bar{width:80px;height:5px;background:var(--border);border-radius:3px}
.mini-fill{height:100%;border-radius:3px;background:var(--accent)}
.streak-box{background:var(--surface);border:1px solid var(--border);border-radius:10px;
  padding:1.2rem;margin-bottom:1.5rem;display:flex;gap:1.5rem;align-items:center}
.streak-num{font-size:2.5rem;font-weight:700;color:var(--yellow)}

/* ─ Nav ─ */
.lesson-nav{display:flex;justify-content:space-between;margin-top:1.5rem;
  padding-top:1rem;border-top:1px solid var(--border)}
.lesson-nav a{background:var(--surface);border:1px solid var(--border);
  padding:.45rem .9rem;border-radius:7px;font-size:.85rem;color:var(--accent);
  max-width:45%;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.lesson-nav a:hover{border-color:var(--accent);text-decoration:none}

/* ─ Footer ─ */
footer{text-align:center;padding:1.5rem;color:var(--muted);font-size:.78rem}

/* ─ Utilities ─ */
.hidden{display:none!important}
.tag{background:var(--surface2);border-radius:20px;padding:.15rem .55rem;
  font-size:.75rem;color:var(--muted)}
.alert{background:var(--surface);border:1px solid var(--yellow);border-radius:8px;
  padding:.7rem 1rem;font-size:.88rem;margin-bottom:1rem;color:var(--yellow)}
"""

# ── JavaScript ────────────────────────────────────────────────────────────────

JS_COMMON = """
// ─ Theme ─
const themeBtn = document.getElementById('theme-btn');
const storedTheme = localStorage.getItem('theme');
if (storedTheme === 'light') document.body.classList.add('light');
function syncThemeBtn(){
  if(themeBtn) themeBtn.textContent = document.body.classList.contains('light')
    ? '🌙 Dark' : '☀️ Light';
}
syncThemeBtn();
if(themeBtn) themeBtn.addEventListener('click',()=>{
  document.body.classList.toggle('light');
  localStorage.setItem('theme', document.body.classList.contains('light') ? 'light' : 'dark');
  syncThemeBtn();
});

// ─ Progress helpers ─
function getScore(slug){ return JSON.parse(localStorage.getItem('score_'+slug)||'null'); }
function setScore(slug, score, total){
  const prev = getScore(slug);
  if(!prev || score >= prev.score){
    localStorage.setItem('score_'+slug, JSON.stringify({score,total,date:new Date().toISOString().slice(0,10)}));
  }
  // update index card bar if visible
  const fill = document.querySelector('.progress-fill[data-slug="'+slug+'"]');
  if(fill) fill.style.width = Math.round(score/total*100)+'%';
}

// ─ Streak ─
function checkStreak(){
  const today = new Date().toISOString().slice(0,10);
  const data = JSON.parse(localStorage.getItem('streak_data')||'{"days":[],"longest":0}');
  if(!data.days.includes(today)){
    data.days.push(today);
    data.days.sort();
    // compute streak
    let streak=1;
    for(let i=data.days.length-2;i>=0;i--){
      const d1=new Date(data.days[i]), d2=new Date(data.days[i+1]);
      if((d2-d1)/86400000===1) streak++; else break;
    }
    data.longest = Math.max(data.longest||0, streak);
    localStorage.setItem('streak_data', JSON.stringify(data));
  }
}
checkStreak();
"""

JS_INDEX = """
// Search
const searchEl = document.getElementById('search-input');
if(searchEl){
  searchEl.addEventListener('input',()=>{
    const q = searchEl.value.toLowerCase();
    document.querySelectorAll('.card').forEach(card=>{
      card.style.display = (!q || card.textContent.toLowerCase().includes(q)) ? '' : 'none';
    });
  });
}
// Load progress bars
document.querySelectorAll('.progress-fill[data-slug]').forEach(fill=>{
  const s = getScore(fill.dataset.slug);
  if(s) fill.style.width = Math.round(s.score/s.total*100)+'%';
});
"""

JS_LESSON = """
// ─ Vocabulary toggle ─
function toggleCz(btn){
  const td = btn.closest('tr').querySelector('.vocab-cz');
  if(td.classList.contains('hidden-cz')){
    td.classList.remove('hidden-cz'); btn.textContent='Hide';
  } else {
    td.classList.add('hidden-cz'); btn.textContent='Show';
  }
}
function toggleAllCz(){
  const all = document.querySelectorAll('.vocab-cz');
  const allHidden = [...all].every(t=>t.classList.contains('hidden-cz'));
  all.forEach(t=>{ allHidden ? t.classList.remove('hidden-cz') : t.classList.add('hidden-cz'); });
  document.getElementById('toggle-all-btn').textContent = allHidden ? 'Hide all' : 'Show all';
}

// ─ Quiz engine ─
const QUIZ = window.QUIZ_DATA || [];
let qIdx=0, correct=0, answered=0;

function renderQuiz(){
  const container = document.getElementById('quiz-area');
  if(!container || !QUIZ.length) return;
  if(qIdx >= QUIZ.length){ showScore(); return; }
  const q = QUIZ[qIdx];
  container.innerHTML = '';

  const div = document.createElement('div');
  div.className = 'quiz-q';

  if(q.type === 'mc'){
    div.innerHTML = '<div class="quiz-prompt">'+escHtml(q.prompt)+'<span class="tag" style="margin-left:.5rem;font-size:.7rem">'+escHtml(qIdx+1+'/'+QUIZ.length)+'</span></div><div class="quiz-options"></div>';
    const opts = div.querySelector('.quiz-options');
    q.options.forEach(opt=>{
      const btn = document.createElement('button');
      btn.className='quiz-opt'; btn.textContent=opt;
      btn.addEventListener('click',()=>checkMC(btn, opt, q.answer, div));
      opts.appendChild(btn);
    });
  } else if(q.type === 'fill'){
    const parts = q.sentence.split('___');
    div.innerHTML = '<div class="quiz-prompt">'+escHtml(qIdx+1+'/'+QUIZ.length)+'</div>'
      +'<div class="fill-blank">'
      +escHtml(parts[0])
      +'<input id="fi" autocomplete="off" placeholder="type answer...">'
      +escHtml(parts[1]||'')
      +'<button class="check-btn" onclick="checkFill()">Check</button>'
      +'</div><div class="quiz-result" id="fb"></div>';
  }
  container.appendChild(div);
}

function escHtml(s){ const d=document.createElement('div'); d.textContent=s; return d.innerHTML; }

function checkMC(btn, chosen, correct_ans, div){
  const all = div.querySelectorAll('.quiz-opt');
  all.forEach(b=>{ b.disabled=true; if(b.textContent===correct_ans) b.classList.add('correct'); });
  if(chosen === correct_ans){ btn.classList.add('correct'); correct++; }
  else { btn.classList.add('wrong'); }
  answered++; qIdx++;
  setTimeout(renderQuiz, 900);
}

function checkFill(){
  const inp = document.getElementById('fi');
  const fb = document.getElementById('fb');
  if(!inp) return;
  const q = QUIZ[qIdx];
  const ok = inp.value.trim().toLowerCase() === q.answer.toLowerCase();
  if(ok){ fb.innerHTML='<span style="color:var(--green)">✓ Correct!</span>'; correct++; }
  else { fb.innerHTML='<span style="color:var(--red)">✗ Answer: <strong>'+escHtml(q.answer)+'</strong></span>'; }
  inp.disabled=true;
  inp.closest('.fill-blank').querySelector('.check-btn').disabled=true;
  answered++; qIdx++;
  setTimeout(renderQuiz, 1000);
}

function showScore(){
  const container = document.getElementById('quiz-area');
  if(!container) return;
  const total = QUIZ.length;
  const pct = Math.round(correct/total*100);
  const msg = pct>=90?'🏆 Excellent!':pct>=70?'👍 Good job!':pct>=50?'📖 Keep practising!':'💪 Review and try again!';
  container.innerHTML = '<div class="quiz-score">'
    +'<div class="score-num">'+correct+'/'+total+'</div>'
    +'<div class="score-pct">'+pct+'%</div>'
    +'<div class="score-msg">'+msg+'</div>'
    +'<button class="btn btn-accent" style="margin-top:.8rem" onclick="restartQuiz()">Restart</button>'
    +'</div>';
  setScore(window.LESSON_SLUG, correct, total);
}

function restartQuiz(){ qIdx=0; correct=0; answered=0; renderQuiz(); }

// ─ Comprehension answers ─
function showModelAnswer(btn){
  const el = btn.nextElementSibling;
  if(el){ el.style.display='block'; btn.style.display='none'; }
}

// Init
renderQuiz();
"""

JS_FLASHCARDS = """
const ALL_CARDS = window.FC_DATA || [];
let fcCards = [...ALL_CARDS], fcIdx=0, fcCorrect=0, fcMode='cz-en';

function shuffleFC(){ fcCards = [...ALL_CARDS].sort(()=>Math.random()-.5); fcIdx=0; fcCorrect=0; renderFC(); }

function renderFC(){
  const card = document.getElementById('fc-card');
  const counter = document.getElementById('fc-counter');
  const remaining = document.getElementById('fc-remaining');
  if(!card || !fcCards.length) return;
  if(fcIdx >= fcCards.length){ showFCResult(); return; }
  const item = fcCards[fcIdx];
  card.classList.remove('flipped');
  document.getElementById('fc-front-word').textContent = fcMode==='cz-en' ? item.cz : item.en;
  document.getElementById('fc-back-word').textContent  = fcMode==='cz-en' ? item.en : item.cz;
  document.getElementById('fc-front-hint').textContent = fcMode==='cz-en' ? 'Click to see English' : 'Click to see Czech';
  if(counter) counter.textContent = (fcIdx+1)+' / '+fcCards.length;
}

function flipFC(){ document.getElementById('fc-card').classList.toggle('flipped'); }

function fcAnswer(knew){
  if(knew) fcCorrect++;
  fcIdx++;
  renderFC();
}

function showFCResult(){
  const area = document.getElementById('fc-area');
  if(!area) return;
  const pct = Math.round(fcCorrect/fcCards.length*100);
  area.innerHTML = '<div class="quiz-score" style="max-width:360px;margin:2rem auto">'
    +'<div class="score-num">'+fcCorrect+'/'+fcCards.length+'</div>'
    +'<div class="score-pct">'+pct+'% recalled</div>'
    +'<button class="btn btn-accent" style="margin-top:1rem" onclick="shuffleFC()">New round</button>'
    +'</div>';
}

// Filter by lesson
document.querySelectorAll('.fc-filter-btn').forEach(btn=>{
  btn.addEventListener('click',()=>{
    document.querySelectorAll('.fc-filter-btn').forEach(b=>b.classList.remove('btn-accent'));
    btn.classList.add('btn-accent');
    const lesson = btn.dataset.lesson;
    fcCards = lesson==='all' ? [...ALL_CARDS] : ALL_CARDS.filter(c=>c.lesson===lesson);
    fcIdx=0; fcCorrect=0;
    const area = document.getElementById('fc-area');
    area.innerHTML = buildFCCard();
    document.getElementById('fc-card').addEventListener('click', flipFC);
    renderFC();
  });
});

function buildFCCard(){
  return '<div class="fc-counter" id="fc-counter"></div>'
    +'<div class="fc-card" id="fc-card">'
    +'<div class="fc-inner">'
    +'<div class="fc-front"><div class="fc-word" id="fc-front-word"></div>'
    +'<div class="fc-hint" id="fc-front-hint">Click to flip</div></div>'
    +'<div class="fc-back"><div class="fc-translation" id="fc-back-word"></div></div>'
    +'</div></div>'
    +'<div class="fc-controls">'
    +'<button class="btn" onclick="fcAnswer(false)">✗ Didn\\'t know</button>'
    +'<button class="btn" onclick="flipFC()">Flip</button>'
    +'<button class="btn btn-accent" onclick="fcAnswer(true)">✓ Knew it</button>'
    +'</div>';
}

document.getElementById('fc-card').addEventListener('click', flipFC);
document.getElementById('mode-btn').addEventListener('click',()=>{
  fcMode = fcMode==='cz-en' ? 'en-cz' : 'cz-en';
  document.getElementById('mode-btn').textContent = fcMode==='cz-en' ? 'CZ → EN' : 'EN → CZ';
  renderFC();
});

shuffleFC();
"""

JS_PROGRESS = """
const LESSON_SLUGS = window.ALL_SLUGS || [];
LESSON_SLUGS.forEach(({slug,num})=>{
  const s = getScore(slug);
  const row = document.getElementById('row-'+slug);
  if(!row) return;
  if(s){
    const pct = Math.round(s.score/s.total*100);
    row.querySelector('.progress-status').textContent = pct>=80?'✅':pct>=50?'🔄':'❌';
    row.querySelector('.progress-pct').textContent = pct+'%';
    row.querySelector('.mini-fill').style.width = pct+'%';
  }
});

// Streak
const sd = JSON.parse(localStorage.getItem('streak_data')||'{"days":[],"longest":0}');
const today = new Date().toISOString().slice(0,10);
let currentStreak=0;
if(sd.days.length){
  const last=sd.days[sd.days.length-1];
  if(last===today || last===(new Date(Date.now()-86400000).toISOString().slice(0,10))){
    currentStreak=1;
    for(let i=sd.days.length-2;i>=0;i--){
      const d1=new Date(sd.days[i]),d2=new Date(sd.days[i+1]);
      if((d2-d1)/86400000===1) currentStreak++; else break;
    }
  }
}
const streakEl = document.getElementById('streak-current');
const longestEl = document.getElementById('streak-longest');
const totalEl = document.getElementById('streak-total');
if(streakEl) streakEl.textContent = currentStreak;
if(longestEl) longestEl.textContent = sd.longest||0;
if(totalEl) totalEl.textContent = sd.days.length;
"""

# ── Page wrapper ──────────────────────────────────────────────────────────────

def page(title, body, js_extra="", back="index.html", extra_nav=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)} — English Course</title>
<style>{CSS}</style>
</head>
<body>
<header>
  <div class="logo"><a href="{back}">🇬🇧 English Course</a></div>
  <div class="hdr-nav">
    {"" if back=="index.html" else '<a href="'+back+'" class="btn">← Home</a>'}
    <a href="{'flashkarty.html' if back=='index.html' else '../flashkarty.html'}" class="btn">🎴 Flashcards</a>
    <a href="{'pokrok.html' if back=='index.html' else '../pokrok.html'}" class="btn">📊 Progress</a>
    <a href="{'slovnik.html' if back=='index.html' else '../slovnik.html'}" class="btn">📖 Vocab</a>
    {extra_nav}
    <button class="btn" id="theme-btn">☀️ Light</button>
  </div>
</header>
<main>{body}</main>
<footer>English Interactive Course · A1–C1 · All content runs in your browser</footer>
<script>{JS_COMMON}{js_extra}</script>
</body>
</html>"""

# ── Lesson HTML ───────────────────────────────────────────────────────────────

SECTIONS_DEF = [
    ("Basics",               "01", "07"),
    ("Grammar — Core",       "08", "15"),
    ("Grammar — Intermediate","16","20"),
    ("Everyday Topics",      "21", "30"),
    ("Advanced Vocabulary",  "31", "40"),
    ("Advanced Grammar",     "41", "50"),
    ("C1 — Style & Skills",  "51", "60"),
]

def build_lesson_html(les, prev_les, next_les, total):
    slug = les["slug"]
    num  = int(les["num"])
    pct  = int((num - 1) / total * 100)

    # vocabulary table
    vocab_rows = ""
    for v in les["vocab"]:
        vocab_rows += (
            f'<tr>'
            f'<td class="vocab-en">{esc(v["en"])}</td>'
            f'<td class="vocab-cz hidden-cz">{esc(v["cz"])}</td>'
            f'<td><button class="vocab-toggle" onclick="toggleCz(this)">Show</button></td>'
            f'</tr>\n'
        )
    vocab_section = ""
    if vocab_rows:
        vocab_section = f"""<div class="section">
<h2>📚 Vocabulary
  <button id="toggle-all-btn" class="btn" style="font-size:.75rem;padding:.2rem .6rem" onclick="toggleAllCz()">Show all</button>
</h2>
<table class="vocab-table">{vocab_rows}</table>
</div>"""

    # dialogue
    dialogue_html = ""
    if les["dialogue"]:
        bubbles = ""
        for d in les["dialogue"]:
            cls = "bubble-a" if d["speaker"] in ("A", "Waiter", "Doctor", "Assistant", "Interviewer", "Teacher") else "bubble-b"
            bubbles += f'<div class="bubble {cls}"><div class="bubble-speaker">{esc(d["speaker"])}</div>{esc(d["text"])}</div>\n'
        dialogue_html = f'<div class="section"><h2>💬 Dialogue</h2><div class="dialogue">{bubbles}</div></div>'

    # notes
    notes_html = ""
    if les["notes"]:
        items = "".join(f'<div class="note">{esc(n)}</div>' for n in les["notes"][:8])
        notes_html = f'<div class="section"><h2>📝 Notes</h2>{items}</div>'

    # examples
    examples_html = ""
    if les["examples"]:
        rows = "".join(
            f'<div class="example-row"><div class="example-en">{esc(e["en"])}</div>'
            f'<div class="example-cz">→ {esc(e["cz"])}</div></div>'
            for e in les["examples"][:6]
        )
        examples_html = f'<div class="section"><h2>💬 Examples</h2>{rows}</div>'

    # quiz
    mc_items = make_mc_quiz(les["vocab"])
    fill_items = [{"type": "fill", **q} for q in les["quiz_items"][:5]]
    quiz_data = [{"type": "mc", **q} for q in mc_items[:8]] + fill_items
    random.shuffle(quiz_data)
    quiz_json = json.dumps(quiz_data, ensure_ascii=False)

    quiz_html = ""
    if quiz_data:
        quiz_html = f'<div class="section" id="quiz-section"><h2>🎯 Quiz</h2><div id="quiz-area"></div></div>'

    # tasks
    tasks_html = ""
    if les["tasks"]:
        items = "".join(f"<li>{esc(t)}</li>" for t in les["tasks"])
        tasks_html = f'<div class="section"><h2>✏️ Your Tasks</h2><ul class="tasks-list">{items}</ul></div>'

    # navigation
    prev_link = f'<a href="{prev_les["slug"]}.html">← {esc(prev_les["title"])}</a>' if prev_les else "<span></span>"
    next_link = f'<a href="{next_les["slug"]}.html">{esc(next_les["title"])} →</a>' if next_les else "<span></span>"

    body = f"""
<div class="lesson-header">
  <h1>{esc(les["title"])}</h1>
  <div class="lesson-meta">
    <span class="tag">Lesson {les["num"]}</span>
    <span class="tag">{esc(les["level"])}</span>
    <span>{esc(les["topics"])}</span>
  </div>
</div>
<div class="course-progress">
  <span>Progress</span>
  <div class="cp-bar"><div class="cp-fill" style="width:{pct}%"></div></div>
  <span>{num}/{total}</span>
</div>
{('<div class="desc-box">'+esc(les["description"])+'</div>') if les["description"] else ""}
{vocab_section}
{dialogue_html}
{notes_html}
{examples_html}
{quiz_html}
{tasks_html}
<div class="lesson-nav">{prev_link}{next_link}</div>
"""
    js = f"window.LESSON_SLUG='{slug}';\nwindow.QUIZ_DATA={quiz_json};\n{JS_LESSON}"
    return page(les["title"], body, js_extra=js, back="../index.html")

# ── Article HTML ──────────────────────────────────────────────────────────────

def build_article_html(art, prev_art, next_art, all_articles):
    body_parts = []
    body_parts.append(f"""
<div class="lesson-header">
  <h1>{esc(art["title"])}</h1>
  <div class="lesson-meta">
    <span class="tag">{esc(art["level"])}</span>
    <span>{esc(art["topics"])}</span>
  </div>
</div>""")

    if art["article_text"]:
        body_parts.append(f'<div class="section"><h2>📄 Article</h2><div class="article-text">{esc(art["article_text"])}</div></div>')

    if art["vocab"]:
        rows = "".join(
            f'<tr><td class="vocab-en">{esc(v["en"])}</td>'
            f'<td class="vocab-cz hidden-cz">{esc(v["cz"])}</td>'
            f'<td><button class="vocab-toggle" onclick="toggleCz(this)">Show</button></td></tr>\n'
            for v in art["vocab"]
        )
        body_parts.append(f'<div class="section"><h2>📚 Vocabulary <button id="toggle-all-btn" class="btn" style="font-size:.75rem;padding:.2rem .6rem" onclick="toggleAllCz()">Show all</button></h2><table class="vocab-table">{rows}</table></div>')

    if art["examples"]:
        rows = "".join(
            f'<div class="comprehension-q"><p>Q: {esc(e["en"])}</p>'
            f'<input type="text" placeholder="Your answer...">'
            f'<button class="show-answer" onclick="showModelAnswer(this)">Show answer</button>'
            f'<div class="model-answer">✓ {esc(e["cz"])}</div></div>'
            for e in art["examples"][:5]
        )
        body_parts.append(f'<div class="section"><h2>🎯 Comprehension</h2>{rows}</div>')

    if art["tasks"]:
        items = "".join(f"<li>{esc(t)}</li>" for t in art["tasks"])
        body_parts.append(f'<div class="section"><h2>✏️ Tasks</h2><ul class="tasks-list">{items}</ul></div>')

    idx = all_articles.index(art)
    prev_a = all_articles[idx-1] if idx > 0 else None
    next_a = all_articles[idx+1] if idx < len(all_articles)-1 else None
    prev_link = f'<a href="{prev_a["slug"]}.html">← {esc(prev_a["title"])}</a>' if prev_a else "<span></span>"
    next_link = f'<a href="{next_a["slug"]}.html">{esc(next_a["title"])} →</a>' if next_a else "<span></span>"
    body_parts.append(f'<div class="lesson-nav">{prev_link}{next_link}</div>')

    js = f"window.LESSON_SLUG='{art['slug']}';\n{JS_LESSON}"
    return page(art["title"], "\n".join(body_parts), js_extra=js, back="../index.html")

# ── Index ─────────────────────────────────────────────────────────────────────

def build_index(lessons, articles):
    by_sec = {}
    for les in lessons:
        for name, start, end in SECTIONS_DEF:
            if start <= les["num"] <= end:
                by_sec.setdefault(name, []).append(les)
                break

    sections_html = ""
    for name, _, _ in SECTIONS_DEF:
        cards = by_sec.get(name, [])
        if not cards: continue
        cards_html = ""
        for les in cards:
            cards_html += f"""<a class="card" href="lekce/{les['slug']}.html" data-slug="{les['slug']}">
  <div class="card-num">Lesson {les['num']}</div>
  <div class="card-title">{esc(les['title'])}</div>
  <div class="card-level">{esc(les['level'])}</div>
  <div class="card-topics">{esc(les['topics'])}</div>
  <div class="progress-bar"><div class="progress-fill" data-slug="{les['slug']}"></div></div>
</a>\n"""
        sections_html += f'<div class="section-title">{name}<span class="section-count">{len(cards)} lessons</span></div>\n<div class="grid">{cards_html}</div>\n'

    art_cards = "".join(f"""<a class="card" href="clanky/{a['slug']}.html">
  <div class="card-num">Article {a['num']}</div>
  <div class="card-title">{esc(a['title'])}</div>
  <div class="card-level">{esc(a['level'])}</div>
  <div class="card-topics">{esc(a['topics'])}</div>
</a>\n""" for a in articles)
    if art_cards:
        sections_html += f'<div class="section-title">Reading Articles<span class="section-count">{len(articles)} articles</span></div>\n<div class="grid">{art_cards}</div>\n'

    hero = f"""<div style="margin-bottom:1.5rem">
  <h1 style="font-size:1.6rem;font-weight:700;margin-bottom:.4rem">🇬🇧 English Interactive Course</h1>
  <p style="color:var(--muted)">{len(lessons)} lessons · {len(articles)} articles · A1 → C1 · Everything runs in your browser</p>
</div>"""

    search_bar = '<input id="search-input" type="search" placeholder="🔍 Search lessons...">'

    body = hero + search_bar + sections_html
    extra_nav = search_bar  # already in body, not needed in header

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>English Interactive Course — A1 to C1</title>
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
<footer>English Interactive Course · {len(lessons)} lessons · A1–C1 · No Python required</footer>
<script>{JS_COMMON}{JS_INDEX}</script>
</body>
</html>"""

# ── Flashcards page ───────────────────────────────────────────────────────────

def build_flashcards(lessons):
    all_cards = []
    lesson_nums = []
    for les in lessons:
        for v in les["vocab"]:
            all_cards.append({"en": v["en"], "cz": v["cz"], "lesson": les["num"]})
        if les["vocab"]:
            lesson_nums.append(les["num"])

    cards_json = json.dumps(all_cards, ensure_ascii=False)
    filter_btns = '<button class="btn btn-accent fc-filter-btn" data-lesson="all">All</button>\n'
    for num in lesson_nums:
        filter_btns += f'<button class="btn fc-filter-btn" data-lesson="{num}">L{num}</button>\n'

    body = f"""
<h1 style="font-size:1.3rem;font-weight:700;margin-bottom:1rem">🎴 Flashcards</h1>
<div style="display:flex;align-items:center;gap:.5rem;flex-wrap:wrap;margin-bottom:1rem">
  <button class="btn" id="mode-btn">CZ → EN</button>
  <span style="color:var(--muted);font-size:.82rem">Filter by lesson:</span>
  <div style="display:flex;gap:.3rem;flex-wrap:wrap">{filter_btns}</div>
</div>
<div id="fc-area" class="fc-area">
  <div class="fc-counter" id="fc-counter"></div>
  <div class="fc-card" id="fc-card">
    <div class="fc-inner">
      <div class="fc-front">
        <div class="fc-word" id="fc-front-word"></div>
        <div class="fc-hint" id="fc-front-hint">Click to flip</div>
      </div>
      <div class="fc-back">
        <div class="fc-translation" id="fc-back-word"></div>
      </div>
    </div>
  </div>
  <div class="fc-controls">
    <button class="btn" onclick="fcAnswer(false)">✗ Didn't know</button>
    <button class="btn" onclick="flipFC()">🔄 Flip</button>
    <button class="btn btn-accent" onclick="fcAnswer(true)">✓ Knew it</button>
  </div>
</div>"""

    js = f"window.FC_DATA={cards_json};\n{JS_FLASHCARDS}"
    return page("Flashcards", body, js_extra=js)

# ── Progress page ─────────────────────────────────────────────────────────────

def build_progress(lessons, articles):
    rows = ""
    slug_data = []
    for les in lessons:
        rows += f"""<div class="progress-row" id="row-{les['slug']}">
  <span class="progress-status">⬜</span>
  <span class="progress-title"><a href="lekce/{les['slug']}.html">L{les['num']} {esc(les['title'])}</a></span>
  <div class="mini-bar"><div class="mini-fill" style="width:0%"></div></div>
  <span class="progress-pct">—</span>
</div>\n"""
        slug_data.append({"slug": les["slug"], "num": les["num"]})

    slug_json = json.dumps(slug_data, ensure_ascii=False)
    body = f"""
<h1 style="font-size:1.3rem;font-weight:700;margin-bottom:1rem">📊 Your Progress</h1>
<div class="streak-box">
  <div>
    <div class="streak-num" id="streak-current">0</div>
    <div style="font-size:.8rem;color:var(--muted)">day streak 🔥</div>
  </div>
  <div>
    <div style="font-size:1.3rem;font-weight:700" id="streak-longest">0</div>
    <div style="font-size:.8rem;color:var(--muted)">longest</div>
  </div>
  <div>
    <div style="font-size:1.3rem;font-weight:700" id="streak-total">0</div>
    <div style="font-size:.8rem;color:var(--muted)">total days</div>
  </div>
</div>
<div class="alert">✅ = 80%+  &nbsp; 🔄 = 50–79%  &nbsp; ❌ = below 50%  &nbsp; ⬜ = not attempted</div>
<div class="section"><h2>📚 Lessons</h2>{rows}</div>
<p style="text-align:center;margin-top:1rem">
  <button class="btn" style="color:var(--red);border-color:var(--red)" onclick="if(confirm('Reset all progress?')){{Object.keys(localStorage).filter(k=>k.startsWith('score_')||k==='streak_data').forEach(k=>localStorage.removeItem(k));location.reload()}}">🗑 Reset all progress</button>
</p>"""

    js = f"window.ALL_SLUGS={slug_json};\n{JS_PROGRESS}"
    return page("Progress", body, js_extra=js)

# ── Vocabulary page ───────────────────────────────────────────────────────────

def build_vocab(lessons):
    sections = ""
    for les in lessons:
        if not les["vocab"]: continue
        rows = "".join(
            f'<div class="vocab-row" style="background:var(--surface);border:1px solid var(--border);border-radius:6px;padding:.4rem .8rem;display:flex;justify-content:space-between;font-size:.85rem;margin-bottom:.3rem">'
            f'<span style="font-weight:500">{esc(v["en"])}</span>'
            f'<span style="color:var(--muted)">{esc(v["cz"])}</span></div>\n'
            for v in les["vocab"]
        )
        sections += f'<div style="margin-bottom:1.5rem"><h3 style="color:var(--accent);font-size:.9rem;margin-bottom:.5rem;border-bottom:1px solid var(--border);padding-bottom:.3rem">L{les["num"]} {esc(les["title"])}</h3>{rows}</div>\n'

    body = f"""
<h1 style="font-size:1.3rem;font-weight:700;margin-bottom:.5rem">📖 Vocabulary</h1>
<input id="search-input" type="search" placeholder="🔍 Filter..." style="margin-bottom:1rem;width:100%;max-width:300px;background:var(--surface);border:1px solid var(--border);color:var(--text);padding:.4rem .8rem;border-radius:6px;font-size:.85rem;outline:none">
<div id="vocab-list">{sections}</div>"""

    js = """
const vocabSearch = document.getElementById('search-input');
const allRows = document.querySelectorAll('#vocab-list .vocab-row');
if(vocabSearch){
  vocabSearch.addEventListener('input',()=>{
    const q = vocabSearch.value.toLowerCase();
    allRows.forEach(r=>{
      r.style.display = (!q || r.textContent.toLowerCase().includes(q)) ? '' : 'none';
    });
  });
}"""
    return page("Vocabulary", body, js_extra=JS_COMMON + js)

# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    root     = pathlib.Path(".")
    out      = root / "web"
    lekce    = out / "lekce"
    clanky   = out / "clanky"
    lekce.mkdir(parents=True, exist_ok=True)
    clanky.mkdir(parents=True, exist_ok=True)

    lesson_files  = sorted(root.glob("[0-9][0-9]_*.py"))
    article_files = sorted((root / "clanky").glob("[0-9][0-9]_*.py"))

    lessons  = [parse_lesson(f) for f in lesson_files]
    articles = [parse_lesson(f) for f in article_files]

    # Index
    (out / "index.html").write_text(build_index(lessons, articles), encoding="utf-8")

    # Lessons
    for i, les in enumerate(lessons):
        prev_l = lessons[i-1] if i > 0 else None
        next_l = lessons[i+1] if i < len(lessons)-1 else None
        html_out = build_lesson_html(les, prev_l, next_l, len(lessons))
        (lekce / f"{les['slug']}.html").write_text(html_out, encoding="utf-8")

    # Articles
    for art in articles:
        html_out = build_article_html(art, None, None, articles)
        (clanky / f"{art['slug']}.html").write_text(html_out, encoding="utf-8")

    # Special pages
    (out / "flashkarty.html").write_text(build_flashcards(lessons),           encoding="utf-8")
    (out / "pokrok.html").write_text(build_progress(lessons, articles),        encoding="utf-8")
    (out / "slovnik.html").write_text(build_vocab(lessons),                    encoding="utf-8")

    total = len(lessons) + len(articles) + 3
    print(f"✓ Built {len(lessons)} lessons + {len(articles)} articles + 3 pages → web/  ({total} files)")

if __name__ == "__main__":
    main()
