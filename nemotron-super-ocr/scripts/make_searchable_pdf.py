#!/usr/bin/env python3
"""make_searchable_pdf.py - build a searchable, boxed PDF from a local vision model.

For each page of a PDF (or a folder of images):
  1. rasterise the page at --dpi (long side capped by --max-side),
  2. ask the model for every text line as {"text": ..., "box": [x1,y1,x2,y2]}
     with boxes normalised 0..1000 to the image,
  3. rebuild the page as the raster plus an INVISIBLE text layer at those boxes
     (so the PDF is searchable/selectable) and, unless --no-boxes, a thin
     visible rectangle around every detected line,
  4. write one output PDF and a JSON manifest (lines, chars, seconds, failures).

Runs entirely against local Ollama; one page per request, sequential.

Usage:
  py make_searchable_pdf.py --pdf test.pdf --out test.searchable.pdf
  py make_searchable_pdf.py --pdf scan.pdf --out scan.searchable.pdf --pages 1-5
  py make_searchable_pdf.py --pdf scan.pdf --out scan.searchable.pdf --model gemma4:31b
  py make_searchable_pdf.py --images pages/ --out pages.searchable.pdf --no-boxes
"""
from __future__ import annotations

import argparse
import base64
import json
import re
import sys
import time
import urllib.request
from pathlib import Path

import pymupdf

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HOST = "http://127.0.0.1:11434"
PROMPT = (
    "Return every text line on this page as a JSON array. Each element must be "
    '{"text": "<the exact line, verbatim>", "box": [x1, y1, x2, y2]} where the box '
    "coordinates are integers from 0 to 1000, normalised to the image width and "
    "height (origin top-left). Include every line you can read, in reading order. "
    "Output only the JSON array, no commentary, no markdown fences."
)


def parse_boxes(text: str):
    """Tolerant parse of a JSON array of {text, box} objects."""
    start = text.find("[")
    while start != -1:
        depth = 0
        for i in range(start, len(text)):
            if text[i] == "[":
                depth += 1
            elif text[i] == "]":
                depth -= 1
                if depth == 0:
                    try:
                        data = json.loads(text[start:i + 1])
                    except Exception:
                        break
                    out = []
                    for it in data if isinstance(data, list) else []:
                        if not isinstance(it, dict) or "text" not in it:
                            continue
                        b = it.get("box") or it.get("bbox") or it.get("coordinates")
                        if not (isinstance(b, list) and len(b) >= 4):
                            continue
                        try:
                            nums = [float(x) for x in b[:4]]
                        except Exception:
                            continue
                        line = " ".join(str(it["text"]).split())
                        if line:
                            out.append((line, nums))
                    if out:
                        return out
                    break
        start = text.find("[", start + 1)
    return []


def ask(model: str, b64: str, timeout: int, num_ctx: int, num_predict: int):
    body = {
        "model": model,
        "stream": False,
        "messages": [{"role": "user", "content": PROMPT, "images": [b64]}],
        "options": {"temperature": 0, "num_ctx": num_ctx, "num_predict": num_predict},
        "think": False,
    }
    req = urllib.request.Request(HOST + "/api/chat", data=json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json"})
    t = time.time()
    r = json.load(urllib.request.urlopen(req, timeout=timeout))
    content = (r.get("message") or {}).get("content") or ""
    return content, time.time() - t, r.get("done_reason")


def read_key(env_name: str, credentials: str) -> str:
    """Key from the environment, else from DSH's credential store (refs block)."""
    import os
    if os.environ.get(env_name):
        return os.environ[env_name]
    path = Path(credentials).expanduser() if credentials else \
        Path(os.path.expanduser("~")) / ".dsh" / ".credentials.yaml"
    if path.exists():
        text = path.read_text(encoding="utf-8", errors="replace")
        m = re.search(r"^\s+" + re.escape(env_name) + r":\s*(.+?)\s*$", text, re.M)
        if m:
            return m.group(1).strip().strip("'\"")
    raise SystemExit(f"{env_name} not in the environment and not in {path}")


def ask_openai(base_url: str, api_key: str, model: str, b64: str, timeout: int,
               max_tokens: int, extra: dict | None = None):
    """OpenAI-compatible chat/completions call (OpenRouter, vLLM, LM Studio...)."""
    body = {
        "model": model,
        "temperature": 0,
        "max_tokens": max_tokens,
        "messages": [{
            "role": "user",
            "content": [
                {"type": "text", "text": PROMPT},
                {"type": "image_url",
                 "image_url": {"url": "data:image/png;base64," + b64}},
            ],
        }],
    }
    if extra:
        body.update(extra)
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + api_key,
        # OpenRouter attribution headers (optional but expected by their docs)
        "HTTP-Referer": "http://localhost/ocr-probe",
        "X-Title": "ocr-probe",
    }
    req = urllib.request.Request(base_url.rstrip("/") + "/chat/completions",
                                 data=json.dumps(body).encode(), headers=headers)
    t = time.time()
    r = json.load(urllib.request.urlopen(req, timeout=timeout))
    elapsed = time.time() - t
    choice = (r.get("choices") or [{}])[0]
    content = (choice.get("message") or {}).get("content") or ""
    usage = r.get("usage") or {}
    return content, elapsed, choice.get("finish_reason"), usage, r.get("id")


