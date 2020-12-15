from tqdm import tqdm

start = [12, 1, 16, 3, 11, 0]
memory: dict[int, list[int]] = {n: [i] for i, n in enumerate(start, start=1)}

last = 0
for turn in tqdm(range(len(start) + 1, 30000001)):
    if len(memory[last]) == 1:
        last = 0
    else:
        last = memory[last][1] - memory[last][0]
    memory[last] = memory.get(last, [])
    memory[last].append(turn)
    memory[last] = memory[last][-2:]

print(last)
