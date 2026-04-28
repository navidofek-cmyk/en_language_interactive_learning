"""
LESSON 12: Modal Verbs
========================
⭐⭐ Level: A2–B1 | Elementary–Pre-Intermediate

Modální slovesa — can, must, should, may, might, have to, need to.
Topics: ability · permission · obligation · advice · possibility
"""
import random

MODALS = {
    "can":      "umět, moci (schopnost/povolení)",
    "can't":    "nemoci, neumět",
    "could":    "mohl/a by, uměl/a (minulost can nebo zdvořilá žádost)",
    "must":     "musím (silná povinnost, vlastní rozhodnutí)",
    "mustn't":  "nesmím (zákaz)",
    "have to":  "musím (vnější povinnost, pravidlo)",
    "don't have to": "nemusím (žádná povinnost)",
    "should":   "měl/a bych (rada, doporučení)",
    "shouldn't":"neměl/a bych",
    "may":      "smím? / možná (formální povolení nebo možnost)",
    "might":    "možná (slabá možnost)",
    "need to":  "potřebovat (nutnost)",
    "needn't":  "nemusím (British English)",
}

GRAMMAR_RULES = [
    "Modal + base verb (no -s, no -ing, no 'to'):",
    "  ✓ She CAN swim.        (NE: She cans swim / She can swims)",
    "  ✓ You MUST go.         (NE: You must to go)",
    "  ✓ He SHOULD eat less.  (NE: He should eating)",
    "",
    "Exception — 'have to' and 'need to' conjugate normally:",
    "  She HAS TO work late.   I NEED TO study.",
]

EXAMPLES = [
    ("can",         "I can speak three languages.",         "Umím mluvit třemi jazyky."),
    ("can't",       "She can't drive — she's too young.",   "Neumí řídit — je příliš mladá."),
    ("could",       "Could you help me, please?",           "Mohl/a byste mi pomoci, prosím?"),
    ("must",        "I must call my mum tonight.",          "Musím dnes večer zavolat mamce."),
    ("mustn't",     "You mustn't smoke here.",              "Zde se nesmí kouřit."),
    ("have to",     "We have to wear a uniform.",           "Musíme nosit uniformu (pravidlo)."),
    ("don't have to","You don't have to come.",             "Nemusíš přijít."),
    ("should",      "You should drink more water.",         "Měl/a bys pít více vody."),
    ("might",       "It might rain tomorrow.",              "Zítra možná bude pršet."),
]

print("=" * 55)
print("  LESSON 12: Modal Verbs")
print("=" * 55)

print("\n📚 MODALS & MEANINGS:")
print("-" * 55)
for modal, meaning in MODALS.items():
    print(f"  {modal:<20} {meaning}")

print("\n📝 GRAMMAR RULES:")
print("-" * 55)
for line in GRAMMAR_RULES:
    print(f"  {line}")

print("\n💬 EXAMPLES IN CONTEXT:")
print("-" * 55)
for modal, en, cz in EXAMPLES:
    print(f"  [{modal}]  {en}")
    print(f"             → {cz}\n")

print("\n📝 MUST vs. HAVE TO vs. SHOULD:")
print("-" * 55)
print("  MUST     → personal feeling of necessity / strong advice")
print("             'I must study harder.' (my decision)")
print("  HAVE TO  → external obligation (rules, laws, others)")
print("             'I have to wear a helmet by law.'")
print("  SHOULD   → advice, recommendation (not compulsory)")
print("             'You should see a doctor.'")

print("\n🎯 QUIZ — choose the right modal:")
print("-" * 55)
quiz = [
    ("The sign says no entry. You ___ go in. (prohibition)", "mustn't"),
    ("I ___ swim well, but I'm learning. (not able yet)", "can't"),
    ("___ you pass the salt, please? (polite request)", "Could"),
    ("It's not compulsory. You ___ come if you're busy.", "don't have to"),
    ("Take an umbrella — it ___ rain later. (weak possibility)", "might"),
    ("You ___ eat breakfast — it's the most important meal. (advice)", "should"),
]
score = 0
for sentence, answer in quiz:
    print(f"  {sentence}")
    ans = input("  → ").strip()
    if ans.lower() == answer.lower():
        print("  ✓ Correct!\n")
        score += 1
    else:
        print(f"  ✗ Answer: {answer}\n")
print(f"  Score: {score}/6")

# YOUR TASK:
# 1. Write 3 sentences for each: must / have to / should (9 total)
# 2. Describe rules at your workplace/school using must/mustn't/have to
# 3. Give 5 pieces of advice to someone learning English (use should/shouldn't)
