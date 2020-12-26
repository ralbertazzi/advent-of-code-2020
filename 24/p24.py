from typing import Iterable

with open("data.txt") as f:
    lines: list[str] = [line.strip() for line in f.readlines()]


def get_moves(s: str) -> Iterable[str]:
    i = 0
    while i < len(s):
        if s[i] in ["n", "s"]:
            yield s[i] + s[i + 1]
            i += 2
        else:
            yield s[i]
            i += 1


def find_coordinates(moves: Iterable[str]) -> tuple[int, int]:
    x, y = 0, 0
    for move in moves:
        dx, dy = moves_deltas[move]
        x += dx
        y += dy

    return x, y


moves_deltas: dict[str, tuple[int, int]] = {
    "e": (1, 0),
    "w": (-1, 0),
    "nw": (0, 1),
    "se": (0, -1),
    "ne": (1, 1),
    "sw": (-1, -1),
}

black_tiles: set[tuple[int, int]] = set()

for line in lines:
    x, y = find_coordinates(get_moves(line))
    if (x, y) in black_tiles:
        black_tiles.remove((x, y))
    else:
        black_tiles.add((x, y))

print(len(black_tiles))


def get_neighbours(x: int, y: int) -> Iterable[tuple[int, int]]:
    for dx, dy in moves_deltas.values():
        yield x + dx, y + dy


def get_white_tiles(current_black_tiles: set[tuple[int, int]]) -> set[tuple[int, int]]:
    white_tiles: set[tuple[int, int]] = set()
    for x, y in current_black_tiles:
        for n in get_neighbours(x, y):
            if n not in current_black_tiles:
                white_tiles.add(n)

    return white_tiles


def count_black_neighbours(xy: tuple[int, int], current_black_tiles: set[tuple[int, int]]) -> int:
    return sum(1 for n in get_neighbours(*xy) if n in current_black_tiles)


def get_next_state(current_black_tiles: set[tuple[int, int]]) -> set[tuple[int, int]]:
    white_tiles = get_white_tiles(current_black_tiles)
    next_black_tiles: set[tuple[int, int]] = set()

    for x, y in current_black_tiles:
        bn = count_black_neighbours((x, y), current_black_tiles)
        if bn == 1 or bn == 2:
            next_black_tiles.add((x, y))

    for x, y in white_tiles:
        bn = count_black_neighbours((x, y), current_black_tiles)
        if bn == 2:
            next_black_tiles.add((x, y))

    return next_black_tiles


for _ in range(100):
    black_tiles = get_next_state(black_tiles)

print(len(black_tiles))
