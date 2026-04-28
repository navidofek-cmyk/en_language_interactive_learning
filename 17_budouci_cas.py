"""
LESSON 17: Future Tenses
==========================
⭐⭐ Level: A2–B1 | Elementary

Budoucí čas — will, going to, present continuous.
Topics: will · going to · present continuous for future · future time expressions
"""
import random

USES = {
    "will": [
        ("Spontaneous decision",    "I'll have the soup, please.",          "Dám si polévku, prosím."),
        ("Prediction (opinion)",    "I think it will rain tomorrow.",        "Myslím, že zítra bude pršet."),
        ("Promise / offer",         "I'll help you move on Saturday.",       "V sobotu ti pomůžu se stěhováním."),
        ("Fact about future",       "The meeting will start at 10.",         "Schůzka začne v 10."),
    ],
    "going to": [
        ("Plan / intention",        "I'm going to study medicine.",          "Chystám se studovat medicínu."),
        ("Prediction with evidence","Look at those clouds — it's going to rain.", "Podívej na ty mraky — bude pršet."),
        ("Decision already made",   "We're going to buy a new car.",         "Chystáme se koupit nové auto."),
    ],
    "present continuous": [
        ("Arranged future event",   "I'm meeting Anna at 6 tomorrow.",      "Zítra v 6 se setkávám s Annou."),
        ("Fixed appointment",       "She's flying to Paris on Friday.",      "V pátek letí do Paříže."),
    ],
}

FUTURE_EXPRESSIONS = {
    "tomorrow":           "zítra",
    "next week/month":    "příští týden/měsíc",
    "in two days":        "za dva dny",
    "soon":               "brzy",
    "in the future":      "v budoucnosti",
    "by Friday":          "do pátku",
    "this evening":       "dnes večer",
    "at the weekend":     "o víkendu",
}

print("=" * 55)
print("  LESSON 17: Future Tenses")
print("=" * 55)

for tense, examples in USES.items():
    print(f"\n📚 {tense.upper()}:")
    print("-" * 55)
    for use, en, cz in examples:
        print(f"  [{use}]")
        print(f"  {en}")
        print(f"    → {cz}\n")

print("\n📝 QUICK GUIDE:")
print("-" * 55)
print("  Unplanned, spontaneous  →  WILL")
print("  Planned intention       →  GOING TO")
print("  Fixed arrangement       →  PRESENT CONTINUOUS")
print()
print("  (Phone rings) 'I'll get it!'              → will (spontaneous)")
print("  'I'm going to call the dentist tomorrow.' → going to (plan)")
print("  'I'm seeing the dentist at 3.'            → pres. cont. (booked)")

print("\n📚 FUTURE TIME EXPRESSIONS:")
print("-" * 55)
for en, cz in FUTURE_EXPRESSIONS.items():
    print(f"  {en:<22} {cz}")

print("\n🎯 QUIZ — will / going to / present continuous?")
print("-" * 55)
quiz = [
    ("You look cold. I ___ get you a blanket. (spontaneous offer)", "will / 'll"),
    ("She ___ start a new job next Monday. (arranged appointment)", "is starting"),
    ("They ___ travel around Asia next year. (plan already decided)", "are going to"),
    ("I think robots ___ replace many jobs in the future. (prediction)", "will"),
    ("'The phone is ringing!' — 'I ___ answer it!' (spontaneous)", "will / 'll"),
]
score = 0
for sentence, answer in quiz:
    print(f"  {sentence}")
    ans = input("  → ").strip()
    if ans.lower() == answer.lower():
        print("  ✓ Correct!\n"); score += 1
    else:
        print(f"  ✗ Answer: {answer}\n")
print(f"  Score: {score}/5")

# YOUR TASK:
# 1. Write your plans for next weekend using 'going to' (5 sentences)
# 2. Write 3 predictions about the world in 2050 using 'will'
# 3. Write your diary for tomorrow using present continuous
#    (at least 4 fixed arrangements)
