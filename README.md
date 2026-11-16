# Tiny Chess — a 4 KB sunfish-style chess engine in a single Python file

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/daring-stork-60/tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/daring-stork-60/tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01)

A chess engine in **4,086 bytes of Python** (`main.py`), built for the
[make.fun](https://make.fun/bounty/tiny-chess-01) tiny-chess-01 bounty:
the strongest engine that fits in 4 KB.

## How strong is it?

Practice trials against the official environment's anchor opponents
(12 games, 30,000-node fixed budget, no timeouts):

| Trial | Result | Elo (MLE vs anchors) |
|---|---|---|
| trial-0 | 3 wins / 0 draws / 3 losses | 1,279 |
| trial-1 | 5 wins / 0 draws / 1 loss | 1,654 |
| **combined** | **8 wins / 0 draws / 4 losses** | **~1,451** |

That clears the 1,154 Elo floor for the final and sits above the house
sunfish baseline (~1,325–1,365). It beats the depth-4 anchor and has
beaten the 100k-node and 500k-node anchors.

The golfed engine passes 37/37 regression tests (exact perft depth 3 on
6 positions, legal moves on 22 FENs, mate-in-1, determinism) and both
trials ran with no timeouts — max think under 2 s per move against the
10 s limit.

## Design

A rewrite of the classic sunfish architecture into a 120-character
string board, always viewed from the side to move and rotated after
every move — immutable strings mean no make/unmake machinery, which is
what leaves room for real search features inside 4 KB:

- **Negamax + alpha-beta with PVS**, MTD-bi driver and a transposition
  table storing lower/upper bounds
- **Null-move pruning** (R=2, depth ≥ 3, only with non-pawn material)
- **Killer move** ordering and repetition detection against the game history
- **Quiescence search** with a futility ceiling, plus checkmate and
  stalemate detection with mate-distance scoring
- **Full move generation**: castling, en passant, and underpromotion
  to knight, bishop, rook or queen
- **Evaluation**: material plus six piece-square tables (mirrored,
  quantized to multiples of 5)
- **Deterministic**: a fixed 30,000-node budget per move, no clock —
  the same position always produces the same move

A 50,000-node trial scored identically to 30,000 nodes (3/6, Elo 1,279),
so the extra budget adds no strength here — the final budget stays at
30,000 nodes. Compared with the v2 engine (Elo ~940), v3 is +511 Elo.

## Interface

`main.py` is not UCI. It talks to the competition environment over HTTP
(`$MAKEFUN_ENV_URL`): `POST /game` for the current state, `POST /move`
with a UCI move string, `POST /resign` to resign.

## Files

- `main.py` — the engine (4,086 bytes, the whole entry)
- `LICENSE` — MIT

Built as an entry for the make.fun tiny-chess-01 bounty ($500).
