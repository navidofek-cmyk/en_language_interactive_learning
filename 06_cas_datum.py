"""
LESSON 06: Time & Date
========================
⭐ Level: A1–A2 | Beginner

Jak říct čas, datum a dny v angličtině.
Topics: days · months · telling the time · dates · seasons
"""
import random

DAYS = {
    "Monday":    "pondělí",  "Tuesday":  "úterý",
    "Wednesday": "středa",   "Thursday": "čtvrtek",
    "Friday":    "pátek",    "Saturday": "sobota",
    "Sunday":    "neděle",
}

MONTHS = {
    "January": "leden",    "February": "únor",     "March":     "březen",
    "April":   "duben",    "May":      "květen",   "June":      "červen",
    "July":    "červenec", "August":   "srpen",    "September": "září",
    "October": "říjen",    "November": "listopad", "December":  "prosinec",
}

SEASONS = {
    "spring": "jaro",  "summer": "léto",
    "autumn / fall": "podzim", "winter": "zima",
}

TIME_PHRASES = {
    "What time is it?":    "Kolik je hodin?",
    "It's three o'clock":  "Je tři hodiny",
    "It's half past two":  "Je půl třetí (2:30)",
    "It's quarter past four": "Je čtvrt na pět (4:15)",
    "It's quarter to six": "Je tři čtvrtě na šest (5:45)",
    "in the morning":      "ráno / dopoledne",
    "in the afternoon":    "odpoledne",
    "in the evening":      "večer",
    "at night":            "v noci",
    "at noon":             "v poledne",
    "at midnight":         "o půlnoci",
}

def tell_time(hour, minute):
    if minute == 0:
        return f"It's {['twelve','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve'][hour % 12]} o'clock"
    elif minute == 30:
        return f"It's half past {['twelve','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve'][hour % 12]}"
    elif minute == 15:
        return f"It's quarter past {['twelve','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve'][hour % 12]}"
    elif minute == 45:
        next_h = (hour + 1) % 12
        return f"It's quarter to {['twelve','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve'][next_h]}"
    return f"It's {hour:02d}:{minute:02d}"

print("=" * 55)
print("  LESSON 06: Time & Date")
print("=" * 55)

print("\n📚 DAYS OF THE WEEK:")
print("-" * 55)
for en, cz in DAYS.items():
    print(f"  {en:<14} {cz}")

print("\n📚 MONTHS:")
print("-" * 55)
months = list(MONTHS.items())
for i in range(0, 12, 3):
    row = months[i:i+3]
    print("  " + "   ".join(f"{en:<12}{cz:<10}" for en, cz in row))

print("\n📚 SEASONS:")
print("-" * 55)
for en, cz in SEASONS.items():
    print(f"  {en:<20} {cz}")

print("\n📚 TELLING THE TIME:")
print("-" * 55)
for en, cz in TIME_PHRASES.items():
    print(f"  {en:<34} {cz}")

print("\n📝 DATE FORMAT:")
print("-" * 55)
print("  British:  15th March 2025  or  15/03/2025")
print("  American: March 15, 2025   or  03/15/2025")
print()
print("  'On Monday'  (NE: 'at Monday' nebo 'in Monday')")
print("  'In March'   (NE: 'on March')")
print("  'At 3 o'clock' (NE: 'in 3 o'clock')")

print("\n💬 EXAMPLES:")
print("-" * 55)
for h, m in [(9,0),(2,30),(4,15),(5,45),(11,0)]:
    print(f"  {h:02d}:{m:02d}  →  {tell_time(h, m)}")

print("\n🎯 QUIZ — days & months:")
print("-" * 55)
all_vocab = {**DAYS, **MONTHS}
pairs = random.sample(list(all_vocab.items()), 8)
score = 0
for en, cz in pairs:
    ans = input(f"  {cz}  →  ").strip()
    if ans.lower() == en.lower():
        print("  ✓ Correct!\n")
        score += 1
    else:
        print(f"  ✗ Answer: {en}\n")
print(f"  Score: {score}/8")

# YOUR TASK:
# 1. Extend tell_time() to handle all minutes (e.g. "It's ten past three")
# 2. Write a function date_to_english(day, month, year) that returns the
#    date as a British English string: date_to_english(15, 3, 2025) → "15th March 2025"
# 3. Create a clock quiz: generate random times and ask user to type them out
