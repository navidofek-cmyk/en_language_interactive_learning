"""
LESSON 57: Environment — Advanced
=====================================
⭐⭐⭐⭐ Level: B2 | Upper-Intermediate

Životní prostředí — pokročilá slovní zásoba a argumenty.
Topics: climate change · sustainability · energy · solutions · debate
"""
import random

CLIMATE_VOCAB = {
    "carbon dioxide (CO₂)":    "oxid uhličitý",
    "greenhouse gas":          "skleníkový plyn",
    "greenhouse effect":       "skleníkový efekt",
    "global warming":          "globální oteplování",
    "climate crisis":          "klimatická krize",
    "carbon footprint":        "uhlíková stopa",
    "carbon neutral":          "uhlíkově neutrální",
    "net zero":                "čisté nulové emise",
    "emissions":               "emise",
    "fossil fuel":             "fosilní palivo",
    "renewable energy":        "obnovitelná energie",
    "solar/wind power":        "sluneční/větrná energie",
    "deforestation":           "odlesňování",
    "biodiversity":            "biodiverzita",
    "ecosystem":               "ekosystém",
    "habitat loss":            "ztráta přirozeného prostředí",
    "extinction":              "vymírání",
    "sea level rise":          "stoupání hladiny moří",
    "heatwave":                "vlna veder",
    "drought":                 "sucho",
    "flood":                   "záplava",
    "sustainable development": "udržitelný rozvoj",
    "circular economy":        "oběhové hospodářství",
    "carbon offsetting":       "kompenzace uhlíku",
    "green technology":        "ekologická technologie",
    "electric vehicle (EV)":   "elektrické vozidlo",
    "insulation":              "zateplení (budov)",
    "plant-based diet":        "rostlinná strava",
    "fast fashion":            "rychlá móda",
}

ARGUMENTS = {
    "FOR strong climate action": [
        "The scientific consensus is overwhelming — we must act now.",
        "The costs of inaction far outweigh the costs of action.",
        "Developing countries are disproportionately affected.",
        "Future generations will inherit the consequences of today's decisions.",
        "Green energy creates jobs and stimulates economic growth.",
    ],
    "SCEPTICAL / nuanced views": [
        "Individual action is meaningless without systemic change.",
        "Developing nations have the right to industrialise.",
        "Technological innovation will solve the problem.",
        "Current policies disproportionately burden the poor.",
        "Political will, not public awareness, is the key bottleneck.",
    ],
}

print("=" * 55)
print("  LESSON 57: Environment — Advanced")
print("=" * 55)

print("\n📚 CLIMATE & ENVIRONMENT VOCABULARY:")
print("-" * 55)
items = list(CLIMATE_VOCAB.items())
for i in range(0, len(items), 2):
    row = items[i:i+2]
    print("  " + "   ".join(f"{en:<30}{cz:<22}" for en, cz in row))

print("\n📚 ARGUMENTS:")
print("-" * 55)
for side, points in ARGUMENTS.items():
    print(f"\n  {side}:")
    for p in points:
        print(f"    • {p}")

print("\n📝 LANGUAGE FOR ENVIRONMENTAL DISCUSSION:")
print("-" * 55)
phrases = [
    ("There is compelling evidence that...",       "Je přesvědčivý důkaz, že..."),
    ("The consequences could be catastrophic.",    "Důsledky by mohly být katastrofické."),
    ("A sustainable approach would involve...",    "Udržitelný přístup by zahrnoval..."),
    ("Addressing this requires both X and Y.",     "Řešení tohoto vyžaduje jak X, tak Y."),
    ("The burden falls disproportionately on...", "Zátěž neúměrně dopadá na..."),
    ("This is a systemic issue, not just individual.","Toto je systémový problém, nejen individuální."),
]
for en, cz in phrases:
    print(f"  {en}")
    print(f"    → {cz}\n")

print("\n🎯 QUIZ:")
print("-" * 55)
pairs = random.sample(list(CLIMATE_VOCAB.items()), 8)
score = 0
for en, cz in pairs:
    ans = input(f"  {cz}  →  ").strip()
    if ans.lower() == en.lower():
        print("  ✓ Correct!\n"); score += 1
    else:
        print(f"  ✗ Answer: {en}\n")
print(f"  Score: {score}/8")

# YOUR TASK:
# 1. Write a 150-word argument FOR or AGAINST a carbon tax
# 2. Calculate your approximate carbon footprint and describe ways to reduce it
# 3. Write a letter to your MP/minister about one environmental issue
