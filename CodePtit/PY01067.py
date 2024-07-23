## SỐ 2 ƯU THẾ

from math import *
from queue import Queue

def check(n):
    s = str(n)
    count2 = s.count('2')
    return count2 * 2 > len(s)

a = []
q = Queue()
q.put(1)
q.put(2)
while True:
    first = q.get()
    if check(first):
        a.append(first)
        if len(a) > 1000: break
    q.put(first * 10 + 0)
    q.put(first * 10 + 1)
    q.put(first * 10 + 2)

t = int(input())
for _ in range(t):
    n = int(input())
    for i in range(n):
        print(a[i] , end = " ")
    print()