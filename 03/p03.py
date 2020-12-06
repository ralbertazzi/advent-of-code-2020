from functools import reduce
from typing import Tuple

with open("data.txt") as f:
    area = [line.strip() for line in f.readlines()]

TREE = "#"


def get_num_trees(move: Tuple[int, int]) -> int:
    y, x = 0, 0
    num_trees = 0
    while y < len(area):
        if area[y][x] == TREE:
            num_trees += 1
        y += move[0]
        x = (x + move[1]) % len(area[0])
    return num_trees


moves = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
result = reduce(lambda x, y: x * y, [get_num_trees(move) for move in moves], 1)
print(result)
