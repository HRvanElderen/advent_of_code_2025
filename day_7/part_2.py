from functools import lru_cache

input_file = "input"

grid = []
with open(input_file, "r") as f:
    for line in f:
        grid.append(list(line.strip()))


@lru_cache
def traverse(i, j):
    if len(grid) == i+1:
        return 1

    if grid[i+1][j] == '^':
        return traverse(i+1, j+1) + traverse(i+1, j-1)
    else:
        return traverse(i+1, j)


start_i = 0
for i, v in enumerate(grid[0]):
    if v == 'S':
        start_i = i
        break

total = traverse(0, start_i)


print(total)
