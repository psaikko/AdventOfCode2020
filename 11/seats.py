from collections import Counter

grid = [list(l.strip()) for l in open("input","r").readlines()]

H = len(grid)
W = len(grid[0])

def adjp(y,x):
    if y > 0 and x > 0:
        yield (y-1,x-1)
    if y > 0:
        yield (y-1,x)
    if y > 0 and x < W-1:
        yield (y-1,x+1)
    if y < H-1 and x > 0:
        yield (y+1, x-1)
    if y < H-1:
        yield (y+1, x)
    if y < H-1 and x < W-1:
        yield (y+1,x+1)
    if x > 0:
        yield (y, x-1)
    if x < W-1:
        yield (y, x+1)

def adjc(g,y,x):
    for y_, x_ in adjp(y,x):
        yield g[y_][x_]

newgrid = [grid[y][:] for y in range(H)]

while True:

    change = False

    for y in range(H):
        for x in range(W):
            if grid[y][x] == '.':
                newgrid[y][x] = grid[y][x]
                pass
            ct = Counter(adjc(grid,y,x))
            if grid[y][x] == 'L' and ct['#'] == 0:
                change = True
                newgrid[y][x] = "#"
            elif grid[y][x] == '#' and ct['#'] >= 4:
                change = True
                newgrid[y][x] = "L"
            else:
                newgrid[y][x] = grid[y][x]


    if not change: break

    #for l in [''.join(l) for l in newgrid]: print(l)

    grid, newgrid = newgrid, grid
    
print(sum(sum(c == "#" for c in l) for l in grid))