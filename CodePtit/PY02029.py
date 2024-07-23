n , m = map(int , input().split())
a = [int(i) for i in input().split()]
b = dict({})
for i in a:
    if i not in b:
        b[i] = 1
    else: b[i] += 1
Max = max(b.values())
Max1 = 0
for i in b.values():
    if Max1 < i < Max:
        Max1 = i
if Max1 == 0:
    print('NONE')
else:
    for i in range(1 , m + 1):
        if b[i] == Max1:
            print(i)
            break