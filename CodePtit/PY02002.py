## LIỆT SỐ FIBONACCI

F = [0] * 93
F[0] = 0
F[1] = F[2] = 1
def fibo():
    for i in range(3 , 93):
        F[i] = F[i - 1] + F[i - 2]

t = int(input())
fibo()
for _ in range(t):
    a , b = map(int , input().split())
    for i in range(a , b + 1):
        print(F[i]  , end = " ")
    print()
