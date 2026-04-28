"""
LESSON 01: Greetings & Introductions
======================================
⭐ Level: A1 | Beginner

Základní anglické pozdravy a věty pro první seznámení.
Topics: greetings · introductions · courtesy phrases
"""
import random

VOCABULARY = {
    "Hello / Hi":          "Ahoj / Dobrý den",
    "Good morning":        "Dobré ráno",
    "Good afternoon":      "Dobré odpoledne",
    "Good evening":        "Dobrý večer",
    "Goodbye / Bye":       "Nashledanou / Čau",
    "See you later":       "Uvidíme se",
    "How are you?":        "Jak se máš?",
    "I'm fine, thank you": "Jsem v pořádku, díky",
    "My name is ...":      "Jmenuji se ...",
    "What's your name?":   "Jak se jmenuješ?",
    "Nice to meet you":    "Těší mě",
    "Where are you from?": "Odkud jsi?",
    "I'm from ...":        "Jsem z ...",
    "Please":              "Prosím",
    "Thank you":           "Děkuji",
    "You're welcome":      "Není zač",
    "Excuse me":           "Promiňte / S dovolením",
    "Sorry":               "Omlouvám se",
}

print("=" * 55)
print("  LESSON 01: Greetings & Introductions")
print("=" * 55)

print("\n📚 VOCABULARY:")
print("-" * 55)
for en, cz in VOCABULARY.items():
    print(f"  {en:<32} {cz}")

print("\n💬 DIALOGUE:")
print("-" * 55)
dialogue = [
    ("A", "Good morning! My name is Jan. What's your name?"),
    ("B", "Hi Jan! I'm Eva. Nice to meet you."),
    ("A", "Nice to meet you too! Where are you from?"),
    ("B", "I'm from Prague. And you?"),
    ("A", "I'm from Brno. Goodbye, Eva!"),
    ("B", "Bye Jan! See you later!"),
]
for speaker, line in dialogue:
    print(f"  {speaker}: {line}")

print("\n📝 GRAMMAR NOTE:")
print("-" * 55)
print("  My name IS Jan.             (správně — ne: My name ARE)")
print("  I AM from Czech Republic.   (správně — ne: I IS)")
print("  Nice to meet YOU.           (správně — ne: nice to meet your)")

print("\n🎯 QUIZ — přelož do angličtiny:")
print("-" * 55)
pairs = random.sample(list(VOCABULARY.items()), min(5, len(VOCABULARY)))
score = 0
for en, cz in pairs:
    ans = input(f"  {cz}  →  ").strip()
    if ans.lower() == en.lower():
        print("  ✓ Correct!\n")
        score += 1
    else:
        print(f"  ✗ Answer: {en}\n")

rating = "🏆 Perfect!" if score == len(pairs) else "👍 Good!" if score >= len(pairs) // 2 else "📖 Keep practising!"
print(f"\n  Score: {score}/{len(pairs)}  {rating}")

# YOUR TASK:
# 1. Add 5 more courtesy phrases to VOCABULARY
# 2. Write a function introduce(name, city) that prints a full
#    self-introduction in English (3–4 sentences)
# 3. Create an interactive conversation: ask the user their name
#    and hometown, then respond naturally in English
