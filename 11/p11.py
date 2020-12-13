from itertools import product
from typing import Callable

with open("data.txt") as f:
    seats: list[str] = [line.strip() for line in f.readlines()]

coordinate = tuple[int, int]

MAX_OCCUPIED: int = None  # type: ignore


def neighbors_1(state: list[str]) -> dict[coordinate, set[coordinate]]:
    result = dict()
    for row in range(len(state)):
        for col in range(len(state[row])):
            result[(row, col)] = set()

            for dx, dy in product((-1, 0, 1), (-1, 0, 1)):
                if dx == dy == 0:
                    continue

                y, x = row + dy, col + dx
                if 0 <= y < len(state) and 0 <= x < len(state[row]):
                    if state[y][x] != ".":
                        result[(row, col)].add((y, x))

    return result


def neighbors_2(state: list[str]) -> dict[coordinate, set[coordinate]]:
    result = dict()
    for row in range(len(state)):
        for col in range(len(state[row])):
            result[(row, col)] = set()

            for dx, dy in product((-1, 0, 1), (-1, 0, 1)):
                if dx == dy == 0:
                    continue

                y, x = row + dy, col + dx
                while 0 <= y < len(state) and 0 <= x < len(state[row]):
                    if state[y][x] != ".":
                        result[(row, col)].add((y, x))
                        break

                    y, x = y + dy, x + dx

    return result


def occupied_seats(
    row: int, col: int, state: list[str], neighbours: dict[coordinate, set[coordinate]]
) -> int:
    return sum(1 for y, x in neighbours[(row, col)] if state[y][x] == "#")


def next_value(
    row: int, col: int, state: list[str], neighbours: dict[coordinate, set[coordinate]]
) -> str:
    curr_value = state[row][col]
    if curr_value == ".":
        return "."
    else:
        occ_seats = occupied_seats(row, col, state, neighbours)
        if curr_value == "L" and occ_seats == 0:
            return "#"
        elif curr_value == "#" and occ_seats >= MAX_OCCUPIED:
            return "L"
        else:
            return curr_value


def transform(
    state: list[str], neighbours: dict[coordinate, set[coordinate]]
) -> list[str]:
    return [
        "".join(
            next_value(row, col, state, neighbours) for col in range(len(state[row]))
        )
        for row in range(len(state))
    ]


def count(state: list[str]) -> int:
    return sum(row.count("#") for row in state)


def loop(neighbours_func: Callable) -> None:
    neighbours = neighbours_func(seats)
    current_state = seats
    while True:
        next_state = transform(current_state, neighbours)
        if next_state == current_state:
            print(count(current_state))
            break
        else:
            current_state = next_state


MAX_OCCUPIED = 4
loop(neighbors_1)

MAX_OCCUPIED = 5
loop(neighbors_2)
