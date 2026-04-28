"""
LESSON 32: Gerunds & Infinitives
===================================
⭐⭐⭐ Level: B1 | Pre-Intermediate

Gerundy a infinitivy — kdy použít -ing a kdy 'to + verb'.
Topics: verb + gerund · verb + infinitive · both (meaning changes) · prepositions
"""
import random

GERUND_VERBS = {
    "enjoy":     "I enjoy swimming in the sea.",
    "finish":    "Have you finished eating?",
    "avoid":     "She avoids making eye contact.",
    "suggest":   "He suggested going to a film.",
    "mind":      "Do you mind waiting a moment?",
    "miss":      "I miss living in Prague.",
    "consider":  "Are you considering changing jobs?",
    "practise":  "I need to practise speaking English.",
    "keep":      "Keep trying — you'll get there.",
    "can't stand":"I can't stand waiting in queues.",
    "give up":   "He gave up smoking last year.",
    "risk":      "Don't risk losing your passport.",
}

INFINITIVE_VERBS = {
    "want":      "I want to learn Spanish.",
    "need":      "She needs to rest.",
    "decide":    "They decided to move abroad.",
    "hope":      "I hope to see you soon.",
    "plan":      "We plan to visit Rome.",
    "refuse":    "He refused to sign the contract.",
    "seem":      "You seem to know everyone here.",
    "manage":    "Did you manage to fix it?",
    "promise":   "She promised to call.",
    "offer":     "He offered to help.",
    "expect":    "I expect to finish by Friday.",
    "afford":    "We can't afford to buy a house.",
}

BOTH_SAME = {
    "like":   ("I like swimming.", "I like to swim."),
    "love":   ("She loves cooking.", "She loves to cook."),
    "hate":   ("He hates waiting.", "He hates to wait."),
    "begin":  ("It began raining.", "It began to rain."),
    "start":  ("She started crying.", "She started to cry."),
    "prefer": ("I prefer walking.", "I prefer to walk."),
}

BOTH_DIFFERENT = {
    "stop": (
        "Stop smoking! (přestaň kouřit)",
        "He stopped to smoke. (zastavil se, aby si zakouřil)",
    ),
    "remember": (
        "I remember locking the door. (pamatuji si, že jsem zamkl)",
        "Remember to lock the door! (nezapomeň zamknout)",
    ),
    "forget": (
        "I'll never forget meeting her. (nikdy nezapomenu, jak jsem ji potkal)",
        "Don't forget to call me. (nezapomeň zavolat)",
    ),
    "try": (
        "Try adding more salt. (zkus přidat sůl)",
        "I tried to open the jar but couldn't. (pokoušel jsem se otevřít)",
    ),
    "regret": (
        "I regret saying that. (lituji, že jsem to řekl)",
        "I regret to inform you... (s lítostí vám oznamuji)",
    ),
}

print("=" * 55)
print("  LESSON 32: Gerunds & Infinitives")
print("=" * 55)

print("\n📚 VERBS FOLLOWED BY GERUND (-ing):")
print("-" * 55)
for verb, example in GERUND_VERBS.items():
    print(f"  {verb:<14} → {example}")

print("\n📚 VERBS FOLLOWED BY INFINITIVE (to + verb):")
print("-" * 55)
for verb, example in INFINITIVE_VERBS.items():
    print(f"  {verb:<14} → {example}")

print("\n📚 VERBS THAT TAKE BOTH (same meaning):")
print("-" * 55)
for verb, (g, inf) in BOTH_SAME.items():
    print(f"  {verb}: {g}  /  {inf}")

print("\n📚 VERBS WHERE MEANING CHANGES (important!):")
print("-" * 55)
for verb, (g, inf) in BOTH_DIFFERENT.items():
    print(f"  {verb} + -ing:  {g}")
    print(f"  {verb} + to:    {inf}\n")

print("\n📝 AFTER PREPOSITIONS → always GERUND:")
print("-" * 55)
prep_examples = [
    "I'm good AT cooking.",
    "She's interested IN learning languages.",
    "He left without saying goodbye.",
    "Thank you FOR helping me.",
    "I look forward TO seeing you.",
    "Before leaving, check the windows.",
]
for ex in prep_examples:
    print(f"  {ex}")

print("\n🎯 QUIZ — gerund or infinitive?")
print("-" * 55)
quiz = [
    ("I enjoy ___ (read) historical novels.", "reading"),
    ("She decided ___ (leave) the company.", "to leave"),
    ("Have you finished ___ (write) the report?", "writing"),
    ("Don't forget ___ (send) the invoice.", "to send"),
    ("He stopped ___ (smoke) five years ago.", "smoking"),
    ("I'm looking forward to ___ (see) you.", "seeing"),
    ("They refused ___ (pay) the fine.", "to pay"),
    ("Try ___ (restart) the computer.", "restarting"),
]
score = 0
for sentence, answer in quiz:
    print(f"  {sentence}")
    ans = input("  → ").strip()
    if ans.lower() == answer.lower():
        print("  ✓ Correct!\n"); score += 1
    else:
        print(f"  ✗ Answer: {answer}\n")
print(f"  Score: {score}/8")

# YOUR TASK:
# 1. Write 5 true sentences about yourself using gerund verbs (enjoy, miss, can't stand...)
# 2. Write 5 sentences using infinitive verbs (want, plan, hope, decide...)
# 3. Write pairs for: stop / remember / try — both meanings in context
