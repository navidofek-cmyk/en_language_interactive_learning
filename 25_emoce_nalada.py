"""
LESSON 25: Emotions & Feelings
================================
⭐⭐ Level: A2–B1 | Elementary

Emoce, pocity a jak je vyjádřit přirozeně.
Topics: emotions · expressing feelings · -ed vs -ing adjectives · intensifiers
"""
import random

EMOTIONS = {
    "happy":       "šťastný/á",     "sad":         "smutný/á",
    "angry":       "naštvaný/á",    "excited":     "nadšený/á",
    "nervous":     "nervózní",      "scared":      "vystrašený/á",
    "worried":     "znepokojený/á", "surprised":   "překvapený/á",
    "bored":       "znuděný/á",     "tired":       "unavený/á",
    "relaxed":     "uvolněný/á",    "stressed":    "vystresovaný/á",
    "proud":       "hrdý/á",        "ashamed":     "zastyděný/á",
    "jealous":     "žárlivý/á",     "lonely":      "osamělý/á",
    "frustrated":  "frustrovaný/á", "grateful":    "vděčný/á",
    "confident":   "sebejistý/á",   "confused":    "zmatený/á",
    "disappointed":"zklamaný/á",    "relieved":    "ulevilo se mi",
    "disgusted":   "znechucený/á",  "embarrassed": "v rozpacích",
}

ED_ING = [
    ("bored",        "boring",       "I'm bored.",          "The film is boring."),
    ("excited",      "exciting",     "She's excited.",      "The news is exciting."),
    ("tired",        "tiring",       "I'm tired.",          "The journey is tiring."),
    ("interested",   "interesting",  "He's interested.",    "The book is interesting."),
    ("frightened",   "frightening",  "I'm frightened.",     "The dog is frightening."),
    ("surprised",    "surprising",   "We're surprised.",    "The result is surprising."),
    ("disappointed", "disappointing","I'm disappointed.",   "The film is disappointing."),
]

INTENSIFIERS = {
    "a bit":        "trochu",         "quite":      "docela",
    "rather":       "poměrně / docela","very":       "velmi",
    "really":       "opravdu",        "extremely":  "nesmírně",
    "absolutely":   "naprosto (strong adj.)", "totally": "úplně",
}

EXPRESSING_FEELINGS = {
    "I feel really ...":          "Cítím se opravdu ...",
    "I'm a bit ...":              "Jsem trochu ...",
    "I can't help feeling ...":   "Nemohu se zbavit pocitu ...",
    "I'm over the moon!":         "Jsem nadšený/á (šťastný/á na sedmém nebi)!",
    "I'm gutted.":                "Jsem zdrcený/á.",
    "It gets on my nerves.":      "Jde mi to na nervy.",
    "I'm fed up with ...":        "Mám dost ...",
    "That makes me so happy.":    "To mě tak potěšuje.",
    "I'm not in the mood for ...":"Nemám náladu na ...",
}

print("=" * 55)
print("  LESSON 25: Emotions & Feelings")
print("=" * 55)

print("\n📚 EMOTIONS:")
print("-" * 55)
items = list(EMOTIONS.items())
for i in range(0, len(items), 2):
    row = items[i:i+2]
    print("  " + "   ".join(f"{en:<16}{cz:<22}" for en, cz in row))

print("\n📚 -ED vs -ING ADJECTIVES:")
print("-" * 55)
print("  -ED   = how a person FEELS")
print("  -ING  = what causes the feeling\n")
print(f"  {'Person feels (-ed)':<24} {'Thing causes it (-ing)'}")
print("-" * 55)
for ed, ing, ex_ed, ex_ing in ED_ING:
    print(f"  {ex_ed:<36} {ex_ing}")

print("\n📚 INTENSIFIERS:")
print("-" * 55)
for en, cz in INTENSIFIERS.items():
    print(f"  {en:<16} {cz}")
print()
print("  Note: 'absolutely' is used with extreme adjectives:")
print("  absolutely terrified / thrilled / exhausted (not: absolutely tired)")

print("\n📚 NATURAL EXPRESSIONS:")
print("-" * 55)
for en, cz in EXPRESSING_FEELINGS.items():
    print(f"  {en:<34} {cz}")

print("\n🎯 QUIZ — -ed or -ing?")
print("-" * 55)
quiz = [
    ("The homework was really ___ (bore).",           "boring"),
    ("I was ___ (surprise) by the ending.",           "surprised"),
    ("The lecture was quite ___ (interest).",         "interesting"),
    ("She felt ___ (embarrass) when she forgot.",     "embarrassed"),
    ("Skydiving sounds absolutely ___ (terrify).",    "terrifying"),
    ("He was ___ (disappoint) with his exam results.","disappointed"),
]
score = 0
for sentence, answer in quiz:
    print(f"  {sentence}")
    ans = input("  → ").strip()
    if ans.lower() == answer.lower():
        print("  ✓ Correct!\n"); score += 1
    else:
        print(f"  ✗ Answer: {answer}\n")
print(f"  Score: {score}/6")

# YOUR TASK:
# 1. Describe how you feel right now using 3 different emotions + intensifiers
# 2. Write about a time you felt very proud or very disappointed
# 3. Write 6 sentences using -ed and -ing adjectives (one pair each)
