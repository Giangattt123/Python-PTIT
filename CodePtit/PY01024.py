## CHẴN LẺ

from math import *

def sumDigit(n):
    Sum = 0
    while n != 0:
        Sum += n % 10
        n //= 10
    if Sum % 10 == 0: return True
    return False

def check(s):
    for i in range(1 , len(s)):
        if abs(int(s[i]) - int(s[i - 1])) != 2:
            return False
    return True

t = int(input())
for i in range(t):
    s = input()
    sNum = int(s)
    if sumDigit(sNum) and check(s): print('YES')
    else: print('NO')
