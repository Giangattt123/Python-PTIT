## ĐẾM CẶP ĐỒNG XU

from math import *

n = int(input())
a = []
cnt = 0
for i in range(n):
    b = list(input())
    a.append(b)
for i in range(n):
    hang = 0
    for j in range(n):
        if a[i][j] == 'C':
            hang += 1
    cnt += comb(hang, 2)
for i in range(n):
    cot = 0
    for j in range(n):
        if a[j][i] == 'C':
            cot += 1
    cnt += comb(cot, 2)
print(cnt)