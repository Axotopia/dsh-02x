# AXOWORKS — KEE'S ARTICLES: THE COMMENTARY REGISTER (Tier A-2)

> **Source.** Kee identified these seven files in `C:\Users\desig\Documents\GitHub\Axoworks\public\articles\` as the ones **most representative of his voice**:
> `three-dog-theory-v2` · `three-dog-theory` · `magic-pill` · `local-llm-privacy` · `hybrid-delivery` · `fight-club` · `developers-feasibility`
>
> Everything else in `public/articles/` is, in his words, **"mostly written by AI with some modifications."** That distinction is now the top-level routing rule for this entire knowledge base.
>
> All seven carry the byline **`Axoworks Commentary`** — not "Technical Report." **The byline is the tell.**

---

## 0. THE CORRECTION THAT REORDERS THE WHOLE VOICE MODEL

⚠ **Two earlier conclusions in this knowledge base were wrong, and both were wrong in the same direction: I mistook the AI-drafted house style for the firm's voice, and treated Kee's actual writing as a retired early phase.**

| Earlier claim | Reality |
|---|---|
| The 2025 "Hype-Man" register — exclamation marks, jokes, second-person "Designers, let's get real" — is **RETIRED**. | **It is not retired. It is Kee.** The 2025–2026 Commentary articles are his hand, and the *updated* versions (`three-dog-theory-v2`, August 2026) still carry the same voice, now loaded with receipts. What changed is not the voice but the **evidence level**. |
| Voice B is "the firm's published voice" — terse, table-heavy, zero profanity, zero emoji. | That description fits only the **AI-drafted technical reports**. Kee's own commentary is warmer, funnier, more profane-adjacent, and far more exclamation-heavy than the house style ever suggested. |
| Profanity is self-censored to `f***` and used sparingly. | True for the *canon* and for LinkedIn (where he uses none). In his **commentary** he is playful and mild — *"covering your hineys"*, *"jailbroken, uncensored beasts straight from the underworld"*, *"Definitely keep the psychopaths."* Still never aimed at a person. |

**The practical consequence:** the ghostwriter should not be aiming for the austere house register when writing in Kee's byline. **It should be aiming for the Commentary register** — and it should be more entertaining than it currently is.

---

## 0b. THE DATING CORRECTION — THE "ERAS" WERE AN ARTIFACT

⚠ **A third correction, and it invalidates the chronological model.** The earlier voice audit ordered the corpus into "Era 1 Hype-Man (Apr–Jul 2025) → Era 3 Adversarial Auditor (2026)" and concluded the first register was **retired**. The printed bylines inside these HTML files say otherwise:

| File | Printed byline date |
|---|---|
| `fight-club` | **December 2025** |
| `local-llm-privacy` | **January 2026** |
| `developers-feasibility` | **January 2026** |
| `three-dog-theory` | **January 2026** |
| `magic-pill` | **February 2026** |
| `three-dog-theory-v2` | **August 2026** |
| `seventy-four-cent-website` | August 2026 |
| `verification-stack` | June / August 2026 |

**Kee's voice and the adversarial-auditor reports are CONTEMPORANEOUS — 2026 both.** This is not a timeline of one voice maturing into another. It is **two registers running in parallel**, by two different authorship processes, in the same year. `three-dog-theory` (January) and `three-dog-theory-v2` (August) are the same voice seven months apart, with receipts added.

**Root cause of the error:** the earlier audit anchored on YAML frontmatter dates in the markdown corpus (`magic-pill` frontmatter 2025-05-08 vs. printed byline "February 2026"). The printed byline is the correct signal; frontmatter dates in this corpus are unreliable. **Always check the printed byline in `public/articles/`, never the frontmatter.**

**Consequence for writing:** there is no "old retired register." Kee's register is **current, live, and the byline's default.** Do not write his pieces in the house register in order to sound modern — that is the opposite of what the record shows.

---

## 1. THE BYLINE ROUTING RULE (governs everything downstream)

| Byline / surface | Who wrote it | Register to match |
|---|---|---|
| **`Axoworks Commentary`** (`fight-club`, `three-dog-theory`, `three-dog-theory-v2`, `magic-pill`, `local-llm-privacy`, `hybrid-delivery`, `developers-feasibility`) | **Kee** | **Tier A-2 — his articles. This is the target for opinion, manifesto and audience-facing pieces.** |
| `Kee \|` (HN, Reddit, peer replies) | **Kee** | **Tier A-1 — personal, loose, typo-tolerant** (`AXOWORKS-KEE-VOICE-PROFILE.md`) |
| LinkedIn / X posts | **Kee** | **Tier A-3 — feed-native** (`AXOWORKS-LINKEDIN-VOICE.md`) |
| **Technical Reports** (`zero-click-marketing`, `proof-of-work`, `the-chef-can-discuss-the-dish`, `verification-stack`, `front-door-is-an-api`, `revit-tools`, `rag-context-budget`, `from-portfolio-to-agent`) | **AI, disclosed** | **Tier C — house register.** Preserve the disclosure; never attribute to Kee personally. |
| `hybrid-delivery` | **Kee**, but benefit-led / service voice | Closest thing to a **sales page** in his hand — use for firm-facing service copy |

---

## 2. THE COMMENTARY ANATOMY

```
1. LABEL         "AxoWorks Intelligence Log" + title + "Axoworks Commentary | <Month Year>"
2. THE HOOK      Direct address to the audience, a high-stakes framing, or a pop-culture cold open.
                    "Designers, hold onto your sketchpads because generative AI is crashing your party,
                     and it's bringing some serious game."
                    "Real estate development is a high-stakes poker game ... one bad call on a zoning
                     code, a missed tax break, or a misjudged rental rate can turn your dream project
                     into a financial flop."
                    "You are a tiny team, no corner glass offices, no $300M training budget, no HR
                     department writing apologies, definitely no legal department covering your hineys."
