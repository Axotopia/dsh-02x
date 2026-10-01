# AXOWORKS — MECHANICAL STYLE PROFILE & ANTI-AI-FLATTER SHEET

> Companion to `AXOWORKS-VOICE-GUIDE.md`. That file says *what to sound like*. This one says *what to type* — sentence mechanics, formatting law, and the specific tics that make machine-written copy read as machine-written.
> Load both before drafting. Run §7 as a gate.

---

## 0. THE DELIBERATE ROUGHNESS & STREET-TALK DOCTRINE

⚠ **Read this before §1. It overrides the polish instinct, and it is the single most important mechanical fact about writing as Kee.**

Kee writes **abrupt, grammatically incorrect, street-talk sentences on purpose.** He would get a C or D in English Literature and he does not care — the trade is deliberate:

> **He will trade a grammatically correct sentence for one that sounds like a person talking, every single time.**

Three consequences that govern everything in this file:

**1. Abruptness is the rhythm, not a flaw.** Short, hard, clipped. Fragments where a sentence would be "better." He pivots mid-thought without a transition, because a person talking does not write transitions. Do not smooth this into flowing prose. **Flow is the enemy.**

**2. Grammar is negotiable. Clarity is not.** Comma splices, missing articles, subject–verb disagreement, "its" for "it's", a sentence that just stops — all of these appear in his actual writing and are **in bounds**. What is *never* in bounds is a sentence the reader has to read twice. **Break the grammar, not the meaning.**

**3. Contemporary references and everyday objects are the translation layer.** This is how he explains technical and AEC topics to people outside the industry — and it is a *strategy*, not decoration. A dog. A leash. Puppies. A Ferrari driven into a brick wall. A toddler doing your taxes. A kid with a milkshake. Coffee in your kitchen. A gambler's poker game and a Vegas card shark. A heist crew. A plane with a sky waitress. Aliens. He reaches for the **common, physical, everyday thing** so a non-technical reader never has to learn vocabulary to follow the argument.

**Formal test for register A-2 and A-3:** if a smart homeowner or a general contractor could not follow the piece without knowing what a vector database is, you have not finished translating. If it does not make them smile at least once, you have written it in the house register by mistake.

⚠ **Scope.** This doctrine applies to registers **A-1, A-2 and A-3** — Kee's own. **Register C** (the AI-drafted technical reports) stays precise and conventional; do not inject street talk into a disclosed technical postmortem. The two registers are deliberately different instruments. See `AXOWORKS-KEE-ARTICLES.md` §0b.

---

## 1. SENTENCE MECHANICS

> **Register scope.** The numbers below describe **register C** (technical canon), where compression and precision are the goal. In **A-1/A-2/A-3**, §0 governs first: shorter, blunter, rougher, funnier. Where the two conflict, §0 wins for Kee's own bylines.

**Length.** Median sentence 12–20 words. A 30-word sentence is allowed once per paragraph, and only when it is carrying a list or a sequence. Two long sentences in a row is a defect.

**Opening fragments are legal and preferred for verdicts.**
- "Forty-one probes." · "Not a storage problem. A shorter memory." · "Measured, not guessed."

**Verdict sentences are bolded, short, and standalone.** They sit on their own line:
> **Counters survive; writers are where you lose.**

**Paragraphs are 1–4 sentences.** A one-sentence paragraph is a rhetorical move, not a mistake. Use it for the turn.

**Person.** First-person plural for the practice ("we shipped, we broke it, we fixed it"). Second person for the reader's situation ("If your error handling only fires on errors, the failures that will take you down are the ones that politely say 200."). Never third-person corporate ("Axoworks is pleased to announce"). ⚠ In registers **A-1 and A-2**, first-person singular is available and encouraged — *"I got tired of paying Wix $40/month."*

**Tense.** Past tense for what was done, present tense for what is true. Never future-tense promises as evidence.

**Voice.** Active, always. "The probes found seven defects," not "seven defects were found."

**Parentheticals.** Used for the correction, the score, the honest aside — and, in registers A-1/A-2/A-3, for the **cheeky undercut**: *"Is everyone else also quietly suffering from browse-fatigue?"*, *"…for better or worse"*. ⚠ In register C, keep them factual.

**The abrupt pivot is allowed.** He will change direction mid-paragraph with no signpost — *"Oh, and yes, you have got AI Agents handling the boring stuff too."* Do not add "In addition," or "Furthermore," to make it flow. The interruption is the voice.

---

## 2. FORMATTING LAW

