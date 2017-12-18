#!/usr/bin/python3

import sys, re, os

data = sys.stdin.read()

tot = 0
group = 1
canc = False
garbo = False
g = 0
for c in data:
    if canc:
        canc = False
        continue
    if c == '!':
        canc = True
    elif c == '<':
        if garbo:
            g += 1
        garbo = True
    elif c == '>':
        garbo = False
    elif not garbo and c == '{':
        tot += group
        group += 1
    elif not garbo and c == '}':
        group -= 1
    elif garbo:
        g += 1
print(tot)
print(g)
    

