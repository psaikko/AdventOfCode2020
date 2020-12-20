from math import sqrt
from collections import defaultdict
from operator import mul
from functools import reduce

tile_data = dict()

with open("input", "r") as file:
    while True:
        l = next(file, None)
        if l == None: break
        
        tile_id = int(l[:-2].split(" ")[1])
        tile_lines = []
        l = next(file, None)
        while l != None and l != "\n":
            tile_lines.append(list(l.strip()))
            l = next(file, None)
        tile_data[tile_id] = tile_lines

tile_edges = dict()
for tid in tile_data:
    tile_lines = tile_data[tid]
    top_edge = ''.join(tile_lines[0])
    right_edge = ''.join(line[-1] for line in tile_lines)
    bottom_edge = ''.join(tile_lines[-1])
    left_edge = ''.join(line[0] for line in tile_lines)
    tile_edges[tid] = {
        'top': top_edge,
        'right': right_edge,
        'bottom': bottom_edge,
        'left': left_edge
    }

edge_counts = defaultdict(int)

def canon(e):
    l = [e, ''.join(reversed(e))]
    s = list(sorted(l))
    return s[0]

for tid in tile_edges:
    edges = tile_edges[tid].values()
    for e in edges:
        edge_counts[canon(e)] += 1

corner_ids = []
for tid in tile_edges:
    uniq = [1 for e in tile_edges[tid].values() if edge_counts[canon(e)] == 1]
    if len(uniq) == 2:
        corner_ids.append(tid)

print(reduce(mul,corner_ids))