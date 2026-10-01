# AXOWORKS.COM — SITE, MCP/A2A & GEO SURFACE MAP

> **Verified live 2026 (this deployment).** Every endpoint, header, and protocol fact below was fetched this session via Node `fetch` — not from memory.
> ⚠ **Transport note for this machine:** `Invoke-WebRequest` / schannel fails against `axoworks.com` ("The underlying connection was closed"). Use Node's fetch:
> `node -e "fetch('<url>').then(r=>r.text()).then(t=>console.log(t.slice(0,20000)))"`
> Never disable TLS verification. This is the documented schannel fallback, not a site problem.

---

## 1. WHAT THE SITE ACTUALLY IS

`axoworks.com` is **not a brochure site**. It is a single-page application whose primary interface is a live multi-model AI agent — **The Concierge** — which is simultaneously the storefront, the portfolio, the intake funnel, and the demonstration. The firm deleted its previous website on 2026-01-01 and replaced it with the agent. The marketing thesis is the site itself.

**Implication for every content decision:** the site is *evidence*, and pages on it are judged by whether they make the agent's claims checkable. A page that cannot be read by a machine or verified against a source is off-strategy.

---

## 2. THE MACHINE-READABLE SURFACE (exact, verified)

| Surface | Value |
|---|---|
| **MCP endpoint** | `https://axoworks.com/api/mcp` |
| MCP transport | Streamable HTTP, JSON-RPC 2.0 (POST / GET) |
| MCP protocol version | `2026-09-02` · schema version `v3` |
| MCP tools | `ask_concierge` (`query` required, `userLocation` optional) · `search_knowledge_base` (`query` required, `limit` 1–10) · `book_consultation` (`name`, `email`, `scope` — **structured invocation only**) |
| JSON-RPC alias | direct method call also accepted, e.g. `{"jsonrpc":"2.0","id":1,"method":"ask_concierge","params":{...}}` |
| stdio bridge | `scripts/mcp-bridge.mjs` (Claude Desktop, Cursor, local harnesses) |
| **A2A endpoint** | `https://axoworks.com/api/a2a` (JSON-RPC 2.0 over POST) |
| **Agent card** | `https://axoworks.com/.well-known/agent-card.json` (alias `agent.json`; schema `agent-card.schema.json`) |
| A2A protocol version | `0.1.0` · card version `3.0.0` · agent name `axoworks-concierge` |
| A2A methods | `message/send` (primary) · `tasks/get` · `tasks/cancel` · `tasks.create` (legacy dialect, accepted) · `skills.list` · `ping` |
| A2A capabilities | `streaming: false` · `push_notifications: false` · `stateful_tasks: true` |
| Task retention | `3600` seconds (1 hour); tasks are owner-bound to the calling client address |
| A2A policy fields | `leadWrite: structured-invocation-only` · `taskAccess: owner-bound to the calling client address` |
| Rate limit | **30 requests / minute per client address** |
| **Discovery** | `<link rel="mcp">`, `<link rel="a2a">`, `<meta name="ai-agent">`, `<meta name="mcp-server">`, `<meta name="a2a-server">`, JSON-LD `potentialAction`, `/.well-known/mcp.json`, `llms.txt`, `robots.txt`, `sitemap.xml` |

**Live probe result (this session):** a `tools/call` → `ask_concierge` POST returned HTTP 200 with a grounded, multi-section answer that correctly described the practice split, the white-label layer, engagement models, and the WA-only permitting limit. The endpoint works and the Concierge answers in the firm's voice.

---

## 3. `robots.txt` — THE DELIBERATE POSTURE

The file is **permissive on purpose**, and its comments are load-bearing policy:

- `User-agent: * / Allow: /` — open by default.
- Named citation/preview bots welcomed in the comment header: GPTBot, OAI-SearchBot, PerplexityBot, ClaudeBot, Claude-SearchBot, Slackbot, Discordbot, `facebookexternalhit`.
- Hostile agentic crawlers and on-demand fetch proxies are blocked **at the edge** (`netlify/edge-functions/block-ai-crawlers.ts`), **not** in `robots.txt`.
- ⚠ **Explicit maintenance warning in the file itself:** never add a per-bot group like `User-agent: GPTBot` with narrow `Allow` rules — a named group overrides the wildcard group and would accidentally disallow that bot from the rest of the site.

**Rule for any content or SEO change:** do not "tighten" `robots.txt`. Crawl policy for AI is enforced at the edge, deliberately. Editing `robots.txt` to block or narrow a bot is an architectural change requiring the principals, not a content task.

---

## 4. THE SITE IS NOW A HYBRID, AND THAT MATTERS

