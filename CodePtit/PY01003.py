## LÀM TRÒN SỐ

t = int(input())
for _ in range(t):
    a = list(int(i) for i in input())
    for i in range(len(a) - 1, 0, -1):
        if a[i] >= 5:
            a[i - 1] = a[i - 1] + 1
        a[i] = 0
    for i in a:
        print(i , end='')
    print()