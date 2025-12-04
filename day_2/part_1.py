input_file = "input"


with open(input_file, "r") as f:
    for line in f.readlines():
        ranges = line.split(',')

print(ranges)
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
