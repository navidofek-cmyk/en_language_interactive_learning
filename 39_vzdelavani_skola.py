"""
LESSON 39: Education & School
================================
⭐⭐ Level: A2–B1 | Elementary

Vzdělání, škola a britský vzdělávací systém.
Topics: school subjects · UK education system · studying · qualifications
"""
import random

SUBJECTS = {
    "Maths / Mathematics": "matematika",
    "English":             "angličtina",
    "Science":             "přírodověda / věda",
    "Physics":             "fyzika",
    "Chemistry":           "chemie",
    "Biology":             "biologie",
    "History":             "dějepis",
    "Geography":           "zeměpis",
    "Art":                 "výtvarná výchova",
    "Music":               "hudební výchova",
    "PE (Physical Education)": "tělesná výchova",
    "ICT":                 "informatika",
    "Languages":           "jazyky",
    "Economics":           "ekonomie",
    "Philosophy":          "filozofie",
}

UK_SYSTEM = {
    "Primary school":      "základní škola (4–11 let)",
    "Secondary school":    "střední škola (11–16 let)",
    "Sixth form / college":"vyšší ročníky / college (16–18 let)",
    "University":          "univerzita (18+)",
    "GCSEs":               "státní zkoušky v 16 letech",
    "A-levels":            "maturita v 18 letech",
    "Bachelor's degree":   "bakalář (BA/BSc)",
    "Master's degree":     "magistr (MA/MSc)",
    "PhD":                 "doktorát",
    "term":                "trimest / pololetí",
    "semester":            "semestr",
    "tuition fee":         "školné",
    "scholarship":         "stipendium",
    "gap year":            "rok přestávky po škole",
}

STUDY_VERBS = {
    "revise":       "opakovat látku",
    "revise for":   "připravovat se na (zkoušku)",
    "sit an exam":  "skládat zkoušku (brit.)",
    "take an exam": "skládat zkoušku (am.)",
    "pass":         "udělat (zkoušku)",
    "fail":         "neudělat (zkoušku)",
    "retake":       "opakovat zkoušku",
    "graduate":     "promovat, absolvovat",
    "drop out":     "nedokončit školu",
    "apply to":     "přihlásit se na",
    "enrol in":     "zapsat se na",
    "attend":       "navštěvovat (hodiny)",
    "skip":         "vynechat (hodinu)",
    "hand in":      "odevzdat",
    "deadline":     "termín odevzdání",
    "dissertation": "diplomová práce",
    "plagiarism":   "plagiátorství",
}

print("=" * 55)
print("  LESSON 39: Education & School")
print("=" * 55)

print("\n📚 SCHOOL SUBJECTS:")
print("-" * 55)
items = list(SUBJECTS.items())
for i in range(0, len(items), 2):
    row = items[i:i+2]
    print("  " + "   ".join(f"{en:<28}{cz:<20}" for en, cz in row))

print("\n📚 UK EDUCATION SYSTEM:")
print("-" * 55)
for en, cz in UK_SYSTEM.items():
    print(f"  {en:<26} {cz}")

print("\n📚 STUDY VOCABULARY:")
print("-" * 55)
for en, cz in STUDY_VERBS.items():
    print(f"  {en:<20} {cz}")

print("\n📝 COMMON MISTAKES:")
print("-" * 55)
print("  ✓ I am AT university. (NE: in university)")
print("  ✓ I study AT Oxford.  (NE: in Oxford University)")
print("  ✓ I passed the exam.  (NE: I passed the exam test)")
print("  ✓ I failed the exam.  (NE: I didn't pass the exam — both correct but 'failed' is direct)")
print("  ✓ I took a gap year.  (NE: I made a gap year)")

print("\n💬 TALKING ABOUT EDUCATION:")
print("-" * 55)
phrases = [
    ("What did you study at university?",
     "Co jsi studoval/a na univerzitě?"),
    ("I graduated in Engineering from Brno University.",
     "Absolvoval/a jsem inženýrství na VUT Brno."),
    ("I'm currently doing a Master's in Computer Science.",
     "Momentálně dělám magistra z informatiky."),
    ("I had to retake my maths exam twice.",
     "Musel/a jsem opakovat zkoušku z matematiky dvakrát."),
]
for en, cz in phrases:
    print(f"  {en}")
    print(f"    → {cz}\n")

print("\n🎯 QUIZ:")
print("-" * 55)
all_vocab = {**SUBJECTS, **STUDY_VERBS}
pairs = random.sample(list(all_vocab.items()), 7)
score = 0
for en, cz in pairs:
    ans = input(f"  {cz}  →  ").strip()
    if ans.lower() == en.lower():
        print("  ✓ Correct!\n"); score += 1
    else:
        print(f"  ✗ Answer: {en}\n")
print(f"  Score: {score}/7")

# YOUR TASK:
# 1. Describe your educational background in 5–7 sentences
# 2. Compare the Czech and British education systems (3 similarities, 3 differences)
# 3. Write advice for a student starting university (use should/must/need to)