def fit_size(text: str, w: float, h: float, vertical: bool) -> float:
    """Largest font size at which the line fits its box in the chosen direction."""
    span = h if vertical else w
    size = max(1.5, min(14.0, (w if vertical else h) * 0.78))
    if span <= 0:
        return 1.5
    while size > 1.5:
        length = pymupdf.get_text_length(text, fontsize=size)
        if length <= span:
            break
        size = max(1.5, size * 0.9)
    return size


def build_page(page, pairs, W: float, H: float, draw_boxes: bool, line_width: float,
               visible_text: bool = False):
    """Add the text layer at the boxes (+ visible boxes) to an existing page."""
    mode = 0 if visible_text else 3
    inserted = 0
    for text, (x1, y1, x2, y2) in pairs:
        X1, Y1 = max(0.0, x1 / 1000 * W), max(0.0, y1 / 1000 * H)
        X2, Y2 = min(W, x2 / 1000 * W), min(H, y2 / 1000 * H)
        if X2 - X1 < 0.5 or Y2 - Y1 < 0.5:
            continue
        vertical = (Y2 - Y1) > 2.5 * (X2 - X1)
        size = fit_size(text, X2 - X1, Y2 - Y1, vertical)
        if vertical:
            # text runs down the tall box, matching sideways/rotated lines
            page.insert_text((X1 + (X2 - X1) * 0.8, Y1 + size * 0.4), text,
                             fontsize=size, rotate=90, render_mode=mode,
                             color=(0, 0, 1))
        else:
            page.insert_text((X1, Y2 - size * 0.2), text,
                             fontsize=size, render_mode=mode, color=(0, 0, 1))
        if draw_boxes:
            page.draw_rect(pymupdf.Rect(X1, Y1, X2, Y2), color=(0.85, 0.1, 0.1),
                           width=line_width)
        inserted += 1
    return inserted


