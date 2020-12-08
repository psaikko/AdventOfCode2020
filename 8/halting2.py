lines = [l.strip().split() for l in open("input","r").readlines()]

for j in range(len(lines)):

    if lines[j][0] == "acc":
        continue

    i = 0
    seen = set()
    acc = 0

    while i not in seen:
        if i == len(lines):
            print("Terminated, acc =", acc)
            exit(1)
        if i > len(lines):
            break

        seen.add(i)
        instr, val_s = lines[i]
        if i == j and instr == "nop":
            instr = "jmp"
        elif i == j and instr == "jmp":
            instr = "nop"

        val = int(val_s)

        if instr == "nop":
            i += 1 
            continue
        elif instr == "acc":
            acc += val
            i += 1
        elif instr == "jmp":
            i += val