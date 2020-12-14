with open("data.txt") as f:
    instructions: list[str] = [line.strip() for line in f.readlines()]


def north(pos: tuple[int, int], orient: int, steps: int) -> tuple[tuple[int, int], int]:
    new_pos = pos[0] + steps, pos[1]
    return new_pos, orient


def south(pos: tuple[int, int], orient: int, steps: int) -> tuple[tuple[int, int], int]:
    new_pos = pos[0] - steps, pos[1]
    return new_pos, orient


def east(pos: tuple[int, int], orient: int, steps: int) -> tuple[tuple[int, int], int]:
    new_pos = pos[0], pos[1] + steps
    return new_pos, orient


def west(pos: tuple[int, int], orient: int, steps: int) -> tuple[tuple[int, int], int]:
    new_pos = pos[0], pos[1] - steps
    return new_pos, orient


def left(pos: tuple[int, int], orient: int, degrees: int) -> tuple[tuple[int, int], int]:
    return pos, (orient + degrees) % 360


def right(pos: tuple[int, int], orient: int, degrees: int) -> tuple[tuple[int, int], int]:
    return pos, (orient - degrees) % 360


def forward(pos: tuple[int, int], orient: int, steps: int) -> tuple[tuple[int, int], int]:
    directions = {0: east, 90: north, 180: west, 270: south}
    return directions[orient](pos, orient, steps)


def part1():
    pos = 0, 0
    orient = 0
    fns = {"E": east, "N": north, "W": west, "S": south, "L": left, "R": right, "F": forward}
    for instruction in instructions:
        fn = fns[instruction[0]]
        steps = int(instruction[1:])
        pos, orient = fn(pos, orient, steps)
    print(abs(pos[0]) + abs(pos[1]))


part1()
