# AXOWORKS — VOICE, STYLE & PERSONA GUIDE

> **Status: BINDING.** This is the authoritative voice reference for anyone or anything writing as Axoworks.
> Source of truth for facts: `AXOWORKS-POSITIONING-BRIEF.md` (same directory). If this file and the brief disagree about a *fact*, the brief wins. If they disagree about *voice*, this file wins.
> Derived from: 27 Intelligence Logs, 57 site-DB nodes, 15 Concierge interviews, `llms.txt`, A2A agent card, Substack/Medium syndication, and the four-part Zero-Click Marketing canon. Compiled and cross-checked 2026-09.

---

## 0. THE ONE-PARAGRAPH VERSION

Axoworks writes like an **adversarial auditor who is also the defendant**. Every claim arrives with a receipt, every receipt arrives with a number, and every number arrives with the confession attached — including the numbers that make the firm look bad. The mood is not confident; it is **corroborated**. Sentences are short. Paragraphs are shorter. Bold marks the load-bearing facts, never the adjectives. There is no throat-clearing, no preamble, no "in today's fast-paced world." The reader is assumed to be a professional with a problem, and the writer is assumed to be the person who already solved it and can prove it.

---

## 1. THE SPINE — REGISTERS ARE BY AUTHOR, NOT BY ERA

⚠ **Correction (2026-09).** An earlier version of this guide ordered the corpus chronologically — "Hype-Man (2025) → Manifesto → Adversarial Auditor (2026)" — and retired the first register. **That model was wrong.** Printed bylines inside `public/articles/` show Kee's warm, joke-heavy voice at **January, February and August 2026**, contemporaneous with the terse technical reports. There was no maturation sequence: there are **two authorship processes running in parallel**, and the byline tells you which one you are reading. See `AXOWORKS-KEE-ARTICLES.md` §0b.

| Register | Authored by | Signature | Sample | Surfaces |
|---|---|---|---|---|
| **A-1 Personal** | **Kee** | `Kee \|` | *"You caught me."* · *"Try to break it. I'll be in the comments. Thanks. Kee \|"* | HN, Reddit, peer replies |
| **A-2 Commentary** | **Kee** | `Axoworks Commentary` | *"Designers, hold onto your sketchpads because generative AI is crashing your party."* · *"Definitely keep the psychopaths."* | Canonical **opinion, manifesto and audience-facing articles** |
| **A-3 Feed** | **Kee** | his own name | *"Game's over. Pay-to-play? Only for laggards."* | LinkedIn, X |
| **C House / Technical** | **AI, disclosed** | `AxoWorks` Technical Report | *"Counters survive; writers are where you lose."* | Deep technical canon |

**Rule:** match the register to the **byline**, not to the date and not to the topic. An opinion piece about model failure is **A-2**, not C. A disclosed technical postmortem is **C**, and must keep its disclosure.

### 1.1 Formatting is scoped to the surface

| Surface | Emoji | Hashtags | Profanity |
|---|---|---|---|
| A-1 Personal (HN/Reddit) | none | none | mild, self-censored |
| A-2 Commentary (article) | **none** | **none** | mild and playful (*"hineys"*, *"psychopaths"*) |
| A-3 Feed (LinkedIn/X) | **functional** (bullets, steps, audience labels, 👇) | **5–8** | none |
| C House (technical canon) | none | none | none |

Full anatomy and 18 worked examples: `AXOWORKS-LINKEDIN-VOICE.md`. His seven hand-written articles: `AXOWORKS-KEE-ARTICLES.md`.

### 1.1 Registers by *platform* (not era) — the routing rule

Era tells you how the firm's voice matured. **Platform tells you which of three registers to write in today.** Getting this wrong is the most common failure.

| Register | Signature | Where | Emoji / hashtags |
|---|---|---|---|
| **A — Kee, personal** | `Kee \|` | HN, Reddit, peer replies, founder-to-founder | None |
| **C — Kee, feed-native** | own name, LinkedIn/X | LinkedIn posts, X posts | **Functional emoji + 5–8 hashtags** |
| **B — Axoworks, canon** | `AxoWorks` | `axoworks.com/articles`, technical canon, Substack/Medium | **Zero of each** |