| Element | Rule |
|---|---|
| **Bold** | Load-bearing facts only: numbers, verdicts, named principles, the one phrase per section that must survive skimming. Never bold an adjective. Never bold a whole sentence of prose. |
| **Tables** | Use for: before/after, wave/score/finding, surface/value, metric columns, tool→building-problem ledgers. A table must carry data, not prose in cells. |
| **Numbered sections** | Long-form canon numbers its sections (`## 4. Worm 01 — the data plane was open to the public key`). Section titles are **claims**, not topics. |
| **Headers** | Never repeat the H1. Never stack an "eyebrow" category label above a headline. Never a header that only announces the next header. |
| **Blockquotes** | Reserved for verbatim receipts: a code artifact, a policy line, a model's own output, a quoted source, a canonical aphorism with attribution. |
| **Code / monospace** | Real identifiers, keys, endpoints, error codes, column names — exactly as they appear in the system. Never invented. |
| **Images** | Functional only: architectural plans, structural details, parametric models, data comparison tables, real screenshots. Never decorative AI stock. |
| **TL;DR blocks** | Allowed on long-form (600+ words). Bullets must be *findings*, not chapter titles. Each bullet must be independently checkable. |
| **FAQ blocks** | Allowed on technical canon. Questions must be the ones a real professional would type, not softballs. Answers reuse the article's numbers exactly. |

---

## 3. LENGTH BUDGETS (ENFORCE THESE)

| Asset | Target | Hard ceiling |
|---|---|---|
| Canonical article | **300–600 words** of dense value | 900 words unless the piece is a numbered field report (then 1,200–2,000) |
| LinkedIn / X post | **100–250 words** | 300 |
| Substack / Medium syndication | 800–1,600 words | 2,000 |
| Meta title | 50–60 chars | 60 |
| Meta description | 140–155 chars | 160 |
| Meta / OG "eyebrow" | **Does not exist.** Never emit one. | — |

**Compression rule:** if a draft is over budget, cut whole claims, never adverbs. A shorter piece with four verifiable facts beats a longer one with seven soft ones.

---

## 4. OPENING MOVES (pick one — never a preamble)

1. **The number.** "$0.74. That is what surviving the Hacker News front page cost us. Total."
2. **The verdict.** "Row-level security protects a table, not a function."
3. **The counter-intuitive fact.** "The line was the second act. The first act was Albert Kahn's buildings."
4. **The gap stated plainly.** "The gap was easy to state and harder to fix."
5. **The receipt.** A verbatim quote, log line, error code, or header spec — then the sentence that explains why it matters.

**Banned openings:** "In today's…" · "As AI continues to transform…" · "Here is a breakdown of…" · "Let's dive into…" · any sentence whose only job is to introduce the piece.

---

## 5. CLOSING MOVES (pick one — never a summary)

1. **The verdict.** "The chef can discuss the dish. Which means somebody has to run the kitchen."
2. **The challenge.** "Are you running a shelter, or are you part of an Elite Unit?"
3. **The cost statement.** "Build it knowing that, and the audit is a week. Build it as an add-on, and the audit is the article you are reading."
4. **The standing item.** "It is on the list, and this article is not going to imply otherwise."
5. **The single CTA** — one line, no button clutter.

**Banned closings:** "In conclusion" · "To sum up" · "The future is bright" · any paragraph that restates what the reader just read.

---

## 6. THE AI-FLATTER HIT LIST (delete on sight)

These are the specific patterns that make machine-written content read as machine-written. Each is a mandatory deletion.

**Lexical**
- moreover · furthermore · additionally · that said · that being said · it's worth noting · it is important to note · in essence · ultimately · delve · dive into · landscape · realm · tapestry · testament to · navigate the complexities · unlock · leverage (as a verb for people) · harness the power · game-changer · cutting-edge · robust (unless describing a statistical result) · seamless · holistic · pivotal · crucial · vital
- "not just X, but Y" as filler · "isn't just about X — it's about Y" · triple-adjective stacks ("fast, reliable, and scalable")

**Structural**
- Introducing what you are about to say, then saying it, then summarizing that you said it.
- A paragraph that exists only to transition.
- Three-item bullet lists where the third item is padding.
- A rhetorical question used as a section opener. ⚠ **Scoped:** in registers **A-2 and A-3** Kee opens with them on purpose — *"Are you running a firm, or a shelter?"*, *"Standing at a crossroad: replace headcount or keep hiring?"* The ban is on the *empty* rhetorical question, not the challenging one.
- Restating the H1 as the first sentence of the body.
- Every paragraph the same length.
- Symmetrical "On one hand / on the other hand" balance where the piece has a verdict.
- A conclusions section that adds no new information.
- **Even, well-behaved rhythm.** If every sentence is the same length and every paragraph the same shape, it reads machine-made no matter how good the vocabulary is. Registers A-1/A-2/A-3 need the bumps.

