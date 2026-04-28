"""
LESSON 18: Conditionals
=========================
⭐⭐⭐ Level: B1 | Pre-Intermediate

Podmínkové věty — real, unreal a past conditions.
Topics: zero · first · second · third conditional · mixed
"""
import random

CONDITIONALS = {
    "Zero": {
        "structure": "If + present simple, present simple",
        "use":       "General truth / scientific fact",
        "example_en":"If you heat water to 100°C, it boils.",
        "example_cz":"Pokud zahřeješ vodu na 100°C, vaří se.",
    },
    "First": {
        "structure": "If + present simple, will + infinitive",
        "use":       "Real / likely future condition",
        "example_en":"If it rains, we will stay inside.",
        "example_cz":"Pokud bude pršet, zůstaneme uvnitř.",
    },
    "Second": {
        "structure": "If + past simple, would + infinitive",
        "use":       "Unreal / hypothetical present/future",
        "example_en":"If I had a million euros, I would travel the world.",
        "example_cz":"Kdybych měl/a milion eur, cestoval/a bych po světě.",
    },
    "Third": {
        "structure": "If + past perfect, would have + past participle",
        "use":       "Unreal past — imagining different outcome",
        "example_en":"If she had studied harder, she would have passed.",
        "example_cz":"Kdyby více studovala, udělala by zkoušku.",
    },
}

COMMON_MISTAKES = [
    ("✗ If I will go...",   "✓ If I go...     (1st conditional — no will in if-clause)"),
    ("✗ If I would have...", "✓ If I had...    (2nd conditional — no would in if-clause)"),
    ("✗ If she would've studied...", "✓ If she had studied...  (3rd conditional)"),
]

print("=" * 55)
print("  LESSON 18: Conditionals")
print("=" * 55)

for name, data in CONDITIONALS.items():
    print(f"\n📚 {name.upper()} CONDITIONAL:")
    print("-" * 55)
    print(f"  Structure: {data['structure']}")
    print(f"  Use:       {data['use']}")
    print(f"  Example:   {data['example_en']}")
    print(f"             → {data['example_cz']}")

print("\n📚 MORE EXAMPLES:")
print("-" * 55)
more = [
    ("1st", "If you leave now, you'll catch the train."),
    ("1st", "Unless it stops raining, we won't go out."),
    ("2nd", "If I were you, I would apologise."),
    ("2nd", "What would you do if you lost your job?"),
    ("3rd", "If they had left earlier, they wouldn't have missed it."),
    ("3rd", "I would have called you if I had known."),
]
for ctype, sentence in more:
    print(f"  [{ctype}]  {sentence}")

print("\n⚠️  COMMON MISTAKES:")
print("-" * 55)
for wrong, right in COMMON_MISTAKES:
    print(f"  {wrong}")
    print(f"  {right}\n")

print("\n📝 'UNLESS' = 'if...not':")
print("-" * 55)
print("  Unless you hurry, you'll miss the bus.")
print("  = If you don't hurry, you'll miss the bus.")

print("\n🎯 QUIZ — complete the conditional:")
print("-" * 55)
quiz = [
    ("If water ___ (freeze) below 0°C. (zero)", "freezes"),
    ("If I ___ (have) more time, I would learn Spanish. (2nd)", "had"),
    ("She would have called if she ___ (know) your number. (3rd)", "had known"),
    ("If you study hard, you ___ (pass) the exam. (1st)", "will pass"),
    ("If I ___ (be) you, I'd see a doctor. (2nd)", "were"),
    ("They ___ (not/arrive) late if they had taken a taxi. (3rd)", "wouldn't have arrived"),
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
# 1. Write 3 first conditional sentences about your near future
# 2. Write 3 second conditional sentences starting with 'If I were...'
# 3. Think of a moment you regret — write 2 third conditional sentences
#    about how things could have been different
