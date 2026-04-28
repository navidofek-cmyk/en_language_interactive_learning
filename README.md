# English — Interactive Course

Interactive English course for Czech speakers: A1–B1 level.
15 lessons, each a standalone `.py` file — run it, read it, practise.

## Start

```bash
git clone https://github.com/navidofek-cmyk/en_language_interactive_learning.git
cd en_language_interactive_learning
python3 01_pozdravy.py
```

Python 3.8+ required.

## Lessons

**Basics (01–07):** Greetings · Numbers · Colours & descriptions · Family · Food & drink · Time & date · Self-introduction project

**Grammar (08–12):** Present Simple · Past Simple · Present Continuous · Questions & negatives · Modal verbs

**Vocabulary & Projects (13–15):** Travel & transport · Shopping · Everyday conversations project

## How each lesson works

1. Run the file — it prints vocabulary, examples and grammar notes
2. Complete the interactive quiz (translate words, fill in gaps)
3. Do the written tasks at the end of the file

## Web

```bash
python3 generator_web.py
# opens web/index.html
```

GitHub Actions automatically deploys to GitHub Pages on every push.

## Structure

```
NN_lesson_name.py   ← lesson files
generator_web.py    ← static site generator
reseni/             ← your solutions (not committed)
web/                ← generated site (not committed)
```