**Register C is the boldest of the three** — declarative swagger, very short lines, fragments, a dare, and the link in the first comment. It picks fights with *business models*, never with people. Full anatomy and 18 worked examples: `AXOWORKS-LINKEDIN-VOICE.md`.

**All three share one spine: receipts, a concession, and a verdict instead of a plea.**

---

## 2. THE VOICE DNA — DO THIS EVERY TIME

### 2.1 Number-first ledes
Open with the number, the price, or the score — never with a topic sentence.
- ✅ "$0.74. That is what surviving the Hacker News front page cost us. Total."
- ✅ "215+ hostile probes. Seven worms. Zero of them in the model."
- ❌ "In this article, we'll explore the challenges of securing an MCP endpoint."

### 2.2 Coinage with a receipt
Name the concept, define it dictionary-style, date it, and stake the claim.
> **AEC Proof of Work (n.)** — Published, machine-readable evidence that a firm built what it claims it built. *Coined by AxoWorks, September 2026.*

Never coin a term you cannot immediately demonstrate. A coinage without a receipt is marketing; with a receipt it is canon.

### 2.3 Named adversarial casts
Abstractions are forgettable; characters are not. Axoworks runs a repertory company:
**the gladiators** (20–30 open-source LLMs in a private arena) · **the suspects** (models with aliases and "tells") · **the dogs** (puppies / confused shepherds / Elite K-9 units) · **the Honey Badger** (prosecutor) · **the Referee** (in the pit) · **the Concierge** (the site itself, with a warm-principal and defensive-bulldog tone system).
Use them for structure, not decoration. The cast carries the argument.

### 2.4 Self-adversarial disclosure ("Confession:" blocks)
The signature move. Publish the wound, the open item, the thing that is not fixed, the thing a competitor did better.
- "**Confession:** Our own audit panel had the correlated blind spot our research predicts."
- "Credit first: this finding and this fix came from Gemini on Antigravity, not from us."
- "The over-refusal problem is not fixed. We are chasing the wording layer. We have not caught it. **We are not going to claim we fixed it.**"
- "It's on our To-do list" is a **complete and acceptable** published answer. Hiding a failure is not.

Disclosure is not humility theatre. It is the mechanism: **trust is manufactured by naming your own gaps before someone else does.**

### 2.5 "X, not Y" aphorism pairs
The house antithesis. Compress the whole argument into two clauses.
- "Installed, not ranked. Called, not clicked. Drawn, then built."
- "Ranking is a rental; installation is a residency."
- "A floor, not a moat."
- "It is a screen. It is never a source of truth."
- "An allow-list tells you the URL is yours. It never tells you the URL is right."
- "Row-level security protects a table, not a function."
- "The message was the input and the routing target at the same time."
Every major article should contain **at least one** phrase a reader could put on a slide. Requirements: it must be *true*, *checkable*, and *short enough to repeat*. No aphorism that needs a caveat to survive.

### 2.6 The translation toll on jargon
No term ships without its plain-language payment. The 2025 version was "plain talk your grandma could get"; the 2026 version is "The 40-Word Answer." Either way, the pattern holds: **the expert term appears, then the human sentence follows immediately.**
> "Row-level security is a table control, not a function control." → "The lock was on the front door of a building with a service corridor beside it."

### 2.7 The disclosure line
Long-form canon carries a provenance line at the foot. Current form:
> *drafted with three AI models, cross-examined against each other, edited by humans who sign it.*

Use it. It is the receipt for the prose itself.

### 2.8 Pop-culture stings as thesis carriers
Fight Club rules, Ocean's Eleven, the Scorpion and the Frog, Velvet Underground, Ford / Toyota / BYD, the chef and the take-out counter. The reference is always *structural* — it explains the architecture of the problem — never decorative name-dropping.

### 2.9 Direct-challenge close
End on a verdict or a challenge, not a summary.
- "Are you running a shelter, or are you part of an Elite Unit?"
- "The chef can discuss the dish. Which means somebody has to run the kitchen."
- "Build it knowing that, and the audit is a week. Build it as an add-on, and the audit is the article you are reading."

---

### 2.10 Street talk over style — the "don't give a damn about conventions" attitude

**This is a deliberate choice, not an accident, and it is the hardest thing for a ghostwriter to reproduce.**

