"""
Web generator — builds static HTML site from lesson .py files.
Run: python3 generator_web.py
Output: web/ directory (deploy to GitHub Pages)
"""
import pathlib, re, html, unicodedata

# ── helpers ───────────────────────────────────────────────────────────────────

def slugify(text):
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = re.sub(r"[^\w\s-]", "", text.lower())
    return re.sub(r"[-\s]+", "_", text).strip("_")

def highlight(code):
    KEYWORDS = {"import","from","as","def","class","return","if","elif","else",
                "for","while","in","not","and","or","is","True","False","None",
                "with","try","except","raise","pass","break","continue","lambda",
                "yield","global","nonlocal","del","assert","finally","print"}
    BUILTINS = {"len","range","list","dict","str","int","float","input","print",
                "min","max","sum","sorted","enumerate","zip","map","filter",
                "random","sample","format","type","isinstance","open","next",
                "any","all","vars","items","keys","values","append","extend"}
    lines = []
    for line in code.split("\n"):
        esc = html.escape(line)
        esc = re.sub(r"(#[^\n]*)", r'<span class="cm">\1</span>', esc)
        if '<span class="cm">' not in esc:
            esc = re.sub(
                r'(&#x27;&#x27;&#x27;.*?&#x27;&#x27;&#x27;|&quot;&quot;&quot;.*?&quot;&quot;&quot;|&#x27;[^&#x27;]*&#x27;|&quot;[^&quot;]*&quot;)',
                r'<span class="st">\1</span>', esc, flags=re.DOTALL)
            def color_word(m):
                w = m.group(0)
                if w in KEYWORDS: return f'<span class="kw">{w}</span>'
                if w in BUILTINS: return f'<span class="fn">{w}</span>'
                return w
            esc = re.sub(r"\b[A-Za-z_]\w*\b", color_word, esc)
            esc = re.sub(r"\b(\d+)\b", r'<span class="nm">\1</span>', esc)
        lines.append(esc)
    return "\n".join(lines)

# ── lesson parser ─────────────────────────────────────────────────────────────

def parse_lesson(path):
    src = path.read_text(encoding="utf-8")
    doc_match = re.match(r'"""(.*?)"""', src, re.DOTALL)
    docstring = doc_match.group(1).strip() if doc_match else ""
    lines = docstring.splitlines()

    title = re.sub(r"^#\s*", "", lines[0].strip()) if lines else path.stem
    level, description, topics = "", [], ""
    for line in lines[2:]:
        if line.strip().startswith("⭐") or "Level:" in line:
            level = line.strip()
        elif line.strip().lower().startswith("topics:"):
            topics = line.strip()[7:].strip()
        elif line.strip():
            description.append(line.strip())

    tasks = []
    for m in re.finditer(r"#\s*(\d+\.\s.*?)(?=\n#\s*\d+\.|\Z)", src, re.DOTALL):
        task_text = re.sub(r"\n#\s*", " ", m.group(1)).strip()
        tasks.append(task_text)

    code = re.sub(r'^""".*?"""\s*', "", src, count=1, flags=re.DOTALL)
    code = re.sub(r"# YOUR TASK:.*", "", code, flags=re.DOTALL).strip()

    # extract vocabulary pairs for the vocab page
    vocab_pairs = []
    pattern = re.compile(r'["\']([A-Za-z][^"\']{1,50}?)["\']\s*:\s*["\']([^\'"]{1,80})["\']')
    for m in pattern.finditer(src):
        en, cz = m.group(1).strip(), m.group(2).strip()
        if any(c in en for c in "(){}[]\\="): continue
        if len(en) > 60 or len(cz) > 80: continue
        if en[0].isupper() and len(en) > 35: continue
        vocab_pairs.append((en, cz))

    return {
        "path": path, "stem": path.stem,
        "slug": slugify(path.stem[3:]) if len(path.stem) > 3 else slugify(path.stem),
        "number": path.stem[:2], "title": title, "level": level,
        "desc": " ".join(description), "topics": topics,
        "tasks": tasks, "code": code, "vocab": vocab_pairs,
    }

