## ĐẾM CẶP ĐỒNG XU

## nC2
def solve(n):
    return (n * (n-1)) // 2

n = int(input())
ans = 0
a = []
for i in range(n):
    a.append(input())

for i in range(n):
    count = 0
    for j in range(n):
        if a[i][j] == 'C': count += 1
    ans += solve(count)

for i in range(n):
    count = 0
    for j in range(n):
        if a[j][i] == 'C': count += 1
    ans += solve(count)
print(ans)