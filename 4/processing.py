lines = [line for line in open("input", "r")]

passports = []

fields = dict()
for line in lines:    
    if line == "\n":
        passports += [fields]
        fields = dict()
        continue
    fields.update({pair.split(":")[0] : pair.split(":")[1] for pair in line.strip().split()})

if len(fields): 
    passports += [fields]

def check(p):
    return (len(p) == 7 and "cid" not in p) or len(p) == 8
    
print(sum(check(p) for p in passports))
