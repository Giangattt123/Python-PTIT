t = int(input())
for _ in range(t) :
    n = int(input())
    a, b, f, ans = [0] * n, [0] * n, [1] * n, 1
    for i in range(n) :
        a[i], b[i] = [float(x) for x in input().split()]
    for i in range(n) :
        for j in range(0, i) :
            if a[i] > a[j] and b[i] < b[j] :
                f[i] = max(f[i], f[j] + 1)
        ans = max(ans, f[i])
    print(ans)