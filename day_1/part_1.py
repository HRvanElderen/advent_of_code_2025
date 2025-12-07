input_file = "input"

moves: list[tuple[str, int]] = []

with open(input_file, "r") as f:
    for line in f.readlines():
        direction = line[0]
        distance = int(line[1:])

        moves.append((direction, distance))

location = 50
count = 0
for direction, distance in moves:
    if direction == 'L':
        location = (location - distance) % 100
    else:
        location = (location + distance) % 100
    if location == 0:
        count += 1

print(count)
