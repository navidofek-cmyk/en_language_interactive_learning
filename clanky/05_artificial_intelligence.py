"""
ARTICLE 05: Artificial Intelligence — Promise and Peril
=========================================================
⭐⭐⭐⭐ Level: B2 | Upper-Intermediate

Umělá inteligence — přínosy, rizika a etické otázky.
Topics: technology · ethics · future · advanced vocabulary
"""

ARTICLE = """
ARTIFICIAL INTELLIGENCE — PROMISE AND PERIL

Artificial intelligence is no longer the stuff of science fiction. It is
diagnosing diseases with greater accuracy than human doctors, generating
legal documents in seconds, and powering the recommendations that shape what
we read, watch, and buy. AI is embedded in the infrastructure of modern life,
often invisibly.

The potential benefits are extraordinary. In healthcare, AI systems have
demonstrated the ability to detect cancers at early stages that human
radiologists miss. In climate science, machine learning models are improving
weather forecasting and optimising energy grids. In education, adaptive
platforms are tailoring content to individual learners at a scale no teacher
could achieve alone.

Yet the risks are equally substantial. The rapid displacement of jobs — not
just manual labour, but knowledge work — is raising profound questions about
economic inequality and social purpose. Autonomous weapons systems raise
troubling ethical questions about accountability and the laws of war.
Perhaps most insidiously, AI systems reflect and amplify the biases present
in their training data, potentially entrenching discrimination in consequential
decisions — who gets a loan, who gets an interview, who is flagged as a
security risk.

Governance has lagged badly behind development. A small number of private
companies now hold unprecedented power over systems that affect billions of
people, with little democratic oversight.

The question is not whether AI will transform society. It already is. The
question is whether that transformation will be shaped by democratic values
and public interest, or by the logic of capital and competitive advantage.
"""

VOCABULARY = {
    "diagnose":        "diagnostikovat",
    "infrastructure":  "infrastruktura",
    "demonstrate":     "prokázat",
    "radiologist":     "radiolog",
    "optimise":        "optimalizovat",
    "adaptive":        "adaptivní",
    "displacement":    "vytlačení, nahrazení",
    "autonomous":      "autonomní, samostatný",
    "accountability":  "odpovědnost",
    "insidiously":     "záludně, nenápadně",
    "amplify":         "zesilovat",
    "entrench":        "zakořenit, upevnit",
    "governance":      "řízení, správa",
    "unprecedented":   "bezprecedentní",
    "oversight":       "dohled, kontrola",
    "competitive advantage": "konkurenční výhoda",
}

COMPREHENSION = [
    ("Give two specific examples of beneficial AI applications mentioned.",
     "Any two: early cancer detection / weather forecasting / energy grid optimisation / personalised education / legal documents."),
    ("What does 'displacement of jobs' refer to in this context?",
     "AI replacing human workers, including knowledge workers, not just manual labourers."),
    ("What is the problem with AI systems reflecting training data biases?",
     "They can entrench discrimination in important decisions (loans, job interviews, security)."),
    ("What does the article say about governance of AI?",
     "It has lagged behind development; private companies hold power with little democratic oversight."),
    ("What does the author argue is the key question about AI?",
     "Whether AI transformation will serve democratic values or commercial interests."),
]

LANGUAGE_FOCUS = [
    ("Parallel structure:",
     "'not just manual labour, BUT knowledge work'"),
    ("Adverb for emphasis:",
     "'Governance has lagged BADLY behind development.'"),
    ("Inversion (journalistic emphasis):",
     "'The question IS NOT WHETHER AI will transform society. It ALREADY IS.'"),
    ("Complex noun phrases:",
     "'the rapid displacement of jobs... raising profound questions about economic inequality'"),
]

DISCUSSION = [
    "Are you excited or worried about the rise of AI? Why?",
    "Should there be international laws governing AI development?",
    "Do you think AI will replace your job (or field of study)? How do you feel about that?",
    "Who should be responsible when an AI system makes a mistake that harms someone?",
]

print("=" * 55)
print("  ARTICLE 05: Artificial Intelligence — Promise and Peril")
print("=" * 55)
print(ARTICLE)

print("\n📚 VOCABULARY:")
print("-" * 55)
for en, cz in VOCABULARY.items():
    print(f"  {en:<22} {cz}")

print("\n🔍 LANGUAGE FOCUS:")
print("-" * 55)
for feature, example in LANGUAGE_FOCUS:
    print(f"  {feature}")
    print(f"    {example}\n")

print("\n🎯 COMPREHENSION:")
print("-" * 55)
for i, (q, a) in enumerate(COMPREHENSION, 1):
    print(f"\n  Q{i}: {q}")
    ans = input("  → ").strip()
    print(f"  ✓ Model: {a}")

print("\n💬 DISCUSSION:")
print("-" * 55)
for i, q in enumerate(DISCUSSION, 1):
    print(f"  {i}. {q}")
    ans = input("  → ").strip()
    print()

# YOUR TASK:
# 1. Write a 150-word opinion piece: "AI will be the most important technology in history."
# 2. Research: What is the EU AI Act and what does it regulate?
# 3. Write a paragraph arguing that AI governance should be handled internationally,
#    using advanced collocations and discourse markers from lessons 58-59.
