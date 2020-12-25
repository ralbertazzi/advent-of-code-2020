with open("data.txt") as f:
    lines: list[str] = [line.strip() for line in f.readlines()]

deck1 = list(map(int, lines[1:26]))
deck2 = list(map(int, lines[28:]))


def game(cards1: list[int], cards2: list[int]) -> tuple[list[int], list[int]]:
    configurations = set()

    while cards1 and cards2:
        config = (tuple(cards1), tuple(cards2))
        if config in configurations:
            return cards1, []
        else:
            configurations.add(config)

        c1, c2 = cards1.pop(0), cards2.pop(0)
        if len(cards1) >= c1 and len(cards2) >= c2:
            sub_cards1, sub_cards2 = game(cards1[:c1], cards2[:c2])
            winner = cards1 if sub_cards1 else cards2
        else:
            winner = cards1 if c1 > c2 else cards2

        winner.extend([c1, c2] if winner == cards1 else [c2, c1])

    return cards1, cards2


deck1, deck2 = game(deck1, deck2)
winner = deck1 if deck1 else deck2
winner_score = sum(score * card for score, card in enumerate(winner[::-1], start=1))
print(winner_score)
