## ƯU THẾ NGUYÊN TỐ

from math import *
def check(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True


for _ in range(int(input())):
    s = input()
    l, count = len(s), 0
    for i in s:
        if check(int(i)):
            count += 1
    print('YES' if check(l) and count > l - count else 'NO')