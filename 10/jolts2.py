lines = [int(l.strip()) for l in open("input","r")]

jolts = sorted(lines) 
output = max(jolts)

mem = dict()
jset = set(jolts)

def ways(v):
    if v < 0: return 0
    if v == 0: return 1
    if v not in jset: return 0
    if v in mem: return mem[v]

    res = ways(v-3) + ways(v-2) + ways(v-1)
    mem[v] = res
    return res

print(ways(output))