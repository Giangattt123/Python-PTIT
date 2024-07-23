## SỐ THUẬN NGHỊCH LỚN NHẤT TRONG MA TRẬN

def res(n):
    s=str(n)
    return s==s[::-1]

n,m=map(int,input().split())
a=[]
for i in range(n):
    a.append([int(i) for i in input().split()])
maxa=-10**9
for i in a:
    for j in i:
        if j>=10 and res(j):
            maxa=max(maxa,j)
if maxa==-10**9:
    print("NOT FOUND")
else:
    print(maxa)
    for i in range(n):
        for j in range(m):
            if a[i][j]==maxa:
                print(f"Vi tri [{i}][{j}]")