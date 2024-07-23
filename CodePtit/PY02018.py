## Số nhỏ nhất còn thiếu

n = int(input())
a = list(map(int , input().split()))
mark = [0] * 30001
for x in a:
    mark[x] = 1
checked = 0
for x in range(min(a) , max(a)):
    if mark[x] == 0:
        checked = 1
        print(x)
        break
if checked == 0:
    print(max(a) + 1)

