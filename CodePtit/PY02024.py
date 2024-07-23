## SẮP XẾP THEO TÍCH CHỮ SỐ
from functools import cmp_to_key

def tich(n):
    res = 1
    while n != 0:
        res *= n % 10
        n //= 10
    return res

def cmp(a , b):
    tich1 , tich2 = tich(a) , tich(b)
    if tich1 != tich2:
        return tich1 - tich2
    else:
        return a - b

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int , input().split()))
    a.sort(key=cmp_to_key(cmp))
    print(" ".join(map(str , a)))
