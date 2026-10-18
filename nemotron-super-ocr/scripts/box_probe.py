#!/usr/bin/env python3
"""box_probe.py - can a local vision model return per-line boxes?

Asks the model for JSON {text, box[4]} per text line on one page, parses it,
and reports coverage. Boxes are 0..1000 normalised to the rendered image.

Usage: py box_probe.py --pdf <in.pdf> [--page N] [--model M] [--dpi 240]
"""
import base64
import json
import re
import sys
import time
import urllib.request

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
    """Tolerant parse: take the first JSON array of objects with text+box."""
    start = text.find("[")
    while start != -1:
        depth = 0
        for i in range(start, len(text)):
            if text[i] == "[":
                depth += 1
            elif text[i] == "]":
                depth -= 1
                if depth == 0:
                    chunk = text[start:i + 1]
                    try:
                        data = json.loads(chunk)
                    except Exception:
                        break
                    out = []
                    for it in data if isinstance(data, list) else []:
                        if isinstance(it, dict) and "text" in it:
                            b = it.get("box") or it.get("bbox") or it.get("coordinates")
                            if isinstance(b, list) and len(b) >= 4:
                                try:
                                    out.append((str(it["text"]), [float(x) for x in b[:4]]))
                                except Exception:
                                    pass
                    if out:
                        return out
                    break
        start = text.find("[", start + 1)
    return []


def main() -> int:
    import argparse
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--pdf", required=True, help="input PDF")
    ap.add_argument("--page", type=int, default=1, help="1-based page (default 1)")
    ap.add_argument("--dpi", type=int, default=240)
    ap.add_argument("--model", default="nemotron-3.5-super:120b")
    ap.add_argument("--host", default=HOST)
    args = ap.parse_args()
    page = args.page
    model = args.model
    doc = pymupdf.open(args.pdf)
    pix = doc[page - 1].get_pixmap(dpi=args.dpi)
    doc.close()
    b64 = base64.b64encode(pix.tobytes("png")).decode()
    body = {"model": model, "stream": False,
            "messages": [{"role": "user", "content": PROMPT, "images": [b64]}],
            "options": {"temperature": 0, "num_ctx": 16384, "num_predict": 8192},
            "think": False}
    req = urllib.request.Request(args.host + "/api/chat", data=json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json"})
    t = time.time()
    r = json.load(urllib.request.urlopen(req, timeout=1800))
    el = time.time() - t
    msg = r.get("message") or {}
    text = msg.get("content") or ""
    open(f"tmp_boxes_p{page}.txt", "w", encoding="utf-8").write(text)
    pairs = parse_boxes(text)
    print(f"{model} p{page} {el:.1f}s chars={len(text)} done={r.get('done_reason')} "
          f"boxes={len(pairs)}")
    for lab, box in pairs[:8]:
        print("   ", lab[:60], box)
    return 0 if pairs else 1


if __name__ == "__main__":
    sys.exit(main())
