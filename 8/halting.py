lines = [l.strip().split() for l in open("input","r").readlines()]

i = 0
seen = set()
acc = 0

while i not in seen:
    seen.add(i)
    instr, val_s = lines[i]
    val = int(val_s)

    if instr == "nop":
        i += 1 
        continue
    elif instr == "acc":
        acc += val
        i += 1
    elif instr == "jmp":
        i += val

print(acc)