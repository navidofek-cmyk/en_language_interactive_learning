"""
LESSON 26: Phrasal Verbs
==========================
⭐⭐⭐ Level: B1 | Pre-Intermediate

Frázová slovesa — 60 nejběžnějších s příklady.
Topics: separable · inseparable · daily routines · relationships · work
"""
import random

PHRASAL_VERBS = {
    # Daily life
    "get up":      ("vstát z postele",         "I get up at 6 every morning."),
    "wake up":     ("probudit se",              "She woke up late today."),
    "turn on":     ("zapnout",                  "Turn on the lights please."),
    "turn off":    ("vypnout",                  "Turn off your phone."),
    "pick up":     ("zvednout, vyzvednout",     "Can you pick me up at 8?"),
    "drop off":    ("odvézt/odložit",           "I'll drop you off at the station."),
    "put on":      ("obléknout si",             "Put on your coat."),
    "take off":    ("svléknout si / vzlétnout", "Take off your shoes."),
    "look for":    ("hledat",                   "I'm looking for my keys."),
    "find out":    ("zjistit",                  "I found out she was lying."),
    "give up":     ("vzdát se",                 "Don't give up!"),
    "carry on":    ("pokračovat",               "Carry on with your work."),
    "run out of":  ("dojít (zásoby)",           "We've run out of milk."),
    "throw away":  ("vyhodit",                  "Throw away those old newspapers."),
    "tidy up":     ("uklidit",                  "Tidy up your room!"),
    # Relationships
    "get on with": ("vycházet s někým",         "I get on well with my colleagues."),
    "fall out with":("pohádat se",              "She fell out with her sister."),
    "make up":     ("usmířit se / nalíčit se",  "They argued but made up later."),
    "break up":    ("rozejít se",               "They broke up after 3 years."),
    "look after":  ("starat se o",              "Can you look after my cat?"),
    "look up to":  ("vzhlížet k",               "I look up to my father."),
    "let down":    ("zklamat",                  "Don't let me down."),
    # Work/Study
    "set up":      ("založit, zřídit",          "She set up her own business."),
    "work out":    ("cvičit / vyjít",           "This plan might not work out."),
    "hand in":     ("odevzdat",                 "Hand in your homework."),
    "take on":     ("přijmout (práci/úkol)",    "We're taking on new staff."),
    "come up with":("vymyslet",                 "She came up with a great idea."),
    "deal with":   ("zabývat se, řešit",        "How do you deal with stress?"),
    "go over":     ("projít si znovu",          "Let's go over the main points."),
    "put off":     ("odložit",                  "Don't put off until tomorrow."),
    # Movement
    "get in/out":  ("nastoupit/vystoupit (auto)","Get in the car."),
    "get on/off":  ("nastoupit/vystoupit (bus)","Get off at the next stop."),
    "come back":   ("vrátit se",                "I'll come back at 5."),
    "go back":     ("vrátit se (tam)",          "I want to go back to Prague."),
    "show up":     ("dostavit se",              "He never showed up."),
    "set off":     ("vydat se na cestu",        "We set off at dawn."),
    # Feelings
    "cheer up":    ("rozveselit se",            "Cheer up! It'll be OK."),
    "calm down":   ("uklidnit se",              "Calm down and breathe."),
    "put up with": ("snášet, tolerovat",        "I can't put up with this noise."),
    "get over":    ("překonat",                 "It took months to get over it."),
    # Communication
    "call back":   ("zavolat zpět",             "I'll call you back later."),
    "hang up":     ("zavěsit telefon",          "She hung up before I could speak."),
    "bring up":    ("zmínit / vychovat",        "Don't bring up politics at dinner."),
    "point out":   ("upozornit na",             "He pointed out my mistake."),
}

print("=" * 55)
print("  LESSON 26: Phrasal Verbs")
print("=" * 55)
print("\n  Phrasal verb = verb + particle (changes the meaning!)")
print("  get → get up / get on / get over / get out of ...")

categories = {
    "Daily life":     ["get up","wake up","turn on","turn off","pick up","drop off",
                       "put on","take off","look for","find out","give up","carry on",
                       "run out of","throw away","tidy up"],
    "Relationships":  ["get on with","fall out with","make up","break up","look after",
                       "look up to","let down"],
    "Work / Study":   ["set up","work out","hand in","take on","come up with",
                       "deal with","go over","put off"],
    "Movement":       ["get in/out","get on/off","come back","go back","show up","set off"],
    "Feelings":       ["cheer up","calm down","put up with","get over"],
    "Communication":  ["call back","hang up","bring up","point out"],
}

for category, verbs in categories.items():
    print(f"\n📚 {category.upper()}:")
    print("-" * 55)
    for verb in verbs:
        if verb in PHRASAL_VERBS:
            meaning, example = PHRASAL_VERBS[verb]
            print(f"  {verb:<18} {meaning}")
            print(f"    → {example}\n")

print("\n🎯 QUIZ — meaning in Czech:")
print("-" * 55)
pairs = random.sample(list(PHRASAL_VERBS.items()), 8)
score = 0
for verb, (meaning, example) in pairs:
    print(f"  '{verb}'  →  what does it mean?")
    ans = input("  → ").strip()
    print(f"  ✓ Meaning: {meaning}")
    print(f"     Example: {example}\n")
    score += 1  # self-check
print(f"  Reviewed {score} phrasal verbs!")

# YOUR TASK:
# 1. Choose 10 phrasal verbs and write a sentence for each using your own life
# 2. Find 5 phrasal verbs you didn't know — look them up and learn them
# 3. Write a short story (10 sentences) using at least 8 phrasal verbs
