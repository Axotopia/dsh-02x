---
name: unpolished-cadence
description: >-
  Build or refine an Axoworks article from a seed draft while deliberately
  preserving Kee's voice, roughness and attitude instead of polishing them
  away. ACTIVATE THIS SKILL when the user says "keep it unpolished", "don't
  polish it", "match his cadence", "calibrate to his voice", "draft this in
  Kee's voice", supplies a rough draft for refinement, or asks for an article
  that must sound like him rather than like the AI-drafted house register.
  Never use this skill to produce clean corporate English.
user-invocable: true
whenToUse: Use for any Axoworks article, LinkedIn post or commentary piece that carries Kee's byline, or whenever a rough draft from Kee needs refining without losing his voice. Requires a seed draft for calibration unless a cadence profile already exists for the audience.
---

# Unpolished cadence — draft in Kee's voice, then check it without flattening it

## The prime directive

**You are not here to write well. You are here to write like him.**

Kee writes abrupt, street-talk, grammatically incorrect sentences **on purpose** and would take a C or D in English Literature for it. Your default instinct — to fix grammar, add transitions, install topic sentences, replace informal words with formal ones — is the single fastest way to destroy this work. **Do not polish. Do not smooth. Do not improve.**

If you catch yourself making a sentence "read better," stop. That sentence was probably right.

## Load order

Read these before doing anything. Full paths under `$HOME/.dsh/.agent-presets/zero-click/reference/` (resolve `$HOME` with the shell first — bash and PowerShell both define it):

| File | Why |
|---|---|
| `AXOWORKS-CADENCE.md` | **The measured numbers.** Bands, shape variants, the arithmetic check. |
| `AXOWORKS-KEE-ARTICLES.md` | His seven hand-written articles — the register you are matching. |
| `AXOWORKS-STYLE-PROFILE.md` | §0 (deliberate roughness), §6 hit list, §7 gate. |
| `AXOWORKS-VOICE-GUIDE.md` | §§2.10–2.11 (street talk, everyday-object translation layer). |
| `AXOWORKS-CALIBRATION-CORPUS.md` | The claims ledger — never invent a number. |

## The eight phases

### Phase 0 — Seed

**Required unless a cadence profile already exists for the audience.** Ask for it plainly:

> "Give me the rough version. Dash it off the way you'd explain it to a contractor — don't make it good, don't fix the grammar, don't organize it. The rougher the better; I'm measuring your rhythm, not your prose."

⚠ **How you ask determines what you get.** If you ask for "a draft that sets the tone," you get his *performance* of a writer. Ask for the unpolished version, because his roughness is the signal.

One seed draft calibrates one audience. His cadence flexes by audience — technical runs denser, homeowner-facing runs lighter, marketing runs swagger. If the new piece targets a different audience from the seed, say so and ask which existing piece to borrow the shape from (see `AXOWORKS-CADENCE.md` §3).

### Phase 1 — Extract, as observables only

Analyse the seed draft and report **only what is measurable**. Hard rule: **do not use trait adjectives.** Never report "conversational tone" — report "median sentence 9 words, 4 fragments ≤3 words, 2 sentences ≥30 words."

Measure: total words · paragraph count · heading count · avg sentence length · longest sentence · count of sentences ≤3 words · per-paragraph avg-sentence min and max · paragraph length min/max · where the heaviest paragraphs sit · heading lengths · whether the closing punchline is a heading · prose share of file words.

### Phase 2 — Skeleton

From the extracted shape plus `AXOWORKS-CADENCE.md` §3, pick a shape variant (verdict arc / feature ladder / continuous rant) and emit a skeleton **with no prose**: arc, section count, per-section word budget, heading length target, block sequence.

If the seed's shape is unusual, **follow the seed, not the median.** The corpus varies its surface more than its shape, and `fight-club` proves headings are optional.

### Phase 3 — Prose, section by section

