## NGUYÊN TỐ

from math import *

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, isqrt(num) + 1):
        if num % i == 0:
            return False
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    k = 0
    for i in range(1, n):
        if gcd(i, n) == 1:
            k += 1
    print('YES' if is_prime(k) else 'NO')
