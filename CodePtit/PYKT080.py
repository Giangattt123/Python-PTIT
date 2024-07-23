## THỐNG KÊ DỊCH TỄ

dx = [-1 , -1 , -1 , 0  , 0 , 1 , 1 , 1]
dy = [-1 , 0 , 1 , -1 , 1 , -1 , 0 , 1]
m , n = map(int , input().split())
check = [[False] * n for _ in range(m)]
a = []
sum = 0
for _ in range(m):
    a.append([int(i) for i in input().split()])

def is_valid(x , y):
    return 0 <= x < m and 0 <= y < n

for i in range(m):
    for j in range(n):
        if a[i][j] == -1:
            for k in range(8):
                idx = i + dx[k]
                jdy = j + dy[k]
                if is_valid(idx, jdy)  and not check[idx][jdy]:
                    sum += a[idx][jdy]
                    check[idx][jdy] = True
print(sum)

