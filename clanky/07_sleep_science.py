"""
ARTICLE 07: The Science of Sleep
=====================================
⭐⭐⭐ Level: B1–B2 | Pre-Intermediate

Věda o spánku — proč je tak důležitý a co se děje, když ho máme málo.
Topics: science · health · passive voice · modal verbs · data
"""

ARTICLE = """
THE SCIENCE OF SLEEP

We spend approximately one third of our lives asleep. Yet despite this,
many people treat sleep as a luxury rather than a necessity. Research
suggests that this attitude could be seriously damaging our health.

During sleep, the brain does not simply switch off. It performs a series
of critical maintenance tasks. Memories are consolidated and transferred
from short-term to long-term storage. The body repairs tissues, regulates
hormones, and strengthens the immune system. The brain also removes
toxic waste products — including proteins associated with Alzheimer's disease —
through a recently discovered system called the glymphatic network.

The consequences of poor sleep are well-documented. A chronic lack of sleep
has been linked to obesity, type 2 diabetes, cardiovascular disease, and
depression. Studies show that sleeping fewer than six hours a night increases
the risk of having a stroke by four times. Concentration, memory, and
decision-making are all impaired after even one night of insufficient sleep.

Yet in many cultures, sleep deprivation is worn as a badge of honour.
'I only sleep four hours' is said with pride, as if suffering were a sign
of dedication. Sleep scientists argue that this attitude is not only
misguided but actively harmful.

Adults need between seven and nine hours of sleep per night. Teenagers need
even more. Creating good sleep habits — a consistent schedule, a dark and
cool room, limiting screens before bed — can make a dramatic difference
to physical and mental health.
"""

VOCABULARY = {
    "consolidate":     "upevnit, konsolidovat",
    "regulate":        "regulovat",
    "immune system":   "imunitní systém",
    "toxic":           "toxický",
    "associated with": "spojený s",
    "glymphatic":      "glymfatický (systém čistění mozku)",
    "chronic":         "chronický",
    "cardiovascular":  "kardiovaskulární (srdeční-cévní)",
    "impaired":        "zhoršený, poškozený",
    "deprivation":     "deprivace, nedostatek",
    "badge of honour": "odznak cti",
    "misguided":       "mylný, špatně nasměrovaný",
    "consistent":      "pravidelný, konzistentní",
}

COMPREHENSION = [
    ("What does the brain do during sleep?",
     "Consolidates memories, repairs tissues, regulates hormones, strengthens immune system, removes toxic waste."),
    ("What is the glymphatic network?",
     "A recently discovered system that removes toxic waste products from the brain."),
    ("What health risks are associated with sleeping fewer than 6 hours?",
     "Obesity, diabetes, cardiovascular disease, depression, increased stroke risk."),
    ("How does the article describe the cultural attitude to sleep deprivation?",
     "It is worn as a badge of honour — sleeping little is seen as a sign of dedication."),
    ("How many hours of sleep do adults need?",
     "Between 7 and 9 hours per night."),
]

LANGUAGE_FOCUS = [
    ("Passive for scientific facts:",
     "'Memories ARE CONSOLIDATED during sleep.'"),
    ("Linking cause and effect:",
     "'Chronic lack of sleep HAS BEEN LINKED TO obesity.'"),
    ("Irony/criticism:",
     "'sleep deprivation is worn as a BADGE OF HONOUR'"),
    ("Hedging with modal verbs:",
     "'this attitude COULD BE seriously damaging our health'"),
]

DISCUSSION = [
    "How many hours do you typically sleep? Do you feel it's enough?",
    "Do you think society places too much value on being 'busy' and too little on rest?",
    "What habits help or hinder your sleep?",
    "Have you ever experienced significant sleep deprivation? How did it affect you?",
]

print("=" * 55)
print("  ARTICLE 07: The Science of Sleep")
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
# 1. Write a 100-word summary of the article's main points
# 2. Write a list of 5 pieces of advice for better sleep using modal verbs
# 3. Research: What is REM sleep and why is it important? Write 3 sentences.
