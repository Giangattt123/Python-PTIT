## DÃY SỐ PHÙ HỢP

def check(a , b):
    a.sort()
    b.sort()
    for i in range(len(a)):
        if a[i] > b[i]: return False
    return True

t = int(input())
for _ in range(t):
    n = input()
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print('YES' if check(a , b) else 'NO')