lines = [line.strip() for line in open("input", "r")]

adj = dict()

for line in lines:
    s = line.split("contain")
    src = s[0].split("bag")[0].strip()

    if "other" in s[1]:
        adj[src] = []
        continue

    dst = [x.split("bag")[0].strip() for x in s[1].split(",")]
    dst_names = [" ".join(s.split()[1:]) for s in dst]
    dst_amts = [int(s.split()[0]) for s in dst]
    adj[src] = list(zip(dst_names, dst_amts))

def count(bagname):
    c = 1
    for name, amount in adj[bagname]:
        c += amount * count(name)
    return c

print(count("shiny gold")-1)