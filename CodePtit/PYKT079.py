## ĐIỀN SỐ

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int , input().split()))
    dd = [0] * 1000
    cnt = []
    for i in a:
        dd[i] = 1
    for i in range(min(a) , max(a) + 1):
        if dd[i] == 0:
            cnt.append(i)
    print(len(cnt))
