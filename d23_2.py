def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False

    return True

a = 1
b = int(input()) # Number of first assignment
c = b
if a != 0:
    b = b * 100 + 100000
    c = b + 17000

h = 0
while True:
    f = 1
    if not isPrime(b):
        h += 1
    if b != c:
        b += 17
    else:
        break

print(h)
