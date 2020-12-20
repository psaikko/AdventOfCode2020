from math import sqrt
from operator import add
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

n = len(tile_data)
puzzle_w, puzzle_h = int(sqrt(n)), int(sqrt(n))
print(puzzle_h, puzzle_w)

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

# for tid in tile_edges:
#     print(tid)
#     print(tile_edges[tid])

def rot(edges):
    return {
        'top': ''.join(reversed(edges['left'])),
        'right': edges['top'],
        'bottom': ''.join(reversed(edges['right'])),
        'left': edges['bottom']
    }

def flip(edges):
    return {
        'top': ''.join(reversed(edges['top'])),
        'right': edges['left'],
        'bottom': ''.join(reversed(edges['bottom'])),
        'left': edges['right']
    }

def rot_grid(lines):
    return list(map(list,zip(*lines[::-1])))

def flip_grid(lines):
    return [line[::-1] for line in lines]

transformations = [
    lambda x: x,
    lambda x: rot(x),
    lambda x: rot(rot(x)),
    lambda x: rot(rot(rot(x))),
    lambda x: flip(x),
    lambda x: rot(flip(x)),
    lambda x: rot(rot(flip(x))),
    lambda x: rot(rot(rot(flip(x))))
]

grid_transformations = [
    lambda x: x,
    lambda x: rot_grid(x),
    lambda x: rot_grid(rot_grid(x)),
    lambda x: rot_grid(rot_grid(rot_grid(x))),
    lambda x: flip_grid(x),
    lambda x: rot_grid(flip_grid(x)),
    lambda x: rot_grid(rot_grid(flip_grid(x))),
    lambda x: rot_grid(rot_grid(rot_grid(flip_grid(x))))
]

# e = tile_edges[list(tile_edges.keys())[0]]
# for t in transformations:
#     print(t(e))

sol_edges = [[None] * puzzle_w for _ in range(puzzle_h)]
sol_orientations = [[-1] * puzzle_w for _ in range(puzzle_h)]
sol_ids = [[-1] * puzzle_w for _ in range(puzzle_h)]

def fill(partial_edges, partial_orientations, partial_ids, free_pieces):
    for y in range(puzzle_h):
        for x in range(puzzle_w):
            if partial_edges[y][x] == None:
                for tid in free_pieces:
                    for i, rf in enumerate(transformations):
                        rotated_edges = rf(tile_edges[tid])

                        # check fit
                        if y > 0:
                            tile_up = partial_edges[y-1][x]
                            if rotated_edges['top'] != tile_up['bottom']:
                                continue
                        if x > 0:
                            tile_left = partial_edges[y][x-1]
                            if rotated_edges['left'] != tile_left['right']:
                                continue

                        # check recursively
                        # print("filling",y,x,"with",tid)
                        partial_edges[y][x] = rotated_edges
                        next_pieces = set(free_pieces)
                        next_pieces.remove(tid)
                        if fill(partial_edges, partial_orientations, partial_ids, next_pieces):
                            partial_orientations[y][x] = i
                            partial_ids[y][x] = tid
                            # print("done")
                            return True
                        # print("removing",y,x)
                        partial_edges[y][x] = None
                # no pieces fit
                return False
    # all squares filled
    return True

fill(sol_edges, sol_orientations, sol_ids, set(tile_data.keys()))

# for line in sol_orientations:
#     print(line)
# for line in sol_edges:
#     print(line)

sol_grids = [[None] * puzzle_w for _ in range(puzzle_h)]
for y in range(puzzle_h):
    for x in range(puzzle_w):
        # apply same transformation to grid that was applied to edges 
        sol_grids[y][x] = grid_transformations[sol_orientations[y][x]](tile_data[sol_ids[y][x]])

        # strip edges
        sol_grids[y][x] = sol_grids[y][x][1:-1]
        sol_grids[y][x] = [line[1:-1] for line in sol_grids[y][x]]

        # print(y,x)
        # print(sol_edges[y][x])
        # for l in sol_grids[y][x]:
        #     print(''.join(l))

grid_h = len(sol_grids[0][0])
grid_w = len(sol_grids[0][0][0])

merged_grid = []
for y in range(puzzle_h):
    for gy in range(grid_h):
        merged_line = reduce(add,[sol_grids[y][x][gy] for x in range(puzzle_w)])
        merged_grid.append(merged_line)

# for l in merged_grid:
#     print(''.join(l))

sea_monster = [
    "                  # ",
    "#    ##    ##    ###",
    " #  #  #  #  #  #   "
]

monster_h = len(sea_monster)
monster_w = len(sea_monster[0])

def check_monster(grid, x, y):
    for my in range(monster_h):
        for mx in range(monster_w):
            if sea_monster[my][mx] == "#" and grid[y+my][x+mx] != "#":
                return False
    return True

base_roughness = sum(sum(1 if c == "#" else 0 for c in l) for l in merged_grid)

# for each orientation
for grid_tf in grid_transformations:
    grid = grid_tf(merged_grid)

    count = 0
    # search for sea monsters!!
    for y in range(len(grid) - monster_h):
        for x in range(len(grid[0]) - monster_w):
            if check_monster(grid, x, y):
                count += 1
    if count:
        print(count)
        for l in grid:
            print(''.join(l))
        print(base_roughness - count * 15)

            

