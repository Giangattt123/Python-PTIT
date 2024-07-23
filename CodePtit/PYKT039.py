## DÃY SỐ PHÙ HỢP

def check(s , v):
    for i in range(len(s)):
        if s[i] > v[i]: return False
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    a.sort()
    b.sort()
    print('YES' if check(a , b) else 'NO')