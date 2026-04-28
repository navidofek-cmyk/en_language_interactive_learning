"""
LESSON 51: Academic Vocabulary
================================
⭐⭐⭐⭐ Level: B2–C1 | Upper-Intermediate

Akademická slovní zásoba — pro eseje, zprávy a formální text.
Topics: academic word list · verbs · nouns · linking language
"""
import random

ACADEMIC_VERBS = {
    "analyse":      "analyzovat",     "assess":       "posoudit, zhodnotit",
    "argue":        "tvrdit, argumentovat", "claim":  "tvrdit, prohlašovat",
    "conclude":     "dospět k závěru","demonstrate":  "prokázat, demonstrovat",
    "determine":    "určit, zjistit", "emphasise":    "zdůraznit",
    "establish":    "zjistit, stanovit","evaluate":   "vyhodnotit",
    "examine":      "zkoumat",        "highlight":    "zdůraznit, poukázat",
    "identify":     "identifikovat",  "illustrate":   "ilustrovat, doložit",
    "imply":        "naznačovat",     "indicate":     "naznačovat, ukazovat",
    "investigate":  "zkoumat, prošetřit","justify":   "zdůvodnit, oправdать",
    "maintain":     "tvrdit, zastávat","outline":     "nastínit",
    "propose":      "navrhnout",      "suggest":      "navrhnout, naznačovat",
    "support":      "podpořit, doložit","challenge":  "zpochybnit",
    "contradict":   "odporovat",      "acknowledge":  "uznat, přiznat",
}

ACADEMIC_NOUNS = {
    "approach":     "přístup",        "assumption":   "předpoklad",
    "concept":      "pojem, koncept", "context":      "kontext",
    "evidence":     "důkaz, doklady", "factor":       "faktor",
    "framework":    "rámec",          "impact":       "dopad, vliv",
    "implication":  "důsledek",       "interpretation":"interpretace",
    "issue":        "otázka, problém","methodology":  "metodologie",
    "outcome":      "výsledek",       "perspective":  "perspektiva, pohled",
    "principle":    "princip, zásada","process":      "proces",
    "research":     "výzkum",         "significance": "význam",
    "theory":       "teorie",         "trend":        "trend",
}

ACADEMIC_PHRASES = {
    "It can be argued that...":       "Lze tvrdit, že...",
    "Evidence suggests that...":      "Důkazy naznačují, že...",
    "This is supported by...":        "To je podpořeno...",
    "A key factor is...":             "Klíčovým faktorem je...",
    "It is worth noting that...":     "Stojí za zmínku, že...",
    "In contrast to this,...":        "V kontrastu s tím,...",
    "Despite this,...":               "Přesto,...",
    "The findings indicate that...":  "Zjištění naznačují, že...",
    "This raises the question of...": "To vznáší otázku ohledně...",
    "A significant implication is...":"Významným důsledkem je...",
}

print("=" * 55)
print("  LESSON 51: Academic Vocabulary")
print("=" * 55)

print("\n📚 ACADEMIC VERBS:")
print("-" * 55)
items = list(ACADEMIC_VERBS.items())
for i in range(0, len(items), 2):
    row = items[i:i+2]
    print("  " + "   ".join(f"{en:<18}{cz:<22}" for en, cz in row))

print("\n📚 ACADEMIC NOUNS:")
print("-" * 55)
items = list(ACADEMIC_NOUNS.items())
for i in range(0, len(items), 2):
    row = items[i:i+2]
    print("  " + "   ".join(f"{en:<18}{cz:<22}" for en, cz in row))

print("\n📚 ACADEMIC PHRASES:")
print("-" * 55)
for en, cz in ACADEMIC_PHRASES.items():
    print(f"  {en}")
    print(f"    → {cz}\n")

print("\n📝 HEDGING LANGUAGE (tentativeness in academic writing):")
print("-" * 55)
hedges = [
    ("It appears/seems that...",    "Zdá se, že..."),
    ("This may/might suggest...",   "To může naznačovat..."),
    ("It is possible that...",      "Je možné, že..."),
    ("In most cases,...",           "Ve většině případů,..."),
    ("There is a tendency to...",   "Existuje tendence k..."),
    ("This could be attributed to..","To by mohlo být přisuzováno..."),
]
for en, cz in hedges:
    print(f"  {en:<38} → {cz}")

print("\n🎯 QUIZ:")
print("-" * 55)
all_vocab = {**ACADEMIC_VERBS, **ACADEMIC_NOUNS}
pairs = random.sample(list(all_vocab.items()), 8)
score = 0
for en, cz in pairs:
    ans = input(f"  {cz}  →  ").strip()
    if ans.lower() == en.lower():
        print("  ✓ Correct!\n"); score += 1
    else:
        print(f"  ✗ Answer: {en}\n")
print(f"  Score: {score}/8")

# YOUR TASK:
# 1. Replace informal words in these sentences with academic equivalents:
#    a) "Lots of research shows that sleep is really important."
#    b) "People think that climate change is a big problem."
# 2. Write an academic paragraph (100 words) on a topic you know,
#    using at least 8 words from this lesson
# 3. Write 5 sentences using hedging language
