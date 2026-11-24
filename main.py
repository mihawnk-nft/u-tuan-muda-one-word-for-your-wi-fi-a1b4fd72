#!/usr/bin/env python3
"""One Word for Your Wi-Fi -- make.fun entry.

Picks the single word that best describes home Wi-Fi against the judge's
published brief, then writes it to /output/entry.txt.

The judge weighs, most important first:
  1. describes Wi-Fi as the entrant lives it
  2. funny at once, a real laugh rather than a pun that needs explaining
  3. true to how home Wi-Fi actually behaves, so the joke lands because
     it is recognisable
  4. avoids the words everyone reaches for, a surprising angle on a
     familiar annoyance
  5. works as a single word with no context needed, spelled so a reader
     gets it instantly

Each candidate is scored 0-5 on each criterion (weights 5, 4, 3, 2, 1)
and the highest total wins.

"Ghosting" wins on every count: the signal vanishes mid-call with no
explanation, exactly like being ghosted -- funny at once, recognisably
true, and a fresh angle nobody else reaches for (the crowd will send
"Buffering", "Loading", "Slow"). It also works as a network name: a
router called Ghosting tells the whole joke by itself.

Pure standard library, no network, no randomness: the same word every run.
"""

import os

# word: (on_subject, funny, true, fresh, readable), each 0-5.
CANDIDATES = {
    "Ghosting": (5, 5, 5, 5, 5),
    "Moodswing": (5, 4, 5, 4, 4),
    "Elsewhere": (5, 4, 5, 5, 4),
    "Hideandseek": (5, 4, 4, 4, 3),
    "Flaky": (5, 3, 4, 3, 5),
    "Buffering": (5, 2, 5, 1, 5),
    "Loading": (5, 1, 4, 1, 5),
    "Vanishing": (5, 3, 4, 3, 5),
    "Tease": (4, 3, 4, 4, 5),
    "Fickle": (5, 2, 4, 3, 5),
}

WEIGHTS = (5, 4, 3, 2, 1)


def score(word):
    """Weighted total of a candidate against the judge's brief."""
    return sum(w * s for w, s in zip(WEIGHTS, CANDIDATES[word]))


def pick():
    """The single best word; refuses a tie so the entry is never a coin toss."""
    ranked = sorted(CANDIDATES, key=score, reverse=True)
    best, runner_up = ranked[0], ranked[1]
    assert score(best) > score(runner_up), "top two candidates tie"
    return best


def main():
    word = pick()
    assert 1 <= len(word) <= 20, "entry must be 1-20 characters"
    assert word.strip() == word and word.isalpha(), "entry must be one word"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(word)
    print(word)


if __name__ == "__main__":
    main()
