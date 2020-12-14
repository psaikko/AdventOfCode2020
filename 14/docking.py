lines = [[e.strip() for e in l.split("=")] for l in open("input","r").readlines()]

mem = dict()
zeromask = int("0"*36,2)
onemask = int("1"*36,2)

for cmd, arg in lines:
    if cmd == "mask":
        ones = "".join("1" if c == "1" else "0" for c in arg)
        zeros = "".join("0" if c == "0" else "1" for c in arg)
        zeromask = int(zeros,2)
        onemask = int(ones,2)
    else:
        arg = int(arg)
        arg |= onemask
        arg &= zeromask
        exec("%s = %d" % (cmd, arg))

print(sum(mem[k] for k in mem))
