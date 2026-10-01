# AXOWORKS — KEE'S VOICE PROFILE (the principal, in his own hand)

> **Provenance.** Built from primary sources retrieved live: two Show HN submissions and **all 13** of his Hacker News comments (`hn.algolia.com/api/v1/search_by_date?tags=comment,author_axotopia`, `nbHits: 13` — exhaustive), both signed **`Kee |`**; the `github.com/Axotopia/revit-tools` README; and his own article corpus.
> Identity chain: HN `axotopia` ≡ GitHub `Axotopia` ("Kee Song | 宋琦賢") ≡ the `github.com/Axotopia` links published in Axoworks' own articles. Full name **Kee H. Song**.
> **LinkedIn (`/in/axosphere`) is login-walled — HTTP 999, zero bytes.** No LinkedIn or X post was retrievable. Everything below is from surfaces he wrote and signed without a wall.

---

## 0. THE HEADLINE FINDING: THERE ARE FOUR REGISTERS, AND THEY ARE NOT INTERCHANGEABLE

⚠ **Updated 2026-09.** This file began with two voices. Two further primary sources expanded it: Kee's **LinkedIn post feed** (register A-3, see `AXOWORKS-LINKEDIN-VOICE.md`) and his **seven hand-written articles** (register A-2, see `AXOWORKS-KEE-ARTICLES.md`). Kee writes in **three** of the four registers; the fourth is the firm's AI-drafted technical voice, which he did not write and which must keep its disclosure.

**The headline is unchanged and now better supported: the registers must never be blended.**

| | **A — Kee, personal** | **B — Axoworks, published** |
|---|---|---|
| **Signature** | `Kee \|` | `AxoWorks` |
| **Pronoun** | **I** for failure, *we* for the firm, *you* for the challenge | **we** for the firm, **you** for the reader's firm. Never *I*. |
| **Register** | Warm, loose, run-on, comma splices, second thoughts, ellipses for enthusiasm | Terse, numbered, bolded, verdict-first |
| **Polish** | Typo-tolerant. Real roughness is a feature. | Machine-tight. Every number receipted. |
| **Profanity** | Real and self-censored (`f***`). Lands on claims and technology, **never a person** | **None.** Zero appears in any report or README. |
| **Metaphor** | Domestic, structural, self-deprecating | Industrial, short, load-bearing |
| **Structure** | Prose paragraphs, "battle scars" bullets, a dare at the end | Numbered sections, tables, TL;DR, Definitions, `Q0.` FAQ, "What is still open" |
| **AI disclosure** | Not applicable — it is him | **Mandatory.** "Drafted with three AI models… edited by humans who sign it." |

**The two registers this table omits** — A-2 `Axoworks Commentary` (his articles: jokey, exclamation-friendly, fun section titles) and A-3 feed (LinkedIn: fragments, swagger, functional emoji) — are documented in their own files and follow the same separation law.

**⚠ The single biggest risk in this workflow:** treating register C's austerity as the house voice and losing Kee. The firm's credibility does not come from the polish. It comes from a 30-year AEC veteran publicly conceding that his own logs leaked contacts — and from a firm whose opinion pieces are allowed to open with *"Designers, hold onto your sketchpads."* **Register C borrows its authority from A's honesty, not the reverse.**

---

## 1. VERBATIM SAMPLES — VOICE A (his own hand)

**On why he killed the website — the domestic detail that makes the whole thing credible:**
> "I run a building design consultancy for homeowners and architects, not a SaaS firm. Honestly, I'm not going to claim we were trying to build some fantastic 'anti-fragile alternative' for the future… I just got tired of paying Wix $40 a month for a brochure no one read. The portfolio was static, the inquiries were generic, and every time a potential client asked about setback variances, I'd lose hours explaining the same thing. **So last December, I told my wife I was killing the website. She thought I'd lost it. Maybe I had.**"
> — `news.ycombinator.com/item?id=47387398`

