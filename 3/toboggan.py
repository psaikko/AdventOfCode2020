TREE = '#'
OPEN = '.'
rows = [line.strip() for line in open("input", "r").readlines()]
height = len(rows)
width = len(rows[0])

x = 0
y = 0

dx = 3
dy = 1

n_trees = 0

while y < height:
    if rows[y][x] == TREE:
        n_trees += 1

    y += dy
    x = (x + dx) % width

print(n_trees)
