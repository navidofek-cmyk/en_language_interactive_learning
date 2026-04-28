"""
ARTICLE 03: Climate Change — The Facts
=========================================
⭐⭐⭐ Level: B1–B2 | Pre-Intermediate

Klimatická změna — fakta, dopady a řešení.
Topics: environment · passive voice · statistics · argument
"""

ARTICLE = """
CLIMATE CHANGE — THE FACTS

The Earth's average temperature has risen by approximately 1.2°C since the
industrial revolution. This may sound small, but it is having profound effects
on weather patterns, sea levels, and ecosystems across the planet. Scientists
agree that this warming is primarily caused by human activities — the burning
of fossil fuels, deforestation, and industrial agriculture.

The consequences are already visible. Extreme weather events — droughts,
floods, and heatwaves — are becoming more frequent and more intense. Arctic
ice is melting at an unprecedented rate, contributing to rising sea levels.
Low-lying island nations and coastal cities face the real prospect of being
partially submerged within this century.

In 2015, nearly 200 countries signed the Paris Agreement, committing to limit
global warming to 1.5°C above pre-industrial levels. Progress has been slow.
Global emissions are still rising, although the rate of increase has slowed.
Renewable energy — solar and wind in particular — has grown dramatically and
is now often cheaper than fossil fuels.

The debate is no longer about whether climate change is happening, but about
how fast we can act. The solutions are known: transition to clean energy,
protect forests, change agricultural practices, and reduce consumption. What
is lacking is not technology, but political will and public pressure.

The window for action is narrowing, but it has not yet closed.
"""

VOCABULARY = {
    "profound":          "hluboký, zásadní",
    "ecosystem":         "ekosystém",
    "primarily":         "především, hlavně",
    "unprecedented":     "bezprecedentní",
    "contribute to":     "přispívat k",
    "submerged":         "zaplavený, ponořený",
    "commit to":         "zavázat se k",
    "emissions":         "emise",
    "transition":        "přechod, transformace",
    "consumption":       "spotřeba",
    "political will":    "politická vůle",
    "narrow":            "zužovat se (okno možností)",
}

COMPREHENSION = [
    ("By how much has the Earth's temperature risen since the industrial revolution?",
     "Approximately 1.2°C."),
    ("Name three human activities that cause global warming.",
     "Burning fossil fuels, deforestation, industrial agriculture."),
    ("What was agreed in the Paris Agreement?",
     "To limit global warming to 1.5°C above pre-industrial levels."),
    ("What does the article say about renewable energy?",
     "It has grown dramatically and is now often cheaper than fossil fuels."),
    ("According to the article, what is lacking in the fight against climate change?",
     "Not technology, but political will and public pressure."),
]

LANGUAGE_FOCUS = [
    ("Passive voice in academic text:",
     "'This warming IS CAUSED BY human activities.'"),
    ("Hedging language:",
     "'Low-lying nations FACE THE REAL PROSPECT of being submerged.'"),
    ("Contrast:",
     "'The debate is no longer about whether..., BUT ABOUT how fast...'"),
    ("Strong adjective:",
     "'melting at an UNPRECEDENTED rate'"),
]

DISCUSSION = [
    "Do you think climate change is the most important issue of our time? Why / why not?",
    "What changes have you personally made (or are you willing to make) to reduce your impact?",
    "Why do you think governments have been slow to act on climate change?",
    "Is individual action enough, or does real change have to come from governments and companies?",
]

print("=" * 55)
print("  ARTICLE 03: Climate Change — The Facts")
print("=" * 55)
print(ARTICLE)

print("\n📚 VOCABULARY:")
print("-" * 55)
for en, cz in VOCABULARY.items():
    print(f"  {en:<22} {cz}")

print("\n🔍 LANGUAGE FOCUS:")
print("-" * 55)
for feature, example in LANGUAGE_FOCUS:
    print(f"  {feature}")
    print(f"    {example}\n")

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
# 1. Write a 5-sentence summary of the article using your own words
# 2. Choose ONE solution mentioned and argue WHY it is the most important
# 3. Write a letter to a government minister urging immediate action on climate change
