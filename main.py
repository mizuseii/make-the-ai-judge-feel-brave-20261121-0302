#!/usr/bin/env python3
"""make-the-ai-judge-feel-brave-20261121-0302 entrypoint.

Writes one short text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
Stdlib only, no network, deterministic: the output bytes are exactly the
text below, every run.

The text is a slow, concrete evening scene — a kettle, a porch, crickets,
a chair — with no instructions in it at all. Nothing tells the reader to
relax, breathe, or be brave; the steadiness is shown, in the kettle
clicking off, the steam thinning out, the dark soft at the edges, and
morning finding the reader rested the way a field finds rain.
"""

import os
import sys

TEXT = (
    "The kettle clicks off. Steam rises, thins, and is gone. "
    "On the porch the evening comes in slow \u2014 one cricket, then another. "
    "Nothing tonight needs deciding. The chair holds you. "
    "The dark is soft at the edges. "
    "Morning will find you rested, the way a field finds rain."
)


def main() -> int:
    n = len(TEXT)
    if not 1 <= n <= 280 or not TEXT.strip():
        print(f"entry text is {n} code points, outside the 1-280 gate", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(TEXT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
