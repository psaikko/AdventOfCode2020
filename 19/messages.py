lines = [l.strip() for l in open("test2","r")]

rules = dict()

rule_strings = dict()

def make_and_rule(part_rule_idxs,name):
    def _rule(s, i):
        print(i, s[i], "and:", name)
        for idx in part_rule_idxs:
            rule = rules[idx]
            (match, i) = rule(s, i)
            if not match:
                return (False, i)
        return (True, i)
    return _rule

def make_or_rule(part_rules,name):
    def _rule(s, i):
        print(i, s[i], "or:", name)
        for rule in part_rules:
            (match, j) = rule(s, i)
            if match:
                return (True, j)
        return (False, i)
    return _rule

def make_char_rule(c):
    def _rule(s, i):
        print(i, s[i], c)
        return (s[i] == c, i+1)
    return _rule

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

matches = 0
for message in lines[1:]:
    match, l = rules[0](message, 0)
    if match and l == len(message):
        matches += 1
print(matches)