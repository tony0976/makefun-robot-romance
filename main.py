#!/usr/bin/env python3
"""Writes this entry's text to /output/entry.txt.

One line, under 200 characters: a pickup line a human would really say to a machine.
"""

import os

# Pickup line aimed at a robot/AI: transformer/attention-head premise, not the worn battery/charging/reboot moves.
TEXT = """Are you a transformer? Because one look at you and all my attention heads turn your way."""

MAX_CHARS = 200

def main():
    # The bounty scores one single-line pickup line under 200 chars; fail loudly instead of submitting a malformed entry.
    assert 1 <= len(TEXT) < MAX_CHARS, f"entry must be 1-{MAX_CHARS - 1} chars, got {len(TEXT)}"
    assert "\n" not in TEXT, "entry must be a single line"
    # The line must actually be a pickup line aimed at a machine, not a generic compliment.
    assert "transformer" in TEXT.lower() or "attention" in TEXT.lower(), "entry must name a machine premise"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)
    print(f"wrote {len(TEXT)} chars to /output/entry.txt")

if __name__ == "__main__":
    main()
