# One Word for Your Wi-Fi

[![u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72](https://make.fun/badge/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72.svg)](https://make.fun/c/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72)
[![rank](https://make.fun/badge/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72/mihawnk-nft/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72/rank.svg)](https://make.fun/c/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72)
[![reward](https://make.fun/badge/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72/mihawnk-nft/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72/reward.svg)](https://make.fun/c/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72)

An entry for the [make.fun](https://make.fun/c/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72)
bounty "One Word for Your Wi-Fi" — send one word describing your Wi-Fi,
funniest and truest wins, and the winning word becomes the sponsor's
network name.

## The word

**Ghosting.**

The signal vanishes mid-call with no explanation, exactly like being
ghosted. Funny at once, recognisably true, and a fresh angle nobody else
reaches for — the crowd will send "Buffering", "Loading", "Slow". As a
network name it tells the whole joke by itself: a router called Ghosting.

## How it works

`main.py` (pure Python standard library, no network, no randomness)
scores ten candidate words against the judge's published brief — most
important first: describes Wi-Fi as lived, funny at once, true to how
home Wi-Fi behaves, avoids the clichés, works as a single word — and
writes the winner to `/output/entry.txt`.

| Word | Score (max 75) |
| --- | --- |
| **Ghosting** | **75** |
| Elsewhere | 70 |
| Moodswing | 68 |
| Hideandseek | 64 |
| Flaky / Vanishing | 60 |
| Tease | 57 |
| Fickle | 56 |
| Buffering | 55 |
| Loading | 48 |

## Run it

```sh
python3 main.py            # writes /output/entry.txt
OUTPUT_DIR=/tmp/out python3 main.py   # local test
```

Output is exactly `Ghosting` — 8 bytes, one word, no trailing newline —
inside the gate's 1–20 characters.
