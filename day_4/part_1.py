input_file = "input"

neighbours = [(-1, 0), (1, 0), (0, -1), (0, 1),
              (1, 1), (-1, -1), (1, -1), (-1, 1)]


def roll_count(grid: list[list[str]], row_i: int, col_i: int):
    row_len = len(grid)
    col_len = len(grid[0])

    rolls = 0
    for dx, dy in neighbours:
        x, y = row_i+dx, col_i+dy
        if row_len > x >= 0 and col_len > y >= 0 and grid[x][y] == '@':
            rolls += 1

    return rolls


grid: list[list[str]] = []

with open(input_file, "r") as f:
    for line in f:
        grid.append(list(line.strip()))


total = 0
for row_i, row in enumerate(grid):
    for col_i, item in enumerate(row):
        if item == '@' and roll_count(grid, row_i, col_i) < 4:
            total += 1

print(total)
