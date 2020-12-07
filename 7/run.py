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
    adj[src] = dst_names

closures = dict()

for bag in adj:
    closures[bag] = set()
    q = adj[bag]

    while len(q):
        n, q = q[0], q[1:]

        if n not in closures[bag]:
            closures[bag].add(n)
            q += adj[n]

print(sum("shiny gold" in v for v in closures.values()))
