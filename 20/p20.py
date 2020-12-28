from collections import Counter, defaultdict
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

transformed_tiles: dict[int, list[np.ndarray]] = defaultdict(list)
for tid in tiles:
    for k in range(4):
        for flip_fn in [lambda x: x, lambda x: np.flip(x, axis=0), lambda x: np.flip(x, axis=1)]:
            transformed_tiles[tid].append(np.rot90(flip_fn(tiles[tid]), k=k))

size = 12
image = np.empty((12 * 10, 12 * 10), dtype=str)

corner_options = transformed_tiles[corners[0]]
for corner in corner_options:
    top_border = "".join(s for s in corner[0, :].flatten())
    left_border = "".join(s for s in corner[:, 0].flatten())
    if counter[top_border] == 1 and counter[left_border] == 1:
        image[:10, :10] = corner
        break
transformed_tiles.pop(corners[0])


def match_rows(a: np.ndarray, b: np.ndarray) -> bool:
    return np.all(a == b[0, :])


def match_cols(a: np.ndarray, b: np.ndarray) -> bool:
    return np.all(a == b[:, 0])


for i in range(size):
    for j in range(size):
        if i == 0 and j == 0:
            continue

        if j == 0:
            border = image[(i * 10) - 1, :10]
            match_fn = match_rows
        else:
            border = image[i * 10 : (i + 1) * 10, (j * 10) - 1]
            match_fn = match_cols

        found = False
        for tid in transformed_tiles:
            for tile in transformed_tiles[tid]:
                if match_fn(border, tile):
                    image[i * 10 : (i + 1) * 10, j * 10 : (j + 1) * 10] = tile
                    transformed_tiles.pop(tid)
                    found = True
                    break
            if found:
                break

indexes = [i for i in range(0, 120, 10)]
indexes.extend(range(9, 120, 10))
image = np.delete(image, indexes, axis=0)
image = np.delete(image, indexes, axis=1)


def find_monsters(img: np.ndarray, mask: np.ndarray) -> np.ndarray:
    result = img.copy()

    for i in range(img.shape[0] - mask.shape[0] + 1):
        for j in range(img.shape[1] - mask.shape[1] + 1):
            starth, endh = i, i + mask.shape[0]
            startw, endw = j, j + mask.shape[1]
            if np.all(img[starth:endh, startw:endw][mask] == "#"):
                result[starth:endh, startw:endw][mask] = "O"

    return result


monster = np.array(
    [
        list("                  # "),
        list("#    ##    ##    ###"),
        list(" #  #  #  #  #  #   "),
    ]
)
mask = monster == "#"

found = False
for k in range(4):
    for flip_fn in [lambda x: x, lambda x: np.flip(x, axis=0), lambda x: np.flip(x, axis=1)]:
        img = np.rot90(flip_fn(image), k=k)
        result = find_monsters(img, mask)
        if np.any(result == "O"):
            found = True
            print(np.count_nonzero(result == "#"))
            break
    if found:
        break
