import sys, re

regs = {}

conds = {'>': lambda a, b: a > b, 
        '<': lambda a, b: a < b,
        '>=': lambda a, b: a >= b,
        '<=': lambda a, b: a <= b,
        '==': lambda a, b: a == b,
        '!=': lambda a, b: a != b}

maxStore = 0
def reg(r, val = None):
    global maxStore
    if val == None:
        if r in regs:
            return regs[r]
        else:
            regs[r] = 0
            return regs[r]
    else:
        regs[r] = val
        maxStore = max(val, maxStore)

for x in sys.stdin:
    l = x.split(' ')
    if len(l) == 1:
        break
    if conds[l[5]](reg(l[4]), int(l[6])):
        if l[1] == 'inc':
            reg(l[0], reg(l[0]) + int(l[2]))
        else:
            reg(l[0], reg(l[0]) - int(l[2]))

print(max(regs.values()))
print(maxStore)
