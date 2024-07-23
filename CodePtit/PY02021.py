## DÃY CON CHUNG CỦA BA DÃY SỐ

t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    c = [int(i) for i in input().split()]
    d = []
    x , y , z = 0 , 0 , 0
    while x < n and y < m and z < k:
        if a[x] == b[y] and b[y] == c[z]:
            d.append(a[x])
            x += 1
            y += 1
            z += 1
        elif a[x] < b[y]:
            x += 1
        elif b[y] < c[z]:
            y += 1
        else: z += 1
    if len(d) == 0: print("NO")
    else:
        for i in d:
            print(i, end=" ")
        print()
