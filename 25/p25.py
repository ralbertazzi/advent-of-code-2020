m1 = 11404017
m2 = 13768789


def loop_step(value: int, subject: int) -> int:
    value *= subject
    value = value % 20201227

    return value


def find_loopsize(m: int) -> int:
    loopsize = 1
    value = 1
    while True:
        value = loop_step(value, 7)
        if value == m:
            break
        loopsize += 1

    return loopsize


l1, l2 = [find_loopsize(m) for m in (m1, m2)]
print(l1, l2)

value = 1
subject = m1 if l1 > l2 else m2
steps = min((l1, l2))
for _ in range(steps):
    value = loop_step(value, subject)

print(value)
