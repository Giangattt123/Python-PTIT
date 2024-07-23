## TÌM SỐ NHỎ NHẤT

import sys
t = int(input())
for _ in range(t):
    s = input()
    ans = sys.maxsize
    _sum = 0
    for char in s:
        if char.isalpha():
            if _sum != 0:
                ans = min(ans, _sum)
            _sum = 0
        else:
            _sum = _sum * 10 + int(char)
    if _sum != 0:
        ans = min(ans, _sum)
    print(ans)
