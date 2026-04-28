"""
LESSON 04: Family & People
============================
⭐ Level: A1 | Beginner

Rodina, vztahy a popis lidí v angličtině.
Topics: family members · relationships · possessives · describing people
"""
import random

FAMILY = {
    "mother / mum":     "matka / máma",
    "father / dad":     "otec / táta",
    "parents":          "rodiče",
    "son":              "syn",
    "daughter":         "dcera",
    "brother":          "bratr",
    "sister":           "sestra",
    "siblings":         "sourozenci",
    "grandfather / grandpa": "dědeček",
    "grandmother / grandma": "babička",
    "grandparents":     "prarodiče",
    "uncle":            "strýc",
    "aunt":             "teta",
    "cousin":           "bratranec / sestřenice",
    "nephew":           "synovec",
    "niece":            "neteř",
    "husband":          "manžel",
    "wife":             "manželka",
    "partner":          "partner/ka",
    "child / children": "dítě / děti",
    "twins":            "dvojčata",
    "only child":       "jedináček",
    "stepfather":       "nevlastní otec",
    "stepmother":       "nevlastní matka",
    "mother-in-law":    "tchyně",
    "father-in-law":    "tchán",
}

POSSESSIVES = {
    "my":    "můj / moje",
    "your":  "tvůj / tvoje",
    "his":   "jeho",
    "her":   "její",
    "our":   "náš / naše",
    "their": "jejich",
}

print("=" * 55)
print("  LESSON 04: Family & People")
print("=" * 55)

print("\n📚 FAMILY MEMBERS:")
print("-" * 55)
for en, cz in FAMILY.items():
    print(f"  {en:<30} {cz}")

print("\n📚 POSSESSIVES (přivlastňovací zájmena):")
print("-" * 55)
for en, cz in POSSESSIVES.items():
    print(f"  {en:<10} {cz}")
print()
print("  my brother  (můj bratr)   | his sister  (jeho sestra)")
print("  her parents (její rodiče) | their son   (jejich syn)")

print("\n📝 POSSESSIVE 'S — přivlastňovací 's:")
print("-" * 55)
print("  Jan's mother     = Janova matka   (Jan + 's)")
print("  my sister's car  = auto mé sestry")
print("  my parents' house = dům mých rodičů  (plural: just ')")

print("\n💬 EXAMPLE — popis rodiny:")
print("-" * 55)
print("  I have a small family. My parents are Jan and Marie.")
print("  I have one brother. His name is Tomáš.")
print("  He is older than me. My grandparents live in Brno.")
print("  I don't have any sisters, but I have two cousins.")

print("\n🎯 QUIZ — přelož do angličtiny:")
print("-" * 55)
pairs = random.sample(list(FAMILY.items()), 7)
score = 0
for en, cz in pairs:
    ans = input(f"  {cz}  →  ").strip()
    if ans.lower() == en.lower():
        print("  ✓ Correct!\n")
        score += 1
    else:
        print(f"  ✗ Answer: {en}\n")
print(f"  Score: {score}/7")

print("\n✏️  SPEAKING TASK:")
print("-" * 55)
print("  Describe your family in 4–6 English sentences.")
print("  Use: I have ... | My ... is/are ... | He/She is ...")
answer = input("  → ")
print(f"  Well done! You wrote: '{answer}'")

# YOUR TASK:
# 1. Add more extended family words (godfather, godmother, foster parent...)
# 2. Write a function family_tree(name, relation) that returns a sentence:
#    family_tree("Eva", "sister") → "Eva is my sister."
# 3. Create a family quiz: show a relation in Czech, ask for English word,
#    then use it in a sentence with a random Czech name
