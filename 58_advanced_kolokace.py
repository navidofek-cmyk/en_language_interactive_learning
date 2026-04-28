"""
LESSON 58: Advanced Collocations — B2/C1
==========================================
⭐⭐⭐⭐ Level: B2–C1 | Upper-Intermediate

Pokročilé kolokace — přirozené kombinace slov na úrovni C1.
Topics: verb + noun · adjective + noun · adverb + adjective · preposition phrases
"""
import random

VERB_NOUN = {
    "raise awareness":      "zvýšit povědomí",
    "address an issue":     "řešit problém",
    "meet a deadline":      "splnit termín",
    "reach a conclusion":   "dojít k závěru",
    "draw a distinction":   "rozlišovat",
    "strike a balance":     "najít rovnováhu",
    "bear responsibility":  "nést odpovědnost",
    "place emphasis on":    "klást důraz na",
    "pose a threat":        "představovat hrozbu",
    "take precedence over": "mít přednost před",
    "launch an initiative": "zahájit iniciativu",
    "foster collaboration": "podporovat spolupráci",
    "undermine confidence": "podkopávat důvěru",
    "yield results":        "přinášet výsledky",
    "conduct research":     "provádět výzkum",
    "implement a strategy": "implementovat strategii",
    "tackle a problem":     "řešit/potýkat se s problémem",
    "exert pressure":       "vyvíjet tlak",
    "spark debate":         "vyvolat debatu",
    "bridge the gap":       "překlenout mezeru/propast",
}

ADJ_NOUN = {
    "compelling evidence":  "přesvědčivý důkaz",
    "sweeping changes":     "rozsáhlé změny",
    "widespread concern":   "rozšířené obavy",
    "dire consequences":    "katastrofální důsledky",
    "profound impact":      "hluboký dopad",
    "robust framework":     "robustní rámec",
    "inherent risk":        "inherentní/vlastní riziko",
    "acute shortage":       "akutní nedostatek",
    "vested interest":      "osobní zájem, zainteresovanost",
    "viable alternative":   "životaschopná alternativa",
    "detrimental effect":   "škodlivý účinek",
    "unprecedented level":  "bezprecedentní úroveň",
    "heightened awareness": "zvýšené povědomí",
    "stark contrast":       "ostrý kontrast",
    "tacit agreement":      "mlčenlivý souhlas",
}

ADV_ADJ = {
    "deeply concerned":         "hluboce znepokojený",
    "highly significant":       "vysoce významný",
    "largely responsible":      "z velké části odpovědný",
    "broadly speaking":         "obecně řečeno",
    "fundamentally different":  "zásadně odlišný",
    "inherently complex":       "ze své podstaty složitý",
    "increasingly common":      "stále běžnější",
    "mutually beneficial":      "vzájemně výhodný",
    "critically important":     "kriticky důležitý",
    "sharply divided":          "ostře rozdělený",
}

print("=" * 55)
print("  LESSON 58: Advanced Collocations — B2/C1")
print("=" * 55)

print("\n📚 VERB + NOUN:")
print("-" * 55)
for col, cz in VERB_NOUN.items():
    print(f"  {col:<30} {cz}")

print("\n📚 ADJECTIVE + NOUN:")
print("-" * 55)
for col, cz in ADJ_NOUN.items():
    print(f"  {col:<28} {cz}")

print("\n📚 ADVERB + ADJECTIVE:")
print("-" * 55)
for col, cz in ADV_ADJ.items():
    print(f"  {col:<28} {cz}")

print("\n💬 IN CONTEXT:")
print("-" * 55)
examples = [
    "The report raises awareness of the widespread concern over inequality.",
    "It is critically important to strike a balance between growth and sustainability.",
    "The government has launched an initiative to tackle the acute shortage of housing.",
    "There is compelling evidence that sweeping changes are needed.",
    "Deeply concerned by the dire consequences, experts are calling for robust frameworks.",
]
for ex in examples:
    print(f"  {ex}")

print("\n🎯 QUIZ — complete the collocation:")
print("-" * 55)
all_col = {**VERB_NOUN, **ADJ_NOUN, **ADV_ADJ}
pairs = random.sample(list(all_col.items()), 8)
score = 0
for col, cz in pairs:
    ans = input(f"  {cz}  →  ").strip()
    if ans.lower() == col.lower():
        print("  ✓ Correct!\n"); score += 1
    else:
        print(f"  ✗ Answer: {col}\n")
print(f"  Score: {score}/8")

# YOUR TASK:
# 1. Write 10 sentences using collocations from VERB + NOUN
# 2. Write a formal paragraph (100 words) using at least 6 advanced collocations
# 3. Find 5 advanced collocations in a quality English newspaper this week