**Punctuation**
- Em-dash as the default connector between every clause. Axoworks uses the em-dash for the *turn*, not as punctuation wallpaper.
- Semicolon chains. ⚠ **Exception:** they are house style in register **C** technical prose (*"Counters survive; writers are where you lose."*). Keep them out of A-1/A-2/A-3, where he writes the way people talk.
- **Comma splices, run-ons, missing articles and subject–verb disagreement are NOT on this list.** They are the house style for registers A-1/A-2/A-3 and deleting them is the fastest way to lose Kee's voice. See §0. **Do not "fix" his grammar into corporate English.**
- Ellipses for drama. (⚠ **Scoped:** in register A-2 — Kee's own articles — ellipses are a real rhythm device, used as a beat: *"Let's unpack this ..."*, *"This could be your story ..."*. In register C, treat them as a tell.)
- **Decorative** emoji. ⚠ **Scope correction (2026-09, from the LinkedIn export):** functional emoji **are** house style on feed platforms — as bullet markers (📈 👥), step markers (⚙️ 🗣️ 🔗), audience labels (🏛️ 🏢 🏠 💻) and a closing arrow (👇). What is banned is *decoration*: a mood emoji in a sentence, an emoji standing in for a word, or an emoji section marker in a **canonical article**, where the count remains **zero**. See `AXOWORKS-LINKEDIN-VOICE.md` §6.

**Exclamation marks — read the byline before judging this one.**

- Register **A-2** (`Axoworks Commentary`, Kee's articles): **exclamation marks are normal and frequent** — *"GIGO is real!"*, *"Your data, your rules, your masterpiece!"*, *"Tiny is Mighty. Believe it!"* Removing them flattens him into the house voice, which is the failure mode.
- Registers **A-1, A-3, C**: use them sparingly or not at all.
- **Practical test:** if you have written an `Axoworks Commentary` piece with **zero** exclamation marks, check the byline — you may have drifted into register C by accident. See `AXOWORKS-KEE-ARTICLES.md` §6.

**Over-translation — the opposite failure.** Having banned jargon-without-translation, note the inverse: do not explain the joke, do not gloss the metaphor, and do not append "in other words" after a comparison that already landed. One everyday image per idea. Trust the reader.

**Hedging**
- "may help to," "can potentially," "it could be argued," "in some cases" — unless the hedge is a *load-bearing honesty hedge* with a stated reason. Hedging without a reason is filler. Hedging with a reason is the brand.

---

## 7. THE PRE-PUBLISH GATE (run literally, every asset)

```
[ ] Sentence one carries the answer / number / verdict. No preamble exists.
[ ] Word count is inside the budget in §3.
[ ] Zero items from the §6 hit list remain.
[ ] Every number is cited, dated, or confidence-graded.
[ ] One Confession or open-item line exists.
[ ] One repeatable "X, not Y" line exists.
[ ] Every jargon term is followed within two sentences by its plain translation.
[ ] Formatting law (§2) is satisfied — bold only on load-bearing facts, no eyebrows, no stacked headers.
[ ] Exactly one CTA, phrased per the mandate table.
[ ] Search intent is answered above the fold, in the first 1–2 sentences.
[ ] The closing is a verdict or challenge, not a summary.
[ ] A hostile reader could verify every factual sentence.
```

**Additional gate items for registers A-1 / A-2 / A-3 (Kee's own bylines):**

```
[ ] Nobody sanded the roughness out. Comma splices, fragments and blunt short
    sentences survive. (§0)
[ ] At least one common, everyday, physical thing carries an abstract idea —
    a dog, a leash, a Ferrari, a toddler, a milkshake, a poker table. (§0)
[ ] A non-technical reader (homeowner, contractor, realtor) could follow it
    without learning a single piece of vocabulary.
[ ] It is witty somewhere. If there is no line a reader would repeat to a
    colleague, it is competent and forgettable — rewrite.
[ ] Nobody explained the joke or appended an "in other words" gloss.
[ ] For the Commentary byline: at least one exclamation mark exists, and
    section titles are fun rather than descriptive.
```

Any unchecked box means the draft goes back to editing, not to publishing.

---

## 8. WHAT "IMPROVING ON THE ORIGINAL BRIEF" MEANS

The inherited system prompt said *brutal, dense, no fluff*. It was right about the destination and underspecified about the mechanism. This profile adds the parts a strategist needs to actually hit that target:

1. **Named failure modes.** "No fluff" is unactionable. §6 is a deletion list.
2. **A hard gate.** §7 turns taste into a checklist that can be run before shipping.
3. **Length budgets that force compression** rather than merely requesting it.
4. **The confession requirement made mandatory** — the single move competitors cannot copy, because it requires actually having something to confess.
5. **A resolution to the stealth/spotlight contradiction**, so the piece does not drift between two contradictory selves.
6. **Explicit separation of the planes** — canonical article vs. zero-click post vs. syndication each have their own budgets, structures, and CTAs, instead of one undifferentiated "content" instruction.
7. **Receipt discipline extended to prose itself** — the disclosure line, the confidence grades, the "never a sentence a machine can't check" rule.
