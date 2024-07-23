## THỐNG KÊ TỪ KHÁC NHAU THEO NGƯỠNG K

t , k = [int(i) for i in input().split()]
s = ""
for _ in range(t):
    s += input().lower() + " "
for i in s:
    if not i.isalnum():
        s = ' '.join(s.split(i))
a = s.split()
b = dict({})
for i in a:
    b[i] = a.count(i)
c = sorted(b.items() , key = lambda x : (-x[1] , x[0]) , reverse = False)
for key , value in c:
    if value >= k:
        print(key , value)
