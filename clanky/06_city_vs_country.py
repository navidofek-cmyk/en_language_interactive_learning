"""
ARTICLE 06: City Life vs Country Life
========================================
⭐⭐⭐ Level: B1 | Pre-Intermediate

Život ve městě vs na venkově — výhody a nevýhody.
Topics: lifestyle · comparison · advantages/disadvantages · opinion
"""

ARTICLE = """
CITY LIFE VS COUNTRY LIFE

Where would you rather live — in a bustling city or a peaceful village?
It is a question that divides people sharply, and the answer says a lot
about what we value in life.

Cities offer opportunity. They are centres of employment, education, culture,
and entertainment. You can find a job more easily, access better hospitals
and universities, and take advantage of a rich social life. Public transport
means you may not even need a car. Cities are also more diverse — living
alongside people from different backgrounds broadens your perspective
in ways that are simply not possible in a small, homogeneous community.

The countryside offers something different: space, quiet, and a connection
to the natural world. Studies consistently show that people in rural areas
report lower stress levels, stronger community ties, and greater life
satisfaction — at least among those who choose to live there. Children who
grow up in the countryside tend to spend more time outdoors and develop
a greater sense of independence.

But country life has real disadvantages too. Services are fewer, distances
are longer, and job opportunities are limited. Young people often leave
for cities, leaving behind ageing communities. Rural areas can feel isolated —
particularly for those who move there from urban backgrounds.

The rise of remote working has blurred the line between city and country.
An increasing number of people are choosing to live in rural areas while
working for city-based employers. Perhaps the future is not a choice between
the two, but a creative combination of both.
"""

VOCABULARY = {
    "bustling":       "rušný, živý",
    "divide":         "rozdělovat",
    "access":         "mít přístup k",
    "diverse":        "různorodý",
    "perspective":    "pohled, perspektiva",
    "homogeneous":    "homogenní, stejnorodý",
    "rural":          "venkovský, rurální",
    "community ties": "komunitní vazby",
    "life satisfaction": "životní spokojenost",
    "isolation":      "izolace, odloučenost",
    "blur":           "setřít, rozmazat (hranice)",
    "ageing":         "stárnoucí",
}

COMPREHENSION = [
    ("Give two advantages of city life mentioned in the article.",
     "Any two: employment / education / culture / entertainment / better hospitals / social life / public transport / diversity."),
    ("What do studies say about stress levels in rural areas?",
     "People in rural areas report lower stress levels."),
    ("What is one disadvantage of country life for young people?",
     "They often leave for cities, leaving ageing communities behind."),
    ("How has remote working changed the city vs country question?",
     "More people can live in rural areas while working for city employers."),
    ("What does the author suggest might be the future?",
     "A creative combination of both city and country life."),
]

LANGUAGE_FOCUS = [
    ("Contrast connectors:",
     "'Cities offer opportunity. The countryside offers SOMETHING DIFFERENT.'"),
    ("Concession:",
     "'at least among those WHO CHOOSE to live there'"),
    ("Hedging:",
     "'Studies CONSISTENTLY SHOW that...'"),
    ("Question as hook:",
     "'Where would you RATHER live?' — engaging the reader directly"),
]

DISCUSSION = [
    "Do you live in a city or the countryside? What do you like and dislike about it?",
    "If you could choose freely, where would you live? Why?",
    "Do you think remote working will lead to a revival of rural areas?",
    "Is there a third option — small towns and suburbs? What do they offer?",
]

print("=" * 55)
print("  ARTICLE 06: City Life vs Country Life")
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
# 1. Write a 150-word comparison of two places you know well
# 2. Write a paragraph: "The ideal place to live would be..." — describe your ideal
# 3. Interview a family member or friend: where would they rather live and why?
#    Report their answers in English using reported speech (lesson 33).
