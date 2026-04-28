"""
LESSON 31: Relative Clauses
=============================
⭐⭐⭐ Level: B1 | Pre-Intermediate

Vztažné věty — who, which, that, where, whose, when.
Topics: defining · non-defining · relative pronouns · omission
"""
import random

PRONOUNS = {
    "who":   ("people",                  "The woman WHO called is my sister."),
    "which": ("things / animals",        "The book WHICH I bought is great."),
    "that":  ("people or things (def.)", "The car THAT I drive is old."),
    "where": ("places",                  "The city WHERE I grew up is Prague."),
    "whose": ("possession",              "The man WHOSE car was stolen called police."),
    "when":  ("time",                    "I remember the day WHEN we met."),
    "whom":  ("people, formal object",   "The person WHOM I spoke to was helpful."),
}

DEFINING = [
    ("The man who lives next door is very quiet.",
     "Muž, který bydlí vedle, je velmi tichý."),
    ("Is this the book that you recommended?",
     "Je to ta kniha, kterou jsi doporučil/a?"),
    ("Do you know a good restaurant where we can eat?",
     "Znáš dobrý restauraci, kde můžeme jíst?"),
    ("The woman whose bag was stolen reported it.",
     "Žena, které ukradli kabelku, to nahlásila."),
]

NON_DEFINING = [
    ("My sister, who lives in London, is a doctor.",
     "Moje sestra, která žije v Londýně, je doktorka."),
    ("Prague, which is the capital of Czechia, is beautiful.",
     "Praha, která je hlavním městem Česka, je krásná."),
    ("His new car, which cost a fortune, broke down.",
     "Jeho nové auto, které stálo majlant, se pokazilo."),
]

print("=" * 55)
print("  LESSON 31: Relative Clauses")
print("=" * 55)

print("\n📚 RELATIVE PRONOUNS:")
print("-" * 55)
for pronoun, (use, example) in PRONOUNS.items():
    print(f"  {pronoun:<8} → {use:<30} {example}")

print("\n📚 DEFINING vs NON-DEFINING:")
print("-" * 55)
print("  DEFINING — identifies which one (no commas):")
print("    'The man WHO called is my boss.' (which man? — the one who called)\n")
print("  NON-DEFINING — adds extra info (use commas):")
print("    'My boss, WHO called, is very busy.' (we already know who)\n")
print("  ⚠️  'that' CANNOT be used in non-defining clauses:")
print("    ✗ My car, that is red, is fast.")
print("    ✓ My car, which is red, is fast.")

print("\n📚 DEFINING RELATIVE CLAUSES:")
print("-" * 55)
for en, cz in DEFINING:
    print(f"  {en}")
    print(f"    → {cz}\n")

print("\n📚 NON-DEFINING RELATIVE CLAUSES:")
print("-" * 55)
for en, cz in NON_DEFINING:
    print(f"  {en}")
    print(f"    → {cz}\n")

print("\n📝 OMITTING THE PRONOUN:")
print("-" * 55)
print("  You can omit 'who/which/that' when it is the OBJECT:")
print("  'The book (that) I read was great.'  ← 'that' is object → can omit")
print("  'The man who called was angry.'      ← 'who' is subject → cannot omit")

print("\n🎯 QUIZ — choose the right pronoun:")
print("-" * 55)
quiz = [
    ("The woman ___ helped me was very kind.",                    "who"),
    ("Is this the town ___ you grew up?",                        "where"),
    ("The film ___ we watched last night was brilliant.",         "that / which"),
    ("That's the student ___ phone kept ringing.",               "whose"),
    ("The day ___ I got married was the happiest of my life.",   "when"),
    ("He spoke to the manager, ___ was very understanding.",     "who"),
]
score = 0
for sentence, answer in quiz:
    print(f"  {sentence}")
    ans = input("  → ").strip()
    if ans.lower() in answer.lower():
        print("  ✓ Correct!\n"); score += 1
    else:
        print(f"  ✗ Answer: {answer}\n")
print(f"  Score: {score}/6")

# YOUR TASK:
# 1. Combine these pairs using a relative clause:
#    a) I have a friend. She speaks five languages.
#    b) That's the restaurant. We had our first date there.
#    c) The man was arrested. His car contained stolen goods.
# 2. Write 3 non-defining relative clauses about people you know
# 3. Write a paragraph describing your city using at least 3 relative clauses
