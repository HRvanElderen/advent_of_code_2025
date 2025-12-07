# Reduce the ranges by adding them up.

input_file = "input"


def reduce(ranges: list[str]) -> set[str]:
    final_ranges: set[str] = set()
# remove ranges in other range
    for r1 in ranges:
        r1_bounds = r1.split("-")
        max_left_bound = int(r1_bounds[0])
        max_right_bound = int(r1_bounds[1])
        for r2 in ranges:
            r2_bounds = r2.split("-")
            left_bound = int(r2_bounds[0])
            right_bound = int(r2_bounds[1])

            if (
                left_bound < max_left_bound and left_bound <= max_left_bound <= right_bound
            ):  # new left bound
                max_left_bound = left_bound

            elif (
                left_bound <= max_right_bound >= max_left_bound
                and max_right_bound < right_bound
            ):  # new right bound
                max_right_bound = right_bound

            elif (
                max_left_bound > left_bound and max_right_bound < right_bound
            ):  # both in range
                max_left_bound = left_bound
                max_right_bound = right_bound

        final_ranges.add(f"{max_left_bound}-{max_right_bound}")
    return final_ranges


ranges: list[str] = []
part_1 = True
with open(input_file, "r") as f:
    for line in f.readlines():
        if line == "\n":
            part_1 = False
            continue

        if part_1:
            ranges.append(line.rstrip())


prev_len = -1
length = len(ranges)
while length != prev_len:
    ranges = list(reduce(ranges))
    prev_len = length
    length = len(ranges)

# sum all ranges
total = 0
for r in ranges:
    r_split = r.split("-")
    total += (int(r_split[1]) - int(r_split[0])) + 1

print(total)
# 354143734113772
