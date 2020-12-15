with open("data.txt") as f:
    data: list[str] = [line.strip() for line in f.readlines()]


def part1():
    earliest_timestamp = int(data[0])
    bus_ids = [int(bid) for bid in data[1].split(",") if bid != "x"]
    time_to_wait = [
        (bus_id, (bus_id - earliest_timestamp % bus_id) % bus_id)
        for bus_id in bus_ids
    ]

    min_value = min(time_to_wait, key=lambda t: t[1])
    print(min_value[0] * min_value[1])


"""
t % a = 0
(t + 1) % b = 0 --> t % b = -1
(t + 4) % c = 0 --> t % c = -4

b = a + k
(t + 1) % (a + k) = t % (a + k) + 1
"""


def part2():
    bus_ids = [(idx, int(bid)) for idx, bid in enumerate(data[1].split(",")) if bid != "x"]
    print(", ".join(f"(t + {idx}) mod {bus_id} = 0" for idx, bus_id in bus_ids))
    # Go to wolframalpha :)


part1()
part2()
