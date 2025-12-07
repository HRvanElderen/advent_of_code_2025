

def max_jolt(b: list[int], s: int, e: int) -> tuple[int, int]:
    m = (0, 0)
    for i, v in enumerate(b):
        if v > m[1] and s <= i <= e:
            m = (i, v)
    return m


def read_input(file: str):
    batteries: list[list[int]] = []

    with open(file, "r") as f:
        for line in f.readlines():
            battery: list[int] = []

            for n in line.strip():
                battery.append(int(n))
            batteries.append(battery)

    return batteries


batteries = read_input("input")

total = 0
for battery in batteries:
    best_batteries: list[int] = []
    i = -1
    row_len = len(battery)
    for b in range(12):
        i, n1 = max_jolt(battery, i+1, row_len-(12-b))

        best_batteries.append(n1)
    total += int(''.join(map(str, best_batteries)))

print(total)
