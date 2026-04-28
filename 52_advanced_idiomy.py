"""
LESSON 52: Advanced Idioms & Fixed Expressions
================================================
⭐⭐⭐⭐ Level: B2–C1 | Upper-Intermediate

Pokročilé idiomy a ustálené výrazy na úrovni C1.
Topics: formal idioms · business idioms · debate expressions · literary idioms
"""
import random

IDIOMS_C1 = {
    # Thinking / knowledge
    "on the tip of my tongue":    ("mám to na jazyku",          "His name is on the tip of my tongue."),
    "cast doubt on":              ("zpochybnit",                 "New evidence cast doubt on the theory."),
    "shed light on":              ("osvětlit, objasnit",         "This research sheds light on the issue."),
    "ring a bell":                ("být povědomý",               "That name rings a bell."),
    "draw a blank":               ("nic si nevybavit",           "I draw a blank when it comes to names."),
    "food for thought":           ("podnět k přemýšlení",        "That's certainly food for thought."),

    # Change / progress
    "turn over a new leaf":       ("začít nový život",           "He turned over a new leaf after prison."),
    "break new ground":           ("být průkopnický",            "Their research breaks new ground."),
    "be at a crossroads":         ("být na křižovatce (v životě)","She's at a crossroads in her career."),
    "go from strength to strength":("nabírat na síle, prosperovat","The company went from strength to strength."),
    "nip in the bud":             ("zlikvidovat v zárodku",      "The problem should be nipped in the bud."),

    # Difficulty / work
    "burn one's bridges":         ("spálit za sebou mosty",      "Don't burn your bridges with that firm."),
    "bite the bullet":            ("skousnout to, vzít to stoicky","Just bite the bullet and apologise."),
    "keep a low profile":         ("nepoutat na sebe pozornost", "He kept a low profile after the scandal."),
    "go the extra mile":          ("udělat více, než se čeká",   "She always goes the extra mile."),
    "bear the brunt of":          ("odnést to nejhůř",           "Small businesses bore the brunt of it."),
    "pass the buck":              ("hodit to na druhého",        "Stop passing the buck — take responsibility."),

    # Communication
    "beat around the bush":       ("chodit kolem horké kaše",    "Stop beating around the bush."),
    "read between the lines":     ("číst mezi řádky",            "If you read between the lines,..."),
    "put one's foot in it":       ("zařídit si do toho",         "I really put my foot in it at dinner."),
    "get straight to the point":  ("jít rovnou k věci",          "Let me get straight to the point."),

    # Decision / action
    "take the bull by the horns": ("vzít býka za rohy",          "It's time to take the bull by the horns."),
    "sit on the fence":           ("sedět na plotě, nerozhodovat se","You can't sit on the fence forever."),
    "take a rain check":          ("odložit na jindy (am.)",     "Can I take a rain check on that?"),
    "cut corners":                ("jít nejsnazší cestou, šidit","They cut corners and the bridge failed."),

    # Success / failure
    "hit the jackpot":            ("trefit jackpot, mít velké štěstí","We hit the jackpot with this contract."),
    "fall flat":                  ("nevyjít, skončit nezdarem",  "The joke fell completely flat."),
    "be a hard act to follow":    ("být těžko nahraditelný",     "The previous CEO was a hard act to follow."),
    "miss the boat":              ("zmeškat příležitost",        "We missed the boat on that investment."),
}

categories = {
    "Thinking & knowledge":   ["on the tip of my tongue","cast doubt on","shed light on","ring a bell","draw a blank","food for thought"],
    "Change & progress":      ["turn over a new leaf","break new ground","be at a crossroads","go from strength to strength","nip in the bud"],
    "Difficulty & work":      ["burn one's bridges","bite the bullet","keep a low profile","go the extra mile","bear the brunt of","pass the buck"],
    "Communication":          ["beat around the bush","read between the lines","put one's foot in it","get straight to the point"],
    "Decision & action":      ["take the bull by the horns","sit on the fence","take a rain check","cut corners"],
    "Success & failure":      ["hit the jackpot","fall flat","be a hard act to follow","miss the boat"],
}

print("=" * 55)
print("  LESSON 52: Advanced Idioms & Fixed Expressions")
print("=" * 55)

for cat, idiom_list in categories.items():
    print(f"\n📚 {cat.upper()}:")
    print("-" * 55)
    for idiom in idiom_list:
        if idiom in IDIOMS_C1:
            meaning, example = IDIOMS_C1[idiom]
            print(f"  '{idiom}'")
            print(f"    = {meaning}")
            print(f"    e.g. {example}\n")

print("\n🎯 QUIZ — meaning in Czech:")
print("-" * 55)
pairs = random.sample(list(IDIOMS_C1.items()), 6)
score = 0
for idiom, (meaning, example) in pairs:
    print(f"  '{idiom}'  →  what does it mean?")
    ans = input("  → ").strip()
    print(f"  ✓ Meaning: {meaning}")
    print(f"     e.g. {example}\n")
    score += 1
print(f"  Reviewed {score} idioms!")

# YOUR TASK:
# 1. Use 8 idioms from this lesson in sentences about your work or life
# 2. Write a short speech using at least 5 idioms naturally (not forced)
# 3. Find 3 of these idioms used in English newspapers this week
