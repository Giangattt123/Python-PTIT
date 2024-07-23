# ## SUM TRIPLE ZERO
## Code bị WA
# def countTripleZero(a, n):
#     cnt = 0
#     checked = False
#     for i in range(n - 1):
#         s = set()
#         for j in range(i + 1, n):
#             x = -(a[i] + a[j])
#             if x in s:
#                 cnt += 1
#                 checked = True
#             else:
#                 s.add(a[j])
#     if checked: return cnt
#     return 0
#
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     a = list(map(int, input().split()))
#     res = countTripleZero(a, n)
#     print(res)


t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    cnt = 0
    for i in range(0, n - 2):
        l = i + 1
        r = len(a) - 1
        x = a[i]
        while l < r:
            if x + a[l] + a[r] == 0:
                cnt += 1
                l += 1
            elif x + a[l] + a[r] < 0:
                l += 1
            else:
                r -= 1
    print(cnt)

