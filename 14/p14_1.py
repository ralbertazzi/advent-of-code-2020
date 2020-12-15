with open("data.txt") as f:
    data: list[str] = [line.strip() for line in f.readlines()]


def get_replacement_map(mask: str) -> dict[int, str]:
    return {i: s for i, s in enumerate(mask) if s != "X"}


def replace(value: str, replacement_map: dict[int, str]) -> str:
    return "".join(replacement_map.get(i, s) for i, s in enumerate(value))


def part1() -> None:
    memory: dict[int, int] = {}
    replacement_map: dict[int, str] = {}

    for line in data:
        instruction, value = line.split(" = ")
        if instruction == "mask":
            replacement_map = get_replacement_map(value)
        else:
            bin_value = format(int(value), "b").zfill(36)
            new_value = replace(bin_value, replacement_map)
            address = int(instruction[4:-1])
            memory[address] = int(new_value, 2)

    print(sum(memory.values()))


part1()
