input_file = "input"


def in_range_other(ranges, r):
    parts = r.split("-")
    for r1 in ranges:

        parts1 = r1.split("-")
        # if in other range
        if int(parts[0]) <= int(parts1[0]) and int(parts[1]) >= int(parts1[1]):
            return True
    return False


def in_range_other2(ranges, r):
    parts = r.split("-")
    for r1 in ranges:

        parts1 = r1.split("-")
        print(parts, parts1)
        # if in other range
        if (
            int(parts[0]) >= int(parts1[0])
            and int(parts[1]) <= int(parts1[1])
            and parts != parts1
        ):
            print("test")
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

final_ranges = set()
# remove ranges in other range
for r1 in ranges:
    r1_bounds = r1.split("-")
    max_left_bound = int(r1_bounds[0])
    max_right_bound = int(r1_bounds[1])
    used = []
    for r2 in ranges:
        if in_range_other(final_ranges, r1):
            break
        r2_bounds = r2.split("-")
        left_bound = int(r2_bounds[0])
        right_bound = int(r2_bounds[1])
        print(
            f"max {max_left_bound}, {max_right_bound}, new {left_bound}, {right_bound} "
        )
        if max_left_bound < left_bound and right_bound < max_right_bound:  # in range
            break

        if (
            left_bound < max_left_bound and left_bound < max_left_bound < right_bound
        ):  # new left bound
            max_left_bound = left_bound

        elif (
            left_bound < max_right_bound > max_left_bound
            and max_right_bound < right_bound
        ):  # new right bound
            max_right_bound = right_bound

        elif (
            max_left_bound > left_bound and max_right_bound < right_bound
        ):  # both in range
            max_left_bound = left_bound
            max_right_bound = right_bound

    final_ranges.add(f"{max_left_bound}-{max_right_bound}")

print(final_ranges)
final_final_ranges = []
for r in final_ranges:
    print(r)
    if not in_range_other2(final_ranges, r):
        final_final_ranges.append(r)
print(final_final_ranges)

total = 0
for r in final_final_ranges:
    r_split = r.split("-")
    total += (int(r_split[1]) - int(r_split[0])) + 1

print(total)
