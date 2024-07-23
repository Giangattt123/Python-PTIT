## ĐỔI CƠ SỐ

s = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
t = int(input())
for _ in range(t):
    n, b = [int(i) for i in input().split()]
    ans = ""
    while n:
        ans += s[n % b]
        n //= b
    print(ans[::-1])