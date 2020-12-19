lines = [l.strip() for l in open("input","r")]

def parse(line, i):
    start = i
    val = None
    op = None
    print("parsing", line[i:])
    while i < len(line):
        if line[i].isdigit():
            res = int(line[i])
            if val == None:
                val = res
            elif op != None:
                val = eval("%d %s %d" % (val, op, res))
            else:
                print("err")
                exit(1)
            i += 1
        elif line[i] == "(":
            res, i = parse(line,i+1)
            if val == None:
                val = res
            elif op != None:
                val = eval("%d %s %d" % (val, op, res))
            else:
                print("err")
                exit(1)

        if i >= len(line):
            print("1 parsed", line[start:i], "=", val)
            return val, i
        if line[i] == ")":
            print("2 parsed", line[start:i], "=", val)
            return val, i+1
        elif line[i] == "*":
            #res, i = parse(line,i+1)
            #val *= res
            op = "*"
            i += 1
        elif line[i] == "+":
            #res, i = parse(line,i+1)
            #val += res
            op = "+"
            i += 1
    print("3 parsed", line[start:i], "=", val)
    return val, i


s = 0

for line in lines:
    line = line.replace(" ","")
    val, i = parse(line, 0)
    print(val)
    s += val


print(s)