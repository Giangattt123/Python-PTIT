## BIẾN ĐỔI VỀ NGUYÊN TỐ

from math import *
def checkNT(n):
    if n < 2: return False
    for i in range(2 , isqrt(n) + 1):
        if n % i == 0: return False
    return True

n = int(input())
a = list(map(int , input().split()))
ans = 0
for i in a:
    tmp = i
    while not checkNT(tmp):
        tmp += 1
    cnt = tmp - i
    tmp = i
    while not checkNT(tmp):
        tmp -= 1
    cnt = min(cnt , i - tmp)
    print(cnt , end = " ")
    ans = max(ans , cnt)
print(ans)
