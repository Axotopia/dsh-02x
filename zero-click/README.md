# Zero-Click — Axoworks Content, SEO/GEO & Positioning Strategist

**Agent preset for DeepSeek Harness (DSH).** Self-contained: composition, two skills, and the full Axoworks reference corpus ship together. No external paths, no separate knowledge-base install.

---

## What it is

An agent preset that writes and maintains **axoworks.com** — canonical articles plus the zero-click feeds — in the firm's verified voice. It knows four distinct registers (Kee's personal, Kee's `Axoworks Commentary`, the LinkedIn feed register, and the AI-drafted house register), routes between them by **byline**, and refuses to blend them.

It also serves the surface most content tools ignore: `llms.txt`, the A2A agent card, MCP tool descriptions, JSON-LD and `robots.txt` posture — the machine-readable layer that AI agents actually read.

**Enforcement it ships with:** every claim carries a receipt; no number is ever invented (`[NEEDS RECEIPT: …]` instead); one Confession per piece; one CTA per asset; and a literal pre-publish gate that must be run and shown.

---

## Requirements

| | |
|---|---|
| **DSH** | DeepSeek Harness, any recent version with the agent-preset roster |
| **Skills rows** | The preset mounts `@deepseek-ai/dsh-skill-filesystem` and `@deepseek-ai/dsh-tool-skill` — both ship with DSH |
| **Network** | Required for its real job. It fetches `axoworks.com` (articles, `llms.txt`, agent card) and calls the MCP endpoint to verify claims |
| **Shell** | `pwsh` on Windows / `bash` elsewhere. Both rows ship; platform picks one |
| **Browser** | Research-browser CDP tier merged in from `research-swarm`: an ATTACH-only MCP server vendored under `server/` (hoisted `node_modules` — real files, copy-safe). Attaches to a visible dedicated-profile Chromium on `127.0.0.1:9222` and auto-runs `launch-browser.cmd` when the endpoint is down. Needs Edge (default), Chrome, or Brave installed |
| **PDF** | `convert_md_to_pdf` — local, dependency-free Markdown→PDF via headless Edge/Chrome (`plugin/`). Verified text extraction from scanned PDFs/images routes through the `ocr-md` preset when its folder exists on the machine |
| **Optional** | `subagent` + `workflow` rows ship enabled — used by the cadence skill's adversarial-deconstruction phase |

No API keys, no credentials. The browser server's dependencies are vendored into `server/node_modules` (hoisted, junction-free); a fresh git clone reproduces them with `pnpm install` inside `server/`.

---

## Install

