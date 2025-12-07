

def read_input(file: str):
    batteries: list[list[int]] = []

    with open(file, "r") as f:
        for line in f.readlines():
            battery: list[int] = []

            for n in line.strip():
                battery.append(int(n))
            batteries.append(battery)

    return batteries


def max_jolt(b: list[int], s: int, e: int):
    m = (0, 0)
    for i, j in enumerate(b[s:e]):
        if j > m[1]:
            m = (i, j)
    return m


batteries = read_input("input")

total = 0
for battery in batteries:
    i, n1 = max_jolt(battery, 0, len(battery)-1)
    i, n2 = max_jolt(battery, i+1, len(battery))
    total += int(str(n1) + str(n2))

print(total)