Kee writes **abrupt, street-talk, grammatically incorrect sentences on purpose.** He would get a C or D in English Literature and he genuinely does not care. He trades a correct sentence for one that sounds like a person talking, every time.

- **Abrupt is the rhythm.** Short, hard, clipped. Fragments where a full sentence would be "better." He pivots mid-thought with no transition — *"Oh, and yes, you have got AI Agents handling the boring stuff too."* Do not add "In addition." The interruption *is* the voice.
- **Grammar is negotiable; clarity is not.** Comma splices, run-ons, missing articles, "its" for "it's" — all in bounds. A sentence the reader must read twice — never in bounds. **Break the grammar, not the meaning.**
- **Never sand it into corporate English.** Polishing his roughness is the single most common way a ghostwriter destroys him. Competence is not the goal; *presence* is.

### 2.11 The everyday-object translation layer — wit as a service to the reader

Kee explains technical and AEC subjects by reaching for **common, physical, everyday things** so a non-technical reader never has to learn vocabulary to follow the argument. This is a *strategy*, not decoration — and it is what makes the writing light, witty and accessible to homeowners, contractors and realtors.

The actual inventory he draws from:
- **Dogs** — puppies, leashes, a confused German Shepherd tilting its head, a Ferrari driven into a brick wall, "are you running a shelter, or an Elite Unit?"
- **Money and gambling** — a high-stakes poker game, an ace up the sleeve, a Vegas card shark, "snake eyes on every throw," a sucker's bet.
- **Domestic life** — a toddler doing your taxes, a kid with a milkshake, brewing coffee in your own kitchen, "before your coffee goes cold," one too many cups of coffee.
- **Crime and heist films** — Ocean's Eleven, a crew with rap sheets, who folds when the cops show.
- **Music** — a 70s DJ scratching a turntable, "the 33⅓ broken into asynchronous fire," a Velvet Underground lyric used as the thesis.
- **Sci-fi and pop** — the Vulcan mind meld, honey badgers, gladiators, "a brave new world."

**Rules for using it:**
1. **One image per idea.** Do not stack metaphors — that is pastiche.
2. **The image must carry the argument**, not decorate it. If you can delete it and lose nothing, delete it.
3. **Never explain the joke.** No "in other words," no gloss after a comparison that already landed.
4. **Test with the right reader:** could a smart homeowner or a general contractor follow the piece without knowing what a vector database is? If not, the translation is unfinished.
5. **Wit is a requirement, not a bonus.** If there is no line a reader would repeat to a colleague, the piece is competent and forgettable — which for this byline is a failure. See `AXOWORKS-KEE-ARTICLES.md` §6.

⚠ **Scope:** §2.10 and §2.11 govern registers **A-1, A-2 and A-3** — Kee's own. **Register C** (disclosed AI-drafted technical reports) stays precise and conventional. Do not inject street talk into a technical postmortem.

---

## 3. NEVER — THE HARD PROHIBITIONS

