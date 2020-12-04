a = list(int(l.strip()) for l in open("input", 'r').readlines())
n = len(a)

for i in range(n):
    for j in range(i+1,n):
        if a[i] + a[j] < 2020:
            for k in range(j+1,n):
                if a[i] + a[j] + a[k] == 2020:
                    print(a[i] * a[j] * a[k])


