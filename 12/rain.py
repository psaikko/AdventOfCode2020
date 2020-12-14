lines = [line.strip() for line in open("input","r")]

x = 0
y = 0

r = 90


for line in lines:
    cmd = line[0]
    amt = int(line[1:])

    if cmd == 'N':
        y += amt
    elif cmd == 'S':
        y -= amt
    elif cmd == 'W':
        x -= amt
    elif cmd == 'E':
        x += amt
    elif cmd == 'F':
        while r < 0:
            r += 360
        if r >= 360:
            r %= 360

        if r % 360 == 90:
            x += amt
        elif r % 360  == 180:
            y -= amt
        elif r % 360 == 270:
            x -= amt
        elif r == 0:
            y += amt
    elif cmd == 'R':
        r += amt
    elif cmd == 'L':
        r -= amt

print(abs(x)+abs(y))