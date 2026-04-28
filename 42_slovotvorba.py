"""
LESSON 42: Word Formation
===========================
⭐⭐⭐ Level: B1–B2 | Pre-Intermediate

Tvoření slov — předpony, přípony a konverze.
Topics: prefixes · suffixes · noun/verb/adjective formation · word families
"""
import random

PREFIXES = {
    "un-":   ("negation",          ["unhappy","unfair","unable","unknown","unofficial"]),
    "re-":   ("again",             ["redo","rewrite","rebuild","return","reconsider"]),
    "over-": ("too much",          ["overwork","overeat","overcook","overestimate"]),
    "under-":("too little",        ["underestimate","underpay","undercooked"]),
    "pre-":  ("before",            ["preview","prepare","predict","prehistoric"]),
    "post-": ("after",             ["postpone","post-war","postgraduate"]),
    "mis-":  ("wrongly",           ["misunderstand","misuse","mislead","mistake"]),
    "dis-":  ("opposite/negative", ["disagree","disappear","dishonest","disconnect"]),
    "out-":  ("surpass",           ["outrun","outsmart","outperform","outlive"]),
    "anti-": ("against",           ["antibiotic","antisocial","antivirus"]),
    "inter-":("between",           ["international","internet","interview","interact"]),
    "self-": ("by oneself",        ["self-employed","self-confident","self-taught"]),
}

NOUN_SUFFIXES = {
    "-tion/-sion": ("verbs → nouns",    "decide→decision, educate→education"),
    "-ment":       ("verbs → nouns",    "develop→development, agree→agreement"),
    "-ness":       ("adj → nouns",      "happy→happiness, dark→darkness"),
    "-ity":        ("adj → nouns",      "able→ability, national→nationality"),
    "-er/-or":     ("verbs → person",   "teach→teacher, direct→director"),
    "-ist":        ("person/belief",    "art→artist, journal→journalist"),
    "-ism":        ("ideology/belief",  "capital→capitalism, tour→tourism"),
    "-hood":       ("state/group",      "child→childhood, neighbour→neighbourhood"),
    "-ship":       ("quality/status",   "friend→friendship, leader→leadership"),
    "-ance/-ence": ("state/quality",    "perform→performance, depend→dependence"),
}

ADJ_SUFFIXES = {
    "-ful":   ("full of",         "hope→hopeful, use→useful"),
    "-less":  ("without",         "hope→hopeless, use→useless, care→careless"),
    "-able/-ible":("can be done", "read→readable, access→accessible"),
    "-ous":   ("having quality",  "danger→dangerous, fame→famous"),
    "-al":    ("relating to",     "nation→national, tradition→traditional"),
    "-ic":    ("relating to",     "artist→artistic, economy→economic"),
    "-ive":   ("having tendency", "create→creative, attract→attractive"),
    "-ing":   ("causing feeling", "interest→interesting, amaze→amazing"),
    "-ed":    ("feeling",         "interest→interested, amaze→amazed"),
}

WORD_FAMILIES = {
    "educate": {
        "noun":    "education, educator",
        "verb":    "educate",
        "adjective":"educated, educational",
        "adverb":  "educationally",
    },
    "create": {
        "noun":    "creation, creator, creativity",
        "verb":    "create",
        "adjective":"creative, created",
        "adverb":  "creatively",
    },
    "depend": {
        "noun":    "dependence, dependency",
        "verb":    "depend",
        "adjective":"dependent, independent",
        "adverb":  "dependently, independently",
    },
}

print("=" * 55)
print("  LESSON 42: Word Formation")
print("=" * 55)

print("\n📚 PREFIXES:")
print("-" * 55)
for prefix, (meaning, examples) in PREFIXES.items():
    print(f"  {prefix:<10} ({meaning:<12}) {', '.join(examples[:4])}")

print("\n📚 NOUN SUFFIXES:")
print("-" * 55)
for suffix, (use, example) in NOUN_SUFFIXES.items():
    print(f"  {suffix:<16} {use:<22} {example}")

print("\n📚 ADJECTIVE SUFFIXES:")
print("-" * 55)
for suffix, (use, example) in ADJ_SUFFIXES.items():
    print(f"  {suffix:<16} {use:<22} {example}")

print("\n📚 WORD FAMILIES:")
print("-" * 55)
for base, forms in WORD_FAMILIES.items():
    print(f"\n  Base: {base}")
    for pos, words in forms.items():
        print(f"    {pos:<12} {words}")

print("\n🎯 QUIZ — form the correct word:")
print("-" * 55)
quiz = [
    ("The ___ (create) of this painting took two years. (noun)", "creation"),
    ("She is very ___ (depend) on her phone. (adj)", "dependent"),
    ("His ___ (manage) of the project was excellent. (noun)", "management"),
    ("The instructions were ___ (read) — I couldn't understand them. (adj, negative)", "unreadable"),
    ("We need to ___ (consider) our strategy. (do again)", "reconsider"),
    ("She is ___ (employ) — she runs her own business. (adj)", "self-employed"),
    ("The film was completely ___ (predict) — I knew the ending. (adj, negative)", "unpredictable"),
]
score = 0
for sentence, answer in quiz:
    print(f"  {sentence}")
    ans = input("  → ").strip()
    if ans.lower() == answer.lower():
        print("  ✓ Correct!\n"); score += 1
    else:
        print(f"  ✗ Answer: {answer}\n")
print(f"  Score: {score}/7")

# YOUR TASK:
# 1. For each suffix, create 3 new words not in the examples
# 2. Build a word family for: nation, develop, employ, succeed
# 3. Write a paragraph using at least 10 words formed with prefixes/suffixes
