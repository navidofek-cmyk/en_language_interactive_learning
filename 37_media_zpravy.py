"""
LESSON 37: Media & News
=========================
⭐⭐⭐ Level: B1 | Pre-Intermediate

Média, zprávy a jak mluvit o aktuálních událostech.
Topics: news vocabulary · media types · headlines · opinion language
"""
import random

MEDIA_TYPES = {
    "broadsheet":       "seriózní noviny (The Times, Guardian)",
    "tabloid":          "bulvár (The Sun, Daily Mirror)",
    "broadband":        "online médium",
    "podcast":          "podcast",
    "documentary":      "dokumentární film",
    "live broadcast":   "živé vysílání",
    "breaking news":    "nejnovější zprávy",
    "headline":         "titulek",
    "article":          "článek",
    "editorial":        "úvodník, komentář",
    "feature":          "publicistický článek",
    "press release":    "tisková zpráva",
    "correspondent":    "zpravodaj",
    "anchor":           "moderátor zpráv",
    "source":           "zdroj",
    "exclusive":        "exkluzivní zpráva",
    "scoop":            "senzační zpráva",
    "bias":             "zaujatost",
    "fake news":        "dezinformace",
    "clickbait":        "clickbait (lákavý titulek)",
}

NEWS_VERBS = {
    "report":       "informovat, hlásit",
    "announce":     "oznámit",
    "claim":        "tvrdit",
    "reveal":       "odhalit",
    "confirm":      "potvrdit",
    "deny":         "popřít",
    "warn":         "varovat",
    "call for":     "vyzývat k",
    "accuse of":    "obvinit z",
    "urge":         "naléhavě vyzývat",
    "launch":       "zahájit",
    "face":         "čelit",
    "back":         "podpořit",
    "slam":         "ostře kritizovat (tabloid)",
}

HEADLINE_LANGUAGE = [
    ("Short, active, often without articles:",  ""),
    ("PM BACKS new housing plan",               "Premiér podporuje nový plán bydlení"),
    ("SCIENTISTS WARN of rising sea levels",    "Vědci varují před stoupajícími hladinami"),
    ("TALKS COLLAPSE over trade deal",          "Jednání o obchodní dohodě se zhroutila"),
    ("FIRM FACES probe over tax claims",        "Firma čelí vyšetřování ohledně daní"),
    ("'I was terrified' — quake survivor",      "Přímá řeč zkrácena v uvozovkách"),
]

OPINION_PHRASES = {
    "In my opinion,...":          "Podle mého názoru,...",
    "It seems to me that...":     "Zdá se mi, že...",
    "I believe that...":          "Věřím, že...",
    "According to...":            "Podle...",
    "It has been reported that...":"Bylo oznámeno, že...",
    "There are concerns that...": "Panují obavy, že...",
    "Experts argue that...":      "Odborníci tvrdí, že...",
    "On the one hand,... but on the other,...": "Na jedné straně,... ale na druhé,...",
}

print("=" * 55)
print("  LESSON 37: Media & News")
print("=" * 55)

print("\n📚 MEDIA & NEWS VOCABULARY:")
print("-" * 55)
for en, cz in MEDIA_TYPES.items():
    print(f"  {en:<22} {cz}")

print("\n📚 NEWS VERBS:")
print("-" * 55)
for en, cz in NEWS_VERBS.items():
    print(f"  {en:<16} {cz}")

print("\n📚 HEADLINE LANGUAGE (compressed style):")
print("-" * 55)
for en, cz in HEADLINE_LANGUAGE:
    if cz:
        print(f"  {en:<44} → {cz}")
    else:
        print(f"\n  {en}")

print("\n📚 OPINION & REPORTING LANGUAGE:")
print("-" * 55)
for en, cz in OPINION_PHRASES.items():
    print(f"  {en}")
    print(f"    → {cz}\n")

print("\n💬 DISCUSSING THE NEWS:")
print("-" * 55)
discussion = [
    ("Have you heard about the new climate agreement?",
     "Slyšel/a jsi o nové klimatické dohodě?"),
    ("According to the BBC, the talks were successful.",
     "Podle BBC jednání proběhla úspěšně."),
    ("I'm not sure I trust that source — it's quite biased.",
     "Nejsem si jistý/á, zda tomu zdroji věřím — je docela zaujatý."),
    ("It's important to check multiple sources.",
     "Je důležité ověřit více zdrojů."),
]
for en, cz in discussion:
    print(f"  {en}")
    print(f"    → {cz}\n")

print("\n🎯 QUIZ — vocabulary:")
print("-" * 55)
all_vocab = {**MEDIA_TYPES, **NEWS_VERBS}
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
# 1. Find a real English news headline and rewrite it as a full sentence
# 2. Write a short news report (80 words) about a local event
# 3. Discuss a current news story: state the facts, then give your opinion
#    using opinion language from this lesson