The `llms-full.txt` URL currently returns the **rendered SPA HTML** (title `AXOWORKS DESIGN RESEARCH | AI-Integrated Building Design Consultancy`, `og:title` = "The Power of One"), not a machine manifest — while `llms.txt` *is* a proper plain-text manifest. Treat `llms-full.txt` as unreliable for agents and verify before citing it.

**Two brand strings are live and in tension:**
- `og:title` → **"The Power of One"** (⚠ orphan canon — see the Positioning Brief Fix List; no article argues it)
- `meta description` → "Axoworks rethinking AI design research and technical execution for the built environment… proprietary AI workflows for high-precision building design and zoning feasibility."

The live `llms.txt` self-description is **"AI-augmented research, design, and pre-construction consultancy"** — which still omits the 50/50 shadow-fulfillment split that the canon article discloses. **This is the single highest-value copy fix available on the machine surface.**

---

## 5. GEO / AEO DOCTRINE (what actually moves citation)

Zero-click marketing is not "SEO with a new name." The retrieval target changed from a ranked link to **a citation inside a generated answer**. That changes what you optimize.

**Optimize for extraction, not dwell time.**
1. **Answer in the first sentence.** A generative engine lifts the direct answer; it does not summarize your buildup.
2. **Ship statistics, quotations, and citations.** The Princeton-led GEO research (KDD 2024) found these can lift visibility in generative answers by up to **40%**. The firm's own corpus cites statistics **+115.1%** and cite-sources **+77.0%**.
3. **Make every figure machine-checkable.** Named source, date, and number. "Studies show" is invisible to a retrieval scorer.
4. **Coined, defined terms get quoted.** Dictionary-form entries ("**AEC Proof of Work (n.)** — …") are the most liftable content shape that exists. This is why the canon coins terminology.
5. **Structured data must match the prose.** JSON-LD, FAQ schema, and article body that disagree create reconciliation drift that machines resolve *against* you. Date hygiene is part of this: set `dateModified` honestly and never refresh-date a piece to fake currency.
6. **Be present in the surfaces agents actually read:** `llms.txt`, agent card, MCP tool descriptions, and `robots.txt` comments. For Axoworks these are already first-class assets — treat them as **publishable copy**, reviewed like an article.
7. **The endpoint is the conversion.** In zero-click, the visitor is a machine that reads everything, clicks nothing, and remembers exactly what you published. The measurable goal is a **tool call**, not a session.

**What zero-click does NOT excuse.**
- It does not excuse thin content — an unverifiable page is uncitable.
- It does not excuse breaking `robots.txt` or the edge policy for a crawler.
- It does not replace canonical articles. Feeds compound citations; canon holds the argument.

---

## 6. THE PUBLISHING SURFACES

| Surface | Role | Notes |
|---|---|---|
| `axoworks.com/articles/<slug>` | **Canon.** BOFU, crawler-optimized, the version with structured data. | Every syndicated post points back here. |
| **Substack — `axotopia.substack.com`** | **Live syndication.** 11 posts, 2026-06-30 → 2026-09-16. | ⚠ Not `axoworks.substack.com` (404). List via `axotopia.substack.com/api/v1/archive?sort=new&limit=40`. Syndicated titles sometimes differ from canon — Part 2 runs as "The Front Door Is an Agentic Chat MCP — Not a Data Feed", and *from-portfolio-to-agent* is subtitled "How a 30-year…". Keep titles aligned or expect reconciliation drift. |
| Medium | Syndication + reach | Bylined from LinkedIn; author page is Cloudflare-walled (403) to automated fetch. |
| LinkedIn (`/in/axosphere`) | Primary human distribution; **feed-native voice** | **Hashtags (5–8) and functional emoji are house style here.** Canonical link goes in the **first comment**, stated as a dare or a reward — never "link in bio." See `AXOWORKS-LINKEDIN-VOICE.md`. |
| X (`@AxOtopia`) | Fast, dense, zero-click-native | Max density, minimum characters. |

**Standing rule:** the canonical link goes in a comment or a passive footnote. The post itself must deliver 100% of its value. A post that exists to drive a click has failed at zero-click.

**Formatting is platform-scoped.** Canonical articles carry **zero** emoji and **zero** hashtags. LinkedIn and X carry functional emoji and a hashtag cluster. Do not import one convention into the other.

---

## 7. HOW TO VERIFY ANY CLAIM BEFORE PUBLISHING

1. **Ask the Concierge.** `POST https://axoworks.com/api/mcp` with `ask_concierge`. It is grounded in the firm's own corpus and is the fastest way to confirm current service language, scope limits, and positioning. It is also a **test**: if the Concierge's answer contradicts your draft, the draft is wrong or the corpus is.
2. **Read `llms.txt`.** It is the current public manifest and the article index.
3. **Fetch the live page.** Never assert what a page says from memory.
4. **For code/security claims:** the four Zero-Click articles are the record, with numbers. Reuse the numbers exactly; do not round or restate them loosely.
