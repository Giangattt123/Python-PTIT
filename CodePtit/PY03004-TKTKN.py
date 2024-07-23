## THỐNG KÊ TỪ KHÁC NHAU
import re
from collections import Counter
def solve(s : str):
    s = s.lower()
    # string = re.sub(r'[^\w\s]', '' , s)
    # listString : list[str] = string.split()
    listString = re.findall(r'\b\w+\b', s)
    stringCounter = Counter(listString)
    stringCounterSort = sorted(stringCounter.items() , key=lambda x : (-x[1] , x[0]))
    for key , value in stringCounterSort:
        print(key , value)

n = int(input())
s = ""
for i in range(n):
    s += input() + " "
solve(s)

s = ''
for t in range (int(input())):
    s += input().lower() + " "
print(s)
for i in s:
    if not i.isalnum():
        s = ' '.join(s.split(i))
a = s.split()
b = {}
for i in a:
    b[i] = a.count(i)
c = sorted(b.items(), key = lambda x: (-x[1], x[0]))
for i in c:
    print(i[0] + " " + str(i[1]))