"""
LESSON 48: Mixed Conditionals & Advanced Conditionals
=======================================================
⭐⭐⭐⭐ Level: B2–C1 | Upper-Intermediate

Smíšené podmínkové věty a pokročilé kondicionální struktury.
Topics: mixed type 2/3 · unless · providing/provided · as long as · but for
"""
import random

MIXED_CONDITIONALS = {
    "Past → Present (most common)": {
        "structure": "If + past perfect, would + infinitive",
        "meaning":   "Past condition → present result",
        "examples": [
            ("If I had studied medicine, I would be a doctor now.",
             "Kdybych studoval/a medicínu, byl/a bych teď doktor/ka."),
            ("If she hadn't emigrated, she would still be living here.",
             "Kdyby neemigrovala, stále by tu žila."),
            ("If we had invested in Bitcoin, we would be rich now.",
             "Kdybychom investovali do Bitcoinu, byli bychom teď bohatí."),
        ],
    },
    "Present → Past (less common)": {
        "structure": "If + past simple, would have + past participle",
        "meaning":   "Present state → past result",
        "examples": [
            ("If I were braver, I would have applied for that job.",
             "Kdybych byl/a odvážnější, přihlásil/a bych se na tu práci."),
            ("If he weren't so stubborn, he would have accepted help.",
             "Kdyby nebyl tak tvrdohlavý, přijal by pomoc."),
        ],
    },
}

OTHER_CONDITIONALS = [
    ("unless",
     "= if...not (only if this condition is NOT met)",
     "Unless you hurry, you'll miss the train.",
     "= If you don't hurry, you'll miss the train."),
    ("provided / providing (that)",
     "= only if (stronger condition than 'if')",
     "You can borrow my car, provided you drive carefully.",
     "Můžeš si půjčit mé auto, pokud budeš opatrně řídit."),
    ("as long as",
     "= only if / on the condition that",
     "I'll help you, as long as you're honest with me.",
     "Pomůžu ti, pokud budeš ke mně upřímný/á."),
    ("on condition that",
     "= formal version of 'as long as'",
     "They agreed on condition that prices weren't raised.",
     "Souhlasili za podmínky, že ceny nebudou zvýšeny."),
    ("but for / were it not for",
     "= if it hadn't been for / without",
     "But for your help, I would have failed.",
     "Nebýt vaší pomoci, byl/a bych selhal/a."),
    ("supposing / suppose",
     "= what if / imagine that",
     "Supposing you won the lottery — what would you do?",
     "Představ si, že vyhraješ v loterii — co bys dělal/a?"),
    ("even if",
     "= the condition doesn't change the result",
     "Even if it rains, we'll go camping.",
     "I kdyby pršelo, půjdeme na kempování."),
]

print("=" * 55)
print("  LESSON 48: Mixed Conditionals & Advanced Conditionals")
print("=" * 55)

for label, data in MIXED_CONDITIONALS.items():
    print(f"\n📚 MIXED CONDITIONAL — {label}:")
    print("-" * 55)
    print(f"  Structure: {data['structure']}")
    print(f"  Meaning:   {data['meaning']}\n")
    for en, cz in data["examples"]:
        print(f"  {en}")
        print(f"    → {cz}\n")

print("\n📝 COMPARE — PURE vs MIXED:")
print("-" * 55)
print("  Pure 3rd:  If I had studied, I would HAVE PASSED. (past→past)")
print("  Mixed:     If I had studied, I WOULD BE a doctor. (past→present)\n")
print("  Pure 2nd:  If I were rich, I WOULD BUY a yacht. (present→present)")
print("  Mixed:     If I were braver, I WOULD HAVE APPLIED. (present→past)")

print("\n📚 OTHER CONDITIONAL STRUCTURES:")
print("-" * 55)
for word, meaning, en, cz in OTHER_CONDITIONALS:
    print(f"\n  [{word}]  {meaning}")
    print(f"  {en}")
    print(f"    → {cz}")

print("\n🎯 QUIZ — complete the mixed conditional:")
print("-" * 55)
quiz = [
    ("If she ___ (study) harder, she would have a degree now.", "had studied"),
    ("If I ___ (be) taller, I would have become a basketball player.", "were"),
    ("___ it not for the rain, we would have had a great day.", "Were / But for"),
    ("I ___ (help) you yesterday if I had known you needed it.", "would have helped"),
    ("You can stay, ___ you behave yourself. (condition)", "as long as / provided"),
]
score = 0
for sentence, answer in quiz:
    print(f"  {sentence}")
    ans = input("  → ").strip()
    if any(a.strip().lower() in ans.lower() for a in answer.split("/")):
        print("  ✓ Correct!\n"); score += 1
    else:
        print(f"  ✗ Answer: {answer}\n")
print(f"  Score: {score}/5")

# YOUR TASK:
# 1. Write 3 mixed conditionals about your own life:
#    "If I had/hadn't..., I would/wouldn't be... now."
# 2. Complete these with your own ideas:
#    "But for _____, I would never have _____."
#    "Provided that _____, I would _____ next year."
# 3. Write a paragraph about a turning point in your life using mixed conditionals
