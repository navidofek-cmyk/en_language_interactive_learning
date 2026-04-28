"""
LESSON 20: Comparatives & Superlatives
========================================
⭐⭐ Level: A2–B1 | Elementary

Stupňování přídavných jmen a příslovcí.
Topics: -er/-est · more/most · irregular · as...as · too/enough
"""
import random

REGULAR = {
    "short":   ("shorter",      "the shortest"),
    "tall":    ("taller",       "the tallest"),
    "fast":    ("faster",       "the fastest"),
    "cheap":   ("cheaper",      "the cheapest"),
    "large":   ("larger",       "the largest"),
    "nice":    ("nicer",        "the nicest"),
    "big":     ("bigger",       "the biggest"),
    "hot":     ("hotter",       "the hottest"),
    "happy":   ("happier",      "the happiest"),
    "heavy":   ("heavier",      "the heaviest"),
}

LONG_ADJECTIVES = {
    "expensive":  ("more expensive",  "the most expensive"),
    "interesting":("more interesting","the most interesting"),
    "beautiful":  ("more beautiful",  "the most beautiful"),
    "comfortable":("more comfortable","the most comfortable"),
    "difficult":  ("more difficult",  "the most difficult"),
    "important":  ("more important",  "the most important"),
}

IRREGULAR = {
    "good":  ("better",  "the best"),
    "bad":   ("worse",   "the worst"),
    "far":   ("further", "the furthest"),
    "little":("less",    "the least"),
    "many/much":("more", "the most"),
}

SPELLING_RULES = [
    ("1 syllable",              "add -er/-est",     "tall → taller/tallest"),
    ("1 syll., silent -e",      "add -r/-st",       "large → larger/largest"),
    ("1 syll., CVC pattern",    "double + -er/-est","big → bigger/biggest"),
    ("2+ syllables",            "more/most",        "interesting → more interesting"),
    ("2 syllables ending -y",   "y→i + -er/-est",   "happy → happier/happiest"),
]

print("=" * 55)
print("  LESSON 20: Comparatives & Superlatives")
print("=" * 55)

print("\n📚 REGULAR SHORT ADJECTIVES:")
print("-" * 55)
print(f"  {'Adjective':<12} {'Comparative':<16} {'Superlative'}")
for adj, (comp, sup) in REGULAR.items():
    print(f"  {adj:<12} {comp:<16} {sup}")

print("\n📚 LONG ADJECTIVES (more/most):")
print("-" * 55)
for adj, (comp, sup) in LONG_ADJECTIVES.items():
    print(f"  {adj:<14} {comp:<22} {sup}")

print("\n📚 IRREGULAR (learn these!):")
print("-" * 55)
for adj, (comp, sup) in IRREGULAR.items():
    print(f"  {adj:<12} {comp:<12} {sup}")

print("\n📚 SPELLING RULES:")
print("-" * 55)
for rule, change, example in SPELLING_RULES:
    print(f"  {rule:<32} {change:<18} {example}")

print("\n📝 KEY STRUCTURES:")
print("-" * 55)
print("  Comparative + THAN:")
print("    Prague is bigger THAN Brno.")
print("    This exam was more difficult THAN the last one.")
print()
print("  AS...AS (stejně ... jako):")
print("    He is as tall as his father.")
print("    It's not as expensive as I thought.")
print()
print("  TOO + adjective (příliš):")
print("    This bag is too heavy. (= víc než chci)")
print()
print("  Adjective + ENOUGH (dostatečně):")
print("    She is old enough to drive. (= dostatečně stará)")
print("    It's not warm enough to swim.")

print("\n💬 EXAMPLES:")
print("-" * 55)
examples = [
    "The Nile is the longest river in the world.",
    "Electric cars are more expensive than petrol cars.",
    "My new flat is better than the old one.",
    "She speaks English more fluently than her brother.",
    "Is the train faster than the bus?",
    "This is the most interesting book I've ever read.",
]
for ex in examples:
    print(f"  {ex}")

print("\n🎯 QUIZ — give the comparative and superlative:")
print("-" * 55)
all_adj = {**REGULAR, **LONG_ADJECTIVES, **IRREGULAR}
pairs = random.sample(list(all_adj.items()), 6)
score = 0
for adj, (comp, sup) in pairs:
    ans = input(f"  {adj} → comparative: ").strip()
    ans2 = input(f"  {adj} → superlative: ").strip()
    ok = (ans.lower() == comp.lower()) and (ans2.lower() == sup.lower())
    if ok:
        print("  ✓ Correct!\n"); score += 1
    else:
        print(f"  ✗ Answer: {comp} / {sup}\n")
print(f"  Score: {score}/6")

# YOUR TASK:
# 1. Compare three cities you know using comparatives and superlatives
# 2. Write 5 sentences using 'as...as' and 5 using 'not as...as'
# 3. Write a short product review comparing two items you own
