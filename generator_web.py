"""
Web generator — builds static HTML site from lesson .py files.
Run: python3 generator_web.py
Output: web/ directory (deploy to GitHub Pages)
"""
import pathlib
import re
import html
import unicodedata
import textwrap

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
                "random","sample","format","type","isinstance","open"}
    lines = []
    for line in code.split("\n"):
        esc = html.escape(line)
        # comments
        esc = re.sub(r"(#[^\n]*)", r'<span class="cm">\1</span>', esc)
        if '<span class="cm">' not in esc:
            # strings
            esc = re.sub(r'(&#x27;&#x27;&#x27;.*?&#x27;&#x27;&#x27;|&quot;&quot;&quot;.*?&quot;&quot;&quot;|&#x27;[^&#x27;]*&#x27;|&quot;[^&quot;]*&quot;)',
                         r'<span class="st">\1</span>', esc, flags=re.DOTALL)
            # keywords & builtins
            def color_word(m):
                w = m.group(0)
                if w in KEYWORDS: return f'<span class="kw">{w}</span>'
                if w in BUILTINS: return f'<span class="fn">{w}</span>'
                return w
            esc = re.sub(r"\b[A-Za-z_]\w*\b", color_word, esc)
            # numbers
            esc = re.sub(r"\b(\d+)\b", r'<span class="nm">\1</span>', esc)
        lines.append(esc)
    return "\n".join(lines)

# ── lesson parser ─────────────────────────────────────────────────────────────

def parse_lesson(path):
    src = path.read_text(encoding="utf-8")
    # docstring
    doc_match = re.match(r'"""(.*?)"""', src, re.DOTALL)
    docstring = doc_match.group(1).strip() if doc_match else ""
    lines = docstring.splitlines()

    title = lines[0].strip() if lines else path.stem
    # strip leading '# ' from title line if present
    title = re.sub(r"^#\s*", "", title)

    level = ""
    description = []
    topics = ""
    for line in lines[2:]:
        if line.strip().startswith("⭐") or "Level:" in line:
            level = line.strip()
        elif line.strip().lower().startswith("topics:"):
            topics = line.strip()[7:].strip()
        elif line.strip():
            description.append(line.strip())

    # tasks section
    tasks = []
    for m in re.finditer(r"#\s*(\d+\.\s.*?)(?=\n#\s*\d+\.|\Z)", src, re.DOTALL):
        task_text = re.sub(r"\n#\s*", " ", m.group(1)).strip()
        tasks.append(task_text)

    # code without docstring
    code = re.sub(r'^""".*?"""\s*', "", src, count=1, flags=re.DOTALL)
    code = re.sub(r"# YOUR TASK:.*", "", code, flags=re.DOTALL).strip()

    return {
        "path":   path,
        "stem":   path.stem,
        "slug":   slugify(path.stem[3:]) if len(path.stem) > 3 else slugify(path.stem),
        "number": path.stem[:2],
        "title":  title,
        "level":  level,
        "desc":   " ".join(description),
        "topics": topics,
        "tasks":  tasks,
        "code":   code,
    }

# ── CSS ───────────────────────────────────────────────────────────────────────

CSS = """
:root {
  --bg:#1e1e2e; --surface:#2a2a3e; --border:#3a3a5e;
  --text:#cdd6f4; --muted:#6c7086; --accent:#89b4fa;
  --green:#a6e3a1; --yellow:#f9e2af; --red:#f38ba8;
  --tag-bg:#313244;
}
body.light {
  --bg:#eff1f5; --surface:#ccd0da; --border:#bcc0cc;
  --text:#4c4f69; --muted:#8c8fa1; --accent:#1e66f5;
  --green:#40a02b; --yellow:#df8e1d; --red:#d20f39;
  --tag-bg:#dce0e8;
}
*{box-sizing:border-box;margin:0;padding:0}
body{background:var(--bg);color:var(--text);font-family:system-ui,sans-serif;line-height:1.6}
a{color:var(--accent);text-decoration:none} a:hover{text-decoration:underline}
header{background:var(--surface);border-bottom:1px solid var(--border);
  padding:1rem 2rem;display:flex;align-items:center;justify-content:space-between;
  position:sticky;top:0;z-index:10}
header h1{font-size:1.1rem;font-weight:700}
.theme-btn{background:var(--tag-bg);border:1px solid var(--border);color:var(--text);
  padding:.3rem .8rem;border-radius:6px;cursor:pointer;font-size:.85rem}
main{max-width:960px;margin:2rem auto;padding:0 1.5rem}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:1rem;margin-top:1.5rem}
.card{background:var(--surface);border:1px solid var(--border);border-radius:10px;
  padding:1.2rem;transition:border-color .2s}
.card:hover{border-color:var(--accent)}
.card-num{font-size:.8rem;color:var(--muted);margin-bottom:.3rem}
.card-title{font-size:1rem;font-weight:600;margin-bottom:.4rem}
.card-level{font-size:.8rem;color:var(--yellow);margin-bottom:.4rem}
.card-topics{font-size:.78rem;color:var(--muted)}
.section-title{font-size:1.2rem;font-weight:700;margin:2rem 0 .5rem;
  color:var(--accent);border-bottom:1px solid var(--border);padding-bottom:.4rem}
/* lesson page */
.lesson-header{margin-bottom:1.5rem}
.lesson-header h1{font-size:1.5rem;font-weight:700;margin-bottom:.4rem}
.lesson-meta{display:flex;gap:.8rem;flex-wrap:wrap;font-size:.85rem;color:var(--muted)}
.lesson-desc{background:var(--surface);border-left:3px solid var(--accent);
  padding:.8rem 1rem;border-radius:0 6px 6px 0;margin-bottom:1.5rem;font-size:.95rem}
pre{background:var(--surface);border:1px solid var(--border);border-radius:8px;
  padding:1.2rem;overflow-x:auto;font-size:.85rem;line-height:1.55;margin-bottom:1.5rem}
code{font-family:'JetBrains Mono','Fira Code',monospace}
.kw{color:#cba6f7} .st{color:var(--green)} .cm{color:var(--muted);font-style:italic}
.fn{color:var(--accent)} .nm{color:var(--yellow)}
.tasks{background:var(--surface);border:1px solid var(--green);
  border-radius:8px;padding:1rem 1.2rem;margin-bottom:1.5rem}
.tasks h3{color:var(--green);font-size:.95rem;margin-bottom:.6rem}
.tasks ol{padding-left:1.2rem} .tasks li{margin-bottom:.3rem;font-size:.9rem}
.nav{display:flex;justify-content:space-between;margin-top:1.5rem;
  padding-top:1rem;border-top:1px solid var(--border)}
.nav a{background:var(--surface);border:1px solid var(--border);
  padding:.5rem 1rem;border-radius:6px;font-size:.9rem;color:var(--accent)}
.nav a:hover{border-color:var(--accent);text-decoration:none}
footer{text-align:center;padding:2rem;color:var(--muted);font-size:.8rem;margin-top:2rem}
"""

