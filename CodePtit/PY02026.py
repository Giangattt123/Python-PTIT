## TẬP HỢP SỐ BẰNG NHAU

n , m  = map(int , input().split())
a = sorted(list(set([int(i) for i in input().split()])))
b = sorted(list(set([int(i) for i in input().split()])))
check = True
if len(a) == len(b):
    for i in a:
        if i not in b:
            check = False
            break
    print("YES" if check else "NO")
else: print("NO")