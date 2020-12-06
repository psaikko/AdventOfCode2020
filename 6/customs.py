lines = [line for line in open("input", "r")]

groups = []

answers = set()
first = True
for line in lines:    
    if line == "\n":
        groups += [answers]
        answers = set()
        first = True
        continue
    #answers.update(set(line.strip()))
    if first:
        answers = set(line.strip())
        first = False
    else:
        answers.intersection_update(set(line.strip()))

if len(answers): 
    groups += [answers]

print(groups)

print(sum(map(len,groups)))