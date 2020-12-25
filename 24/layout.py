from collections import defaultdict

lines = open("input","r").readlines()

dir_map = {
    "e": (1,0),
    "se": (0,-1),
    "sw": (-1,-1),
    "w": (-1,0),
    "ne": (1,1),
    "nw": (0,1)
}

seqs = []

for line in lines:
    line = line.strip()
    i = 0
    seq = []
    while i < len(line):
        c = line[i]
        if c == "e" or c == "w":
            seq.append(c)
            i += 1
        else:
            seq.append(line[i:i+2])
            i += 2
    seqs.append(seq)

floor = defaultdict(int)
ref = (0,0)

for seq in seqs:
    pos = list(ref)
    for ds in seq:
        d = dir_map[ds]
        pos[0] += d[0]
        pos[1] += d[1]
    floor[tuple(pos)] += 1

ct = 0
for pos in floor:
    if floor[pos] % 2 == 1:
        ct += 1
print(ct)