## KIỂM TRA NGUYÊN TỐ

from math import *


def check(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

for _ in range(int(input())):
    s = input()
    n = int(s[-4:])
    print('YES' if check(n) else 'NO')