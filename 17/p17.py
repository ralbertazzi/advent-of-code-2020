from itertools import product

import numpy as np

with open("data.txt") as f:
    data: list[str] = [line.strip() for line in f.readlines()]


def get_next_state_1(state: np.ndarray) -> np.ndarray:
    padded_state = np.pad(state, ((1, 1), (1, 1), (1, 1)), constant_values=".")
    next_state = np.copy(padded_state)

    for (z, x, y), value in np.ndenumerate(padded_state):
        active = 0
        for dz, dx, dy in product((-1, 0, 1), repeat=3):
            if dx == dy == dz == 0:
                continue
            nz, nx, ny = z + dz, x + dx, y + dy
            if (
                nz < 0
                or nz >= padded_state.shape[0]
                or nx < 0
                or nx >= padded_state.shape[1]
                or ny < 0
                or ny >= padded_state.shape[2]
            ):
                continue
            active += 1 if padded_state[nz, nx, ny] == "#" else 0

        if value == "." and active == 3:
            next_state[z, x, y] = "#"
        elif value == "#" and active not in [2, 3]:
            next_state[z, x, y] = "."

    return next_state


def get_next_state_2(state: np.ndarray) -> np.ndarray:
    padded_state = np.pad(state, ((1, 1), (1, 1), (1, 1), (1, 1)), constant_values=".")
    next_state = np.copy(padded_state)

    for (w, z, x, y), value in np.ndenumerate(padded_state):
        active = 0
        for dw, dz, dx, dy in product((-1, 0, 1), repeat=4):
            if dx == dy == dz == dw == 0:
                continue
            nw, nz, nx, ny = w + dw, z + dz, x + dx, y + dy
            if (
                nw < 0
                or nw >= padded_state.shape[0]
                or nz < 0
                or nz >= padded_state.shape[1]
                or nx < 0
                or nx >= padded_state.shape[2]
                or ny < 0
                or ny >= padded_state.shape[3]
            ):
                continue
            active += 1 if padded_state[nw, nz, nx, ny] == "#" else 0

        if value == "." and active == 3:
            next_state[w, z, x, y] = "#"
        elif value == "#" and active not in [2, 3]:
            next_state[w, z, x, y] = "."

    return next_state


def part1():
    state = np.array([[list(s) for s in data]])
    for _ in range(6):
        state = get_next_state_1(state)

    print(np.count_nonzero(state == "#"))


def part2():
    state = np.array([[[list(s) for s in data]]])
    for _ in range(6):
        state = get_next_state_2(state)

    print(np.count_nonzero(state == "#"))


part1()
part2()
