lines = [[e.strip() for e in l.split("=")] for l in open("input","r").readlines()]

mem = dict()
zeromask = int("0"*36,2)
onemask = int("1"*36,2)

def generate_floats(prefix, addr, mask):
    if len(addr) == 0: 
        yield prefix
    elif mask[0] == "X":
        yield from generate_floats(prefix + "1", addr[1:], mask[1:])
        yield from generate_floats(prefix + "0", addr[1:], mask[1:])
    else:
        yield from generate_floats(prefix + addr[0], addr[1:], mask[1:])

def apply_mask(addr, mask):
    # convert to binary, apply padding
    addr_str = bin(addr)[2:]
    addr_str = "0"*(36-len(addr_str)) + addr_str
    # apply masked 1-bits
    addr_str = list(addr_str)
    for i,v in enumerate(mask):
        if v == "1":
            addr_str[i] = "1"
    addr_str = "".join(addr_str)
    # generate floating bit combinations
    return generate_floats("",addr_str,mask)

for cmd, arg in lines:
    if cmd == "mask":
        mask = arg
    else:
        addr = int(cmd[4:-1])
        for a in apply_mask(addr, mask):
            mem[a] = int(arg)

print(sum(mem[k] for k in mem))
