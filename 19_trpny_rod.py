"""
LESSON 19: Passive Voice
==========================
⭐⭐⭐ Level: B1 | Pre-Intermediate

Trpný rod — kdy a jak ho použít.
Topics: be + past participle · tenses in passive · by-agent · causative
"""
import random

PASSIVE_FORMS = [
    ("Present simple",  "is/are + PP",          "English is spoken worldwide."),
    ("Past simple",     "was/were + PP",         "The bridge was built in 1890."),
    ("Present perfect", "has/have been + PP",    "The email has been sent."),
    ("Past perfect",    "had been + PP",         "The report had been finished."),
    ("Future will",     "will be + PP",          "The results will be announced tomorrow."),
    ("Modal",           "modal + be + PP",       "The form must be completed online."),
    ("Present cont.",   "is/are being + PP",     "The road is being repaired."),
]

ACTIVE_TO_PASSIVE = [
    ("Active:  They build cars here.",
     "Passive: Cars are built here."),
    ("Active:  Someone stole my wallet.",
     "Passive: My wallet was stolen."),
    ("Active:  The chef is cooking dinner.",
     "Passive: Dinner is being cooked."),
    ("Active:  We will finish the project next week.",
     "Passive: The project will be finished next week."),
    ("Active:  They have cancelled the flight.",
     "Passive: The flight has been cancelled."),
]

WHEN_TO_USE = [
    "When the agent (doer) is unknown or unimportant",
    "In formal writing (reports, news, science)",
    "To emphasise the result/object rather than who did it",
    "When you don't want to say who did something",
]

print("=" * 55)
print("  LESSON 19: Passive Voice")
print("=" * 55)

print("\n📚 FORM:  be (conjugated) + past participle")
print("-" * 55)
for tense, form, example in PASSIVE_FORMS:
    print(f"  {tense:<20} {form:<22} {example}")

print("\n📚 ACTIVE → PASSIVE:")
print("-" * 55)
for active, passive in ACTIVE_TO_PASSIVE:
    print(f"  {active}")
    print(f"  {passive}\n")

print("\n📝 WHEN TO USE PASSIVE:")
print("-" * 55)
for reason in WHEN_TO_USE:
    print(f"  • {reason}")

print("\n📝 'BY' — naming the agent:")
print("-" * 55)
print("  The painting was created BY Picasso.")
print("  The window was broken BY the wind.")
print("  (Omit 'by' when agent is obvious or unimportant)")

print("\n📝 CAUSATIVE — have/get something done:")
print("-" * 55)
print("  I had my car repaired.   (nechal jsem si opravit auto)")
print("  She got her hair cut.    (nechala si ostříhat vlasy)")
print("  We're having the house painted. (necháváme si natřít dům)")

print("\n🎯 QUIZ — rewrite in passive:")
print("-" * 55)
quiz = [
    ("They speak French in Quebec. →", "French is spoken in Quebec."),
    ("Someone broke the window. →", "The window was broken."),
    ("They are building a new hospital. →", "A new hospital is being built."),
    ("You must sign the form. →", "The form must be signed."),
    ("They have delivered the package. →", "The package has been delivered."),
]
score = 0
for question, answer in quiz:
    print(f"  {question}")
    ans = input("  → ").strip()
    if ans.lower() == answer.lower():
        print("  ✓ Correct!\n"); score += 1
    else:
        print(f"  ✗ Answer: {answer}\n")
print(f"  Score: {score}/5")

# YOUR TASK:
# 1. Rewrite these active sentences in passive:
#    a) Agatha Christie wrote 'And Then There Were None.'
#    b) They will announce the winner on Friday.
#    c) Someone has hacked my account.
# 2. Find 5 passive sentences in a news article
# 3. Write a short paragraph about how your favourite food is made
#    using passive voice
