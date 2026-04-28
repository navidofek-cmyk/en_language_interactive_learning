"""
LESSON 22: Work & Jobs
========================
⭐⭐ Level: A2–B1 | Elementary

Povolání, práce a pracovní pohovor.
Topics: jobs · workplace · job interview · work phrases
"""
import random

JOBS = {
    "engineer":      "inženýr/ka",      "doctor":       "lékař/ka",
    "nurse":         "zdravotní sestra/bratr", "teacher": "učitel/ka",
    "lawyer":        "právník/čka",     "accountant":   "účetní",
    "architect":     "architekt/ka",    "programmer":   "programátor/ka",
    "designer":      "designér/ka",     "journalist":   "novinář/ka",
    "manager":       "manažer/ka",      "sales rep":    "obchodní zástupce",
    "mechanic":      "mechanik/čka",    "electrician":  "elektrikář/ka",
    "chef":          "šéfkuchař/ka",    "waiter/waitress": "číšník/servírka",
    "driver":        "řidič/ka",        "pilot":        "pilot/ka",
    "police officer":"policista/ka",    "firefighter":  "hasič/ka",
    "scientist":     "vědec/vědkyně",   "researcher":   "výzkumník/ce",
}

WORKPLACE = {
    "office":        "kancelář",        "factory":      "továrna",
    "hospital":      "nemocnice",       "school":       "škola",
    "laboratory":    "laboratoř",       "site":         "staveniště",
    "warehouse":     "sklad",           "remote":       "vzdáleně/home office",
    "shift work":    "směnný provoz",   "overtime":     "přesčas",
    "salary":        "plat (měsíční)",  "wage":         "mzda (hodinová)",
    "contract":      "smlouva",         "CV / résumé":  "životopis",
    "interview":     "pohovor",         "promotion":    "povýšení",
    "deadline":      "termín",          "colleague":    "kolega/kolegyně",
}

INTERVIEW_PHRASES = {
    "Tell me about yourself.":
        "Řekněte mi o sobě.",
    "What are your strengths?":
        "Jaké jsou vaše silné stránky?",
    "What are your weaknesses?":
        "Jaké jsou vaše slabé stránky?",
    "Why do you want this job?":
        "Proč chcete tuto práci?",
    "Where do you see yourself in 5 years?":
        "Kde se vidíte za 5 let?",
    "I have experience in ...":
        "Mám zkušenosti v oblasti ...",
    "I'm a good team player.":
        "Jsem dobrý/á týmový/á hráč/ka.",
    "I work well under pressure.":
        "Dobře pracuji pod tlakem.",
    "I'm looking for new challenges.":
        "Hledám nové výzvy.",
    "What does the role involve?":
        "Co tato pozice zahrnuje?",
    "What is the salary range?":
        "Jaký je platový rozsah?",
}

print("=" * 55)
print("  LESSON 22: Work & Jobs")
print("=" * 55)

print("\n📚 JOBS:")
print("-" * 55)
items = list(JOBS.items())
for i in range(0, len(items), 2):
    row = items[i:i+2]
    print("  " + "   ".join(f"{en:<20}{cz:<22}" for en, cz in row))

print("\n📚 WORKPLACE VOCABULARY:")
print("-" * 55)
for en, cz in WORKPLACE.items():
    print(f"  {en:<20} {cz}")

print("\n📝 GRAMMAR — job descriptions:")
print("-" * 55)
print("  I am an engineer.      (NOT: I am engineer)")
print("  She works AS a nurse.  (works as = pracuje jako)")
print("  He works FOR a bank.   (works for = pracuje pro)")
print("  I work IN an office.   (works in = pracuje v)")

print("\n📚 JOB INTERVIEW PHRASES:")
print("-" * 55)
for en, cz in INTERVIEW_PHRASES.items():
    print(f"  {en}")
    print(f"    → {cz}\n")

print("\n💬 INTERVIEW DIALOGUE:")
print("-" * 55)
dialogue = [
    ("Interviewer", "Can you tell me a bit about your background?"),
    ("Candidate",   "Of course. I've worked as a software engineer for five years."),
    ("Interviewer", "What are your main strengths?"),
    ("Candidate",   "I'm analytical, I work well under pressure, and I'm a good communicator."),
    ("Interviewer", "Why are you leaving your current job?"),
    ("Candidate",   "I'm looking for new challenges and opportunities to grow."),
    ("Interviewer", "Do you have any questions for us?"),
    ("Candidate",   "Yes — what does a typical day in this role look like?"),
]
for speaker, line in dialogue:
    print(f"  {speaker}: {line}")

print("\n🎯 QUIZ — přelož povolání:")
print("-" * 55)
pairs = random.sample(list(JOBS.items()), 7)
score = 0
for en, cz in pairs:
    ans = input(f"  {cz}  →  ").strip()
    if ans.lower() == en.lower():
        print("  ✓ Correct!\n"); score += 1
    else:
        print(f"  ✗ Answer: {en}\n")
print(f"  Score: {score}/7")

# YOUR TASK:
# 1. Describe your job (or dream job) in 5 English sentences
# 2. Prepare answers to the 5 most common interview questions
# 3. Write a short cover letter (6–8 sentences) for a job you'd like
