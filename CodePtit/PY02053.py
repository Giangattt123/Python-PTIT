## TÍNH CÂN ĐỐI CỦA MA TRẬN - 2

from math import *

n = int(input())
a = [[0 for i in range(n)] for _ in range(n)]
for i in range(n):
    a[i] = list(map(int, input().split()))
k = int(input())
sumTop , sumBottom = 0 , 0
for i in range(n):
    for j in range(n):
        if i + j < n - 1: sumTop += a[i][j]
        if i + j >= n: sumBottom += a[i][j]
quantity = abs(sumTop - sumBottom)
print('YES' if quantity <= k else 'NO')
print(quantity)