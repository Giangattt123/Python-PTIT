## TÁCH ĐÔI VÀ TÍNH TỔNG

n = int(input())
while n >= 10:
    s = str(n)
    l = len(s)
    n = int(s[:l//2]) + int(s[l//2:])
    print(n)