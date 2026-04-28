"""
LESSON 23: Technology & Internet
===================================
⭐⭐ Level: A2–B1 | Elementary

Technologie, internet a digitální svět.
Topics: devices · internet · social media · tech verbs · cyber safety
"""
import random

DEVICES = {
    "laptop":           "notebook",        "desktop":        "stolní počítač",
    "tablet":           "tablet",          "smartphone":     "chytrý telefon",
    "smartwatch":       "chytré hodinky",  "headphones":     "sluchátka",
    "charger":          "nabíječka",       "cable":          "kabel",
    "keyboard":         "klávesnice",      "mouse":          "myš",
    "screen / monitor": "obrazovka",       "printer":        "tiskárna",
    "hard drive":       "pevný disk",      "USB stick":      "USB flash disk",
    "router":           "router",          "server":         "server",
}

INTERNET = {
    "browser":          "prohlížeč",       "website":        "webová stránka",
    "search engine":    "vyhledávač",      "download":       "stáhnout",
    "upload":           "nahrát",          "stream":         "streamovat",
    "connection":       "připojení",       "bandwidth":      "přenosová rychlost",
    "Wi-Fi":            "Wi-Fi",           "password":       "heslo",
    "username":         "uživatelské jméno","account":       "účet",
    "log in / sign in": "přihlásit se",    "log out":        "odhlásit se",
    "update":           "aktualizace",     "bug":            "chyba v programu",
    "crash":            "padnout/zhavarovat","back up":       "zálohovat",
}

SOCIAL_MEDIA = {
    "post":             "příspěvek / přidat příspěvek",
    "share":            "sdílet",          "like":           "lajkovat",
    "comment":          "komentář",        "follow":         "sledovat",
    "unfollow":         "přestat sledovat","block":          "zablokovat",
    "tag":              "označit",         "story":          "příběh (story)",
    "reel / short":     "krátké video",    "live stream":    "živé vysílání",
    "DM (direct message)":"soukromá zpráva","notification":  "oznámení",
    "trending":         "v trendu",        "viral":          "virální",
}

TECH_VERBS = [
    ("click on",   "kliknout na"),      ("scroll",     "scrollovat"),
    ("swipe",      "přejet prstem"),    ("zoom in/out","přiblížit/oddálit"),
    ("copy/paste", "kopírovat/vložit"), ("drag",       "přetáhnout"),
    ("install",    "nainstalovat"),     ("delete",     "smazat"),
    ("save",       "uložit"),           ("attach",     "přiložit"),
]

print("=" * 55)
print("  LESSON 23: Technology & Internet")
print("=" * 55)

print("\n📚 DEVICES:")
print("-" * 55)
items = list(DEVICES.items())
for i in range(0, len(items), 2):
    row = items[i:i+2]
    print("  " + "   ".join(f"{en:<22}{cz:<20}" for en, cz in row))

print("\n📚 INTERNET VOCABULARY:")
print("-" * 55)
for en, cz in INTERNET.items():
    print(f"  {en:<24} {cz}")

print("\n📚 SOCIAL MEDIA:")
print("-" * 55)
for en, cz in SOCIAL_MEDIA.items():
    print(f"  {en:<24} {cz}")

print("\n📚 TECH VERBS:")
print("-" * 55)
for en, cz in TECH_VERBS:
    print(f"  {en:<20} {cz}")

print("\n📝 USEFUL PHRASES:")
print("-" * 55)
phrases = [
    "My phone has run out of battery.",
    "The Wi-Fi is really slow today.",
    "I can't log in — I've forgotten my password.",
    "Can you send me the file as an attachment?",
    "I need to update my operating system.",
    "The app keeps crashing.",
    "Make sure you back up your data.",
]
for p in phrases:
    print(f"  {p}")

print("\n🎯 QUIZ — přelož do angličtiny:")
print("-" * 55)
all_vocab = {**DEVICES, **INTERNET, **SOCIAL_MEDIA}
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
# 1. Describe your phone / computer setup in English (5–7 sentences)
# 2. Write instructions for a non-technical person on how to:
#    a) set up a new email account  b) share a photo on social media
# 3. Write a short paragraph: What technology could you not live without, and why?
