## BÀI TOÁN ĐẾM

n = int(input())
a , m , s , check = [] , {} , 0 , 0
while len(a) < n:
    x = [int(x) for x in input().split()]
    a += x
for i in a:
    m[i] = 1
    s = max(s, i)
for i in range(1, s + 1):
    if not (i in m):
        print(i)
        check = 1
if check == 0: print('Excellent!')