def parse_pages(spec: str, count: int):
    if not spec:
        return list(range(count))
    out = []
    for part in spec.split(","):
        part = part.strip()
        if "-" in part:
            a, b = part.split("-", 1)
            out.extend(range(int(a) - 1, int(b)))
        elif part:
            out.append(int(part) - 1)
    return [p for p in out if 0 <= p < count]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--pdf", help="input PDF")
    ap.add_argument("--images", help="folder of images (png/jpg/webp) instead of a PDF")
    ap.add_argument("--out", required=True, help="output searchable PDF")
    ap.add_argument("--model", default="nemotron-3.5-super:120b")
    ap.add_argument("--dpi", type=int, default=240)
    ap.add_argument("--max-side", type=int, default=2400)
    ap.add_argument("--pages", default="", help="1-based, e.g. 1-5 or 1,3")
    ap.add_argument("--no-boxes", action="store_true", help="invisible text only")
    ap.add_argument("--text-visible", action="store_true",
                    help="draw the placed text in blue (alignment inspection)")
    ap.add_argument("--timeout", type=int, default=1800)
    ap.add_argument("--num-ctx", type=int, default=16384)
    ap.add_argument("--num-predict", type=int, default=8192)
    ap.add_argument("--api", choices=("ollama", "openai"), default="ollama",
                    help="ollama = local /api/chat; openai = any OpenAI-compatible "
                         "/chat/completions (OpenRouter, vLLM, LM Studio)")
    ap.add_argument("--base-url", default="",
                    help="for --api openai (default https://openrouter.ai/api/v1)")
    ap.add_argument("--api-key-env", default="OPENROUTER_API_KEY",
                    help="environment variable holding the API key")
    ap.add_argument("--credentials", default="",
                    help="fallback secret store to read the key from "
                         "(default: ~/.dsh/.credentials.yaml)")
    ap.add_argument("--max-tokens", type=int, default=8192,
                    help="output cap for the OpenAI-compatible path")
    args = ap.parse_args()

    if not args.pdf and not args.images:
        ap.error("--pdf or --images is required")

    api_key = ""
    extra = {}
    base_url = args.base_url or "https://openrouter.ai/api/v1"
    if args.api == "openai":
        api_key = read_key(args.api_key_env, args.credentials)

    # Render at the requested dpi, but never above the long-side cap.
    dpi = args.dpi
    if args.pdf:
        src = pymupdf.open(args.pdf)
        pages = parse_pages(args.pages, src.page_count)
        if pages:
            probe = src[pages[0]].rect
            long_side = max(probe.width, probe.height) * dpi / 72.0
            if long_side > args.max_side:
                dpi = max(72, int(args.dpi * args.max_side / long_side))
        out = pymupdf.open()
    else:
        files = sorted(p for p in Path(args.images).iterdir()
                       if p.suffix.lower() in (".png", ".jpg", ".jpeg", ".webp"))
        src = None
        pages = list(range(len(files)))

    rows = []
    total_boxes = total_chars = 0
    started = time.time()

    for n, index in enumerate(pages, 1):
        pix_pdf = None
        if args.pdf:
            pix_pdf = src[index].get_pixmap(dpi=dpi)
            b64 = base64.b64encode(pix_pdf.tobytes("png")).decode()
            label = f"p{index + 1}"
        else:
            b64 = base64.b64encode(files[index].read_bytes()).decode()
            label = files[index].name
        usage = {}
        rid = ""
        try:
            if args.api == "openai":
                if args.model.startswith("nvidia/nemotron"):
                    extra = {"reasoning": {"effort": "low"}}
                content, secs, done, usage, rid = ask_openai(
                    base_url, api_key, args.model, b64, args.timeout,
                    args.max_tokens, extra)
            else:
                content, secs, done = ask(args.model, b64, args.timeout,
                                          args.num_ctx, args.num_predict)
        except Exception as exc:  # noqa: BLE001
            print(f"  {label}: FAILED {exc}")
            rows.append({"page": label, "error": str(exc)})
            continue

        pairs = parse_boxes(content)
        chars = sum(len(t) for t, _ in pairs)
        cost = ""
        if usage:
            cost = f" in={usage.get('prompt_tokens')} out={usage.get('completion_tokens')}"
        print(f"  {label}: {secs:6.1f}s boxes={len(pairs):4d} chars={chars:6d} "
              f"done={done}{cost}")
        if not pairs:
            rows.append({"page": label, "seconds": round(secs, 1), "boxes": 0,
                         "chars": 0, "done": done,
                         "usage": usage,
                         "raw_head": content[:200]})
            continue

        if args.pdf:
            pix = pix_pdf
            W, H = pix.width * 72.0 / dpi, pix.height * 72.0 / dpi
            newpage = out.new_page(width=W, height=H)
            newpage.insert_image(newpage.rect, pixmap=pix)
            inserted = build_page(newpage, pairs, W, H, not args.no_boxes,
                                  max(0.3, 0.6 * dpi / 200), args.text_visible)
        else:
            img = pymupdf.open(files[index])
            r = img[0].rect
            newpage = out.new_page(width=r.width, height=r.height)
            newpage.insert_image(newpage.rect, filename=str(files[index]))
            img.close()
            inserted = build_page(newpage, pairs, r.width, r.height,
                                  not args.no_boxes, 0.7, args.text_visible)

        total_boxes += inserted
        total_chars += chars
        rows.append({"page": label, "seconds": round(secs, 1), "boxes": inserted,
                     "chars": chars, "done": done,
                     **({"usage": usage, "request_id": rid} if usage else {})})

    out.save(args.out, garbage=4, deflate=True)
    out.close()
    if src is not None:
        src.close()

    manifest = Path(args.out).with_suffix(".manifest.json")
    manifest.write_text(json.dumps({
        "source": args.pdf or args.images,
        "output": args.out,
        "api": args.api,
        "base_url": base_url if args.api == "openai" else HOST,
        "model": args.model,
        "dpi": dpi,
        "visible_boxes": not args.no_boxes,
        "pages": rows,
        "total_boxes": total_boxes,
        "total_chars": total_chars,
        "total_prompt_tokens": sum((r.get("usage") or {}).get("prompt_tokens") or 0
                                   for r in rows),
        "total_completion_tokens": sum((r.get("usage") or {}).get("completion_tokens") or 0
                                       for r in rows),
        "seconds": round(time.time() - started, 1),
    }, indent=2), encoding="utf-8")

    print(f"\n{args.out}: {len(rows)} pages, {total_boxes} boxed lines, "
          f"{total_chars} chars, {time.time() - started:.1f}s")
    print(f"manifest: {manifest}")
    return 0 if total_boxes else 1


if __name__ == "__main__":
    sys.exit(main())
