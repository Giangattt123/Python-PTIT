class ToaDo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
t = int(input())
for _ in range(t):
    n = int(input())
    a = []
    for i in range(n):
        x, y = map(int , input().split())
        a.append(ToaDo(x, y))
    a = sorted(a, key = lambda tmp : tmp.y , reverse=False)
    cnt, tmp = 1, a[0].y
    for i in range(1, n):
        if a[i].x >= tmp:
            cnt += 1
            tmp = a[i].y
    print(cnt)