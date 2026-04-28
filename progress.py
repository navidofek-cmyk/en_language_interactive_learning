"""
PROGRESS TRACKER — Quiz Score Logger
======================================
Ukládá skóre z kvízů, zobrazuje přehled a doporučuje co procvičovat.

Automaticky se spustí po každém kvízu — nebo ručně:
  python3 progress.py           # zobraz celkový přehled
  python3 progress.py --reset   # smaž vše a začni znovu
"""
import pathlib, json, datetime, re, argparse

SCORES_FILE = pathlib.Path("scores.json")
LESSON_META = {}  # populated from lesson docstrings

def load_scores():
    if SCORES_FILE.exists():
        return json.loads(SCORES_FILE.read_text(encoding="utf-8"))
    return {}

def save_score(lesson_num, score, total):
    """Call this from any lesson to log a result."""
    scores = load_scores()
    key = f"{lesson_num:02d}"
    entry = {
        "date":    datetime.date.today().isoformat(),
        "score":   score,
        "total":   total,
        "percent": round(score / total * 100) if total else 0,
    }
    scores.setdefault(key, []).append(entry)
    SCORES_FILE.write_text(json.dumps(scores, ensure_ascii=False, indent=2), encoding="utf-8")
    return entry

def parse_lesson_meta():
    root = pathlib.Path(".")
    meta = {}
    for path in sorted(root.glob("[0-9][0-9]_*.py")):
        num = path.stem[:2]
        src = path.read_text(encoding="utf-8")
        doc = re.match(r'"""(.*?)"""', src, re.DOTALL)
        if doc:
            lines = doc.group(1).strip().splitlines()
            title = re.sub(r"^#\s*", "", lines[0].strip()) if lines else path.stem
            level = next((l.strip() for l in lines if "Level:" in l or "⭐" in l), "")
            meta[num] = {"title": title, "level": level}
    return meta

def show_progress():
    scores = load_scores()
    meta   = parse_lesson_meta()
    root   = pathlib.Path(".")
    all_lessons = sorted(root.glob("[0-9][0-9]_*.py"))

    print("=" * 60)
    print("  📊 PROGRESS OVERVIEW")
    print("=" * 60)

    completed = 0
    needs_work = []

    for path in all_lessons:
        num = path.stem[:2]
        info = meta.get(num, {})
        title = info.get("title", path.stem)[:35]
        level = info.get("level", "")

        if num in scores:
            entries = scores[num]
            last    = entries[-1]
            best    = max(e["percent"] for e in entries)
            avg     = int(sum(e["percent"] for e in entries) / len(entries))
            attempts = len(entries)

            if best >= 80:
                status = "✓"
                completed += 1
            elif best >= 50:
                status = "~"
                needs_work.append(num)
            else:
                status = "✗"
                needs_work.append(num)

            bar = "█" * (best // 10) + "░" * (10 - best // 10)
            print(f"  [{status}] {num} {title:<36} {bar} {best}% (best) | {attempts}x done")
        else:
            print(f"  [ ] {num} {title:<36} {'░' * 10}  not yet attempted")

    total = len(all_lessons)
    print()
    print(f"  Completed (≥80%): {completed}/{total}")
    if needs_work:
        print(f"  Needs work:  lessons {', '.join(needs_work[:5])}")

    if scores:
        print("\n  📅 RECENT ACTIVITY:")
        print("-" * 60)
        recent = []
        for num, entries in scores.items():
            for e in entries:
                recent.append((e["date"], num, e["score"], e["total"], e["percent"]))
        recent.sort(reverse=True)
        for date, num, score, total, pct in recent[:8]:
            m = meta.get(num, {})
            title = m.get("title", f"Lesson {num}")[:30]
            print(f"  {date}  Lesson {num} — {title:<32} {score}/{total} ({pct}%)")

    print()
    if completed == total:
        print("  🏆 Course complete! Try the flashcards: python3 flashkarty.py")
    elif completed >= total * 0.5:
        print("  👍 Good progress! Keep going.")
    else:
        print("  💪 You're getting started — consistency is the key!")

def reset_progress():
    confirm = input("  Reset ALL progress? This cannot be undone. (yes/no): ")
    if confirm.lower() == "yes":
        if SCORES_FILE.exists():
            SCORES_FILE.unlink()
        fp = pathlib.Path("progress.json")
        if fp.exists():
            fp.unlink()
        print("  ✓ Progress reset.")
    else:
        print("  ✗ Cancelled.")

def main():
    parser = argparse.ArgumentParser(description="English course progress tracker")
    parser.add_argument("--reset", action="store_true", help="Reset all progress data")
    args = parser.parse_args()
    if args.reset:
        reset_progress()
    else:
        show_progress()

if __name__ == "__main__":
    main()
