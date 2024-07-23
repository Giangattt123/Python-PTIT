## ĐẦU CUỐI

t = int(input())
for _ in range(t):
    s = input()
    res1 = s[:2]
    res2 = s[-2:]
    print('YES' if res1 == res2 else 'NO')