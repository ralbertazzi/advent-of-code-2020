from math import cos, radians, sin

with open("data.txt") as f:
    instructions: list[str] = [line.strip() for line in f.readlines()]


def north(pos: tuple[int, int], steps: int) -> tuple[int, int]:
    new_pos = pos[0] + steps, pos[1]
    return new_pos


def south(pos: tuple[int, int], steps: int) -> tuple[int, int]:
    new_pos = pos[0] - steps, pos[1]
    return new_pos


def east(pos: tuple[int, int], steps: int) -> tuple[int, int]:
    new_pos = pos[0], pos[1] + steps
    return new_pos


def west(pos: tuple[int, int], steps: int) -> tuple[int, int]:
    new_pos = pos[0], pos[1] - steps
    return new_pos


def rotate(pos: tuple[int, int], degrees: int) -> tuple[int, int]:
    rad = radians(degrees)
    y = cos(rad) * pos[0] + sin(rad) * pos[1]
    x = -sin(rad) * pos[0] + cos(rad) * pos[1]
    return int(round(y)), int(round(x))


def left(pos: tuple[int, int], degrees: int) -> tuple[int, int]:
    return rotate(pos, degrees)


def right(pos: tuple[int, int], degrees: int) -> tuple[int, int]:
    return rotate(pos, -degrees)


def forward(
    ship: tuple[int, int], waypoint: tuple[int, int], n: int
) -> tuple[int, int]:
    return ship[0] + n * waypoint[0], ship[1] + n * waypoint[1]


def part2():
    ship = (0, 0)
    waypoint = (1, 10)
    fns = {"N": north, "S": south, "E": east, "W": west, "L": left, "R": right}

    for instruction in instructions:
        code = instruction[0]
        value = int(instruction[1:])
        if code == "F":
            ship = forward(ship, waypoint, value)
        else:
            fn = fns[code]
            waypoint = fn(waypoint, value)

    print(abs(ship[0]) + abs(ship[1]))


part2()
