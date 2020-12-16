lines = [line.strip() for line in open("input","r")]

ts = int(lines[0])
buses = lines[1].split(",")

mm = float('inf')
mn = None

for b in buses:
    if b != "x":
        if -ts % int(b) < mm:
            mm = -ts % int(b)
            mb = int(b)

print(mb*mm)