import sys

regs = {}
def reg(x, val = None):
    if val == None:
        if not x in regs:
            return 0
        else:
            return regs[x]
    else:
        regs[x] = val

def vv(s):
    try:
        return int(s)
    except:
        return reg(s)

code = [l[:-1].split(' ') for l in sys.stdin]
snd = 0
off = 0
while True:
    parts = code[off]
    if parts[0] == 'snd':
        snd = vv(parts[1])
    elif parts[0] == 'set':
        reg(parts[1], vv(parts[2]))
    elif parts[0] == 'add':
        reg(parts[1], reg(parts[1]) + vv(parts[2]))
    elif parts[0] == 'mul':
        reg(parts[1], reg(parts[1]) * vv(parts[2]))
    elif parts[0] == 'mod':
        reg(parts[1], reg(parts[1]) % vv(parts[2]))
    elif parts[0] == 'rcv':
        if vv(parts[1]) != 0:
            break
    elif parts[0] == 'jgz':
        if (vv(parts[1]) > 0):
            off += vv(parts[2])
            continue
    off += 1


print(snd)
