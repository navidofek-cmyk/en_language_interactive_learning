"""
CLOZE TEST GENERATOR — Fill-in-the-blank from any lesson
===========================================================
Použití:
  python3 cloze_test.py              # random test ze všech lekcí
  python3 cloze_test.py --lekce 8   # test z lekce 08
  python3 cloze_test.py --obtiznost easy/medium/hard
  python3 cloze_test.py --pocet 10  # počet otázek
"""
import pathlib, re, random, argparse

def extract_examples(path):
    """Extract quoted English sentences from lesson files."""
    src = path.read_text(encoding="utf-8")
    sentences = []
    # Get sentences from tuples like ("English sentence", "Czech")
    for m in re.finditer(
        r'\("([A-Z][^"]{10,120}?[.!?])"\s*,\s*"[^"]*"\)', src
    ):
        sentences.append(m.group(1).strip())
    # Also get standalone example sentences in lists
    for m in re.finditer(r'"([A-Z][A-Za-z][^"]{12,100}[.!?])"', src):
        s = m.group(1).strip()
        if not any(c in s for c in ["→", "✓", "✗", "=", "("]):
            sentences.append(s)
    return list(dict.fromkeys(sentences))  # deduplicate

def make_cloze(sentence, difficulty="medium"):
    """Remove words from a sentence to create a gap-fill exercise."""
    words = sentence.split()
    if len(words) < 4:
        return None

    # Choose which words to remove
    candidates = []
    skip = {"a", "an", "the", "to", "of", "in", "on", "at", "and",
            "or", "but", "I", "you", "he", "she", "it", "we", "they"}

    for i, word in enumerate(words):
        clean = re.sub(r"[^a-zA-Z'']", "", word)
        if clean.lower() not in skip and len(clean) > 2:
            candidates.append((i, word, clean))

    if not candidates:
        return None

    if difficulty == "easy":
        n_gaps = 1
    elif difficulty == "hard":
        n_gaps = min(3, len(candidates))
    else:
        n_gaps = min(2, len(candidates))

    chosen = random.sample(candidates, min(n_gaps, len(candidates)))
    chosen_indices = {i for i, _, _ in chosen}
    answers = {i: (word, clean) for i, word, clean in chosen}

    gapped = []
    for i, word in enumerate(words):
        if i in chosen_indices:
            gapped.append("___")
        else:
            gapped.append(word)

    return {
        "sentence":   sentence,
        "gapped":     " ".join(gapped),
        "answers":    answers,
        "answer_list": [clean for _, (_, clean) in sorted(answers.items())],
    }

def run_cloze_test(lesson_filter, difficulty, count):
    root = pathlib.Path(".")
    all_sentences = []

    for path in sorted(root.glob("[0-9][0-9]_*.py")):
        num = path.stem[:2]
        if lesson_filter and num != f"{lesson_filter:02d}":
            continue
        sentences = extract_examples(path)
        for s in sentences:
            all_sentences.append((num, path.stem, s))

    if not all_sentences:
        print("  No sentences found. Check that lesson files are present.")
        return

    random.shuffle(all_sentences)
    items = []
    for num, stem, sentence in all_sentences:
        cloze = make_cloze(sentence, difficulty)
        if cloze:
            items.append((num, stem, cloze))
        if len(items) >= count:
            break

    if not items:
        print("  Could not generate cloze items from available sentences.")
        return

    print(f"\n  {len(items)} gap-fill questions | difficulty: {difficulty}")
    print("  Fill in the missing word(s). Type your answer.\n")
    print("-" * 55)

    correct, total = 0, 0
    for num, stem, cloze in items:
        print(f"\n  [Lesson {num}]  {cloze['gapped']}")
        answers = cloze["answer_list"]
        for j, expected in enumerate(answers, 1):
            label = f"Gap {j}" if len(answers) > 1 else "Answer"
            ans = input(f"  {label}: ").strip()
            total += 1
            if ans.lower() == expected.lower():
                print("  ✓ Correct!")
                correct += 1
            else:
                print(f"  ✗ Answer: {expected}")

    print("\n" + "=" * 55)
    pct = int(correct / total * 100) if total else 0
    print(f"  Result: {correct}/{total} ({pct}%)")
    if pct >= 90: print("  🏆 Excellent!")
    elif pct >= 70: print("  👍 Good job!")
    elif pct >= 50: print("  📖 Keep practising!")
    else: print("  💪 Review the lessons and try again.")

def main():
    parser = argparse.ArgumentParser(description="English cloze test generator")
    parser.add_argument("--lekce",     type=int, help="Lesson number (1–45)")
    parser.add_argument("--obtiznost", choices=["easy", "medium", "hard"],
                        default="medium", help="Difficulty (default: medium)")
    parser.add_argument("--pocet",     type=int, default=10, help="Number of questions")
    args = parser.parse_args()

    print("=" * 55)
    print("  📝 CLOZE TEST — Fill in the Gaps")
    print("=" * 55)

    run_cloze_test(args.lekce, args.obtiznost, args.pocet)

if __name__ == "__main__":
    main()
