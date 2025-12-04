input_file = "input"

moves = []
with open(input_file, "r") as f:
    for line in f.readlines():
        d = line[0]
        n = int(line[1:])

        moves.append((d, n))

l = 50
count = 0
for d, n in moves:
    prev = l

    if d == 'L':
        prev = l
        l = l - n

        if l == 0:
            count += 1
        if l < 0:
            # don't count double when passing 0
            if prev != 0:
                count += 1
            count += abs(int(l/100))
    else:
        l = l + n
        count += int(l/100)

    l = l % 100


print(count)
