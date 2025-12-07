input_file = "input"

grid: list[list[str]] = []

with open(input_file, "r") as f:
    for line in f:
        grid.append(list(line.strip()))

total = 0
# iterate over the grid and update the beam inplace, count every split.
for row_i, row in enumerate(grid):
    if len(grid) == row_i+1:
        continue
    for col_i, value in enumerate(row):
        if value == 'S' or value == '|':
            if grid[row_i+1][col_i] == '^':
                total += 1
                grid[row_i+1][col_i+1] = '|'
                grid[row_i+1][col_i-1] = '|'
            else:
                grid[row_i+1][col_i] = '|'

print(total)
