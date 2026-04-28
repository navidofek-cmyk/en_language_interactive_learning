"""
LESSON 29: Pronunciation — Czech Speaker Traps
================================================
⭐⭐ Level: A2–B1 | Elementary

Nejčastější výslovnostní chyby Čechů v angličtině.
Topics: TH sound · W vs V · vowels · word stress · silent letters · rhythm
"""

TRAPS = {
    "TH": {
        "desc": "The 'TH' sound — tongue between teeth",
        "voiced_th": [
            ("the",     "ðə",    "NE: 'ze'  ✓: tongue out for 'th'"),
            ("this",    "ðɪs",   "NE: 'zis' ✓: voiced th"),
            ("that",    "ðæt",   "NE: 'zat'"),
            ("they",    "ðeɪ",   "NE: 'zey'"),
            ("brother", "ˈbrʌðə","NE: 'brozer'"),
        ],
        "voiceless_th": [
            ("think",   "θɪŋk",  "NE: 'sink' or 'tink'"),
            ("three",   "θriː",  "NE: 'tree' ✓: TH-ree"),
            ("thank",   "θæŋk",  "NE: 'tank'"),
            ("mouth",   "maʊθ",  "NE: 'mowt'"),
            ("birthday","ˈbɜːθdeɪ","NE: 'birt-day'"),
        ],
    },
    "W vs V": {
        "desc": "W = lips rounded, no teeth | V = top teeth on lower lip",
        "examples": [
            ("wine",  "waɪn",  "NE: 'vine'  — W: round lips, blow"),
            ("very",  "ˈveri", "NE: 'wery'  — V: teeth on lip"),
            ("west",  "west",  "NE: 'vest'"),
            ("video", "ˈvɪdɪəʊ","NE: 'wideo'"),
            ("wave",  "weɪv",  "both W and V in one word!"),
        ],
    },
    "Vowel length": {
        "desc": "English vowels have different lengths — short vs long",
        "examples": [
            ("ship/sheep",   "ɪ / iː",  "'I' in 'sit' vs 'ee' in 'feet'"),
            ("live/leave",   "ɪ / iː",  "to live (žít) vs to leave (odejít)"),
            ("full/fool",    "ʊ / uː",  "short U vs long U"),
            ("cat/cart",     "æ / ɑː",  "short A vs long A"),
            ("pull/pool",    "ʊ / uː",  "pull ≠ pool"),
            ("bed/bird",     "e / ɜː",  "short E vs 'ER' sound"),
        ],
    },
    "Silent letters": {
        "desc": "These letters are written but NOT pronounced",
        "examples": [
            ("know",     "nəʊ",      "K is silent"),
            ("write",    "raɪt",     "W is silent"),
            ("knife",    "naɪf",     "K is silent"),
            ("Wednesday","ˈwenzdeɪ", "D is silent"),
            ("doubt",    "daʊt",     "B is silent"),
            ("island",   "ˈaɪlənd",  "S is silent"),
            ("could",    "kʊd",      "L is silent"),
            ("receipt",  "rɪˈsiːt",  "P is silent"),
            ("hour",     "aʊə",      "H is silent"),
            ("foreign",  "ˈfɒrɪn",   "G is silent"),
        ],
    },
    "Word stress": {
        "desc": "English words have ONE stressed syllable — wrong stress changes meaning!",
        "examples": [
            ("PREsent (noun)", "a present = dárek"),
            ("preSENT (verb)", "to present = prezentovat"),
            ("REcord (noun)",  "a record = záznam"),
            ("reCORD (verb)",  "to record = nahrávat"),
            ("PHOtograph",     "FOtograph"),
            ("phoTOgraphy",    "foTOgrafia"),
            ("photoGRAPHic",   "fotoGRAFIcký"),
        ],
    },
    "Czech sounds to avoid": {
        "desc": "Sounds that don't exist in English",
        "examples": [
            ("R",      "English R is soft: 'red' — not the Czech rolled R"),
            ("Á/Í/Ú",  "No long vowels — 'Praha' in English = 'Pra-ha' not 'Praaaha'"),
            ("Ř",      "No equivalent — closest: 'rzh'"),
            ("-ing",   "The G is often dropped: 'comin' — but write with G"),
            ("Schwa ə","Most unstressed vowels become 'uh': 'about' = ə'baʊt"),
        ],
    },
}

print("=" * 55)
print("  LESSON 29: Pronunciation — Czech Speaker Traps")
print("=" * 55)

print("\n  Tip: Read each example ALOUD. Pronunciation only improves")
print("  when you actually speak — not just read.\n")

for trap_name, data in TRAPS.items():
    print(f"\n📚 {trap_name.upper()}: {data['desc']}")
    print("-" * 55)
    for sub_key, items in data.items():
        if sub_key == "desc":
            continue
        for item in items:
            if len(item) == 3:
                word, ipa, note = item
                print(f"  {word:<16} /{ipa}/  {note}")
            else:
                print(f"  {item[0]:<30} → {item[1] if len(item) > 1 else ''}")

print("\n\n🎯 PRACTICE — minimal pairs:")
print("-" * 55)
minimal_pairs = [
    ("three / tree",    "θriː / triː",  "TH sound at start"),
    ("ship / sheep",    "ʃɪp / ʃiːp",   "short vs long I"),
    ("wine / vine",     "waɪn / vaɪn",  "W vs V"),
    ("live / leave",    "lɪv / liːv",   "short vs long I"),
    ("think / sink",    "θɪŋk / sɪŋk",  "TH vs S"),
    ("walk / work",     "wɔːk / wɜːk",  "different vowels"),
]
for pair, ipa, note in minimal_pairs:
    print(f"  {pair:<22} {ipa:<22} ({note})")

print("\n  ✓ Say each pair 5 times, exaggerating the difference.")
print("  ✓ Record yourself and compare to an online pronunciation tool.")
print("  ✓ Resources: forvo.com, youglish.com, Cambridge Dictionary audio")

# YOUR TASK:
# 1. Record yourself reading the first 10 words from the TH section
# 2. Find 5 words you regularly mispronounce — look them up in a dictionary
# 3. Read the dialogue from Lesson 15 aloud, focusing on TH and W/V sounds
