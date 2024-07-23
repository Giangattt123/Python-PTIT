## MA TRẬN - 1

from math import *

n = int(input())
a = [[0 for i in range(n)] for _ in range(n)]
print(a)
for i in range(n):
    a[i] = list(map(int, input().split()))
k = int(input())
sumTop , sumBottom = 0 , 0
for i in range(n):
    for j in range(i + 1, n):
        sumTop += a[j][i]
        sumBottom += a[i][j]
quantity = abs(sumTop - sumBottom)
print('YES' if quantity <= k else 'NO')
print(quantity)