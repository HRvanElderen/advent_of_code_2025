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
    if d == 'L':
        l = (l - n) % 100
    else:
        l = (l + n) % 100
    if l == 0:
        count += 1

print(count)
