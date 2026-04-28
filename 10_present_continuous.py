"""
LESSON 10: Present Continuous
================================
⭐⭐ Level: A2 | Elementary

Přítomný čas průběhový — co se děje právě teď nebo dočasně.
Topics: am/is/are + -ing · uses · vs. present simple · stative verbs
"""
import random

CONJUGATION = {
    "I":          "am working",
    "you":        "are working",
    "he / she":   "is working",
    "we / they":  "are working",
}

SPELLING_RULES = [
    ("Most verbs",              "add -ing",      "work → working"),
    ("Silent -e at end",        "drop e + -ing", "live → living"),
    ("Short vowel + consonant", "double + -ing", "sit → sitting"),
    ("Ends in -ie",             "ie → y + -ing", "lie → lying"),
]

USES = {
    "Right now (právě teď)":        "She is reading a book right now.",
    "Temporary (dočasné děje)":     "I'm staying at a hotel this week.",
    "Changing situations":          "Prices are rising every year.",
    "Planned future arrangement":   "We are meeting at 6 pm tomorrow.",
    "Annoyance (with 'always')":    "He is always losing his keys!",
}

STATIVE_VERBS = [
    "know", "understand", "believe", "think (opinion)", "want",
    "need", "like", "love", "hate", "prefer", "see", "hear",
    "smell", "taste", "feel (emotion)", "own", "have (possession)",
    "belong", "contain", "seem", "appear",
]

VS_SIMPLE = [
    ("I read every morning.     (habit)",      "I am reading right now.    (this moment)"),
    ("He lives in Prague.       (permanent)",  "He is living in Brno now.  (temporary)"),
    ("She works in a bank.      (her job)",    "She is working late today. (right now)"),
    ("They play football.       (hobby)",      "They are playing now.      (in progress)"),
]

print("=" * 55)
print("  LESSON 10: Present Continuous")
print("=" * 55)

print("\n📚 HOW TO FORM IT:  am/is/are + verb-ing")
print("-" * 55)
for pronoun, form in CONJUGATION.items():
    print(f"  {pronoun:<14} {form}")

print("\n📚 SPELLING RULES for -ing:")
print("-" * 55)
for rule, change, example in SPELLING_RULES:
    print(f"  {rule:<32} {change:<16} {example}")

print("\n📚 WHEN TO USE IT:")
print("-" * 55)
for use, example in USES.items():
    print(f"  {use}")
    print(f"    → {example}\n")

print("\n📚 STATIVE VERBS — NOT used in continuous:")
print("-" * 55)
print("  These verbs describe states (not actions) — no -ing form!\n")
print("  " + " · ".join(STATIVE_VERBS))
print()
print("  ✓ I know the answer.   (NE: I am knowing)")
print("  ✓ She loves coffee.    (NE: She is loving)")
print("  ✓ Do you understand?   (NE: Are you understanding?)")

print("\n📚 PRESENT SIMPLE vs. PRESENT CONTINUOUS:")
print("-" * 55)
for simple, continuous in VS_SIMPLE:
    print(f"  {simple}")
    print(f"  {continuous}\n")

print("\n💬 QUICK QUIZ — simple or continuous?")
print("-" * 55)
quiz = [
    ("She usually ___ (drink) tea, but today she ___ (drink) coffee.",
     "drinks / is drinking"),
    ("Look! The children ___ (play) in the garden.", "are playing"),
    ("I ___ (not / understand) this question.", "don't understand"),
    ("He ___ (work) late this week because of a deadline.", "is working"),
    ("Water ___ (boil) at 100 degrees.", "boils"),
]
score = 0
for sentence, answer in quiz:
    print(f"  {sentence}")
    ans = input("  → ").strip()
    if ans.lower() == answer.lower():
        print("  ✓ Correct!\n")
        score += 1
    else:
        print(f"  ✗ Answer: {answer}\n")
print(f"  Score: {score}/5")

# YOUR TASK:
# 1. Look around you right now and write 5 sentences about what
#    is happening using present continuous
# 2. Write 3 sentence pairs showing the contrast between
#    present simple (habit) and present continuous (now)
# 3. Find 5 stative verbs not listed above and explain why they
#    cannot be used in the continuous form
