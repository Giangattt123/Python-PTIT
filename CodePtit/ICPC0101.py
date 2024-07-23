## THU GỌN DÃY SỐ

n = int(input())
s = input().split()
a = [int(num) for num in s]
i = 1
while i < len(a):
    if (a[i] + a[i-1]) % 2 == 0:
        del a[i]
        del a[i-1]
        if i > 1: i = i - 1
    else: i = i + 1
print(len(a))