# ── CSS + JS ──────────────────────────────────────────────────────────────────

CSS = """
:root{--bg:#1e1e2e;--surface:#2a2a3e;--border:#3a3a5e;--text:#cdd6f4;
  --muted:#6c7086;--accent:#89b4fa;--green:#a6e3a1;--yellow:#f9e2af;
  --red:#f38ba8;--tag-bg:#313244;--progress-bg:#313244}
body.light{--bg:#eff1f5;--surface:#ccd0da;--border:#bcc0cc;--text:#4c4f69;
  --muted:#8c8fa1;--accent:#1e66f5;--green:#40a02b;--yellow:#df8e1d;
  --red:#d20f39;--tag-bg:#dce0e8;--progress-bg:#dce0e8}
*{box-sizing:border-box;margin:0;padding:0}
body{background:var(--bg);color:var(--text);font-family:system-ui,sans-serif;line-height:1.6}
a{color:var(--accent);text-decoration:none} a:hover{text-decoration:underline}
header{background:var(--surface);border-bottom:1px solid var(--border);
  padding:.8rem 2rem;display:flex;align-items:center;gap:1rem;
  justify-content:space-between;position:sticky;top:0;z-index:10;flex-wrap:wrap}
header h1{font-size:1rem;font-weight:700}
.header-actions{display:flex;gap:.5rem;align-items:center}
.theme-btn,.nav-btn{background:var(--tag-bg);border:1px solid var(--border);
  color:var(--text);padding:.3rem .7rem;border-radius:6px;cursor:pointer;font-size:.82rem}
.search-box{background:var(--tag-bg);border:1px solid var(--border);
  color:var(--text);padding:.3rem .8rem;border-radius:6px;font-size:.85rem;
  outline:none;width:200px}
.search-box:focus{border-color:var(--accent)}
main{max-width:980px;margin:1.5rem auto;padding:0 1.5rem}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(270px,1fr));gap:.9rem;margin-top:1rem}
.card{background:var(--surface);border:1px solid var(--border);border-radius:10px;
  padding:1.1rem;transition:border-color .2s;position:relative}
.card:hover{border-color:var(--accent)}
.card-num{font-size:.78rem;color:var(--muted);margin-bottom:.2rem}
.card-title{font-size:.95rem;font-weight:600;margin-bottom:.3rem}
.card-level{font-size:.78rem;color:var(--yellow);margin-bottom:.3rem}
.card-topics{font-size:.76rem;color:var(--muted)}
.progress-bar{height:4px;background:var(--progress-bg);border-radius:2px;
  margin-top:.6rem;overflow:hidden}
.progress-fill{height:100%;background:var(--accent);border-radius:2px;transition:width .3s}
.section-title{font-size:1.1rem;font-weight:700;margin:1.8rem 0 .4rem;
  color:var(--accent);border-bottom:1px solid var(--border);padding-bottom:.3rem;
  display:flex;justify-content:space-between;align-items:center}
.section-count{font-size:.8rem;color:var(--muted);font-weight:400}
/* lesson page */
.lesson-header{margin-bottom:1.2rem}
.lesson-header h1{font-size:1.4rem;font-weight:700;margin-bottom:.3rem}
.lesson-meta{display:flex;gap:.7rem;flex-wrap:wrap;font-size:.83rem;color:var(--muted)}
.lesson-progress{background:var(--surface);border:1px solid var(--border);
  border-radius:8px;padding:.7rem 1rem;margin-bottom:1.2rem;
  display:flex;align-items:center;gap:.8rem;font-size:.85rem}
.lp-bar{flex:1;height:6px;background:var(--progress-bg);border-radius:3px}
.lp-fill{height:100%;background:var(--accent);border-radius:3px}
.lesson-desc{background:var(--surface);border-left:3px solid var(--accent);
  padding:.7rem 1rem;border-radius:0 6px 6px 0;margin-bottom:1.2rem;font-size:.92rem}
pre{background:var(--surface);border:1px solid var(--border);border-radius:8px;
  padding:1.1rem;overflow-x:auto;font-size:.83rem;line-height:1.55;margin-bottom:1.2rem}
code{font-family:'JetBrains Mono','Fira Code',monospace}
.kw{color:#cba6f7} .st{color:var(--green)} .cm{color:var(--muted);font-style:italic}
.fn{color:var(--accent)} .nm{color:var(--yellow)}
.tasks{background:var(--surface);border:1px solid var(--green);
  border-radius:8px;padding:.9rem 1.1rem;margin-bottom:1.2rem}
.tasks h3{color:var(--green);font-size:.92rem;margin-bottom:.5rem}
.tasks ol{padding-left:1.2rem} .tasks li{margin-bottom:.25rem;font-size:.88rem}
.nav{display:flex;justify-content:space-between;margin-top:1.2rem;
  padding-top:.9rem;border-top:1px solid var(--border)}
.nav a{background:var(--surface);border:1px solid var(--border);
  padding:.45rem .9rem;border-radius:6px;font-size:.88rem;color:var(--accent)}
.nav a:hover{border-color:var(--accent);text-decoration:none}
/* vocab page */
.vocab-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:.5rem;margin-top:1rem}
.vocab-row{background:var(--surface);border:1px solid var(--border);
  border-radius:6px;padding:.5rem .9rem;display:flex;justify-content:space-between;
  align-items:center;font-size:.85rem}
.vocab-en{font-weight:500} .vocab-cz{color:var(--muted)}
.hidden{display:none!important}
footer{text-align:center;padding:1.5rem;color:var(--muted);font-size:.78rem;margin-top:2rem}
"""

