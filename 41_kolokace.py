"""
LESSON 41: Collocations
=========================
⭐⭐⭐ Level: B1–B2 | Pre-Intermediate

Kolokace — které slova přirozeně patří k sobě.
Topics: make/do · have/take · strong adjectives · verb + noun collocations
"""
import random

MAKE_DO = {
    "make": [
        "a decision", "a mistake", "progress", "an effort", "a suggestion",
        "a phone call", "an appointment", "money", "a noise", "a difference",
        "friends", "a complaint", "a comment", "a speech", "plans",
        "breakfast/lunch/dinner", "a profit", "an exception", "sense",
    ],
    "do": [
        "homework", "the shopping", "the washing-up", "research", "business",
        "someone a favour", "your best", "damage", "harm", "good",
        "the housework", "exercise", "a course", "a job", "nothing",
        "well/badly", "your hair", "the ironing", "overtime",
    ],
}

HAVE_TAKE = {
    "have": [
        "a break", "a shower", "a meeting", "a look", "a problem",
        "an argument", "a conversation", "a drink", "a meal", "fun",
        "a rest", "a headache", "a baby", "a good time", "an idea",
    ],
    "take": [
        "a photo", "a taxi", "a risk", "a break", "an exam",
        "a decision", "responsibility", "notes", "turns", "medicine",
        "a step", "advantage", "part in", "place", "time",
    ],
}

STRONG_ADJECTIVES = {
    "very good":       "excellent, outstanding, superb, brilliant, exceptional",
    "very bad":        "terrible, awful, dreadful, appalling, disastrous",
    "very big":        "enormous, massive, huge, vast, gigantic",
    "very small":      "tiny, miniature, microscopic, minuscule",
    "very tired":      "exhausted, drained, shattered, worn out",
    "very surprised":  "astonished, astounded, stunned, gobsmacked",
    "very angry":      "furious, livid, outraged, incensed",
    "very happy":      "thrilled, delighted, ecstatic, overjoyed",
    "very cold":       "freezing, icy, bitter, arctic",
    "very hot":        "boiling, sweltering, scorching, blazing",
    "very dirty":      "filthy, disgusting, grimy",
    "very clean":      "spotless, immaculate, pristine",
    "very hungry":     "starving, famished, ravenous",
    "very funny":      "hilarious, side-splitting",
    "very scared":     "terrified, petrified, horrified",
}

print("=" * 55)
print("  LESSON 41: Collocations")
print("=" * 55)

print("\n📚 MAKE vs DO — common collocations:")
print("-" * 55)
print("  MAKE = create, produce / DO = activity, task\n")
for verb, nouns in MAKE_DO.items():
    print(f"  {verb.upper()}: {', '.join(nouns)}\n")

print("\n📚 HAVE vs TAKE:")
print("-" * 55)
for verb, nouns in HAVE_TAKE.items():
    print(f"  {verb.upper()}: {', '.join(nouns)}\n")

print("\n📚 STRONG ADJECTIVES (replace 'very + basic adj.'):")
print("-" * 55)
print("  ⚠️  Don't say 'very' before strong adjectives:")
print("  ✓ absolutely exhausted  (NE: very exhausted)")
print("  ✓ completely freezing   (NE: very freezing)\n")
for basic, strong in STRONG_ADJECTIVES.items():
    print(f"  {basic:<22} → {strong}")

print("\n🎯 QUIZ — make or do?")
print("-" * 55)
make_quiz = random.sample(MAKE_DO["make"], 4)
do_quiz   = random.sample(MAKE_DO["do"], 4)
all_quiz  = [(n, "make") for n in make_quiz] + [(n, "do") for n in do_quiz]
random.shuffle(all_quiz)
score = 0
for noun, answer in all_quiz[:8]:
    ans = input(f"  ___ {noun}  →  make or do? ").strip()
    if ans.lower() == answer.lower():
        print("  ✓ Correct!\n"); score += 1
    else:
        print(f"  ✗ Answer: {answer}\n")
print(f"  Score: {score}/8")

print("\n🎯 QUIZ — strong adjective:")
print("-" * 55)
basics = random.sample(list(STRONG_ADJECTIVES.items()), 4)
for basic, strong in basics:
    print(f"  Another word for '{basic}'?")
    ans = input("  → ").strip()
    print(f"  ✓ Options: {strong}\n")

# YOUR TASK:
# 1. Write 10 sentences using make/do collocations from your daily life
# 2. Replace the underlined weak adjective with a strong one:
#    "The film was very bad. The acting was very good. I was very tired afterwards."
# 3. Write a short paragraph about a bad day using strong adjectives
