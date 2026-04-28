"""
LESSON 56: IELTS / CAE Writing — Essay Structure
==================================================
⭐⭐⭐⭐⭐ Level: B2–C1 | Upper-Intermediate

Psaní esejí pro IELTS Task 2 a CAE — struktura a jazyk.
Topics: essay types · paragraphing · thesis · argument · band descriptors
"""

ESSAY_TYPES = {
    "Opinion":        "Do you agree or disagree? Give your opinion.",
    "Discussion":     "Discuss both views and give your opinion.",
    "Problem-Solution":"What are the causes/problems? What solutions exist?",
    "Advantages-Disadvantages": "Discuss the advantages and disadvantages.",
    "Two-part question": "Two separate questions requiring two answers.",
}

ESSAY_STRUCTURE = {
    "Introduction (2–3 sentences)": [
        "1. Paraphrase the topic (don't copy the question!)",
        "2. State your thesis / main argument clearly",
        "3. Optional: outline what you will discuss",
    ],
    "Body Paragraph 1 (4–5 sentences)": [
        "Topic sentence — main point of this paragraph",
        "Explanation — develop the point",
        "Example / evidence — support with a specific example",
        "Result / implication — what this means",
    ],
    "Body Paragraph 2 (4–5 sentences)": [
        "Topic sentence — second main point (or counterargument)",
        "Explanation",
        "Example / evidence",
        "Concession or rebuttal if counterargument",
    ],
    "Conclusion (2–3 sentences)": [
        "Restate your thesis (in different words!)",
        "Summarise main points briefly",
        "Final thought / recommendation / prediction",
    ],
}

BAND_DESCRIPTORS = {
    "Task Achievement":    "Does it answer the question? Is the position clear?",
    "Coherence & Cohesion":"Is it well-organised? Does it flow logically?",
    "Lexical Resource":    "Variety of vocabulary? Accuracy? Collocation?",
    "Grammar Range":       "Variety of structures? Complex sentences? Accuracy?",
}

USEFUL_LANGUAGE = {
    "Introduction": [
        "In recent years, there has been growing debate about...",
        "It is widely argued that...",
        "This essay will examine...",
        "While some people believe..., others maintain that...",
    ],
    "Adding arguments": [
        "Furthermore, it is worth considering...",
        "A further point to note is...",
        "Not only..., but also...",
        "What is more,...",
    ],
    "Counterargument": [
        "However, it could be argued that...",
        "Critics of this view point out that...",
        "Admittedly,...",
        "Despite this,...",
        "While it is true that..., nevertheless...",
    ],
    "Examples": [
        "This is illustrated by...",
        "A clear example of this can be seen in...",
        "For instance,...",
        "Research has shown that...",
    ],
    "Conclusion": [
        "In conclusion, it is clear that...",
        "Taking everything into account,...",
        "On balance, I believe that...",
        "It is therefore evident that...",
    ],
}

SAMPLE_TOPIC = (
    "Some people believe that social media has had a negative impact on society. "
    "To what extent do you agree or disagree?"
)

SAMPLE_INTRO = (
    "In recent years, the rise of social media platforms has fundamentally changed "
    "the way people communicate and consume information. While critics argue that "
    "these platforms have had a largely detrimental effect on society, I believe "
    "the reality is more nuanced, with both significant benefits and drawbacks."
)

print("=" * 55)
print("  LESSON 56: IELTS / CAE Writing — Essay Structure")
print("=" * 55)

print("\n📚 ESSAY TYPES:")
print("-" * 55)
for etype, description in ESSAY_TYPES.items():
    print(f"  {etype:<28} → {description}")

print("\n📚 ESSAY STRUCTURE:")
print("-" * 55)
for section, points in ESSAY_STRUCTURE.items():
    print(f"\n  {section}:")
    for p in points:
        print(f"    • {p}")

print("\n📚 IELTS BAND DESCRIPTORS:")
print("-" * 55)
for criterion, description in BAND_DESCRIPTORS.items():
    print(f"  {criterion:<26} {description}")

print("\n📚 USEFUL LANGUAGE:")
print("-" * 55)
for section, phrases in USEFUL_LANGUAGE.items():
    print(f"\n  {section}:")
    for p in phrases:
        print(f"    {p}")

print("\n💬 SAMPLE INTRODUCTION:")
print("-" * 55)
print(f"  Topic: '{SAMPLE_TOPIC}'\n")
print(f"  Introduction:")
print(f"  {SAMPLE_INTRO}")

print("\n✏️  YOUR TASK:")
print("-" * 55)
print("  Topic: 'Governments should invest more in public transport")
print("  rather than building new roads. To what extent do you agree?'\n")
print("  Write your introduction (3 sentences):")
intro = []
while True:
    line = input("  ")
    if line == "" and intro and intro[-1] == "":
        break
    intro.append(line)
print("\n  Your introduction:")
for line in intro:
    if line: print(f"  {line}")
print("\n  ✓ Check: Did you paraphrase the topic? Is your thesis clear?")

# YOUR TASK:
# 1. Write a full 250-word essay on the sample topic above
# 2. Time yourself: aim for 40 minutes (IELTS standard)
# 3. Self-assess using the 4 band descriptors
