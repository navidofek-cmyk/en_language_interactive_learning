"""
LESSON 43: Register — Formal & Informal
==========================================
⭐⭐⭐ Level: B1–B2 | Pre-Intermediate

Formální vs neformální angličtina — stejná myšlenka, jiný styl.
Topics: formal · informal · neutral · contractions · vocabulary level
"""
import random

REGISTER_PAIRS = [
    ("Formal",                          "Informal"),
    ("I would like to...",              "I want to... / I'd like to..."),
    ("I am writing to enquire...",      "I'm getting in touch about..."),
    ("Please do not hesitate to...",    "Feel free to..."),
    ("I regret to inform you that...",  "I'm sorry to say that..."),
    ("I would be grateful if...",       "Could you... / Can you..."),
    ("I look forward to hearing from you.", "Hope to hear from you soon."),
    ("It is my pleasure to...",         "I'm happy to..."),
    ("Enclosed please find...",         "I've attached..."),
    ("With reference to...",            "About... / Regarding..."),
    ("Commence / Initiate",             "Start / Begin"),
    ("Terminate / Cease",               "Stop / End"),
    ("Require / Request",               "Need / Ask for"),
    ("Assist / Aid",                    "Help"),
    ("Obtain / Acquire",                "Get"),
    ("Sufficient",                      "Enough"),
    ("Approximately",                   "About / Around"),
    ("Subsequently",                    "Then / After that"),
    ("Nevertheless",                    "But / However"),
    ("Furthermore",                     "Also / And"),
    ("In order to",                     "To"),
    ("Due to the fact that",            "Because"),
    ("At this point in time",           "Now"),
    ("In the event that",               "If"),
]

CONTRACTIONS = {
    "Formal (no contractions)":   "Informal (contractions OK)",
    "I am":                       "I'm",
    "It is":                      "It's",
    "We are":                     "We're",
    "I have":                     "I've",
    "I will":                     "I'll",
    "do not":                     "don't",
    "cannot":                     "can't",
    "would not":                  "wouldn't",
    "I would":                    "I'd",
    "they are":                   "they're",
}

REWRITE_EXERCISES = [
    ("Formal → Informal:",
     "I am writing to enquire whether you would be available to meet.",
     "Informal: ___",
     "I'm wondering if you're free to meet."),
    ("Informal → Formal:",
     "Hi! Sorry I can't make it on Monday — I'm really busy.",
     "Formal: ___",
     "Dear [Name], I regret to inform you that I will be unable to attend on Monday due to prior commitments."),
    ("Formal → Informal:",
     "I would be grateful if you could provide further information regarding the matter.",
     "Informal: ___",
     "Could you tell me a bit more about it?"),
]

print("=" * 55)
print("  LESSON 43: Register — Formal & Informal")
print("=" * 55)

print("\n📚 REGISTER COMPARISON:")
print("-" * 55)
print(f"  {'FORMAL':<42} INFORMAL")
print("-" * 55)
for formal, informal in REGISTER_PAIRS[1:]:
    print(f"  {formal:<42} {informal}")

print("\n📚 CONTRACTIONS — formal vs informal:")
print("-" * 55)
print(f"  {'FORMAL (write out fully)':<28} INFORMAL (contractions OK)")
print("-" * 55)
for formal, informal in list(CONTRACTIONS.items())[1:]:
    print(f"  {formal:<28} {informal}")

print("\n📝 KEY RULES:")
print("-" * 55)
print("  FORMAL:")
print("    • No contractions")
print("    • Passive voice preferred ('It has been decided...')")
print("    • Longer, more complex sentences")
print("    • Advanced vocabulary")
print("    • Impersonal tone ('One could argue...')")
print()
print("  INFORMAL:")
print("    • Contractions normal")
print("    • Short, direct sentences")
print("    • Phrasal verbs (find out, come up with, put off)")
print("    • Conversational openers (By the way, Anyway, So...)")
print("    • Ellipsis OK (Going well? instead of How are you going?)")

print("\n💬 REWRITE EXERCISES:")
print("-" * 55)
for label, original, prompt, example in REWRITE_EXERCISES:
    print(f"\n  {label}")
    print(f"  Original: '{original}'")
    ans = input("  Your version: ")
    print(f"  Model answer: '{example}'\n")

print("\n🎯 QUIZ — formal or informal?")
print("-" * 55)
quiz = [
    ("'I can't make it on Friday, sorry!' →",                 "informal"),
    ("'I regret to inform you that I will be unable to attend.' →", "formal"),
    ("'Please find attached the requested documents.' →",     "formal"),
    ("'Just letting you know I've sent the files.' →",        "informal"),
    ("'In order to facilitate the process...' →",             "formal"),
    ("'Hope this helps!' →",                                  "informal"),
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
# 1. Rewrite these in the opposite register (formal ↔ informal):
#    a) "I was wondering if you'd be up for grabbing coffee sometime?"
#    b) "Please be advised that the meeting has been rescheduled."
# 2. Write the same message in 3 registers: text to a friend, email to a manager,
#    formal letter to a company
# 3. Find 5 phrasal verbs from lesson 26 and replace them with formal equivalents
