import sys, os

MOD = 2**31-1
a = int(input())
b = int(input())

pairs = 0
for i in range(5000000):
    a = (a * 16807) % MOD
    b = (b * 48271) % MOD
    while (a & 3) != 0:
        a = (a * 16807) % MOD
    while (b & 7) != 0:
        b = (b * 48271) % MOD
    if a & 0xFFFF == b & 0xFFFF:
        pairs += 1

print(pairs)
