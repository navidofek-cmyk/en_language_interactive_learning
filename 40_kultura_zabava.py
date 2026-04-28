"""
LESSON 40: Culture & Entertainment
=====================================
⭐⭐ Level: B1 | Pre-Intermediate

Kultura, zábava a jak mluvit o filmech, hudbě a knihách.
Topics: film · music · books · art · reviewing · recommendations
"""
import random

FILM_GENRES = {
    "action":       "akční",         "comedy":      "komedie",
    "drama":        "drama",         "thriller":    "thriller",
    "horror":       "horor",         "sci-fi":      "sci-fi",
    "romance":      "romantický",    "documentary": "dokumentární",
    "animation":    "animovaný",     "musical":     "muzikál",
    "crime":        "krimi",         "biopic":      "životopisný film",
    "fantasy":      "fantasy",       "western":     "western",
}

FILM_VOCAB = {
    "plot":          "děj",           "storyline":   "zápletka",
    "cast":          "obsazení",      "lead role":   "hlavní role",
    "director":      "režisér",       "screenplay":  "scénář",
    "special effects":"speciální efekty","soundtrack":"soundtrack",
    "sequel":        "pokračování",   "prequel":     "prequel",
    "box office":    "pokladna (výdělky)", "trailer": "upoutávka",
    "award-winning": "oceněný",       "critically acclaimed":"kriticky uznávaný",
    "blockbuster":   "trhák",         "flop":        "propadák",
}

MUSIC_VOCAB = {
    "genre":         "žánr",          "album":       "album",
    "track":         "skladba",       "gig / concert":"koncert",
    "lyrics":        "text písně",    "chord":       "akord",
    "live":          "naživo",        "acoustic":    "akustický",
    "catchy":        "chytlavý",      "upbeat":      "svěží, energický",
    "moving":        "dojemný",       "haunting":    "znepokojivý, líbivý",
}

REVIEW_LANGUAGE = {
    "I'd highly recommend it.":      "Vřele doporučuji.",
    "It's not really my thing.":     "Není to moc pro mě.",
    "The plot is gripping.":         "Děj je strhující.",
    "The acting is outstanding.":    "Herectví je vynikající.",
    "It's a bit slow in places.":    "Na některých místech je to trochu pomalé.",
    "The ending was disappointing.": "Konec byl zklamáním.",
    "It's thought-provoking.":       "Nutí to přemýšlet.",
    "It's a masterpiece.":           "Je to mistrovské dílo.",
    "It's overrated.":               "Je to přeceňované.",
    "I couldn't put it down.":       "Nemohl/a jsem to odložit. (book)",
    "It kept me on the edge of my seat.":"Seděl/a jsem na kraji křesla.",
}

print("=" * 55)
print("  LESSON 40: Culture & Entertainment")
print("=" * 55)

print("\n📚 FILM GENRES:")
print("-" * 55)
items = list(FILM_GENRES.items())
for i in range(0, len(items), 3):
    row = items[i:i+3]
    print("  " + "   ".join(f"{en:<14}{cz:<14}" for en, cz in row))

print("\n📚 FILM VOCABULARY:")
print("-" * 55)
for en, cz in FILM_VOCAB.items():
    print(f"  {en:<24} {cz}")

print("\n📚 MUSIC VOCABULARY:")
print("-" * 55)
for en, cz in MUSIC_VOCAB.items():
    print(f"  {en:<20} {cz}")

print("\n📚 REVIEW LANGUAGE:")
print("-" * 55)
for en, cz in REVIEW_LANGUAGE.items():
    print(f"  {en:<42} → {cz}")

print("\n💬 EXAMPLE MINI-REVIEW:")
print("-" * 55)
review = """  'Oppenheimer' (2023) — ★★★★★

  Christopher Nolan's biographical thriller about the development
  of the atomic bomb is, without doubt, one of the most
  thought-provoking films I've seen in years. The performances
  are outstanding, particularly Cillian Murphy in the lead role.
  The non-linear structure keeps you engaged throughout, though
  it can be a bit overwhelming at times. The soundtrack by
  Ludwig Göransson is haunting and perfectly atmospheric.
  I'd highly recommend it to anyone interested in history."""
print(review)

print("\n🎯 QUIZ — vocabulary:")
print("-" * 55)
all_vocab = {**FILM_VOCAB, **MUSIC_VOCAB}
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
# 1. Write a 100-word review of a film/book/album you know well
# 2. Recommend something to a friend using review language (4–5 sentences)
# 3. Describe your music taste: genres, favourite artists, what kind of music
#    you listen to in different situations
