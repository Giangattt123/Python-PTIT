## SẮP XẾP THEO TỔNG CHỮ SỐ

def sumDigit(n):
    tong = 0
    while n != 0:
        tong += n % 10
        n //= 10
    return tong

t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int , input().split()))
    a.sort(key = lambda x : (sumDigit(x) , x))
    print(" ".join(map(str , a)))