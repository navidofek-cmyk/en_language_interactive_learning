"""
LESSON 35: Quantifiers
========================
⭐⭐ Level: A2–B1 | Elementary

Kvantifikátory — some, any, much, many, few, little, a lot of...
Topics: countable · uncountable · some/any · much/many · few/little · enough/too
"""
import random

QUANTIFIERS = {
    "some":       ("affirmative, offers, requests",   "I have SOME milk. / Would you like SOME?"),
    "any":        ("negatives, questions, conditions", "I don't have ANY sugar. / Do you have ANY?"),
    "much":       ("uncountable — questions/negatives","I don't have MUCH time."),
    "many":       ("countable — questions/negatives",  "How MANY people came?"),
    "a lot of":   ("large quantity, any sentence",     "There's A LOT OF traffic today."),
    "lots of":    ("informal version of a lot of",     "We have LOTS OF time."),
    "a few":      ("small positive number (countable)","I have A FEW friends here."),
    "few":        ("almost none — negative feel",      "FEW people know this fact."),
    "a little":   ("small amount (uncountable)",       "Add A LITTLE salt."),
    "little":     ("almost none — negative feel",      "There's LITTLE hope left."),
    "enough":     ("sufficient quantity",              "Is there ENOUGH food for everyone?"),
    "too many":   ("excessive countable",              "There are TOO MANY cars in cities."),
    "too much":   ("excessive uncountable",            "I drank TOO MUCH coffee."),
    "no":         ("zero quantity",                    "There's NO milk left."),
    "none":       ("zero — standalone",               "None of the students passed."),
    "each/every": ("individual / all without exception","Each student got a certificate."),
    "both":       ("two things",                       "Both answers are correct."),
    "either":     ("one of two",                       "You can take either road."),
    "neither":    ("not one nor the other",            "Neither option is ideal."),
    "all":        ("entire group",                     "All students must attend."),
    "most":       ("majority",                         "Most people enjoy music."),
    "several":    ("more than two, not very many",     "I've been there several times."),
}

COUNTABLE = ["apple", "car", "book", "person", "idea", "problem", "question"]
UNCOUNTABLE = ["water", "money", "information", "advice", "furniture", "luggage", "news",
               "traffic", "weather", "equipment", "knowledge", "work", "music"]

print("=" * 55)
print("  LESSON 35: Quantifiers")
print("=" * 55)

print("\n📚 COUNTABLE vs UNCOUNTABLE (reminder):")
print("-" * 55)
print(f"  Countable:   {' · '.join(COUNTABLE)}")
print(f"  Uncountable: {' · '.join(UNCOUNTABLE)}")
print()
print("  ⚠️  Common Czech mistakes:")
print("    'an advice' ✗ → 'a piece of advice' ✓")
print("    'an information' ✗ → 'some information' ✓")
print("    'a luggage' ✗ → 'a piece of luggage' ✓")
print("    'a news' ✗ → 'some news' ✓")

print("\n📚 QUANTIFIERS:")
print("-" * 55)
for q, (use, example) in QUANTIFIERS.items():
    print(f"  {q:<14} [{use}]")
    print(f"             {example}\n")

print("\n📝 SOME vs ANY:")
print("-" * 55)
print("  SOME → affirmative:  I have some eggs.")
print("         offers:       Would you like some tea?")
print("         requests:     Could I have some water?")
print()
print("  ANY  → negatives:    I don't have any butter.")
print("         questions:    Do you have any questions?")
print("         conditions:   If you find any, let me know.")

print("\n📝 A FEW vs FEW / A LITTLE vs LITTLE:")
print("-" * 55)
print("  A FEW / A LITTLE = some, but not much → POSITIVE meaning")
print("    'I have a few friends here.' (= some friends, good)")
print("    'Add a little more salt.'   (= a small amount)")
print()
print("  FEW / LITTLE = almost none → NEGATIVE/pessimistic meaning")
print("    'Few people care about this.'  (= almost nobody)")
print("    'There's little we can do.'    (= almost nothing)")

print("\n🎯 QUIZ — choose the correct quantifier:")
print("-" * 55)
quiz = [
    ("There isn't ___ sugar left. (uncountable, negative)", "any / much"),
    ("I need ___ minutes — just wait! (small positive)", "a few"),
    ("She has ___ knowledge of the subject. (almost none)", "little"),
    ("How ___ money do you need? (uncountable, question)", "much"),
    ("'News' is uncountable — you say ___ news, not 'a news'.", "some"),
    ("There are ___ people in the queue today. (excessive)", "too many"),
]
score = 0
for sentence, answer in quiz:
    print(f"  {sentence}")
    ans = input("  → ").strip()
    if any(a.strip().lower() in ans.lower() for a in answer.split("/")):
        print("  ✓ Correct!\n"); score += 1
    else:
        print(f"  ✗ Answer: {answer}\n")
print(f"  Score: {score}/6")

# YOUR TASK:
# 1. Describe what's in your fridge using quantifiers (some, a few, a lot of, no...)
# 2. Write 5 sentences about your city using much/many/a lot of/few/little
# 3. Write a complaint letter mentioning problems using too much/too many
