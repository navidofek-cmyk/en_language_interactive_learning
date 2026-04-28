"""
LESSON 27: Common Idioms
==========================
⭐⭐⭐ Level: B1 | Pre-Intermediate

Nejběžnější anglické idiomy — výrazy, které nelze přeložit doslova.
Topics: body idioms · time · feelings · work · everyday idioms
"""
import random

IDIOMS = {
    # Body
    "cost an arm and a leg":    ("být velmi drahý",           "That new laptop cost an arm and a leg."),
    "keep an eye on":           ("hlídat, dohlížet na",       "Can you keep an eye on my bag?"),
    "pull someone's leg":       ("dělat si z někoho legraci","Are you serious or pulling my leg?"),
    "face the music":           ("čelit následkům",           "He made a mistake and had to face the music."),
    "get cold feet":            ("dostat strach na poslední chvíli","She got cold feet before the wedding."),
    "bite off more than you can chew":("vzít si víc než zvládneš","I bit off more than I could chew this semester."),
    "turn a blind eye":         ("přimhouřit oko",            "He turned a blind eye to the problem."),
    "have butterflies":         ("mít motýly v břiše (nervozita)","I had butterflies before the interview."),
    # Time
    "once in a blue moon":      ("jednou za uherský rok",     "We visit them once in a blue moon."),
    "in the nick of time":      ("na poslední chvíli",        "We arrived in the nick of time."),
    "hit the nail on the head": ("trefit hřebík na hlavičku", "You hit the nail on the head."),
    "under the weather":        ("být pod psa / nemocný",     "I'm feeling under the weather today."),
    # Feelings / situations
    "break the ice":            ("prolomit ledy",             "He told a joke to break the ice."),
    "spill the beans":          ("prásknout, vyzradit tajemství","Who spilled the beans about the surprise?"),
    "bite the bullet":          ("skousnout to",              "Bite the bullet and go to the dentist."),
    "add fuel to the fire":     ("přilít olej do ohně",       "His comment just added fuel to the fire."),
    "the last straw":           ("přetékající pohár",         "That was the last straw — I quit."),
    "hit the sack":             ("jít na kutě (spát)",        "I'm exhausted. I'm going to hit the sack."),
    "be in hot water":          ("být v malvéru, mít potíže", "He's in hot water with his boss."),
    # Work / effort
    "burn the midnight oil":    ("pracovat do noci",          "She burned the midnight oil to finish the report."),
    "get the ball rolling":     ("rozhýbat věci",             "Let's get the ball rolling on this project."),
    "go back to the drawing board":("začít od začátku",       "The plan failed — back to the drawing board."),
    "bite the hand that feeds you":("kousat do ruky, která tě krmí","Don't bite the hand that feeds you."),
    "think outside the box":    ("myslet kreativně, mimo rámeček","We need to think outside the box here."),
    # Everyday
    "it's raining cats and dogs":("lije jako z konve",        "Take an umbrella — it's raining cats and dogs."),
    "a blessing in disguise":   ("požehnání v přestrojení",  "Losing that job was a blessing in disguise."),
    "kill two birds with one stone":("zabít dvě mouchy jednou ranou","I'll kill two birds with one stone."),
    "bite the dust":            ("selhat / zemřít / zhroutit se","Another company has bitten the dust."),
    "the ball is in your court":("míč je na tvé straně (tvůj tah)","I've offered help — the ball is in your court."),
    "speak of the devil":       ("vzpomínali jsme na tebe!",  "Speak of the devil — here comes Jan."),
}

print("=" * 55)
print("  LESSON 27: Common Idioms")
print("=" * 55)
print("\n  Idiom = fixed phrase with non-literal meaning")
print("  'It's raining cats and dogs' ≠ skutečné kočky a psi!\n")

categories = {
    "Body idioms":    ["cost an arm and a leg","keep an eye on","pull someone's leg",
                       "face the music","get cold feet","bite off more than you can chew",
                       "turn a blind eye","have butterflies"],
    "Time & situations":["once in a blue moon","in the nick of time","under the weather",
                         "hit the nail on the head"],
    "Feelings":       ["break the ice","spill the beans","bite the bullet",
                       "add fuel to the fire","the last straw","hit the sack","be in hot water"],
    "Work & effort":  ["burn the midnight oil","get the ball rolling",
                       "go back to the drawing board","think outside the box"],
    "Everyday":       ["it's raining cats and dogs","a blessing in disguise",
                       "kill two birds with one stone","the ball is in your court","speak of the devil"],
}

for cat, idiom_list in categories.items():
    print(f"\n📚 {cat.upper()}:")
    print("-" * 55)
    for idiom in idiom_list:
        if idiom in IDIOMS:
            meaning, example = IDIOMS[idiom]
            print(f"  '{idiom}'")
            print(f"    = {meaning}")
            print(f"    e.g. {example}\n")

print("\n🎯 QUIZ — what does it mean?")
print("-" * 55)
pairs = random.sample(list(IDIOMS.items()), 6)
score = 0
for idiom, (meaning, example) in pairs:
    print(f"  '{idiom}'")
    ans = input("  Meaning: ").strip()
    print(f"  ✓ {meaning}")
    print(f"     e.g. {example}\n")
    score += 1
print(f"  Reviewed {score} idioms!")

# YOUR TASK:
# 1. Choose 5 idioms and use each in your own sentence about real life
# 2. Find 3 idioms you've heard in films or songs — look up their meanings
# 3. Write a short story using at least 6 idioms from this lesson
