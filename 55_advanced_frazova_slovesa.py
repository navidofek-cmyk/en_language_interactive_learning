"""
LESSON 55: Advanced Phrasal Verbs — C1
=========================================
⭐⭐⭐⭐ Level: B2–C1 | Upper-Intermediate

Pokročilá frázová slovesa — 50 pro úroveň C1.
Topics: formal contexts · abstract meanings · multiple meanings
"""
import random

PHRASAL_VERBS_C1 = {
    # Thinking / opinion
    "account for":      ("vysvětlit, tvořit (podíl)",  "How do you account for the difference?"),
    "come to terms with":("smířit se s",               "She came to terms with the diagnosis."),
    "draw on":          ("čerpat z",                   "He drew on years of experience."),
    "dwell on":         ("zabývat se, přemítat o",     "Don't dwell on past mistakes."),
    "grapple with":     ("potýkat se s",               "We're grappling with a complex issue."),
    "build on":         ("stavět na, rozvíjet",         "We need to build on this success."),
    "stem from":        ("pramenit z, vznikat kvůli",  "The problem stems from poor communication."),
    "boil down to":     ("v podstatě jde o",           "It all boils down to trust."),

    # Change / development
    "phase out":        ("postupně vyřadit",           "They're phasing out diesel engines."),
    "phase in":         ("postupně zavádět",           "The new system is being phased in."),
    "iron out":         ("vyřešit (problémy)",         "We need to iron out a few issues."),
    "smooth over":      ("zahladit, vyhladit",         "He tried to smooth over the conflict."),
    "scale up":         ("navýšit, rozšířit",          "We need to scale up production."),
    "wind down":        ("utlumit, ukončovat",         "The company is winding down."),
    "spin off":         ("oddělit jako novou společnost","The software division was spun off."),

    # Work / achievement
    "follow through":   ("dotáhnout do konce",         "He rarely follows through on promises."),
    "see through":      ("prohlédnout / dotáhnout",    "I saw through his lies."),
    "carry out":        ("provést, uskutečnit",        "The research was carried out last year."),
    "embark on":        ("pustit se do, začít",        "They're embarking on a new project."),
    "pull off":         ("podařit se, provést",        "She pulled off an amazing presentation."),
    "live up to":       ("dostát, splnit očekávání",   "It didn't live up to expectations."),
    "fall short of":    ("nesplnit, nedosáhnout",      "Sales fell short of targets."),
    "measure up to":    ("obstát, splnit požadavky",   "He didn't measure up to the standard."),

    # Communication
    "allude to":        ("narážet na, naznačovat",     "She alluded to recent changes."),
    "elaborate on":     ("rozvinout, rozvést",         "Could you elaborate on that point?"),
    "gloss over":       ("přejít, bagatelizovat",      "She glossed over the problems."),
    "play down":        ("bagatelizovat, zlehčovat",   "He played down the significance."),
    "play up":          ("zdůraznit, nadsadit",        "The media played up the story."),
    "back up":          ("podpořit důkazy / zálohovat","Can you back up that claim?"),

    # Relationships
    "fall out with":    ("pohádat se s",               "He fell out with his business partner."),
    "drift apart":      ("oddálit se (od sebe)",       "Old friends tend to drift apart."),
    "make up for":      ("vyvážit, napravit",          "Hard work makes up for lack of talent."),
    "stand by":         ("stát při, podpořit",         "I'll stand by you whatever happens."),
    "look down on":     ("dívat se spatra na",         "She looks down on people who lie."),
    "warm to":          ("začít mít rádi",             "I'm starting to warm to the idea."),

    # Money / business
    "write off":        ("odepsat (daňově/dluh)",      "They wrote off bad debts."),
    "bail out":         ("zachránit (finančně)",       "The government bailed out the bank."),
    "cash in on":       ("vytěžit z, využít",          "He cashed in on the property boom."),
    "fork out":         ("vysolit (peníze)",           "I had to fork out £500 for repairs."),
}

categories = {
    "Thinking & opinion":     ["account for","come to terms with","draw on","dwell on",
                               "grapple with","build on","stem from","boil down to"],
    "Change & development":   ["phase out","phase in","iron out","smooth over",
                               "scale up","wind down","spin off"],
    "Work & achievement":     ["follow through","see through","carry out","embark on",
                               "pull off","live up to","fall short of","measure up to"],
    "Communication":          ["allude to","elaborate on","gloss over","play down","play up","back up"],
    "Relationships":          ["fall out with","drift apart","make up for","stand by",
                               "look down on","warm to"],
    "Money & business":       ["write off","bail out","cash in on","fork out"],
}

print("=" * 55)
print("  LESSON 55: Advanced Phrasal Verbs — C1")
print("=" * 55)

for cat, verbs in categories.items():
    print(f"\n📚 {cat.upper()}:")
    print("-" * 55)
    for verb in verbs:
        if verb in PHRASAL_VERBS_C1:
            meaning, example = PHRASAL_VERBS_C1[verb]
            print(f"  {verb:<24} {meaning}")
            print(f"    → {example}\n")

print("\n🎯 QUIZ — meaning:")
print("-" * 55)
pairs = random.sample(list(PHRASAL_VERBS_C1.items()), 8)
score = 0
for verb, (meaning, example) in pairs:
    print(f"  '{verb}'")
    print(f"  e.g. {example}")
    print(f"  Meaning: {meaning}\n")
    score += 1
print(f"  Reviewed {score} phrasal verbs!")

# YOUR TASK:
# 1. Write 10 sentences using phrasal verbs from the Work & Achievement section
# 2. Replace these informal/simple phrases with phrasal verbs from this lesson:
#    a) "The problem originates from budget cuts."
#    b) "She minimised the importance of the mistake."
#    c) "The plan didn't achieve the required standard."
# 3. Write a business email using at least 5 phrasal verbs from this lesson
