numbers = list(map(int,open("input","r").readlines()[0].strip().split(",")))
print(numbers)

last = dict()

for (i,v) in enumerate(numbers[:-1]):
    last[v] = i

prev = numbers[-1]

for i in range(len(numbers),30000000):
    if prev not in last:
        v = 0
        last[prev] = i - 1
        prev = v
    else:
        v = i - 1 - last[prev]
        last[prev] = i - 1
        prev = v

print(prev)