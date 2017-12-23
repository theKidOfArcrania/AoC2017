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

off = 0
code = [l[:-1].split(' ') for l in sys.stdin]
mulTimes = 0
while off < len(code):
    parts = code[off]
    print(code[off])
    if parts[0] == 'set':
        reg(parts[1], vv(parts[2]))
    elif parts[0] == 'mul':
        reg(parts[1], reg(parts[1]) * vv(parts[2]))
        mulTimes += 1
    elif parts[0] == 'sub':
        reg(parts[1], reg(parts[1]) - vv(parts[2]))
    elif parts[0] == 'jnz':
        if (vv(parts[1]) != 0):
            off += vv(parts[2])
            continue
    off += 1


print(mulTimes)
