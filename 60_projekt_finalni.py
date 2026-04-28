"""
LESSON 60: Final Project — C1 Showcase
=========================================
⭐⭐⭐⭐⭐ Level: C1 | Advanced

Finální projekt: demonstrace všech dovedností kurzu.
Combines: all tenses · advanced grammar · vocabulary · style · register
"""

TASKS = {
    "1. Written Essay (250 words)": {
        "prompt":   "Technology is making human interaction increasingly unnecessary. "
                    "To what extent do you agree with this statement?",
        "checklist":[
            "Clear thesis in introduction",
            "2 body paragraphs with topic sentences",
            "Evidence / examples in each paragraph",
            "Counterargument acknowledged",
            "Formal register throughout",
            "Advanced vocabulary (academic word list)",
            "Variety of grammar structures (passive, cleft, conditionals)",
            "Discourse markers used effectively",
            "Conclusion restates thesis (in different words)",
        ],
    },
    "2. Formal Email (150 words)": {
        "prompt":   "Write to a professional conference to: enquire about speaking opportunities, "
                    "outline your expertise briefly, and request a brochure.",
        "checklist":[
            "Correct opening (Dear Mr/Ms + surname)",
            "State purpose in first sentence",
            "No contractions",
            "Formal vocabulary",
            "Polite request phrasing",
            "Formal closing + full name",
        ],
    },
    "3. Opinion Piece (200 words)": {
        "prompt":   "Write a short opinion piece for a magazine about whether cities should "
                    "ban private cars from their centres.",
        "checklist":[
            "Engaging opening sentence",
            "Clear position stated early",
            "Arguments supported by examples",
            "Acknowledge the opposite view",
            "Confident, persuasive conclusion",
            "Semi-formal register appropriate for magazine",
        ],
    },
    "4. Short Story Opening (150 words)": {
        "prompt":   "Write the opening of a story that begins: "
                    "'The last train had already left when she noticed the envelope.'",
        "checklist":[
            "All 3 narrative tenses used",
            "Vivid, sensory language",
            "Short sentences for tension",
            "Character established quickly",
            "Reader hooked — want to read more",
        ],
    },
}

C1_GRAMMAR_CHECKLIST = [
    "✓ Inversion after negative adverbials (Never have I...)",
    "✓ Cleft sentences (What I found was... / It was X that...)",
    "✓ Participle clauses (Having finished..., Exhausted,...)",
    "✓ Mixed conditionals (If I had..., I would be...)",
    "✓ Subjunctive (It is vital that he be...)",
    "✓ Wish / If only (I wish I had... / If only she were...)",
    "✓ Reporting verbs (She claimed/admitted/acknowledged...)",
    "✓ Advanced passives (have sth done, it is claimed that...)",
    "✓ Relative clauses — defining & non-defining",
    "✓ Gerunds vs infinitives with meaning changes",
]

C1_VOCABULARY_CHECKLIST = [
    "✓ Academic word list (analyse, assess, demonstrate...)",
    "✓ Advanced collocations (raise awareness, strike a balance...)",
    "✓ Discourse markers (nevertheless, consequently, notwithstanding...)",
    "✓ Hedging language (it appears, there is a tendency to...)",
    "✓ Strong adjectives (exhausted, appalling, meticulous...)",
    "✓ Formal vs informal register distinction",
    "✓ Advanced phrasal verbs (account for, boil down to...)",
    "✓ C1 idioms (cast doubt on, shed light on...)",
]

print("=" * 55)
print("  LESSON 60: Final Project — C1 Showcase")
print("=" * 55)
print("\n  Congratulations on reaching Lesson 60!")
print("  This final lesson tests everything you have learned.\n")

print("\n📚 C1 GRAMMAR CHECKLIST:")
print("-" * 55)
for item in C1_GRAMMAR_CHECKLIST:
    print(f"  {item}")

print("\n📚 C1 VOCABULARY CHECKLIST:")
print("-" * 55)
for item in C1_VOCABULARY_CHECKLIST:
    print(f"  {item}")

for task_name, task_data in TASKS.items():
    print(f"\n{'=' * 55}")
    print(f"  {task_name}")
    print("=" * 55)
    print(f"\n  Prompt: {task_data['prompt']}\n")
    print("  Checklist:")
    for item in task_data["checklist"]:
        print(f"    ☐ {item}")
    print()
    print("  Write your response (press Enter twice to finish):")
    lines = []
    while True:
        line = input("  ")
        if line == "" and lines and lines[-1] == "":
            break
        lines.append(line)
    if any(l.strip() for l in lines):
        print(f"\n  Your {task_name}:")
        print("-" * 55)
        for line in lines:
            if line: print(f"  {line}")
        print()

print("=" * 55)
print("  🏆 COURSE COMPLETE!")
print("=" * 55)
print("""
  You have completed the English Interactive Course.

  What next?
  • Take an official exam: IELTS, Cambridge C1 Advanced (CAE), TOEFL
  • Read quality English daily: The Guardian, The Economist, BBC News
  • Listen: BBC Radio 4, TED Talks, podcasts on topics you enjoy
  • Speak: find a language exchange partner at italki.com or Tandem
  • Write: keep a journal in English, comment on articles, write reviews
  • Review: run python3 flashkarty.py daily for 10 minutes

  The difference between B2 and C1 is EXPOSURE and PRACTICE.
  You now have the tools. Use them every day.

  python3 streak.py    ← keep your streak alive
  python3 flashkarty.py ← review vocabulary daily
""")

# FINAL TASK:
# Record yourself speaking on the essay topic for 3 minutes.
# Listen back and note:
#   1. Grammar mistakes
#   2. Vocabulary you wish you had used
#   3. Pronunciation issues
# Then write the essay and compare spoken vs written expression.
