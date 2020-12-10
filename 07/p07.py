with open("data.txt") as f:
    lines = [line.strip() for line in f.readlines()]

# color -> contained colors (number, color)
direct: dict[str, set[tuple[int, str]]] = {}

for line in lines:
    words = line.split(" bags contain ")
    color = words[0]
    contents = words[1].replace(".", "").split(", ")
    if contents[0] == "no other bags":
        direct[color] = set()
    else:
        values = set()
        for content in contents:
            splits = content.split(" ")
            values.add((int(splits[0]), " ".join(splits[1:3])))
        direct[color] = values


def part1():
    reverse: dict[str, set[str]] = {}
    for color, contents in direct.items():
        for _, content in contents:
            s = reverse.get(content, set())
            s.add(color)
            reverse[content] = s

    elements: set[str] = set()
    curr_it = reverse["shiny gold"]

    while curr_it:
        next_it = set()
        for el in curr_it:
            elements.add(el)
            next_it.update(reverse.get(el, set()))

        curr_it = next_it

    print(len(elements))


def part2():
    def num_bags(color: str) -> int:
        return sum(n * (num_bags(sub_color) + 1) for n, sub_color in direct[color])

    n = num_bags("shiny gold")
    print(n)


part1()
part2()
