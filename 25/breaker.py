door_key = 10705932
card_key = 12301431

# # Test data
# door_key = 17807724
# card_key = 5764801

sn = 7

M = 20201227

def find_loop_number(key):
    loop = 0
    t = 1
    while t != key:
        t *= sn
        t %= M
        loop += 1
    return loop

door_loop = find_loop_number(door_key)
card_loop = find_loop_number(card_key)

print(card_loop, door_loop)

enc_key = 1
for l in range(card_loop):
    enc_key *= door_key
    enc_key %= M

print(enc_key)
