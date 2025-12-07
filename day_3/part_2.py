input_file = "input"


def max_jolt(b, s, e):
    m = (0, 0)
    for i, v in enumerate(b):
        if v > m[1] and s <= i <= e:
            m = (i, v)
    return m


rows = []
with open(input_file, "r") as f:
    for line in f.readlines():
        b = []
        for n in line:
            if n == '\n':
                continue
            b.append(int(n))
        rows.append(b)

total = 0
for row in rows:
    batteries = []
    i = -1
    row_len = len(row)
    for b in range(12):
        i, n1 = max_jolt(row, i+1, row_len-(12-b))

        batteries.append(n1)
    total += int(''.join(map(str, batteries)))

print(total)
