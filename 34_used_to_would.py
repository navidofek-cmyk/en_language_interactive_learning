"""
LESSON 34: Used To & Would
============================
⭐⭐ Level: B1 | Pre-Intermediate

Minulé zvyky a stavy — used to, would, be/get used to.
Topics: used to · would · be used to · get used to
"""
import random

STRUCTURES = {
    "used to + infinitive": {
        "use":   "Past habit or state that no longer exists",
        "examples": [
            ("I used to play football every weekend.",
             "Každý víkend jsem hrával fotbal. (už ne)"),
            ("She used to live in Paris.",
             "Dřív žila v Paříži. (teď ne)"),
            ("Did you use to have long hair?",
             "Nosil/a jsi dřív dlouhé vlasy?"),
            ("He didn't use to like coffee.",
             "Dřív neměl rád kávu."),
        ],
        "note": "For BOTH habits AND states in the past",
    },
    "would + infinitive": {
        "use":   "Past habit (repeated action, NOT states)",
        "examples": [
            ("When I was young, we would spend summers at the lake.",
             "Když jsem byl/a malý/á, trávili jsme léta u jezera."),
            ("Every Sunday she would bake bread.",
             "Každou neděli pekla chléb."),
            ("He would always forget his keys.",
             "Vždy zapomínal klíče."),
        ],
        "note": "Only for HABITS, not states. Cannot say: 'I would live in Paris.'",
    },
    "be used to + gerund": {
        "use":   "Accustomed to something (now)",
        "examples": [
            ("I'm used to getting up early.",
             "Jsem zvyklý/á vstávat brzy."),
            ("She's used to working long hours.",
             "Je zvyklá pracovat dlouho."),
            ("Are you used to driving on the left?",
             "Jsi zvyklý/á řídit vpravo? (Británie)"),
        ],
        "note": "be + used to = be accustomed to — NOT past!",
    },
    "get used to + gerund": {
        "use":   "Becoming accustomed (process)",
        "examples": [
            ("I'm getting used to the new system.",
             "Zvykám si na nový systém."),
            ("She got used to living alone quickly.",
             "Rychle si zvykla na život sama."),
            ("It takes time to get used to a new country.",
             "Zabere čas zvyknout si na novou zemi."),
        ],
        "note": "get used to = process of becoming accustomed",
    },
}

print("=" * 55)
print("  LESSON 34: Used To & Would")
print("=" * 55)

for structure, data in STRUCTURES.items():
    print(f"\n📚 {structure.upper()}:")
    print("-" * 55)
    print(f"  Use: {data['use']}")
    print(f"  Note: {data['note']}\n")
    for en, cz in data["examples"]:
        print(f"  {en}")
        print(f"    → {cz}\n")

print("\n📝 COMPARISON:")
print("-" * 55)
print("  used to live   = I lived there before (no longer)")
print("  would live     ✗ cannot use would for states")
print("  be used to living = I'm accustomed to living there (now)")
print("  get used to living = I'm becoming accustomed (process)")
print()
print("  ⚠️  'use to' (without 'd') only appears in questions/negatives:")
print("  Did you USE TO play piano?  /  I didn't USE TO like vegetables.")

print("\n🎯 QUIZ — used to / would / be used to / get used to?")
print("-" * 55)
quiz = [
    ("When I was a child, I ___ climb trees every day. (habit)", "used to / would"),
    ("She ___ live in London — now she's in Berlin. (state)", "used to"),
    ("I'm ___ working night shifts — I've done it for years. (accustomed)", "used to"),
    ("It's hard at first but you'll soon ___ the cold. (becoming accustomed)", "get used to"),
    ("Every summer we ___ visit our grandparents. (repeated past action)", "would / used to"),
    ("Is he ___ driving on the left yet? (accustomed)", "used to"),
]
score = 0
for sentence, answer in quiz:
    print(f"  {sentence}")
    ans = input("  → ").strip()
    if any(a.strip().lower() in ans.lower() for a in answer.split("/")):
        print("  ✓ Correct!\n"); score += 1
    else:
        print(f"  ✗ Answer: {answer}\n")
print(f"  Score: {score}/6")

# YOUR TASK:
# 1. Write 5 sentences about what you used to do as a child
# 2. Describe a typical childhood summer using 'would'
# 3. Write about something you had to get used to (new job, city, habit)
