"""
LESSON 15: Project — Everyday Conversations
=============================================
⭐⭐⭐ Level: A2–B1 | Elementary–Pre-Intermediate

Projekt: 6 každodenních konverzačních situací.
Combines grammar and vocabulary from lessons 01–14.
Topics: small talk · phone · email · requests · opinions
"""
import random

SITUATIONS = {
    "Small talk at work": [
        "How was your weekend?",
        "Not bad, thanks. I went to the cinema. You?",
        "I stayed home — the weather was terrible.",
        "Yeah, typical November. Have you seen the new Bond film?",
        "Not yet. Is it good?",
        "Really good actually. You should watch it.",
    ],
    "Calling a doctor": [
        "Good morning, City Medical Centre.",
        "Hello, I'd like to make an appointment please.",
        "Certainly. What's the problem?",
        "I have a bad cough and a sore throat.",
        "Can you come in on Thursday at 10 am?",
        "Yes, that's fine. Thank you.",
    ],
    "At the hotel check-in": [
        "Good evening. I have a reservation — the name is Novák.",
        "Let me check... Yes, a double room for three nights?",
        "That's right.",
        "Here's your key card. Breakfast is from 7 to 10.",
        "Could I have a wake-up call at 6:30?",
        "Of course. Have a pleasant stay!",
    ],
    "Asking for help": [
        "Excuse me, could you help me?",
        "Of course, what's the matter?",
        "I'm looking for the post office.",
        "It's about 5 minutes' walk. Go straight and turn left at the lights.",
        "And is it on the left or right?",
        "On the right, next to the bank. You can't miss it.",
    ],
    "Expressing opinion": [
        "What do you think about working from home?",
        "Personally, I think it's great for concentration.",
        "I'm not so sure. I prefer being in the office.",
        "Really? Don't you find commuting stressful?",
        "Not really. I actually enjoy the train journey.",
        "Fair enough. I suppose it depends on the person.",
    ],
    "Polite requests": [
        "Could I possibly borrow your pen?",
        "Sure, here you go.",
        "Thanks. Also, would you mind turning down the music a bit?",
        "Oh sorry, of course.",
        "I really appreciate it. I'm trying to concentrate.",
        "No problem at all. Let me know if I'm disturbing you.",
    ],
}

USEFUL_CONNECTORS = {
    "Personally, I think...":     "Osobně si myslím...",
    "In my opinion...":           "Podle mého názoru...",
    "I'm not sure about that.":   "Nejsem si tím jistý/á.",
    "That's a good point.":       "To je dobrý postřeh.",
    "I see what you mean.":       "Rozumím, co tím myslíš.",
    "I agree / I disagree.":      "Souhlasím / Nesouhlasím.",
    "Fair enough.":               "Tak tedy dobře / Kladná odpověď.",
    "It depends.":                "Záleží na tom.",
    "To be honest...":            "Upřímně řečeno...",
    "Having said that...":        "Na druhou stranu...",
}

print("=" * 55)
print("  LESSON 15: Project — Everyday Conversations")
print("=" * 55)

print("\n📚 USEFUL CONNECTORS & PHRASES:")
print("-" * 55)
for en, cz in USEFUL_CONNECTORS.items():
    print(f"  {en:<32} {cz}")

print()
for situation, lines in SITUATIONS.items():
    print(f"\n💬 SITUATION: {situation}")
    print("-" * 55)
    speakers = ["A", "B"] * 10
    for speaker, line in zip(speakers, lines):
        print(f"  {speaker}: {line}")

print("\n" + "=" * 55)
print("  ✏️  YOUR SPEAKING TASK")
print("=" * 55)
print()
print("  Choose one situation and write your own version:")
print()
for i, situation in enumerate(SITUATIONS.keys(), 1):
    print(f"  {i}. {situation}")
print()
choice = input("  Enter number (1–6): ").strip()
print()
print("  Write your dialogue (min. 6 lines). Press Enter twice to finish.")
lines = []
while True:
    line = input("  → ")
    if line == "" and lines and lines[-1] == "":
        break
    lines.append(line)

print("\n  📝 Your dialogue:")
print("-" * 55)
for line in lines:
    if line:
        print(f"  {line}")
print("-" * 55)
print("\n  ✓ Great work! Read it aloud and focus on natural rhythm.")
print("  Tip: Record yourself and listen back — it's the fastest way to improve.")

# YOUR TASK:
# 1. Practise each of the 6 situations by reading both roles aloud
# 2. Rewrite the 'Expressing opinion' dialogue using a different topic
#    (e.g. social media, electric cars, remote learning)
# 3. Write a formal email requesting information about a product or service
