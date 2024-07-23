## BIẾN ĐỔI VỀ DÃY BẰNG NHAU

n = int(input())
a = [int(i) for i in input().split()]
ans = 10**9
value = 0
for i in range(n):
    cnt = 0
    for j in range(n):
        cnt += abs(a[i]-a[j])
    if ans > cnt:
        ans = cnt
        value = a[i]
print(ans, value)