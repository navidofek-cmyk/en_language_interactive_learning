"""
LESSON 07: Project — Full Self Introduction
=============================================
⭐⭐ Level: A1–A2 | Beginner–Elementary

Projekt: sestav kompletní sebepředstavení v angličtině.
Combines vocabulary from lessons 01–06.
Topics: putting it all together · natural conversation · writing
"""

TEMPLATE = """
Hello! My name is {name}.
I am {age} years old and I'm from {city}, Czech Republic.
I have {family_desc}.
My favourite colour is {colour} and my favourite food is {food}.
I like {hobby}.
Nice to meet you!
"""

EXAMPLE_PHRASES = {
    "I was born in ...":        "Narodil/a jsem se v ...",
    "I grew up in ...":         "Vyrůstal/a jsem v ...",
    "I work as a ...":          "Pracuji jako ...",
    "I study ...":              "Studuji ...",
    "In my free time I ...":    "Ve volném čase ...",
    "I enjoy ...":              "Baví mě ...",
    "I'm interested in ...":    "Zajímám se o ...",
    "My hobbies are ...":       "Moje koníčky jsou ...",
    "I live with my family":    "Žiju s rodinou",
    "I live alone":             "Žiju sám/sama",
    "I have a dog/cat":         "Mám psa/kočku",
}

HOBBIES = [
    "reading", "cooking", "cycling", "football", "swimming",
    "hiking", "drawing", "gaming", "travelling", "photography",
    "music", "dancing", "yoga", "running", "gardening",
]

print("=" * 55)
print("  LESSON 07: Project — Full Self Introduction")
print("=" * 55)

print("\n📚 USEFUL PHRASES:")
print("-" * 55)
for en, cz in EXAMPLE_PHRASES.items():
    print(f"  {en:<32} {cz}")

print("\n💬 EXAMPLE INTRODUCTION:")
print("-" * 55)
print(TEMPLATE.format(
    name="Jan Novák",
    age=28,
    city="Brno",
    family_desc="one sister and two brothers",
    colour="blue",
    food="pizza",
    hobby="cycling and reading",
))

print("\n✏️  YOUR TURN — build your introduction:")
print("-" * 55)
name   = input("  Your name: ")
age    = input("  Your age: ")
city   = input("  Your city: ")
family = input("  Your family (e.g. 'a brother and two sisters'): ")
colour = input("  Favourite colour: ")
food   = input("  Favourite food: ")
hobby  = input("  Hobby/hobbies: ")

intro = TEMPLATE.format(
    name=name, age=age, city=city,
    family_desc=family, colour=colour,
    food=food, hobby=hobby,
)
print("\n  📝 Your introduction:")
print("-" * 55)
print(intro)
print("-" * 55)
print("\n  ✓ Well done! Try reading it aloud — pronunciation matters!")

print("\n💡 TIPS FOR NATURAL SPEECH:")
print("-" * 55)
print("  ✓ Use contractions: I'm, I've, I don't (sounds more natural)")
print("  ✓ Vary sentence starters: Also... / As well as... / Apart from...")
print("  ✓ Add opinions: I really enjoy... / I'm quite good at...")
print("  ✓ End with a question: What about you?")

# YOUR TASK:
# 1. Expand the introduction to 8–10 sentences using EXAMPLE_PHRASES
# 2. Write a second version as a formal introduction (job interview style)
# 3. Add pronunciation notes: which words are commonly mispronounced
#    by Czech speakers (e.g. 'three' not 'tree', 'the' not 'ze')
