"""
ARTICLE 04: Social Media — Blessing or Curse?
================================================
⭐⭐⭐ Level: B1–B2 | Pre-Intermediate

Sociální sítě — výhody, rizika a psychologický dopad.
Topics: technology · health · argument · opinion language
"""

ARTICLE = """
SOCIAL MEDIA — BLESSING OR CURSE?

There are currently over five billion social media users worldwide. These
platforms have fundamentally transformed the way we communicate, consume
information, and present ourselves to the world. But at what cost?

The case for social media is compelling. It has connected people across
continents, given a voice to marginalised communities, and enabled grassroots
movements to organise and achieve change. Businesses have reached customers
they never could before. During the pandemic, social media kept many people
mentally connected when physical contact was impossible.

The case against is equally powerful. Studies consistently link heavy social
media use — particularly among teenagers — to increased rates of anxiety,
depression, and low self-esteem. The algorithmic design of these platforms is
deliberately engineered to maximise engagement, exploiting psychological
vulnerabilities to keep users scrolling. Misinformation spreads faster than
fact, and echo chambers reinforce existing beliefs rather than challenging them.

The picture is further complicated by issues of data privacy, political
manipulation, and the concentration of enormous power in the hands of a small
number of technology companies.

So: blessing or curse? The honest answer is both. Social media is a tool.
Like any tool, its impact depends on how it is used, who controls it, and
what rules govern it. What is clear is that the current model — profit-driven,
largely unregulated — is causing real harm that can no longer be ignored.
"""

VOCABULARY = {
    "marginalised":      "marginalizovaný",
    "grassroots":        "od základů, lidové hnutí",
    "compellingly":      "přesvědčivě",
    "consistently":      "soustavně, opakovaně",
    "algorithmic":       "algoritmický",
    "engineered":        "záměrně navržený",
    "vulnerability":     "zranitelnost",
    "misinformation":    "dezinformace",
    "echo chamber":      "informační bublina",
    "reinforcement":     "posílení, upevnění",
    "data privacy":      "ochrana osobních dat",
    "manipulation":      "manipulace",
    "unregulated":       "neregulovaný",
    "concentration":     "koncentrace (moci)",
}

COMPREHENSION = [
    ("How many social media users are there worldwide?",
     "Over five billion."),
    ("Give two positive effects of social media mentioned in the article.",
     "Any two: connected people / gave voice to marginalised communities / helped businesses / kept people connected during pandemic."),
    ("What psychological effect does social media have on teenagers?",
     "Increased anxiety, depression, and low self-esteem."),
    ("What does 'echo chamber' mean in this context?",
     "A space where existing beliefs are reinforced rather than challenged."),
    ("What is the author's conclusion about social media?",
     "It is both a blessing and a curse — its impact depends on how it is used and regulated."),
]

LANGUAGE_FOCUS = [
    ("Balanced argument structure:",
     "'The case FOR... / The case AGAINST... is equally powerful.'"),
    ("Passive for emphasis:",
     "'These platforms ARE DELIBERATELY ENGINEERED to maximise engagement.'"),
    ("Concessive clause:",
     "'What is clear IS THAT the current model is causing real harm.'"),
    ("Fronting for emphasis:",
     "'So: blessing or curse? THE HONEST ANSWER IS BOTH.'"),
]

DISCUSSION = [
    "How much time do you spend on social media each day? Do you think it's too much?",
    "Do you think social media should be more heavily regulated? By whom?",
    "Should there be a minimum age for using social media? What age, and why?",
    "Can you think of a time when social media had a positive impact on society?",
]

print("=" * 55)
print("  ARTICLE 04: Social Media — Blessing or Curse?")
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
# 1. Write a for/against essay (200 words): "Social media does more harm than good."
# 2. Design a 'digital detox' plan for yourself — what would you change?
# 3. Find a real news article about social media regulation and summarise it in English
