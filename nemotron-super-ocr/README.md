# Nemotron Super OCR — DSH 0.2.x agent preset

Turns difficult scans into **searchable PDFs with the text boxed** — not Markdown reports.

For every page the preset's bench script rasterises the page at 240 dpi, asks a local
vision model for each detected line as `{"text": ..., "box": [x1,y1,x2,y2]}`, and
rebuilds the page as:

* the page image (no reflow, nothing moved),
* an **invisible text layer** at those boxes, so Ctrl+F, copy and drag-select work,
* a thin **visible rectangle** around every detected line,
* a `*.manifest.json` recording boxes, characters, seconds and failures per page.

The agent's persona is written around what the model actually does well and badly on
bad scans, so it reports defects instead of papering over them.

---

## What ships

| File | Purpose |
| --- | --- |
| `cordis.patch.yml` | Bundle patch: one `@deepseek-ai/dsh-agent-preset` insert (generated from `agent.cordis.yml`) |
| `package.json` | Bundle manifest (`dsh.bundle.patch` → `./cordis.patch.yml`) |
| `agent.cordis.yml` | Agent-plane entry list (persona + tool rows) — the source of truth |
| `preset.yml` | Display name / description / order |
| `scripts/make_searchable_pdf.py` | The pipeline (PDF or image folder → searchable, boxed PDF + manifest) |
| `scripts/box_probe.py` | One-page sanity check of the model's JSON box format |
| `scripts/make_bundle_patch.py` | Regenerates `cordis.patch.yml` from `agent.cordis.yml` |

---

## Requirements

* **DSH 0.2.x** (the bundle format; rc.2 tested).
* Python 3.9+ with **PyMuPDF**: `py -m pip install pymupdf`.
* **Ollama** running locally at `127.0.0.1:11434` with a vision model — the preset
  defaults to `nemotron-3.5-super:120b` (`ollama pull nemotron-3.5-super:120b`).
* Optional, for the cloud comparison only: an **OpenRouter** API key.

Hardware note: `nemotron-3.5-super:120b` is a 123.6B MoE at Q4_K_M (~90 GB on disk).
It needs roughly **89 GB of VRAM** and therefore a 96 GB card to stay fully on the GPU;
a cold load takes ~37 s and only one model can be resident at a time. Any smaller
vision model works too — pass `--model`.

---

## Install

Copy or clone this directory into the DSH preset bundle root, then install the bundle
by absolute path (plugin manager):

```
plugin_manager install_bundle <presets-root>/nemotron-super-ocr
```

The entry rows are agent-plane only; the host composition keeps the model route,
sandbox and approval stack. Select the model in the composer — the preset does not own
the model route.

---

## Use

The agent runs this for you; the commands below are the underlying contract.

```powershell
# whole PDF, local model (default)
py scripts\make_searchable_pdf.py --pdf "C:\scans\letter.pdf" --out "letter.searchable.pdf"

# a page range, invisible layer only (no red boxes)
py scripts\make_searchable_pdf.py --pdf "C:\scans\letter.pdf" --out "letter.searchable.pdf" --pages 1-5 --no-boxes

# image folder instead of a PDF
py scripts\make_searchable_pdf.py --images "C:\scans\pages" --out "pages.searchable.pdf"

# alignment inspection: draw the placed text in blue over the words
py scripts\make_searchable_pdf.py --pdf "C:\scans\letter.pdf" --out "check.pdf" --pages 1 --text-visible

# one-page check that the model returns parseable boxes at all
py scripts\box_probe.py --pdf "C:\scans\letter.pdf" --page 1

# cloud comparison (same model, OpenRouter) — explicit opt-in only
py scripts\make_searchable_pdf.py --api openai --model nvidia/nemotron-3.5-super-vl `
    --pdf "C:\scans\letter.pdf" --out "letter.openrouter.searchable.pdf"
```

### Flags

| Flag | Default | Meaning |
| --- | --- | --- |
| `--pdf` / `--images` / `--out` | — | input PDF, or a folder of png/jpg/webp, and the output PDF |
| `--model` | `nemotron-3.5-super:120b` | any Ollama tag, or an OpenRouter id with `--api openai` |
| `--dpi` / `--max-side` | `240` / `2400` | render resolution; the long side is capped |
| `--pages` | all | `1-5` or `1,3` (1-based) |
| `--no-boxes` | off | invisible text layer only |
| `--text-visible` | off | draw the placed text in blue (inspection) |
| `--api` | `ollama` | `ollama` = local `/api/chat`, `openai` = OpenAI-compatible `/chat/completions` |
| `--base-url` | `https://openrouter.ai/api/v1` | for `--api openai` |
| `--api-key-env` | `OPENROUTER_API_KEY` | environment variable holding the key |
| `--credentials` | `~/.dsh/.credentials.yaml` | fallback secret store when the env var is unset |
| `--num-ctx` / `--num-predict` | `16384` / `8192` | local generation budget |
| `--max-tokens` | `8192` | output cap on the OpenAI-compatible path |

### Verify the result

```powershell
py -c "import pymupdf; d=pymupdf.open('letter.searchable.pdf'); print([(p.number+1, len(p.get_text())) for p in d])"
```

Every processed page must show a non-trivial text length. A page with 0 chars or 0 boxes
is a failed page — not a blank one.

---

## Measured behaviour (3-page reference scan, all pages rotated 90°)

A four-panel screenshot montage, a photo sheet of labelled cards, and a rotated report:

| run | boxed lines | chars | time | notes |
| --- | ---: | ---: | ---: | --- |
| local `nemotron-3.5-super:120b`, 240 dpi | 223 | 4170 | 373 s | line-level boxes; small upward drift in the densest list |
| OpenRouter `nvidia/nemotron-3.5-super-vl`, 240 dpi | 137 | 4198 | 25 s | **row-level** boxes on the dense page, and the granularity varies between identical calls |

What to expect:

* **240 dpi (long side 2400 px) is not optional.** At 1600 px, photo-sheet pages
  collapse to their captions and small digits get corrupted.
* **Photo sheets are the weak page** — 0–4 boxes with the generic prompt. Re-run that
  page with a card-directed prompt rather than lowering the bar for every page.
* **Truncation happens**: a line can come back as `Name : J DOE` when the page reads
  `Name : J DOE SMITH`. Geometry stays usable; the text does not. The preset reports it
  as a defect instead of presenting it as the reading.
* **Cloud granularity is coarser and less reproducible** than local; treat OpenRouter
  as the speed/comparison route, not the precision route.
* JSON-box mode costs **90–160 s per dense page** locally — run it as a background job.

---

## Privacy and keys

Local by default: pages never leave the machine unless the user explicitly asks for the
cloud comparison. The OpenRouter route uploads page images to a third party and spends
on the user's OpenRouter budget (~$0.002 per dense page at the time of writing).

The API key is read from the `OPENROUTER_API_KEY` environment variable, and failing that
from the DSH credential store (`~/.dsh/.credentials.yaml`), which is where the GUI's
**Settings → Models → OpenRouter → API key** field writes it. No key is stored in this
bundle.

## Sanitised for publication

This directory carries no credentials, no personal absolute paths and no document data:
paths are expressed as `%USERPROFILE%`, the credential store is resolved at runtime, and
the persona's examples use fictitious names and generic identifiers.
