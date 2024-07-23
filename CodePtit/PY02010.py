## LỚN NHẤT VÀ NHỎ NHẤT

import sys

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    a = []
    for i in range(n):
        a.append(int(sys.stdin.readline()))
    Min = min(a)
    Max = max(a)
    if Min == Max:
        print("BANG NHAU")
    else:
        print(Min, Max)