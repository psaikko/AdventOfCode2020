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

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.

required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

def intbounds(s, lo, hi):
    return int(s) >= lo and int(s) <= hi

def valid(p):
    for field in required_fields: 
        if field not in p: return False

    if not intbounds(p["byr"], 1920, 2002): return False

    if not intbounds(p["iyr"], 2010, 2020): return False

    if not intbounds(p["eyr"], 2020, 2030): return False

    if not p["hgt"][:-2].isnumeric(): return False

    if p["hgt"][-2:] == "cm":
        if not intbounds(p["hgt"][:-2], 150, 193): return False
    else:
        if not intbounds(p["hgt"][:-2], 59, 76): return False

    if len(p["hcl"]) != 7: return False
    for c in p["hcl"][1:]:
        if c not in ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]:
            return False

    if p["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return False

    if len(p["pid"]) != 9: return False
    if not p["pid"].isnumeric(): return False

    return True

print(sum(map(valid, passports)))