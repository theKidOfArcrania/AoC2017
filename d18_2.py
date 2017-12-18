import sys

regs = [{'p': 0},{'p': 1}]
def reg(pg, x, val = None):
    if val == None:
        xx = regs[pg]
        if not x in xx:
            return 0
        else:
            return regs[pg][x]
    else:
        regs[pg][x] = val

def vv(pg, s):
    try:
        return int(s)
    except:
        return reg(pg, s)

def inv(pg):
    return (1,0)[pg]

values = [[],[]]
code = [l[:-1].split(' ') for l in sys.stdin]
off = [0,0]
pg = 0
waiting = [False, False]

snd = 0
while True:
    waiting[pg] = False
    parts = code[off[pg]]
    if parts[0] == 'snd':
        values[inv(pg)] += [vv(pg, parts[1])]
        if pg == 1:
            snd += 1
    elif parts[0] == 'set':
        reg(pg, parts[1], vv(pg, parts[2]))
    elif parts[0] == 'add':
        reg(pg, parts[1], reg(pg, parts[1]) + vv(pg, parts[2]))
    elif parts[0] == 'mul':
        reg(pg, parts[1], reg(pg, parts[1]) * vv(pg, parts[2]))
    elif parts[0] == 'mod':
        reg(pg, parts[1], reg(pg, parts[1]) % vv(pg, parts[2]))
    elif parts[0] == 'rcv':
        if len(values[pg]) > 0:
            reg(pg, parts[1], values[pg][0])
            values[pg] = values[pg][1:]
        elif waiting[inv(pg)] and len(values[inv(pg)]) == 0:
            break
        else:
            waiting[pg] = True
            pg = inv(pg)
            continue
    elif parts[0] == 'jgz':
        if (vv(pg, parts[1]) > 0):
            off[pg] += vv(pg, parts[2])
            continue
    off[pg] += 1

print(snd)
