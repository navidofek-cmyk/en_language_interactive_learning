"""
LESSON 30: Project — Written Communication
============================================
⭐⭐⭐ Level: B1 | Pre-Intermediate

Projekt: formální a neformální psaný projev.
Topics: informal email · formal email · complaint · CV summary · review
"""

TEMPLATES = {
    "informal_email": {
        "title": "Informal Email (to a friend)",
        "structure": [
            "Hi [name],",
            "",
            "Hope you're well! [Reference to last contact]",
            "",
            "[Main reason for writing — 2–3 sentences]",
            "",
            "[Second point or question]",
            "",
            "Anyway, [closing comment]. Let me know [question].",
            "",
            "[Sign-off], [Your name]",
        ],
        "tips": [
            "Use contractions: I'm, don't, we've",
            "Use informal connectors: Anyway, By the way, So,...",
            "Keep sentences short and natural",
            "End with a question to keep the conversation going",
        ],
    },
    "formal_email": {
        "title": "Formal Email (to a company)",
        "structure": [
            "Dear Mr/Ms [Surname], (or 'Dear Sir/Madam')",
            "",
            "I am writing to [purpose].",
            "",
            "[Main content — 2–3 formal sentences]",
            "",
            "[Second paragraph — detail or request]",
            "",
            "I would be grateful if you could [specific request].",
            "Please do not hesitate to contact me should you require further information.",
            "",
            "Yours sincerely, (known name) / Yours faithfully, (Sir/Madam)",
            "[Full name]",
        ],
        "tips": [
            "No contractions: I am (not I'm), do not (not don't)",
            "Use formal vocabulary: enquire, inform, request, assist",
            "State purpose in first sentence",
            "One idea per paragraph",
        ],
    },
    "complaint": {
        "title": "Letter of Complaint",
        "structure": [
            "Dear [name/Sir/Madam],",
            "",
            "I am writing to express my dissatisfaction with [product/service].",
            "",
            "On [date], I [describe what happened]. Unfortunately, [problem].",
            "",
            "As a result, [describe impact].",
            "",
            "I would therefore request that you [specific resolution requested].",
            "I look forward to your prompt response.",
            "",
            "Yours sincerely,",
            "[Name]",
        ],
        "tips": [
            "Be firm but polite — do not be rude",
            "Include dates and order numbers",
            "State clearly what resolution you want",
            "Give a deadline: 'within 14 days'",
        ],
    },
}

USEFUL_CONNECTORS = {
    "Adding":       ["Furthermore,", "In addition,", "Moreover,", "Also,"],
    "Contrasting":  ["However,", "On the other hand,", "Although", "Despite"],
    "Cause/effect": ["Therefore,", "As a result,", "Consequently,", "This led to"],
    "Sequencing":   ["Firstly,", "Secondly,", "Finally,", "To begin with,"],
    "Concluding":   ["In conclusion,", "To summarise,", "Overall,", "In short,"],
}

print("=" * 55)
print("  LESSON 30: Project — Written Communication")
print("=" * 55)

for key, template in TEMPLATES.items():
    print(f"\n📚 {template['title'].upper()}:")
    print("-" * 55)
    print("  Structure:")
    for line in template["structure"]:
        print(f"    {line}")
    print("\n  Tips:")
    for tip in template["tips"]:
        print(f"    • {tip}")

print("\n📚 USEFUL CONNECTORS:")
print("-" * 55)
for category, connectors in USEFUL_CONNECTORS.items():
    print(f"  {category:<14} {' · '.join(connectors)}")

print("\n" + "=" * 55)
print("  ✏️  WRITING TASKS")
print("=" * 55)

tasks = [
    ("1", "INFORMAL EMAIL",
     "Write an email to a friend you haven't spoken to in 6 months.\n"
     "  • Say why you haven't been in touch\n"
     "  • Describe what's been happening in your life\n"
     "  • Invite them to meet up\n"
     "  Length: 120–150 words"),
    ("2", "FORMAL EMAIL",
     "Write an email to a language school asking for information.\n"
     "  • Enquire about courses available\n"
     "  • Ask about prices and schedule\n"
     "  • Request a brochure\n"
     "  Length: 100–130 words"),
    ("3", "COMPLAINT",
     "Write a complaint about a product that arrived damaged.\n"
     "  • State when and what you ordered\n"
     "  • Describe the problem\n"
     "  • Request a replacement or refund\n"
     "  Length: 100–120 words"),
]

print()
for num, title, desc in tasks:
    print(f"  TASK {num}: {title}")
    print(f"  {desc}\n")

print("  Which task would you like to write now? (1/2/3)")
choice = input("  → ").strip()
chosen = next((t for t in tasks if t[0] == choice), tasks[0])
print(f"\n  Writing: {chosen[1]}")
print(f"  {chosen[2]}\n")
print("-" * 55)
lines = []
print("  Start writing (press Enter twice to finish):")
while True:
    line = input("  ")
    if line == "" and lines and lines[-1] == "":
        break
    lines.append(line)
print("\n  Your text:")
print("-" * 55)
for line in lines:
    if line:
        print(f"  {line}")
print("-" * 55)
print("\n  ✓ Check: Did you use connectors? Correct level of formality?")

# YOUR TASK:
# 1. Write all three texts above (informal email, formal email, complaint)
# 2. Exchange with a language partner for peer feedback
# 3. Write a short online product review (positive and negative) — 80 words each
