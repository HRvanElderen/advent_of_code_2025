input_file = "input"

moves: list[tuple[str, int]] = []

with open(input_file, "r") as f:
    for line in f.readlines():
        d = line[0]
        n = int(line[1:])

        moves.append((d, n))

location = 50
count = 0
for direction, distance in moves:
    prev = location

    if direction == 'L':
        prev = location
        location = location - distance

        if location == 0:
            count += 1
        if location < 0:
            # don't count double when passing 0
            if prev != 0:
                count += 1
            count += abs(int(location/100))
    else:
        location = location + distance
        count += int(location/100)

    location = location % 100


print(count)
