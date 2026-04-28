"""
LESSON 50: The Subjunctive
============================
⭐⭐⭐⭐ Level: B2–C1 | Upper-Intermediate

Konjunktiv v angličtině — formální doporučení a přání.
Topics: present subjunctive · were subjunctive · subjunctive phrases
"""

PRESENT_SUBJUNCTIVE = [
    ("It is essential that he BE present.",
     "Je nezbytné, aby byl přítomen.",
     "(not: is present)"),
    ("The committee recommends that she TAKE the position.",
     "Výbor doporučuje, aby tuto pozici přijala.",
     "(not: takes)"),
    ("I suggest that he CONSIDER the options carefully.",
     "Navrhuji, aby pečlivě zvážil možnosti.",
     "(not: considers)"),
    ("It is vital that all participants ARRIVE on time.",
     "Je nezbytné, aby všichni účastníci přijeli včas.",
     "(not: arrives)"),
    ("The doctor recommended that she STOP smoking.",
     "Doktor doporučil, aby přestala kouřit.",
     "(not: stops)"),
    ("It is important that the form BE completed in full.",
     "Je důležité, aby byl formulář kompletně vyplněn.",
     "(passive: be + pp)"),
]

WERE_SUBJUNCTIVE = [
    ("If I were you, I would apply.",
     "Na tvém místě bych se přihlásil/a.",
     "(NOT: If I was you — formal)"),
    ("If she were to accept, that would be great.",
     "Kdyby přijala, bylo by to skvělé.",
     "(hypothetical future)"),
    ("I wish he were here.",
     "Přál/a bych si, aby tu byl.",
     "(wish + were — NOT was in formal)"),
    ("Suppose it were possible — what would you do?",
     "Předpokládejme, že by to bylo možné — co bys dělal/a?",
     ""),
    ("Were it not for her support, I would have quit.",
     "Nebýt její podpory, vzdal/a bych to.",
     "(inversion of subjunctive)"),
]

PHRASES = {
    "I suggest that...":        "suggest + base form (no -s, no to)",
    "I recommend that...":      "recommend + base form",
    "It is essential/vital that...": "essential/vital + base form",
    "It is important that...":  "important + base form",
    "The proposal requires that...": "requires + base form",
    "God save the Queen!":      "fixed expression (no -s)",
    "Be that as it may,...":    "= Whatever the case may be",
    "So be it.":                "= Let it be so. (resignation)",
    "Suffice it to say,...":    "= It is enough to say that...",
    "Come what may,...":        "= Whatever happens",
}

print("=" * 55)
print("  LESSON 50: The Subjunctive")
print("=" * 55)
print("\n  The subjunctive uses the BASE FORM of the verb (no -s, no -ing)")
print("  Used after: suggest, recommend, insist, propose, request,")
print("  demand, require, vital, essential, important that...\n")

print("\n📚 PRESENT SUBJUNCTIVE:")
print("-" * 55)
for en, cz, note in PRESENT_SUBJUNCTIVE:
    print(f"  {en}")
    print(f"    → {cz}  {note}\n")

print("\n📚 WERE-SUBJUNCTIVE (hypothetical):")
print("-" * 55)
for en, cz, note in WERE_SUBJUNCTIVE:
    print(f"  {en}")
    if cz: print(f"    → {cz}")
    if note: print(f"    [{note}]")
    print()

print("\n📚 FIXED PHRASES WITH SUBJUNCTIVE:")
print("-" * 55)
for phrase, note in PHRASES.items():
    print(f"  {phrase:<38} [{note}]")

print("\n📝 BRITISH vs AMERICAN:")
print("-" * 55)
print("  British (more common): It is essential that he SHOULD BE present.")
print("  American (formal):     It is essential that he BE present.")
print("  Both are correct. The 'should' form is more common in British English.\n")

print("\n🎯 QUIZ — correct subjunctive form:")
print("-" * 55)
quiz = [
    ("It is vital that every employee ___ (be) aware of the policy.", "be"),
    ("The judge insisted that the witness ___ (tell) the truth.", "tell"),
    ("If she ___ (be) here, she would know what to do.", "were"),
    ("I recommend that he ___ (consider) all options. (subjunctive)", "consider"),
    ("It is important that the report ___ (submit) by Friday. (passive)", "be submitted"),
]
score = 0
for sentence, answer in quiz:
    print(f"  {sentence}")
    ans = input("  → ").strip()
    if ans.lower() == answer.lower():
        print("  ✓ Correct!\n"); score += 1
    else:
        print(f"  ✗ Answer: {answer}\n")
print(f"  Score: {score}/5")

# YOUR TASK:
# 1. Write 5 sentences using suggest/recommend/insist + subjunctive
# 2. Write a formal recommendation letter using at least 3 subjunctive structures
# 3. Find examples of the subjunctive in formal documents or official reports
