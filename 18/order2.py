from operator import mul
from functools import reduce

lines = [l.strip() for l in open("input","r")]

def parse(line, i):
    start = i
    stack = []
    op = None

    while i < len(line):
        if line[i].isdigit():
            res, i = int(line[i]), i+1
        elif line[i] == "(":
            res, i = parse(line,i+1)
        else:
            print("err")
            exit(1)

        stack.append(res)

        if op == "+":
            stack, (a, b) = stack[:-2], stack[-2:]
            stack.append(a+b)

        if i >= len(line):
            break
        if line[i] == ")":
            i += 1
            break

        op = line[i]
        i += 1

    val = reduce(mul,stack)
    print("parsed", line[start:i], "=", val)
    return val, i


s = 0

for line in lines:
    line = line.replace(" ","")
    val, i = parse(line, 0)
    print(val)
    s += val


print(s)