"""
LESSON 59: Discourse Markers & Linking Language
==================================================
⭐⭐⭐⭐ Level: B2–C1 | Upper-Intermediate

Diskurzní markery — spojky a přechodové výrazy pro plynulý text.
Topics: spoken · written · contrast · addition · result · position
"""
import random

DISCOURSE_MARKERS = {
    "Addition": {
        "simple":   ["also", "too", "as well", "besides"],
        "formal":   ["furthermore", "moreover", "in addition", "what is more",
                     "not only... but also", "additionally"],
    },
    "Contrast": {
        "simple":   ["but", "however", "although", "even though", "while"],
        "formal":   ["nevertheless", "nonetheless", "on the other hand",
                     "in contrast", "notwithstanding", "despite this",
                     "that said", "be that as it may", "yet"],
    },
    "Cause & Result": {
        "simple":   ["so", "because", "as", "since"],
        "formal":   ["therefore", "consequently", "as a result", "hence",
                     "thus", "for this reason", "this led to",
                     "owing to", "due to the fact that"],
    },
    "Concession": {
        "simple":   ["although", "though", "even if"],
        "formal":   ["admittedly", "granted", "it is true that",
                     "while it cannot be denied that", "despite + noun",
                     "in spite of + noun"],
    },
    "Exemplification": {
        "simple":   ["for example", "for instance", "like", "such as"],
        "formal":   ["to illustrate", "a case in point is",
                     "this is exemplified by", "notably"],
    },
    "Summary": {
        "simple":   ["in short", "to sum up", "basically"],
        "formal":   ["in conclusion", "to conclude", "in summary",
                     "on balance", "taking everything into account",
                     "all things considered"],
    },
    "Clarification": {
        "simple":   ["I mean", "that is", "in other words"],
        "formal":   ["that is to say", "to put it another way",
                     "in other words", "to clarify", "to be more precise"],
    },
    "Attitude": {
        "spoken":   ["honestly", "frankly", "to be honest", "personally"],
        "written":  ["it is worth noting", "it should be emphasised",
                     "it is significant that", "arguably"],
    },
}

POSITION_RULES = [
    ("Beginning of sentence", "Furthermore, the results were inconclusive.",  "comma after"),
    ("Middle of sentence",    "The results, moreover, were inconclusive.",    "commas around"),
    ("After semicolon",       "The plan failed; nevertheless, we persisted.", "semicolon before"),
    ("Subordinate clause",    "Although the plan failed, we persisted.",      "comma after clause"),
]

print("=" * 55)
print("  LESSON 59: Discourse Markers & Linking Language")
print("=" * 55)

for category, levels in DISCOURSE_MARKERS.items():
    print(f"\n📚 {category.upper()}:")
    print("-" * 55)
    for level, markers in levels.items():
        print(f"  [{level}] {' · '.join(markers)}")

print("\n📝 PUNCTUATION & POSITION:")
print("-" * 55)
for position, example, rule in POSITION_RULES:
    print(f"  {position}:")
    print(f"    {example}  [{rule}]\n")

print("\n📝 COMMON MISTAKES:")
print("-" * 55)
mistakes = [
    ("Despite + noun:   ✓ Despite the rain,... ✗ Despite it rained,..."),
    ("Although + clause: ✓ Although it rained,... ✗ Although the rain,..."),
    ("Nevertheless ≠ despite: both mean contrast but different grammar"),
    ("'However' at end of sentence needs comma: He agreed, however."),
    ("'Moreover' sounds unnatural in speech — use 'also' or 'what's more'"),
]
for m in mistakes:
    print(f"  • {m}")

print("\n💬 PARAGRAPH WITH DISCOURSE MARKERS:")
print("-" * 55)
print("""  Remote working has become increasingly prevalent in recent years.
  On the one hand, it offers employees greater flexibility; consequently,
  job satisfaction tends to increase. Furthermore, companies benefit from
  reduced overhead costs. Nevertheless, there are significant drawbacks.
  Despite the advantages, many workers report feelings of isolation.
  In addition, collaboration can suffer. All things considered, a hybrid
  model appears to offer the most balanced solution.""")

print("\n🎯 QUIZ — choose the correct discourse marker:")
print("-" * 55)
quiz = [
    ("The results were positive. ___, the cost was too high. (contrast)", "However / Nevertheless"),
    ("___ the bad weather, the event was a success. (concession)", "Despite"),
    ("She studied hard. ___, she passed with distinction. (result)", "As a result / Consequently"),
    ("___ it cannot be denied that progress has been slow,... (concession)", "Admittedly / Granted"),
    ("___ to illustrate this point, consider the case of... (exemplification)", "To / In order"),
]
score = 0
for sentence, answer in quiz:
    print(f"  {sentence}")
    ans = input("  → ").strip()
    if any(a.strip().lower() in ans.lower() for a in answer.split("/")):
        print("  ✓ Correct!\n"); score += 1
    else:
        print(f"  ✗ Answer: {answer}\n")
print(f"  Score: {score}/5")

# YOUR TASK:
# 1. Rewrite this paragraph adding at least 5 discourse markers:
#    "Social media is popular. It has benefits. It has drawbacks.
#     Young people use it a lot. It affects their mental health."
# 2. Write a paragraph arguing a point, using markers from each category
# 3. Read a quality English article and highlight all discourse markers you find
