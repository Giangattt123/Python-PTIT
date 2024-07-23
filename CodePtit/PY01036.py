## TÍNH TỔNG PHÂN THỨC

t = int(input())
for i in range(t):
    n = int(input())
    ans = 0.0
    if n & 1 == 1:
        for j in range(1, n + 1, 2):
            ans += 1.0 / j
    else:
        for j in range(2, n + 1, 2):
            ans += 1.0 / j
    print("{:.6f}".format(ans))