# # test
# order_s = 389125467

# input
order_s = 327465189

max_cup = 1000000
moves   = 10000000

order = list(map(int, str(order_s)))
order += list(range(10,max_cup+1))

next_arr = [0] * (max_cup+1)
for i in range(len(order)):
    next_arr[order[i]] = order[(i+1)%max_cup]
current = order[0]

for i in range(moves):
    pickups = []
    n = current
    for i in range(3):
        n = next_arr[n]
        pickups += [n]

    dest = current - 1
    if dest == 0:
        dest += max_cup
    while dest in pickups:
        dest -= 1
        if dest == 0:
            dest += max_cup

    dest_end = next_arr[dest]

    next_arr[current] = next_arr[pickups[2]]
    next_arr[dest] = pickups[0]
    next_arr[pickups[2]] = dest_end
    
    current = next_arr[current]

v1 = next_arr[1]
v2 = next_arr[v1]

print(v1*v2)
