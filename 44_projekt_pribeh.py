"""
LESSON 44: Project — Story Writing
=====================================
⭐⭐⭐ Level: B1 | Pre-Intermediate

Projekt: napsat krátký příběh v angličtině.
Topics: narrative tenses · story structure · connectors · vivid writing
"""

NARRATIVE_TENSES = {
    "Past simple":       ("main events, sequence",   "She opened the door and saw a stranger."),
    "Past continuous":   ("background, interrupted", "It was raining when she arrived."),
    "Past perfect":      ("before the main event",   "She had never seen him before."),
    "Past perfect cont.":("duration before past",    "He had been waiting for two hours."),
}

STORY_STRUCTURE = [
    ("1. Setting",      "Establish when/where/who (1–2 sentences)"),
    ("2. Build-up",     "Introduce the situation and characters"),
    ("3. Problem",      "Something goes wrong or changes"),
    ("4. Climax",       "The peak moment of tension or action"),
    ("5. Resolution",   "How it ends — can be happy, sad, or open"),
]

TIME_CONNECTORS = [
    "At first,", "Initially,", "Suddenly,", "Without warning,",
    "Meanwhile,", "At the same time,", "By the time...",
    "A few minutes later,", "Eventually,", "Finally,",
    "As soon as...", "Just as...", "Before long,",
    "Looking back,", "To this day,",
]

VIVID_TECHNIQUES = [
    ("Show, don't tell",
     "✗ She was scared.  ✓ Her hands trembled and her heart pounded."),
    ("Vary sentence length",
     "Short sentences create tension. Longer sentences slow the pace and build atmosphere."),
    ("Use the senses",
     "The smell of coffee. The distant sound of a train. The cold of the metal door."),
    ("Dialogue",
     "'Are you sure about this?' she whispered."),
    ("Strong verbs",
     "✗ He walked quickly.  ✓ He rushed / sprinted / darted / strode."),
]

EXAMPLE_OPENING = """  It was past midnight when I heard the noise. I had been trying
  to sleep for hours, but something was keeping me awake — some
  uneasy feeling I couldn't name. The sound came again: a slow,
  deliberate knock on the front door. I hadn't been expecting
  anyone."""

STORY_STARTERS = [
    "It all started with a wrong number.",
    "I had never believed in coincidences — until that Tuesday.",
    "The letter arrived three weeks after she had left.",
    "Nobody warned me that the job interview would change my life.",
    "I found the notebook on the train seat beside me.",
    "The last thing I expected was to see her there.",
]

print("=" * 55)
print("  LESSON 44: Project — Story Writing")
print("=" * 55)

print("\n📚 NARRATIVE TENSES:")
print("-" * 55)
for tense, (use, example) in NARRATIVE_TENSES.items():
    print(f"  {tense:<24} [{use}]")
    print(f"    e.g. {example}\n")

print("\n📚 STORY STRUCTURE:")
print("-" * 55)
for stage, desc in STORY_STRUCTURE:
    print(f"  {stage:<16} {desc}")

print("\n📚 STORY CONNECTORS:")
print("-" * 55)
for i in range(0, len(TIME_CONNECTORS), 4):
    row = TIME_CONNECTORS[i:i+4]
    print("  " + "  ".join(f"{c:<22}" for c in row))

print("\n📚 VIVID WRITING TECHNIQUES:")
print("-" * 55)
for technique, example in VIVID_TECHNIQUES:
    print(f"\n  [{technique}]")
    print(f"  {example}")

print("\n💬 EXAMPLE OPENING:")
print("-" * 55)
print(EXAMPLE_OPENING)

print("\n" + "=" * 55)
print("  ✏️  YOUR STORY")
print("=" * 55)
print()
print("  Choose a starter or write your own:\n")
for i, starter in enumerate(STORY_STARTERS, 1):
    print(f"  {i}. {starter}")
print()
choice = input("  Choose number (1–6) or press Enter to write your own: ").strip()

if choice and choice.isdigit() and 1 <= int(choice) <= 6:
    first_line = STORY_STARTERS[int(choice) - 1]
else:
    first_line = input("  Your opening line: ").strip()

print(f"\n  Starting with: '{first_line}'")
print("  Write your story (min. 10 sentences). Press Enter twice to finish.\n")
lines = [first_line]
while True:
    line = input("  ")
    if line == "" and lines and lines[-1] == "":
        break
    lines.append(line)

print("\n  📝 Your story:")
print("-" * 55)
for line in lines:
    if line: print(f"  {line}")
print("-" * 55)
print("\n  ✓ Check: Did you use all 3 narrative tenses? Story connectors? Vivid verbs?")

# YOUR TASK:
# 1. Expand your story to 200 words, adding dialogue and sensory details
# 2. Write a second version of the same story from a different character's perspective
# 3. Write a story with a twist ending — the last sentence should surprise the reader
