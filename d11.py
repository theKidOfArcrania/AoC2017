import sys
from functools import reduce
from sys import stdin

def dist(x, y):
    if (x < 0) != (y < 0):
        return max(abs(x), abs(y))
    else:
        return abs(x) + abs(y)

dirs = {'n': (1, -1), 's': (-1, 1), 'nw': (0, -1), 'se': (0, 1), 'sw': (-1, 0),
        'ne': (1, 0)}

mdist = 0
x = 0
y = 0
for m in input().split(','):
    m = dirs[m]
    x += m[0]
    y += m[1]
    mdist = max(dist(x, y), mdist)

print(x, y)
print(dist(x, y))
print(mdist)
