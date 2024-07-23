## SỐ NGUYÊN TỐ TRONG MA TRẬN

from math import *
def nt(n):
    if n < 2: return False
    for i in range(2 , isqrt(n) + 1):
        if n % i == 0: return False
    return True

n , m = map(int , input().split())
a = [[0]] * n
for i in range(n):
    a[i] = [int(value) for value in input().split()]

Max = -10e18
for i in range(n):
    for j in range(m):
        if nt(a[i][j]) and a[i][j] > Max: Max = a[i][j]
if Max == -10e18: print("NOT FOUND")
else:
    print(Max)
    for i in range(n):
        for j in range(m):
            if a[i][j] == Max: print('Vi tri [', i, '][', j, ']', sep='')
