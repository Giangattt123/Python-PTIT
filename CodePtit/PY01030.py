## NGUYÊN TỐ CÙNG NHAU

from math import *

n , k = map(int , input().split())
Min, Max = 10**(k - 1) , 10**k
dem = 0
for i in range(Min , Max):
    if gcd(i , n) == 1:
        print(i , end = " ")
        dem += 1
    if dem % 10 == 0: print()