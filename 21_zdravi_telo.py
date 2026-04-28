"""
LESSON 21: Health & Body
==========================
⭐⭐ Level: A2 | Elementary

Tělo, zdraví a jak mluvit u doktora.
Topics: body parts · symptoms · at the doctor · health advice
"""
import random

BODY_PARTS = {
    "head": "hlava",      "face":    "obličej",  "eye":    "oko",
    "ear":  "ucho",       "nose":    "nos",      "mouth":  "ústa",
    "tooth/teeth": "zub/zuby", "throat": "krk",  "neck":   "krk",
    "shoulder": "rameno", "arm":     "paže",     "elbow":  "loket",
    "wrist": "zápěstí",   "hand":    "ruka",     "finger": "prst",
    "chest": "hrudník",   "back":    "záda",     "stomach":"žaludek",
    "leg":   "noha",      "knee":    "koleno",   "ankle":  "kotník",
    "foot/feet": "chodidlo/chodidla", "toe": "palec u nohy",
    "heart": "srdce",     "lung":    "plíce",    "brain":  "mozek",
}

SYMPTOMS = {
    "I have a headache":        "Bolí mě hlava",
    "I have a sore throat":     "Bolí mě v krku",
    "I have a temperature/fever":"Mám teplotu",
    "I feel sick / nauseous":   "Je mi špatně / nevolno",
    "I've been vomiting":       "Zvracím",
    "I have a cold":            "Jsem nachlazený/á",
    "I have the flu":           "Mám chřipku",
    "I'm coughing":             "Kašlu",
    "I have a rash":            "Mám vyrážku",
    "I'm exhausted":            "Jsem vyčerpaný/á",
    "I hurt my knee":           "Zranil/a jsem si koleno",
    "I've sprained my ankle":   "Vyvrtl/a jsem si kotník",
    "I'm allergic to ...":      "Jsem alergický/á na ...",
    "I can't sleep":            "Nemohu spát",
}

DOCTOR_PHRASES = {
    "I'd like to make an appointment": "Chtěl/a bych se objednat",
    "How long have you had this?":     "Jak dlouho to máte?",
    "Where does it hurt?":             "Kde vás to bolí?",
    "Roll up your sleeve please":      "Vyhrňte si rukáv, prosím",
    "Take a deep breath":              "Zhluboka se nadechněte",
    "I'll prescribe you ...":          "Předepíšu vám ...",
    "Take one tablet three times a day":"Berte jednu tabletu třikrát denně",
    "Come back in a week":             "Přijďte za týden",
    "You need to rest":                "Musíte odpočívat",
}

print("=" * 55)
print("  LESSON 21: Health & Body")
print("=" * 55)

print("\n📚 BODY PARTS:")
print("-" * 55)
items = list(BODY_PARTS.items())
for i in range(0, len(items), 3):
    row = items[i:i+3]
    print("  " + "   ".join(f"{en:<18}{cz:<14}" for en, cz in row))

print("\n📚 SYMPTOMS — říct co tě bolí:")
print("-" * 55)
for en, cz in SYMPTOMS.items():
    print(f"  {en:<34} {cz}")

print("\n📝 GRAMMAR — expressing pain:")
print("-" * 55)
print("  My ... HURTS / HURT:")
print("    My back hurts.   My feet hurt. (plural)")
print()
print("  I HAVE a + illness:")
print("    I have a headache. / I have a cold. / I have the flu.")
print()
print("  I FEEL + adjective:")
print("    I feel dizzy. / tired. / unwell. / sick.")

print("\n📚 AT THE DOCTOR:")
print("-" * 55)
for en, cz in DOCTOR_PHRASES.items():
    print(f"  {en}")
    print(f"    → {cz}\n")

print("\n💬 DIALOGUE — At the surgery:")
print("-" * 55)
dialogue = [
    ("Doctor",  "Good morning. What seems to be the problem?"),
    ("Patient", "I've had a sore throat and a temperature for two days."),
    ("Doctor",  "Have you been coughing?"),
    ("Patient", "Yes, quite a lot. And I feel exhausted."),
    ("Doctor",  "It sounds like the flu. I'll prescribe you some medication."),
    ("Patient", "Should I take time off work?"),
    ("Doctor",  "Yes, you need to rest for at least three days."),
]
for speaker, line in dialogue:
    print(f"  {speaker}: {line}")

print("\n🎯 QUIZ — přelož symptom do angličtiny:")
print("-" * 55)
pairs = random.sample(list(SYMPTOMS.items()), 6)
score = 0
for en, cz in pairs:
    ans = input(f"  {cz}  →  ").strip()
    if ans.lower() == en.lower():
        print("  ✓ Correct!\n"); score += 1
    else:
        print(f"  ✗ Answer: {en}\n")
print(f"  Score: {score}/6")

# YOUR TASK:
# 1. Describe the last time you were ill — what symptoms did you have?
# 2. Write a dialogue at the pharmacy asking for medicine
# 3. Write 5 health tips using 'should/shouldn't' and 'must/mustn't'
