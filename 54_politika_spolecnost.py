"""
LESSON 54: Politics & Society
================================
⭐⭐⭐⭐ Level: B2 | Upper-Intermediate

Politika, společnost a aktuální otázky.
Topics: government · politics · social issues · economy · globalisation
"""
import random

GOVERNMENT = {
    "parliament":       "parlament",      "government":     "vláda",
    "prime minister":   "premiér",        "president":      "prezident",
    "minister":         "ministr",        "MP (member of parliament)":"poslanec",
    "opposition":       "opozice",        "coalition":      "koalice",
    "election":         "volby",          "vote":           "hlasovat/hlas",
    "ballot":           "hlasovací lístek","constituency":  "volební obvod",
    "policy":           "politika (opatření)","legislation": "zákonodárství",
    "bill":             "návrh zákona",   "act":            "zákon (přijatý)",
    "referendum":       "referendum",     "debate":         "debata",
    "democracy":        "demokracie",     "dictatorship":   "diktatura",
    "left-wing":        "levicový",       "right-wing":     "pravicový",
    "liberal":          "liberální",      "conservative":   "konzervativní",
}

SOCIAL_ISSUES = {
    "inequality":       "nerovnost",      "poverty":        "chudoba",
    "homelessness":     "bezdomovectví",  "unemployment":   "nezaměstnanost",
    "immigration":      "imigrace",       "integration":    "integrace",
    "discrimination":   "diskriminace",   "racism":         "rasismus",
    "gender equality":  "rovnost pohlaví","human rights":   "lidská práva",
    "welfare state":    "sociální stát",  "pension":        "důchod",
    "healthcare":       "zdravotní péče", "public services":"veřejné služby",
    "social mobility":  "sociální mobilita","austerity":    "úsporná opatření",
}

OPINION_PHRASES = {
    "The government should...":      "Vláda by měla...",
    "It is the state's responsibility to...":"Je odpovědností státu...",
    "There is a growing concern that...":"Roste obava, že...",
    "Evidence suggests that...":     "Důkazy naznačují, že...",
    "Critics argue that...":         "Kritici tvrdí, že...",
    "Proponents claim that...":      "Zastánci tvrdí, že...",
    "On the one hand,... on the other,...":"Na jedné straně,... na druhé,...",
    "This raises questions about...":"To vyvolává otázky ohledně...",
}

print("=" * 55)
print("  LESSON 54: Politics & Society")
print("=" * 55)

print("\n📚 GOVERNMENT & POLITICS:")
print("-" * 55)
items = list(GOVERNMENT.items())
for i in range(0, len(items), 2):
    row = items[i:i+2]
    print("  " + "   ".join(f"{en:<24}{cz:<22}" for en, cz in row))

print("\n📚 SOCIAL ISSUES:")
print("-" * 55)
for en, cz in SOCIAL_ISSUES.items():
    print(f"  {en:<24} {cz}")

print("\n📚 OPINION LANGUAGE:")
print("-" * 55)
for en, cz in OPINION_PHRASES.items():
    print(f"  {en}")
    print(f"    → {cz}\n")

print("\n💬 SAMPLE DISCUSSION:")
print("-" * 55)
print("  'Should university education be funded by the state?'")
print()
print("  Proponents argue that free education reduces inequality")
print("  and improves social mobility. Evidence from Scandinavian")
print("  countries suggests that state-funded education leads to")
print("  a more educated and productive workforce. Critics, however,")
print("  claim that the high cost is unsustainable and that students")
print("  who pay for their education value it more.")

print("\n🎯 QUIZ:")
print("-" * 55)
all_vocab = {**GOVERNMENT, **SOCIAL_ISSUES}
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
# 1. Describe the political system in your country in 5 sentences
# 2. Choose a social issue and write a for/against paragraph (100 words)
# 3. Write a letter to a politician about an issue you care about
