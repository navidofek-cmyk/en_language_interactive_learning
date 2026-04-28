"""
LESSON 45: Project — Discussion & Debate
==========================================
⭐⭐⭐ Level: B1–B2 | Pre-Intermediate

Projekt: strukturovaná diskuze a argumentace v angličtině.
Topics: argument structure · for/against · conceding · discussion phrases
"""

DISCUSSION_PHRASES = {
    "Stating opinion": [
        "In my opinion,...",       "I believe that...",
        "Personally, I think...",  "It seems to me that...",
        "As far as I'm concerned,..","From my point of view,...",
    ],
    "Agreeing": [
        "I completely agree.",     "That's a valid point.",
        "Absolutely.",             "You're absolutely right.",
        "I couldn't agree more.",  "That's exactly what I think.",
    ],
    "Disagreeing politely": [
        "I'm not sure I agree.",   "I see your point, but...",
        "I take your point, however...", "With all due respect,...",
        "Actually, I'd argue the opposite.", "That's one way to look at it, but...",
    ],
    "Conceding a point": [
        "Fair enough.",            "You have a point.",
        "I accept that, but...",   "That may be true, nevertheless...",
        "Even if that's true,...", "Granted, but...",
    ],
    "Adding arguments": [
        "Furthermore,...",         "What's more,...",
        "Not only that, but...",   "In addition to this,...",
        "Another point is that...", "It's also worth mentioning that...",
    ],
    "Giving examples": [
        "For example,...",         "For instance,...",
        "A good example of this is...", "Take..., for instance.",
        "This is illustrated by...", "Evidence for this includes...",
    ],
    "Concluding": [
        "In conclusion,...",       "To sum up,...",
        "Overall, I believe...",   "Taking everything into account,...",
        "On balance,...",          "All things considered,...",
    ],
}

TOPICS = [
    {
        "title":  "Social media does more harm than good.",
        "for":    ["Causes anxiety and depression", "Spreads misinformation",
                   "Reduces face-to-face contact", "Creates unrealistic expectations"],
        "against":["Connects people worldwide", "Enables free expression",
                   "Vital for business", "Raises awareness for important causes"],
    },
    {
        "title":  "University education should be free for everyone.",
        "for":    ["Equal opportunities", "Benefits society long-term",
                   "Reduces debt burden on graduates", "Encourages more people to study"],
        "against":["Too expensive for governments", "May reduce course quality",
                   "Many well-paid jobs don't need a degree",
                   "Students value what they pay for"],
    },
    {
        "title":  "Working from home is better than working in an office.",
        "for":    ["No commute", "Better work-life balance",
                   "Often more productive", "Saves office costs"],
        "against":["Difficult to separate work and home life",
                   "Less collaboration and creativity", "Can feel isolating",
                   "Not possible in all professions"],
    },
    {
        "title":  "Eating meat should be taxed like tobacco.",
        "for":    ["Reduces environmental damage", "Improves public health",
                   "Raises funds for sustainability", "Encourages plant-based diets"],
        "against":["Personal freedom", "Unfair to lower incomes",
                   "Not all meat equally harmful", "Ineffective if tax too low"],
    },
]

print("=" * 55)
print("  LESSON 45: Project — Discussion & Debate")
print("=" * 55)

print("\n📚 DISCUSSION PHRASES:")
print("-" * 55)
for category, phrases in DISCUSSION_PHRASES.items():
    print(f"\n  {category}:")
    for p in phrases:
        print(f"    • {p}")

print("\n" + "=" * 55)
print("  ✏️  DEBATE TOPICS")
print("=" * 55)
print()
for i, topic in enumerate(TOPICS, 1):
    print(f"  {i}. '{topic['title']}'")
print()
choice = input("  Choose topic (1–4): ").strip()
idx = int(choice) - 1 if choice.isdigit() and 1 <= int(choice) <= 4 else 0
topic = TOPICS[idx]

print(f"\n  Topic: '{topic['title']}'")
print("\n  ARGUMENTS FOR:")
for arg in topic["for"]:
    print(f"    + {arg}")
print("\n  ARGUMENTS AGAINST:")
for arg in topic["against"]:
    print(f"    - {arg}")

print("\n  What is your position? (for/against/neutral)")
position = input("  → ").strip()
print(f"\n  Position: {position}")
print("\n  Now write your argument (6–8 sentences).")
print("  Use phrases from the list above. Press Enter twice to finish.\n")
lines = []
while True:
    line = input("  ")
    if line == "" and lines and lines[-1] == "":
        break
    lines.append(line)
print("\n  📝 Your argument:")
print("-" * 55)
for line in lines:
    if line: print(f"  {line}")
print("-" * 55)
print("\n  ✓ Check: Did you state your position clearly? Did you acknowledge the other side?")
print("  ✓ Tip: A strong argument concedes a point, then counters it.")

# YOUR TASK:
# 1. Write a full for/against essay on one topic (200–250 words)
#    Structure: intro → for arguments → against arguments → your conclusion
# 2. Prepare a 2-minute spoken argument on your chosen position
# 3. Find a debate topic you feel strongly about and research real data
#    to support your argument
