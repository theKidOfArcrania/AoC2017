import sys

d = {}
for x in sys.stdin:
    p = x.split(': ')
    d[int(p[0])] = int(p[1])

sev = 0
for i in range(max(d.keys()) + 1):
    if (i in d) and (i % ((d[i] - 1) * 2) == 0):
        sev += i * d[i]
print(sev)
