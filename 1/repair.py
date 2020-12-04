a = list(int(l.strip()) for l in open("input", 'r').readlines())
print([v1 * v2 for v1 in a for v2 in a if v1 + v2 == 2020])