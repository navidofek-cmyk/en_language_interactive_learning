"""
LESSON 36: Wish & If Only
===========================
⭐⭐⭐ Level: B1 | Pre-Intermediate

Výrazy přání a lítosti — wish, if only, would rather, it's time.
Topics: wish + past · wish + would · wish + past perfect · if only · regret
"""
import random

STRUCTURES = {
    "wish + past simple": {
        "use":   "Wish for a different present/future situation",
        "examples": [
            ("I wish I had more time.",      "Přál/a bych si mít více času. (teď nemám)"),
            ("She wishes she lived closer.", "Přeje si bydlet blíž. (nežije blíž)"),
            ("I wish I could drive.",        "Přál/a bych si umět řídit. (neumím)"),
            ("Don't you wish it was Friday?","Nepřeješ si, aby byl pátek?"),
        ],
    },
    "wish + would": {
        "use":   "Wish for a change in someone's behaviour (often complaint)",
        "examples": [
            ("I wish you would listen!",          "Přál/a bych si, abys poslouchal/a!"),
            ("She wishes he would stop smoking.", "Přeje si, aby přestal kouřit."),
            ("I wish it would stop raining.",     "Přál/a bych si, aby přestalo pršet."),
        ],
        "note": "Cannot use 'I wish I would' — use wish + past simple for yourself",
    },
    "wish + past perfect": {
        "use":   "Regret about the past",
        "examples": [
            ("I wish I had studied harder.",        "Přál/a bych si, že jsem více studoval/a."),
            ("She wishes she hadn't said that.",    "Přeje si, aby to nebyla řekla."),
            ("I wish I had taken that job.",        "Přál/a bych si, abych tu práci vzal/a."),
            ("If only I hadn't eaten so much!",     "Kdyby jen jsem tolik nejedl/a!"),
        ],
    },
    "if only": {
        "use":   "Stronger form of wish — more emotional",
        "examples": [
            ("If only I had more money!",       "Kéž bych měl/a více peněz!"),
            ("If only she would call!",         "Kéž by zavolala!"),
            ("If only I hadn't said that.",     "Kéž bych to nebyl/a řekl/a."),
        ],
    },
    "would rather": {
        "use":   "Preference — would prefer to",
        "examples": [
            ("I'd rather stay home tonight.",    "Raději bych zůstal/a doma dnes večer."),
            ("She'd rather have tea than coffee.","Raději by si dala čaj než kávu."),
            ("I'd rather you didn't tell anyone.","Raději bych, abys nikomu neříkal/a."),
        ],
    },
    "it's time": {
        "use":   "Something should happen (possibly overdue)",
        "examples": [
            ("It's time to leave.",              "Je čas odejít."),
            ("It's time we left.",               "Je čas, abychom odešli. (+ past = overdue)"),
            ("It's high time you apologised.",   "Nejvyšší čas, abys se omluvil/a."),
        ],
    },
}

print("=" * 55)
print("  LESSON 36: Wish & If Only")
print("=" * 55)

for structure, data in STRUCTURES.items():
    print(f"\n📚 {structure.upper()}:")
    print("-" * 55)
    print(f"  Use: {data['use']}")
    if "note" in data:
        print(f"  ⚠️  {data['note']}")
    print()
    for en, cz in data["examples"]:
        print(f"  {en}")
        print(f"    → {cz}\n")

print("\n📝 WISH vs IF ONLY:")
print("-" * 55)
print("  Same grammar — 'if only' is more emotional/dramatic:")
print("  'I wish I had more time.'   (neutral)")
print("  'If only I had more time!'  (stronger feeling)")

print("\n🎯 QUIZ — complete with wish/if only structure:")
print("-" * 55)
quiz = [
    ("I can't swim. I wish I ___ (can) swim.", "could"),
    ("I ate too much. I wish I ___ (not eat) so much.", "hadn't eaten"),
    ("He's always late! I wish he ___ (be) on time.", "would be"),
    ("She doesn't live near us. If only she ___ (live) closer.", "lived"),
    ("I didn't take the job. I wish I ___ (take) it.", "had taken"),
    ("It's time you ___ (start) saving money. (overdue)", "started"),
]
score = 0
for sentence, answer in quiz:
    print(f"  {sentence}")
    ans = input("  → ").strip()
    if ans.lower() == answer.lower():
        print("  ✓ Correct!\n"); score += 1
    else:
        print(f"  ✗ Answer: {answer}\n")
print(f"  Score: {score}/6")

# YOUR TASK:
# 1. Write 5 wishes about your present life (wish + past simple)
# 2. Write 3 regrets about your past (wish/if only + past perfect)
# 3. Write 3 complaints about someone else's behaviour (wish + would)
