## PHÂN TÍCH THỪA SỐ NGUYÊN TỐ

from math import  *
t = int(input())
for i in range(t):
    n = int(input())
    ans = "1"
    for j in range(2 , isqrt(n) + 1):
        somu = 0
        if n % j == 0:
            while n % j == 0:
                somu += 1
                n /= j
        if somu != 0: ans += " * " +  str(j) + "^" + str(somu)
    if n != 1: ans += " * " + str(int(n)) + "^1"
    print(ans)


