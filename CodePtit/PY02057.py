## SỐ MAY MẮN TRONG MA TRẬN

n , m = map(int , input().split())
a = [[]] * n
Max , Min = -10000 , 10000
for i in range(n):
    a[i] = [int(j) for j in input().split()]
    Max = max(Max , max(a[i]))
    Min = min(Min , min(a[i]))
distance = Max - Min
check = False
for i in range(n):
    for j in range(m):
        if a[i][j] == distance:
            check = True
if not check:
    print('NOT FOUND')
else:
    print(distance)
    for i in range(n):
        for j in range(m):
            if a[i][j] == distance:
                print('Vi tri [' + str(i) + ']' + '[' + str(j) + ']')

