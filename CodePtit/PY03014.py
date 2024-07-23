## BIỂU THỨC
"""
Input: (a + (b * c) ) + (d/e)
Output: 1 2 2 1 3 3

2
(a + (b *c) ) + (d/e)
( ( () ) ( () ) )
1  2  2  1  3  3
1  2  3  3  2  4  5  5  4  1
"""

t = int(input())
for _ in range(t):
    s = input()
    a = []
    value = 0
    for i in s:
        if i == '(':
            value += 1
            a.append(value)
            print(value , end = " ")
        elif i == ')':
            print(a[-1] , end = " ")
            a.pop()
    print()