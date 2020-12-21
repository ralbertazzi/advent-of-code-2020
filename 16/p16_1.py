with open("data.txt") as f:
    data: list[str] = [line.strip() for line in f.readlines()]

rules, tickets = data[:20], data[25:]
print(rules)

valid_numbers = set()
for rule in rules:
    ranges = rule.split(": ")[1]
    ranges = ranges.split(" or ")
    for r in ranges:
        min_value, max_value = r.split("-")
        valid_numbers.update(set(range(int(min_value), int(max_value) + 1)))

print(len(valid_numbers))

all_invalid_numbers = []
for ticket in tickets:
    numbers = [int(n) for n in ticket.split(",")]
    invalid_numbers = [n for n in numbers if n not in valid_numbers]
    assert len(invalid_numbers) <= 1
    all_invalid_numbers.extend(invalid_numbers)

print(sum(all_invalid_numbers))
