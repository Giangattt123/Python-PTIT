## SỐ NGUYÊN TỐ LỚN NHẤT TRONG MA TRẬN

from math import sqrt

def nto(n):
    end=int(sqrt(n))
    for i in range(2,end+1):
        if n%i==0:
            return False
    return n>1

n,m=map(int,input().split())
a=[]
for i in range(n):
    a.append([int(i) for i in input().split()])
maxa=-10**9
for i in a:
    for j in i:
        if nto(j):
            maxa=max(maxa,j)
if maxa==-10**9:
    print("NOT FOUND")
else:
    print(maxa)
    for i in range(n):
        for j in range(m):
            if a[i][j]==maxa:
                print(f"Vi tri [{i}][{j}]")