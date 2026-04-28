"""
LESSON 13: Travel & Transport
================================
⭐⭐ Level: A2–B1 | Elementary

Cestování, doprava a situace na cestách.
Topics: transport · airport · hotel · directions · travel phrases
"""
import random

TRANSPORT = {
    "plane / aircraft": "letadlo",  "train":   "vlak",
    "bus":              "autobus",  "tram":    "tramvaj",
    "underground / metro": "metro", "taxi":    "taxi",
    "car":              "auto",     "bicycle / bike": "kolo",
    "motorbike":        "motorka",  "ferry":   "trajekt",
    "coach":            "dálkový autobus", "lorry / truck": "nákladní auto",
}

AIRPORT = {
    "passport control":  "pasová kontrola",
    "customs":           "celnice",
    "departure gate":    "odletová brána",
    "arrivals / departures": "příjezdy / odjezdy",
    "check-in":          "odbavení",
    "boarding pass":     "palubní lístek",
    "hand luggage":      "příruční zavazadlo",
    "baggage reclaim":   "výdej zavazadel",
    "delayed / on time": "zpožděný / včas",
    "flight number":     "číslo letu",
}

DIRECTIONS = {
    "Turn left":         "Odbočte doleva",
    "Turn right":        "Odbočte doprava",
    "Go straight on":    "Jděte rovně",
    "Take the first left":"Odbočte první doleva",
    "It's on your left": "Je to na vaší levé straně",
    "Opposite":          "Naproti",
    "Next to":           "Vedle",
    "In front of":       "Před",
    "Behind":            "Za",
    "At the traffic lights": "Na semaforu",
    "At the roundabout": "Na kruhovém objezdu",
}

USEFUL_PHRASES = {
    "A return ticket to ..., please":  "Zpáteční jízdenku do ..., prosím",
    "What time does the next ... leave?":"Kdy odjíždí/odlétá příští ...?",
    "Which platform?":                 "Které nástupiště?",
    "Is this seat taken?":             "Je toto místo obsazeno?",
    "Where is the nearest ...?":       "Kde je nejbližší ...?",
    "How far is it?":                  "Jak daleko je to?",
    "Can you call me a taxi?":         "Můžete mi zavolat taxi?",
    "I've missed my connection.":      "Zmeškal/a jsem přestup.",
    "My luggage is lost.":             "Moje zavazadlo se ztratilo.",
    "I'd like to check in.":           "Chtěl/a bych se ubytovat.",
}

print("=" * 55)
print("  LESSON 13: Travel & Transport")
print("=" * 55)

print("\n📚 TRANSPORT:")
print("-" * 55)
items = list(TRANSPORT.items())
for i in range(0, len(items), 2):
    row = items[i:i+2]
    print("  " + "   ".join(f"{en:<26}{cz:<18}" for en, cz in row))

print("\n📚 AT THE AIRPORT:")
print("-" * 55)
for en, cz in AIRPORT.items():
    print(f"  {en:<28} {cz}")

print("\n📚 ASKING FOR DIRECTIONS:")
print("-" * 55)
for en, cz in DIRECTIONS.items():
    print(f"  {en:<28} {cz}")

print("\n📚 USEFUL TRAVEL PHRASES:")
print("-" * 55)
for en, cz in USEFUL_PHRASES.items():
    print(f"  {en}")
    print(f"    → {cz}\n")

print("\n📝 PREPOSITIONS OF TRANSPORT:")
print("-" * 55)
print("  BY train / bus / plane / car / bike  (dopravní prostředek)")
print("  ON the train / bus / plane           (být na palubě)")
print("  IN the car / taxi                    (uzavřené vozidlo)")
print("  GET ON a bus/train | GET IN a car    (nastoupit)")
print("  GET OFF a bus/train | GET OUT of a car (vystoupit)")

print("\n🎯 QUIZ — přelož do angličtiny:")
print("-" * 55)
all_vocab = {**TRANSPORT, **AIRPORT, **DIRECTIONS}
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
# 1. Write directions from your home to the nearest train station
# 2. Write a short dialogue at a ticket office: buying a return ticket
# 3. Describe your last trip abroad (or a dream trip) using past simple
