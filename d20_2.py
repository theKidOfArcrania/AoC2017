import sys, os



class Part:
    def __init__(s, p, v, a):
        s.p = p
        s.v = v
        s.a = a

    def step(s):
        s.v = [s.v[i] + s.a[i] for i in range(3)]
        s.p = [s.v[i] + s.p[i] for i in range(3)]
        return abs(s.p[0]) + abs(s.p[1]) + abs(s.p[2])

def parse(vec):
    vec = vec[3:-1]
    return [int(i) for i in vec.split(',')]

parts = []
for li in sys.stdin:
    prt = li[:-1].split(', ')
    parts += [Part(parse(prt[0]), parse(prt[1]), parse(prt[2]))]

best = 0
while True:
    locs = {} 
    removing = {}
    for i in range(len(parts)):
        parts[i].step()
        x = tuple(parts[i].p)
        if x in locs:
            removing[i] = True
            removing[locs[x]] = True
        locs[x] = i
    for i in range(len(parts) - 1, -1, -1):
        if i in removing:
            del parts[i]

    print(len(parts))

    
