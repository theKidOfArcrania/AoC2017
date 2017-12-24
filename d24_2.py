import sys

def better(x, y):
    if x[1] == y[1]:
        return (max(x[0], y[0]), y[1])
    elif x[1] > y[1]:
        return x
    else:
        return y

def best(conn, used, bridges, poss, z, y):
    val = [z, y]
    for ind in poss[conn]:
        x = bridges[ind]
        strength = x[0] + x[1]
        if not used[ind]:
            cpy = used[::]
            cpy[ind] = True
            val = better(val, 
                    best(strength - conn, cpy, bridges, poss, z + strength, y + 1))
    return val

poss = {}
bridges = []

ind = 0
for li in sys.stdin:
    li = li[:-1]
    b = tuple(map(int, li.split('/')))
    if not b[0] in poss:
        poss[b[0]] = []
    poss[b[0]] += [ind]
    if not b[1] in poss:
        poss[b[1]] = []
    poss[b[1]] += [ind]
    bridges += [b]
    ind += 1

print(poss)
used = [False for x in bridges]
print(best(0, used, bridges, poss, 0, 0))
