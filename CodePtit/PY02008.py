## KHOẢNG CÁCH NGUYÊN TỐ

from math import *
def nt(n):
    if n < 2: return False
    for i in range(2 , isqrt(n) + 1):
        if n % i == 0: return False
    return True


prime = [2]
for i in range(3, 10000, 2):
    if nt(i):
        prime.append(i)

n, x = list(map(int, input().split()))
print(x, end = ' ')
for i in range(n):
    print(x + prime[i], end = ' ')
    x = x + prime[i]