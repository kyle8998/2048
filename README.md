# 2048

A 2048 implementation on the command line created by Kyle Lim

### How it works

If you aren't familiar with the rules of 2048 see https://en.wikipedia.org/wiki/2048_(video_game)

You first select a board size (standard is 4x4), and then I render the board on the command line.
You then can perform actions by pressing the wasd keys for up, left, down, right respectively.
These directions will slide the blocks in that direction and merge if necessary.

Scoring is based on the tiles that are merged. For example if a 2 and 2 are merged you will score 4 points.

You lose if there are no more valid possible moves.

