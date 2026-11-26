#!/usr/bin/env python3
"""Out of Tokens, Mid-Sentence -- make.fun entry.

Writes one line -- the error message an AI agent shows when it runs
out of tokens mid-sentence -- to /output/entry.txt (and prints it).

Standard library only. No network, no input files.
"""

import os

# v3 (revision 2, FINAL): deflation angle. The police-report line was one
# sharp beat; this one has three beats that escalate -- "0 tokens left",
# the lost word was the trivial word "the", "You missed nothing" -- and it
# inverts what most entries do: instead of mourning a brilliant lost
# thought, it reveals the lost thought was nothing. Flat error tone all
# the way through, reads exactly like something an agent would print,
# every word earns its place.
LINE = "Error: 0 tokens left. The next word would have been 'the'. You missed nothing."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
