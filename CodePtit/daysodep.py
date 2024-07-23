from math import *
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int , input().split()))
    count = 0
    for i in range(n - 1):
        minValue = min(a[i] , a[i + 1])
        maxValue = max(a[i] , a[i + 1])
        while minValue * 2 < maxValue:
            count = count + 1
            minValue *= 2
    print(count)
