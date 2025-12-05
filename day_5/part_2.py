input_file = "input"


def in_range_other(ranges, r):
    for r1 in ranges:
        parts = r.split('-')
        parts1 = r1.split('-')
        # if in other range
        if int(parts[0]) > int(parts1[0]) and int(parts[1]) < int(parts1[1]):
            return True
    return False


ranges = []
ingredients = []
part_1 = True
with open(input_file, "r") as f:
    for line in f.readlines():
        if line == "\n":
            part_1 = False
            continue

        if part_1:
            ranges.append(line.rstrip())
        else:
            ingredients.append(line.rstrip())

print(ranges)

r_new = []
fresh = set()
# remove ranges in other range
for ingredient in ingredients:
    for i, r in enumerate(ranges):
        if in_range_other(ranges, r):
            ranges.pop(i)


print(ranges)

fresh = set()
for ingredient in ingredients:
    for r in ranges:
        parts = r.split('-')
        fresh.update(range(int(parts[0]), int(parts[1])+1))
        # for n in range(int(parts[0]), int(parts[1])+1):
        #     fresh.add(n)

print(len(fresh))
