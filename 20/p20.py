from collections import Counter
from functools import reduce

import numpy as np

with open("data.txt") as f:
    data: list[str] = [line.strip() for line in f.readlines()]

tiles: dict[int, np.ndarray] = {}

for i in range(0, len(data), 12):
    num = int(data[i][5:-1])
    tiles[num] = np.array([list(s) for s in data[i + 1 : i + 11]])

borders: list[str] = []
tiles_borders: dict[int, list[str]] = {}
for tid, tile in tiles.items():
    tiles_borders[tid] = []
    for border in [tile[0, :], tile[-1, :], tile[:, 0], tile[:, -1]]:
        b = "".join(s for s in border.flatten())
        tiles_borders[tid].append(b)
        borders.extend([b, b[::-1]])

counter = Counter(borders)

corners: list[int] = []
for tid in tiles_borders:
    n = sum(1 if counter[b] == 1 else 0 for b in tiles_borders[tid])
    if n == 2:
        corners.append(tid)

print(reduce(lambda x, y: x * y, corners, 1))
