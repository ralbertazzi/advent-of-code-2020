from copy import copy
from typing import Tuple, Optional

with open("data.txt") as f:
    numbers = set(int(l.strip()) for l in f.readlines())


def find_couple(s: set, target: int) -> Optional[Tuple[int, int]]:
    for n in s:
        if target - n in numbers:
            return n, target - n
    return None


# PART 1
n1, n2 = find_couple(numbers, 2020)
print(n1, n2, n1 * n2)

# PART 2
for n in numbers:
    numbers_copy = copy(numbers)
    numbers_copy.remove(n)
    res = find_couple(numbers_copy, 2020 - n)
    if res:
        print(n, res[0], res[1], n * res[0] * res[1])
        break
