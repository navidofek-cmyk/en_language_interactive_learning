"""
ARTICLE 02: The Rise of Remote Work
======================================
⭐⭐⭐ Level: B1 | Pre-Intermediate

Přečti si článek o práci na dálku a odpověz na otázky.
Topics: work · technology · advantages/disadvantages · present perfect
"""

ARTICLE = """
THE RISE OF REMOTE WORK

Before 2020, working from home was a privilege enjoyed by only a small
percentage of the workforce. Then the COVID-19 pandemic changed everything.
Almost overnight, millions of people around the world were forced to work
from their homes. What began as a temporary emergency measure has become,
for many, a permanent way of working.

The advantages of remote work are well-documented. Employees save time and
money by not commuting. Many report higher productivity, fewer interruptions,
and a better work-life balance. Companies benefit from lower office costs and
access to a global talent pool — geography no longer limits who they can hire.

However, remote work is not without its challenges. Many workers struggle with
isolation and the blurring of boundaries between work and home life.
Collaboration can suffer when teams are not physically together. Junior
employees, in particular, miss out on the informal learning and mentoring that
happens naturally in an office environment.

A 2023 survey found that 58% of workers preferred a hybrid model — some days
in the office, some at home. Employers are increasingly offering this as a
standard arrangement. The future of work appears to be neither fully remote
nor fully in-person, but somewhere in between.

The office has not disappeared. But it has changed its purpose — from a place
where work happens, to a place for collaboration, creativity, and connection.
"""

VOCABULARY = {
    "workforce":       "pracovní síla, zaměstnanci",
    "overnight":       "přes noc, ze dne na den",
    "temporary":       "dočasný",
    "permanent":       "trvalý, stálý",
    "commuting":       "dojíždění",
    "productivity":    "produktivita",
    "interruption":    "přerušení",
    "talent pool":     "zásobník talentů",
    "isolation":       "izolace",
    "blurring":        "rozostření, setření hranic",
    "mentoring":       "mentorování",
    "hybrid":          "hybridní",
    "arrangement":     "ujednání, dohoda",
    "collaboration":   "spolupráce",
}

COMPREHENSION = [
    ("What caused remote work to become widespread?",
     "The COVID-19 pandemic."),
    ("Name two advantages of remote work mentioned in the article.",
     "Any two: no commuting / higher productivity / better work-life balance / lower costs for companies."),
    ("What is one disadvantage for junior employees?",
     "They miss out on informal learning and mentoring."),
    ("What percentage of workers prefer a hybrid model?",
     "58%."),
    ("According to the article, what is the new purpose of the office?",
     "Collaboration, creativity, and connection."),
]

LANGUAGE_FOCUS = [
    ("Present perfect for current relevance:",
     "'Remote work HAS BECOME a permanent way of working.'"),
    ("Passive voice:",
     "'Millions of people WERE FORCED to work from home.'"),
    ("Contrast connector:",
     "'However, remote work IS NOT WITHOUT its challenges.'"),
    ("Concessive clause:",
     "'What began as temporary HAS BECOME permanent.'"),
]

DISCUSSION = [
    "Do you work (or study) from home? What are your personal experiences?",
    "What do you think is lost when people don't work in an office together?",
    "Would you prefer to work fully remotely, in an office, or hybrid? Why?",
    "Has the pandemic permanently changed the way we think about work?",
]

print("=" * 55)
print("  ARTICLE 02: The Rise of Remote Work")
print("=" * 55)
print(ARTICLE)

print("\n📚 VOCABULARY:")
print("-" * 55)
for en, cz in VOCABULARY.items():
    print(f"  {en:<22} {cz}")

print("\n🔍 LANGUAGE FOCUS:")
print("-" * 55)
for feature, example in LANGUAGE_FOCUS:
    print(f"  {feature}")
    print(f"    {example}\n")

print("\n🎯 COMPREHENSION:")
print("-" * 55)
for i, (q, a) in enumerate(COMPREHENSION, 1):
    print(f"\n  Q{i}: {q}")
    ans = input("  → ").strip()
    print(f"  ✓ Model: {a}")

print("\n💬 DISCUSSION:")
print("-" * 55)
for i, q in enumerate(DISCUSSION, 1):
    print(f"  {i}. {q}")
    ans = input("  → ").strip()
    print()

# YOUR TASK:
# 1. Write a 100-word summary of the article in your own words
# 2. Write a paragraph: what are the main advantages of remote work FOR YOU?
# 3. Conduct a survey of 3 people you know: do they prefer remote, office, or hybrid?
#    Report the results in English.