**On the mess, volunteered without being asked:**
> "The stack? It's messy. We started on Netlify because it was cheap. Hit that stupid 10-second serverless timeout after a week when I started customizing the bot. The bot would just… freeze."
> "It works, but it's not elegant. **It's duct tape.** Last time I coded was over 30 yrs ago. AI helped a lot, but it feels like **3 steps forward, 2 steps back** when it starts obsessing about one area and wrecks what was done 5 refactors ago."
> "We've gone through four architectural versions. **Started with 30k lines of spaghetti.**"
> — `item?id=47387398`

**On liability — the sentence that explains the entire verification doctrine:**
> "**Liability is the real killer.** In our world, if the AI hallucinates a building code clause, we're done. Insurance won't touch us. … **We publish the crash logs publicly because hiding them feels dishonest. Also, it keeps us honest.**"
> — `item?id=47387398`

**The dare and the sign-off:**
> "The terminal is live at https://axoworks.com. Mic optional. No signup. **Try to break it.** Ask a complex zoning question. See if it over-promises. … I'll be in the comments. Thanks. **Kee |**"
> — `item?id=47387398`

**Near-verbatim repeat in the second Show HN — his instincts are consistent:**
> "A few battle scars: … Liability is the killer. Hallucinate a building code clause? We're dead. … We publish the audit logs to keep ourselves honest and make sure the system stays hardened."
> "The hardest part was getting the intent right: making one LLM pivot seamlessly from a warm principal's tone with a homeowner, to a defensive bulldog when attacked by a peer. That took 2.5 months of tuning."
> "Try to break it. I'll be in the comments. **Kee |**"
> — `item?id=47441587`

**The concession cadence — this is his most reproducible move.** Six separate times in one hostile thread:
> "**You caught me.** Tina is my co-founder, so those are her business contacts, but you're absolutely right, still a dumb move to leave them exposed instead of routing everything through single secure point of contact. I completely missed them when I dumped our raw resumes into the RAG context. **My oversight for blindly claiming the logs were totally clean.** I just updated the backend and permanently scrubbed the contacts. Genuinely appreciate you pushing back and catching my blind spot!"
> — comment `47460105`

> "**Good point.** … But you are 100% right that seeing it raw in the logs looks sketchy to a user. **Thanks for keeping me honest here.**" — `47458929`
> "**You are spot on.** Right now it's just a messy backend data dump. … **Appreciate the reality check.**" — `47448741`
> "**Good catch.** Those bios and lists are essentially grounding truth for the training data for the RAG. … **Appreciate the sharp eye!**" — `47446565`
> "**haha, good catch!** I focused on the AEC logic but did not put enough on the general guardrails. … **Appreciate the stress test!**" — `47446020`
> "**haha, I might have let the Agent Experience persona get to dramatic here**… its definitely feeling the oats today. I'll dial it back on my next refinement. Thanks!" — `47445334`

**The honest hedge — his model for any claim he cannot prove:**
> "I don't have his/her ID, just a session ID with technical substance of the chat to sound alarm bells on my end. Respectfully, it's OK if find the tool lacking. … If it doesn't weork for your workflow, that's fair critique." — `47444576`
> (Note the typo `weork` — preserved here as evidence, **not** as a template. Do not manufacture typos.)

**The generosity that reads as confidence, not naivety:**
> "the real value isn't in the text since it is very specific to my firm and work experience, the value is the underlying design logic and the specific 'if-then' professional constrains baked into the system. Plus, the audit logs are part of a 'transparency' experiment, **if it helps someone else build a better tool for the industry, Im all for it!**" — `47447716`

**The deliberate crippling — scope limits stated as design, not weakness:**
> "I'm a 2-person firm, cannot compete with ChatGPT on general knowledge, but I'm also **intentionally 'crippling' the bot's autonomy for liability reasons.** It is designed to move the user toward a human once/if the technical complexity gets high, so it doesn't accidentally misrepresent a code or site issue, that could get us into legal trouble. It is a balancing act between utility and risk… if that makes sense?" — `47447182`

**The one line that shows he knows exactly what he is doing:**
> "I hope it proves our worth in the AI arena against the big firms, and filters out the **95% of the dead inquiries** we get. **Time will tell me this works.**" — `47445063`

