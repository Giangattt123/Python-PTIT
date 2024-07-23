## LÃI SUẤT NGÂN HÀNG

from math import *

t = int(input())
for i in range(t):
    N, X, M = map(float, input().split())
    ans = log(M / N, 1 + X / 100)
    print(ceil(ans))
    