JS_COMMON = """
// Theme toggle
const btn = document.querySelector('.theme-btn');
const saved = localStorage.getItem('theme');
if (saved === 'light') document.body.classList.add('light');
function updateBtn(){
  btn.textContent = document.body.classList.contains('light') ? '🌙 Dark' : '☀️ Light';
}
updateBtn();
btn.addEventListener('click', () => {
  document.body.classList.toggle('light');
  localStorage.setItem('theme', document.body.classList.contains('light') ? 'light' : 'dark');
  updateBtn();
});
"""

JS_INDEX = JS_COMMON + """
// Search
const searchBox = document.getElementById('search');
if (searchBox) {
  searchBox.addEventListener('input', () => {
    const q = searchBox.value.toLowerCase();
    document.querySelectorAll('.card').forEach(card => {
      const text = card.textContent.toLowerCase();
      card.parentElement.style.display = text.includes(q) ? '' : 'none';
    });
    // show/hide section titles
    document.querySelectorAll('.section-title').forEach(sec => {
      const grid = sec.nextElementSibling;
      if (!grid) return;
      const visible = [...grid.querySelectorAll('a')].some(a => a.style.display !== 'none');
      sec.style.display = visible || !q ? '' : 'none';
    });
  });
}
// Progress from localStorage
document.querySelectorAll('.card[data-lesson]').forEach(card => {
  const key = 'lesson_done_' + card.dataset.lesson;
  const done = parseInt(localStorage.getItem(key) || '0');
  const fill = card.querySelector('.progress-fill');
  if (fill && done) fill.style.width = done + '%';
});
"""

JS_LESSON = JS_COMMON + """
// Mark quiz answers in localStorage (simple progress)
const lessonNum = document.body.dataset.lesson;
let score = 0, total = 0;
document.querySelectorAll('.quiz-item').forEach(item => {
  total++;
  // placeholder — real scoring happens in Python
});
"""

# ── sections ──────────────────────────────────────────────────────────────────

SECTIONS = [
    ("Basics",               "01", "07"),
    ("Grammar",              "08", "12"),
    ("Grammar — Advanced",   "16", "20"),
    ("Vocabulary",           "13", "15"),
    ("Everyday Topics",      "21", "25"),
    ("Advanced",             "26", "30"),
]

