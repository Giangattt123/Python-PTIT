## XUẤT HIỆN NHIỀU LẦN NHẤT

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int , input().split()))
    dic = dict([])
    for i in a:
        if i in dic: dic[i] += 1
        else: dic[i] = 1
    max_freq = max(dic.values())
    if max_freq > n // 2:
        ans = min(key for key, value in dic.items() if value == max_freq)
        print(ans)
    else: print('NO')
