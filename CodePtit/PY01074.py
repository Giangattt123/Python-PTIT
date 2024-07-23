## TỔNG ƯỚC SỐ

from math import *
maxSize = 2000001
prime = [1] * maxSize
prime[0] = prime[1] = 0
i = 2

while i <= isqrt(maxSize):
    if prime[i] == 1:
        for j in range(i * i , maxSize , i):
            if prime[j] == 1: prime[j] = i
    i += 1

for k in range(2 , maxSize):
    if prime[k] == 1: prime[k] = k

t = int(input())
ans = 0
for _ in range(t):
    n = int(input())
    while n >= 2:
        ans += prime[n]
        n //= prime[n]
print(ans)