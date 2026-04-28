"""
LESSON 46: Inversion
======================
⭐⭐⭐⭐ Level: B2–C1 | Upper-Intermediate

Inverze — zdůraznění větnou inverzí (formální/literární styl).
Topics: negative adverbials · conditional inversion · formal emphasis
"""
import random

NEGATIVE_ADVERBIALS = [
    ("Never",         "Never have I seen such a beautiful sunset.",
                      "Nikdy jsem neviděl/a tak krásný západ slunce."),
    ("Rarely",        "Rarely does she complain about anything.",
                      "Jen zřídka si na cokoliv stěžuje."),
    ("Seldom",        "Seldom had he felt so nervous.",
                      "Jen zřídka se cítil tak nervózní."),
    ("Hardly",        "Hardly had I sat down when the phone rang.",
                      "Sotva jsem si sedl/a, zazvonil telefon."),
    ("No sooner",     "No sooner had she left than it started raining.",
                      "Sotva odešla, začalo pršet."),
    ("Not only",      "Not only did he lie, but he also stole money.",
                      "Nejenže lhal, ale také ukradl peníze."),
    ("Not until",     "Not until midnight did they finally arrive.",
                      "Teprve o půlnoci konečně přijeli."),
    ("Only then",     "Only then did I realise my mistake.",
                      "Teprve tehdy jsem si uvědomil/a svou chybu."),
    ("Only by",       "Only by working hard can you succeed.",
                      "Jen tvrdou prací lze uspět."),
    ("On no account", "On no account should you open that door.",
                      "Za žádných okolností nesmíte otevřít ty dveře."),
    ("Under no circumstances",
                      "Under no circumstances will we accept this.",
                      "Za žádných okolností to nepřijmeme."),
    ("Little",        "Little did she know what awaited her.",
                      "Málokdo věděl, co ji čeká."),
    ("In no way",     "In no way is this acceptable.",
                      "Toto není v žádném případě přijatelné."),
]

CONDITIONAL_INVERSION = [
    ("If I had known → Had I known",
     "Had I known the truth, I would have acted differently.",
     "Kdybych byl/a znal/a pravdu, byl/a bych jednal/a jinak."),
    ("If it were → Were it",
     "Were it not for your help, I would have failed.",
     "Nebýt vaší pomoci, byl/a bych selhal/a."),
    ("If it should happen → Should it happen",
     "Should you need any help, please call me.",
     "Pokud byste potřeboval/a pomoc, zavolejte mi."),
]

print("=" * 55)
print("  LESSON 46: Inversion")
print("=" * 55)
print("\n  Inversion = auxiliary verb before subject (for emphasis)")
print("  Used in formal writing, speeches, literature.\n")

print("\n📚 NEGATIVE ADVERBIALS + INVERSION:")
print("-" * 55)
print("  Structure: negative adverb + auxiliary + subject + verb\n")
for adv, en, cz in NEGATIVE_ADVERBIALS:
    print(f"  [{adv}]")
    print(f"  {en}")
    print(f"    → {cz}\n")

print("\n📚 CONDITIONAL INVERSION (formal 'if' replacement):")
print("-" * 55)
for structure, en, cz in CONDITIONAL_INVERSION:
    print(f"  {structure}")
    print(f"  {en}")
    print(f"    → {cz}\n")

print("\n📝 PATTERN:")
print("-" * 55)
print("  Normal:   I had never felt so proud.")
print("  Inverted: Never had I felt so proud.\n")
print("  Normal:   If I had known...")
print("  Inverted: Had I known...")

print("\n🎯 QUIZ — rewrite with inversion:")
print("-" * 55)
quiz = [
    ("I have never been so embarrassed. (Never...)",
     "Never have I been so embarrassed."),
    ("If I had arrived earlier, I would have met her. (Had...)",
     "Had I arrived earlier, I would have met her."),
    ("She had hardly sat down when the alarm went off. (Hardly...)",
     "Hardly had she sat down when the alarm went off."),
    ("He not only failed the exam but also lost his scholarship. (Not only...)",
     "Not only did he fail the exam, but he also lost his scholarship."),
    ("If you should have any questions, contact me. (Should...)",
     "Should you have any questions, contact me."),
]
score = 0
for normal, inverted in quiz:
    print(f"  {normal}")
    ans = input("  → ").strip()
    if ans.lower() == inverted.lower():
        print("  ✓ Correct!\n"); score += 1
    else:
        print(f"  ✗ Answer: {inverted}\n")
print(f"  Score: {score}/5")

# YOUR TASK:
# 1. Rewrite 5 ordinary sentences using negative adverbial inversion
# 2. Rewrite these conditionals using inversion:
#    a) If he should call, tell him I'm busy.
#    b) If it weren't for the traffic, I'd be on time.
# 3. Find 3 examples of inversion in an English newspaper or novel
