"""
LESSON 53: Crime & Justice
============================
⭐⭐⭐ Level: B1–B2 | Pre-Intermediate

Zločin, právo a spravedlnost.
Topics: crimes · criminals · legal system · punishment · verbs
"""
import random

CRIMES = {
    "theft":            "krádež",         "burglary":       "vloupání",
    "robbery":          "loupež (se silou)","shoplifting":   "krádež v obchodě",
    "mugging":          "přepadení na ulici","fraud":        "podvod",
    "forgery":          "padělání",       "smuggling":      "pašování",
    "drug dealing":     "dealování drog", "bribery":        "úplatkářství",
    "murder":           "vražda",         "manslaughter":   "zabití (bez úmyslu)",
    "assault":          "napadení",       "arson":          "žhářství",
    "vandalism":        "vandalismus",    "blackmail":      "vydírání",
    "kidnapping":       "únos",           "cybercrime":     "kyberkriminalita",
    "money laundering": "praní špinavých peněz","identity theft":"krádež identity",
}

CRIMINALS = {
    "thief":        "zloděj",        "burglar":      "vloupač",
    "robber":       "lupič",         "mugger":       "přepadávač",
    "murderer":     "vrah",          "arsonist":     "žhář",
    "smuggler":     "pašerák",       "fraudster":    "podvodník",
    "pickpocket":   "kapsář",        "vandal":       "vandal",
    "hacker":       "hacker",        "offender":     "pachatel",
    "suspect":      "podezřelý",     "defendant":    "obžalovaný",
    "convict":      "odsouzenec",    "witness":      "svědek",
    "victim":       "oběť",
}

LEGAL_SYSTEM = {
    "arrest":           "zatknout",       "charge with":    "obvinit z",
    "prosecute":        "stíhat (soudně)","appear in court":"stát před soudem",
    "plead guilty":     "přiznat vinu",   "plead not guilty":"popřít vinu",
    "convict":          "odsoudit",       "acquit":         "zprostit viny",
    "sentence to":      "odsoudit k",     "appeal":         "odvolat se",
    "bail":             "kauce",          "fine":           "pokuta",
    "community service":"veřejná služba", "probation":      "podmíněný trest",
    "prison sentence":  "trest odnětí svobody","on parole":  "na podmínce",
    "attorney/solicitor":"právník/advokát","jury":           "porota",
    "judge":            "soudce",         "verdict":        "rozsudek",
    "evidence":         "důkaz",          "alibi":          "alibi",
}

print("=" * 55)
print("  LESSON 53: Crime & Justice")
print("=" * 55)

print("\n📚 CRIMES:")
print("-" * 55)
items = list(CRIMES.items())
for i in range(0, len(items), 2):
    row = items[i:i+2]
    print("  " + "   ".join(f"{en:<24}{cz:<22}" for en, cz in row))

print("\n📚 CRIMINALS:")
print("-" * 55)
items = list(CRIMINALS.items())
for i in range(0, len(items), 3):
    row = items[i:i+3]
    print("  " + "   ".join(f"{en:<16}{cz:<16}" for en, cz in row))

print("\n📚 LEGAL PROCESS:")
print("-" * 55)
for en, cz in LEGAL_SYSTEM.items():
    print(f"  {en:<26} {cz}")

print("\n📝 CRIME + CRIMINAL pattern:")
print("-" * 55)
patterns = [("theft","thief"), ("burglary","burglar"), ("murder","murderer"),
            ("fraud","fraudster"), ("arson","arsonist"), ("robbery","robber")]
for crime, criminal in patterns:
    print(f"  {crime:<18} → {criminal}")

print("\n💬 TALKING ABOUT CRIME:")
print("-" * 55)
phrases = [
    ("She was charged with fraud and sentenced to 3 years.",
     "Byla obviněna z podvodu a odsouzena na 3 roky."),
    ("The suspect was arrested but later acquitted.",
     "Podezřelý byl zatčen, ale později zproštěn viny."),
    ("Crime rates have fallen significantly over the past decade.",
     "Kriminalita výrazně poklesla za poslední desetiletí."),
]
for en, cz in phrases:
    print(f"  {en}")
    print(f"    → {cz}\n")

print("\n🎯 QUIZ:")
print("-" * 55)
all_vocab = {**CRIMES, **CRIMINALS, **LEGAL_SYSTEM}
pairs = random.sample(list(all_vocab.items()), 8)
score = 0
for en, cz in pairs:
    ans = input(f"  {cz}  →  ").strip()
    if ans.lower() == en.lower():
        print("  ✓ Correct!\n"); score += 1
    else:
        print(f"  ✗ Answer: {en}\n")
print(f"  Score: {score}/8")

# YOUR TASK:
# 1. Describe a crime you read about in the news using vocabulary from this lesson
# 2. Write a short newspaper report about a fictional crime (use passive voice)
# 3. Discuss: Should non-violent offenders go to prison? Use for/against structure.