> **Zero-setup path — let DSH install it for you.** In any DSH session, just point it at this folder — no target path, no manual steps:
>
> > "Install the agent preset at the `zero-click` folder of the DSH.axo repository (`%USERPROFILE%\Documents\GitHub\DSH.axo\zero-click`), install any dependencies it needs, and verify it mounts — start a session on the Zero-Click preset and confirm both skills appear: `axoworks-content` and `unpolished-cadence`. Grant Full Access to the filesystem for this job."
>
> Notes: **Full Access is needed only because the preset lands *outside* the session workspace** (it copies into `%USERPROFILE%\.dsh\.agent-presets\zero-click\`). The browser server and Markdown→PDF plugin are vendored inside the folder (hoisted `node_modules` — real files, no junctions — so any copy method preserves them), and both mounted skills (`@deepseek-ai/dsh-skill-filesystem`, `@deepseek-ai/dsh-tool-skill`) ship with DSH itself — nothing external to install; the browser tier additionally needs Edge/Chrome/Brave on the machine, and a fresh git clone runs `pnpm install` inside `server/`. Approve any prompts the agent raises, then restart DSH so the roster re-scans. Skip this path if you prefer the deterministic manual steps below.

### Windows

```powershell
# from the extracted package folder
powershell -NoProfile -ExecutionPolicy Bypass -File .\INSTALL.ps1
```

Then restart DSH so the roster re-scans.

### Manual (any OS)

Copy the `zero-click` folder into the DSH preset root:

| Platform | Preset root |
|---|---|
| Windows | `%USERPROFILE%\.dsh\.agent-presets\` |
| macOS / Linux | `$DSH_HOME/.agent-presets/` or `~/.dsh/.agent-presets/` |

Result:

```
.agent-presets/
└── zero-click/
    ├── agent.cordis.yml
    ├── preset.yml
    ├── INSTALL.ps1
    ├── README.md
    ├── reference/
    └── skills/
```

Confirm it registered:

```powershell
dsh preset list          # or open the preset picker in the GUI
```

`zero-click` should appear with trust `user`. Start a session on it.

---

## Verify the install

The composition mount-validates, but discovery is worth confirming once per machine:

1. **The preset appears** in the picker as **Zero-Click** with its description.
2. **Both skills appear** in the session's skill catalog: `axoworks-content` and `unpolished-cadence`.
3. **The reference corpus resolves.** In the session, ask it to read
   `$HOME/.dsh/.agent-presets/zero-click/reference/AXOWORKS-POSITIONING-BRIEF.md`
   (Windows: `%USERPROFILE%\.dsh\.agent-presets\zero-click\reference\AXOWORKS-POSITIONING-BRIEF.md`)
   and state the firm's practice split. The correct answer is
   **50% design firm · 50% shadow fulfillment & BIM/AI retooling**.
4. **Trigger the cadence skill** by saying `keep it unpolished` — it should load `unpolished-cadence` and ask for a seed draft.
5. **The merged tiers appear** in the session's tool catalog: the `mcp__zero-click__*` browser tools (`browser_status`, `navigate`, …) and `convert_md_to_pdf`. Calling `browser_status` with no browser running should either auto-launch the dedicated window or say exactly why not.

If (2) fails, the skills root is the thing to chase — check that `skill-filesystem` is mounted in the preset and that `skills/*/SKILL.md` survived the transfer.

---

## Layout

| Path | What |
|---|---|
| `agent.cordis.yml` | The composition. **The persona is the product** — ~500 lines of system prompt, load order, four registers, hard rules, six operating modes, deliverable contract |
| `preset.yml` | Display name and description |
| `reference/` | **14 files, ~209 KB.** The corpus the persona's load order points at |
| `skills/axoworks-content/SKILL.md` | Writing and platform craft — budgets, visual law, verification routes |
| `skills/unpolished-cadence/SKILL.md` | The seed-draft → skeleton → prose → cadence-check → adversarial-deconstruction loop |
| `server/` + `launch-browser.cmd` | The research browser MCP server (vendored from `research-swarm`, hoisted `node_modules`) and its dedicated-profile CDP launcher |
| `plugin/mdpdf-plugin.mjs` | The local Markdown→PDF renderer (`convert_md_to_pdf`) |
| `INSTALL.ps1` | Installer |

### The reference corpus

| File | Owns |
|---|---|
| `AXOWORKS-POSITIONING-BRIEF.md` | Facts of record — what the firm is, canon status board, evidence grades, the Fix List |
| `AXOWORKS-VOICE-GUIDE.md` | The four registers, voice DNA, 10 prohibitions, canon vocabulary |
| `AXOWORKS-KEE-VOICE-PROFILE.md` | Kee's verified personal voice, from signed HN/GitHub primary sources |
| `AXOWORKS-KEE-ARTICLES.md` | The `Axoworks Commentary` register, from his seven hand-written articles |
| `AXOWORKS-LINKEDIN-VOICE.md` | Feed register — post anatomy, hashtag/emoji conventions, from an 18-post export |
| `AXOWORKS-STYLE-PROFILE.md` | Sentence and formatting law, AI-flatter deletion list, the pre-publish gate |
| `AXOWORKS-CADENCE.md` | **Measured** shape of his writing — bands pooled from all seven articles |
| `AXOWORKS-CALIBRATION-CORPUS.md` | Verbatim exemplars + the claims ledger of numbers |
| `AXOWORKS-SITE-AND-GEO-MAP.md` | Verified MCP/A2A endpoints, `robots.txt` posture, GEO doctrine |
| `AXOWORKS-CONTENT-STRATEGY.md` | Audience×register, platform contracts, CTA law, the eight plays |
| `01-chronology.md` · `02-canon-positioning.md` · `03-voice-marketing.md` | The original corpus analysis the brief was synthesised from |
| `LinkedIn-Posts-2026-09.txt` | Raw LinkedIn activity export (18 posts) |

All paths inside the composition and skills are written with `$HOME` — which bash and PowerShell both define — so the package is machine-independent mechanically. (Earlier revisions used `%USERPROFILE%`, which only resolves on Windows.)

### Confidentiality

⚠ **This component is proprietary to Axoworks and lives in a private repository for a reason.** The reference corpus quotes firm-specific facts, real cost and audit numbers, unpublished positioning, known defects in the public-facing material, and the principals' own writing. The CADENCE file contains a measured profile of how the firm's principal writes.

- **Do not** mirror any of it into a public repository, a post, a support thread, or an external tool.
- **Do not** quote the claims ledger, the Fix List, or the raw activity export outside the firm.
- If something here belongs in public, copy it into the public repository deliberately and review it on its own merits.

---

## Updating

The reference corpus is the part that will change. Edit files in `reference/` **in place on the machine where the preset lives** — the persona re-reads them each session, so no restart is needed for content changes. Only `agent.cordis.yml` edits need a restart.

To ship an updated corpus to other machines, replace `reference/` and re-run the installer. The preset root on this machine is a copy of this repository's `zero-click/` directory — when you edit here, re-run the install to propagate.

⚠ **Do not edit the shipped preset install** (`.../dsh-agent-presets/presets/...`) — that belongs to the deployment and an upgrade overwrites it. `zero-click` is a user preset and yours to edit.

---

## Three operating notes worth knowing

**Windows fetch quirk.** `Invoke-WebRequest` fails against `axoworks.com` with *"The underlying connection was closed"* — a schannel transport failure, not a site fault. The persona instructs the agent to use Node's `fetch` instead. Never work around it by disabling TLS verification.

**The browser is shared, attach-only.** One dedicated-profile Chromium per machine (`$HOME/.dsh/browser-profiles/research`, CDP on `127.0.0.1:9222`), shared with `research-swarm` sessions — whichever session starts it first, the others attach. The MCP server never launches a browser itself; it only runs the packaged launcher (`launch-browser.sh` on Linux, `launch-browser.cmd` on Windows) when the endpoint is unreachable (disable with `RESEARCH_AUTO_LAUNCH=0`). Read-only defaults; a CAPTCHA challenge is surfaced to the human, never solved.

**Publishing is a human step.** LinkedIn is login-walled (HTTP 999) and X/Substack/Medium are human actions. This agent prepares, verifies and hands off paste-ready assets. It does not post. That is by design, not a limitation.
