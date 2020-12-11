from collections import Counter

grid = [list(l.strip()) for l in open("input","r").readlines()]

H = len(grid)
W = len(grid[0])

def inbounds(y,x):
    return y >= 0 and x >= 0 and y < H and x < W

def look(g,y,x,dy,dx):
    y_, x_ = y+dy, x+dx
    while inbounds(y_, x_) and g[y_][x_] == '.':
        y_ += dy
        x_ += dx
    if inbounds(y_, x_):
        return (y_, x_)
    else:
        return None

def adjp(g,y,x):
    if inbounds(y-1,x-1):
        p = look(g,y,x,-1,-1)
        if p: yield p
    if inbounds(y-1,x):
        p = look(g,y,x,-1,0)
        if p: yield p
    if inbounds(y-1,x+1):
        p = look(g,y,x,-1,1)
        if p: yield p
    if inbounds(y+1,x-1):
        p = look(g,y,x,1,-1)
        if p: yield p
    if inbounds(y+1,x):
        p = look(g,y,x,1,0)
        if p: yield p
    if inbounds(y+1,x+1):
        p = look(g,y,x,1,1)
        if p: yield p
    if inbounds(y,x-1):
        p = look(g,y,x,0,-1)
        if p: yield p
    if inbounds(y,x+1):
        p = look(g,y,x,0,1)
        if p: yield p

mem = dict()
def adjc(g,y,x):
    if (y,x) in mem: return [g[y_][x_] for (y_,x_) in mem[(y,x)]]
    n = list(adjp(g,y,x))
    mem[(y,x)] = n
    return [g[y_][x_] for (y_,x_) in n]

newgrid = [grid[y][:] for y in range(H)]

while True:

    change = False

    for y in range(H):
        for x in range(W):
            if grid[y][x] == '.':
                newgrid[y][x] = grid[y][x]
                pass
            ct = Counter(adjc(grid,y,x))
            #print(ct)
            if grid[y][x] == 'L' and ct['#'] == 0:
                change = True
                newgrid[y][x] = "#"
            elif grid[y][x] == '#' and ct['#'] >= 5:
                change = True
                newgrid[y][x] = "L"
            else:
                newgrid[y][x] = grid[y][x]


    if not change: break

    # for l in [''.join(l) for l in newgrid]: print(l)

    grid, newgrid = newgrid, grid
    
print(sum(sum(c == "#" for c in l) for l in grid))