def get_section(num):
    for name, start, end in SECTIONS:
        if start <= num <= end:
            return name
    return "Other"

# ── page builders ─────────────────────────────────────────────────────────────

def wrap(title, body, back="index.html", data_lesson=""):
    lesson_attr = f' data-lesson="{data_lesson}"' if data_lesson else ""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)} — English Course</title>
<style>{CSS}</style>
</head>
<body{lesson_attr}>
<header>
  <h1><a href="{back}" style="color:var(--text)">🇬🇧 English Interactive Course</a></h1>
  <div class="header-actions">
    <a href="{back}" class="nav-btn">← All lessons</a>
    <a href="vocab.html" class="nav-btn">📖 Vocab</a>
    <button class="theme-btn">☀️ Light</button>
  </div>
</header>
<main>{body}</main>
<footer>Interactive English Course · Run lessons with <code>python3 NN_file.py</code></footer>
<script>{'JS_LESSON' if data_lesson else JS_COMMON}</script>
</body>
</html>"""

def build_index(lessons):
    from_lekce = "../"
    body  = '<h2 style="font-size:1.3rem;margin-bottom:.3rem">Interactive English Course</h2>\n'
    body += '<p style="color:var(--muted);margin-bottom:.8rem">'
    body += f'{len(lessons)} lessons · A1–B1 · Czech explanations · '
    body += 'run each lesson with <code>python3 NN_file.py</code>'
    body += '</p>\n'
    body += '<input id="search" class="search-box" type="search" placeholder="🔍 Search lessons..." style="margin-bottom:1rem">\n'

    by_section = {}
    for les in lessons:
        sec = get_section(les["number"])
        by_section.setdefault(sec, []).append(les)

    for sec_name, _, _ in SECTIONS:
        cards = by_section.get(sec_name, [])
        if not cards:
            continue
        body += f'<div class="section-title">{sec_name} <span class="section-count">{len(cards)} lessons</span></div>\n'
        body += '<div class="grid">\n'
        for les in cards:
            url = f"lekce/{les['slug']}.html"
            body += f"""<a href="{url}" style="text-decoration:none">
  <div class="card" data-lesson="{les['number']}">
    <div class="card-num">Lesson {les['number']}</div>
    <div class="card-title">{html.escape(les['title'])}</div>
    <div class="card-level">{html.escape(les['level'])}</div>
    <div class="card-topics">{html.escape(les['topics'])}</div>
    <div class="progress-bar"><div class="progress-fill" style="width:0%"></div></div>
  </div>
</a>\n"""
        body += '</div>\n'

    # extra nav links in header
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>English Interactive Course</title>
<style>{CSS}</style>
</head>
<body>
<header>
  <h1>🇬🇧 English Interactive Course</h1>
  <div class="header-actions">
    <input id="search" class="search-box" type="search" placeholder="🔍 Search...">
    <a href="vocab.html" class="nav-btn">📖 Vocab</a>
    <button class="theme-btn">☀️ Light</button>
  </div>
</header>
<main>{body}</main>
<footer>Interactive English Course · {len(lessons)} lessons · A1–B1</footer>
<script>{JS_INDEX}</script>
</body>
</html>"""

