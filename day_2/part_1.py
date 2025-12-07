# goal: if number in range has two equal parts.
# iterate over all ranges and split the number using slicing and check if parts are equal.
input_file = "input"

ranges: list[str] = []

with open(input_file, "r") as f:
    for line in f.readlines():
        ranges = line.split(',')


total = 0
for id_range in ranges:
    parts = id_range.split('-')
    for n in range(int(parts[0]), int(parts[1])+1):
        s = str(n)
        first_half = s[:len(s)//2]
        second_half = s[len(s)//2:]

        if first_half == second_half:
            total += n

print(total)