JS = """
const btn = document.querySelector('.theme-btn');
const saved = localStorage.getItem('theme');
if (saved === 'light') document.body.classList.add('light');
btn.textContent = document.body.classList.contains('light') ? '🌙 Dark' : '☀️ Light';
btn.addEventListener('click', () => {
  document.body.classList.toggle('light');
  const isLight = document.body.classList.contains('light');
  localStorage.setItem('theme', isLight ? 'light' : 'dark');
  btn.textContent = isLight ? '🌙 Dark' : '☀️ Light';
});
"""

# ── page builders ─────────────────────────────────────────────────────────────

SECTIONS = [
    ("Basics", "01", "07"),
    ("Grammar", "08", "12"),
    ("Vocabulary & Projects", "13", "99"),
]

def wrap(title, body, back_link="../index.html"):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)} — English Interactive Course</title>
<style>{CSS}</style>
</head>
<body>
<header>
  <h1><a href="{back_link}" style="color:var(--text)">🇬🇧 English Interactive Course</a></h1>
  <button class="theme-btn">☀️ Light</button>
</header>
<main>{body}</main>
<footer>Interactive English Course · Run lessons with Python 3.8+</footer>
<script>{JS}</script>
</body>
</html>"""

def build_index(lessons):
    cards_by_section = {s: [] for s, _, _ in SECTIONS}
    for les in lessons:
        for section, start, end in SECTIONS:
            if start <= les["number"] <= end:
                cards_by_section[section].append(les)
                break

    body = "<h2 style='font-size:1.5rem;margin-bottom:.5rem'>Interactive English Course</h2>\n"
    body += "<p style='color:var(--muted);margin-bottom:1rem'>15 lessons · A1–B1 · Run each lesson with <code>python3 NN_file.py</code></p>\n"

    for section, _, _ in SECTIONS:
        cards = cards_by_section[section]
        if not cards:
            continue
        body += f'<div class="section-title">{section}</div>\n<div class="grid">\n'
        for les in cards:
            url = f"lekce/{les['slug']}.html"
            body += f"""<a href="{url}" style="text-decoration:none">
  <div class="card">
    <div class="card-num">Lesson {les['number']}</div>
    <div class="card-title">{html.escape(les['title'])}</div>
    <div class="card-level">{html.escape(les['level'])}</div>
    <div class="card-topics">{html.escape(les['topics'])}</div>
  </div>
</a>\n"""
        body += "</div>\n"
    return wrap("English Interactive Course", body, back_link="index.html")

def build_lesson_page(les, prev_les, next_les):
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
    <span>{html.escape(les['level'])}</span>
    <span>·</span>
    <span>{html.escape(les['topics'])}</span>
  </div>
</div>
<div class="lesson-desc">{html.escape(les['desc'])}</div>
<pre><code>{highlight(les['code'])}</code></pre>
{tasks_html}
<div class="nav">{prev_link}{next_link}</div>
"""
    return wrap(les["title"], body)

# ── main ──────────────────────────────────────────────────────────────────────

def main():
    root = pathlib.Path(".")
    out  = root / "web"
    lekce_dir = out / "lekce"
    lekce_dir.mkdir(parents=True, exist_ok=True)

    files = sorted(root.glob("[0-9][0-9]_*.py"))
    lessons = [parse_lesson(f) for f in files]

    (out / "index.html").write_text(build_index(lessons), encoding="utf-8")

    for i, les in enumerate(lessons):
        prev_les = lessons[i - 1] if i > 0 else None
        next_les = lessons[i + 1] if i < len(lessons) - 1 else None
        page = build_lesson_page(les, prev_les, next_les)
        (lekce_dir / f"{les['slug']}.html").write_text(page, encoding="utf-8")

    print(f"✓ Built {len(lessons)} lessons → web/")

if __name__ == "__main__":
    main()
