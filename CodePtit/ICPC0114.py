## PERFECT PRIME

import math
def nt(n):
    if n < 2: return False
    for i in range(2 , int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True

def check(s):
    for i in s:
        if not nt(int(i)): return 'No'
    total = sum([int(i) for i in s])
    sRev = s[::-1]
    if not nt(int(s)) or not nt(int(sRev)) or not nt(int(total)):
        return 'No'
    return 'Yes'
for i in range(int(input())):
    n = input()
    print(check(n))
