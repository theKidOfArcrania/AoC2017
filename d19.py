import sys

grid = list(sys.stdin)
rows = len(grid)
cols = len(grid[0])

def at(pt):
    return grid[pt[0]][pt[1]]

def incr(pt, d):
    i = (-1, 1)[d[1]]
    if d[0]:
        return (pt[0] + i, pt[1])
    else:
        return (pt[0], pt[1] + i)

pt = None
for i in range(cols):
    if grid[0][i] == '|':
        pt = (0, i)
        break

steps = 0
s = ''
d = (True, True) # is vertical, is going in positive direction
while True:
    x = at(pt)
    if x == ' ':
        break
    elif x == '+':
        d = (not d[0], at(incr(pt, (not d[0], True))) != ' ')
    elif x != '-' and x != '|':
        s += x
    pt = incr(pt, d)
    steps += 1

print(s)
print(steps)

