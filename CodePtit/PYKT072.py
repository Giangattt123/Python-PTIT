## XOAY VÒNG XÂU KÍ TỰ

def rotate(s):
    return s[1:]+s[0]

n = int(input())
a = []
for i in range(n):
    a.append(input())
ans = 10**9
for i in range(n):
    cnt1 = 0
    for j in range(n):
        if i != j:
            s = a[j]
            cnt2 = 0
            while s != a[i] and cnt2 < len(a[i]):
                s = rotate(s)
                cnt2 += 1
            if s != a[i]:
                ans = -1
                break
            cnt1 += cnt2
    if ans == -1:
        break
    ans = min(ans, cnt1)
print(ans)