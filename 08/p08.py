from copy import copy
from typing import Callable

with open("data.txt") as f:
    lines = [line.strip() for line in f.readlines()]


def acc_fn(pc: int, acc: int, value: int) -> tuple[int, int]:
    return pc + 1, acc + value


def nop_fn(pc: int, acc: int, value: int) -> tuple[int, int]:
    return pc + 1, acc


def jmp_fn(pc: int, acc: int, value: int) -> tuple[int, int]:
    return pc + value, acc


fns: dict[str, Callable] = {"acc": acc_fn, "nop": nop_fn, "jmp": jmp_fn}


def run(lines: list[str]) -> tuple[bool, int]:
    executed_lines: set[int] = set()
    acc = 0
    pc = 0

    while pc not in executed_lines and pc < len(lines):
        next_line = lines[pc]
        executed_lines.add(pc)
        fn, value = next_line.split(" ")
        pc, acc = fns[fn](pc, acc, int(value))

    terminated = pc == len(lines)

    return terminated, acc


def part1():
    _, acc = run(lines)
    print(acc)


def part2():
    for i, line in enumerate(lines):
        if line[:3] in ["nop", "jmp"]:
            modified_lines = copy(lines)
            modified_lines[i] = modified_lines[i].replace("nop", "jmp").replace("jmp", "nop")
            terminated, acc = run(modified_lines)
            if terminated:
                print(acc)
                break


part1()
part2()
