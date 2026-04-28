"""
LESSON 09: Past Simple
========================
⭐⭐ Level: A2 | Elementary

Minulý čas prostý — dokončené děje v minulosti.
Topics: regular verbs (-ed) · irregular verbs · negatives · questions
"""
import random

REGULAR_EXAMPLES = {
    "work":  "worked",   "play":   "played",  "watch":  "watched",
    "start": "started",  "finish": "finished","visit":  "visited",
    "love":  "loved",    "use":    "used",    "live":   "lived",
    "stop":  "stopped",  "plan":   "planned", "travel": "travelled",
    "study": "studied",  "try":    "tried",   "cry":    "cried",
}

IRREGULAR_VERBS = {
    "be":    "was/were", "have":  "had",    "go":    "went",
    "come":  "came",     "see":   "saw",    "get":   "got",
    "make":  "made",     "take":  "took",   "know":  "knew",
    "think": "thought",  "say":   "said",   "give":  "gave",
    "find":  "found",    "tell":  "told",   "buy":   "bought",
    "eat":   "ate",      "drink": "drank",  "sleep": "slept",
    "write": "wrote",    "read":  "read",   "meet":  "met",
    "drive": "drove",    "fly":   "flew",   "speak": "spoke",
    "run":   "ran",      "swim":  "swam",   "win":   "won",
    "lose":  "lost",     "break": "broke",  "feel":  "felt",
}

SPELLING_RULES = [
    ("Most verbs",             "+ ed",     "work → worked"),
    ("Silent -e at end",       "+ d only", "live → lived"),
    ("Short vowel + consonant","double + ed","stop → stopped"),
    ("Consonant + y",          "y → ied",  "study → studied"),
]

print("=" * 55)
print("  LESSON 09: Past Simple")
print("=" * 55)

print("\n📚 WHEN TO USE IT:")
print("-" * 55)
print("  • Completed action in the past:")
print("    I watched a film yesterday.")
print("  • Series of past actions:")
print("    She got up, had breakfast and left.")
print("  • Past habit (with 'used to' or time expressions):")
print("    We always went to the sea in summer.")

print("\n📚 REGULAR VERBS — spelling rules:")
print("-" * 55)
for rule, change, example in SPELLING_RULES:
    print(f"  {rule:<30} {change:<14} {example}")

print("\n📚 COMMON IRREGULAR VERBS (learn these!):")
print("-" * 55)
irr = list(IRREGULAR_VERBS.items())
for i in range(0, len(irr), 3):
    row = irr[i:i+3]
    print("  " + "   ".join(f"{base:<8} → {past:<9}" for base, past in row))

print("\n📚 NEGATIVES & QUESTIONS:")
print("-" * 55)
print("  (+)  I   worked.   She  went.    They  ate.")
print("  (−)  I   didn't work. She didn't go.  They didn't eat.")
print("  (?)  Did you work?   Did she go?    Did they eat?")
print()
print("  ⚠️  With DID/DIDN'T — main verb always in BASE form:")
print("  ✓ Did she GO?   (NE: Did she went?)")
print("  ✓ I didn't EAT. (NE: I didn't ate.)")

print("\n💬 EXAMPLE SENTENCES:")
print("-" * 55)
examples = [
    ("I went to London last summer.",         "Loni v létě jsem byl/a v Londýně."),
    ("She didn't come to the party.",         "Nepřišla na párty."),
    ("Did you see that film?",               "Viděl/a jsi ten film?"),
    ("We met at a coffee shop in 2019.",      "Poznali jsme se v kavárně v 2019."),
    ("He studied all night but failed.",      "Studoval celou noc, ale neuspěl."),
    ("They bought a new house last year.",    "Loni si koupili nový dům."),
]
for en, cz in examples:
    print(f"  {en}")
    print(f"    → {cz}\n")

print("\n🎯 QUIZ — give the past simple form:")
print("-" * 55)
all_verbs = {**{f"{v} (regular)": p for v, p in REGULAR_EXAMPLES.items()},
             **{f"{v} (irregular)": p for v, p in IRREGULAR_VERBS.items()}}
pairs = random.sample(list(IRREGULAR_VERBS.items()), 8)
score = 0
for base, past in pairs:
    ans = input(f"  {base}  →  ").strip().lower()
    if ans == past.lower():
        print("  ✓ Correct!\n")
        score += 1
    else:
        print(f"  ✗ Answer: {past}\n")
print(f"  Score: {score}/8")

# YOUR TASK:
# 1. Write a short paragraph (5–7 sentences) about what you did last weekend
# 2. Convert each sentence to a question (Did you ...?)
# 3. Learn the 50 most common irregular verbs — create flashcard pairs
