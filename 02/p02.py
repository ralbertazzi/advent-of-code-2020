from collections import Counter
from typing import Tuple

with open("data.txt") as f:
    lines = [l.strip() for l in f.readlines()]


def extract_info(line: str) -> Tuple[str, str, int, int]:
    left, right = line.split(":")
    pwd = right[1:]
    letter = left[-1]
    policy = left[:-2]
    policy_min, policy_max = map(int, policy.split("-"))
    return pwd, letter, policy_min, policy_max


def valid_line_part_1(line: str) -> bool:
    pwd, letter, policy_min, policy_max = extract_info(line)
    counter = Counter(pwd)
    return policy_min <= counter[letter] <= policy_max


def valid_line_part_2(line: str) -> bool:
    pwd, letter, idx1, idx2 = extract_info(line)
    occ1, occ2 = pwd[idx1 - 1] == letter, pwd[idx2 - 1] == letter
    return occ1 ^ occ2


for valid_func in valid_line_part_1, valid_line_part_2:
    valid_lines = sum(1 for line in lines if valid_func(line))
    print(valid_lines)
