lines = [line.strip() for line in open("input","r")]
buses = lines[1].split(",")

pairs = []
for i,b in enumerate(buses):
    if b != 'x':
        b = int(b)
        pairs += [(b, i)]

pairs = sorted(pairs)[::-1]

print(pairs)

pre = 3

skip = 1
for m,_ in pairs[:pre]:
    skip *= m

start = 0
while start < skip:
    start += 1
    ok = True
    for m, r in pairs[:pre]:
        if start % m != (m - r) % m:
            ok = False
            break
    if ok:
        break

k = start
z = 0

while True:
    k += skip
    ok = True
    for m, r in pairs[pre:]:
        if k % m != (m - r) % m:
            ok = False
            break
    if ok:
        print("timestamp:",k)
        break
