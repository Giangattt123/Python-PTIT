## SẮP XẾP NGUYÊN TỐ

from math import *
def nt(n):
    if n < 2: return False
    for i in range(2 , isqrt(n) + 1):
        if n % i == 0: return False
    return True

n = int(input())
a = list(map(int , input().split()))
b , c = [] , []
for i in range(n):
    if nt(a[i]):
        b.append(a[i])
        c.append(i)
b.sort()
for i in range(len(c)):
    a[c[i]] = b[i]
for i in a:
    print(i , end = " ")