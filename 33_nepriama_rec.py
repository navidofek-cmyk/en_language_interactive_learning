"""
LESSON 33: Reported Speech
============================
⭐⭐⭐ Level: B1 | Pre-Intermediate

Nepřímá řeč — jak převést přímou řeč do nepřímé.
Topics: tense backshift · reporting verbs · questions · commands
"""
import random

TENSE_BACKSHIFT = [
    ("Present simple",  "→", "Past simple",    "\"I work here.\"",          "He said he worked there."),
    ("Present cont.",   "→", "Past cont.",      "\"I'm leaving.\"",          "She said she was leaving."),
    ("Past simple",     "→", "Past perfect",   "\"I saw him.\"",            "He said he had seen him."),
    ("Present perfect", "→", "Past perfect",   "\"I've finished.\"",        "She said she had finished."),
    ("Will",            "→", "Would",           "\"I'll call you.\"",        "He said he would call me."),
    ("Can",             "→", "Could",           "\"I can help.\"",           "She said she could help."),
    ("Must",            "→", "Had to",          "\"I must go.\"",            "He said he had to go."),
    ("May",             "→", "Might",           "\"It may rain.\"",          "She said it might rain."),
]

PRONOUN_CHANGES = [
    ("I",    "→ he/she"),
    ("we",   "→ they"),
    ("my",   "→ his/her"),
    ("you",  "→ I/they (depends on context)"),
    ("here", "→ there"),
    ("now",  "→ then"),
    ("today","→ that day"),
    ("yesterday","→ the day before"),
    ("tomorrow","→ the next day / the following day"),
    ("this", "→ that"),
]

REPORTING_VERBS = {
    "+ that":    ["say", "tell", "explain", "add", "mention", "claim", "admit",
                  "deny", "promise", "warn", "suggest", "agree"],
    "+ to-inf":  ["ask", "tell", "order", "warn", "advise", "beg", "remind",
                  "invite", "encourage", "forbid"],
    "+ -ing":    ["suggest", "recommend", "admit", "deny", "mention"],
}

EXAMPLES = [
    ('Direct:   "I\'m tired," she said.',
     'Reported:  She said (that) she was tired.'),
    ('Direct:   "We have already eaten," they told us.',
     'Reported:  They told us (that) they had already eaten.'),
    ('Direct:   "Will you come?" he asked.',
     'Reported:  He asked if/whether I would come.'),
    ('Direct:   "Don\'t open the window!" she said.',
     'Reported:  She told me not to open the window.'),
    ('Direct:   "Why did you leave?" he asked.',
     'Reported:  He asked why I had left.'),
]

print("=" * 55)
print("  LESSON 33: Reported Speech")
print("=" * 55)

print("\n📚 TENSE BACKSHIFT:")
print("-" * 55)
print(f"  {'Direct':<20} {'→':<4} {'Reported':<20} {'Example'}")
print("-" * 55)
for t1, arrow, t2, direct, reported in TENSE_BACKSHIFT:
    print(f"  {t1:<20} {arrow:<4} {t2:<20}")
    print(f"    {direct} → {reported}\n")

print("\n📚 WORD / PRONOUN CHANGES:")
print("-" * 55)
for original, change in PRONOUN_CHANGES:
    print(f"  {original:<12} {change}")

print("\n📚 REPORTING QUESTIONS:")
print("-" * 55)
print("  Yes/No question → if / whether:")
print('    "Are you ready?" → She asked if I was ready.')
print()
print("  WH-question → same wh-word, normal word order:")
print('    "Where do you live?" → He asked where I lived.')
print('    ⚠️  No question mark, no auxiliary do/does/did in reported questions')

print("\n📚 REPORTING COMMANDS:")
print("-" * 55)
print('  "Sit down!" → She told me TO sit down.')
print('  "Don\'t be late!" → He told her NOT TO be late.')
print('  "Please help me." → She asked me TO help her.')

print("\n📚 REPORTING VERBS:")
print("-" * 55)
for pattern, verbs in REPORTING_VERBS.items():
    print(f"  {pattern:<14} {', '.join(verbs)}")

print("\n💬 EXAMPLES:")
print("-" * 55)
for direct, reported in EXAMPLES:
    print(f"  {direct}")
    print(f"  {reported}\n")

print("\n🎯 QUIZ — convert to reported speech:")
print("-" * 55)
quiz = [
    ('"I am very happy," she said.',            "She said (that) she was very happy."),
    ('"We will arrive tomorrow," they said.',   "They said (that) they would arrive the next day."),
    ('"Have you seen my keys?" he asked.',      "He asked if/whether I had seen his keys."),
    ('"Don\'t touch that!" she warned.',        "She warned me not to touch that."),
    ('"Where does she work?" he asked.',        "He asked where she worked."),
]
score = 0
for direct, answer in quiz:
    print(f"  {direct}")
    ans = input("  → ").strip()
    if ans.lower() == answer.lower():
        print("  ✓ Correct!\n"); score += 1
    else:
        print(f"  ✗ Answer: {answer}\n")
print(f"  Score: {score}/5")

# YOUR TASK:
# 1. Report what someone said to you recently (5 sentences)
# 2. Convert this dialogue to reported speech:
#    A: "Are you coming to the meeting?"
#    B: "I can't — I have to finish this report."
#    A: "Please try. It's important."
# 3. Write a news article reporting what a politician said (use varied reporting verbs)
