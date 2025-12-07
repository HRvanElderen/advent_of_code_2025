input_file = "input"

neighbours = [(-1, 0), (1, 0), (0, -1), (0, 1),
              (1, 1), (-1, -1), (1, -1), (-1, 1)]


def roll_count(grid, ri, ci):
    row_len = len(grid)
    col_len = len(grid[0])

    rolls = 0
    for dx, dy in neighbours:
        x, y = ri+dx, ci+dy
        if row_len > x >= 0 and col_len > y >= 0 and grid[x][y] == '@':
            rolls += 1

    return rolls


grid = []
with open(input_file, "r") as f:
    for line in f.readlines():
        row = []
        for n in line:
            if n == '\n':
                continue
            row.append(n)
        grid.append(row)


total = 0
for ri, row in enumerate(grid):
    for ci, item in enumerate(row):
        if item == '.':
            continue
        elif roll_count(grid, ri, ci) < 4:
            total += 1

print(grid)
print(total)
