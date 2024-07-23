## CHIA HẾT CHO K

a , K , N = map(int , input().split())
b = K - a % K
check = 0
for i in range(a + b , N + 1 , K):
    print(i - a , end = " ")
    check = 1
if not check: print("-1")
