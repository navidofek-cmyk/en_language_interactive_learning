"""
LESSON 49: Participle Clauses
================================
⭐⭐⭐⭐ Level: B2–C1 | Upper-Intermediate

Participiální věty — kompaktnější, formálnější vyjádření.
Topics: present participle · past participle · perfect participle · position
"""
import random

TYPES = {
    "Present participle (-ing)": {
        "use":      "Active action, simultaneous or causal",
        "examples": [
            ("Seeing the danger, she stopped immediately.",
             "Když uviděla nebezpečí, okamžitě zastavila.",
             "= When she saw the danger, she stopped."),
            ("Not knowing what to say, he just smiled.",
             "Nevědě, co říct, jen se usmál.",
             "= Because he didn't know what to say, he smiled."),
            ("She sat at her desk, reading a report.",
             "Seděla u stolu a četla zprávu.",
             "= She sat at her desk and read a report."),
            ("The train arriving on platform 3 is delayed.",
             "Vlak přijíždějící na nástupiště 3 má zpoždění.",
             "= The train which is arriving on platform 3..."),
        ],
    },
    "Past participle (-ed/irregular)": {
        "use":      "Passive meaning",
        "examples": [
            ("Disappointed by the result, he resigned.",
             "Zklamaný výsledkem, podal výpověď.",
             "= Because he was disappointed by the result, he resigned."),
            ("The documents, signed by the manager, were sent.",
             "Dokumenty, podepsané manažerem, byly odeslány.",
             "= The documents, which were signed by the manager, were sent."),
            ("Given the circumstances, this was the right decision.",
             "Vzhledem k okolnostem to bylo správné rozhodnutí.",
             "= Given that these were the circumstances..."),
        ],
    },
    "Perfect participle (having + pp)": {
        "use":      "Action completed before the main clause",
        "examples": [
            ("Having finished the report, she went home.",
             "Poté, co dokončila zprávu, šla domů.",
             "= After she had finished the report, she went home."),
            ("Having lived in London for years, she knows it well.",
             "Poté, co léta žila v Londýně, dobře ho zná.",
             "= Because she has lived in London for years, she knows it well."),
            ("Not having eaten all day, he was starving.",
             "Poté, co celý den nejedl, byl vyhladovělý.",
             "= Because he hadn't eaten all day, he was starving."),
        ],
    },
}

print("=" * 55)
print("  LESSON 49: Participle Clauses")
print("=" * 55)
print("\n  Participle clauses replace subordinate clauses.")
print("  More formal, more concise — common in writing and speeches.\n")
print("  ⚠️  The subject of both clauses MUST be the same:")
print("  ✗ Walking down the street, the rain started.")
print("    (rain didn't walk — the subject changed)")
print("  ✓ Walking down the street, I got soaked.\n")

for ptype, data in TYPES.items():
    print(f"\n📚 {ptype.upper()}:")
    print(f"  Use: {data['use']}")
    print("-" * 55)
    for en, cz, equiv in data["examples"]:
        print(f"  {en}")
        print(f"    → {cz}")
        print(f"    ≈ {equiv}\n")

print("\n🎯 QUIZ — rewrite using a participle clause:")
print("-" * 55)
quiz = [
    ("Because she was exhausted, she went straight to bed.",
     "Exhausted, she went straight to bed."),
    ("After he had checked the figures, he submitted the report.",
     "Having checked the figures, he submitted the report."),
    ("Because we don't know the answer, we can't proceed.",
     "Not knowing the answer, we can't proceed."),
    ("The letter, which was written in 1918, is now in a museum.",
     "The letter, written in 1918, is now in a museum."),
]
score = 0
for long_form, short_form in quiz:
    print(f"  {long_form}")
    ans = input("  → ").strip()
    if ans.lower() == short_form.lower():
        print("  ✓ Correct!\n"); score += 1
    else:
        print(f"  ✗ Answer: {short_form}\n")
print(f"  Score: {score}/4")

# YOUR TASK:
# 1. Rewrite these using participle clauses:
#    a) Because she had worked for 12 hours, she was exhausted.
#    b) The man who was standing at the door was a detective.
#    c) After I had read the email, I called my manager.
# 2. Write a short news report (8 sentences) using at least 3 participle clauses
# 3. Find 5 participle clauses in a newspaper article
