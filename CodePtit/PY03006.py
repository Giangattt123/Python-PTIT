## THỐNG KÊ TỪ KHÁC NHAU KHÔNG CHỨA CHỮ SỐ

def checkDigit(s):
    n = ''
    for i in s:
        if not i.isdigit():
            n += i
    return n

s = ''
for t in range (int(input())):
    s += input().lower() + " "

s = checkDigit(s)
for i in s:
    if not i.isalnum():
        s = ' '.join(s.split(i))

a = s.split()
b = {}
for i in a:
    b[i] = a.count(i)
c = sorted(b.items(), key = lambda x: (-x[1], x[0]))
for i in c:
    print(*i)