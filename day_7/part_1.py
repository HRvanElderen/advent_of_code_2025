input_file = "input"

grid = []
with open(input_file, "r") as f:
    for line in f.readlines():
        row = []
        for n in line:
            if n == '\n':
                continue
            row.append(n)
        grid.append(row)

print(grid)

total = 0
for i, row in enumerate(grid):
    if len(grid) == i+1:
        continue
    for j, value in enumerate(row):
        if value == '.':
            continue
        if value == 'S' or value == '|':
            if grid[i+1][j] == '^':
                total += 1
                grid[i+1][j+1] = '|'
                grid[i+1][j-1] = '|'
            else:
                grid[i+1][j] = '|'
print(grid)
print(total)
