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

floor = defaultdict(bool)
ref = (0,0)

for seq in seqs:
    pos = list(ref)
    for ds in seq:
        d = dir_map[ds]
        pos[0] += d[0]
        pos[1] += d[1]
    floor[tuple(pos)] = not floor[tuple(pos)]

ct = 0
for pos in floor:
    if floor[pos]:
        ct += 1
print(ct)

def get_neighbours(pos):
    x, y = pos
    for d in dir_map.values():
        dx, dy = d
        yield (x+dx, y+dy)

def get_frontier(floor):
    black_tiles = {k for k in floor if floor[k]}
    neighbours = {n for t in black_tiles for n in get_neighbours(t)}
    return black_tiles.union(neighbours)

def n_adjacent_black_tiles(floor, pos):
    return sum(floor[p] for p in get_neighbours(pos))

for i in range(100):
    new_floor = defaultdict(bool)
    tiles = get_frontier(floor)
    for tile in tiles:
        adj = n_adjacent_black_tiles(floor, tile)
        if floor[tile] and adj == 0 or adj > 2:
            new_floor[tile] = False
        elif adj == 2:
            new_floor[tile] = True
        else:
            new_floor[tile] = floor[tile]

    new_floor, floor = floor, new_floor

    ct = 0
    for pos in floor:
        if floor[pos]:
            ct += 1
    print(i+1, ct)

