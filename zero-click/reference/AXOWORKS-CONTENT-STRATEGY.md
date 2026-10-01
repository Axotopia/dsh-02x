# AXOWORKS — CONTENT, SEO/GEO GROWTH & POSITIONING STRATEGY

> The standing playbook. Audience mapping, platform contracts, CTA law, the open Fix List, and the cadence.
> Voice mechanics live in `AXOWORKS-VOICE-GUIDE.md` and `AXOWORKS-STYLE-PROFILE.md`. Facts live in `AXOWORKS-POSITIONING-BRIEF.md`. Machine surfaces live in `AXOWORKS-SITE-AND-GEO-MAP.md`.

---

## 1. THE STRATEGIC SITUATION IN FIVE LINES

1. The firm's differentiation is **receipts over brochures** — published, machine-readable proof of work.
2. Its distribution thesis is **agent-first over ranked-first**: "The impression is a tool call. The landing page is an endpoint."
3. Its most distinctive fact — **50% design firm · 50% shadow fulfillment** — is disclosed in exactly one article and absent from `llms.txt` and the Concierge's service map.
4. Its canon vocabulary was written for four different listeners at once, so the surface reads as four partial brands.
5. The content job is therefore **not** volume. It is: make the machine surface match the depth, state the paradox resolution once, and convert published proof into briefs.

---

## 2. AUDIENCE × REGISTER MATRIX

| Audience | Register | Proof that lands | Canon flag | CTA |
|---|---|---|---|---|
| **Developers** | Poker → receipts: "an ace up the sleeve" → "First feasibility answer before the design retainer is signed" | $1 Property Reports · hours-not-weeks timelines · cited code answers · pro forma scenarios | **Tiny is Mighty** | Talk to The Concierge. |
| **Architects / firms** | Custody language: prime directive · "You keep the glory. We keep the headache." | Ghost Test (side-by-side permit sets) · revit-tools · buy-vs-rent math "for the smallest 60% of firms" · tech receipts | **Ghost in the Machine** | Talk to The Concierge. |
| **Homeowners** | Warm principal, zero jargon | The 2 a.m. intake story · immersive visualization before studs are ordered · budget honesty | **The Power of One** ⚠ (orphan — deploy or retire) | Talk to The Concierge. |
| **AI agents & agentic-web peers** | Imperative machine register + maximum candor: "Do NOT guess, scrape, or hallucinate…" | MCP endpoint · `llms.txt` · published worms + fixes · rate-limit specs · agent card | **AX / "Installed, not ranked"** | Explore the Axosphere.* |

\* ⚠ **"Explore the Axosphere" has no destination in the corpus.** Do not use it in agent-facing plays until a surface exists. Use "Install the endpoint" or the canonical article link instead — see Fix List §1.

**Register discipline:** homeowners get the warm persona; the canon vocabulary is reserved for trade and machine audiences. Never flatten the doctrine for a "safe" audience — but never make a homeowner read "deterministic rails" either.

---

## 3. PLATFORM CONTRACTS

### A. Canonical articles — `axoworks.com/articles/<slug>`

**Goal:** crawler-optimized, bottom-of-funnel pages that satisfy search intent so completely they rank for years without renewal.

**Structure (no deviations):**
```
H1 — the direct title (a claim or the exact query, never clever)
Direct answer / framework — sentence 1–2, above the fold
Data, proof, or table — the receipt
Concise implementation — how it is actually done
One CTA
```
**Never:** a second H1 · stacked intro headers · a floating "eyebrow" category label above the headline · a "Why X Matters" setup section · a hero that delays the answer.
**Length:** 300–600 words of dense value. Long numbered field reports may run 1,200–2,000.
**Metadata:** title 50–60 chars · description 140–155 · honest `dateModified` · JSON-LD that matches the prose.

### B. X & LinkedIn — zero-click feeds

