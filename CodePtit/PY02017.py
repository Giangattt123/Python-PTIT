## TẤN SUẤT LẺ

t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    ans = 0
    for value in a:
        ans ^= value
        print(ans , end = " ")
    print(ans)