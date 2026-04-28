"""
FLASHCARDS — Spaced Repetition Vocabulary Drill
=================================================
Načte slovní zásobu ze všech lekcí a procvičuje ji.

Použití:
  python3 flashkarty.py              # procvičuj vše
  python3 flashkarty.py --lekce 3    # jen lekce 03
  python3 flashkarty.py --smer cz    # česky → anglicky
  python3 flashkarty.py --smer en    # anglicky → česky
  python3 flashkarty.py --stats      # zobraz statistiky
"""
import pathlib, re, random, json, argparse, datetime

PROGRESS_FILE = pathlib.Path("progress.json")

# ── progress store ─────────────────────────────────────────────────────────────

def load_progress():
    if PROGRESS_FILE.exists():
        return json.loads(PROGRESS_FILE.read_text(encoding="utf-8"))
    return {}

def save_progress(data):
    PROGRESS_FILE.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

def update_card(progress, key, correct):
    card = progress.get(key, {"correct": 0, "wrong": 0, "streak": 0, "next_review": 0})
    if correct:
        card["correct"] += 1
        card["streak"]  += 1
        # simple interval: 1, 2, 4, 8, 16 days
        days = min(2 ** card["streak"], 16)
    else:
        card["wrong"] += 1
        card["streak"] = 0
        days = 0
    card["next_review"] = (datetime.date.today() + datetime.timedelta(days=days)).isoformat()
    progress[key] = card
    return progress

def due_today(card):
    nr = card.get("next_review", "0")
    return nr <= datetime.date.today().isoformat()

# ── vocabulary extractor ───────────────────────────────────────────────────────

def extract_vocab(path):
    """Extract EN→CZ pairs from VOCABULARY / WORDS / dict literals in a lesson file."""
    src = path.read_text(encoding="utf-8")
    pairs = {}
    # match "english key": "czech value"  (handles both ' and ")
    pattern = re.compile(
        r'["\']([A-Za-z][^"\']{1,50}?)["\']\s*:\s*["\']([^\'"]{1,80})["\']'
    )
    for m in pattern.finditer(src):
        en, cz = m.group(1).strip(), m.group(2).strip()
        # filter out code-like strings
        if any(c in en for c in "(){}[]\\="):
            continue
        if len(en) > 60 or len(cz) > 80:
            continue
        if en[0].isupper() and len(en) > 30:
            continue
        pairs[en] = cz
    return pairs

def load_all_vocab(lesson_filter=None):
    root = pathlib.Path(".")
    all_vocab = {}  # (en, cz, lesson_num)
    for path in sorted(root.glob("[0-9][0-9]_*.py")):
        num = path.stem[:2]
        if lesson_filter and num != f"{lesson_filter:02d}":
            continue
        pairs = extract_vocab(path)
        for en, cz in pairs.items():
            all_vocab[f"{num}|{en}"] = (en, cz, num)
    return all_vocab

# ── quiz engine ────────────────────────────────────────────────────────────────

def run_quiz(vocab, direction, progress, limit=None):
    keys = list(vocab.keys())

    # prioritise due cards
    due   = [k for k in keys if k in progress and due_today(progress[k])]
    fresh = [k for k in keys if k not in progress]
    rest  = [k for k in keys if k in progress and not due_today(progress[k])]
    ordered = due + random.sample(fresh, min(len(fresh), 30)) + random.sample(rest, min(len(rest), 10))

    if limit:
        ordered = ordered[:limit]

    correct_total, wrong_total = 0, 0

    print(f"\n  Cards to review: {len(ordered)}")
    print("  Type 'skip' to skip, 'quit' to stop.\n")
    print("-" * 55)

    for key in ordered:
        en, cz, num = vocab[key]
        if direction == "cz":
            prompt, answer = cz, en
        else:
            prompt, answer = en, cz

        print(f"  [Lesson {num}]  {prompt}")
        ans = input("  → ").strip()

        if ans.lower() == "quit":
            break
        if ans.lower() == "skip":
            print("  ⏭  Skipped\n")
            continue

        correct = ans.lower() == answer.lower()
        if correct:
            print("  ✓ Correct!\n")
            correct_total += 1
        else:
            print(f"  ✗ Answer: {answer}\n")
            wrong_total += 1

        progress = update_card(progress, key, correct)

    save_progress(progress)
    total = correct_total + wrong_total
    if total:
        pct = int(correct_total / total * 100)
        print(f"\n  Session result: {correct_total}/{total} ({pct}%)")

# ── stats ──────────────────────────────────────────────────────────────────────

def show_stats(progress, vocab):
    print("\n" + "=" * 55)
    print("  VOCABULARY PROGRESS")
    print("=" * 55)
    total_vocab = len(vocab)
    seen   = len([k for k in vocab if k in progress])
    strong = len([k for k in vocab if k in progress and progress[k]["streak"] >= 3])
    due    = len([k for k in vocab if k in progress and due_today(progress[k])])
    fresh  = total_vocab - seen
    print(f"\n  Total vocabulary:  {total_vocab}")
    print(f"  Seen at least once:{seen}")
    print(f"  Strong (streak ≥3):{strong}")
    print(f"  Due for review:    {due}")
    print(f"  Not yet seen:      {fresh}")

    if progress:
        by_lesson = {}
        for key, card in progress.items():
            num = key.split("|")[0]
            ls = by_lesson.setdefault(num, {"correct": 0, "wrong": 0})
            ls["correct"] += card["correct"]
            ls["wrong"]   += card["wrong"]
        print("\n  Per-lesson accuracy:")
        for num in sorted(by_lesson):
            c = by_lesson[num]["correct"]
            w = by_lesson[num]["wrong"]
            total = c + w
            pct = int(c / total * 100) if total else 0
            bar = "█" * (pct // 10) + "░" * (10 - pct // 10)
            print(f"  Lesson {num}  {bar} {pct}%  ({c}/{total})")

# ── main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="English flashcard drill")
    parser.add_argument("--lekce", type=int, help="Lesson number (1–30)")
    parser.add_argument("--smer", choices=["cz","en"], default="cz",
                        help="cz = Czech→English (default) | en = English→Czech")
    parser.add_argument("--stats", action="store_true", help="Show progress stats")
    parser.add_argument("--pocet", type=int, default=None, help="Number of cards per session")
    args = parser.parse_args()

    vocab    = load_all_vocab(args.lekce)
    progress = load_progress()

    print("=" * 55)
    print("  🎴 FLASHCARDS — English Vocabulary Drill")
    print("=" * 55)

    if not vocab:
        print("\n  No vocabulary found. Make sure lesson files are present.")
        return

    if args.stats:
        show_stats(progress, vocab)
        return

    direction_label = "Czech → English" if args.smer == "cz" else "English → Czech"
    lesson_label = f"Lesson {args.lekce:02d}" if args.lekce else "All lessons"
    print(f"\n  Mode: {direction_label} | {lesson_label}")
    run_quiz(vocab, args.smer, progress, args.pocet)

if __name__ == "__main__":
    main()
