from collections import Counter

with open("data.txt") as f:
    values = set(int(line.strip()) for line in f.readlines())

values.add(0)
values.add(max(values) + 3)


def part1():
    value_list = sorted(values)
    diffs = [value_list[i] - value_list[i - 1] for i in range(1, len(value_list))]
    counter = Counter(diffs)
    print(counter[3] * counter[1])


def part2():
    arr_cache: dict[int, int] = dict()
    arr_cache[max(values)] = 1

    def arrangements(adapter: int) -> int:
        result = arr_cache.get(adapter)
        if result is None:
            result = sum(
                arrangements(candidate)
                for candidate in range(adapter + 3, adapter, -1)
                if candidate in values
            )
            arr_cache[adapter] = result
        return result

    print(arrangements(0))


part1()
part2()
