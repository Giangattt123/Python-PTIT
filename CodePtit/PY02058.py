## SỐ ĐẸP TRONG MA TRẬN

# Code WA
# n , m = map(int , input().split())
# a = [[0]] * n
# Min , Max = 10e18 , -10e18
# for i in range(n):
#     a[i] = [int(value) for value in input().split()]
#     Min = min(Min , min(a[i]))
#     Max = max(Max , max(a[i]))
#
# distance = Max - Min
# print(distance)
# check = 0
# for i in range(n):
#     for j in range(m):
#         if a[i][j] == distance:
#             check = 1
#             print("Vi tri [" + str(i) + "]" + "[" + str(j) + "]")
# if not check: print("NOT FOUND")

## Code AC
n, m = [int(x) for x in input().split()]
a = [[0] * m for _ in range(n)]
Max, Min, ok = 0, 10**6, 0

for i in range(n):
    a[i] = [int(x) for x in input().split()]
    Max = max(Max, max(a[i]))
    Min = min(Min, min(a[i]))

for i in range(n):
    for j in range(m):
        if a[i][j] == Max - Min:
            if ok == 0:
                print(Max - Min)
                ok = 1
            print('Vi tri [', i, '][', j, ']', sep='')
if ok == 0:
    print('NOT FOUND')

