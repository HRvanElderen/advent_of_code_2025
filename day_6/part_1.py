
equations = []

with open("input", "r") as f:
    for line in f.readlines():
        parts = line.split()
        # for p in parts:
        equations.append(parts)

print(equations)

operators = equations[-1]
numbers = equations[:-1]
print(numbers)

total = 0
for i in range(len(numbers[0])):
    eq = ''
    op = operators[i]
    for j in range(len(numbers)):
        eq += numbers[j][i]
        if j != len(numbers)-1:
            eq += op
    print(eq)
    total += eval(eq)

print(total)
