input_file = "input"


def check_ingredient(ranges: list[str], ingredient: int):
    for r in ranges:
        parts = r.split('-')
        if ingredient > int(parts[0]) and ingredient < int(parts[1])+1:
            return 1
    return 0


ranges: list[str] = []
ingredients: list[str] = []
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

count = 0
for ingredient in ingredients:
    count += check_ingredient(ranges, int(ingredient))

print(count)
