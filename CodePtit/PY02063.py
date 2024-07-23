n = input()
a = list(map(int , input().split()))
a = sorted(a)
print(max(a[0]*a[1],a[-1]*a[-2],a[0]*a[1]*a[2],a[-1]*a[-2]*a[-3],a[0]*a[1]*a[-1],a[-1]*a[-2]*a[0]))
