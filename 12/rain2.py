lines = [line.strip() for line in open("input","r")]

x = 0
y = 0

wx = 10
wy = 1

for line in lines:
    cmd = line[0]
    amt = int(line[1:])

    if cmd == 'N':
        wy += amt
    elif cmd == 'S':
        wy -= amt
    elif cmd == 'W':
        wx -= amt
    elif cmd == 'E':
        wx += amt
    elif cmd == 'F':
        x += wx * amt
        y += wy * amt
    elif cmd == 'R':
        while amt > 0:
            amt -= 90
            wx, wy = wy, -wx
    elif cmd == 'L':
        while amt > 0:
            amt -= 90
            wx, wy = -wy, wx

print(abs(x)+abs(y))