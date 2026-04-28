"""
LESSON 08: Present Simple
===========================
⭐⭐ Level: A1–A2 | Elementary

Přítomný čas prostý — pravidelné děje, fakta, zvyky.
Topics: present simple · third person -s · negatives · questions
"""
import random

CONJUGATION = {
    "I":    "work",      "you":  "work",
    "he":   "works",     "she":  "works",
    "it":   "works",     "we":   "work",
    "they": "work",
}

IRREGULAR_VERBS = {
    "be":  {"I": "am", "you": "are", "he/she/it": "is",  "we/they": "are"},
    "have":{"I": "have","you":"have","he/she/it":"has",   "we/they": "have"},
    "do":  {"I": "do", "you": "do", "he/she/it": "does", "we/they": "do"},
    "go":  {"I": "go", "you": "go", "he/she/it": "goes", "we/they": "go"},
}

SPELLING_RULES = [
    ("Most verbs",              "add -s",    "work → works, play → plays"),
    ("Ends in -s,-sh,-ch,-x,-o","add -es",   "watch → watches, go → goes"),
    ("Ends in consonant + y",   "y → -ies",  "study → studies, fly → flies"),
]

USES = {
    "Facts & general truths": "Water boils at 100°C.",
    "Habits & routines":      "She drinks coffee every morning.",
    "Permanent situations":   "He lives in Prague.",
    "Timetables & schedules": "The train leaves at 8:15.",
    "Instructions":           "First, you open the file.",
}

EXAMPLE_SENTENCES = [
    ("I get up at 7 o'clock every day.",    "Vstávám každý den v 7 hodin."),
    ("She doesn't eat meat.",               "Ona nejí maso."),
    ("Do you speak English?",              "Mluvíš anglicky?"),
    ("He works in a hospital.",            "Pracuje v nemocnici."),
    ("We don't live in a big city.",        "Nežijeme ve velkém městě."),
    ("Does she have a car?",               "Má ona auto?"),
    ("They don't watch TV very often.",    "Moc televizí nesledují."),
    ("It rains a lot in autumn.",          "Na podzim hodně prší."),
]

print("=" * 55)
print("  LESSON 08: Present Simple")
print("=" * 55)

print("\n📚 WHEN TO USE IT:")
print("-" * 55)
for use, example in USES.items():
    print(f"  {use:<30} → {example}")

print("\n📚 CONJUGATION — verb 'to work':")
print("-" * 55)
for pronoun, form in CONJUGATION.items():
    s_note = "  ← third person adds -s!" if pronoun in ("he","she","it") else ""
    print(f"  {pronoun:<8} {form}{s_note}")

print("\n📚 SPELLING RULES for third person -s/-es/-ies:")
print("-" * 55)
for rule, change, example in SPELLING_RULES:
    print(f"  {rule:<32} {change:<12} {example}")

print("\n📚 NEGATIVES & QUESTIONS:")
print("-" * 55)
print("  (+)  I    work   / He   works")
print("  (−)  I    don't work  / He doesn't work")
print("  (?)  Do   you   work? / Does he    work?")
print()
print("  ⚠️  In negatives & questions use DO/DOES — the main verb stays in base form:")
print("  ✓ Does she WORK?   (NE: Does she workS?)")
print("  ✓ He doesn't HAVE. (NE: He doesn't haS.)")

print("\n💬 EXAMPLE SENTENCES:")
print("-" * 55)
for en, cz in EXAMPLE_SENTENCES:
    print(f"  {en}")
    print(f"    → {cz}\n")

print("\n🎯 QUIZ — correct form of the verb:")
print("-" * 55)
quiz = [
    ("She ___ (work) in a bank.", "works"),
    ("They ___ (not / like) horror films.", "don't like"),
    ("___ he ___ (speak) French? (question)", "Does ... speak"),
    ("I ___ (get up) at 6 every morning.", "get up"),
    ("It ___ (rain) a lot here in spring.", "rains"),
    ("We ___ (not / have) a garden.", "don't have"),
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
print(f"  Score: {score}/6")

# YOUR TASK:
# 1. Write 5 true sentences about your own daily routine using present simple
# 2. Convert these sentences to negatives and questions
# 3. Create a "describe a friend" paragraph using only present simple
