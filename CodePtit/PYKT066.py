## DÃY CON NGẮN NHẤT

import math
from sys import *

from math import *

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    # a = [int(i) for i in input().split()]
    a = []
    while len(a) < n:
        x = [int(i) for i in input().split()]
        a += x
    cnt = n + 1
    for i in range(n):
        ucln = a[i]
        for j in range(i, n):
            ucln = gcd(ucln, a[j])
            if ucln == k:
                cnt = min(cnt, j - i + 1)
                break
            if ucln < k:
                break
    if cnt == n + 1:
        print(-1)
    else:
        print(cnt)