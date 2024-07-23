## DÃY SỐ HAMMING

a = []
dic = dict({})
def binarySearch(left , right, value):
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == value: return mid + 1
        elif a[mid] < value: left = mid + 1
        else: right = mid - 1
    return -1

for i in range(60):
    for j in range(40):
        for k in range(30):
            value = (2**i)*(3**j)*(5**k)
            if value not in dic:
                dic[value] = 1
                a.append(value)
a.sort()
t = int(input())
for i in range(t):
    n = int(input())
    index = binarySearch(0 , len(a) , n)
    if index != -1: print(index)
    else: print('Not in sequence')