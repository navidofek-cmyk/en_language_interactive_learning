"""
LESSON 24: Weather & Nature
=============================
⭐⭐ Level: A2 | Elementary

Počasí, příroda a životní prostředí.
Topics: weather · natural world · environment · seasons
"""
import random

WEATHER = {
    "sunny":          "slunečno",        "cloudy":       "oblačno",
    "overcast":       "zataženo",        "rainy":        "deštivo",
    "drizzle":        "mrholení",        "shower":       "přeháňka",
    "thunderstorm":   "bouřka",          "lightning":    "blesk",
    "thunder":        "hrom",            "foggy":        "mlhavo",
    "windy":          "větrno",          "breezy":       "vane mírný vítr",
    "snowy":          "sněživo",         "icy":          "ledovkovo",
    "frosty":         "mrzne",           "heatwave":     "vlna veder",
    "humid":          "vlhko",           "dry":          "sucho",
    "mild":           "mírné (počasí)",  "chilly":       "chladivo",
}

NATURE = {
    "mountain":       "hora",            "river":        "řeka",
    "lake":           "jezero",          "sea":          "moře",
    "ocean":          "oceán",           "forest":       "les",
    "field":          "pole",            "valley":       "údolí",
    "hill":           "kopec",           "cliff":        "útes",
    "waterfall":      "vodopád",         "island":       "ostrov",
    "desert":         "poušť",           "jungle":       "džungle",
    "glacier":        "ledovec",         "volcano":      "sopka",
}

ENVIRONMENT = {
    "climate change":   "změna klimatu",
    "global warming":   "globální oteplování",
    "renewable energy": "obnovitelná energie",
    "carbon footprint": "uhlíková stopa",
    "recycle":          "recyklovat",
    "pollution":        "znečištění",
    "endangered species":"ohrožený druh",
    "deforestation":    "odlesňování",
    "sustainable":      "udržitelný",
    "solar panel":      "solární panel",
}

def describe_weather(temp_c):
    if temp_c < 0:    return "It's freezing!"
    elif temp_c < 5:  return "It's very cold."
    elif temp_c < 10: return "It's cold."
    elif temp_c < 15: return "It's chilly."
    elif temp_c < 20: return "It's mild."
    elif temp_c < 25: return "It's warm."
    elif temp_c < 30: return "It's hot."
    else:             return "It's boiling!"

print("=" * 55)
print("  LESSON 24: Weather & Nature")
print("=" * 55)

print("\n📚 WEATHER:")
print("-" * 55)
items = list(WEATHER.items())
for i in range(0, len(items), 2):
    row = items[i:i+2]
    print("  " + "   ".join(f"{en:<20}{cz:<18}" for en, cz in row))

print("\n📚 NATURE:")
print("-" * 55)
items = list(NATURE.items())
for i in range(0, len(items), 3):
    row = items[i:i+3]
    print("  " + "   ".join(f"{en:<16}{cz:<14}" for en, cz in row))

print("\n📚 ENVIRONMENT:")
print("-" * 55)
for en, cz in ENVIRONMENT.items():
    print(f"  {en:<24} {cz}")

print("\n📝 GRAMMAR — talking about weather:")
print("-" * 55)
print("  IT + to be + adjective:")
print("    It's sunny.  It was cold.  It will be rainy.")
print()
print("  IT + verb:")
print("    It's raining.  It snowed last night.  It thundered.")
print()
print("  Temperature:")
print("    It's 20 degrees (Celsius).")
print("    The temperature is below zero.")

print("\n💬 TEMPERATURE DESCRIPTIONS:")
print("-" * 55)
for temp in [-5, 0, 8, 15, 22, 28, 35]:
    print(f"  {temp:>3}°C  →  {describe_weather(temp)}")

print("\n🎯 QUIZ — přelož do angličtiny:")
print("-" * 55)
all_vocab = {**WEATHER, **NATURE}
pairs = random.sample(list(all_vocab.items()), 7)
score = 0
for en, cz in pairs:
    ans = input(f"  {cz}  →  ").strip()
    if ans.lower() == en.lower():
        print("  ✓ Correct!\n"); score += 1
    else:
        print(f"  ✗ Answer: {en}\n")
print(f"  Score: {score}/7")

# YOUR TASK:
# 1. Describe today's weather in 3–4 sentences
# 2. Describe your favourite season and explain why you like it
# 3. Write 5 sentences about an environmental problem you care about,
#    using vocabulary from the ENVIRONMENT section
