## ĐỒ THỊ HÌNH SAO

n = int(input())
a = [[] for _ in range(n)]

for i in range(1, n):
    x, y = map(int, input().split())
    a[x - 1].append(y - 1)
    a[y - 1].append(x - 1)

check = 0
for i in a:
    if len(i) == n - 1:
        check = 1
        break

print('Yes' if check == 1 else 'No')