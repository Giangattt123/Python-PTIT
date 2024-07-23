## BIẾN ĐỔI DÃY SỐ

while True:
    a = list(map(int , input().split()))
    if a == [0 , 0 , 0 , 0]: break
    count = 0
    while len(set(a)) > 1:
        b = []
        for i in range(3):
            b.append(abs(a[i] - a[i + 1]))
        b.append(abs(a[3] - a[0]))
        a = b
        count += 1
    print(count)