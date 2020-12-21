with open("data.txt") as f:
    data: list[str] = [line.strip() for line in f.readlines()]

rules_, tickets = data[:20], data[25:]
tickets.append(data[22])
tickets = [[int(n) for n in ticket.split(",")] for ticket in tickets]

rules: dict[str, set[int]] = dict()
for rule in rules_:
    name, ranges = rule.split(": ")
    ranges = ranges.split(" or ")
    numbers = set()
    for r in ranges:
        min_value, max_value = r.split("-")
        numbers.update(set(range(int(min_value), int(max_value) + 1)))
    rules[name] = numbers

tickets = [
    ticket
    for ticket in tickets
    if all(any(n in rules[rule] for rule in rules) for n in ticket)
]

columns_valid: dict[str, set[int]] = dict()
columns = list(range(len(tickets[0])))
for rule in rules:
    columns_valid[rule] = set(columns)
    for c in columns:
        for ticket in tickets:
            if ticket[c] not in rules[rule]:
                columns_valid[rule].remove(c)
                break

final: dict[str, int] = dict()
while any(len(options) > 1 for options in columns_valid.values()):
    rule = next(
        rule
        for rule in columns_valid
        if rule not in final and len(columns_valid[rule]) == 1
    )
    column = columns_valid[rule].pop()
    final[rule] = column
    for other_rule in columns_valid:
        columns_valid[other_rule].discard(column)

print(final)
my_ticket = tickets[-1]
result = 1
for rule in rules:
    if rule.startswith("departure"):
        result *= my_ticket[final[rule]]

print(result)
