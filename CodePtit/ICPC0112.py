## PRIME – TRIPLET

# # Code TLE
# from math import *
# def nt(n):
#     if n < 2:
#         return False
#     for i in range(2 , isqrt(n) + 1):
#         if n % i == 0:
#             return False
#     return True
#
# if __name__ == '__main__':
#     t = int(input())
#     for i in range(t):
#         n = int(input())
#         cnt = 0
#         for j in range(2 , n - 6):
#             if nt(j) and nt(j + 2) and nt(j + 6):
#                 cnt += 1
#             if nt(j) and nt(j + 4) and nt(j + 6):
#                 cnt += 1
#         print(cnt)

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
    cnt = 0
    for j in range(2,n-6):
        if (sieve[j] and sieve[j + 2] and sieve[j + 6]) or (sieve[j] and sieve[j + 4] and sieve[j + 6]):
            cnt += 1
    print(cnt)





