## TÍNH TÍCH CHẬP CỦA MA TRẬN
### => 2D Convolution(Phép tích chập)

t = int(input())
for _ in range(t):
    n , m = map(int , input().split())
    x = [[]] * n
    h = [[]] * 3
    res = [[] for _ in range(n - 2)]
    s = 0
    for i in range(m):
        x[i] = [int(j) for j in input().split()]
    for i in range(3):
        h[i] = [int(j) for j in input().split()]
    for i in range(n - 2):
        for j in range(m - 2):
            total = 0
            for k in range(3):
                for l in range(3):
                    total += x[i + k][j + l] * h[k][l]
            res[i].append(total)
    print(res)
    print(sum([sum(row) for row in res]))




