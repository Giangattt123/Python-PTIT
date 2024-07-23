## SỐ THUẬN NGHỊCH TRONG MA TRẬN

def check(s):
    if len(s) < 2: return False
    return s == s[::-1]

n , m = map(int , input().split())
a = []
Max = -10**9

for _ in range(n):
    a.append([int(i) for i in input().split()])
for i in range(n):
    for j in range(m):
        if check(str(a[i][j])):
            Max = max(Max , a[i][j])

if Max==-10**9:
    print("NOT FOUND")
else:
    print(Max)
    for i in range(n):
        for j in range(m):
            if a[i][j] == Max:
                print(f'Vi tri [{i}][{j}]')



