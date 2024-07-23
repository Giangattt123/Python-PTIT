## EMIRP NUMBER

from math import *
maxSieve = int(1e6+1)
sieve = [1] * maxSieve
sieve[0] = sieve[1] = 0
for i in range(isqrt(maxSieve) + 1):
    if sieve[i]:
        for j in range(i*i , maxSieve , i):
            sieve[j] = 0

t = int(input())
for i in range(t):
    n = int(input())
    checked = set()
    for j in range(13 , n):
        num = int(str(j)[::-1])
        if sieve[j] and sieve[num] and j != num and num < n and (j, num) not in checked and (
        num, j) not in checked:
            print(j, num, end=" ")
            checked.add((j, num))
    print()