**The README tick — "honest unavailable, never invent a number" (his doctrine, stated in code):**
> "**Deterministic math.** The audit tools compute numbers from the model's geometry. **When data is absent, the tool says "not in the model" instead of inventing a figure.**"
> "Audit tools marked 'placeholder' return honest narratives about what they could and could not compute. **They never invent a number.**"
> "**Single-threaded.** Every query queues on Revit's UI thread. Rapid-fire calls or retry loops can **permanently deadlock** the MCP connection… The only cure is restarting the add-in or Revit. **One query at a time, stop on error, never retry-storm.**"
> "**No governance layer.** … The *agent* must be disciplined: stop on error, do not retry blindly."
> — `raw.githubusercontent.com/Axotopia/revit-tools/main/README.md`

---

## 2. MECHANICS OF VOICE A

**Rhythm.** Short declaratives, then a two-word verdict. Fragments as emphasis — *"Total."* *"Sucker's bet."* *"Still a headache."* Comma splices are normal. Ellipses (…) and em-dashes carry enthusiasm rather than precision.

**Openers.** Never a setup. Always a concrete grievance, cost, or confession in sentence one: *"I run a building design consultancy."* / *"I got tired of paying Wix $40/month."* / *"2 weeks ago, a licensed architect attacked the bot."*

**Quantification.** Informal and specific: `30 yrs`, `2.5 months`, `$40/month`, `95% of the dead inquiries`, `19 out of 20 visitors`, `30k lines of spaghetti`, `four architectural versions`. He quantifies *effort and failure* as readily as success — which is why it reads as honest.

**Concession cadence (institutionalize this).** Two-word concession → restate the error plainly → name the fix → thank the critic. The two-word openers he actually uses: *"You caught me." · "Good catch." · "Good point." · "You are spot on." · "Fair call." · "Fair criticism."*

**Hedges that signal a real person thinking live:** *"if that makes sense?" · "Time will tell me this works." · "IDK if this is the final answer." · "Maybe I had." · "for better or worse."*

**Endings.** A dare plus a sign-off: *"Try to break it. I'll be in the comments. Thanks. Kee |"*

---

## 3. MECHANICS OF VOICE B (firm register — for contrast)

**Openers.** A bolded one-paragraph definition of the pre-synthesized thesis, quantified. Or the number alone.

**Shape.** Numbered sections where each title is a **claim**; a TL;DR whose bullets are *findings*; a comparison table in nearly every section; a formal **Definitions** block; an FAQ whose first question is literally `Q0.`; a "What is still open" section; Sources; then the AI-drafting disclosure.

**The house construction — shared by BOTH voices.** The `X, not Y` pair. This is the one move that appears in Kee's own hand *and* the AI-drafted canon:
> "The license is a floor, not a moat." · "Rails, not refusal. Mechanism design, not exhortation." · "Installed, not ranked; called, not clicked." · "Bought plumbing. Built soul." · "not a Pet; it's a Partner." · "The receipt is on the GitHub, not on the parapet." · "An instrument, not a boombox."

**Voice B metaphors — industrial and short.** *"a press release wearing a trench coat"* · *"a mirror with a search bar"* · *"a panel of witnesses who all read the same newspaper"* · *"The model is a fast, tireless, occasionally fabulist junior employee. It never signs the sheet."*

**Counterargument pattern.** Put the objection in its own bolded line and answer it in the next sentence:
> **"You're a technology company."** No. The technology is the receipt; the buildings are the work.

---

## 4. THE COMMENTARY REGISTER (A-2) — his articles, not a proxy

⚠ **Corrected 2026-09.** This section was originally labelled "the bridge — closest proxy to LinkedIn," on the assumption that LinkedIn was unreadable and the commentary pieces were merely AI-drafted work in his cadence. **Both assumptions were wrong.** Kee confirmed the seven Commentary articles as the pieces most representative of his own voice, and the LinkedIn feed is now captured separately.

**A-2 is not a proxy for anything. It is his.**

> "You are a tiny team, no corner glass offices, no $300M training budget, no HR department writing apologies, definitely no legal department covering your hineys." … "**Your arena. Your game. See you in the pit.**" — *fight-club*

> "Designers, hold onto your sketchpads because generative AI is crashing your party, and it's bringing some serious game." — *magic-pill*

