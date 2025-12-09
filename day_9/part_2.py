input_file = "input"


def surface_area(point_a, point_b):
    return abs(point_a[0] - point_b[0] + 1) * abs(point_a[1] - point_b[1] + 1)


points = []
with open(input_file, "r") as f:
    for line in f:
        point = list(map(int, line.strip().split(",")))
        points.append(point)

print(points)
max_size = 0
for point_1 in points:
    for point_2 in points:
        if point_1 != point_2:
            size = surface_area(point_1, point_2)
            if size > max_size:
                max_size = size

print(max_size)
