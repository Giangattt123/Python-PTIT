## KIỂM TRA CHIA HẾT CHO 7

def checkSeven(n):
    for i in range(1000):
        if n % 7 == 0: return n
        nRev = int(str(n)[::-1])
        n += nRev
    return -1

t = int(input())
for j in range(t):
    n = int(input())
    print(checkSeven(n))
