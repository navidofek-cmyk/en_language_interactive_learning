"""
LESSON 47: Cleft Sentences
============================
⭐⭐⭐⭐ Level: B2–C1 | Upper-Intermediate

Rozštěpené věty — důraz na konkrétní část věty.
Topics: it-cleft · wh-cleft · all-cleft · pseudo-cleft
"""
import random

IT_CLEFT = [
    ("Normal:   Tom broke the window.",
     "Cleft:    It was TOM who broke the window.  (not someone else)"),
    ("Normal:   She called me last night.",
     "Cleft:    It was LAST NIGHT that she called me.  (not another time)"),
    ("Normal:   I need your advice.",
     "Cleft:    It's YOUR ADVICE that I need.  (not something else)"),
    ("Normal:   The loud music bothered us.",
     "Cleft:    It was THE LOUD MUSIC that bothered us."),
]

WH_CLEFT = [
    ("Normal:   I want a holiday.",
     "Wh-cleft: What I want is a holiday."),
    ("Normal:   She needs more time.",
     "Wh-cleft: What she needs is more time."),
    ("Normal:   This project requires teamwork.",
     "Wh-cleft: What this project requires is teamwork."),
    ("Normal:   He did was check the figures again.",
     "Wh-cleft: What he did was (to) check the figures again."),
]

ALL_CLEFT = [
    ("All I want is a cup of tea.",       "Vše, co chci, je šálek čaje."),
    ("All she did was smile.",            "Jediné, co udělala, bylo, že se usmála."),
    ("All we need is a bit more time.",   "Vše, co potřebujeme, je trochu více času."),
]

USES = [
    ("Contrast:    It was MARIA who solved it, not Pedro."),
    ("Correction:  It wasn't laziness that caused it — it was poor planning."),
    ("Emphasis:    What I find most surprising is the speed of change."),
    ("Explanation: What happened was (that) the file got corrupted."),
]

print("=" * 55)
print("  LESSON 47: Cleft Sentences")
print("=" * 55)
print("\n  Cleft = split the sentence to put focus on one part.")
print("  Very common in spoken English and journalism.\n")

print("\n📚 IT-CLEFT:  It + be + FOCUS + who/that + rest")
print("-" * 55)
for normal, cleft in IT_CLEFT:
    print(f"  {normal}")
    print(f"  {cleft}\n")

print("\n📚 WH-CLEFT (pseudo-cleft):  What + subject + verb + be + FOCUS")
print("-" * 55)
for normal, wh in WH_CLEFT:
    print(f"  {normal}")
    print(f"  {wh}\n")

print("\n📚 ALL-CLEFT:  All + subject + verb + be + noun/clause")
print("-" * 55)
for en, cz in ALL_CLEFT:
    print(f"  {en}")
    print(f"    → {cz}\n")

print("\n📚 WHEN TO USE CLEFT SENTENCES:")
print("-" * 55)
for use in USES:
    print(f"  • {use}")

print("\n🎯 QUIZ — rewrite as cleft sentence:")
print("-" * 55)
quiz = [
    ("The noise woke me up. (It-cleft — emphasise 'the noise')",
     "It was the noise that woke me up."),
    ("I need more practice. (Wh-cleft)",
     "What I need is more practice."),
    ("She just wants to be understood. (All-cleft)",
     "All she wants is to be understood."),
    ("The deadline caused the stress, not the workload. (It-cleft — correction)",
     "It was the deadline that caused the stress, not the workload."),
]
score = 0
for normal, cleft in quiz:
    print(f"  {normal}")
    ans = input("  → ").strip()
    if ans.lower() == cleft.lower():
        print("  ✓ Correct!\n"); score += 1
    else:
        print(f"  ✗ Answer: {cleft}\n")
print(f"  Score: {score}/4")

# YOUR TASK:
# 1. Write 3 it-cleft sentences emphasising different parts of:
#    "My manager gave me some excellent feedback on Friday."
# 2. Complete these wh-clefts with your own information:
#    "What I enjoy most about English is..."
#    "What I find most difficult is..."
# 3. Write a short paragraph (6 sentences) using at least 2 cleft structures
