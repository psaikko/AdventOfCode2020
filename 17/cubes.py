from collections import defaultdict

lines = [list(l.strip()) for l in open("input","r")]

m = defaultdict(int)

for x in range(len(lines[0])):
    for y in range(len(lines)):
        val = 1 if lines[y][x] == "#" else 0
        m[(x,y,0)] = val
        print(val)

print(lines)
print(m)

def neighbors(v):
    ds = [-1,0,1]
    for dx in ds:
        for dy in ds:
            for dz in ds:
                if not (dx == 0 and dy == 0 and dz == 0):
                    yield (v[0]+dx ,v[1]+dy,v[2]+dz)

print(sum(m[n] for n in neighbors((2,2,1))))

for l in lines:
    print("".join(l))

for r in range(1,7):
    print("cycle",r)
    m2 = defaultdict(int)

    ks = list(m.keys())
    for v in ks:
        ns = sum(m[n] for n in neighbors(v))
        if m[v] == 1:
            if (ns == 2 or ns == 3):
                m2[v] = 1

    c = [3,3,0]
    s = 4
    for dx in range(-r-s-1,r+2+s):
        for dy in range(-r-s-1,r+2+s):
            for dz in range(-r,r+1):
                v = (c[0]+dx,c[1]+dy,c[2]+dz)
                if m[v] == 0:
                    ns = sum(m[n] for n in neighbors(v))
                    if ns == 3:
                        m2[v] = 1

    # for dz in range(-r,r+1):
    #     print("z=",c[2]+dz)
    #     for dy in range(-r-1,r+2):
    #         l = ""
    #         for dx in range(-r-1,r+2):
    #             l += str(m2[(c[0]+dx,c[1]+dy,c[2]+dz)])
    #         print(l)
    #     print()
    m = m2

print(sum(m[k] for k in m))