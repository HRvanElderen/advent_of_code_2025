from functools import lru_cache

input_file = "input"

grid: list[list[str]] = []

with open(input_file, "r") as f:
    for line in f:
        grid.append(list(line.strip()))


@lru_cache
def traverse(row_i: int, col_i: int) -> int:
    if len(grid) == row_i+1:
        return 1

    if grid[row_i+1][col_i] == '^':
        return traverse(row_i+1, col_i+1) + traverse(row_i+1, col_i-1)
    else:
        return traverse(row_i+1, col_i)


# find the starting index
start_i = 0
for i, v in enumerate(grid[0]):
    if v == 'S':
        start_i = i
        break

total = traverse(0, start_i)

print(total)
