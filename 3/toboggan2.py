TREE = '#'
OPEN = '.'
rows = [line.strip() for line in open("input", "r").readlines()]
height = len(rows)
width = len(rows[0])

slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]

prod = 1

for (dx, dy) in slopes:
    x = 0
    y = 0 
    n_trees = 0
    while y < height:
        if rows[y][x] == TREE:
            n_trees += 1

        y += dy
        x = (x + dx) % width
    prod *= n_trees

print(prod)