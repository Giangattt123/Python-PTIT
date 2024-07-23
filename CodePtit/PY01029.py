## SỐ ĐẢO NGUYÊN TỐ CÙNG NHAU
from math import *

t = int(input())
for i in range(t):
    s = input()
    sRev = s[::-1]
    print('YES' if gcd(int(s) , int(sRev)) == 1 else 'NO')