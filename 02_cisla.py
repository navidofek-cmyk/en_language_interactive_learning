"""
LESSON 02: Numbers & Basic Maths
==================================
⭐ Level: A1 | Beginner

Čísla, počítání a základní matematické výrazy v angličtině.
Topics: cardinal numbers · ordinal numbers · maths vocabulary
"""
import random

CARDINAL = {
    0: "zero",   1: "one",    2: "two",    3: "three",  4: "four",
    5: "five",   6: "six",    7: "seven",  8: "eight",  9: "nine",
    10: "ten",   11: "eleven",12: "twelve",13: "thirteen",14: "fourteen",
    15: "fifteen",16: "sixteen",17: "seventeen",18: "eighteen",19: "nineteen",
    20: "twenty",30: "thirty",40: "forty", 50: "fifty", 60: "sixty",
    70: "seventy",80: "eighty",90: "ninety",100: "one hundred",
    1000: "one thousand",1_000_000: "one million",
}

ORDINAL = {
    1: "1st — first",   2: "2nd — second",  3: "3rd — third",
    4: "4th — fourth",  5: "5th — fifth",   6: "6th — sixth",
    7: "7th — seventh", 8: "8th — eighth",  9: "9th — ninth",
    10: "10th — tenth", 20: "20th — twentieth", 100: "100th — hundredth",
}

MATHS = {
    "plus / and":          "+ (sčítání)",
    "minus":               "− (odčítání)",
    "times / multiplied by":"× (násobení)",
    "divided by":          "÷ (dělení)",
    "equals":              "= (rovná se)",
    "percent":             "% (procent)",
    "a half":              "1/2 (polovina)",
    "a quarter":           "1/4 (čtvrtina)",
    "point":               ". (desetinná tečka: 3.14)",
}

def number_to_english(n):
    if n in CARDINAL:
        return CARDINAL[n]
    if n < 100:
        tens = (n // 10) * 10
        ones = n % 10
        return f"{CARDINAL[tens]}-{CARDINAL[ones]}"
    return str(n)

print("=" * 55)
print("  LESSON 02: Numbers & Basic Maths")
print("=" * 55)

print("\n📚 CARDINAL NUMBERS (základní číslovky):")
print("-" * 55)
for num, word in CARDINAL.items():
    print(f"  {num:<12} {word}")

print("\n📚 ORDINAL NUMBERS (řadové číslovky):")
print("-" * 55)
for num, word in ORDINAL.items():
    print(f"  {word}")

print("\n📚 MATHS VOCABULARY:")
print("-" * 55)
for en, cz in MATHS.items():
    print(f"  {en:<26} {cz}")

print("\n💬 EXAMPLES:")
print("-" * 55)
print("  Two plus three equals five.      (2 + 3 = 5)")
print("  Ten minus four equals six.       (10 − 4 = 6)")
print("  Six times seven equals forty-two.(6 × 7 = 42)")
print("  Twenty divided by four equals five. (20 ÷ 4 = 5)")
print("  It costs fifteen pounds fifty.   (£15.50)")
print("  My phone number is oh-seven...   (0 = 'oh' v phone numbers)")

print("\n🎯 QUIZ — napiš číslo anglicky:")
print("-" * 55)
nums = random.sample([1,2,3,4,5,6,7,8,9,10,11,12,13,15,20,30,40,50,100], 6)
score = 0
for n in nums:
    ans = input(f"  {n}  →  ").strip().lower()
    correct = number_to_english(n)
    if ans == correct:
        print("  ✓ Correct!\n")
        score += 1
    else:
        print(f"  ✗ Answer: {correct}\n")

print(f"\n  Score: {score}/6")

print("\n🎯 MATHS QUIZ — přečti příklad anglicky:")
print("-" * 55)
a, b = random.randint(1, 9), random.randint(1, 9)
print(f"  How do you say: {a} + {b} = {a+b} ?")
print(f"  Answer: {number_to_english(a)} plus {number_to_english(b)} equals {number_to_english(a+b)}")

# YOUR TASK:
# 1. Extend number_to_english() to handle numbers 21–99
# 2. Write a function read_price(pounds, pence) that reads a
#    price aloud: read_price(5, 99) → "five pounds ninety-nine"
# 3. Create a maths quiz that generates 10 random additions and
#    asks the user to type the answer in English words
