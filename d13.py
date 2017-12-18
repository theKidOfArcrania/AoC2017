import sys

d = {}
for x in sys.stdin:
    p = x.split(': ')
    d[int(p[0])] = int(p[1])

nums = max(d.keys()) + 1
dl = 0
while True:
    hit = False
    sev = 0
    for i in range(nums):
        if (i in d) and ((i + dl) % ((d[i] - 1) * 2) == 0):
            break
    else:
        break
    dl += 1
print(dl)
