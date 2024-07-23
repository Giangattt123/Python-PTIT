## ƯỚC SỐ CHUNG NGUYÊN TỐ

from math import *
def nt(n):
    if n < 2: return False
    for i in range(2 , isqrt(n) + 1):
        if n % i == 0: return False
    return True

t = int(input())
for i in range(t):
    a , b = [int(i) for i in input().split()]
    g = gcd(a , b)
    sum = 0
    while g != 0:
        sum += (g % 10)
        g //= 10
    print('YES' if nt(sum) else 'NO')

