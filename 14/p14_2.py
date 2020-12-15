from itertools import product
from typing import Iterable

with open("data.txt") as f:
    data: list[str] = [line.strip() for line in f.readlines()]


def get_replacement_map(mask: str) -> dict[int, str]:
    return {i: s for i, s in enumerate(mask) if s != "0"}


def replace(address: str, replacement_map: dict[int, str]) -> str:
    return "".join(replacement_map.get(i, s) for i, s in enumerate(address))


def get_addresses(address: str) -> Iterable[int]:
    indices = [i for i, s in enumerate(address) if s == "X"]
    for values in product("01", repeat=len(indices)):
        mask = {indices[i]: values[i] for i in range(len(indices))}
        yield int("".join(mask.get(i, s) for i, s in enumerate(address)))


def part2() -> None:
    memory: dict[int, int] = {}
    replacement_map: dict[int, str] = {}

    for line in data:
        instruction, value = line.split(" = ")
        if instruction == "mask":
            replacement_map = get_replacement_map(value)
        else:
            address = int(instruction[4:-1])
            bin_address = format(int(address), "b").zfill(36)
            new_address = replace(bin_address, replacement_map)
            for addr in get_addresses(new_address):
                memory[addr] = int(value)

    print(sum(memory.values()))


part2()
