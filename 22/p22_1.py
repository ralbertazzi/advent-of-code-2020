with open("data.txt") as f:
    lines: list[str] = [line.strip() for line in f.readlines()]

cards1 = list(map(int, lines[1:26]))
cards2 = list(map(int, lines[28:]))

while cards1 and cards2:
    c1, c2 = cards1.pop(0), cards2.pop(0)
    winner = cards1 if c1 > c2 else cards2
    winner.extend(sorted([c1, c2], reverse=True))

winner = cards1 if cards1 else cards2
winner_score = sum(score * card for score, card in enumerate(winner[::-1], start=1))
print(winner_score)
