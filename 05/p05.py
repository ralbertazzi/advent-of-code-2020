with open("data.txt") as f:
    lines = [line.strip() for line in f.readlines()]


def translate(boarding_pass: str) -> tuple[int, int]:
    vertical, horizontal = boarding_pass[:7], boarding_pass[7:]
    row = int(vertical.replace("F", "0").replace("B", "1"), 2)
    col = int(horizontal.replace("L", "0").replace("R", "1"), 2)
    return row, col


translations = [translate(boarding_pass) for boarding_pass in lines]
seat_ids = set(row * 8 + column for row, column in translations)
max_seat_id = max(seat_ids)
print(max_seat_id)

all_seat_ids = set(range(0, 128 * 8))
print(all_seat_ids - seat_ids)
