## SẮP XẾP DÃY SỐ

t = int(input())
for _ in range(t):
    n , m = map(int , input().split())
    a = list(map(int , input().split()))
    Max = max(a)
    for i in range(n):
        if a[i] == Max:
            a.insert(i, m)
            break
    for i in a:
        if i < 0:
            print(i, end=" ")
    for i in a:
        if i >= 0:
            print(i, end=" ")
    print()