import re
from collections import Counter
line_tokens = [re.split(r"[-: ]+", line.strip()) for line in open("input", "r").readlines()]
pwd_data = [list(map(int, a[:2])) + a[2:] for a in line_tokens]

n_valid = 0
for (lo, hi, c, pwd) in pwd_data:
    if (pwd[lo-1] == c) ^ (pwd[hi-1] == c):
        n_valid += 1
print(n_valid)