## TÍNH TOÁN LƯỢNG MƯA

def timer(h1 , h2):
    return h2[0] * 60 + h2[1] - (h1[0] * 60 + h1[1])

a = dict({})
n = int(input())
for i in range(n):
    name = input()
    start = [int(i) for i in input().split(':')]
    end = [int(i) for i in input().split(':')]
    count = int(input())
    if name in a:
        a[name] = (a[name][0] + timer(start , end) , a[name][1] + count)
    else:
        a[name] = (timer(start , end) , count)

t = 1
for i in a:
    print('T{:02d}'.format(t), i, "{:.2f}".format(a[i][1] * 60 / a[i][0]))
    t += 1