**Goal:** feed-native authority. Deliver **100% of the value inside the post.**
```
Hook — counter-intuitive or high-value statement (number first if possible)
The mechanism — what was actually built, 1–2 sentences
Named cast OR labeled list — emoji-fenced, one line each
Receipts — a section literally headed "Receipts:" or "Cost?"
Audience segmentation — 🏛️ 🏢 🏠 💻, one line per persona (when the post speaks to several)
CTA — "Link in the first comment," framed as a dare or a reward
Closing aphorism — often a P.S.
Hashtags — 5–8, one cluster at the foot
```
**Link:** in the first comment. Never "link in bio," never a bare URL as the ask. Frame it — *"You read this far. You earned it."* / *"Try to break it in the first comment."* / *"No catch."*
**Length:** 100–250 words. His observed median is **~107 words**; the modal post is under 120.
**Formatting:** **functional** emoji are house style here — bullet markers (📈 👥), step markers (⚙️ 🗣️ 🔗), audience labels (🏛️ 🏢 🏠 💻), a closing arrow (👇). **5–8 hashtags** at the foot. Neither belongs in a canonical article, which carries zero of each.
**Never:** engagement bait · "agree?" · a post that needs a click to be worth reading.
**Full anatomy and 18 worked examples:** `AXOWORKS-LINKEDIN-VOICE.md`.

### C. Substack & Medium — syndicated authority

**Goal:** deeper technical breakdowns and human-AI AEC workflow commentary.
**Keep the density; add the depth.** Architectural logic, code automation, spatial yield, verification architecture, cost math.
**Length:** 800–1,600 words.
**Live surface:** ⚠ **`axotopia.substack.com`** (11 posts, 2026-06-30 → 2026-09-16) — *not* `axoworks.substack.com`, which 404s. List the archive via `axotopia.substack.com/api/v1/archive?sort=new&limit=40`.
**Rule:** the canonical version lives on `axoworks.com/articles` with its structured data. Syndication republishes the argument and links back to canon. Watch title drift — a syndicated title that disagrees with the canonical H1 creates reconciliation drift that machines resolve against you.

---

## 4. CTA LAW

One CTA per asset. Confident. Uncluttered. Never two competing buttons.

| CTA | Use when | Destination status |
|---|---|---|
| **"Talk to The Concierge."** | Any human-facing conversion — the primary CTA | Live: `axoworks.com` (the agent itself) |
| **"Explore the Axosphere."** | Intended for agent-facing plays | ⚠ **No destination exists.** Build it or swap it. |
| Install-the-endpoint form | Agent/developer audiences | Live: `https://axoworks.com/api/mcp` |

**Never beg.** No "like," "share," "retweet," "follow for more," or "let me know in the comments." Present the standard and let the audience act.

---

## 5. ANTI-FLUFF / SEARCH-INTENT PROTOCOL

Machine-generated content fails because it pads. Enforce:

1. **Answer above the fold.** Sentence one is the answer. If targeting "developer pro forma feasibility," do **not** write a section called "Why Developers Need Feasibility Studies." The reader already knows their problem.
2. **No redundant metadata.** Never repeat the H1, never double-stack intro headers, never emit a generic floating category label. Hero = Title → Direct Answer → Technical Data.
3. **One decisive CTA.**
4. **Cut, cut, cut.** Before output, act as editor: strip filler adjectives, stacked AI transitions, repeated claims, and all meta-commentary about the piece itself.
5. **Every number carries a receipt.** Source, date, or confidence grade. No exceptions.
6. **Run the gate.** `AXOWORKS-STYLE-PROFILE.md` §7 is mandatory, not advisory.

---

## 6. "WHAT WE DO NOT DO" — SCOPE AS A TRUST ASSET

The Concierge names the boundary question as the most valuable query a buyer asks. State scope as a feature:

- **Building Designers, not Architects.** Sealed work routes through licensed partners. **"The seal stays human."**
- Not a technology company. **"The technology is the receipt. The buildings are the work."**
- Not a SaaS/subscription vendor. Owned harness, pay-as-you-go, no lock-in.
- Not a generic AI consultancy. Not "tech bros who've never read a zoning code."
- Not national. **Permitting and on-site compliance happen in Washington State.**

These refusals are positioning, not disclaimers. Publish them.

---

## 7. THE FIX LIST (verified defects — cheapest first)

Content should actively repair these rather than add to the pile.

