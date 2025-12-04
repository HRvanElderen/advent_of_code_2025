input_file = "input"

with open(input_file, "r") as f:
    for line in f.readlines():
        ranges = line.split(',')


total = 0
for id_range in ranges:
    parts = id_range.split('-')
    for n in range(int(parts[0]), int(parts[1])+1):
        s = str(n)
        for size in range(1, len(s)):
            parts = [s[i:i+size] for i in range(0, len(s), size)]

            if len(set(parts)) == 1:

                total += n
                break
print(total)
