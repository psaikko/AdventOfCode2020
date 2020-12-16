lines = [l.strip() for l in open("input", "r").readlines()]

constraints = []
my_ticket = None
nearby_tickets = []

i = 0
while lines[i] != '':
    name, rest = lines[i].split(":")
    first, second = [t.strip() for t in rest.split("or")]
    first = list(map(int, first.split("-")))
    second = list(map(int, second.split("-")))
    constraints.append((name, first, second))
    i += 1

i += 2
my_ticket = list(map(int, lines[i].split(",")))

i += 3
while i < len(lines):
    nearby_tickets.append(list(map(int, lines[i].split(","))))
    i += 1

def check_range(v, r):
    return v >= r[0] and v <= r[1]

def check_constraint(v, c):
    return check_range(v, c[1]) or check_range(v, c[2])

def valid_for_any(v):
    for c in constraints:
        if check_constraint(v, c):
            return True
    return False

def bad_values(ticket):
    return list(filter(lambda v : not valid_for_any(v), ticket))

error_rate = 0
for ticket in nearby_tickets:
    error_rate += sum(bad_values(ticket))

print(error_rate)
            
# filter out tickets with invalid values
nearby_valid_tickets = list(filter(lambda t: not len(bad_values(t)), nearby_tickets))

# Find possible fields for each column
possible_fields = [set() for _ in range(len(my_ticket))]
for i in range(len(my_ticket)):
    vals = [t[i] for t in nearby_valid_tickets]
    for c in constraints:
        if all([check_constraint(v2,c) for v2 in vals]):
            possible_fields[i].add(c[0])


# Propagate singletons
converged = False
while not converged:
    converged = True
    for i in range(len(possible_fields)):
        if len(possible_fields[i]) == 1:
            e = list(possible_fields[i])[0]
            for j in range(len(possible_fields)):
                if i != j and e in possible_fields[j]:
                    possible_fields[j] -= set([e])
                    converged = False

field_names = [list(fields)[0] for fields in possible_fields]

v = 1 
for (name, val) in zip(field_names, my_ticket):
    if "departure" in name:
        v *= val
print(v)