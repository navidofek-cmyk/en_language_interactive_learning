"""
LESSON 14: Shopping & Money
==============================
⭐⭐ Level: A2 | Elementary

Nakupování, peníze a jak komunikovat v obchodě.
Topics: shopping · money · clothes · comparing prices
"""
import random

CLOTHES = {
    "jacket":     "bunda / sako",  "coat":      "kabát",
    "shirt":      "košile",        "blouse":    "halenka",
    "trousers":   "kalhoty",       "jeans":     "džíny",
    "skirt":      "sukně",         "dress":     "šaty",
    "suit":       "oblek",         "jumper / sweater": "svetr",
    "hoodie":     "mikina s kapucí","T-shirt":   "tričko",
    "socks":      "ponožky",       "underwear": "spodní prádlo",
    "shoes":      "boty",          "boots":     "kotníkové boty",
    "trainers":   "tenisky",       "sandals":   "sandály",
    "scarf":      "šátek / šála",  "gloves":    "rukavice",
    "hat":        "čepice / klobouk","belt":     "opasek",
}

SHOPPING_PHRASES = {
    "Can I try this on?":         "Mohu si to vyzkoušet?",
    "Do you have this in a size M?":"Máte toto ve velikosti M?",
    "Have you got it in blue?":   "Máte to v modré barvě?",
    "How much is this?":          "Kolik to stojí?",
    "It's too expensive.":        "Je to příliš drahé.",
    "I'll take it.":              "Vezmu si to.",
    "Can I pay by card?":         "Mohu platit kartou?",
    "Do you accept contactless?": "Přijímáte bezkontaktní platby?",
    "Can I have a receipt?":      "Mohu dostat účtenku?",
    "Do you have anything cheaper?":"Máte něco levnějšího?",
    "It doesn't fit.":            "Nesedí mi to.",
    "Can I return this?":         "Mohu toto vrátit?",
    "The changing rooms are over there.":"Kabinky jsou tam.",
}

ADJECTIVES = {
    "cheap ↔ expensive":  "levný ↔ drahý",
    "good value":         "dobrá hodnota za peníze",
    "on sale / reduced":  "ve slevě",
    "sold out":           "vyprodáno",
    "in stock":           "skladem",
    "fits well":          "sedí dobře",
    "tight ↔ loose":      "těsné ↔ volné",
    "smart / casual":     "elegantní / neformální",
}

print("=" * 55)
print("  LESSON 14: Shopping & Money")
print("=" * 55)

print("\n📚 CLOTHES:")
print("-" * 55)
items = list(CLOTHES.items())
for i in range(0, len(items), 2):
    row = items[i:i+2]
    print("  " + "   ".join(f"{en:<20}{cz:<20}" for en, cz in row))

print("\n📚 IN THE SHOP:")
print("-" * 55)
for en, cz in SHOPPING_PHRASES.items():
    print(f"  {en}")
    print(f"    → {cz}\n")

print("\n📚 USEFUL ADJECTIVES:")
print("-" * 55)
for en, cz in ADJECTIVES.items():
    print(f"  {en:<24} {cz}")

print("\n📝 COMPARING PRICES:")
print("-" * 55)
print("  This jacket is MORE EXPENSIVE than that one.")
print("  These shoes are CHEAPER than those boots.")
print("  This is the BEST VALUE item in the shop.")
print("  That coat is TOO EXPENSIVE — I can't afford it.")
print("  This scarf is NOT EXPENSIVE ENOUGH — I want something nicer.")

print("\n💬 DIALOGUE — In a clothes shop:")
print("-" * 55)
print("  Assistant: Can I help you?")
print("  Customer:  Yes, I'm looking for a jacket.")
print("  Assistant: What size are you?")
print("  Customer:  Medium, I think. How much is this one?")
print("  Assistant: It's £45.99. Would you like to try it on?")
print("  Customer:  Yes, please. ... Hmm, it's a bit tight.")
print("             Do you have it in a large?")
print("  Assistant: Let me check... Yes, here you are.")
print("  Customer:  Perfect, it fits. I'll take it. Can I pay by card?")

print("\n🎯 QUIZ — přelož do angličtiny:")
print("-" * 55)
all_vocab = {**CLOTHES, **ADJECTIVES}
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
# 1. Describe what you are wearing right now in English
# 2. Write a dialogue at a shoe shop (at least 8 exchanges)
# 3. Compare two clothing items: price, quality, style
#    using comparatives (more expensive, better, cheaper...)
