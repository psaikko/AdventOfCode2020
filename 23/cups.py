# # test
# order_s = 389125467

# input
order_s = 327465189

order = list(map(int, str(order_s)))

moves = 100
current = order[0]

def print_state(current, order):
    print("cups: ",end="")
    for cup in order:
        if cup == current:
            print("(%d)" % cup,end="")
        else:
            print(" %d " % cup,end="")
    print()

for i in range(moves):
    print("-- move %d --" % (i+1))
    print_state(current, order)
    ci = order.index(current)
    pickup = (order + order)[ci+1:ci+4]
    print("pick up:", ", ".join(map(str,pickup)))

    dest = current - 1
    if dest == 0: dest += 9
    while dest in pickup:
        dest -= 1
        if dest == 0: dest += 9

    print("destination:", dest)
    print()

    for x in pickup:
        order.remove(x)

    di = order.index(dest)
    order = order[:di+1] + pickup + order[di+1:]
    current = order[((order+order).index(current)+1)%len(order)]

i = order.index(1)
order = order[i+1:]+order[:i]
print("".join(map(str,order)))