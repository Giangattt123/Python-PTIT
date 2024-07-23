## ĐOẠN LIÊN TIẾP NHỎ HƠN

# code TLE time > 2.0s O(n^2)
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     a = list(map(int , input().split()))
#     for i in range(n):
#         cnt = 0
#         for j in range(i + 1):
#             if a[j] < a[i]:
#                 cnt += 1
#             elif a[j] == a[i] and j == i: cnt += 1
#         print(cnt , end = " ")
#     print()

# Code AC , Timecomplexity: O(N)
def ans(a):
    l = len(a)
    cnt = [1] * l
    for i in range(1 , l):
        j = i - 1
        while j >= 0 and a[j] <= a[i]:
            cnt[i] += cnt[j]
            j -= cnt[j]
    return cnt

t  = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int , input().split()))
    res = " ".join(map(str , ans(a)))
    print(res)