from dataclasses import dataclass
from typing import Optional

from tqdm import trange

cups = [9, 6, 2, 7, 1, 3, 8, 5, 4]


@dataclass
class Node:
    value: int
    next: Optional["Node"]


def play(cups: list[int], rounds: int) -> list[int]:
    initial_length = len(cups)

    values_map: dict[int, Node] = dict()
    for i in range(len(cups)):
        values_map[cups[i]] = Node(cups[i], None)
        if i > 0:
            values_map[cups[i - 1]].next = values_map[cups[i]]

    values_map[cups[-1]].next = values_map[cups[0]]

    current: Node = values_map[cups[0]]
    for _ in trange(rounds):
        removed = current.next
        current.next = current.next.next.next.next

        destination_value = current.value - 1 if current.value - 1 != 0 else initial_length
        removed_values = {removed.value, removed.next.value, removed.next.next.value}
        while destination_value in removed_values:
            destination_value = destination_value - 1 if destination_value - 1 != 0 else initial_length

        destination = values_map[destination_value]
        destination_next = destination.next
        destination.next = removed
        removed.next.next.next = destination_next
        current = current.next

    current = values_map[1].next
    while current.value != 1:
        yield current.value
        current = current.next


part1 = list(play(cups[::], rounds=100))
print("".join(map(str, part1)))

part2 = play(cups + list(range(max(cups) + 1, 1_000_000 + 1)), rounds=10_000_000)
print(next(part2) * next(part2))