One section per pass. Each pass carries its own word budget **and its own sentence-length target**, because a single 650-word generation flattens to uniform sentence length and the oscillation does not survive.

Per section, honour:
- The rhythm target — short opener block, long payoff block, alternating.
- ≥ one sentence ≤3 words in the piece, and ≥3 in total.
- The longest sentence ≥26 words somewhere.
- **At least one common, everyday, physical thing carrying an abstract idea** — a dog, a leash, a Ferrari, a toddler, a milkshake, a coffee cup, a poker table. One image per idea. Never stack metaphors. Never explain the joke.
- The body heading style for the chosen shape: fun titles (verdict arc) or named benefits (feature ladder).
- Zero emoji, zero hashtags, zero exclamation-mark suppression in a Commentary piece.

### Phase 4 — Cadence check (arithmetic, independent)

Run `AXOWORKS-CADENCE.md` §4 against the draft. **Report violations against the targeted shape's band** — a continuous-rant piece failing the heading count is correct, not a defect.

This phase **reports**. It does not rewrite. If it rewrites, it will sand.

### Phase 5 — Adversarial deconstruction

Delegate to a child agent that has **never seen the draft's rationale**. Give it the skeleton only, and ask:

1. What argument does this make, in one sentence?
2. Which section carries the weight?
3. What is the closing line?
4. What single everyday image would you use for the central mechanism?

Then compare against the draft. Two findings matter:
- **The child cannot state the thesis** → the structure is not carrying the argument. Fix the structure.
- **The child's image is better than the draft's** → the draft is structurally sound and imaginatively empty. That is the real defect, and it is the one arithmetic cannot find.

### Phase 6 — Kee's pass (the loop)

Present the draft plus the Phase 4 violations and Phase 5 findings. **Do not present a "finished" article.** Ask for keeps and cuts, and offer sentence-level proposals rather than rewrites:

- Cadence deviations he should know about.
- Missing receipts, marked `[NEEDS RECEIPT: …]`.
- Slots where an image is weak and a better one may exist.

**Arithmetic you own. Words he owns.**

### Phase 7 — Feed the diff back

⚠ **The most valuable signal in this entire workflow is what he changes, not what he writes.**

After he edits, diff his version against yours. Each correction is labelled data:

- **Deletions** → filler, transitions, over-explanation. Add to the hit list.
- **Word swaps** → his real vocabulary. Add to the ledger.
- **Sentence splits and merges** → his true rhythm, more accurately than any statistic.
- **Kept lines** → high-confidence voice. Promote to the exemplar corpus.

Append the findings to the relevant file — the diff is worth more than another seed draft, because a draft shows where he starts and an edit shows what he **rejects**. Without this phase the system clones one artifact; with it, it converges on him.

## Hard prohibitions

1. **Never fix grammar.** Comma splices, fragments, run-ons, missing articles, "its" for "it's" — all in bounds. Break the grammar, not the meaning.
2. **Never add transitions.** No "In addition," "Furthermore," "Moreover." The abrupt pivot is the voice — *"Oh, and yes, you have got AI Agents handling the boring stuff too."*
3. **Never formalize his vocabulary.** "Slurp" stays "slurp." "Hineys" stays "hineys."
4. **Never sand roughness on a "polish" pass.** If the user asks you to polish, ask which register they mean first — polishing is the failure mode, not the service.
5. **Never invent a number.** `[NEEDS RECEIPT: …]` and say so.
6. **Never skip Phase 5.** A draft that passes every number and says nothing is the exact outcome this skill exists to prevent.
7. **Never claim the numbers prove it sounds like him.** They prove it is the right shape. Attitude is not measurable.

## Report shape

Phase 1 extraction table → skeleton → the draft → Phase 4 violations → Phase 5 findings → Phase 6 questions for Kee. Never a summary of what you just wrote, and never a "hope this helps." Close on the verdict, per the voice.
