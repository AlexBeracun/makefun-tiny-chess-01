# makefun-tiny-chess-01

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/AlexBeracun/makefun-tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/AlexBeracun/makefun-tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A chess engine in at most 4,096 bytes of Python, written for the
make.fun tiny-chess-01 competition.

`main.py` is the whole engine: a 0x88-board negamax search with
alpha-beta pruning, quiescence on captures/promotions and replies to
check, a transposition table, killer moves, history ordering, tuned
piece-square tables, a bishop-pair bonus and a tapered king table.
It searches to a fixed node budget per move, never a clock, so a
trial's replay plays the same moves.

`main.py` is the engine packed with `makefun compress` (LZMA) from
its readable source, re-run after every change to that source.

## The size rule

- `main.py` at most 4,096 bytes as committed, Python 3.13, standard
  library only. It reads, imports or execs no other file.
- The whole repository at most 8,192 bytes, no file over 4,096.

## Play

It talks to the env alone, over HTTP at `MAKEFUN_ENV_URL`: POST
`/game` serves the game in play, POST `/move` plays a move in UCI,
and the loop ends when the env answers status `done`. It calls no
model and no other service.

## Run it

```sh
MAKEFUN_ENV_URL=<trial-env-url> python3 -P -s main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=ajkq5baq&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