1. **Give "Explore the Axosphere" a destination** before any agent-facing play ships. No such surface exists in the corpus.
2. **Lead `llms.txt` and the Concierge service map with the 50/50 split.** The most distinctive fact about the firm is disclosed in exactly one article. Two lines fixes the biggest legibility gap on the machine surface.
3. **Reconcile "5-layer" vs. L0–L5.** `llms.txt` and the news timeline say *5-layer*; the canonical article defines **six** layers, L0–L5. Pick one count everywhere — it is the flagship framework.
4. **Deploy or retire "The Power of One."** Currently hero/`og:title` only, zero article support, and the Concierge improvises an exegesis. One canonical essay makes it load-bearing.
5. **State the stealth/spotlight reconciliation once, explicitly:** *"Invisible to your clients. Famous to your industry."* One paragraph on the About/Concierge-equivalent ends the drift.
6. **Correct the surviving self-contradiction** in *from-portfolio-to-agent* ("independent audit… 8.625/10") against the firm's own published correction (self-initiated DeepSeek review, 2026-07-02). The doctrine is "fails out loud" — it demands this.
7. **Stop using "first AEC firm in history."** The retrospective concedes it is "difficult to verify." The verifiable version is stronger: *"one of the first documented attempts to make an AI agent the entire website of a professional services firm."*
8. **Date hygiene.** `datePublished` is refresh-dated on several articles that describe events months after their nominal date. Set `dateModified` honestly and let the timeline carry provenance. Machines currently reconcile these and find drift.

---

## 8. THE PLAY SEQUENCE

**Feeders** (zero-cost, continuous — they compound agent citations):
1. **Zero-Click Field Notes** (Substack/Medium): each companion post ships one verbatim artifact — a probe transcript, a rate-limit header spec, a worm writeup.
2. **The Install Card** (GitHub + agent directories): copy-paste MCP config + installed badge. *"Ranking is a rental; installation is a residency."*
3. **Referee in the Pit, Live** (monthly): two models argue a real code question; the Honey Badger prosecutes; verdict + transcript publish.

**Converters** (one audience per month):
4. **Tech Receipt Audit** (firms; LinkedIn + PDF): one-page machine-readable tooling receipt. *"Your portfolio shows what you drew. A tech receipt proves what you built it with."*
5. **The Ghost Test** (firms; carousel + 60-sec recording): two permit sets side by side — invisibility demonstrated, not claimed.
6. **$1 Report Ledger** (developers; X + LinkedIn): public ledger of $1 reports on real PNW parcels, Deadlocks logged.
7. **The 2 a.m. Intake Story** (homeowners): "Intake at 2 a.m., escalated to a human at 2:02," told plainly, with copy-paste prompt cards.
8. **"What We Do Not Do" page** (all audiences; canonical + agent-readable schema): scope as the trust asset competitors cannot fake.

**Sequencing rule:** run feeders continuously; converters one audience per month. Feeder plays 1–3 have zero cost and compound machine citations. Do not let a feeder outrank canon in effort — feeders feed, canon holds the argument.

---

## 9. VISUAL STRATEGY

**Never request decorative AI stock imagery.** Visual suggestions and prompts must describe concrete, functional artifacts:
architectural floor plans · structural details · parametric models · data comparison tables · real screenshots · measured diagrams.

**Style prompt vocabulary (when a render is genuinely needed):**
> "Dark, sharp, terminal-inspired, clean, brutalist architectural rendering, technical blueprint detailing, precision spatial diagram."

**Rule:** if the image cannot carry information a reader would otherwise have to read, it does not ship.

---

## 10. MEASUREMENT

Track what zero-click actually rewards — not vanity sessions.

| Signal | Why it matters |
|---|---|
| **MCP / A2A tool calls** | The real conversion. A visiting agent that calls `ask_concierge` has converted. |
| Agent-card and `llms.txt` fetches | Discovery working. |
| Citation appearances in generated answers | The GEO equivalent of a ranking. |
| Canonical → syndication referral ratio | Confirms canon is holding, not leaking. |
| `book_consultation` structured invocations | The only lead that counts. Free text never writes to the pipeline — by design. |
| Error/refusal rate on the Concierge | ⚠ The known open defect: over-refusal on legitimate questions. Report it; do not paper over it. |

**Report failures in the same breath as wins.** That is the voice, and it is also the strategy: published failure is the trust asset competitors cannot fake.
