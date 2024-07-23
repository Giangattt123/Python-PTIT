## XOAY MẢNG

t = int(input())
for i in range(t):
    n , d = input().split()
    n = int(n)
    d = int(d)
    a = list(map(int , input().split()))
    for j in range(d , n):
        print(a[j] , end=" ")
    for k in range(0 , d):
        print(a[k] , end=" ")
    print()