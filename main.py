#!/usr/bin/env python3
"""Fix Human Sleep: Funniest Patch Note.

Writes a single patch-note line announcing that human sleep is fixed
to /output/entry.txt. Deterministic: the same line on every run.

Concept: the brain as a browser that opens 47 tabs at bedtime --
a concrete, specific scene in genuine changelog voice. The fix is
specific and unexpected (tabs auto-closing at lights-out), not a flat
claim that sleep now works.
"""

import os

ENTRY = (
    "Fixed a bug where the brain opened 47 tabs at bedtime; "
    "tabs now auto-close at lights-out, no restart required."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
