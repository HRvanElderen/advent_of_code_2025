input_file = "input"


def max_jolt(b, s, e):
    m = (0, 0)
    for i, j in enumerate(b[s:e]):
        if j > m[1]:
            m = (i, j)
    return m


batteries = []
with open(input_file, "r") as f:
    for line in f.readlines():
        b = []
        for n in line:
            if n == '\n':
                continue
            b.append(int(n))
        batteries.append(b)

print(batteries)

total = 0
for b in batteries:
    i, n1 = max_jolt(b, 0, len(b)-1)
    print(b[0:len(b)])
    i, n2 = max_jolt(b, i+1, len(b))
    total += int(str(n1) + str(n2))
print(total)