> "Pure bullshit. LLMs are stochastic dice-rollers wearing a suit. Expecting deterministic output? That's like expecting 'snake eyes' with every throw because you did the math on your wrist snap. **Sucker's bet.**" … "**Verdict:** You don't have a partner. You got a mirror with a search bar." — *the-lineup*

> "**A quota is a short position on your ambition.**" … "**That's the honest version of the pitch. It's also the LinkedIn version. They're the same post.**" — *death-of-the-dashboard*

> "$0.74. That is what surviving the Hacker News front page cost us. Total." … "**Tiny is Mighty. Believe it!**" — *seventy-four-cent-website*

> "The dogs are already in your yard. The only question left is: **Are you running a shelter, or are you part of an Elite Unit?**" — *three-dog-theory*

⚠ **Mechanics note:** A-2 uses **exclamation marks freely** and closes under the literal heading **"The Final Word."** Neither appears in register C. Full anatomy: `AXOWORKS-KEE-ARTICLES.md`.

---

## 5. DO'S AND DON'TS FOR A GHOSTWRITER

### If you are writing as Kee (Voice A)

**DO**
1. Open with "I" and a concrete grievance or cost.
2. Admit the messy middle unprompted — *"It's duct tape."* / *"3 steps forward, 2 steps back."*
3. Allow loose punctuation, second thoughts, and genuine informality.
4. Include one unguarded human detail. One. It is what makes the rest believable.
5. Concede in the first two words when corrected, then name the fix, then thank the critic.
6. Hedge honestly: *"if that makes sense?"* / *"Time will tell."*
7. Quantify effort and failure as readily as success — `30 yrs`, `four architectural versions`, `2.5 months`.
8. End on a dare plus `Kee |`.
9. Say the thing that costs you: *"Liability is the killer. Insurance won't touch us."*

**DON'T**
1. **No hashtags, no decorative emoji.** Zero appear anywhere in the retrievable corpus.
2. Never profane a person or a client. Claims and technology only; self-censor when strong.
3. No throat-clearing openers.
4. Never end on a neutral CTA like "thoughts welcome." End on a dare, a verdict, or your name.
5. Never claim a superlative without the hedge pattern *("I'm not going to claim we were trying to build some fantastic…")*.
6. Never hide the unresolved item.
7. Never defend the tool against fair criticism.
8. **Do not manufacture typos.** His roughness is authentic; faked roughness is pastiche. Do not sand his roughness away either — just do not invent it.

### If you are writing as Axoworks (Voice B)

**DO** — bolded thesis paragraph, coined-and-capitalized mechanism names with a Definitions block, numbered sections, a table per section, `Q0.` FAQ, "What is still open", Sources, the AI-drafting disclosure, `we`/`you` pronouns, the `X, not Y` pair, a closing triad, the licensure boundary stated as a feature, and the honest-absence rule verbatim (*"never invent a number"*).

**DON'T** — never attribute a technical report to Kee personally; never carry heist/dog/fight-club metaphors into a technical report; no profanity; never leave a counterargument unanswered; never drop the limitations section; never over-claim a first; **never write a marketing conclusion — write a verdict, then the sources.**

---

## 6. THE FOUR-REGISTER ROUTING RULE

> If it is signed **`Kee |`**, it is short-sentence, confessional, `I`-led and typo-tolerant.
> If it is signed **`AxoWorks`**, it is table-heavy, `we`-led, formally defined and disclosed.
> **Both share exactly one signature move: the `X, not Y` aphorism, and a closing verdict instead of a call to action.**

---

## 7b. HOW TO EXTEND THIS PROFILE

All four registers are now documented from primary sources. What remains thin:

- **LinkedIn comments and the LinkedIn Articles tab** — the posts feed is captured (18 posts), but comments are not, and that is where the most unguarded writing usually lives.
- **X/Twitter** — no posts publicly retrievable.
- **Medium** — bylined throughout LinkedIn but Cloudflare-walled (403) to automated fetch.
- **Podcast audio** — three mp3s exist in the corpus, untranscribed.

When Kee supplies any of these, extend the matching register file and note the date range. Until then, say what is unread rather than implying coverage.
