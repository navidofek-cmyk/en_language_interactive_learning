# English — Interactive Course

[![Web](https://img.shields.io/badge/🌐_Live_Web-Visit_Course-89b4fa?style=for-the-badge)](https://navidofek-cmyk.github.io/en_language_interactive_learning/)

Interactive English course for Czech speakers: **A1 → C1**.
60 lessons + reading articles — each a standalone `.py` file.

## 🌐 [→ Open Course Website](https://navidofek-cmyk.github.io/en_language_interactive_learning/)

---

## Quick Start

```bash
git clone https://github.com/navidofek-cmyk/en_language_interactive_learning.git
cd en_language_interactive_learning
python3 01_pozdravy.py
```

Python 3.8+ required.

## Lessons

| Section | Lessons | Level |
|---|---|---|
| Basics | 01–07 | A1 |
| Grammar — Core | 08–15 | A1–A2 |
| Grammar — Intermediate | 16–20 | A2–B1 |
| Everyday Topics | 21–30 | A2–B1 |
| Advanced Vocabulary | 31–40 | B1 |
| Advanced Grammar | 41–50 | B1–B2 |
| C1 Grammar & Style | 51–60 | B2–C1 |
| Reading Articles | clanky/ | A2–C1 |

## Tools

| Tool | Usage |
|---|---|
| `flashkarty.py` | Spaced repetition vocab drill |
| `cloze_test.py` | Fill-in-the-blank tests |
| `streak.py` | Daily learning streak tracker |
| `progress.py` | Quiz score overview |

## How lessons work

1. Run: `python3 NN_lesson.py`
2. Read vocabulary, grammar notes, examples
3. Complete the interactive quiz
4. Do the written tasks at the end

## Structure

```
NN_lesson.py        ← lesson files (01–60)
clanky/             ← reading articles with comprehension
flashkarty.py       ← vocabulary flashcards
cloze_test.py       ← gap-fill test generator
streak.py           ← daily streak tracker
progress.py         ← score tracker
generator_web.py    ← builds the website
```
