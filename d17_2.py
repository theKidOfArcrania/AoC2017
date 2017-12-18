import sys, os

num = int(input())

last = 0;
val = 0
for i in range(50000000):
    if i == 0:
        last = 0
    else:
        last = (last + num) % i + 1
    if last == 1:
        val = i

print(val)
