# AXOWORKS — CADENCE PROFILE (measured from Kee's seven articles)

> **What this is.** The *measurable* shape of Kee's writing, extracted from the seven files he identified as most representative of his voice: `three-dog-theory-v2`, `three-dog-theory`, `magic-pill`, `local-llm-privacy`, `hybrid-delivery`, `fight-club`, `developers-feasibility` (all in `Documents\GitHub\Axoworks\public\articles\`).
>
> **What this is not.** It is **not** a template and **not** a measurement of the voice. Cadence is the *skeleton*. The image, the joke, the aphorism and the attitude are the voice, and none of them are in these numbers. A draft can satisfy every number below and still be dead.
>
> **Rule of use:** hold the numbers strictly when **checking** a draft, and loosely when **writing** one. Over-tight generation produces the same three-beat drum every time; the corpus varies its surface far more than its shape.
>
> Measured 2026-09 across all seven articles. Re-measure when new hand-written pieces appear.

---

## 0. THE HEADLINE NUMBER

**`three-dog-theory` sits at or near the median in every dimension measured.** It is a *typical* piece, not an outlier — which is why it works as a reference. `magic-pill` and `fight-club` are the outliers at opposite ends: `magic-pill` is the densest and longest-paragraphed; `fight-club` is the shortest and has almost no structure at all.

---

## 1. THE MEASURED BANDS

Pooled across all seven articles. **Aim inside p10–p90. Investigate anything outside min–max.**

| Dimension | min | p10 | median | p90 | max |
|---|---|---|---|---|---|
| **Total words** | 377 | 377 | **637** | 857 | 1,005 |
| **Paragraph count** | 11 | 11 | **14** | 23 | 24 |
| **Heading count** | 1 | 1 | **6** | 7 | 8 |
| **Avg sentence length** (per article) | 11.0 | 11.0 | **13.3** | 16.6 | 16.7 |
| **Longest sentence** (per article) | 26 | 26 | **38** | 45 | 55 |
| **Avg paragraph** (words) | 26.5 | 26.5 | **36.7** | 58.5 | 83.8 |
| **Longest paragraph** (words) | 47 | 47 | **74** | 96 | 155 |
| **Heading length** (words) | 2 | — | **6–8** | — | 17 |

### Sentence-length distribution (338 sentences, pooled)

| Statistic | Value |
|---|---|
| mean | **13.6 words** |
| median | 13 words |
| p10 | **3 words** |
| p90 | **25 words** |
| range | **1 → 55 words** |

**Read that p10 again: one sentence in ten is three words or shorter.** The short-sentence bursts are not occasional garnish — they are a tenth of the prose.

### Per-paragraph average sentence length (111 paragraphs, pooled)

| Statistic | Value |
|---|---|
| mean | 13.9 |
| median | 13.3 |
| p10 | **5.3** |
| p90 | 24.0 |
| range | **2 → 41** |

A paragraph averaging **2 words per sentence** and a paragraph averaging **41** appear in the same corpus. That spread is the rhythm.

---

## 2. THE FOUR NON-NEGOTIABLE SHAPE RULES

Everything else is a range. These four held in every article measured.

1. **The average sentence length is tight and low (11–17 words) while the ceiling is high (26–55).** All seven articles land within ~6 words of each other on the average, yet every one contains a sentence double or triple that length. **The voice lives in the variance, not the mean.** A draft with a uniform 14-word sentence length fails even though its average is correct.

2. **Short sentences are structural, not incidental.** ≥10% of sentences run ≤3 words. Expect 3–6 per article of pure fragment (*"It's adorable."*, *"Suckers bet."*, *"Not a Pet; it's a Partner."*).

3. **The verdict carries the heaviest prose. The setup never does.** In every structured piece the largest paragraphs cluster in the closing section. Front-loaded context is the house-register (C) shape, not his.

4. **One promoted H2 closes the piece.** The final punchline is frequently marked up as a **heading**, not a paragraph, so it survives as an outline item for a reader who never reads the body — *"The hard choice: Do you want to play with puppies, or do you want to get paid?"* (17 words, the longest heading in the corpus).

---

## 3. THE SHAPE VARIANTS (choosing among them is legitimate)

The seven articles are **not** one template. Three recognisable shapes, and picking among them is how you avoid the same drum every time:

| Shape | Books | Signature | Use for |
|---|---|---|---|
| **Verdict arc** | `three-dog-theory`, `three-dog-theory-v2` | Setup (~15%) → 3 escalating named sections (~16/19/21%) → verdict (~29%). Short H2 label, short opener paragraph, long payoff paragraph, repeated per section. | Manifesto and framework pieces. Frameworks delivered as numbered *characters*. |
| **Feature ladder** | `hybrid-delivery`, `developers-feasibility` | 5–7 H2s, each a **named benefit**, one short paragraph or a bolded `**Label:**` + explanation. No jokes; benefit-led. | Firm-facing service copy and audience-specific pages. |
| **Continuous rant** | `fight-club` | **One heading. 377 words. 11 paragraphs.** It just goes, and it ends on *"See you in the pit."* | When the argument is a single sustained attitude. Proves headings are optional — do not force structure onto a piece that wants to run. |

`magic-pill` is a fourth mode — playful, long paragraphs (avg 83.8 words), joke section titles — closest to a magazine feature. Use sparingly; it is the far end of the paragraph-length band.

---

## 4. HOW TO CHECK A DRAFT (arithmetic — ungameable)

Compute these on the finished draft. Report violations; do not silently rewrite.

```
[ ] Total words within 377–1,000, targeting ~637
[ ] Paragraphs 11–24, targeting ~14
[ ] Headings 1–8, targeting ~6  (1 is legal — see "continuous rant")
[ ] Average sentence length 11–17
[ ] Longest sentence ≥26  (if the max is ~17, the draft has no release valve)
[ ] ≥10% of sentences ≤3 words  (count them; expect 3–6 fragments)
[ ] No more than 2 consecutive sentences within 3 words of each other in length
[ ] Per-paragraph avg-sentence spread reaches at least one paragraph ≤6 and one ≥20
[ ] The longest paragraphs sit in the closing section, not the opening
[ ] Headings: median 6–8 words; at least one is a joke, a label or a question
[ ] Closing punchline promoted to a heading
[ ] Prose is 46–70% of the file's total words (markup overhead is normal)
```

Any ❌ means the draft is off-shape. **It does not mean the draft is bad** — `fight-club` would fail the heading count and be entirely correct. Say which shape you targeted and check against that shape's band.

---

## 5. WHAT THESE NUMBERS CANNOT DO

State this plainly to anyone who asks the cadence engine to "make it sound like Kee."

- They cannot choose the image. Why a dog and not a poker table is taste.
- They cannot judge whether the joke lands.
- They cannot write the aphorism. They can only detect that none exists.
- They cannot detect attitude. A grammatically perfect draft can hit every number.

**A draft that passes §4 and has no line a reader would repeat to a colleague is a failure, not a pass.** The numeric gate is necessary and not sufficient. See `AXOWORKS-STYLE-PROFILE.md` §7 for the human-taste gates that sit alongside it.
