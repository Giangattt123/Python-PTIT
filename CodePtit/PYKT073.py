## XÁC ĐỊNH THỂ LOẠI THƠ

n = int(input())
a = []
for i in range(n):
    a.append(len(input().split()))
print(a)
b = []
j = 0
while j < len(a):
    if a[j] == 6:
        b.append(1)
        while j < len(a) and (a[j] == 6 or a[j] == 8):
            j += 1
    elif a[j] == 7:
        b.append(2)
        j += 4
    else: j += 1
print(len(b))
for _ in b:
    print(_)
