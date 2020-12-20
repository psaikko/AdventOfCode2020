lines = [l.strip() for l in open("input","r")]

rules = dict()

rule_strings = dict()

def make_and_rule(part_rule_idxs,name):
    def _rule(s, i):
        if i >= len(s): return
        # print(i, s[i], "and:", name)
        matches = [i]
        for idx in part_rule_idxs:
            next_matches = []
            for j in matches:
                next_matches += list(rules[idx](s,j))
            matches = next_matches
        for j in matches:
            yield j
    return _rule

def make_or_rule(part_rules, name):
    def _rule(s, i):
        if i >= len(s): return
        # print(i, s[i], "or:", name)
        for rule in part_rules:
            yield from rule(s, i)
    return _rule

def make_char_rule(c):
    def _rule(s, i):
        if i >= len(s): return
        # print(i, s[i], c)
        if s[i] == c:
            yield i+1
    return _rule

max_depth = 10

def rule_8(s, j):
    or_parts = []
    for i in range(1,max_depth+1):
        idxs = [42] * i
        or_parts.append(make_and_rule(idxs, " ".join(map(str,idxs))))
    yield from make_or_rule(or_parts,"Rule 8")(s, j)

def rule_11(s, j):
    or_parts = []
    for i in range(1,max_depth+1):
        idxs = ([42] * i) + ([31] * i)
        or_parts.append(make_and_rule(idxs, " ".join(map(str,idxs))))
    yield from make_or_rule(or_parts,"Rule 11")(s, j)

while lines[0] != "":
    line, lines = lines[0], lines[1:]
    idx, body = line.split(":")
    rule_strings[idx] = body
    idx = int(idx)
    body = body.strip()
    rule = None
    if body[0] == '"':
        c = body[1]
        rule = make_char_rule(c)
    else:
        parts = [list(map(int, s.split())) for s in body.split("|")]
        part_rules = []
        for part in parts:
            part_rules.append(make_and_rule(part, " ".join(map(str,part))))
        rule = make_or_rule(part_rules, body)
    rules[idx] = rule

rules[8] = rule_8
rules[11] = rule_11

count = 0
for message in lines[1:]:
    matches = rules[0](message, 0)
    for match in matches:
        if match == len(message):
            count += 1
print(count)