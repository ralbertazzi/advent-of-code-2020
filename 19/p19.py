from itertools import product
from typing import Iterable

from tqdm import tqdm

with open("data.txt") as f:
    data: list[str] = [line.strip() for line in f.readlines()]

temp_rules: dict[int, str] = {}
for s in data[:130]:
    splits = s.split(": ")
    temp_rules[int(splits[0])] = splits[1]


rules: dict[int, set[str]] = {}


def solve(rule: int) -> set[str]:
    if rule not in rules:
        value = temp_rules[rule]
        if '"' in value:
            rules[rule] = set(value[1])
        else:
            options = value.split(" | ")
            values = set()
            for option in options:
                suboptions = [int(op) for op in option.split(" ")]
                suboptions_values = [solve(subop) for subop in suboptions]
                if len(suboptions_values) == 1:
                    values.update(suboptions_values[0])
                else:
                    values.update(
                        "".join(chunks) for chunks in product(*suboptions_values)
                    )
            rules[rule] = values
        # print(rule)

    return rules[rule]


messages = set(data[131:])
allowed = solve(0)
print(len(messages.intersection(allowed)))

for index in [0, 8, 11]:
    rules.pop(index)

temp_rules[8] = "42 | 42 42"
temp_rules[11] = "42 31 | 42 42 31 31"
print(set(len(s) for s in rules[42]))


def combinations(n_chunks: int) -> Iterable[list[int]]:
    max31 = (n_chunks - 1) // 2
    for n31 in range(1, max31 + 1):
        yield [42] * (n_chunks - n31) + [31] * n31


def chunks(s: str, n: int) -> Iterable[str]:
    for i in range(0, len(s), n):
        yield s[i : i + n]


ok = 0
for message in tqdm(messages):
    if len(message) % 8 != 0:
        continue

    n_chunks = len(message) // 8
    for comb in combinations(n_chunks):
        if all(chunk in rules[c] for c, chunk in zip(comb, chunks(message, 8))):
            ok += 1
            break

print(ok)
# allowed = solve(0)
# print(len(messages.intersection(allowed)))
