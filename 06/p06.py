from typing import Optional

with open("data.txt") as f:
    lines = [line.strip() for line in f.readlines()]


def part1():
    sets: list[set[str]] = []
    curr_set: set[str] = set()
    for line in lines:
        if line == "":
            sets.append(curr_set)
            curr_set = set()
            continue

        curr_set.update(set(line))

    result = sum(len(s) for s in sets)
    print(result)


def part2():
    all_yes: list[int] = []
    curr_set: Optional[set[str]] = None
    for line in lines:
        if line == "" and curr_set is not None:
            all_yes.append(len(curr_set))
            curr_set = None
            continue

        if curr_set is None:
            curr_set = set(line)
        else:
            curr_set = curr_set.intersection(set(line))

    result = sum(all_yes)
    print(result)


part1()
part2()
