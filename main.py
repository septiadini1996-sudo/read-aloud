#!/usr/bin/env python3
"""One line that replaces a pointless meeting.

Writes a single sentence to /output/entry.txt: the line that, spoken aloud,
ends the meeting it replaces.
"""

import os

LINE = "Approved — the email's already sent, so this meeting is just that email, read aloud, slowly."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
