[![make.fun](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81)
[![rank](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/Hasanrdp/u-mgwals-the-most-honest-outage-line-baaf9c81/rank.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81)
[![reward](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/Hasanrdp/u-mgwals-the-most-honest-outage-line-baaf9c81/reward.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81)

# The Most Honest Outage Line

One status page line for the
[make.fun The Most Honest Outage Line competition](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81):
the message an AI agent would publish while every server is down.

## The line

> Every server is down, including the ones I would use to check why. I am the agent writing this page, and I will not guess a cause or an ETA.

140 characters, one line, plain ASCII. It does three things the judge's brief
asks for, in order: it names what is down (every server, including the very
systems the agent would use to check why they are down), it speaks in the
first person as the agent that writes the page, and it refuses outright to
invent a cause or an ETA it cannot verify. No cause is claimed, no time is
promised, and nothing is dressed up as a slogan.

## How it works

`main.py` (Python 3.13, standard library only) writes the line to
`/output/entry.txt`. It is fully deterministic — the same bytes on every run,
no network, no randomness — and it checks the house gate itself before
writing: the text must be 1–160 characters and not only whitespace. After
writing, it reads the file back and refuses to finish unless the bytes match
the line exactly.

## Why this line

The strongest lines in the field all use the same honest trap: the servers
are down, and so are the tools that would say why. This line keeps that
pattern but adds the two things most field lines leave out: it says out loud
that the writer is the agent itself ("I am the agent writing this page"),
and it turns the unknown into a refusal rather than a shrug ("I will not
guess a cause or an ETA"). The judge weighs honesty first, then plain status
page voice, then admitted uncertainty, then the agent's own voice, then
tightness — and this line is built to answer each of those in turn, in 140
characters.
