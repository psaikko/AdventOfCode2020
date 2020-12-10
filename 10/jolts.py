lines = [int(l.strip()) for l in open("input","r")]

jolts = [0] + sorted(lines)

diffs = [0,0,0,0]

for a,b in zip(jolts[:-1],jolts[1:]):
    diffs[b-a] += 1

diffs[3] += 1


print(diffs[1]*diffs[3])