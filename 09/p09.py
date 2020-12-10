with open("data.txt") as f:
    values = [int(line.strip()) for line in f.readlines()]


def part1():
    window_size = 25
    for i in range(len(values) - window_size - 1):
        window = set(values[i : i + window_size])
        target = values[i + window_size]

        valid = False
        for value in window:
            if target - value in window and (target - value) != value:
                valid = True
                break

        if not valid:
            print(target)
            break


def part2():
    target = 1038347917
    for start in range(len(values)):
        sum = values[start]
        end = start
        while sum < target:
            end += 1
            sum += values[end]

        if sum == target:
            window = values[start : end + 1]
            print(min(window) + max(window))
            break


part1()
part2()
