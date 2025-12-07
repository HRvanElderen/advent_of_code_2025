
equations = []

with open("input", "r") as f:
    for line in f.readlines():
        l = []
        for i in line:
            if i != "\n":
                l.append(i)
        equations.append(l)

pivot = list(map(list, zip(*equations[:-1])))
operators = equations[-1]

ops = []
for i in operators:
    if i != ' ':
        ops.append(i)

# combine pivoted strings into numbers
equations = []
eq = []
for part in pivot:
    print(part)
    number = ("".join(part)).strip()
    if len(number) > 0:
        eq.append(number)
    else:
        equations.append(eq)
        eq = []
equations.append(eq)

# execute equations
total = 0
for i, op in enumerate(ops):
    eq = equations[i]
    total += eval(op.join(eq))

print(total)