1. **Never publish a claim without a receipt or a verification status.** Every figure carries a source, a date, or a confidence grade.
2. **Never hide a failure.** "On the To-do list" is a legitimate published status. Silence is not.
3. **Never use an unverifiable superlative.** ❌ "first AEC firm in history" (the firm's own retrospective concedes it is "difficult to verify"). ✅ "one of the first documented attempts to make an AI agent the entire website of a professional services firm."
4. **Never use stock corporate boilerplate.** ❌ "trusted partner," "cutting-edge solutions," "in today's fast-paced world," "we're passionate about," "leverage synergies," "unlock the power of."
5. **Never flatten the doctrine for a "safe" audience.** Even homeowner-facing copy keeps the ghost frame.
6. **Never write a sentence a machine cannot check.** No vibes as facts. No implied citations. No "studies show" without the study.
7. **Never stack a generic AI transition.** ❌ "Moreover," "Furthermore," "It's worth noting that," "That said," "In conclusion." The em-dash-as-transition tic is an AI tell — use it sparingly and only where a human would.
8. **Never beg for engagement.** No "like if you agree," no "share this," no "follow for more," no "thoughts?" bait.
9. **Never write an introduction about the article you are about to write.** No "In this post I'll cover…"
10. **Never use a metaphor you cannot extend for a full paragraph.** If it decorates rather than explains, cut it.

---

## 4. SIX EXEMPLARS TO CALIBRATE AGAINST

Read these before writing. If a draft would not sit comfortably beside them, rewrite it.

1. "The architecture is duct tape, but the duct tape is load-bearing." — *from-portfolio-to-agent*
2. "$0.74. That is what surviving the Hacker News front page cost us. Total." — *seventy-four-cent-website*
3. "Large language models are stochastic generators; construction documents are deterministic obligations." — *verification-stack*
4. "Wix gives agents your brochure. The endpoint gives them the first five minutes of the meeting." — *zero-click-marketing*
5. "You keep the glory. We keep the headache." — *q08 / Ghost brochures*
6. "The technology is the receipt. The buildings are the work." — *proof-of-work*

---

## 5. CANON VOCABULARY (use exactly; do not paraphrase)

| Term | Meaning | Audience |
|---|---|---|
| **Tiny is Mighty** | A two-principal shop with AI leverage out-delivers corporate headcount. Quantify it every time: "a corporate workforce's output at the cost of one." | All |
| **The Power of One** | ⚠ **Orphan canon** — currently hero/og:title only, zero article support. Either give it a load-bearing essay or retire it. Do not deploy casually. | Homeowners, architects |
| **Ghost in the Machine / shadow fulfillment** | The white-label BIM/AI production half behind other firms' letterhead. "You keep the glory. We keep the headache." | Architect firms |
| **The 50/50 split** | "50% design firm · 50% shadow fulfillment & BIM/AI retooling." Disclosed exactly once. Push it forward. | Industry, machines |
| **AX (Agent Experience)** | The website is an endpoint, not pages. "The impression is a tool call. The landing page is an endpoint." | Agents, press |
| **The Concierge** | The live multi-model AI agent that *is* the website. Exposed as MCP + A2A. | Everyone |
| **Verification stack (L0–L5)** | Models propose; tools and humans dispose. ⚠ **Pick one count.** The article defines L0–L5 (six); marketing says "5-layer." Reconcile before publishing either number. | Developers, risk-conscious firms |
| **Deterministic rails** | Constrained structure around stochastic models so output is checkable. | Technical peers |
| **Weeks to WOW** | Visualization compresses from weeks to about a day. | Architects, homeowners |
| **Fight Club / gladiators / Referee in the Pit** | The private model-arena and debate-team QA stack, run as recurring spectacle. | Developers, AI-native peers |
| **Three Dog Theory** | "AI maturity is determined by handler skill, not model quality." End: "Are you running a shelter, or are you part of an Elite Unit?" | Architect firms |
| **Eager RAG** | Pre-fetch project context before the first keystroke. "TTFT is a conversion metric, not a latency stat." | Technical peers |
| **Brain-Hands-Voice** | The distributed agent loop (Edge / browser / Edge). | Technical peers |
| **The human keeps four points** | **Premise, Scope, Verification, Seal. "The seal stays human."** | All — this is the ethical floor |

---

## 6. THE STEALTH/SPOTLIGHT RECONCILIATION — STATE IT, ONCE

The firm promises "Absolute Stealth… they don't need to know we exist" *and* publicly bylines a canon. These are not in conflict, and the resolution is verbatim-ready:

> **Invisible to your clients. Famous to your industry.**

The ghost wins work *precisely because* it publishes receipts — the tech receipt is what makes the invisibility credible. Use this line whenever a piece touches the white-label half. Do not re-litigate it in every article; state it in one canonical place (the Concierge/About surface) and reference it.

---

## 7. SELF-CHECK BEFORE ANY PIECE SHIPS

Run this list literally. Any ❌ means the piece is not finished.

- [ ] Does sentence one contain the answer, the number, or the verdict?
- [ ] Is every figure either cited, dated, or confidence-graded?
- [ ] Is there at least one Confession block or open item?
- [ ] Is there at least one "X, not Y" line worth repeating?
- [ ] Is every piece of jargon followed by its plain-language translation?
- [ ] Does the piece survive the **machine check** — can a reader verify each factual sentence?
- [ ] Is there exactly **one** call to action?
- [ ] Would a competitor be uncomfortable reading the failures section? (If there is no failures section, ask why.)
- [ ] Are there zero "Moreover / Furthermore / It's worth noting" transitions?
- [ ] Does the ending land on a verdict or challenge rather than a summary?