def build_lesson_page(les, prev_les, next_les, total_lessons):
    idx = int(les["number"])
    pct = int((idx - 1) / total_lessons * 100)

    tasks_html = ""
    if les["tasks"]:
        items = "".join(f"<li>{html.escape(t)}</li>" for t in les["tasks"])
        tasks_html = f'<div class="tasks"><h3>✏️ Your Tasks</h3><ol>{items}</ol></div>'

    prev_link = f'<a href="{prev_les["slug"]}.html">← {html.escape(prev_les["title"])}</a>' if prev_les else "<span></span>"
    next_link = f'<a href="{next_les["slug"]}.html">{html.escape(next_les["title"])} →</a>' if next_les else "<span></span>"

    body = f"""
<div class="lesson-header">
  <h1>{html.escape(les['title'])}</h1>
  <div class="lesson-meta">
    <span>Lesson {les['number']}</span>
    <span>·</span>
    <span>{html.escape(les['level'])}</span>
    <span>·</span>
    <span>{html.escape(les['topics'])}</span>
  </div>
</div>
<div class="lesson-progress">
  <span>Course progress</span>
  <div class="lp-bar"><div class="lp-fill" style="width:{pct}%"></div></div>
  <span>{idx}/{total_lessons}</span>
</div>
<div class="lesson-desc">{html.escape(les['desc'])}</div>
<pre><code>{highlight(les['code'])}</code></pre>
{tasks_html}
<div class="nav">{prev_link}{next_link}</div>
"""
    return wrap(les["title"], body, back="../index.html", data_lesson=les["number"])

def build_vocab_page(lessons):
    all_vocab = []
    for les in lessons:
        for en, cz in les["vocab"]:
            all_vocab.append((les["number"], les["title"], en, cz))

    body = f'<h2 style="font-size:1.3rem;margin-bottom:.3rem">📖 Full Vocabulary</h2>\n'
    body += f'<p style="color:var(--muted);margin-bottom:.8rem">{len(all_vocab)} words & phrases across all lessons</p>\n'
    body += '<input id="search" class="search-box" type="search" placeholder="🔍 Filter vocabulary..." style="margin-bottom:1rem"><br>\n'

    current_num = None
    body += '<div class="vocab-grid" id="vocab-grid">\n'
    for num, title, en, cz in all_vocab:
        if num != current_num:
            current_num = num
            body += f'</div>\n<div class="section-title" style="margin-top:1.2rem">Lesson {num} — {html.escape(title)}</div>\n<div class="vocab-grid" id="vocab-grid">\n'
        body += f'<div class="vocab-row"><span class="vocab-en">{html.escape(en)}</span><span class="vocab-cz">{html.escape(cz)}</span></div>\n'
    body += '</div>\n'

    search_js = JS_COMMON + """
const vocabSearch = document.getElementById('search');
if (vocabSearch) {
  vocabSearch.addEventListener('input', () => {
    const q = vocabSearch.value.toLowerCase();
    document.querySelectorAll('.vocab-row').forEach(row => {
      row.style.display = row.textContent.toLowerCase().includes(q) ? '' : 'none';
    });
  });
}
"""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Vocabulary — English Course</title>
<style>{CSS}</style>
</head>
<body>
<header>
  <h1><a href="index.html" style="color:var(--text)">🇬🇧 English Interactive Course</a></h1>
  <div class="header-actions">
    <a href="index.html" class="nav-btn">← All lessons</a>
    <button class="theme-btn">☀️ Light</button>
  </div>
</header>
<main>{body}</main>
<footer>{len(all_vocab)} vocabulary items · Interactive English Course</footer>
<script>{search_js}</script>
</body>
</html>"""

# ── main ──────────────────────────────────────────────────────────────────────

def main():
    root = pathlib.Path(".")
    out  = root / "web"
    lekce_dir = out / "lekce"
    lekce_dir.mkdir(parents=True, exist_ok=True)

    files   = sorted(root.glob("[0-9][0-9]_*.py"))
    lessons = [parse_lesson(f) for f in files]

    (out / "index.html").write_text(build_index(lessons), encoding="utf-8")
    (out / "vocab.html").write_text(build_vocab_page(lessons), encoding="utf-8")

    for i, les in enumerate(lessons):
        prev_les = lessons[i - 1] if i > 0 else None
        next_les = lessons[i + 1] if i < len(lessons) - 1 else None
        page = build_lesson_page(les, prev_les, next_les, len(lessons))
        (lekce_dir / f"{les['slug']}.html").write_text(page, encoding="utf-8")

    print(f"✓ Built {len(lessons)} lessons + vocabulary page → web/")

if __name__ == "__main__":
    main()
