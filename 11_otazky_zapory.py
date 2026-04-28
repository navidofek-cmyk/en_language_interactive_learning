"""
LESSON 11: Questions & Negatives
===================================
⭐⭐ Level: A2 | Elementary

Jak tvořit otázky a záporné věty v angličtině.
Topics: yes/no questions · wh-questions · negatives · question tags
"""
import random

WH_WORDS = {
    "What":  "Co / Jaký",  "Who":   "Kdo",
    "Where": "Kde / Kam",  "When":  "Kdy",
    "Why":   "Proč",       "Which": "Který",
    "How":   "Jak",        "How much / How many": "Kolik",
    "How long": "Jak dlouho", "How often": "Jak často",
    "How far":  "Jak daleko", "Whose": "Čí",
}

QUESTION_STRUCTURE = [
    ("Yes/No",  "Do/Does/Did + subject + verb?",    "Do you like coffee?"),
    ("Yes/No",  "Am/Is/Are + subject + ...?",        "Is she at home?"),
    ("WH-",     "WH + do/does/did + subject + verb?","What do you want?"),
    ("WH-",     "WH + am/is/are + subject + ...?",  "Where is he going?"),
    ("WH-subj", "Who/What + verb (no auxiliary)?",  "Who called you?"),
]

NEGATIVE_STRUCTURE = [
    ("Present simple", "do not / don't",   "I don't like spicy food."),
    ("Present simple", "does not / doesn't","She doesn't work here."),
    ("Past simple",    "did not / didn't",  "They didn't come yesterday."),
    ("Present cont.",  "am/is/are not",     "I'm not listening."),
    ("To be",          "am/is/are not",     "He isn't happy about it."),
]

QUESTION_TAGS = [
    ("It's cold today, ___?",         "isn't it?"),
    ("You don't like it, ___?",       "do you?"),
    ("She came yesterday, ___?",      "didn't she?"),
    ("They haven't finished, ___?",   "have they?"),
    ("You're coming, ___?",           "aren't you?"),
    ("He can swim, ___?",             "can't he?"),
]

print("=" * 55)
print("  LESSON 11: Questions & Negatives")
print("=" * 55)

print("\n📚 WH-QUESTION WORDS:")
print("-" * 55)
for en, cz in WH_WORDS.items():
    print(f"  {en:<22} {cz}")

print("\n📚 QUESTION STRUCTURE:")
print("-" * 55)
for qtype, structure, example in QUESTION_STRUCTURE:
    print(f"  [{qtype}] {structure}")
    print(f"          e.g. {example}\n")

print("\n📝 COMMON MISTAKE — subject questions:")
print("-" * 55)
print("  Who CALLED you?  (subject = who → no do/did)")
print("  Who did you CALL? (object = who → need did)")
print()
print("  What HAPPENED?   (subject = what → no did)")
print("  What did you DO? (object = what → need did)")

print("\n📚 NEGATIVE STRUCTURE:")
print("-" * 55)
for tense, aux, example in NEGATIVE_STRUCTURE:
    print(f"  {tense:<20} {aux:<20} {example}")

print("\n📚 QUESTION TAGS (kontrolní otázky):")
print("-" * 55)
print("  Rule: positive sentence → negative tag | negative → positive tag\n")
for sentence, tag in QUESTION_TAGS:
    full = sentence.replace("___", tag)
    print(f"  {full}")

print("\n🎯 QUIZ — form the question:")
print("-" * 55)
quiz = [
    ("Turn into question: 'She works in London.'",
     "Does she work in London?"),
    ("WH-question for underlined: She lives in [Prague].",
     "Where does she live?"),
    ("Turn into negative: 'He went to school.'",
     "He didn't go to school."),
    ("Add question tag: 'You speak English, ___?'",
     "don't you?"),
    ("WH-question for underlined: [Tom] called me.",
     "Who called you?"),
]
score = 0
for question, answer in quiz:
    print(f"  {question}")
    ans = input("  → ").strip()
    if ans.lower() == answer.lower():
        print("  ✓ Correct!\n")
        score += 1
    else:
        print(f"  ✗ Answer: {answer}\n")
print(f"  Score: {score}/5")

# YOUR TASK:
# 1. Write 5 wh-questions you could ask a new friend
# 2. Take 5 positive sentences and convert them to:
#    a) yes/no question  b) negative  c) question tag
# 3. Write a short interview (10 Q&A pairs) about daily life
