
equations: list[list[str]] = []

with open("input", "r") as f:
    for line in f.readlines():
        l: list[str] = []
        for i in line:
            if i != "\n":
                l.append(i)
        equations.append(l)

pivot = list(map(list, zip(*equations[:-1])))
operators = equations[-1]

clean_operators: list[str] = []
for i in operators:
    if i != ' ':
        clean_operators.append(i)

# combine pivoted strings into numbers
equations = []
equation: list[str] = []
for part in pivot:
    number = ("".join(part)).strip()
    if len(number) > 0:
        equation.append(number)
    else:
        equations.append(equation)
        equation = []
equations.append(equation)

# execute equations
total = 0
for i, operator in enumerate(clean_operators):
    equation = equations[i]
    total += eval(operator.join(equation))

print(total)
