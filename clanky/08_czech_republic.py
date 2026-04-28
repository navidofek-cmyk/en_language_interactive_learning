"""
ARTICLE 08: The Czech Republic — An Introduction
==================================================
⭐⭐ Level: A2–B1 | Elementary

Krátký anglický text o České republice — pro procvičení čtení.
Topics: geography · history · culture · describing your country
"""

ARTICLE = """
THE CZECH REPUBLIC — AN INTRODUCTION

The Czech Republic, also known as Czechia, is a landlocked country in the
heart of Central Europe. It borders Germany to the west, Austria to the south,
Slovakia to the east, and Poland to the north. The capital and largest city
is Prague, which has a population of approximately 1.4 million people.

The country has a rich and complex history. For much of the 20th century,
it was part of Czechoslovakia — a state that was created in 1918 after the
collapse of the Austro-Hungarian Empire. After World War Two, Czechoslovakia
became a communist state under Soviet influence. In 1989, the Velvet Revolution
brought peaceful change, and democracy was restored. In 1993, Czechoslovakia
peacefully split into two independent countries: the Czech Republic and Slovakia.

Culturally, the Czech Republic is known for its medieval architecture, its
world-class beer, and its classical music tradition. Prague's historic centre
is a UNESCO World Heritage Site and attracts millions of tourists each year.
The country has produced notable writers, including Franz Kafka and Milan Kundera,
and composers such as Antonín Dvořák and Bedřich Smetana.

The Czech economy is one of the most developed in Central Europe. The country
is a member of the European Union and NATO, though it still uses the Czech
koruna rather than the euro. The standard of living is high, and unemployment
has historically been among the lowest in the EU.

If you visit, don't miss the castle district (Hradčany), the Old Town Square,
and the Charles Bridge in Prague — and definitely try the local food and beer.
"""

VOCABULARY = {
    "landlocked":     "vnitrozemský (bez přístupu k moři)",
    "border":         "sousedit s, hraničit s",
    "collapse":       "rozpad, zhroucení",
    "Velvet Revolution": "Sametová revoluce",
    "democracy":      "demokracie",
    "medieval":       "středověký",
    "UNESCO World Heritage Site": "lokalita světového dědictví UNESCO",
    "notable":        "pozoruhodný, významný",
    "composer":       "skladatel",
    "koruna":         "koruna (měna)",
    "unemployment":   "nezaměstnanost",
    "standard of living": "životní úroveň",
}

COMPREHENSION = [
    ("Which countries border the Czech Republic?",
     "Germany (west), Austria (south), Slovakia (east), Poland (north)."),
    ("What was Czechoslovakia, and when was it created?",
     "A country created in 1918 after the collapse of the Austro-Hungarian Empire."),
    ("What happened in 1989?",
     "The Velvet Revolution — peaceful change and restoration of democracy."),
    ("Name two famous Czech writers mentioned in the article.",
     "Franz Kafka and Milan Kundera."),
    ("Does the Czech Republic use the euro?",
     "No — it uses the Czech koruna."),
]

USEFUL_PHRASES = {
    "The country is known for...":    "Země je známá pro...",
    "It is located in...":            "Nachází se v...",
    "It borders...":                  "Hraničí s...",
    "The population is...":           "Počet obyvatel je...",
    "Historically,...":               "Historicky,...",
    "The capital city is...":         "Hlavní město je...",
    "The economy is...":              "Ekonomika je...",
    "If you visit, don't miss...":    "Pokud přijedete, nevynechejte...",
}

DISCUSSION = [
    "What do you think are the most interesting things about the Czech Republic?",
    "What would you tell a foreign visitor — what should they absolutely see or do?",
    "How has the Czech Republic changed over the last 30 years?",
    "What do Czech people value most in life, in your opinion?",
]

print("=" * 55)
print("  ARTICLE 08: The Czech Republic — An Introduction")
print("=" * 55)
print(ARTICLE)

print("\n📚 VOCABULARY:")
print("-" * 55)
for en, cz in VOCABULARY.items():
    print(f"  {en:<30} {cz}")

print("\n📚 USEFUL PHRASES FOR DESCRIBING A COUNTRY:")
print("-" * 55)
for en, cz in USEFUL_PHRASES.items():
    print(f"  {en:<38} {cz}")

print("\n🎯 COMPREHENSION:")
print("-" * 55)
for i, (q, a) in enumerate(COMPREHENSION, 1):
    print(f"\n  Q{i}: {q}")
    ans = input("  → ").strip()
    print(f"  ✓ Model: {a}")

print("\n💬 DISCUSSION:")
print("-" * 55)
for i, q in enumerate(DISCUSSION, 1):
    print(f"  {i}. {q}")
    ans = input("  → ").strip()
    print()

# YOUR TASK:
# 1. Write a short introduction to your city or town in English (100 words)
#    Use the article as a model.
# 2. Write a short tourist guide entry for one Czech place you love (80 words)
# 3. Explain the Velvet Revolution to a non-Czech person in 5 sentences
