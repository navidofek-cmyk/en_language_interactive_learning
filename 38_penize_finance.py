"""
LESSON 38: Money & Finance
============================
⭐⭐ Level: B1 | Pre-Intermediate

Peníze, bankovnictví a osobní finance.
Topics: banking · spending · saving · expressions with money
"""
import random

BANKING = {
    "current account":    "běžný účet",
    "savings account":    "spořicí účet",
    "mortgage":           "hypotéka",
    "loan":               "půjčka",
    "interest rate":      "úroková sazba",
    "overdraft":          "přečerpání účtu",
    "direct debit":       "inkaso",
    "standing order":     "trvalý příkaz",
    "statement":          "výpis z účtu",
    "PIN":                "PIN kód",
    "transaction":        "transakce",
    "currency":           "měna",
    "exchange rate":      "kurz",
    "cash":               "hotovost",
    "cashless":           "bezhotovostní",
}

SPENDING = {
    "afford":             "dovolit si",
    "spend":              "utratit",
    "waste":              "plýtvat",
    "invest":             "investovat",
    "save":               "šetřit",
    "borrow":             "půjčit si (od někoho)",
    "lend":               "půjčit (někomu)",
    "owe":                "dlužit",
    "pay back":           "splatit",
    "charge":             "účtovat",
    "discount":           "sleva",
    "refund":             "vrácení peněz",
    "tip":                "spropitné",
    "budget":             "rozpočet",
    "debt":               "dluh",
    "income":             "příjem",
    "tax":                "daň",
    "invoice":            "faktura",
}

IDIOMS = {
    "break the bank":           "stát jmění / zruinovat",
    "penny-wise, pound foolish":"šetří se na maličkostech, plýtvá na větším",
    "money doesn't grow on trees":"peníze nerostou na stromech",
    "to be broke":              "být bez peněz (neformální)",
    "to go Dutch":              "platit každý za sebe",
    "in the red":               "v mínusu",
    "in the black":             "v plusu (zisku)",
    "live within your means":   "žít podle svých možností",
    "a ballpark figure":        "přibližná cifra",
    "cut costs":                "snížit náklady",
}

print("=" * 55)
print("  LESSON 38: Money & Finance")
print("=" * 55)

print("\n📚 BANKING:")
print("-" * 55)
for en, cz in BANKING.items():
    print(f"  {en:<24} {cz}")

print("\n📚 SPENDING & SAVING:")
print("-" * 55)
for en, cz in SPENDING.items():
    print(f"  {en:<20} {cz}")

print("\n📝 BORROW vs LEND:")
print("-" * 55)
print("  BORROW (from) = vzít si na čas od někoho")
print("    Can I BORROW your pen?  (mohu si půjčit?)")
print("    I borrowed £50 FROM my friend.")
print()
print("  LEND (to) = dát na čas někomu")
print("    Can you LEND me your pen?  (půjčíš mi?)")
print("    She lent me her car.")
print()
print("  Memory trick: you LEND something OUT, you BORROW something IN")

print("\n📚 MONEY EXPRESSIONS & IDIOMS:")
print("-" * 55)
for en, cz in IDIOMS.items():
    print(f"  '{en}'")
    print(f"    → {cz}\n")

print("\n💬 AT THE BANK:")
print("-" * 55)
dialogue = [
    ("Customer", "I'd like to open a savings account, please."),
    ("Clerk",    "Of course. Do you have ID with you?"),
    ("Customer", "Yes, here's my passport. What's the interest rate?"),
    ("Clerk",    "Currently 3.5% per annum. Would you like a debit card?"),
    ("Customer", "Yes please. Can I set up a direct debit for my rent?"),
    ("Clerk",    "Absolutely. I'll send you the forms to sign online."),
]
for speaker, line in dialogue:
    print(f"  {speaker}: {line}")

print("\n🎯 QUIZ:")
print("-" * 55)
all_vocab = {**BANKING, **SPENDING}
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
# 1. Write 5 sentences about your spending habits using vocabulary from this lesson
# 2. Write a short dialogue: calling your bank about an unrecognised transaction
# 3. Write a simple monthly budget in English (income, fixed costs, savings, spending)
