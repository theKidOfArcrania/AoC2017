import sys, os

num = int(input())

last = 0;
l = []
for i in range(2017):
    if i == 0:
        l += [0]
    else:
        last = (last + num) % i + 1
        l.insert(last, i)

print(l[last + 1])
