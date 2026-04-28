"""
migrate.py — converts Python lesson files to clean JSON data files.
Run once: python3 migrate.py
Output: data/*.json and data/articles/*.json
"""
import pathlib, re, json, unicodedata

def slugify(text):
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = re.sub(r"[^\w\s-]", "", text.lower())
    return re.sub(r"[-\s]+", "_", text).strip("_")

def parse_py(path):
    src = path.read_text(encoding="utf-8")
    num = path.stem[:2]
    is_article = path.parent.name == "clanky"

    # metadata
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

    # vocabulary
    vocab = []
    seen = set()
    for m in re.finditer(r'^[A-Z_]+\s*=\s*\{([^}]+)\}', src, re.MULTILINE | re.DOTALL):
        for pair in re.finditer(
            r'["\']([A-Za-z /\-\'\.,!?&()]+?)["\']\s*:\s*["\']([^"\']{1,80})["\']',
            m.group(1)
        ):
            en, cz = pair.group(1).strip(), pair.group(2).strip()
            if len(en) > 1 and len(cz) > 1 and not any(c in en for c in "{}[]\\=") and en.lower() not in seen:
                seen.add(en.lower())
                vocab.append({"en": en, "cz": cz})

    # dialogue
    dialogue = []
    for m in re.finditer(
        r'\(\s*["\']([AB]|Waiter|Customer|Doctor|Patient|Assistant|Candidate|Interviewer)["\'],\s*["\']([^"\']{4,200})["\']',
        src
    ):
        dialogue.append({"speaker": m.group(1), "text": m.group(2)})

    # notes (lines with grammar markers)
    notes = []
    for m in re.finditer(r'print\(["\']([^"\']{10,200})["\']', src):
        s = m.group(1)
        if any(c in s for c in ["✓", "✗", "⚠️", "→", "≠", "NOT", "NE:"]):
            notes.append(s.replace("  ", " ").strip())

    # examples
    examples = []
    for m in re.finditer(
        r'\(\s*["\']([A-Z][^"\']{8,120}[.!?])["\'],\s*\n?\s*["\']([^"\']{4,120})["\']', src
    ):
        en, cz = m.group(1).strip(), m.group(2).strip()
        if not any(c in en for c in ["→","✓","✗","=","("]):
            examples.append({"en": en, "cz": cz})

    # quiz items
    quiz = []
    for m in re.finditer(
        r'\(\s*["\']([^"\']+___[^"\']*)["\'],\s*\n?\s*["\']([^"\']{1,60})["\']', src
    ):
        quiz.append({"type": "fill", "sentence": m.group(1).strip(), "answer": m.group(2).strip()})

    # article text
    article_text = ""
    if is_article:
        am = re.search(r'ARTICLE\s*=\s*"""(.*?)"""', src, re.DOTALL)
        if am: article_text = am.group(1).strip()

    # tasks
    tasks = []
    for m in re.finditer(r'#\s*(\d+\.\s.+)', src):
        tasks.append(m.group(1).strip())

    slug_base = path.stem[3:] if len(path.stem) > 3 else path.stem
    result = {
        "num":         num,
        "slug":        slugify(slug_base),
        "title":       title,
        "level":       level,
        "topics":      topics,
        "description": " ".join(desc_lines),
        "vocabulary":  vocab[:50],
        "dialogue":    dialogue[:12],
        "notes":       notes[:15],
        "examples":    examples[:8],
        "quiz":        quiz[:8],
        "tasks":       tasks[:5],
    }
    if article_text:
        result["article_text"] = article_text
    return result

def main():
    root = pathlib.Path(".")
    (root / "data").mkdir(exist_ok=True)
    (root / "data" / "articles").mkdir(exist_ok=True)

    for path in sorted(root.glob("[0-9][0-9]_*.py")):
        if path.stem in ("migrate", "flashkarty", "progress", "streak", "cloze_test"):
            continue
        data = parse_py(path)
        out = root / "data" / f"{path.stem}.json"
        out.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"  ✓ {path.stem}")

    for path in sorted((root / "clanky").glob("[0-9][0-9]_*.py")):
        data = parse_py(path)
        out = root / "data" / "articles" / f"{path.stem}.json"
        out.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"  ✓ clanky/{path.stem}")

    lesson_count  = len(list((root/"data").glob("[0-9][0-9]_*.json")))
    article_count = len(list((root/"data"/"articles").glob("*.json")))
    print(f"\n✓ Migrated {lesson_count} lessons + {article_count} articles → data/")

if __name__ == "__main__":
    main()
