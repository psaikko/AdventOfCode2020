lines = [line.strip() for line in open("input", "r").readlines()]

m = 0

seats = set()

for line in lines:
    row = line[:7]
    col = line[-3:]

    row = row.replace('F', '0').replace('B', '1')
    col = col.replace('R', '1').replace('L', '0')

    row = int(row, 2)
    col = int(col, 2)

    i = row * 8 + col
    m = max(i, m)

    seats.add(i)

print("Max:", m)

for s in range(1,m-1):
    if s not in seats and s+1 in seats and s-1 in seats:
        print("Seat:",s)