"""
LESSON 28: Business English
=============================
⭐⭐⭐ Level: B1–B2 | Pre-Intermediate

Obchodní angličtina — emaily, schůzky a prezentace.
Topics: formal emails · meetings · presentations · negotiation
"""
import random

EMAIL_PHRASES = {
    "Opening": {
        "Dear Mr/Ms [surname],":      "Vážený pane/Vážená paní,",
        "Dear [first name],":         "Milý/á ...,",
        "To whom it may concern,":    "Vážení,",
        "I am writing to enquire about...": "Píšu vám ohledně ...",
        "I am writing with reference to...":"Odkazuji na ...",
        "Further to your email,...":  "V návaznosti na váš email,...",
    },
    "Body": {
        "I would like to inform you that...": "Rád/a bych vás informoval/a, že ...",
        "Please find attached...":      "V příloze naleznete ...",
        "I would appreciate it if...":  "Byl/a bych vděčný/á, kdybyste ...",
        "Could you please...":          "Mohl/a byste prosím ...",
        "I am afraid that...":          "Bohužel ...",
        "As agreed...":                 "Jak jsme se dohodli ...",
        "I am pleased to confirm...":   "S potěšením potvrzuji ...",
    },
    "Closing": {
        "Please do not hesitate to contact me.": "Neváhejte mě kontaktovat.",
        "I look forward to hearing from you.":   "Těším se na vaši odpověď.",
        "I look forward to meeting you.":        "Těším se na setkání s vámi.",
        "Kind regards,":                         "S pozdravem,",
        "Best regards,":                         "S přátelským pozdravem,",
        "Yours sincerely,":                      "S úctou, (known recipient)",
        "Yours faithfully,":                     "S úctou, (Dear Sir/Madam)",
    },
}

MEETING_PHRASES = {
    "Shall we get started?":          "Začneme?",
    "Let's move on to the next point.":"Přejdeme k dalšímu bodu.",
    "Could I just come in here?":     "Mohu se vložit?",
    "To sum up,...":                  "Shrneme-li,...",
    "Can we table that for now?":     "Odložíme to na potom?",
    "I'd like to raise a point.":     "Rád/a bych zmínil/a...",
    "That's outside the scope of today's meeting.":"To je nad rámec dnešní schůzky.",
    "Let's take a vote on this.":     "Hlasujme o tom.",
    "We'll circulate the minutes.":   "Pošleme zápis ze schůzky.",
    "Let's schedule a follow-up.":    "Naplánujme navazující schůzku.",
}

PRESENTATION_PHRASES = [
    ("Opening",     "Good morning. I'd like to talk to you today about..."),
    ("Overview",    "I've divided my presentation into three parts."),
    ("Transition",  "Moving on to my next point..."),
    ("Emphasise",   "What I'd like to highlight here is..."),
    ("Graph",       "As you can see from this slide..."),
    ("Conclusion",  "To conclude, I'd like to summarise the key points."),
    ("Q&A",         "I'd be happy to take any questions now."),
]

NEGOTIATION = {
    "That's not quite what we had in mind.":"To není úplně to, co jsme měli na mysli.",
    "We could meet you halfway.":          "Mohli bychom jít na kompromis.",
    "That's a fair point.":                "To je oprávněný argument.",
    "Could you be more flexible on...?":   "Mohli byste být pružnější, pokud jde o ...?",
    "Let me check with my team.":          "Poradím se se svým týmem.",
    "I think we can work with that.":      "Myslím, že s tím pracovat lze.",
    "We need to see a better offer.":      "Potřebujeme lepší nabídku.",
    "It's a deal.":                        "Máme dohodu.",
}

print("=" * 55)
print("  LESSON 28: Business English")
print("=" * 55)

for section, phrases in EMAIL_PHRASES.items():
    print(f"\n📚 EMAIL — {section.upper()}:")
    print("-" * 55)
    for en, cz in phrases.items():
        print(f"  {en}")
        print(f"    → {cz}\n")

print("\n📚 MEETING PHRASES:")
print("-" * 55)
for en, cz in MEETING_PHRASES.items():
    print(f"  {en:<44} → {cz}")

print("\n📚 PRESENTATION STRUCTURE:")
print("-" * 55)
for stage, phrase in PRESENTATION_PHRASES:
    print(f"  [{stage}]  {phrase}")

print("\n📚 NEGOTIATION:")
print("-" * 55)
for en, cz in NEGOTIATION.items():
    print(f"  {en}")
    print(f"    → {cz}\n")

print("\n✏️  WRITING TASK:")
print("-" * 55)
print("  Write a formal email using these details:")
print("  • You are enquiring about a product/service")
print("  • Ask for pricing and availability")
print("  • Mention you saw their website")
print("  • Close professionally\n")
email = []
print("  Type your email (press Enter twice to finish):")
while True:
    line = input("  ")
    if line == "" and email and email[-1] == "":
        break
    email.append(line)
print("\n  Your email:")
print("-" * 55)
for line in email:
    if line: print(f"  {line}")

# YOUR TASK:
# 1. Write a complete formal email requesting a meeting (8–10 lines)
# 2. Write a complaint email about a delayed delivery
# 3. Prepare a 3-minute presentation outline on a topic you know well
