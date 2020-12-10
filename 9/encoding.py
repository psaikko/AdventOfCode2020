numbers = [int(l.strip()) for l in open("input","r")]

prev25 = set(numbers[:25])

ix = 0

for i in range(25, len(numbers)):

    v = numbers[i]

    ok = False

    # check if v is a sum of two values in prev25
    for n in prev25:
        if v - n in prev25:
            ok = True
            break

    if not ok:
        ix = i
        print(v)
        break

    # slide window forward
    prev25.add(numbers[i])
    prev25.remove(numbers[i-25])

#
# Part 2
#

# compute cumulative sums up to bad index
csums = numbers[:ix]
for i in range(1,len(csums)):
    csums[i] += csums[i - 1]

for i in range(0,len(csums)):
    for j in range(i, len(csums)):
        # find a range that sums to bad value v
        if csums[j] - csums[i] == v:
            #print("range", i+1, j+1)
            print(min(numbers[i+1:j+1])+max(numbers[i+1:j+1]))
            exit(1)
