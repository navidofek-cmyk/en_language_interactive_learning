"""
LESSON 05: Food & Drink
=========================
⭐ Level: A1–A2 | Beginner

Jídlo, pití a jak objednat v restauraci.
Topics: food · drink · ordering · countable vs uncountable nouns
"""
import random

FOOD = {
    "bread":      "chléb",      "butter":     "máslo",
    "cheese":     "sýr",        "egg":        "vejce",
    "meat":       "maso",       "chicken":    "kuře",
    "fish":       "ryba",       "rice":       "rýže",
    "pasta":      "těstoviny",  "soup":       "polévka",
    "salad":      "salát",      "sandwich":   "sendvič",
    "pizza":      "pizza",      "burger":     "hamburger",
    "apple":      "jablko",     "banana":     "banán",
    "orange":     "pomeranč",   "strawberry": "jahoda",
    "cake":       "dort / koláč","chocolate":  "čokoláda",
    "ice cream":  "zmrzlina",   "biscuit":    "sušenka",
    "vegetables": "zelenina",   "fruit":      "ovoce",
}

DRINK = {
    "water":        "voda",
    "still water":  "neperlivá voda",
    "sparkling water": "perlivá voda",
    "coffee":       "káva",
    "tea":          "čaj",
    "juice":        "džus",
    "milk":         "mléko",
    "beer":         "pivo",
    "wine":         "víno",
    "lemonade":     "limonáda",
}

RESTAURANT = {
    "I'd like ...":           "Chtěl/a bych ...",
    "Can I have ... please?": "Mohl/a bych dostat ...?",
    "What do you recommend?": "Co doporučujete?",
    "The bill, please":       "Účet, prosím",
    "Is service included?":   "Je zahrnuta obsluha?",
    "I'm vegetarian":         "Jsem vegetarián/ka",
    "I'm allergic to ...":    "Jsem alergický/á na ...",
    "It's delicious!":        "Je to skvělé!",
    "Enjoy your meal!":       "Dobrou chuť!",
    "Could I see the menu?":  "Mohl/a bych dostat jídelní lístek?",
}

print("=" * 55)
print("  LESSON 05: Food & Drink")
print("=" * 55)

print("\n📚 FOOD:")
print("-" * 55)
items = list(FOOD.items())
for i in range(0, len(items), 2):
    pair = items[i:i+2]
    line = "  "
    for en, cz in pair:
        line += f"{en:<16} {cz:<18}"
    print(line)

print("\n📚 DRINKS:")
print("-" * 55)
for en, cz in DRINK.items():
    print(f"  {en:<22} {cz}")

print("\n📚 AT THE RESTAURANT:")
print("-" * 55)
for en, cz in RESTAURANT.items():
    print(f"  {en:<34} {cz}")

print("\n📝 COUNTABLE vs UNCOUNTABLE:")
print("-" * 55)
print("  Countable (lze počítat):")
print("    an apple / two apples   an egg / three eggs")
print()
print("  Uncountable (nelze počítat — bez číslovky a 'a/an'):")
print("    some water  (NE: a water)   some rice  (NE: a rice)")
print("    some bread  (NE: a bread)   some milk  (NE: a milk)")
print()
print("  Tip: 'a glass of water' / 'a cup of tea' / 'a slice of bread'")

print("\n💬 DIALOGUE — At the restaurant:")
print("-" * 55)
print("  Waiter: Good evening! Are you ready to order?")
print("  Customer: Yes. I'd like the chicken soup and pasta, please.")
print("  Waiter: And to drink?")
print("  Customer: A glass of sparkling water, please.")
print("  Waiter: Certainly. Enjoy your meal!")
print("  Customer: Thank you! Could I have the bill afterwards?")

print("\n🎯 QUIZ — přelož do angličtiny:")
print("-" * 55)
all_vocab = {**FOOD, **DRINK}
pairs = random.sample(list(all_vocab.items()), 7)
score = 0
for en, cz in pairs:
    ans = input(f"  {cz}  →  ").strip()
    if ans.lower() == en.lower():
        print("  ✓ Correct!\n")
        score += 1
    else:
        print(f"  ✗ Answer: {en}\n")
print(f"  Score: {score}/7")

# YOUR TASK:
# 1. Add 10 more food items to FOOD dictionary
# 2. Write a function order(food, drink) that generates a polite
#    restaurant order in English
# 3. Create a menu game: show a random Czech food name, the user
#    must order it correctly in English using restaurant phrases