3. THE PROMISE   One line of what the reader gets, with a wink.
4. BODY          Named sections with JOKE TITLES ("From Weeks to Wow in a Snack", "Cracking the Code
                 Jungle", "Pro Forma & Market Scoop Wizardry", "Go Local for Privacy and Power").
                 Numbered cast members for frameworks (1. The Puppy / 2. The Confused German Shepherd
                 / 3. The Elite K-9 Unit).
5. RECEIPTS      Data, costs, cites — heavy in v2-era pieces, light in 2025 pieces.
6. THE FINAL WORD  His literal standing close for the early pieces — an aphorism or a dare.
7. CTA           Soft, and occasionally third-person-referral ("Partner with AI-savvy consultants
                 like AxoWorks") — an OLD habit, retired in the newer voice.
```

---

## 3. VERBATIM — WHAT HIS ARTICLES ACTUALLY SOUND LIKE

**Cold opens that address the reader directly:**
> "Designers, hold onto your sketchpads because generative AI is crashing your party, and it's bringing some serious game. This isn't just another tool to clutter your toolbar; it's a turbo-charged sidekick that works faster than you can chug your morning coffee." — *magic-pill*

> "Real estate development is a high-stakes poker game ... one bad call on a zoning code, a missed tax break, or a misjudged rental rate can turn your dream project into a financial flop. But fear not, developers, because Large Language Models (LLMs) are here to be your AI-powered ace up the sleeve. … Buckle up as we dive into how LLMs can transform your game, why choosing the right one is key, and how to play your cards right." — *developers-feasibility*

> "In the digital wild west, your data is gold, and companies are mining it faster than you can say 'privacy settings.'" — *local-llm-privacy*

> "You are a tiny team, no corner glass offices, no $300M training budget, no HR department writing apologies, definitely no legal department covering your hineys." — *fight-club*

**The jokes — puns, cartoons, and deliberate corniness. This is the part the house style erased:**
> "Using it for professional work is like hiring a toddler to do your taxes. It's cute, but a disaster waiting to happen." — *three-dog-theory, v2*

> "The dog tilts its head. It looks at you with pity. The dog isn't stupid; it's confused by you. You are giving it 'Garbage In,' so it's giving you 'Garbage Out.' You have a Ferrari of intelligence, but you are driving it into a brick wall because you don't know how to give clear commands." — *three-dog-theory*

> "Web-based tools often slurp up your data like a kid with a milkshake." — *magic-pill*

> "Local LLMs: Your Data's Fortress … It's like brewing coffee in your kitchen: you control the beans, the brew, and nobody's sniffing your mug." — *local-llm-privacy*

> "Proprietary AI, on the other hand? It's a locked box with a 'just trust us' sticker. Good luck with that." — *local-llm-privacy*

> "Some are polite librarians, some jailbroken, uncensored beasts straight from the underworld. They fight to their last breath on every prompt. The survivor speaks." — *fight-club*

> "Keep the polite models. Definitely keep the psychopaths." — *fight-club*

**The X-not-Y law, abundant:**
> "This isn't a Pet; it's a Partner." — *three-dog-theory*
> "Smarter doesn't mean better; smarter means the errors are now even harder to spot." — *three-dog-theory-v2*
> "this handler give sharp, disciplined instructions" — *three-dog-theory*

**The signature close:**
> "The Final Word" — his literal standing heading in the early pieces, then an aphorism beneath it.

> "Your arena. Your game. See you in the pit." — *fight-club*
> "The hard choice: Do you want to play with puppies, or do you want to get paid?" — *three-dog-theory*
> "The only question left is: Are you running a shelter, or are you part of an Elite Unit?" — *three-dog-theory-v2*
> "Your data, your rules, your masterpiece!" — *local-llm-privacy*

**The v2 upgrade — same voice, now armed.** Compare the two dog-theory versions and the difference is *only* evidence:
> "As capability exploded, failure modes got worse. Hallucination rates on most complex reasoning still run at 5–20%, a 2024 Stanford study found legal hallucinations jumped to 69–88% for state-of-the-art (SOTA) models. Even with corporate RAG guardrails, 17–33% of the time. Agentic systems now hallucinate entire software packages. Exploits through 'slopsquatting', registering the fake packages an agent suggests so it installs malware. One USENIX study found 19.7% of packages AI recommended didn't exist at all." — *three-dog-theory-v2*

**Hybrid delivery — a different purpose, the same man.** `hybrid-delivery` is the sales surface, and it drops the jokes for tight benefit statements with **named benefits in the subheads**:
> "Native Linking: Revit natively links your DWG files… You maintain 100% authorship; the 3D model simply conforms to your linework."
> "You get X-ray vision into your design without touching the authoring software."
> "Manual counting is prone to human error. Door, window, hardware, and room finish schedules are extracted directly from the 3D components we build over your CAD plans."

**The old habit worth retiring:** early pieces close with third-person referral —
> "Partner with AI-savvy consultants like AxoWorks to nail your initial setup and training." — *local-llm-privacy*
> "Team up with AI-savvy consultants like AxoWorks to help pick the perfect tool." — *developers-feasibility*

That is **Era 1 and it should not be revived.** Current CTA law is one decisive CTA — *"Talk to The Concierge."*

---

## 4. MECHANICS (measured from the seven files)

| Trait | Observation |
|---|---|
| **Exclamation marks** | Real and frequent in his hand (`GIGO is real!`, `Your data, your rules, your masterpiece!`, `Believe it!`). **Absent from the AI-drafted technical reports.** This is the fastest way to tell the two apart. |
| **Ellipses** | Heavy — `...` as a beat, a pause, a shrug: *"Let's unpack this ..."*, *"This could be your story ..."*, *"Maybe make it look more professional? Check some of the stuff?"* |
| **Second person** | The default. He talks *to* the reader — "Designers", "developers, because", "you grab the leash". |
| **Pop-culture** | Fight Club, Ferraris into brick walls, poker/Vegas card sharks, toddlers doing taxes, milkshakes, the digital wild west, superheroes and bandits. |
| **Joke section titles** | *"From Weeks to Wow in a Snack"*, *"Cracking the Code Jungle"*, *"Pro Forma & Market Scoop Wizardry"*, *"Sneaky Sting of Paid Platforms"*, *"Bonus Wins of Going Local"*, *"How to Get Started"*. |
| **Rhetorical triads** | *"The devil is in the local details"* structures; three-item runs everywhere (*"politicians, advertisers, and the New York Times"*). |
| **Bolded micro-labels** | `**Native Linking:**`, `**Total Control:**`, `**Offline Power:**` — label + colon + one-sentence benefit. The same construction appears in his GitHub README. |
| **Roughness** | Preserved: `"this handler give sharp"`, `"generative tool's"`, double spaces after periods, "for better or worse". **Do not sand it flat; do not manufacture it either.** |
| **Profanity** | Mild and playful, never aimed at a person: *"hineys"*, *"psychopaths"*, *"wild wolves"*, *"sub-intelligence with a pretty face"*. |
| **Emoji / hashtags** | **Zero in article bodies.** Zero hashtags across all seven. Emoji belong to LinkedIn only. |

### 4.1 The two preferences that define him (Kee's own statement of preference)

**He writes abrupt, street-talk, grammatically incorrect sentences on purpose — and would happily take a C or D in English Literature for it.** The trade is deliberate: a grammatically correct sentence loses to one that sounds like a person talking. Abruptness and roughness are the rhythm. Comma splices, run-ons and blunt fragments are in bounds; a sentence the reader must read twice is not.

**He reaches for common, everyday, contemporary things to keep topics simple and light for non-tech, non-AEC readers.** This is wit deployed as a service: a dog on a leash, a puppy, a Ferrari into a brick wall, a toddler doing your taxes, a kid with a milkshake, coffee in your own kitchen, a high-stakes poker game, an ace up the sleeve, a Vegas card shark, Ocean's Eleven, a 70s DJ scratching vinyl, the Vulcan mind meld, a Velvet Underground lyric as the thesis.

**The attitude:** a very human *don't give a damn about conventions*. He is not trying to impress an English teacher, a style guide, or a marketing department. He is trying to be understood and enjoyed by a builder, a homeowner, or a developer — and to have fun doing it.

⚠ **The two failure modes this creates for a ghostwriter:**
1. **Over-polishing.** Writing him in clean corporate English destroys the voice faster than any factual error. Do not fix his grammar.
2. **Under-translating.** Writing an A-2 piece with no everyday image and no wit makes it competent and forgettable — exactly what the byline exists to prevent.

Full doctrine: `AXOWORKS-STYLE-PROFILE.md` §0, and `AXOWORKS-VOICE-GUIDE.md` §§2.10–2.11.

---

## 5. THE FOUR-REGISTER FINAL MODEL

| Register | Signature | Surface | Emoji / tags | Profanity | Polish |
|---|---|---|---|---|---|
| **A-1 Personal** | `Kee \|` | HN, Reddit, peer replies | None | Mild, self-censored | Loose, typo-tolerant |
| **A-2 Commentary** | `Axoworks Commentary` | Canonical opinion, manifesto, audience-facing articles | **None** | Mild, playful | Warm, jokey, exclamation-friendly |
| **A-3 Feed** | his name | LinkedIn, X | **Functional emoji + 5–8 hashtags** | None | Short lines, fragments, swagger |
| **C House / Technical** | `AxoWorks` Technical Report | Deep technical canon, disclosed AI drafting | None | None | Terse, numbered, table-heavy |

**The one rule that spans all four:** receipts, a concession, and a verdict instead of a plea. **The one thing that must never happen:** writing A-2 in the C register. That is the failure mode this file exists to prevent — the firm's own opinion pieces sounding like they were written by a committee that has never met a dog.

---

## 6. THE QUICK TEST

Before shipping anything bylined `Axoworks Commentary`, ask:

1. Could a reader who knows nothing about AEC still enjoy the first paragraph? *(If no, it is a technical report — move it.)*
2. Is there at least one joke, pun, or cartoon image that *carries the argument* rather than decorating it?
3. Is every section title fun rather than descriptive?
4. Does it end on an aphorism, a dare, or a question — **not** a summary?
5. Zero exclamation marks anywhere? *(Then check the byline — you may have drifted into the AI-drafted house register by accident.)*
