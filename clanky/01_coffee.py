"""
ARTICLE 01: The History of Coffee
=====================================
⭐⭐ Level: A2–B1 | Elementary

Přečti si článek, nauč se slovíčka a odpověz na otázky.
Topics: history · food & drink · past tenses
"""
import random

ARTICLE = """
THE HISTORY OF COFFEE

Coffee is one of the most popular drinks in the world, but where did it
come from? The story begins in Ethiopia, around the year 850 AD. According
to legend, a goat herder named Kaldi noticed that his goats became very
energetic after eating berries from a certain tree. He tried the berries
himself and felt the same effect. Monks at a nearby monastery used the
berries to make a drink that helped them stay awake during long evening prayers.

By the 15th century, coffee had spread to the Arabian Peninsula. People began
growing coffee plants and trading the beans. Coffee houses, known as qahveh
khaneh, opened across the Middle East. They became important social places
where people could meet, talk, and play chess.

Coffee arrived in Europe in the 17th century and quickly became very popular.
In 1652, the first coffee house in England opened in Oxford. By 1675, there
were more than 3,000 coffee houses in England. Some of today's most important
institutions began in coffee houses — Lloyd's of London, the famous insurance
company, started as a coffee house.

Today, over 2.25 billion cups of coffee are consumed every day worldwide.
Brazil is the largest producer, followed by Vietnam and Colombia. Coffee
remains not just a drink, but a global cultural phenomenon.
"""

VOCABULARY = {
    "legend":        "legenda, pověst",
    "goat herder":   "pastýř koz",
    "energetic":     "energický",
    "monastery":     "klášter",
    "prayer":        "modlitba",
    "Arabian Peninsula": "Arabský poloostrov",
    "trade":         "obchodovat",
    "qahveh khaneh": "kavárna (arabsky)",
    "institution":   "instituce",
    "phenomenon":    "jev, fenomén",
    "consume":       "spotřebovat, konzumovat",
    "producer":      "producent, výrobce",
}

COMPREHENSION = [
    ("Where did coffee originally come from?",
     "Ethiopia (East Africa)"),
    ("What did Kaldi notice about his goats?",
     "They became very energetic after eating certain berries."),
    ("What were qahveh khaneh?",
     "Coffee houses / social places in the Middle East."),
    ("When did the first English coffee house open?",
     "1652 (in Oxford)."),
    ("How many cups of coffee are consumed worldwide every day?",
     "Over 2.25 billion."),
]

DISCUSSION = [
    "Do you drink coffee? How much, and when?",
    "Why do you think coffee became so popular worldwide?",
    "What is the 'coffee culture' like in your country?",
    "Do you think coffee has a positive or negative effect on people?",
]

print("=" * 55)
print("  ARTICLE 01: The History of Coffee")
print("=" * 55)
print(ARTICLE)

print("\n📚 VOCABULARY:")
print("-" * 55)
for en, cz in VOCABULARY.items():
    print(f"  {en:<24} {cz}")

print("\n🎯 COMPREHENSION QUESTIONS:")
print("-" * 55)
score = 0
for i, (question, answer) in enumerate(COMPREHENSION, 1):
    print(f"\n  Q{i}: {question}")
    ans = input("  Your answer: ").strip()
    print(f"  ✓ Model answer: {answer}")
    score += 1

print("\n💬 DISCUSSION QUESTIONS:")
print("-" * 55)
for i, q in enumerate(DISCUSSION, 1):
    print(f"  {i}. {q}")
    ans = input("  → ").strip()
    print()

print("\n  ✓ Well done! Try to answer without looking at the article next time.")

# YOUR TASK:
# 1. Summarise the article in 3 sentences (without looking)
# 2. Write a short paragraph about the history of a food/drink from your country
# 3. Research: What is the difference between Arabica and Robusta coffee?
