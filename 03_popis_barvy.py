"""
LESSON 03: Colours, Shapes & Descriptions
==========================================
⭐ Level: A1 | Beginner

Barvy, tvary a jak popsat věci v angličtině.
Topics: colours · shapes · adjectives · word order
"""
import random

COLOURS = {
    "red":    "červená",  "blue":   "modrá",   "green":  "zelená",
    "yellow": "žlutá",   "orange": "oranžová", "purple": "fialová",
    "pink":   "růžová",  "brown":  "hnědá",   "black":  "černá",
    "white":  "bílá",    "grey":   "šedá",    "gold":   "zlatá",
    "silver": "stříbrná","dark blue":"tmavě modrá","light green":"světle zelená",
}

SHAPES = {
    "circle":    "kruh",     "square":   "čtverec",
    "rectangle": "obdélník", "triangle": "trojúhelník",
    "oval":      "ovál",     "star":     "hvězda",
    "heart":     "srdce",    "cube":     "kostka",
    "sphere":    "koule",    "cylinder": "válec",
}

SIZE_ADJECTIVES = {
    "big / large": "velký",    "small / little": "malý",
    "tall":        "vysoký",   "short":          "krátký / nízký",
    "long":        "dlouhý",   "wide":           "široký",
    "narrow":      "úzký",     "thick":          "tlustý",
    "thin":        "tenký",    "heavy":          "těžký",
    "light":       "lehký",    "round":          "kulatý",
    "flat":        "plochý",   "deep":           "hluboký",
}

print("=" * 55)
print("  LESSON 03: Colours, Shapes & Descriptions")
print("=" * 55)

print("\n📚 COLOURS:")
print("-" * 55)
for en, cz in COLOURS.items():
    print(f"  {en:<20} {cz}")

print("\n📚 SHAPES:")
print("-" * 55)
for en, cz in SHAPES.items():
    print(f"  {en:<20} {cz}")

print("\n📚 SIZE & DESCRIPTION:")
print("-" * 55)
for en, cz in SIZE_ADJECTIVES.items():
    print(f"  {en:<22} {cz}")

print("\n📝 WORD ORDER — adjectives BEFORE noun:")
print("-" * 55)
print("  a RED car          (červené auto)")
print("  a BIG house        (velký dům)")
print("  a SMALL black cat  (malá černá kočka)")
print("  a TALL thin man    (vysoký hubený muž)")
print()
print("  ⚠️  Czech: 'červené AUTO' | English: 'RED car'")
print("  Adjective NEVER changes: a red car / red cars (not reds cars)")

print("\n💬 EXAMPLES:")
print("-" * 55)
print("  The sky is blue and the grass is green.")
print("  She has long brown hair and big blue eyes.")
print("  I live in a small white house with a red door.")

print("\n🎯 QUIZ — přelož do angličtiny:")
print("-" * 55)
all_vocab = {**COLOURS, **SHAPES, **SIZE_ADJECTIVES}
pairs = random.sample(list(all_vocab.items()), 6)
score = 0
for en, cz in pairs:
    ans = input(f"  {cz}  →  ").strip()
    if ans.lower() == en.lower():
        print("  ✓ Correct!\n")
        score += 1
    else:
        print(f"  ✗ Answer: {en}\n")
print(f"  Score: {score}/6")

print("\n🎯 DESCRIBE IT — popiš předmět:")
print("-" * 55)
print("  Describe your bag in English (colour, size, shape):")
desc = input("  → ")
print(f"  Nice description: '{desc}'")

# YOUR TASK:
# 1. Add 10 more adjectives (hot, cold, old, new, clean, dirty...)
# 2. Write a guessing game: describe an object using 3 adjectives,
#    have the user guess what it is
# 3. Create describe_person(hair_colour, eye_colour, height) that
#    outputs a full English description sentence
