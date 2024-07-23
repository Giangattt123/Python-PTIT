## PHÂN CHIA NGUYÊN TỐ

from math import *
def checkNT(n):
    if n < 2: return False
    for i in range(2 , isqrt(n) + 1):
        if n % i == 0: return False
    return True

n = int(input())
a = [int(i) for i in input().split()]
b = []
se = set()
for num in a:
    if num not in se:
        b.append(num)
        se.add(num)
print(b)
f = [0] * len(b)
f[0] = b[0]
for i in range(1 , len(b)): f[i] = f[i - 1] + b[i]
check = True
for i in range(len(b)):
    if checkNT(f[i]) and checkNT(f[len(b) - 1] - f[i]):
        check = False
        print(i)
        break
if check: print('NOT FOUND')




