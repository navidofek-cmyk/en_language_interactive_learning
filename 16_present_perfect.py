"""
LESSON 16: Present Perfect
============================
⭐⭐ Level: A2–B1 | Elementary–Pre-Intermediate

Předpřítomný čas — spojení minulosti s přítomností.
Topics: have/has + past participle · ever/never · already/yet · for/since
"""
import random

IRREGULAR_PP = {
    "be":    "been",   "have":  "had",    "go":    "gone/been",
    "see":   "seen",   "do":    "done",   "make":  "made",
    "get":   "got",    "give":  "given",  "take":  "taken",
    "come":  "come",   "know":  "known",  "think": "thought",
    "write": "written","read":  "read",   "speak": "spoken",
    "eat":   "eaten",  "drink": "drunk",  "buy":   "bought",
    "find":  "found",  "lose":  "lost",   "meet":  "met",
    "say":   "said",   "tell":  "told",   "win":   "won",
    "break": "broken", "fall":  "fallen", "grow":  "grown",
}

USES = [
    ("Life experience (with ever/never)",
     "Have you ever been to London?",
     "Byl/a jsi někdy v Londýně?"),
    ("Result in the present",
     "I've lost my keys. (= I don't have them now)",
     "Ztratil/a jsem klíče. (teď je nemám)"),
    ("Unfinished time period (today, this week)",
     "I haven't eaten anything today.",
     "Dnes jsem nic nejedl/a."),
    ("With just / already / yet",
     "She has just arrived. / Have you finished yet?",
     "Právě přijela. / Už jsi skončil/a?"),
    ("With for / since",
     "I've lived here for 5 years / since 2019.",
     "Bydlím tady 5 let / od roku 2019."),
]

print("=" * 55)
print("  LESSON 16: Present Perfect")
print("=" * 55)

print("\n📚 FORM:  have/has + past participle")
print("-" * 55)
print("  I/you/we/they  HAVE worked / been / seen")
print("  he/she/it      HAS  worked / been / seen")
print()
print("  (−) I haven't seen him.   She hasn't called.")
print("  (?) Have you eaten?       Has he left?")

print("\n📚 COMMON IRREGULAR PAST PARTICIPLES:")
print("-" * 55)
irr = list(IRREGULAR_PP.items())
for i in range(0, len(irr), 3):
    row = irr[i:i+3]
    print("  " + "   ".join(f"{b:<8} → {p:<10}" for b, p in row))

print("\n📚 WHEN TO USE IT:")
print("-" * 55)
for use, en, cz in USES:
    print(f"  [{use}]")
    print(f"  {en}")
    print(f"    → {cz}\n")

print("\n📝 PRESENT PERFECT vs. PAST SIMPLE:")
print("-" * 55)
print("  Present perfect → connection to NOW, no specific time")
print("  Past simple     → finished time, specific moment\n")
pairs = [
    ("I've seen that film.",         "I saw that film last week."),
    ("She has lived here for years.", "She lived here in 2010."),
    ("Have you eaten yet?",          "Did you eat at the party?"),
]
for pp, ps in pairs:
    print(f"  ✓ {pp:<40} (present perfect)")
    print(f"  ✓ {ps:<40} (past simple)\n")

print("\n📝 KEY TIME EXPRESSIONS:")
print("-" * 55)
exprs = {
    "ever":    "někdy (in questions)",
    "never":   "nikdy",
    "just":    "právě",
    "already": "už (affirmative)",
    "yet":     "ještě/už (questions & negatives)",
    "for":     "po dobu (for 3 years)",
    "since":   "od (since Monday / 2020)",
    "recently":"nedávno",
    "so far":  "zatím",
}
for en, cz in exprs.items():
    print(f"  {en:<12} {cz}")

print("\n🎯 QUIZ — present perfect or past simple?")
print("-" * 55)
quiz = [
    ("___ you ever ___ (be) to Japan?",                 "Have ... been"),
    ("I ___ (not/see) him since last Monday.",           "haven't seen"),
    ("She ___ (finish) the report an hour ago.",         "finished"),
    ("We ___ (live) here for ten years.",                "have lived / 've lived"),
    ("___ (you/eat) breakfast yet?",                     "Have you eaten"),
    ("He ___ (break) his leg in 2022.",                  "broke"),
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
# 1. Write 5 sentences about your life experiences using 'ever/never'
# 2. Write 3 sentence pairs showing the difference between
#    present perfect and past simple
# 3. Describe what you have done today using present perfect
