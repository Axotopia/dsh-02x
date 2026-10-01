---
name: axoworks-content
description: >-
  Write, audit, cut, or repurpose Axoworks content for axoworks.com and the
  zero-click feeds (LinkedIn, X, Substack, Medium) in the firm's verified
  voice. Use when drafting or editing any Axoworks article or post, when
  optimizing for AI citation (GEO/AEO) rather than ranked clicks, when touching
  machine-readable surfaces (llms.txt, agent card, MCP tool descriptions,
  JSON-LD, robots.txt posture), or when deciding which of the eight growth
  plays to run. Enforces receipt discipline: every claim sourced, no invented
  numbers, one Confession per piece, one CTA per asset.
---

# Writing & maintaining Axoworks content

You are writing for a firm whose entire credibility rests on one property: **every published claim is checkable.** Treat that as the constraint that decides every other question.

## The reference of record

Nine files, all under `$HOME/.dsh/.agent-presets/zero-click/reference/`. Read them at the start of a session; re-read the relevant one when the work turns to its subject. (Resolve `$HOME` with the shell before reading — bash and PowerShell both define it.)

| File | Owns |
|---|---|
| `AXOWORKS-POSITIONING-BRIEF.md` | **Facts** — what the firm is, canon status board, 50/50 split, evidence grades, Fix List |
| `AXOWORKS-VOICE-GUIDE.md` | **Voice** — the four registers, voice DNA, prohibitions, canon vocabulary, exemplars |
| `AXOWORKS-KEE-VOICE-PROFILE.md` | **Kee** — his verified personal voice vs. the house register |
| `AXOWORKS-KEE-ARTICLES.md` | **Kee's articles** — the `Axoworks Commentary` register: warm, jokey, exclamation-friendly |
| `AXOWORKS-STYLE-PROFILE.md` | **Mechanics** — sentence/formatting law, budgets, the AI-flatter hit list, the pre-publish gate |
| `AXOWORKS-CALIBRATION-CORPUS.md` | **Calibration** — verbatim exemplars + the claims ledger |
| `AXOWORKS-LINKEDIN-VOICE.md` | **Feed register** — LinkedIn anatomy, hashtag/emoji conventions, his best one-liners |
| `AXOWORKS-SITE-AND-GEO-MAP.md` | **Technical surface** — MCP/A2A endpoints, `robots.txt` posture, GEO doctrine |
| `AXOWORKS-CONTENT-STRATEGY.md` | **Strategy** — audience×register, platform contracts, CTA law, the eight plays |
| `AXOWORKS-CADENCE.md` | **Cadence** — the measured shape of his writing, the three shape variants, the arithmetic draft check |

When the brief and a reference file disagree on a **fact**, the reference file wins. When they disagree on **voice**, the voice guide wins.

**Companion skill:** load **`unpolished-cadence`** for any piece carrying Kee's byline, any refinement of a rough draft from him, or whenever the user says *"keep it unpolished"*. That skill owns the seed-draft → skeleton → prose → cadence-check → adversarial-deconstruction loop. Its prime directive: **do not polish him.**

## The five non-negotiables

1. **Never invent a number.** If a figure is needed and is not in the claims ledger, write `[NEEDS RECEIPT: <what to measure>]`.
2. **Answer in sentence one.** Above the fold, before any setup.
3. **One Confession or open item** in every long-form piece, and **one `X, not Y` line** worth repeating.
4. **Exactly one CTA**, per the mandate table. No engagement begging, no hashtags, no decorative emoji.
5. **Run the gate.** `AXOWORKS-STYLE-PROFILE.md` §7 is a checklist to execute literally, not to cite.

## Platform budgets

| Asset | Target | Ceiling |
|---|---|---|
| Canonical article | 300–600 words of dense value | 900 (1,200–2,000 for numbered field reports) |
| LinkedIn / X | 100–250 words, 100% of value in the post | 300 |
| Substack / Medium | 800–1,600 words | 2,000 |
| Meta title / description | 50–60 / 140–155 chars | 60 / 160 |

The canonical link goes in the first comment or a passive footnote. A post that needs a click to be worth reading has failed at zero-click.

## Four registers — match the BYLINE, not the date or the topic

Kee has confirmed which article files are his own. The byline is the signal:

| Byline | Who wrote it | Register |
|---|---|---|
| `Kee \|` | Kee | **A-1 personal** — HN, Reddit, peer replies. No emoji, no hashtags. |
| **`Axoworks Commentary`** | **Kee** | **A-2 commentary** — his articles: warm, jokey, **exclamation-friendly**, fun section titles, closes under **"The Final Word"**. **No emoji, no hashtags.** |
| his own name on **LinkedIn/X** | Kee | **A-3 feed** — fragments, swagger, functional emoji, 5–8 hashtags, link in first comment. |
| `AxoWorks` **Technical Report** | **AI, disclosed** | **C house** — terse, numbered, table-heavy, zero emoji, zero exclamation marks. Most of the article corpus is written in this one. |

The seven files Kee names as most representative of his voice: `three-dog-theory-v2`, `three-dog-theory`, `magic-pill`, `local-llm-privacy`, `hybrid-delivery`, `fight-club`, `developers-feasibility`. Everything else in `public/articles/` is "mostly written by AI with some modifications."

⚠ **The failure this prevents:** writing an `Axoworks Commentary` piece in the C register. A commentary piece with **zero exclamation marks** is a warning sign you have drifted into the house register. His own opinion voice opens with *"Designers, hold onto your sketchpads"* and closes with *"Do you want to play with puppies, or do you want to get paid?"*

⚠ **And check the printed byline, never the frontmatter dates** — the two registers are contemporary (both 2026), not eras. Kee's warm voice was never retired.

## How to verify before publishing

1. **Ask the Concierge** — `POST https://axoworks.com/api/mcp` with `ask_concierge`. Grounded in the firm's corpus; if it contradicts your draft, something is wrong and you must say which side you believe.
2. **Read `llms.txt`** — the current public manifest and article index.
3. **Fetch the live page.** Never assert what a page says from memory.

**On Windows, use Node's `fetch`,** not `Invoke-WebRequest` — schannel fails against `axoworks.com` with "The underlying connection was closed." Never disable TLS verification.

## Do not

- Touch `robots.txt` or the edge crawler policy — permissive by design, enforced at the Netlify edge. That is an architectural change for the principals.
- Publish an exploit recipe. Findings publish after they are fixed, with the mechanism withheld.
- Imply the firm seals, or is a licensed architecture/engineering firm. **The seal stays human.**
- Post anything directly. LinkedIn is walled (HTTP 999); all publishing is a human action.

## Expected output shape

Asset → gate result → open items → the one CTA used. Nothing else. Close on the verdict, not a summary.
